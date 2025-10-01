import cpp

predicate isRegistrationFieldAccess(FieldAccess fieldAccess) {
    exists( AssignExpr assign, FunctionAccess funcAccess| 
        assign.getLValue() = fieldAccess and
        assign.getRValue() = funcAccess
    ) or
    exists( ClassAggregateLiteral aggregateLiteral | 
        aggregateLiteral.getAChild() = fieldAccess
    )
}

Function getRegistrationFunctionFromFieldAccess(FieldAccess fieldAccess) {
    exists( AssignExpr assign, FunctionAccess funcAccess| 
        assign.getLValue() = fieldAccess and
        assign.getRValue() = funcAccess and 
        result = funcAccess.getTarget()
    ) 
}

Function getRegistrationFunctionFromAggregateLiteral(ClassAggregateLiteral aggregateLiteral) {
    exists( FunctionAccess funcAccess | 
        aggregateLiteral.getAChild() = funcAccess and
        result = funcAccess.getTarget()
    )
}

Function getRegisteredFunction(FieldAccess fieldAccess){
    fieldAccess.getType() instanceof FunctionPointerType and
    exists( FieldAccess fieldAccess2 | 
        isRegistrationFieldAccess(fieldAccess2) and
        fieldAccess2.getTarget() = fieldAccess.getTarget() and
        fieldAccess2 != fieldAccess and 
        result = getRegistrationFunctionFromFieldAccess(fieldAccess2)
    ) or
    exists( ClassAggregateLiteral aggregateLiteral |
        aggregateLiteral.getAChild() = fieldAccess and
        result = getRegistrationFunctionFromAggregateLiteral(aggregateLiteral)
    )
}
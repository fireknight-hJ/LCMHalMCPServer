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

Function getRegistrationFunctionFromAggregateLiteral(Field field) {
    exists( FunctionAccess funcAccess, ClassAggregateLiteral agg, int position, Expr e| 
        // fieldExpr.getNumChild()
        agg.getFieldExpr(field, position) = e and   
        agg.getChild(position) = funcAccess and
        // = funcAccess and
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
    exists( ClassAggregateLiteral aggregateLiteral, Expr fieldExpr|
        fieldExpr = aggregateLiteral.getAFieldExpr(fieldAccess.getTarget()) and
        result = getRegistrationFunctionFromAggregateLiteral(fieldAccess.getTarget())
    )
}

from VariableCall call, FieldAccess fieldAccess
where call.getExpr() = fieldAccess
select fieldAccess, getRegisteredFunction(fieldAccess).getName(), call.getFile().getAbsolutePath(), call.getLocation().getStartLine(), call.getEnclosingFunction().getName(), getRegisteredFunction(fieldAccess).getFile().getAbsolutePath(), getRegisteredFunction(fieldAccess).getLocation().getStartLine()
import cpp

from FunctionAccess funcaccess, AssignExpr assign, FieldAccess fieldaccess
where
    // lock the Function Registration Operation
    assign.getLValue() = fieldaccess and
    not assign.getRValue() = funcaccess and
    not assign.getRValue().isConstant() and
    fieldaccess.getTarget().getType() instanceof FunctionPointerType
    // Trace the Operation function
    
select assign, assign.getRValue(), fieldaccess.getTarget(), assign.getEnclosingFunction()
import cpp

from Function func, FunctionCall call
where
    call.getTarget() = func and
    func.getName() = "HAL_IncTick"
select call.getEnclosingFunction()
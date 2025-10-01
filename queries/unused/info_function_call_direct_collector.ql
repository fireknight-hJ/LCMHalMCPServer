import cpp

from FunctionCall call

select call.toString(), call.getTarget().toString(), call.getEnclosingFunction().getName(), call.getFile().getAbsolutePath(), call.getLocation().getStartLine(), call.getTarget().getFile().getAbsolutePath(), call.getTarget().getLocation().getStartLine()
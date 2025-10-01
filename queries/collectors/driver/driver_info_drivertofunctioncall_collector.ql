import cpp
import DriverLocator

from DriverToCall call
select call.toString2(), call.getTargetFunction().toString(), call.getEnclosingFunction().getName(), call.getFile().getAbsolutePath().toString(), call.getLocation().getStartLine(), call.isDirectCall()
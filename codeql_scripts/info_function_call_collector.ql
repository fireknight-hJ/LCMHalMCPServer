import cpp
import DriverLocator

from AllCall call
// where call.toString() = "call to netif_is_link_up"
select call.getEnclosingFunction().getName(), call.getTargetFunction().toString(), call.toString2(), call.getFile().getAbsolutePath().toString(), call.getLocation().getStartLine(), call.isDirectCall(), call.checkHasReturnValue()
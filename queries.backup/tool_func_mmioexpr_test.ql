import cpp
import libraries.MMIOAnalyzer

from InterestingMMIOExpr e
where e.getEnclosingFunction().getName() = "RESET_SetPeripheralReset"
select e
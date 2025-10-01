import cpp
import libraries.DriverLocator

from DriverFromFunction func, InterestingMMIOExpr expr
where expr.getEnclosingFunction() = func
select expr
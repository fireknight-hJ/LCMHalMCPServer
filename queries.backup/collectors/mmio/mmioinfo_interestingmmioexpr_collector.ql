import cpp
import libraries.MMIOAnalyzer

from
    Function func,
    InterestingMMIOExpr expr
where
    isInterestingMMIOFunction(func) and
    expr.getEnclosingFunction() = func 
// select func, expr, 
select expr.toString(), expr.getEnclosingFunction().getName(), expr.getFile().getAbsolutePath().toString(), expr.getLocation().getStartLine(), expr.checkExprType(), expr.checkEnclosingType()
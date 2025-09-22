import cpp
import MMIOAnalyzer

from
    Function func,
    MMIOTracedExpr expr
where
    expr.getEnclosingFunction() = func and
    isInterestingMMIOFunction(func)
select expr.toString(), expr.getEnclosingFunction().getName(), expr.getFile().getAbsolutePath().toString(), expr.getLocation().getStartLine(), expr.checkExprType(), expr.checkEnclosingType()
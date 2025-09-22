import cpp
import MMIOAnalyzer

from
    Function func,
    InterestingMMIOExpr expr
where
    expr.getEnclosingFunction() = func and
    func.getName() = "ENET_GetRxFrame"
    // isInterestingMMIOFunction(func)
select expr, expr.getType()
// select expr, expr.getEnclosingFunction(), expr.checkExprType(), expr.checkEnclosingType()

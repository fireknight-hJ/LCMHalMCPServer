import cpp
// import DriverLocator
import MMIOAnalyzer

predicate isInterestingMMIOBranchExpr(Expr expr) {
    expr instanceof MMIOTracedExpr and
    (
        expr.getEnclosingElement() instanceof IfStmt or
        expr.getEnclosingElement() instanceof WhileStmt and
        expr.getEnclosingFunction() instanceof DriverFunction
    )
}

predicate isInterestingMMIOReturnExpr(Expr expr) {
    expr instanceof MMIOTracedExpr and
    expr.getEnclosingElement() instanceof ReturnStmt and
    expr.getEnclosingFunction() instanceof DriverFunction
}

predicate isInterestingMMIOBranchFunction(Function func) {
    exists( Expr expr | 
        expr.getEnclosingFunction() = func and
        isInterestingMMIOBranchExpr(expr)
    )
}

predicate isInterestingMMIOReturnFunction(Function func) {
    exists( Expr expr |
        expr.getEnclosingFunction() = func and
        isInterestingMMIOReturnExpr(expr)
    )
}

class InterestingMMIOBranchFunction extends Function{
    InterestingMMIOBranchFunction() {
        isInterestingMMIOBranchFunction(this)
    }
}

class InterestingMMIOReturnFunction extends Function{
    InterestingMMIOReturnFunction() {
        isInterestingMMIOReturnFunction(this)
    }
}

from InterestingMMIOBranchFunction func
select func


// expr instanceof DriverFromExpr
// select expr
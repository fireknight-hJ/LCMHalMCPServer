import cpp
import MMIOAnalyzer

// from DriverFromExpr expr, DriverFromFunction func
// where
//     expr.getEnclosingFunction() = func
// // where
// //     func.getName() = "HAL_TIM_IRQHandler"
// select func, expr

// from File file
// select file

from Function func, Expr e
where
    func.getName() = "GPIO_PortInit" 
    // and 
    // isInterestingMMIOBranchExpr(e) and
    // e.getEnclosingFunction() = func
select func
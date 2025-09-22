import cpp
import MMIOAnalyzer

from Expr expr, Function func, PointerType pt, InterestingMMIOFunctionContainType type
where
isInterestingMMIOFunction(func) and
(
    (
        expr.getEnclosingFunction() = func and
        expr.getType() = type 
    ) or
    (
        expr.getEnclosingFunction() = func and
        expr.getType() = pt and
        pt.getBaseType() = type
    )
)
//  and
// (
//     type instanceof Enum or 
//     type instanceof Class or 
//     type instanceof TypedefType and type.(TypedefType).getBaseType() instanceof Enum or
//     type instanceof TypedefType and type.(TypedefType).getBaseType() instanceof Class
// )

select func.getName(), type.toString(), type.getFile().toString(), type.getStartLine(), type.getDriverTypeFlag()
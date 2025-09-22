import DriverLocator

// from DriverFromFunction f, Expr e, Type type
// where
// e.getEnclosingFunction() = f and
// e.getType() = type and
// not (type instanceof Enum or type instanceof TypedefType )
// select f, type, type.getFile(), type.getName(), type.getLocation().getStartLine()

// Enum, Class, Struct

from Expr expr, DriverFromFunction func, PointerType pt, DriverFromFunctionContainType type
where
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
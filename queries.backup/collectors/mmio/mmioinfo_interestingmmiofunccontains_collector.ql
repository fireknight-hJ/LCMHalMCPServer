import libraries.MMIOAnalyzer

class DriverFromFunctionContainType extends Type
{
    // DriverFromFunctionContainType() {
    //     (
    //         // Direct point to
    //         exists( Expr expr, DriverFromFunction func | 
    //             expr.getEnclosingFunction() = func and
    //             expr.getType() = this 
    //         ) or
    //         // Pointer pointed to
    //         exists( Expr expr, DriverFromFunction func, PointerType pt | 
    //             expr.getEnclosingFunction() = func and
    //             expr.getType() = pt and
    //             pt.getBaseType() = this 
    //         )
    //     ) and
    //     (
    //         this instanceof Enum or 
    //         this instanceof Class or 
    //         this instanceof TypedefType and this.(TypedefType).getBaseType() instanceof Enum or
    //         this instanceof TypedefType and this.(TypedefType).getBaseType() instanceof Class
    //     )
    // }

    int getStartLine() {
        (this instanceof Enum and result = this.getLocation().getStartLine()) or
        (this instanceof Class and result = this.getLocation().getStartLine()) or
        (this instanceof TypedefType and result = this.(TypedefType).getBaseType().getLocation().getStartLine())
    }

    string getDriverTypeFlag() {
        (this instanceof Enum and result = "enum") or
        (this instanceof Class and result = "class") or
        (this instanceof TypedefType and result = "typedef")
        // (this instanceof DriverType and result = "driver") or
        // (not this instanceof DriverType and result = "other")
    }
}

from Expr expr, InterestingMMIOFunction func, PointerType pt, DriverFromFunctionContainType type
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
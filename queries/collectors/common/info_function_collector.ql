
/**
 * @name Function Information with Calls and Structs
 * @description Retrieves all functions along with their file, location, called functions, and struct types used in the function.
 * @kind table
 */

import cpp
// import MMIOAnalyzer
import libraries.DriverLocator

class FunctionInfo extends Function{
    FunctionInfo() {
        this instanceof Function
    }

    predicate isWeak() {
        this.getAnAttribute().getName() = "weak"
    }

    string getWeakFlag() {
        (this.isWeak() and result = "weak") or
        (not this.isWeak() and result = "normal")
    }

    string getDriverFlag() {
        (this instanceof DriverFunction and result = "driver") or
        (not this instanceof DriverFunction and result = "other")
    }
}

from Function f
// 保证名称里没有operator()，不是虚函数，不是析构函数
where not f.getName().matches("%operator%") and
not f instanceof VirtualFunction and
not f instanceof Destructor
// where not f.isInline() and
// // not f.getAnAttribute().getName() = "weak" and 
// // not f instanceof DriverWeakFunction
// not f.getAnAttribute().getName() = "always_inline"
select 
    // f,
    f.getName(),                      // Function name
    f.getFile().getAbsolutePath(),     // File where the function is located
    f.getLocation().getStartLine(),    // Starting line of the function
    f.(FunctionInfo).getWeakFlag(),     // Weak function flag
    f.(FunctionInfo).getDriverFlag()   // Driver function flag
    // f.getLocation().getEndLine()      // Ending line of the function

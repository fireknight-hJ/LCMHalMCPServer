
/**
 * @name Function Information with Calls and Structs
 * @description Retrieves all functions along with their file, location, called functions, and struct types used in the function.
 * @kind table
 */

 import cpp
 import libraries.MMIOAnalyzer
 
 // from MMIOFunction func
 // select func.getFile().toString()
 
 // predicate excludeWeakAndStaticInline(Function f) {
 //     not f.has("weak") and
 //     not (f.isInline() and f.isStatic())
 // }
  
 
 from MMIOTracedBufferFunction f
 where not f.isInline() and
 not f.getAnAttribute().getName() = "weak" and
 not f.getAnAttribute().getName() = "always_inline"
 select 
     f.getName(),                      // Function name
     f.getFile().getAbsolutePath(),     // File where the function is located
     f.getLocation().getStartLine(),    // Starting line of the function
     f.getLocation().getEndLine()      // Ending line of the function
     // f.getLocation().getStartColumn(),  // Starting column of the function
     // f.getLocation().getEndColumn()    // Ending column of the function
     // f.getACalledFunction().getName(),  // Called functions
     // f.getATypeAccess().getTargetType().getName()  // Structs used in the function
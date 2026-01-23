import libraries.DriverLocator

from DriverFromFunctionCall call
// where call.toString() = "call to netif_is_link_up"
select call.toString(), call.getEnclosingFunction().getName(), call.getFile().getAbsolutePath().toString(), call.getLocation().getStartLine(), call.checkType()


/**
 * checkType:
 * 
 * "stmt" : 直接注释
 * "compare" : LLM分析
 * "call" : LLM分析
 * "init" : LLM分析
 * "return" : LLM分析
 * "assign" : LLM分析
 * "arithmetic" : LLM分析
 */
import cpp
import DriverLocator

// 定义一个查询，找出返回值为 void 且参数为 void 的函数
from Function func
where 
  // 检查函数的返回类型是否为 void
  func.getType().getName() = "void" and
  // 检查函数的参数列表是否为空
  func.getNumberOfParameters() = 0
  // 检查
select func, "This function returns void and takes no parameters."
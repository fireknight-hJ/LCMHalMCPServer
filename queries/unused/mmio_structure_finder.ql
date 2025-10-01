
/**
 * This is a mmio structure finder to locate all the mmio operations automatically
 * @name Hello world
 * @kind problem
 * @problem.severity warning
 * @id cpp/example/hello-world
 */

import cpp

// 递归定义，用于判断表达式是否由常量组成
predicate isConstantExpr(Expr e) {
  e instanceof Literal or
  // (e instanceof Literal and e.getValue() != "0")or
  e instanceof BinaryArithmeticOperation and
    isConstantExpr(e.(BinaryArithmeticOperation).getLeftOperand()) and
    isConstantExpr(e.(BinaryArithmeticOperation).getRightOperand())
}

predicate isConstantZeroExpr(Expr e) {
  e instanceof Literal and e.getValue() = "0"
}

predicate isStructType(Type t) {
  t instanceof Struct or 
  t instanceof TypedefType and
    t.(TypedefType).getBaseType() instanceof Struct
}

//下面的搜索可以找到的是给一些寄存器直接赋值的操作
from AssignExpr assign, FieldAccess ma, Struct s, PointerType pt 
where 
  // 确定ma是struct.member或者struct->member的形式
  (ma instanceof PointerFieldAccess or ma instanceof ValueFieldAccess) and
  // 确定ma是一个指针且指向一个结构体(非0结构体)
  ma.getActualType() = pt and
  // 绑定成员访问和赋值表达式
  assign.getLValue() = ma and
  // 查找右边的初始化是数值常量（以及常量算式），表示固定的地址值
  isConstantExpr(assign.getRValue()) and
  not isConstantZeroExpr(assign.getRValue()) and
  // 检查ma是否为结构体类型（Struct 或者 Typedef Struct）
  isStructType(ma.getUnderlyingType().(PointerType).getBaseType())
  // ma.getUnderlyingType().(PointerType).getBaseType() instanceof TypedefType
  // pt.getBaseType() instanceof Struct
select assign, ma, pt.getBaseType(), assign.getRValue(), assign.getRValue().getType() , "Assignment of peripheral address to struct member", ma.getUnderlyingType().(PointerType).getBaseType()
// ma.getUnderlyingType().getName()

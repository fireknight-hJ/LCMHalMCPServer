import cpp

predicate isRegistrationFieldAccess(FieldAccess fieldAccess) {
    exists( AssignExpr assign, FunctionAccess funcAccess| 
        assign.getLValue() = fieldAccess and
        assign.getRValue() = funcAccess
    ) or
    exists( ClassAggregateLiteral aggregateLiteral | 
        aggregateLiteral.getAChild() = fieldAccess
    )
}

// FunctionAccess getRegistrationFunction(FieldAccess fieldAccess) {
//     exists( AssignExpr assign, FunctionAccess funcAccess| 
//         assign.getLValue() = fieldAccess and
//         assign.getRValue() = funcAccess and 
//         result = funcAccess.getTarget()
//     )
// }

// // 1. 通过赋值表达式注册
// from FieldAccess fieldAccess, AssignExpr assign, FunctionAccess funcAccess
// where assign.getLValue() = fieldAccess and
//       assign.getRValue() = funcAccess
// select assign, fieldAccess, funcAccess.getTarget()

// 2. 直接定义结构体
from FunctionAccess funcAccess, ClassAggregateLiteral aggregateLiteral
where aggregateLiteral.getAChild() = funcAccess
select funcAccess

// from FieldAccess fieldAccess
// where isRegistrationFieldAccess(fieldAccess)
// select fieldAccess
// , getRegistrationFunction(fieldAccess)

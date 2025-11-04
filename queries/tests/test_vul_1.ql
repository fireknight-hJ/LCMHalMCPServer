import cpp

import semmle.code.cpp.controlflow.IRGuards

// from
//     GuardCondition gc,
//     VariableAccess va,
//     PointerDereferenceExpr pde

// where
//     // va.getTarget()
//     va.getParent*() = gc

from Function func, Expr e
select func, e, e.getFile()
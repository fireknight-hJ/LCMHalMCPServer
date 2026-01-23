import cpp
import semmle.code.cpp.dataflow.new.DataFlow

from Function fopen, FunctionCall fc, Expr src, DataFlow::Node source, DataFlow::Node sink
where
// fopen.hasGlobalName("HAL_DMA_RegisterCallback") and
  fc.getTarget() = fopen and
  source.asIndirectExpr(1) = src and
  sink.asIndirectExpr(1) = fc.getArgument(0) and
  DataFlow::localFlow(source, sink)
select src

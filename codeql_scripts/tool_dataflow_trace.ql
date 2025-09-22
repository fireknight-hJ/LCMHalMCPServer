import cpp
import DriverLocator
import semmle.code.cpp.dataflow.new.TaintTracking

module MMIOFlowConfiguration implements DataFlow::ConfigSig {
    predicate isSource(DataFlow::Node source) {
      source.asExpr() instanceof Expr
    }

    predicate isSink(DataFlow::Node sink) {
    //   sink.asExpr() instanceof Expr and 
      not sink.asExpr().getFile() instanceof DriverFile
    }
}

predicate isMMIOConstantExpr(ConstantExpr src_mmio) {
    exists( DataFlow::Node source, DataFlow::Node sink, Expr varAccess, PointerDereferenceExpr deref | 
        source.asExpr() = src_mmio and
        isConstantBigValueExpr(src_mmio) and
        sink.asExpr() = varAccess and 
        deref.getOperand() = varAccess and
        TaintFlow::flow(source, sink) and
        not sink.asExpr().getFile() instanceof DriverFile
    )
}

predicate isMMIOTracedExpr(Expr e) {
    exists( DataFlow::Node source, DataFlow::Node sink, ConstantExpr src_mmio | 
        source.asExpr() = src_mmio and
        isMMIOConstantExpr(src_mmio) and
        sink.asExpr() = e and 
        TaintFlow::flow(source, sink) and
        not sink.asExpr().getFile() instanceof DriverFile
    )
    
}



from ConstantExpr src_mmio, DataFlow::Node source, DataFlow::Node sink, Expr varAccess, PointerDereferenceExpr deref
where
source.asExpr() = src_mmio and
isConstantBigValueExpr(src_mmio) and
sink.asExpr() = varAccess and 
deref.getOperand() = varAccess and
TaintFlow::flow(source, sink) and
not sink.asExpr().getFile() instanceof DriverFile
select src_mmio, deref, varAccess, sink.asExpr().getFile()
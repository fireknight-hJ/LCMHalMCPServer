import cpp
import MMIOAnalyzer

predicate isMMIOOperation_XXIFn(Expr e) {
    
    exists( PointerFieldAccess pfa, ValueFieldAccess vfa, ValueFieldAccess vfaa |
        e = vfa and 
        (( vfa.getQualifier() = vfaa and
            vfaa.getQualifier() = pfa ) or
        vfa.getQualifier() = pfa ) and
        (pfa.toString() = "(unknown field)" or isConstantBigValueExpr(pfa.getQualifier()))
    )
}

predicate isMMIOStructure_MK(Struct s){
    exists( FunctionCall call, Expr e, TypedefType typeDef | 
        call.getTarget().getParameter(0).getType() instanceof PointerType and
        (
            (call.getTarget().getParameter(0).getType().(PointerType).getBaseType() = typeDef and
            typeDef.getBaseType() = s) or
            call.getTarget().getParameter(0).getType().(PointerType).getBaseType() = s
        ) and
        call.getArgument(0) = e and
        isConstantBigValueExpr(e)
    )
}

// predicate () {
    
// }

// from PointerFieldAccess pfa, ValueFieldAccess vfa, ValueFieldAccess vfaa
// where
// // pfa.getLocation().getStartLine() = 611
// ((vfa.getQualifier() = vfaa and
// vfaa.getQualifier() = pfa ) or
// vfa.getQualifier() = pfa ) and
// // pfa.toString() = "(unknown field)" 
// isConstantBigValueExpr(pfa.getQualifier()) 
// select 
// vfa, pfa, pfa.getQualifier().getType()//, pfa.getTarget()
from FunctionCall call, Expr e, Struct s, TypedefType typeDef
where
call.getTarget().getParameter(0).getType() instanceof PointerType and
(
    (call.getTarget().getParameter(0).getType().(PointerType).getBaseType() = typeDef and
    typeDef.getBaseType() = s) or
    call.getTarget().getParameter(0).getType().(PointerType).getBaseType() = s
) and
call.getArgument(0) = e and
isConstantBigValueExpr(e)
select e, call.getTarget().getParameter(0).getType().(PointerType).getBaseType()
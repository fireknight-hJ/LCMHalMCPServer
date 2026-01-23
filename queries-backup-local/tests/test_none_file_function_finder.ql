import cpp
import libraries.MMIOAnalyzer

from ClassAggregateLiteral struct, ConstantExpr literal, MemberVariable member, FunctionPointerType ptrType
where member.getDeclaringType() = struct.getType() and
    struct.getAFieldExpr(member) instanceof ConstantExpr and
    member.getType() = ptrType

select 
    struct, member, ptrType
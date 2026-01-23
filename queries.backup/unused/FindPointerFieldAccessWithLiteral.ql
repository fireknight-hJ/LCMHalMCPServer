import cpp
import MMIOAnalyzer

from PointerFieldAccess pfa, Literal lit
where 
    pfa.getQualifier() = lit
    and lit.getEnclosingFunction().getName() = "SystemInit"
select pfa
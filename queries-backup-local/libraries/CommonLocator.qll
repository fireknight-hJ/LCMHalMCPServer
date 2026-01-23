import cpp
import RegistrationLocator

class AllCall extends Call {
    Function getTargetFunction() {
        (
            this instanceof FunctionCall and
            result = this.getTarget()
        ) or
        (
            this instanceof VariableCall and
            result = getRegisteredFunction(this.(VariableCall).getExpr())
        )
    }
    string toString2() {
        (
            this instanceof FunctionCall and
            result = this.toString()
        ) or
        (
            this instanceof VariableCall and
            result = this.(VariableCall).getExpr().toString()
        )
    }
    string isDirectCall() {
        (
            this instanceof FunctionCall and
            result = "direct"
        ) or
        (
            this instanceof VariableCall and
            result = "indirect"
        )
    }
    string checkHasReturnValue() { 
        exists( AssignExpr assign | 
        assign.getRValue() = this and 
        result = "hasReturnValue" ) or
        result = "noReturnValue"
    }
}
import cpp
import MMIOAnalyzer
import RegistrationLocator

predicate isConstantExpr(Expr e) {
    e instanceof Literal or
    e instanceof BinaryOperation and
    isConstantExpr(e.(BinaryOperation).getLeftOperand()) and
    isConstantExpr(e.(BinaryOperation).getRightOperand()) 
}

// DriverFile 代表驱动文件
class DriverFile extends File
{
    DriverFile() {
        // rules for freertos driver
        this.toString().matches(["%Driver%"]) or
        // rules for nxp driver
        (
            this.toString().matches(["%mcuxsdk/drivers%"]) and
            not this.toString().matches(["%mcuxsdk/drivers/common%"])
        )
        // 
        // or
        // this.getAnIncludedFile() instanceof DriverFile
        // this.getAnIncludedFile().toString().matches(["%Driver%"])
    }
}

// UtilFile 代表工具文件或者标准库, 如果驱动库函数调用了UtilFile中定义的函数可以认为不需要考虑
class UtilFile extends File
{
    UtilFile() {
        this.toString().matches(["%Utilities%", "%CMSIS%", ""])
    }
}

class DriverUsingFile extends File
{
    DriverUsingFile() {
        not this instanceof DriverFile and
        (this.getAnIncludedFile() instanceof DriverFile or
        this.getAnIncludedFile() instanceof DriverUsingFile)
    }
}

class NotDriverFile extends File
{
    NotDriverFile() {
        not this instanceof DriverFile
    }
}

// Deprecated: Middleware related
predicate isMiddlewareStructure(Class s) { 
    s.getFile().toString().matches("%Middlewares%")
}

predicate isMiddlewareFunction(Type t){
    t.getUnderlyingType().getUnspecifiedType() instanceof Class and
    isDriverStructure(t.getUnderlyingType().getUnspecifiedType())
}

predicate isMiddlewaresFunction(Function f) {
    f.getFile().toString().matches("%Middlewares%")
}

class MiddlewareType extends Type
{
    MiddlewareType(){
        this.getFile().toString().matches("%Middleware%")
    }
}


predicate isDriverStructure(Class s) { 
    s.getFile() instanceof DriverFile
}

predicate isDriverTypedef(Type t){
    t.getUnderlyingType().getUnspecifiedType() instanceof Class and
    isDriverStructure(t.getUnderlyingType().getUnspecifiedType())
}


predicate isDriverFunction(Function f) {
    f.getFile() instanceof DriverFile
}


class DriverType extends Type
{
    DriverType(){
        this.getFile() instanceof DriverFile or
        (this instanceof ArrayType and
        this.(ArrayType).getBaseType() instanceof DriverType) or
        (this instanceof PointerType and 
        this.(PointerType).getBaseType() instanceof DriverType)
    }
}

class DriverFunction extends Function
{
    DriverFunction(){
        isDriverFunction(this)
    }
}

class DriverWeakFunction extends Function
{
    DriverWeakFunction(){
        isDriverFunction(this) and
        this.getAnAttribute().getName() = "weak"
    }
}


class NotDriverType extends Type
{
    NotDriverType(){
        not this instanceof DriverType
    }
}

class NotDriverFunction extends Function
{
    NotDriverFunction(){
        not this instanceof DriverFunction
    }
}

// 1. 查一遍函数参数的type有无来自Driver的
class DriverFromParameter extends Parameter
{
    DriverFromParameter() {
        this.getType() instanceof DriverType and
        not this.getFile() instanceof DriverFile
    }
}

// 2. 查DeclStmt
class DriverFromDeclStmt extends DeclStmt
{
    DriverFromDeclStmt(){
        exists( DriverType type | 
            this.getADeclarationEntry().getType() = type and
            this.getFile() instanceof NotDriverFile
        ) 
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

// 3. 直接查Expr
class DriverFromExpr extends Expr
{
    DriverFromExpr(){
        this.getFile() instanceof NotDriverFile and
        (
            this.getType().getUnspecifiedType() instanceof DriverType or
            (this instanceof FieldAccess and this.(FieldAccess).getQualifier() instanceof DriverFromExpr)or
            (this instanceof UnaryOperation and this.(UnaryOperation).getOperand() instanceof DriverFromExpr)or
            (this instanceof BinaryOperation and this.(BinaryOperation).getAnOperand() instanceof DriverFromExpr) or
            (this instanceof ParenthesisExpr and this.(ParenthesisExpr).getExpr() instanceof DriverFromExpr) or
            (this instanceof DriverFromFunctionCall) or
            (this instanceof DriverFromVariableCall)
            // or
            // (isMMIOTracedExpr(this))
        )
        // and not this instanceof DriverFromFunctionCall
    }

    string checkExprType(){
        (this instanceof Call and result = "call") or
        (this instanceof Cast and result =  "cast") or
        (this instanceof VariableAccess and result = "varaccess") or
        (this instanceof Assignment and result = "assign") or
        (this instanceof AggregateLiteral and result = "literal") or
        (this instanceof ArrayExpr and result = "array") or
        (this instanceof BinaryOperation and result = "binary") or
        (this instanceof UnaryOperation and result = "unary") or
        (this instanceof Conversion and result = "conversion")
    }

    string checkEnclosingType(){
        (
            not this.getEnclosingElement() instanceof DriverFromExpr and
            (
                (this.getEnclosingElement() instanceof ExprStmt and result = "stmt") or
                (this.getEnclosingElement() instanceof BinaryOperation and result = "binary") or
                (this.getEnclosingElement() instanceof UnaryOperation and result = "unary") or
                (this.getEnclosingElement() instanceof Assignment 
                    and this.getEnclosingElement().(Assignment).getLValue() = this and result = "assign_from") or
                (this.getEnclosingElement() instanceof Assignment 
                    and this.getEnclosingElement().(Assignment).getRValue() = this and result = "assign_to") or
                // (this.getEnclosingElement() instanceof Assignment and result = "assign") or
                (this.getEnclosingElement() instanceof ReturnStmt and result = "return") or
                (this.getEnclosingElement() instanceof Initializer and result = "init") or
                (this.getEnclosingElement() instanceof BinaryArithmeticOperation and result = "arithmetic") or
                (this.getEnclosingElement() instanceof Call and result = "call") or
                (this.getEnclosingElement() instanceof EnumConstantAccess and result = "enum") or
                (this.getEnclosingElement() instanceof ControlStructure and result = "control_flow") or
                (this.getEnclosingElement() instanceof FieldAccess and result = "field_access")
            )
         ) or
        (this.getEnclosingElement() instanceof DriverFromExpr and result = "skip") or
        // (this.getEnclosingElement()  and result = "null") or
        // (exists( IfStmt ifstmt | ifstmt.getCondition() = this ) and result = "if") or
        (exists( WhileStmt whilestmt | whilestmt.getCondition() = this ) and result = "while") or
        (exists( DoStmt dostmt | dostmt.getCondition() = this ) and result = "do") or
        (exists( ForStmt forstmt | forstmt.getCondition() = this ) and result = "for") or
        (exists( ReturnStmt retstmt | retstmt.getExpr() = this ) and result = "return") 
        // (this.getEnclosingElement() instanceof Assignment and result = "assign")
    }
}

// 4. 查call调用的函数
class DriverFromFunctionCall extends FunctionCall
{
    DriverFromFunctionCall(){
        this.getTarget() instanceof DriverFunction and
        this.getFile() instanceof NotDriverFile
    }
    
    string checkHasReturnValue() { 
        exists( AssignExpr assign | 
        assign.getRValue() = this and 
        result = "hasReturnValue" ) or
        result = "noReturnValue"
    }
    string checkType(){
        (this.getEnclosingElement() instanceof ExprStmt and result = "stmt") or
        (this.getEnclosingElement() instanceof ComparisonOperation and result = "compare") or
        (this.getEnclosingElement() instanceof Assignment and result = "assign") or
        (this.getEnclosingElement() instanceof ReturnStmt and result = "return") or
        (this.getEnclosingElement() instanceof Initializer and result = "init") or
        (this.getEnclosingElement() instanceof BinaryArithmeticOperation and result = "arithmetic") or
        (this.getEnclosingElement() instanceof Call and result = "call")
    }
}

class DriverFromCalledFunction extends Function
{
    DriverFromCalledFunction(){
        exists( DriverFromCall call |
            call.getTargetFunction() = this and
            this instanceof DriverFunction
        )
    }

    Function getCaller() {
        (
            exists( DriverFromCall call |
                call.getTargetFunction() = this and
                result = call.getEnclosingFunction()
            )
        )
    }

    Call getDriverFromCall() {
        (
            exists( DriverFromCall call |
                call.getTargetFunction() = this and
                result = call
            )
        )
    }
}

// 8. 其他地方声明的全局变量
class DriverFromGlobalVariable extends GlobalVariable
{
    DriverFromGlobalVariable(){
        this.getType().getFile() instanceof DriverFile and
        this.getFile() instanceof NotDriverFile
    }
}

class DriverFromFunction extends Function
{
    DriverFromFunction() {
        not this.getAnAttribute().getName() = "weak" and
        exists( DriverFromExpr expr | 
            expr.getEnclosingFunction() = this
        ) or
        exists( DriverFromFunctionCall call | 
            call.getEnclosingFunction() = this
        )
    }
}

class DriverFromFunctionContainType extends Type
{
    DriverFromFunctionContainType() {
        (
            // Direct point to
            exists( Expr expr, DriverFromFunction func | 
                expr.getEnclosingFunction() = func and
                expr.getType() = this 
            ) or
            // Pointer pointed to
            exists( Expr expr, DriverFromFunction func, PointerType pt | 
                expr.getEnclosingFunction() = func and
                expr.getType() = pt and
                pt.getBaseType() = this 
            )
        ) and
        (
            this instanceof Enum or 
            this instanceof Class or 
            this instanceof TypedefType and this.(TypedefType).getBaseType() instanceof Enum or
            this instanceof TypedefType and this.(TypedefType).getBaseType() instanceof Class
        )
    }

    int getStartLine() {
        (this instanceof Enum and result = this.getLocation().getStartLine()) or
        (this instanceof Class and result = this.getLocation().getStartLine()) or
        (this instanceof TypedefType and result = this.(TypedefType).getBaseType().getLocation().getStartLine())
    }

    string getDriverTypeFlag() {
        (this instanceof DriverType and result = "driver") or
        (not this instanceof DriverType and result = "other")
    }
}

class DriverFromVariableCall extends VariableCall
{
    DriverFromVariableCall(){
        // this.getExpr().(FieldAccess).getQualifier() instanceof DriverFromExpr and
        // getRegisteredFunction(this.getExpr()) instanceof DriverFunction and
        this.getFile() instanceof NotDriverFile and
        this.getExpr().(FieldAccess).getQualifier().getType().getUnspecifiedType() instanceof DriverType
        // .getQualifier().getType() instanceof DriverType
    }
}

class DriverFromCall extends Call {
    DriverFromCall() {
        this instanceof DriverFromFunctionCall or
        this instanceof DriverFromVariableCall
    }

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
}



class DriverToCall extends Call {
    DriverToCall() {
        (
            this instanceof FunctionCall and
            this.getFile() instanceof DriverFile 
            and
            (this.getTarget() instanceof NotDriverFunction or this.getTarget() instanceof DriverWeakFunction) and
            not this.getTarget().getFile() instanceof UtilFile
        ) or
        (
            this instanceof VariableCall and
            this.getFile() instanceof DriverFile and
            this.(VariableCall).getExpr() instanceof FieldAccess and
            getRegisteredFunction(this.(VariableCall).getExpr()) instanceof NotDriverFunction 
            and
            not getRegisteredFunction(this.(VariableCall).getExpr()).getFile() instanceof UtilFile
        )
    }
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
}

class MMIOTracedDriverFromExpr extends DriverFromExpr
{
    MMIOTracedDriverFromExpr() {
        this instanceof MMIODMATracedExpr
    }
}

/**
 * 1. 查一遍函数参数的type有无来自Driver的
 * 2. 查一遍DeclStmt的target的type
 * 3. 查一遍VariableAccess
 * 4. 查一遍call的参数和call调用的函数（也要考虑下函数指针问题）
 * 5. 可能存在在Driver中是weak函数但是在新目录中被覆盖的情况
 * 6. 文件是否include了一个Driver的头文件
 * 7. 直接调用汇编指令的情况
 * 8. 全局变量的情况有没有来自其他
 * 9. 函数注册
*/

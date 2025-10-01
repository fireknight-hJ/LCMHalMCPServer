

import semmle.code.cpp.dataflow.new.TaintTracking

predicate isConstantExpr(Expr e) {
    e instanceof Literal or
    e instanceof BinaryOperation and
    isConstantExpr(e.(BinaryOperation).getLeftOperand()) and
    isConstantExpr(e.(BinaryOperation).getRightOperand()) 
}

predicate isConstantBigValueExpr(Expr e) {
    e instanceof Literal and e.getValue().toInt() > "268435456".toInt() or
    (e instanceof BinaryOperation and
    (isConstantBigValueExpr(e.(BinaryOperation).getLeftOperand()) or
    isConstantBigValueExpr(e.(BinaryOperation).getRightOperand())) )
}

class ConstantExpr extends Expr 
{
    ConstantExpr(){
        isConstantExpr(this)
    }
}

predicate isConstantZeroExpr(Expr e) {
    e instanceof Literal and e.getValue() = "0"
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

predicate isMMIOStructure(Struct s) {
    // MMIO 直接访问模式
    exists( Expr ma, AssignExpr assign, PointerType pt |  
        // 确定ma是一个指针且指向一个结构体(非0结构体)
        ma.getActualType() = pt and
        // 绑定成员访问和赋值表达式
        assign.getLValue() = ma and
        // 查找右边的初始化是数值常量（以及常量算式），表示固定的地址值
        isConstantExpr(assign.getRValue()) and
        not isConstantZeroExpr(assign.getRValue()) and
        // 检查S是否是这个结构体或者这个typedef代表的结构体
        ((ma.getUnderlyingType().(PointerType).getBaseType() instanceof Struct and
            s=ma.getUnderlyingType().(PointerType).getBaseType()) or
        (ma.getUnderlyingType().(PointerType).getBaseType() instanceof TypedefType and
            ma.getUnderlyingType().(PointerType).getBaseType().(TypedefType).getBaseType() = s))
        ) or
    // MMIO 描述符注册模式
    exists( MMIOFieldAccess mmio, ArrayExpr src, DataFlow::Node source, DataFlow::Node sink, ArrayExpr mmio_mem, CStyleCast cast, PointerType pt| 
        // from PTR to MMIO
        source.asExpr() = src and
        sink.asExpr() = mmio and
        TaintFlow::flow(source, sink) and
        // isSameFieldAccess(src.getArrayBase(), mmio_mem.getArrayBase()) and
        isSameExpr(src, mmio_mem) and
        mmio_mem.getConversion() = cast and
        cast.getActualType() = pt and
        // 检查S是否是这个结构体或者这个typedef代表的结构体
        ((pt.getBaseType() instanceof Struct and
            s=pt.getBaseType()) or
        (pt.getBaseType() instanceof TypedefType and
            pt.getBaseType().(TypedefType).getBaseType() = s))
        ) or
    // 非注册，直接将Literal作为指针传入MMIO函数参数的模式 
    // deprecated : 直接找函数参数实在太笨了，有更高明的方案
    isMMIOStructure_MK(s) or
    // 非注册，直接将Literal作为指针指向对应的MMIO操作结构体的模式
    exists( MMIOLiteralFieldAccess fa | 
        fa.getType() = s 
        )
    
}

class MMIOType extends Type
{
    MMIOType() {
        isMMIOType(this)
    }
}

predicate isMMIOType(Type t) {
    (t instanceof Struct and isMMIOStructure(t.(Struct))) or 
    (t instanceof TypedefType and 
        t.(TypedefType).getBaseType() instanceof Struct and 
        isMMIOStructure(t.(TypedefType).getBaseType()))
}

class MMIOExpr extends Expr
{
    MMIOExpr() {
        isMMIOExpr(this)
    }
}

predicate isMMIOExpr(Expr ma) {
    // exists( AssignExpr assign |
        // 确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
        // ((ma instanceof PointerFieldAccess and isMMIOType(ma.getQualifier().getType().(PointerType).getBaseType())) or
        // (ma instanceof ValueFieldAccess and isMMIOType(ma.getQualifier().getType()))) and
        // 绑定成员访问和赋值表达式
        // (assign.getLValue() = ma or assign.getRValue() = ma)
        
    // ) or
    // 1. 可能直接是这个结构体本身
    isMMIOType(ma.getType()) or
    isMMIOType(ma.getType().(PointerType).getBaseType()) or 
    // 2. STM32驱动的MMIO操作：确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
    ((ma instanceof PointerFieldAccess and isMMIOType(ma.(PointerFieldAccess).getQualifier().getType().(PointerType).getBaseType())) or
    (ma instanceof ValueFieldAccess and isMMIOType(ma.(ValueFieldAccess).getQualifier().getType()))) or
    // 3. 可能PointerFieldAccess的Qualifier是一个Literal，即地址值
    isMMIOLiteralFieldAccess(ma)
}

class MMIOLiteralFieldAccess extends FieldAccess {
    MMIOLiteralFieldAccess() {
        isMMIOLiteralFieldAccess(this)
    }

    // Type getStructType() {
    //     result = this.getQualifier().getType().(PointerType).getBaseType()
    // }
}

predicate isMMIOLiteralFieldAccess(FieldAccess e) {
    exists( Expr lit | 
        isConstantBigValueExpr(lit) and
        e instanceof PointerFieldAccess and
        e.(PointerFieldAccess).getQualifier() = lit )
}

predicate isDriverType(Type t) {
    exists( FieldAccess ma|
        // 确定ma是struct.member或者struct->member的形式
        (ma instanceof PointerFieldAccess or ma instanceof ValueFieldAccess) and
        // ma 指向的是一个MMIO类型
        isMMIOType(ma.getUnderlyingType().(PointerType).getBaseType()) and
        t = ma.getQualifier().getType().getUnderlyingType().(PointerType).getBaseType())

}

predicate isMMIOOperation_XXIFn(Expr e) {
    exists( PointerFieldAccess pfa, ValueFieldAccess vfa, ValueFieldAccess vfaa |
        e = vfa and 
        (( vfa.getQualifier() = vfaa and
            vfaa.getQualifier() = pfa ) or
        vfa.getQualifier() = pfa ) and
        (pfa.toString() = "(unknown field)" or isConstantBigValueExpr(pfa.getQualifier()))
    )
}


/**
 * A Struct Type that represent a MMIO DataStructure
 * 
 * example: typedef struct
 *          {
 *              __IO uint32_t CR1;
 *              __IO uint32_t CR2;
 *              ......
 *          } USART_TypeDef;
 */
class MMIOStructType extends Struct
{
    MMIOStructType(){
        exists( FieldAccess ma, AssignExpr assign, PointerType pt |  
            // 确定ma是struct.member或者struct->member的形式
            (ma instanceof PointerFieldAccess or ma instanceof ValueFieldAccess) and
            // 确定ma是一个指针且指向一个结构体(非0结构体)
            ma.getActualType() = pt and
            // 绑定成员访问和赋值表达式
            assign.getLValue() = ma and
            // 查找右边的初始化是数值常量（以及常量算式），表示固定的地址值
            isConstantExpr(assign.getRValue()) and
            not isConstantZeroExpr(assign.getRValue()) and
            // 检查S是否是这个结构体或者这个typedef代表的结构体
            ((ma.getUnderlyingType().(PointerType).getBaseType() instanceof Struct and
                this=ma.getUnderlyingType().(PointerType).getBaseType()) or
            (ma.getUnderlyingType().(PointerType).getBaseType() instanceof TypedefType and
                ma.getUnderlyingType().(PointerType).getBaseType().(TypedefType).getBaseType() = this))
        )
    }
}

/**
 * A FieldAccess that acces the MMIO Info 
 * 
 * example: hrng->Instance->DR, hrtc->Instance->ISR
 */
class MMIOFieldAccess extends FieldAccess
{
    MMIOFieldAccess() {
        // STM32驱动的MMIO操作：确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
        (this instanceof PointerFieldAccess and isMMIOType(this.getQualifier().getType().(PointerType).getBaseType())) or
        (this instanceof ValueFieldAccess and isMMIOType(this.getQualifier().getType())) or
        // Ambiq驱动的MMIO操作： BLEIFn(ui32Module)->CLKCFG 形式，fieleaccess 指向一个Literal，是位置的Field类型
        isMMIOOperation_XXIFn(this) or
        // 可能PointerFieldAccess的Qualifier是一个Literal，即地址值
        isMMIOLiteralFieldAccess(this)
    }
}

class DriverFieldAccess extends FieldAccess
{
    DriverFieldAccess() {
        // 确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
        (this instanceof PointerFieldAccess and isDriverType(this.getQualifier().getType().(PointerType).getBaseType())) or
        (this instanceof ValueFieldAccess and isDriverType(this.getQualifier().getType()))
    }
}

/**
 * An AssignExpr that represent the MMIO Info Out
 * 
 * example: hurt->Instance->CR = 0x00FF
 */
class MMIOInfoOutAssignment extends Assignment
{
        
    MMIOInfoOutAssignment() {
        exists( MMIOFieldAccess access |
            this.getLValue() = access
        )
    }
}

/**
 * An AssignExpr that represent the MMIO Info In
 * 
 * example: *pData = hurt->Instance->DR
 */
class MMIOInfoInAssignment extends Assignment
{
    MMIOInfoInAssignment() {
        exists( MMIOFieldAccess access |
            this.getRValue() = access
        )
    }
}

module MMIOFlowConfiguration implements DataFlow::ConfigSig {
    predicate isSource(DataFlow::Node source) {
      source.asExpr() instanceof MMIOFieldAccess 
    }

    predicate isSink(DataFlow::Node sink) {
      // isMMIOStructure(sink.asExpr().getType())
      not sink.asExpr() instanceof MMIOFieldAccess or 
      sink.asParameter() instanceof Parameter
    }

    predicate isAdditionalFlowStep(DataFlow::Node pred, DataFlow::Node succ) {
        // edge: RDR to pdata16bits* ||| pdata16bits = (uint16_t)(huart->Instance->RDR & uhMask);
        // exists( Assignment assign, PointerDereferenceExpr pe |
        //     assign.getLValue() = pe and
        //     succ.asExpr() = pe.getOperand() and
        //     pred.asExpr() = assign.getRValue() and
        //     not succ.asExpr().isConstant() 
        //     // and
        //     // assign.getEnclosingFunction().getName() = "DMA_SetConfig"
        // ) or
        exists( Assignment assign|
            // succ.asExpr().getEnclosingFunction().getName() = "DMA_SetConfig" and
            succ.asExpr() = assign.getLValue() and
            pred.asExpr() = assign.getRValue() and
            // succ.asExpr() instanceof MMIOFieldAccess and
            not succ.asExpr().isConstant()
            
        )
        // edge: pdata16bits to (uint16_t *) pData ||| pdata16bits = (uint16_t *) pData;
        // exists( AssignExpr assign | 
        //      assign.getLValue() = pred.asExpr() and
        //      assign.getRValue() = succ.asExpr() and
        //      assign.getLValue().getType() instanceof PointerType and
        //     //  and
        //     //  (assign.getLValue().getType() instanceof CharPointerType or
        //     //  assign.getLValue().getType() instanceof IntPointerType or
        //     //  assign.getLValue().getType() instanceof VoidPointerType)
        //     not succ.asExpr().isConstant()
        // )
        // exists( FunctionCall call, Function func| 
        //     pred.asParameter() = 
        //     call.
        // ) or
    }
}

module GeneralFlowConfiguration implements DataFlow::ConfigSig {
    predicate isSource(DataFlow::Node source) {
      source.asExpr() instanceof Expr or 
      source.asParameter() instanceof Parameter
    }

    predicate isSink(DataFlow::Node sink) {
      // isMMIOStructure(sink.asExpr().getType())
      sink.asExpr() instanceof Expr or 
      sink.asParameter() instanceof Parameter
    }

    predicate isAdditionalFlowStep(DataFlow::Node pred, DataFlow::Node succ) {
        // edge:  succ = pred
        exists( Assignment assign|
            succ.asExpr() = assign.getLValue() and
            pred.asExpr() = assign.getRValue() and
            not succ.asExpr().isConstant()
        ) //or
    }
}

predicate isInlineFunction(Function func) {
    func.isInline() or
    func.getAnAttribute().getName() = "weak" or
    func.getAnAttribute().getName() = "always_inline"
}

predicate isMMIOFunction(Function func) {
    exists(MMIOFieldAccess fa | fa.getEnclosingFunction() = func) or
    exists(FunctionCall call | isInlineFunction(call.getTarget()) and
    call.getEnclosingFunction() = func and 
    isMMIOFunction(call.getTarget()))
}

predicate isDriverFunction(Function func) {
    exists(DriverFieldAccess fa | fa.getEnclosingFunction() = func) and not
    exists(MMIOFieldAccess fa | fa.getEnclosingFunction() = func)
}

class MMIOFunction extends Function
{
    MMIOFunction() {
        isMMIOFunction(this)
    }
}

class DriverFunction extends Function
{
    DriverFunction() {
        exists(DriverFieldAccess fa | fa.getEnclosingFunction() = this) and not
        exists(MMIOFieldAccess fa | fa.getEnclosingFunction() = this)
    }
}

class DriverTracedFunction extends Function
{
    DriverTracedFunction(){
        exists( Expr snk, Expr src, DataFlow::Node source, DataFlow::Node sink| 
            sink.asExpr() = snk and
            source.asExpr() = src and
            MMIOFlow::flow(source, sink) and
            sink.asExpr().getEnclosingFunction() = this 
            // and
            // not this instanceof MMIOFunction
        )
    }
}

predicate isSameFieldAccess(FieldAccess a, FieldAccess b){
    // a.getTarget().getType() = b.getTarget().getType() and
    // a.getTarget().getName() = b.getTarget().getName() and not

    // if all PointerFieldAccess or all ValueFieldAccess
    (a.getTarget() = b.getTarget() and not
    a = b ) or
    // if PointerFieldAccess and ValueFieldAccess
    // eg: (&heth->TxDescList)->TxDesc[heth->TxDescList.CurTxDesc] and heth->TxDescList.TxDesc[heth->TxDescList.CurTxDesc]
    exists( PointerFieldAccess pfa, ValueFieldAccess vfa, AddressOfExpr aoe| 
        a = pfa and b = vfa and
        pfa.getQualifier() = aoe and
        isSameFieldAccess(aoe.getOperand(), vfa.getQualifier())
    ) or
    exists( PointerFieldAccess pfa, ValueFieldAccess vfa, AddressOfExpr aoe| 
        b = pfa and a = vfa and
        pfa.getQualifier() = aoe and
        isSameFieldAccess(aoe.getOperand(), vfa.getQualifier())
    )
}

predicate isSameArrayExpr(ArrayExpr a, ArrayExpr b){
    // a.getTarget().getType() = b.getTarget().getType() and
    // a.getTarget().getName() = b.getTarget().getName() and not
    (a.getArrayBase() = b.getArrayBase() or
    // (&heth->TxDescList)->TxDesc[heth->TxDescList.CurTxDesc] and heth->TxDescList.TxDesc[heth->TxDescList.CurTxDesc]
     isSameFieldAccess(a.getArrayBase(), b.getArrayBase()))
     and not
    a = b
}

predicate isSameExpr(Expr a, Expr b) {
    isSameArrayExpr(a, b) or
    isSameFieldAccess(a, b)
}

predicate isBufferPtrExpr(Expr expr){
    // is pointer and is not pointer of Structure
    isBufferPtrType(expr.getType())
    // and
    // not expr.getType().(PointerType).getBaseType() instanceof Struct
}

predicate isBufferPtrType(Type type){
    type instanceof PointerType and
    not type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType() instanceof Struct and
    not type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType() instanceof PointerType and
    not type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType() instanceof FunctionPointerType and
    not type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType() instanceof Enum
}

class BufferPtrType extends Type
{
    BufferPtrType() {
        isBufferPtrType(this)
    }
}

module MMIOFlow = TaintTracking::Global<MMIOFlowConfiguration>;
module TaintFlow = TaintTracking::Global<GeneralFlowConfiguration>;

class MMIOTracedExpr extends Expr
{
    MMIOTracedExpr() {
        this instanceof MMIODirectTracedExpr or
        this instanceof MMIODRTracedExpr or
        this instanceof MMIOITTracedExpr or
        this instanceof MMIODMATracedExpr
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
            not this.getEnclosingElement() instanceof MMIOTracedExpr and
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
        (this.getEnclosingElement() instanceof MMIOTracedExpr and result = "skip") or
        // (this.getEnclosingElement()  and result = "null") or
        // (exists( IfStmt ifstmt | ifstmt.getCondition() = this ) and result = "if") or
        (exists( WhileStmt whilestmt | whilestmt.getCondition() = this ) and result = "while") or
        (exists( DoStmt dostmt | dostmt.getCondition() = this ) and result = "do") or
        (exists( ForStmt forstmt | forstmt.getCondition() = this ) and result = "for") or
        (exists( ReturnStmt retstmt | retstmt.getExpr() = this ) and result = "return") 
        // (this.getEnclosingElement() instanceof Assignment and result = "assign")
    }
}

class MMIODirectTracedExpr extends Expr
{
    /**
     * exists PATH : this  <- MMIOSource
     */
    MMIODirectTracedExpr() {
        exists( Expr src, DataFlow::Node source, DataFlow::Node sink | 
            // sink.asExpr().getEnclosingFunction().getName() = "DMA_SetConfig" and
            sink.asExpr() = this and
            source.asExpr() = src and
            TaintFlow::flow(source, sink) and
            src instanceof MMIOFieldAccess and
            not isConstantExpr(this) and
            this != src 
        )
    }
}

class MMIODRTracedExpr extends Expr
{
    /**
     * exists PATH : this -> sink <- MMIOSource
     */
    MMIODRTracedExpr() {
        // exists( Expr snk, Expr src, DataFlow::Node source, DataFlow::Node sink, DataFlow::Node sourcensink1 | 
        //     sink.asExpr() = snk and
        //     source.asExpr() = src and
        //     MMIOFlow::flow(source, sink) and
        //     sourcensink1.asExpr() = this and
        //     TaintFlow::flow(sourcensink1, sink) and
        //     not isConstantExpr(this) and
        //     not TaintFlow::flow(source, sourcensink1) and
        //     this != src and
        //     // this != snk and
        //     sink.asExpr().getEnclosingFunction().getName() = "HAL_UART_Receive_IT"
        // )
        exists( MMIODirectTracedExpr snk, DataFlow::Node source, DataFlow::Node sink| 
            sink.asExpr() = snk and
            source.asExpr() = this and
            TaintFlow::flow(source, sink) and
            not isConstantExpr(this) and
            not this instanceof MMIODirectTracedExpr and
            not this instanceof MMIOFieldAccess //and
            //sink.asExpr().getEnclosingFunction().getName() = "UART_RxISR_16BIT"
        )
    }
}

class MMIOITTracedExpr extends Expr
{
    /**
     * exists PATH : this -> sinkrc (ISR) that -> sink <- MMIOSource
     */
    MMIOITTracedExpr() {
        // exists( Expr snk, Expr src, DataFlow::Node source, DataFlow::Node sink, DataFlow::Node sourcensink1, DataFlow::Node sourcensink, DataFlow::Node sinksrc, Expr snkrc, Expr that| 
        //     // this -> sinkrc
        //     sourcensink.asExpr() = this and
        //     sinksrc.asExpr() = snkrc and
        //     // that -> sink <- MMIOSource
        //     sink.asExpr() = snk and
        //     source.asExpr() = src and
        //     MMIOFlow::flow(source, sink) and
        //     sourcensink1.asExpr() = that and
        //     TaintFlow::flow(sourcensink1, sink) and
        //     // not isConstantExpr(that) and
        //     not isConstantExpr(this) and
        //     not TaintFlow::flow(source, sourcensink1) and
        //     that != src and
        //     // that = sinkrc
        //     isSameExpr(that, snkrc) and
        //     sink.asExpr().getEnclosingFunction().getName() = "UART_RxISR_16BIT"
        // )
        exists( MMIODRTracedExpr snk_mmio, Expr snk, DataFlow::Node source, DataFlow::Node sink| 
            // snk_mmio.getEnclosingFunction().getName() = "UART_RxISR_16BIT" and
            sink.asExpr() = snk and
            source.asExpr() = this and
            TaintFlow::flow(source, sink) and
            not isConstantExpr(this) and
            isSameExpr(snk_mmio, snk) and
            // not this instanceof MMIODRTracedExpr and
            not this instanceof MMIODirectTracedExpr and
            not this instanceof MMIOFieldAccess
            
        )
    }
}

class MMIODMATracedExpr extends Expr
{
    /**
     * exists: this(is buffer) -> MMIO
     */
    MMIODMATracedExpr() {
        exists( MMIOFieldAccess mmio, DataFlow::Node source, DataFlow::Node sink |
            // sink.asExpr().getEnclosingFunction().getName() = "DMA_SetConfig" and
            source.asExpr() = this and
            sink.asExpr() = mmio and
            isBufferPtrExpr(this) and
            TaintFlow::flow(source, sink) 
        )
    }
}

class MMIOBufferedFunction extends Function
{
    MMIOBufferedFunction() {
        exists( MMIOTracedBufferExpr expr |
            expr.getEnclosingFunction() = this
        )
    }
}

class MMIOTracedBufferExpr extends Expr
{
    /**
     * TODO: some of the results are incorrect:  (uint32_t)&huart->Instance->TDR
     * 
     * locate all the buffer traced to MMIO operation
     */
    MMIOTracedBufferExpr() {
        isBufferPtrExpr(this) and
        (   this instanceof MMIODMATracedExpr or
            this instanceof MMIOITTracedExpr or
            this instanceof MMIODirectTracedExpr or
            this instanceof MMIODRTracedExpr
        )
        
    }
}

class MMIOTracedBufferFunction extends Function
{
    MMIOTracedBufferFunction(){
        exists( MMIOTracedBufferExpr expr | 
            expr.getEnclosingFunction() = this
        )
    }
}

class InterestingMMIOExpr extends MMIOTracedExpr {
    InterestingMMIOExpr() {
        isInterestingMMIOBranchExpr(this) 
        // or
        // isInterestingMMIOReturnExpr(this)
    }
    string checkEnclosingStmt() {
        (this.getEnclosingElement*() instanceof IfStmt and result = "if") or
        (this.getEnclosingElement*() instanceof WhileStmt and result = "while") or
        (this.getEnclosingElement*() instanceof ReturnStmt and result = "return")
    }

    Function getf() {
        result = this.getEnclosingFunction()
    }
}

class InterestingMMIOFunctionContainType extends Type
{
    InterestingMMIOFunctionContainType() {
        (
            // Direct point to
            exists( Expr expr, InterestingMMIOFunction func | 
                expr.getEnclosingFunction() = func and
                expr.getType() = this 
            ) or
            // Pointer pointed to
            exists( Expr expr, InterestingMMIOFunction func, PointerType pt | 
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
        (this instanceof MMIOType and result = "driver") or
        (not this instanceof MMIOType and result = "other")
    }
}

class InterestingMMIOFunction extends Function {
    InterestingMMIOFunction() {
        isInterestingMMIOFunction(this)
    }
}

// 有危险操作的MMIO函数
predicate isInterestingMMIOFunction(Function func) {
    exists( InterestingMMIOExpr expr| 
        expr.getEnclosingFunction() = func )
    and
    // 添加限制：必须同时还含有MMIO操作（筛掉部分纯工具函数）
    exists( MMIOExpr expr |
        expr.getEnclosingFunction() = func)
}

// 可以直接被删掉的的MMIO函数
predicate isToRemoveMMIOFunction(Function func) {
    // 首先在interesting范围
    isInterestingMMIOFunction(func) and
    // 其次是没有参数和指针返回值的函数
    isVoidArgRetFunction(func) and
    // 最后没有除MMIO之外的全局变量操作
    not isGlobalVarAssignFunction(func)
}

// 递归扩散查找范围
predicate isRecToRemoveMMIOFunction(Function func) {
    isInterestingMMIOFunction(func) and
    // 不存在  函数调用
    not exists( FunctionCall call |
        call.getEnclosingFunction() = func and
        not isToRemoveMMIOFunction(func)
    )
}

// TODO 1. only rely on ToRemoveMMIOFunction
// TODO 2. potential IRQ handler (字符串匹配，MMIO相关分支数量)

predicate isInterestingMMIOBranchExpr(Expr expr) {
    expr instanceof MMIOTracedExpr and
    (
        // expr.getEnclosingElement*() instanceof IfStmt or
        expr.getEnclosingElement*() instanceof WhileStmt or
        expr.getEnclosingElement*() instanceof ForStmt
        or 
        expr.getEnclosingElement*() instanceof DoStmt 
        // or
        // expr.getEnclosingElement*() instanceof SwitchStmt or
        // expr.getEnclosingElement*() instanceof IfStmt
        // and
        // expr.getEnclosingFunction() instanceof DriverFunction
    )
}

// 输入参数无指针并且输出返回值是void的函数
predicate isVoidArgRetFunction(Function func) {
  // 检查函数的返回类型是否为 void
  func.getType().getName() = "void" and
//   // 检查函数的参数列表是否为空
//   func.getNumberOfParameters() = 0
  not exists( Parameter p |
    p = func.getAParameter() and 
    // 检查参数 p 的类型是否为指针类型
    p.getType() instanceof PointerType
  )
}

// TODO: 参数除MMIO指针外无其他指针
// TODO：存在指针参数但是只读

// TODO: 如果需要处理，判断是否存在可能死循环的部分（for, while）

// 有对全局变量进行赋值的函数
predicate isGlobalVarAssignFunction(Function func) {
    exists( Expr e, GlobalVariable gv | 
        e.getEnclosingFunction() = func and
        // 给全局变量赋值的操作
        e = gv.getAnAssignedValue()
    )
}

predicate isNoInfoOutFunction(Function func) {
    isVoidArgRetFunction(func) and 
    not isGlobalVarAssignFunction(func)
}

predicate isInterestingMMIOReturnExpr(Expr expr) {
    expr instanceof MMIOTracedExpr and
    expr.getEnclosingElement() instanceof ReturnStmt and
    expr.getEnclosingFunction() instanceof DriverFunction
}

predicate isInterestingMMIOBranchFunction(Function func) {
    exists( Expr expr | 
        expr.getEnclosingFunction() = func and
        isInterestingMMIOBranchExpr(expr)
    )
}

predicate isInterestingMMIOReturnFunction(Function func) {
    exists( Expr expr |
        expr.getEnclosingFunction() = func and
        isInterestingMMIOReturnExpr(expr)
    )
}

class InterestingMMIOBranchFunction extends Function{
    InterestingMMIOBranchFunction() {
        isInterestingMMIOBranchFunction(this)
    }
}

class InterestingMMIOReturnFunction extends Function{
    InterestingMMIOReturnFunction() {
        isInterestingMMIOReturnFunction(this)
    }
}

/**
 * source : Instance->RDR
 * sink : pdata16bits (sink of pData, sink of RDR)
 * 
 */
// from Expr snk, Expr src, DataFlow::Node source, DataFlow::Node sink, DataFlow::Node sourcensink1, DataFlow::Node sourcensink2, Expr srnk1, Expr srnk2
// where
//     sink.asExpr() = snk and
//     source.asExpr() = src and
//     MMIOFlow::flow(source, sink) and
//     sourcensink1.asExpr() = srnk1 and
//     TaintFlow::flow(sourcensink1, sink) and
//     not isConstantExpr(srnk1) and
//     // sourcensink2.asExpr() = srnk2 and
//     // isSameNode(sourcensink1, sourcensink2) and
//     srnk1 != src and
//     srnk1 != snk and
//     sink.asExpr().getEnclosingFunction().getName() = "HAL_UART_Receive"
// select src, src.getType(), src.getEnclosingFunction(),  srnk1, srnk1.getType(), srnk1.getEnclosingFunction()
// , srnk2, srnk2.getType(), srnk2.getEnclosingFunction()
// snk, snk.getType(), snk.getEnclosingFunction(),

// from MMIOITTracedExpr exp
// select exp, exp.getEnclosingFunction()

/**
 * Check if the Type is potentially BufferType
 * 
 */
// from Type type
// where     
//     type instanceof PointerType and
//     not type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType() instanceof Struct and
//     not type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType() instanceof PointerType and
//     not type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType() instanceof FunctionPointerType and
//     not type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType() instanceof Enum
// select type, type.(PointerType).getBaseType().getUnspecifiedType().getUnderlyingType()


/**
 * Find all the DMA Traced Buffer
 * 
 */
// from MMIOFieldAccess mmio, DataFlow::Node source, DataFlow::Node sink, VariableAccess exp, Parameter param
// where
//     source.asExpr() = exp and
//     sink.asExpr() = mmio and
//     // isBufferPtrExpr(exp) and
//     TaintFlow::flow(source, sink) and
//     // exp.getType() instanceof BufferPtrType and
//     source.asExpr().getEnclosingFunction().getName() = "DMA_SetConfig"
// select exp

/**
 * Some confusion of DataFlow
 * why hdma->Instance->CMAR = SrcAddress; and this has no flow
 * 
 * 
 */
// from Expr src, DataFlow::Node source, DataFlow::Node sink, Expr driver
// where
//     sink.asExpr() = driver and
//     source.asExpr() = src and
//     TaintFlow::flow(sink, source) and
//     src instanceof MMIOFieldAccess and
//     not isConstantExpr(driver) and
//     driver != src and
//     source.asExpr().getEnclosingFunction().getName() = "HAL_ETH_Transmit_IT"
// select src, driver,src.getType(), driver.getType()

// param, "DMA_SetConfig"

/**
 * 
 * 
 */

// select MMIOTra

/**
需要解决的问题：
1. 跟踪MMIO到上层
    a. 确认Driver数据结构（结构体），认为是与MMIO直接连接的结构体
    b. DMA我很疑惑(如何锁定DMA的Src和Dest的buffer，例如通过)

 * 
 */


/**
 * 网卡DMA描述符数据结构锁定测试
 * 
 * 
 * 
 */

// predicate isSameExpr() {
    
// }

// from MMIOFieldAccess mmio, ArrayExpr src, DataFlow::Node source, DataFlow::Node sink, ArrayExpr mmio_mem, CStyleCast cast, PointerType pt, Struct s
// where
//     // source.asExpr().getEnclosingFunction().getName() = "HAL_ETH_Transmit" and
//     // from PTR to MMIO
//     source.asExpr() = src and
//     sink.asExpr() = mmio and
//     TaintFlow::flow(source, sink) and
//     // isSameFieldAccess(src.getArrayBase(), mmio_mem.getArrayBase()) and
//     isSameExpr(src, mmio_mem) and
//     mmio_mem.getConversion() = cast and
//     cast.getActualType() = pt and
//     // 检查S是否是这个结构体或者这个typedef代表的结构体
//     ((pt.getBaseType() instanceof Struct and
//         s=pt.getBaseType()) or
//     (pt.getBaseType() instanceof TypedefType and
//         pt.getBaseType().(TypedefType).getBaseType() = s))
// select src, mmio,mmio.getEnclosingFunction(), src.getType(), mmio_mem, s//mmio_mem, mmio_mem.getType(), mmio_mem.getFullyConverted() //, cast



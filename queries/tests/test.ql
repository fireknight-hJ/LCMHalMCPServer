// import cpp
// import semmle.code.cpp.dataflow.new.DataFlow

// module LiteralToGethostbynameConfiguration implements DataFlow::ConfigSig {
//   predicate isSource(DataFlow::Node source) {
//     source.asIndirectExpr(1) instanceof StringLiteral
//   }

//   predicate isSink(DataFlow::Node sink) {
//     exists(FunctionCall fc |
//       sink.asIndirectExpr(1) = fc.getArgument(0) and
//       fc.getTarget().hasName("printf")
//     )
//   }
// }

// module LiteralToGethostbynameFlow = DataFlow::Global<LiteralToGethostbynameConfiguration>;

// from
//   StringLiteral sl, FunctionCall fc, DataFlow::Node source, DataFlow::Node sink
// where
//   source.asIndirectExpr(1) = sl and
//   sink.asIndirectExpr(1) = fc.getArgument(0) and
//   LiteralToGethostbynameFlow::flow(source, sink)
// select sl, fc



import semmle.code.cpp.dataflow.new.TaintTracking

predicate isConstantExpr(Expr e) {
    e instanceof Literal or
    e instanceof BinaryOperation and
    isConstantExpr(e.(BinaryOperation).getLeftOperand()) and
    isConstantExpr(e.(BinaryOperation).getRightOperand()) //or
    // e instanceof BinaryArithmeticOperation and
    //   isConstantExpr(e.(BinaryArithmeticOperation).getLeftOperand()) and
    //   isConstantExpr(e.(BinaryArithmeticOperation).getRightOperand())
}
predicate isConstantZeroExpr(Expr e) {
    e instanceof Literal and e.getValue() = "0"
}

predicate isMMIOStructure(Struct s) {
    // MMIO 直接访问模式
    exists( Expr ma, AssignExpr assign, PointerType pt |  
        // 确定ma是struct.member或者struct->member的形式
        // (ma instanceof PointerFieldAccess or ma instanceof ValueFieldAccess) and
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
        )

}
predicate isMMIOType(Type t) {
    (t instanceof Struct and isMMIOStructure(t.(Struct))) or 
    (t instanceof TypedefType and 
        t.(TypedefType).getBaseType() instanceof Struct and 
        isMMIOStructure(t.(TypedefType).getBaseType()))
}
predicate isMMIOExpr(FieldAccess ma) {
    exists( AssignExpr assign |
        // 确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
        ((ma instanceof PointerFieldAccess and isMMIOType(ma.getQualifier().getType().(PointerType).getBaseType())) or
        (ma instanceof ValueFieldAccess and isMMIOType(ma.getQualifier().getType()))) and
        // 绑定成员访问和赋值表达式
        (assign.getLValue() = ma or assign.getRValue() = ma)
    )
}

predicate isDriverType(Type t) {
    exists( FieldAccess ma|  
        // 确定ma是struct.member或者struct->member的形式
        (ma instanceof PointerFieldAccess or ma instanceof ValueFieldAccess) and
        // ma 指向的是一个MMIO类型
        isMMIOType(ma.getUnderlyingType().(PointerType).getBaseType()) and
        t = ma.getQualifier().getType().getUnderlyingType().(PointerType).getBaseType())

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
        // 确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
        (this instanceof PointerFieldAccess and isMMIOType(this.getQualifier().getType().(PointerType).getBaseType())) or
        (this instanceof ValueFieldAccess and isMMIOType(this.getQualifier().getType()))
    }
    // MMIOFieldAccess() {
    //     exists( AssignExpr assign |
    //         // 确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
    //         ((this instanceof PointerFieldAccess and isMMIOType(this.getQualifier().getType().(PointerType).getBaseType())) or
    //         (this instanceof ValueFieldAccess and isMMIOType(this.getQualifier().getType()))) and
    //         // 绑定成员访问和赋值表达式
    //         (assign.getLValue() = this or assign.getRValue() = this)
    //     )
    // }
}

class DriverFieldAccess extends FieldAccess
{
    DriverFieldAccess() {
        // 确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
        (this instanceof PointerFieldAccess and isDriverType(this.getQualifier().getType().(PointerType).getBaseType())) or
        (this instanceof ValueFieldAccess and isDriverType(this.getQualifier().getType()))
    }
    // MMIOFieldAccess() {
    //     exists( AssignExpr assign |
    //         // 确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
    //         ((this instanceof PointerFieldAccess and isMMIOType(this.getQualifier().getType().(PointerType).getBaseType())) or
    //         (this instanceof ValueFieldAccess and isMMIOType(this.getQualifier().getType()))) and
    //         // 绑定成员访问和赋值表达式
    //         (assign.getLValue() = this or assign.getRValue() = this)
    //     )
    // }
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
      source.asExpr() instanceof MMIOFieldAccess //and
    //   source.(MMIOFieldAccess).hasGlobalQualifiedName()
      // isMMIOExpr(source.asIndirectExpr(1))
      // isConstantZeroExpr(source.asIndirectExpr(1))
    }

    predicate isSink(DataFlow::Node sink) {
      // isMMIOStructure(sink.asExpr().getType())
      not sink.asExpr() instanceof MMIOFieldAccess or 
      sink.asParameter() instanceof Parameter//and
    //   sink.asExpr().(MMIOFieldAccess).toString().indexOf("DR") != -1
    //   sink.asConvertedExpr() instanceof MMIOFieldAccess
      
      // sink.asExpr().getType() instanceof Struct
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


predicate isMMIOFunction(Function func) {
    exists(MMIOFieldAccess fa | fa.getEnclosingFunction() = func)
}

predicate isDriverFunction(Function func) {
    exists(DriverFieldAccess fa | fa.getEnclosingFunction() = func) and not
    exists(MMIOFieldAccess fa | fa.getEnclosingFunction() = func)
}

class MMIOFunction extends Function
{
    MMIOFunction() {
        exists(MMIOFieldAccess fa | fa.getEnclosingFunction() = this)
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

from MMIOFieldAccess mmio, ArrayExpr src, DataFlow::Node source, DataFlow::Node sink, ArrayExpr mmio_mem, CStyleCast cast, PointerType pt, Struct s
where
    // source.asExpr().getEnclosingFunction().getName() = "HAL_ETH_Transmit" and
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
select src, mmio,mmio.getEnclosingFunction(), src.getType(), mmio_mem, s//mmio_mem, mmio_mem.getType(), mmio_mem.getFullyConverted() //, cast



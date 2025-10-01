/**
 * This is an automatically generated file
 * @name Hello world
 * @kind problem
 * @problem.severity warning
 * @id cpp/example/hello-world
 */

// import cpp

// from File f
// select f, "Hello, world!"

// from FunctionReferenceType t
// select t, t.getName()

import cpp

// util function
predicate isInlineFunction(Function func) {
    func.isInline() or
    func.getAnAttribute().getName() = "weak" or
    func.getAnAttribute().getName() = "always_inline"
}


// DriverFile
class DriverFile extends File
{
    DriverFile() {
        this.toString().matches(["%Driver%"]) 
        // or
        // this.getAnIncludedFile() instanceof DriverFile
        // this.getAnIncludedFile().toString().matches(["%Driver%"])
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
        this.getFile() instanceof DriverFile
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

// 3. 直接查Expr
class DriverFromExpr extends Expr
{
    DriverFromExpr(){
        this.getType() instanceof DriverType and
        this.getFile() instanceof NotDriverFile
    }
}

// 4. 查call调用的函数
class DriverFromFunctionCall extends FunctionCall
{
    DriverFromFunctionCall(){
        this.getTarget() instanceof DriverFunction and
        this.getFile() instanceof NotDriverFile
    }
}

class InlineAsmFunction extends Function
{
    InlineAsmFunction() {
        exists( AsmStmt asm | 
            isInlineFunction(this) and
            this = asm.getEnclosingFunction()

        ) or
        exists( InlineAsmFunction inlineAsmFun, FunctionCall call | 
            isInlineFunction(this) and
            call.getEnclosingFunction() = this and
            call.getTarget() = inlineAsmFun
        )
    }
}

// 7. class asm
class AsmFunction extends Function
{
    AsmFunction() {
        exists( AsmStmt asm | 
            // not isInlineFunction(this) and
            this = asm.getEnclosingFunction()
        ) 
        // or
        // exists( AsmStmt asm , Function inlineAsmFun, FunctionCall call| 
        //     isInlineFunction(inlineAsmFun) and
        //     inlineAsmFun = asm.getEnclosingFunction() and
        //     call.getEnclosingFunction() = this and
        //     call.getTarget() = inlineAsmFun
        // )
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

// 9. 查VariableCall


// 查找调用Driver中的函数的API（暂时忽略可能的间接调用）
// from FieldAccess fa
// where
// isMiddlewaresFunction(f) and
// fa.getType().getUnderlyingType().getUnspecifiedType() 


// var.getFile().
// select t, t.getUnderlyingType().getUnspecifiedType().getFile(), 

/**
 * 1. 查一遍函数参数的type有无来自Driver的
 * 2. 查一遍DeclStmt的target的type
 * 3. 查一遍VariableAccess
 * 4. 查一遍call的参数和call调用的函数（也要考虑下函数指针问题）
 * 5. 可能存在在Driver中是weak函数但是在新目录中被覆盖的情况
 * 6. 文件是否include了一个Driver的头文件
 * 7. 直接调用汇编指令的情况
 * 8. 全局变量的情况有没有来自其他
 */

// 2. 查DeclStmt
// from Function f, DeclStmt decl, DriverType type
// where
// f instanceof NotDriverFunction and
// decl.getADeclarationEntry().getType() = type and
// decl.getEnclosingFunction() = f
// select
// f//, decl, type

// 3. 查VariableAccess
// from Function f, Expr e
// where
// e.getEnclosingFunction() = f and
// e.getType() instanceof DriverType and
// e.getFile() instanceof NotDriverFile
// select 
// f



// 4. 查call调用的函数
// from Function f, FunctionCall call
// where 
// f instanceof NotDriverFunction and
// call.getTarget() instanceof DriverFunction and
// call.getEnclosingFunction() = f
// select f //, call, call.getTarget()

// 6. 文件是否include了一个Driver的头文件
// from File file, DriverUsingFile drv_file
// where
// file.getAnIncludedFile() = drv_file and
// not file instanceof DriverUsingFile and
// not file instanceof DriverFile
// select
// file, drv_file

// 7. 汇编指令使用收集
// from AsmStmt asm
// select asm, asm.getEnclosingFunction(), asm.getFile()

// 8. 全局变量来自Driver
// from GlobalVariable globalVar
// where globalVar.getType().getFile() instanceof DriverFile and
// globalVar.getFile() instanceof NotDriverFile
// select globalVar

// 9. 函数注册问题 (暂时跳过因为查了一遍暂时没碰到Driver函数注册到中间件中)
from FunctionAccess funcaccess, AssignExpr assign
where
    assign.getRValue() = funcaccess and
    funcaccess.getTarget() instanceof DriverFunction
    // // lock the Function Registration Operation
    // assign.getLValue() = fieldaccess and
    // // not assign.getRValue() = funcaccess and
    // // not assign.getRValue().isConstant() and
    // fieldaccess.getTarget().getType() instanceof FunctionPointerType
    // // Trace the Operation function
select assign, assign.getRValue(), funcaccess.getTarget(), assign.getEnclosingFunction()

// from VariableCall call
// where call.getFile() instanceof NotDriverFile
// select call.getExpr()
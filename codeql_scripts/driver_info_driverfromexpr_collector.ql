import DriverLocator

from DriverFromExpr expr
// where expr.getFile().getAbsolutePath().toString().matches("%LoRaMac.c")
// where
// expr.getEnclosingFunction().getName() = "inHandlerMode" //and
// expr.getEnclosingElement() instanceof DriverFromExpr
// not (expr.getEnclosingElement() instanceof ExprStmt or
// expr.getEnclosingElement() instanceof BinaryOperation or
// expr.getEnclosingElement() instanceof UnaryOperation or
// expr.getEnclosingElement() instanceof Assignment or
// expr.getEnclosingElement() instanceof ReturnStmt or
// expr.getEnclosingElement() instanceof Initializer or
// expr.getEnclosingElement() instanceof BinaryArithmeticOperation or
// expr.getEnclosingElement() instanceof Call or
// expr.getEnclosingElement() instanceof EnumConstantAccess or
// expr.getEnclosingElement() instanceof DriverFromExpr or
// expr.getEnclosingElement() instanceof IfStmt or
// expr.getEnclosingElement() instanceof ParenthesisExpr or
// expr.getEnclosingElement() instanceof ControlStructure
// )
// expr.getEnclosingElement() instanceof VariableDeclarationEntry)
// not ( expr instanceof Call or
//     expr instanceof Cast or
//     expr instanceof VariableAccess or
//     expr instanceof Assignment or
//     expr instanceof AggregateLiteral or
//     expr instanceof ArrayExpr or
//     expr instanceof BinaryOperation or
//     expr instanceof UnaryOperation or
//     expr instanceof Conversion
// )
// select expr, expr.toString(), expr.getEnclosingFunction().getName(), expr.getFile().getAbsolutePath().toString(), expr.getLocation().getStartLine(), expr.getEnclosingElement(), expr.checkExprType(), expr.checkEnclosingType()
select expr.toString(), expr.getEnclosingFunction().getName(), expr.getFile().getAbsolutePath().toString(), expr.getLocation().getStartLine(), expr.checkExprType(), expr.checkEnclosingType()
// 
//expr.getAQlClass(),
/*
(this.getEnclosingElement() instanceof ExprStmt and result = "stmt") or
(this.getEnclosingElement() instanceof BinaryOperation and result = "binary") or
(this.getEnclosingElement() instanceof UnaryOperation and result = "unary") or
(this.getEnclosingElement() instanceof Assignment and result = "assign") or
(this.getEnclosingElement() instanceof ReturnStmt and result = "return") or
(this.getEnclosingElement() instanceof Initializer and result = "init") or
(this.getEnclosingElement() instanceof BinaryArithmeticOperation and result = "arithmetic") or
(this.getEnclosingElement() instanceof Call and result = "call") or
(this.getEnclosingElement() instanceof EnumConstantAccess and result = "enum") //or
// (this.getEnclosingElement() instanceof Assignment and result = "assign")
*/
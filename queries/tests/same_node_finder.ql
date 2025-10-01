import cpp


predicate isSameExpr(FieldAccess a, FieldAccess b){
    // a.getTarget().getType() = b.getTarget().getType() and
    // a.getTarget().getName() = b.getTarget().getName() and not
    a.getTarget() = b.getTarget() and not
    a = b
}


from Expr a, Expr b
where
    isSameExpr(a, b) and
    b.getEnclosingFunction().getName() = "UART_RxISR_16BIT"
select a, a.getType(), a.getEnclosingFunction(),  b, b.getType(), b.getEnclosingFunction()
// snk, snk.getType(), snk.getEnclosingFunction(),

// HAL_UART_Receive_IT UART_RxISR_16BIT
import libraries.DriverLocator

from DriverFromDeclStmt decl
select decl, decl.toString(), decl.getEnclosingFunction().getName(), decl.getFile().getAbsolutePath().toString(), decl.getLocation().getStartLine()

/**
 * Decl 理论上均可以直接删除
 * 
 */
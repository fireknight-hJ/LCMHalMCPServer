
/**
 * @name Function Information with Calls and Structs
 * @description Retrieves all functions along with their file, location, called functions, and struct types used in the function.
 * @kind table
 */

import cpp

from Struct s, MemberVariable var, int number, string name, TypedefType typedef, TypedefType varTypedef, string typeName
where var.getDeclaringType() = s and
(
    // 优先从对应的typedef获取名字
    ( typedef.getBaseType() = s and name = typedef.getName()) or
    // struct 本身有名字
    ( s.getName() != "(unnamed class/struct/union)" and name = s.getName() )
) and
(
    // 优先从var的typedef获取名字
    (varTypedef.getBaseType() = var.getUnderlyingType().getUnspecifiedType() and
    typeName = varTypedef.getName()) or
    // var 本身有名字
    (var.getUnderlyingType().getUnspecifiedType().getName() != "(unnamed class/struct/union)" and typeName = var.getUnderlyingType().getUnspecifiedType().getName())
) and
    number = var.getLocation().getStartLine()
select 
    name, var.toString(), typeName.toString(), s.getFile().toString(), s.getLocation().getStartLine(), number
order by name, number

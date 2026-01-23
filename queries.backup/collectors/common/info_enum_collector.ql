import cpp

// 获取所有枚举类型及其值
// from Enum e, EnumConstant v
// where v.getDeclaringEnum()= e
// select  v.getName(), v.getValue()

from Enum e, EnumConstant v, string name, TypedefType typedef
where v.getDeclaringEnum()= e and
(
    // 优先从对应的typedef获取名字
    ( typedef.getBaseType() = e and name = typedef.getName()) or
    // struct 本身有名字
    ( e.getName() != "(unnamed class/struct/union)" and name = e.getName() )
) 
select 
    name, v.getName(), v.getValue(), e.getFile().toString(), e.getLocation().getStartLine()
order by name
// e.getName(),

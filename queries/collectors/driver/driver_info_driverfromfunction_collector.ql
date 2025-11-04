import libraries.DriverLocator

from DriverFromFunction func
select func.getName(), func.getFile().getAbsolutePath(), func.getLocation().getStartLine()

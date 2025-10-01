import libraries.DriverLocator

from DriverFromGlobalVariable globalVar
select globalVar.getName(), globalVar.getFile().getAbsolutePath().toString(), globalVar.getLocation().getStartLine()
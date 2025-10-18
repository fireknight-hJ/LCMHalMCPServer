from pydantic import BaseModel, Field
from typing import Literal

class DriverDirLocatorResponse(BaseModel):
    """Response of driver directory locate"""
    driver_dir_list: list[str]   = Field(description="List of paths of the driver (HAL_LIB_DRIVERS) directory")
    kernel_support_dir_list: list[str] = Field(description="List of paths of the kernel support (KERNEL_SUPPORT) directory")
    classify_reason: list[dict[str, str]] = Field(description="Explanation of the classification result for each directory, key is the directory name, value is the explanation")
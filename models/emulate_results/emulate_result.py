from pydantic import BaseModel, Field
from typing import Literal

class EmulateResult(BaseModel):
    """Emulate result infos"""
    std_err: str = Field(description="Standard error output of the emulate process")
    std_out: str = Field(description="Standard output of the emulate process")
    exit_code: int = Field(description="Exit code of the emulate process")
    success: bool = Field(description="Whether the emulate process was successful")
    reason: Literal["success", "failure"] = Field(description="Reason of the emulate process result")

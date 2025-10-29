from pydantic import BaseModel, Field
from typing import Literal

class BuildOutput(BaseModel):
    """Build output infos"""
    std_err: str = Field(description="Standard error output of the build process")
    std_out: str = Field(description="Standard output of the build process")
    exit_code: int = Field(description="Exit code of the build process")
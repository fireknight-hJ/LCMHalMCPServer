from pydantic import BaseModel, Field


class BuilderFixerResult(BaseModel):
    """Structured result from BuilderFixer sub-agent."""
    success: bool = Field(description="True if the attributed errors are resolved (build succeeds or the given error snippet no longer appears in stderr)")
    reason: str = Field(description="Explanation, e.g. 'Fixed: signature aligned' or 'Failed: the given error is not caused by this function'")
    modifications: str = Field(description="Summary of the change applied (e.g. 'Updated replacement for HAL_XXX to fix conflicting types')")

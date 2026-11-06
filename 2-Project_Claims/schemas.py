from pydantic import BaseModel, Field
from typing import Literal

class ClaimDecision(BaseModel):
    """A claims handler's decision on one claim."""

    rationale: str = Field(description="2-3 sentences to explain the decision along with the relevant section of the policy")
    decision: Literal["approve", "decline", "refer"]
    payout: float = Field(description="The amount to pay in US dollars, or 0 for a decline or a referral")
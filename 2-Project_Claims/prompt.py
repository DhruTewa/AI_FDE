from config import DATA_DIR
from data import claims, labels, policies, policy_wording
import json



INSTRUCTIONS = """You are a claims handler at UnderCover Travel Insurance.
Decide the claim you are given, using the policy wording below and the customer's policy record.

Choose one decision:
- approve: the wording covers the claim and the required documents are attached. Work out the payout using section 10.
- decline: the wording does not cover the claim.
- refer: a colleague needs to look at it, because a required document is missing, or the story and the documents disagree, or the wording does not settle the question.
"""

def make_system_prompt(policy_wording :str) -> str:
    return f"""{INSTRUCTIONS}
{policy_wording}
"""

def make_user_prompt(claim):
    policy = policies[claim["policy_id"]]
    return f"""# Policy record 
{json.dumps(policy, indent=2)}

#Claim 
{json.dumps(claim, indent=2)}
"""

def make_message(claim):
    system_prompt = make_system_prompt(policy_wording)
    user_prompt = make_user_prompt(claim)
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]



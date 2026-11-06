import json
from config import DATA_DIR

def load_json(file_name):
    """
    Load a JSON file and return its contents as a Python object.

    Args:
        file_name (str): The name of the JSON file to load. 

    Returns:
        dict: The contents of the JSON file as a Python dictionary.
    """
    file_path = DATA_DIR / file_name
    with open(file_path, "r") as f:
        return json.load(f)
    
    
def get_sample_data(tiny=False, held_out=False):
    """Return a list of claims, and the handlers' decisions on them keyed by claim id.

    held_out=True gives the twenty-five held-out claims in place of the queue.
    tiny=True keeps the five claims marked for the tiny version of either set.
    """
    claims = load_json("evals/held_out_claims.json" if held_out else "claims.json")
    decisions = load_json("evals/held_out_decisions.json" if held_out else "evals/decisions.json")
    if tiny:
        chosen = {decision["claim_id"] for decision in decisions if decision["tiny"]}
        claims = [claim for claim in claims if claim["claim_id"] in chosen]
        decisions = [decision for decision in decisions if decision["tiny"]]
    labels = {decision["claim_id"]: decision for decision in decisions}
    return claims, labels

TINY = False

claims, labels = get_sample_data(tiny=TINY)
policies = {policy["policy_id"]: policy for policy in load_json("policies.json")}
policy_wording = (DATA_DIR / "policy_wording.md").read_text(encoding="utf-8")

#print(f"{len(claims)} claims, {len(labels)} labels, {len(policies)} policies")
#print(f"The policy wording is {len(policy_wording.split()):,} words")
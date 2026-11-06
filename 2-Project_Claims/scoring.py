import pandas as pd
from llm_decider import decide

def is_right(answer, label):
    """True when the decision matches the handler's and the payout is within a dollar."""
    return answer["decision"] == label["decision"] and abs(answer["payout"] - label["payout"]) <= 1

def run(model, effort, claims, labels,client):
    """Run the model on the claims and compare against the labels."""
    results = []
    
    for claim in claims:
        answer = decide(client = client,claim = claim, model = model, effort = effort)
        label = labels[claim["claim_id"]]
        results.append({**answer, "difficulty": label["difficulty"], "right": is_right(answer, label)})
    right = sum(result["right"] for result in results)
    cost = sum(result["cost"] for result in results)
    seconds = sum(result["seconds"] for result in results)
    print(f"{model} at {effort}: {right} of {len(results)} right for ${cost:.4f} in {seconds:.0f} seconds")
    return results

def accuracy_by_difficulty(results: list[dict]) -> pd.DataFrame:
    """Count the claims each model and effort got right at each difficulty."""
    return pd.DataFrame(results).pivot_table(
        index=["model", "effort"], columns="difficulty", values="right", aggfunc="sum", sort=False
    )

def cost_summary(results: list[dict]) -> pd.DataFrame:
    """Total right answers, cost and time for each model and effort."""
    return pd.DataFrame(results).groupby(["model", "effort"], sort=False)[["right", "cost", "seconds"]].sum()

def show_misses(results: list[dict], labels: dict) -> None:
    """Print each wrong claim with the model's rationale next to the handler's reason."""
    for result in results:
        if not result["right"]:
            label = labels[result["claim_id"]]
            print(f"{result['claim_id']}, {label['difficulty']}: {result['decision']} ${result['payout']:,.2f}, "
                  f"handler said {label['decision']} ${label['payout']:,.2f}")
            print(f"  Model: {result['rationale']}")
            print(f"  Handler: {label['reason']}")
            print(f"  Tests: {label['tests']}\n")

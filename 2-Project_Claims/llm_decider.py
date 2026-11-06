import time
from schemas import ClaimDecision
from prompt import make_message
from data import claims
from llm_client import get_client
from config import get_key


def decide(client,claim, model,effort):
    start = time.time()
    response = client.chat.completions.parse(
        model=model,
        messages=make_message(claim),
        response_format=ClaimDecision,
        reasoning_effort=effort,
        extra_body={"provider": {"require_parameters": True}},
    )
    
    answer = response.choices[0].message.parsed
    return {
        "model": model,
        "effort": effort,
        "claim_id": claim["claim_id"],
        "technique": "LLM",
        "decision": answer.decision,
        "payout": answer.payout,
        "rationale": answer.rationale,
        "cost": response.usage.cost,
        "seconds": round(time.time() - start, 1)
    }

if __name__ == "__main__":
    first = decide(claim = claims[0], model = "openai/gpt-6-luna", effort = "low"
                   ,client = get_client(get_key())) 
    print(first)
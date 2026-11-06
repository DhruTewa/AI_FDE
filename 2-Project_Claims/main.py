from config import get_key
from llm_client import get_client
from scoring import run, accuracy_by_difficulty, cost_summary, show_misses
from data import claims, labels

def main():
    """Run the experiments, then print the results tables and the misses."""
    client = get_client(get_key())
    luna_low = run(model="openai/gpt-6-luna", effort="low", claims=claims, labels=labels, client=client)
    luna_medium = run(model="openai/gpt-6-luna", effort="medium", claims=claims, labels=labels, client=client)
    gemini = run(model="google/gemini-3.5-flash-lite", effort="low", claims=claims, labels=labels, client=client)

    scored = luna_low + luna_medium + gemini
    print(accuracy_by_difficulty(scored))
    print(cost_summary(scored))
    show_misses(luna_low, labels)

if __name__ == "__main__":
    main()

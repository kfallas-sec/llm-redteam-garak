import json

path = "reports/garak.be858972-033c-4101-9984-150455fcd2a8.report.jsonl"
found = 0
max_examples = 5

with open(path) as f:
    for line in f:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue

        if entry.get("entry_type") != "attempt":
            continue

        triggers = entry.get("notes", {}).get("triggers", [])
        outputs = entry.get("outputs", [])
        if not outputs or not triggers:
            continue

        output_text = outputs[0].get("text", "") or ""
        prompt_text = entry["prompt"]["turns"][0]["content"]["text"]

        if any(t.lower() in output_text.lower() for t in triggers):
            found += 1
            print(f"--- FAILURE EXAMPLE {found} ---")
            print("PROMPT:")
            print(prompt_text)
            print("\nMODEL OUTPUT:")
            print(output_text)
            print("=" * 60)
            if found >= max_examples:
                break

print(f"\nShown {found} failure example(s).")

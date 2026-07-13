# Tool Comparison Matrix — garak vs. Promptfoo

Target: llama3.2:1b (Ollama, local, CPU-only)

| Dimension | garak | Promptfoo |
|---|---|---|
| Setup effort | Low — CLI flags only, no config file | Medium — requires writing a YAML config with explicit prompts + assertions |
| Attack library | Large built-in library (256 prompts for `promptinject.HijackHateHumans` alone; hundreds of probes total) | None built-in — you write your own test cases |
| Runtime (this lab) | ~87 min (256 prompts, generations=1, CPU-only) | 37s (3 prompts) |
| Sample size tested | 256 | 3 |
| Reported attack success rate | 39.84% [95% CI: 33.59%, 45.70%] | 33.33% (1/3) — too small a sample for a confidence interval |
| Detection method | Built-in detectors per probe (substring match for this probe) | User-defined assertions (`not-icontains` used here) |
| Standards mapping | Built-in — auto-tags findings with OWASP LLM Top 10 and AVID | None built-in — mapped manually for this writeup |
| False positive observed | Yes — 1 example where correct behavior was flagged as FAIL due to substring matching | Not observed in this small sample, but same detection weakness applies (also substring-based) |
| Best suited for | Broad, automated vulnerability discovery at scale | Precise, repeatable regression testing of specific known attacks (e.g., in CI/CD) |

## Interpretation

The two tools answer different questions, and the numbers above are not
directly comparable as "which tool is more accurate" — they tested different
sample sizes against different specific prompts. garak's large built-in
library makes it better for *discovering* unknown weaknesses; Promptfoo's
config-driven approach makes it better for *verifying* a specific known
weakness stays fixed (or doesn't regress) over time, e.g. after a system
prompt change.

Both tools share the same core limitation observed in this lab: naive
substring-based detection can produce false positives when a model correctly
performs its task but happens to reference the trigger phrase as part of a
legitimate response (see garak run 1, example 5).

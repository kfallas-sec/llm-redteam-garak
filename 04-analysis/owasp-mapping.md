# OWASP Top 10 for LLM Applications (2025) — Findings Mapping

## LLM01: Prompt Injection

Both garak and Promptfoo findings in this lab fall under **LLM01 — Prompt
Injection**: instructions embedded within otherwise-legitimate input content
that cause the model to deviate from its intended task.

**Evidence:**
- garak: 39.84% attack success rate across 256 prompt variants using the
  "ignore previous instructions" pattern (`promptinject.HijackHateHumans`)
- Promptfoo: 1/3 test cases succeeded using the same pattern manually adapted
  to 3 different base tasks

**Severity (garak DEFCON scale):** DC-3 (medium)

**AVID tag:** S0403

## Secondary observation: detection reliability (not an OWASP category, but relevant)

Both tools' detection mechanisms rely on simple substring matching, which
produced at least one false positive in this lab (garak run 1, example 5).
This is not a vulnerability in the target model — it's a limitation of the
measurement tooling itself, and worth flagging separately in the writeup as
a methodology note rather than a security finding.

## Not tested in this lab

- LLM02 (Sensitive Information Disclosure) — not probed
- LLM06 (Excessive Agency) — not applicable, no agentic/tool-use setup tested
- LLM04 (Data and Model Poisoning) — out of scope, would require training-time access
- Multi-turn / conversational attacks (would require PyRIT or similar) — deferred, not covered in this iteration

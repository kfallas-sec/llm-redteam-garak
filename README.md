# LLM Red-Teaming Lab — garak / Promptfoo

Independent, personal security research project. Not affiliated with any employer.

## Goal

Adversarial testing of a locally-hosted LLM (served via Ollama) against
prompt injection, using two different red-teaming tools:

- [garak](https://github.com/NVIDIA/garak) — automated vulnerability scanning
- [Promptfoo](https://github.com/promptfoo/promptfoo) — eval/regression testing framework

Findings are mapped to the [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/).

## Status

✅ Complete — garak scan, Promptfoo comparison, analysis, and writeup all done.

[PyRIT](https://github.com/microsoft/PyRIT) (multi-turn, conversational red-teaming) was scoped out of this first iteration to keep it focused — noted as future work in the writeup.

## Key result

A 256-prompt garak scan against `llama3.2:1b` found a **39.84% prompt injection success rate** (95% CI: 33.59%–45.70%), replicated and compared against Promptfoo, with a methodology finding on detector false positives along the way.

**Full writeup:** [`writeup/llm-redteam-writeup.md`](writeup/llm-redteam-writeup.md)

## Environment

- Kali Linux (VirtualBox VM)
- Ollama running locally (CPU-only)
- Model tested: llama3.2:1b

## Structure

```
01-garak/       → garak scan, raw reports, commands, findings
02-promptfoo/   → Promptfoo eval config, findings, tool comparison
04-analysis/    → comparison matrix + OWASP LLM Top 10 mapping
writeup/        → final writeup, the one to read first
```

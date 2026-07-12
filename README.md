# LLM Red-Teaming Lab — garak / Promptfoo / PyRIT

Independent, personal security research project. Not affiliated with any employer.

## Goal

Adversarial testing of local LLMs (served via Ollama) against prompt injection,
jailbreaks, and other failure modes, using three tools:

- [garak](https://github.com/NVIDIA/garak) — automated vulnerability scanning
- [Promptfoo](https://github.com/promptfoo/promptfoo) — eval/regression testing framework
- [PyRIT](https://github.com/Azure/PyRIT) — orchestrated, multi-turn red-teaming

Findings are mapped to the [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/).

## Status

🔧 In progress — garak baseline scans underway.

## Environment

- Kali Linux (VirtualBox VM)
- Ollama running locally (CPU-only)
- Models tested: llama3.2:1b, llama3.2:3b

## Structure

See individual folders for tool-specific commands, raw reports, and notes.
Full findings and comparison will be in `writeup/`.

# garak — Notes & Findings

## Setup
- Target: llama3.2:1b via Ollama (local, CPU-only)
- Probe: promptinject.HijackHateHumans (256 prompt variants)
- Generations: 1 per prompt
- Environment: Kali Linux VM (VirtualBox), 4 vCPUs, 8GB RAM

## Result
- Attack success rate: 39.84% [95% CI: 33.59%, 45.70%]
- OWASP mapping: LLM01 (Prompt Injection)
- AVID tag: S0403
- garak DEFCON severity: DC-3 (medium)

## Key observation: model size vs. robustness
A 1B-parameter model shows a fairly high injection success rate. This lines up
with the general expectation that smaller models have weaker instruction-
following alignment and are easier to redirect with injected instructions.
Worth testing against llama3.2:3b or larger later for comparison (currently
CPU-only performance made larger models impractical for a full 256-prompt run).

## Key observation: detector limitation (false positive risk)
The detector (`promptinject.AttackRogueString`) does simple substring matching
for the trigger phrase ("I hate humans") in the model's output. One captured
example (see extract_failures.py output, example 5) shows the model correctly
resisting the injection — it analyzed the tweet's sentiment as instructed and
only *referenced* the phrase as part of that analysis — but was still scored
as a FAIL because the trigger string appeared in the output.

This means the reported 39.84% success rate is likely a slight overestimate.
A more accurate measurement would require manual review of borderline cases,
or a more semantically-aware detector. This is a real limitation of automated
LLM red-teaming tools worth discussing in the final writeup / tool comparison.

## Runtime notes
- First run attempt (llama3.2:3b, generations=2) was abandoned after the VM
  froze — traced to duplicate llama-server processes competing for CPU after
  a prior OOM crash. Resolved with `pkill -9 -f llama-server` + service restart.
- Switched to llama3.2:1b + generations=1 for a feasible runtime on CPU-only
  hardware. Full run: 5218.55s (~87 min).
- Lesson: for CPU-only labs, model size matters far more than vCPU count for
  practical runtime.

## Next steps
- [ ] Run a second probe (e.g. dan.Dan_11_0) once Promptfoo/PyRIT phases are done, for a broader comparison
- [ ] Compare against llama3.2:3b if time allows
- [ ] Move to Promptfoo — same target, similar attack vector, compare detection approach

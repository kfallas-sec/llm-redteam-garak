# garak — commands log

## Run 1 — 2026-07-12
```bash
garak --target_type ollama --target_name llama3.2:1b --probes promptinject.HijackHateHumans --generations 1
```

**Result:**
- Detector: `promptinject.AttackRogueString`
- FAIL ok on 154/256
- Attack success rate: 39.84% [95% CI: 33.59%, 45.70%]
- Runtime: 5218.55s (~87 min, CPU-only, no GPU)

**Environment notes:**
- Kali Linux VM (VirtualBox), 4 vCPUs, 8GB RAM
- Ollama, CPU-only inference
- Model: llama3.2:1b (switched from 3b due to CPU-only performance constraints)

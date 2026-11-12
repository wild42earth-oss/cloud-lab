# Group-Evolving Agents: Student-Scale Research Prototype

An offline prototype inspired by Weng et al. (2026), arXiv:2602.04837. This is a student-scale simulation using a finite set of known Python implementations and a small synthetic benchmark. It is **not** a reproduction of full GEA and does not claim to run SWE-bench Verified or Aider Polyglot.

## Research question
Under the same evaluation budget, does sharing validated problem-solving experience across a selected agent group improve performance over independent evolution?

## Quick start
Python 3.10+:

```bash
cd group-evolving-agents
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m gea.experiments.run --seeds 5 --generations 6
python -m gea.evaluation.plot_results
python -m unittest discover -s tests -v
```

No API key, paid service, or GPU is required. Results are written to `results/` as CSV and JSON; plots are saved under `results/figures/`.

## Components
- Six coding-agent strategy profiles.
- Twelve small Python function tasks, four test cases each.
- Independent-evolution baseline.
- Group evolution with performance/novelty parent-group scoring.
- Successful-experience validation and cross-agent sharing.
- Repeated seeded experiments, aggregate metrics, visualisation and unit tests.

## Research integrity and limitations
The benchmark is manually authored and synthetic. Agents choose among a finite portfolio of tested implementations; they do not generate code with an LLM. Behavioural novelty is approximated by distinct strategy labels, and experience is stored as successful category/strategy observations. Treat outcomes only as evidence about this prototype. Do not describe them as SWE-bench, Polyglot, or full GEA results. Details are in `docs/methodology.md`.

## Citation
Weng, Z., Antoniades, A., Nathani, D., Zhang, Z., Pu, X., & Wang, X. E. (2026). *Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing*. arXiv:2602.04837. https://arxiv.org/abs/2602.04837

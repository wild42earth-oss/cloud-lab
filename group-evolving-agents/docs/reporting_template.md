# Experimental report template (fill with generated artifacts)

Do not insert invented results. Generate results with:

```bash
python -m gea.experiments.run --seeds 5 --generations 6
python -m gea.evaluation.plot_results
```

Use `results/summary.csv`, `results/metrics.json`, and the graph in `results/figures/`.

## Implementation statement
The implementation is a student-scale, offline simulation using six fixed candidate-order policies and twelve manually authored Python tasks. It is not a large language model coding agent or a full reproduction of GEA.

## Dataset
- Source: locally authored `data/problems.json`.
- Size: 12 tasks × 4 tests each.
- Categories: arithmetic, predicate, comparison, iteration, string and list.
- Preprocessing: JSON parsing and schema validation; no external dataset download or train/test split.

## Experimental protocol
- Methods: independent evolution and selected-group experience sharing.
- Default population: six agents.
- Parent group: two agents.
- Parent score: 0.7 × mean performance + 0.3 × categorical strategy diversity.
- Shared record validation: all test cases for the problem must pass.
- Seeds: report the actual seed count passed to the runner.
- Generations: report the actual generation count.

## Results
Paste exact mean accuracy and standard deviation values from `results/summary.csv`. Include the generated graph. Describe differences as descriptive results from this finite synthetic benchmark; do not generalise to real software repositories.

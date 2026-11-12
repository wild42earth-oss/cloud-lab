import argparse,csv,json,statistics,platform
from pathlib import Path
from collections import defaultdict
from gea.evolution import run_method
from gea.dataset import load_problems

ROOT=Path(__file__).resolve().parents[2]
def run(seeds=5,generations=6,population_size=6):
    if seeds<1 or generations<1 or population_size<2: raise ValueError("Invalid experiment size")
    rows=[]
    for seed in range(seeds):
        for method in ("independent","group"):
            rows.extend(run_method(method,seed,generations,population_size))
    out=ROOT/"results";out.mkdir(exist_ok=True)
    with (out/"runs.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    buckets=defaultdict(list)
    for r in rows:buckets[(r["method"],r["generation"])].append(r["accuracy"])
    summary=[]
    for (method,gen),vals in sorted(buckets.items()):
        summary.append({"method":method,"generation":gen,"mean_accuracy":statistics.mean(vals),
                        "stdev_accuracy":statistics.stdev(vals) if len(vals)>1 else 0.0,
                        "agent_observations":len(vals)})
    with (out/"summary.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
    metrics={"python":platform.python_version(),"seeds":seeds,"generations":generations,
             "population_size":population_size,"dataset_size":len(load_problems()),
             "tasks":[p["id"] for p in load_problems()],
             "methods":["independent","group"],"summary":summary,
             "scope_note":"Finite deterministic strategy-portfolio simulation; not an LLM evaluation or full SWE-bench/Polyglot run."}
    (out/"metrics.json").write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    return summary
def main():
    p=argparse.ArgumentParser();p.add_argument("--seeds",type=int,default=5)
    p.add_argument("--generations",type=int,default=6);p.add_argument("--population-size",type=int,default=6)
    a=p.parse_args()
    for row in run(a.seeds,a.generations,a.population_size):print(row)
if __name__=="__main__":main()

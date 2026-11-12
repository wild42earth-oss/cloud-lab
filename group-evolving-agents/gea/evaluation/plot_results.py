import argparse,csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2]
def plot(input_path=None):
    source=Path(input_path) if input_path else ROOT/"results"/"summary.csv"
    with source.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    out=ROOT/"results"/"figures";out.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots()
    for method in sorted({r["method"] for r in rows}):
        data=sorted((r for r in rows if r["method"]==method),key=lambda r:int(r["generation"]))
        x=[int(r["generation"]) for r in data];y=[float(r["mean_accuracy"]) for r in data]
        e=[float(r["stdev_accuracy"]) for r in data]
        ax.errorbar(x,y,yerr=e,marker="o",capsize=3,label=method)
    ax.set(xlabel="Generation",ylabel="Mean agent task success rate",ylim=(0,1.05),title="Independent vs group evolution")
    ax.grid(alpha=.25);ax.legend();fig.tight_layout();fig.savefig(out/"success_rate.png",dpi=160);plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--input");plot(p.parse_args().input)

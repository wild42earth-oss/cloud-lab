import random
from gea.agents import make_population
from gea.dataset import load_problems
from gea.experience import ExperienceRecord, ExperienceStore
from gea.selection import select_parent_group
from gea.evaluation.runner import evaluate_agent

def run_method(method,seed,generations=6,population_size=6,parent_group_size=2,performance_weight=.7,novelty_weight=.3):
 if method not in {"independent","group"}: raise ValueError(method)
 rng=random.Random(seed); population=make_population(population_size,seed)
 store=ExperienceStore(); rows=[]; problems=load_problems()
 for gen in range(generations):
  ordered=problems[:]; rng.shuffle(ordered); evaluated=[]
  for agent in population:
   result=evaluate_agent(agent,ordered,store if method=="group" else None)
   agent.update(result["accuracy"]); evaluated.append((agent,result))
  parents=select_parent_group(population,parent_group_size,performance_weight,novelty_weight) if method=="group" else []
  for agent,result in evaluated:
   rows.append({"seed":seed,"method":method,"generation":gen,"agent_id":agent.agent_id,
                "strategy":agent.strategy,"accuracy":result["accuracy"],"solved":result["solved"],
                "total":result["total"],"unique_behaviours":len({a.strategy for a in population}),
                "experience_records":len(store.records),"selected_parent":agent in parents,
                "evaluations":(gen+1)*len(problems)})
  if method=="group":
   for agent,result in evaluated:
    if agent in parents:
     for r in result["records"]:
      if r["success"]:
       store.add_validated(ExperienceRecord(agent.agent_id,r["problem_id"],r["category"],r["strategy"],True,gen))
 return rows

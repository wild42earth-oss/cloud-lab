from gea.strategies import IMPLEMENTATIONS, candidate_order

def evaluate_function(fn, problem):
    for args, expected in problem["tests"]:
        try: actual=fn(*args)
        except Exception: return False
        if actual != expected or type(actual) is not type(expected): return False
    return True

def evaluate_agent(agent, problems, experience=None):
    solved=0; records=[]
    for p in problems:
        preference=experience.best_strategy_for(p["category"]) if experience else None
        chosen=None
        for strategy in candidate_order(agent.strategy, preference):
            if evaluate_function(IMPLEMENTATIONS[strategy],p):
                chosen=strategy; break
        ok=chosen is not None; solved+=int(ok)
        records.append({"problem_id":p["id"],"category":p["category"],"success":ok,"strategy":chosen})
    return {"solved":solved,"total":len(problems),"accuracy":solved/len(problems),"records":records}

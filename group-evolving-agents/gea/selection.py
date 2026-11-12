from itertools import combinations

def group_score(group, performance_weight=0.7, novelty_weight=0.3):
    if not group: return 0.0
    performance=sum(a.last_accuracy for a in group)/len(group)
    novelty=len({a.descriptor() for a in group})/len(group)
    return performance_weight*performance + novelty_weight*novelty

def select_parent_group(population,k=2,performance_weight=0.7,novelty_weight=0.3):
    if k<1 or k>len(population): raise ValueError("Invalid parent group size")
    groups=list(combinations(population,k))
    groups.sort(key=lambda g:(-group_score(g,performance_weight,novelty_weight),tuple(a.agent_id for a in g)))
    return list(groups[0])

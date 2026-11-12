from dataclasses import dataclass, asdict
from collections import defaultdict

@dataclass
class ExperienceRecord:
    source_agent: str
    problem_id: str
    category: str
    strategy: str
    passed: bool
    generation: int

class ExperienceStore:
    def __init__(self): self.records=[]
    def add_validated(self, record):
        # A record enters the shared store only after all tests for the task pass.
        if record.passed and record.strategy: self.records.append(record)
    def best_strategy_for(self, category):
        counts=defaultdict(int)
        for r in self.records:
            if r.category==category: counts[r.strategy]+=1
        if not counts: return None
        return sorted(counts.items(),key=lambda kv:(-kv[1],kv[0]))[0][0]
    def to_dicts(self): return [asdict(r) for r in self.records]

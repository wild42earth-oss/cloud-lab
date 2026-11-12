from dataclasses import dataclass, field

STRATEGIES = ["direct", "arithmetic_first", "string_first", "iteration_first", "comparison_first", "reverse"]

@dataclass
class Agent:
    agent_id: str
    strategy: str
    last_accuracy: float = 0.0
    history: list[float] = field(default_factory=list)

    def update(self, accuracy: float) -> None:
        self.last_accuracy = accuracy
        self.history.append(accuracy)

    def descriptor(self) -> str:
        return self.strategy

def make_population(size: int, seed: int) -> list[Agent]:
    return [Agent(f"A{i+1}", STRATEGIES[(i + seed) % len(STRATEGIES)]) for i in range(size)]

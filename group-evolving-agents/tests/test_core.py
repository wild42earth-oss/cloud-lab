import unittest
from gea.dataset import load_problems
from gea.strategies import IMPLEMENTATIONS
from gea.evaluation.runner import evaluate_function
from gea.agents import make_population
from gea.selection import select_parent_group

class TestCore(unittest.TestCase):
    def test_dataset_size(self): self.assertEqual(len(load_problems()),12)
    def test_reference_functions(self):
        for p in load_problems(): self.assertTrue(evaluate_function(IMPLEMENTATIONS[p["name"]],p),p["id"])
    def test_group_size(self):
        pop=make_population(6,0)
        for a in pop:a.last_accuracy=.5
        self.assertEqual(len(select_parent_group(pop,2)),2)
    def test_invalid_group_size(self):
        with self.assertRaises(ValueError):select_parent_group(make_population(3,0),4)
if __name__=="__main__":unittest.main()

"""Finite, deterministic strategy portfolio; no arbitrary generated code is executed."""
IMPLEMENTATIONS = {
    "add_two": lambda a,b: a+b,
    "is_even": lambda n: n%2==0,
    "square": lambda n: n*n,
    "maximum": lambda a,b: a if a>=b else b,
    "absolute": lambda n: abs(n),
    "factorial": lambda n: __import__("math").factorial(n),
    "count_vowels": lambda s: sum(c in "aeiou" for c in s),
    "reverse_string": lambda s: s[::-1],
    "sum_list": lambda xs: sum(xs),
    "is_palindrome": lambda s: s==s[::-1],
    "clamp": lambda x,lo,hi: max(lo,min(x,hi)),
    "fibonacci": lambda n: _fib(n),
}
def _fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

STRATEGIES = {
 "direct": list(IMPLEMENTATIONS),
 "arithmetic_first": ["add_two","square","absolute","factorial","fibonacci","is_even","maximum","clamp","sum_list","count_vowels","reverse_string","is_palindrome"],
 "string_first": ["count_vowels","reverse_string","is_palindrome","add_two","square","absolute","factorial","fibonacci","is_even","maximum","clamp","sum_list"],
 "iteration_first": ["factorial","fibonacci","sum_list","add_two","square","absolute","count_vowels","reverse_string","is_palindrome","is_even","maximum","clamp"],
 "comparison_first": ["maximum","clamp","is_even","absolute","add_two","square","factorial","fibonacci","count_vowels","reverse_string","is_palindrome","sum_list"],
 "reverse": list(reversed(IMPLEMENTATIONS)),
}
def candidate_order(strategy, shared_strategy=None):
    order=list(STRATEGIES[strategy])
    if shared_strategy in order:
        order.remove(shared_strategy); order.insert(0,shared_strategy)
    return order

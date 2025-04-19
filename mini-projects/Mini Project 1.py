from itertools import product

def satisfies_conditions(A, B, C, D, E, F):
    cond1 = (not A) or (not B)  # B is lying, A → ¬B
    cond2 = (not B) or (C and D)  # C and D are both truth-tellers, B → (C ∧ D)
    cond3 = (not C) or ((not A) or (not E))  # If A is truthful, then E is lying, C → (A → ¬E)
    cond4 = (not D) or (A == B)  # A and B are either both truthful or both lying, D → (A ↔ B)
    cond5 = (not E) or (sum([not A, not B, not C, not D, not F]) >= 2)  # E → At least 2 liars
    cond6 = (not F) or (D and not E)  # D is truthful, and Traveler E is lying, F → (D ∧ ¬E)
    
    at_least_one_truthful = any([A, B, C, D, E, F])
    at_least_one_liar = any([not A, not B, not C, not D, not E, not F])

    return all([cond1, cond2, cond3, cond4, cond5, cond6, at_least_one_truthful, at_least_one_liar])

#testing
test_cases = [
    (True, False, True, True, False, True),  #valid case
    (False, True, False, False, True, False),  #invalid case
]

print("Running predefined test cases:")
for truth_values in test_cases:
    A, B, C, D, E, F = truth_values
    result = satisfies_conditions(A, B, C, D, E, F)
    print(f"Test case: A={A}, B={B}, C={C}, D={D}, E={E}, F={F} -> {'Valid' if result else 'Invalid'}")

print("\nFinding all valid configurations:")

valid_configurations = []
for truth_values in product([True, False], repeat=6):
    A, B, C, D, E, F = truth_values
    if satisfies_conditions(A, B, C, D, E, F):
        valid_configurations.append(truth_values)
        print(f"Valid configuration: A={A}, B={B}, C={C}, D={D}, E={E}, F={F}")

print(f"\nTotal valid configurations found: {len(valid_configurations)}")

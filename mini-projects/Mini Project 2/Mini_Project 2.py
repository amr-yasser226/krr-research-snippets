def english_to_predicate(sentence):
    w = sentence.lower().split()
    if len(w) < 3:
        return "Invalid sentence: too short"

    quantifier, subject = w[0], w[1]

    try:
        are_index = w.index("are")
    except ValueError:
        return "Invalid sentence: missing 'are'"

    negated = False
    if are_index + 1 < len(w) and w[are_index + 1] == "not":
        negated = True
        prop_index = are_index + 2
    else:
        prop_index = are_index + 1

    if prop_index >= len(w):
        return "Invalid sentence: missing property"

    property_name = w[prop_index]
    singular_subject = subject.rstrip('s')
    subject_pred = f"is_{singular_subject}(x)"
    property_pred = f"is_{property_name}(x)"

    if quantifier in {"all", "every", "each"}:
        final_property = f"¬{property_pred}" if negated else property_pred
        return f"∀x ({subject_pred} → {final_property})"
    elif quantifier in {"some", "a", "an"}:
        final_property = f"¬{property_pred}" if negated else property_pred
        return f"∃x ({subject_pred} ∧ {final_property})"
    elif quantifier in {"no", "none"}:
        final_property = property_pred if negated else f"¬{property_pred}"
        return f"∀x ({subject_pred} → {final_property})"
    else:
        return f"Invalid quantifier: {quantifier}"


def predicate_to_english(logic):
    logic = logic.strip()

    if logic.startswith("∀x ("):
        quantifier = "∀x"
    elif logic.startswith("∃x ("):
        quantifier = "∃x"
    else:
        return "Invalid logic: must start with ∀x or ∃x"

    inner = logic[4:-1]

    if " → " in inner:
        operator = "→"
    elif " ∧ " in inner:
        operator = "∧"
    else:
        return "Invalid logic: missing → or ∧"

    try:
        subject_part, property_part = inner.split(f" {operator} ")
    except ValueError:
        return "Invalid logic: malformed expression"

    if not (subject_part.startswith("is_") and subject_part.endswith("(x)")):
        return "Invalid predicate: subject format incorrect"
    subject = subject_part[3:-3] + "s"

    if property_part.startswith("¬is_"):
        negated = True
        property_name = property_part[4:-3]
    elif property_part.startswith("is_") and property_part.endswith("(x)"):
        negated = False
        property_name = property_part[3:-3]
    else:
        return "Invalid predicate: property format incorrect"

    if quantifier == "∀x" and operator == "→":
        if negated:
            return f"no {subject} are {property_name}"
        return f"all {subject} are {property_name}"
    elif quantifier == "∃x" and operator == "∧":
        if negated:
            return f"some {subject} are not {property_name}"
        return f"some {subject} are {property_name}"
    else:
        return "Invalid combination of quantifier and operator"


def run_tests():
    test_cases = [
        ("All dinosaurs are extinct", "∀x (is_dinosaur(x) → is_extinct(x))"),
        ("Some animals are endangered", "∃x (is_animal(x) ∧ is_endangered(x))"),
        ("No dinosaurs are alive", "∀x (is_dinosaur(x) → ¬is_alive(x))"),
    ]

    print("English → Predicate Logic:")
    for sentence, expected in test_cases:
        result = english_to_predicate(sentence)
        print(f"Input:     {sentence}")
        print(f"Expected:  {expected}")
        print(f"Result:    {result}")
        print(f"Pass:      {result == expected}\n")

    print("Predicate Logic → English:")
    reverse_cases = [(logic, sentence.lower()) for sentence, logic in test_cases]
    for logic, expected in reverse_cases:
        result = predicate_to_english(logic)
        print(f"Input:     {logic}")
        print(f"Expected:  {expected}")
        print(f"Result:    {result}")
        print(f"Pass:      {result == expected}\n")
if __name__ == "__main__":
    run_tests()

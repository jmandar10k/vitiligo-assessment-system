
# 1) family scoring
def calculate_family_history_score(responses: dict) -> int:
    """
    responses: dictionary of question_key → selected_score
    """
    return sum(responses.values())

# 2) diet scoring
def calculate_food_score(responses: dict) -> int:

    total_score = 0

    def day_weight(days):
        return 1 if days == "1-3" else 2 if days == "3-5" else 3

    # 2x multiplier categories
    for category in ["sour_foods", "salty_foods", "processed_foods"]:
        total_score += sum(
            2 * day_weight(item["days"])
            for item in responses.get(category, [])
        )

    # incompatible combinations (stronger weight)
    total_score += sum(
        3 * (2 * day_weight(item["days"]))
        for item in responses.get("incompatible_combinations", [])
    )

    # lighter categories
    for category in ["food_habits", "oily_foods"]:
        total_score += sum(
            1 * day_weight(item["days"])
            for item in responses.get(category, [])
        )

    # meals before digestion
    if responses.get("meals_before_digestion") == "Yes":
        total_score += 6

    return total_score

# 3) lifestyle scoring
def calculate_lifestyle_score(responses: dict) -> int:
    return sum(responses.values())

# 4) psychological scoring
def calculate_psychological_score(responses: dict) -> int:
    return sum(responses.values())

# 5) environmental scoring
def calculate_environmental_score(responses: dict) -> int:
    return sum(responses.values())

# 6) combined score
def calculate_combined_score(section_scores: dict) -> int:
    """
    section_scores: dictionary containing all section scores
    """
    return sum(section_scores.values())
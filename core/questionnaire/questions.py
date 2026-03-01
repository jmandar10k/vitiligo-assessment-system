
# 1) Family question
FAMILY_HISTORY_QUESTIONS = {
    "family_history_skin_disorders": {
        "question": "Do you have a family history of vitiligo or other skin disorders?",
        "options": {0: "No (0)", 10: "Yes (10)"}
    },
    "family_history_depigmentation": {
        "question": "Has anyone in your family experienced depigmentation (loss of skin colour)?",
        "options": {0: "No (0)", 10: "Yes (10)"}
    },
    "personal_history_autoimmune": {
        "question": "Do you have a personal history of autoimmune diseases (e.g., thyroid disorders, diabetes)?",
        "options": {0: "No (0)", 10: "Yes (10)"}
    }
}


# FOOD SECTION DATA

FOOD_CATEGORIES = {
    "sour_foods": {
        "label": "Sour Foods",
        "items": [
            "Fermented products", "Pickles", "Bhelpuri", "Sour fruit juices",
            "Tomato sauce", "Excess intake of preserved foods", "Curd",
            "Buttermilk", "Lemon juice", "Vinegar", "Alcohol", "Cold drinks"
        ]
    },
    "salty_foods": {
        "label": "Salty Foods",
        "items": [
            "Salt predominant foods", "Papad", "Chips", "Namkeen", "Salt while eating"
        ]
    },
    "processed_foods": {
        "label": "Processed or Fried Foods",
        "items": [
            "Pizza", "Cheese mixed foods", "Bakery products", "Kidney beans",
            "Paneer", "Dosa", "Idli", "Vada", "Beef", "Pork",
            "Food prepared from flour", "Regular intake of meat products",
            "Intake of milk shakes", "Kheer"
        ]
    },
    "incompatible_combinations": {
        "label": "Incompatible Food Combinations",
        "items": [
            "Sprouted vegetables/grains with meat", "Milk with meat",
            "Jaggery with meat", "Milk or honey with leafy vegetables",
            "Curd with chicken", "Honey + hot water",
            "Seafood with milk", "Seafood with sweet",
            "Banana or fruit with milk", "Fruit salad",
            "Smoothies", "Milk with sour food",
            "Alcohol with or after milk", "Milk + rice + salt",
            "Curd + milk + rice"
        ]
    },
    "food_habits": {
        "label": "Food Habits",
        "items": [
            "Cold + hot food together",
            "Cold food soon after intake of hot food or vice versa",
            "Cold water with hot lunch/dinner",
            "Dessert along with hot food",
            "Using cold milk with hot samosa",
            "Spicy and pungent foods"
        ]
    },
    "oily_foods": {
        "label": "Oily Foods",
        "items": [
            "Excessively oily foods", "Biriyani", "Meat soups",
            "Sweets made of excess ghee, milk",
            "Food prepared with cheese & ghee"
        ]
    }
}

DAY_OPTIONS = ["1-3", "3-5", "5-7"]


# LIFESTYLE SECTION QUESTIONS

LIFESTYLE_QUESTIONS = {
    "suppress_urges": {
        "question": "Do you often suppress natural urges (e.g., urination, defecation, sneezing)?",
        "options": {0: "Never (0)", 1: "Rarely (1)", 3: "Sometimes (3)", 4: "Often (4)"}
    },
    "heavy_exercise": {
        "question": "How often do you engage in heavy physical exercise (Ati Vyayama)?",
        "options": {0: "Never (0)", 1: "Rarely (1)", 2: "Sometimes (2)", 3: "Often (3)"}
    },
    "sleep_after_meal": {
        "question": "Do you sleep immediately after having lunch/dinner?",
        "options": {0: "No (0)", 10: "Yes (10)"}
    },
    "day_sleep": {
        "question": "Do you often sleep during the day (Diwaswapan)?",
        "options": {0: "Never (0)", 2: "Rarely (2)", 4: "Sometimes (4)", 5: "Often (5)"}
    },
    "exhausted": {
        "question": "How often do you feel physically or mentally exhausted (Ati Santapa)?",
        "options": {0: "Never (0)", 1: "Rarely (1)", 2: "Sometimes (2)", 3: "Often (3)"}
    },
    "insomnia": {
        "question": "Do you suffer from insomnia or disturbed sleep at night?",
        "options": {0: "Never (0)", 1: "Rarely (1)", 3: "Sometimes (3)", 4: "Often (4)"}
    },
    "workout_after_meal": {
        "question": "Do you engage in heavy workouts at the gym soon after a heavy meal?",
        "options": {0: "No (0)", 5: "Yes (5)"}
    },
    "heavy_food_after_fasting": {
        "question": "Do you consume heavy and highly nutritive food soon after fasting?",
        "options": {0: "No (0)", 5: "Yes (5)"}
    },
    "cold_bath": {
        "question": "Do you bathe in cold water immediately after coming from a hot environment?",
        "options": {0: "Never (0)", 1: "Rarely (1)", 2: "Sometimes (2)", 3: "Often (3)"}
    },
    "eat_with_fear": {
        "question": "Do you eat when your mind is agitated by fear?",
        "options": {0: "Never (0)", 2: "Rarely (2)", 3: "Sometimes (3)", 4: "Often (4)"}
    }
}


# PSYCHOLOGICAL SECTION QUESTIONS

PSYCHOLOGICAL_QUESTIONS = {

    "stress_anxiety": {
        "question": "How often do you experience stress or anxiety?",
        "options": {
            0: "Never (0)",
            1: "Rarely (1)",
            2: "Sometimes (2)",
            3: "Often (3)",
            4: "Very Often (4)",
            5: "Always (5)"
        }
    },

    "grief_sadness": {
        "question": "Have you experienced prolonged grief or sadness recently?",
        "options": {0: "No (0)", 5: "Yes (5)"}
    },

    "anger_frustration": {
        "question": "How often do you feel anger or frustration?",
        "options": {
            0: "Never (0)",
            1: "Rarely (1)",
            2: "Sometimes (2)",
            3: "Often (3)",
            4: "Very Often (4)",
            5: "Always (5)"
        }
    },

    "mental_exhaustion": {
        "question": "Do you often feel mentally exhausted or overwhelmed?",
        "options": {
            0: "Never (0)",
            1: "Rarely (1)",
            2: "Sometimes (2)",
            3: "Often (3)"
        }
    },

    "guilt_distress": {
        "question": "Have you experienced guilt or moral distress recently?",
        "options": {0: "No (0)", 10: "Yes (10)"}
    },

    "conflicts": {
        "question": "Do you feel any pressure or unresolved conflicts in your family or work environment?",
        "options": {0: "No (0)", 5: "Yes (5)"}
    },

    "disrespect_authority": {
        "question": "Do you ever find yourself speaking disrespectfully or acting rudely towards elders or authority?",
        "options": {
            0: "Never (0)",
            3: "Rarely (3)",
            5: "Sometimes (5)",
            6: "Often (6)"
        }
    },

    "unethical_actions": {
        "question": "Have you ever justified or engaged in unethical actions for personal gain?",
        "options": {
            0: "Never (0)",
            3: "Rarely (3)",
            5: "Sometimes (5)",
            6: "Often (6)"
        }
    },

    "taken_something": {
        "question": "Have you ever taken something from someone for personal gain?",
        "options": {
            0: "Never (0)",
            3: "Rarely (3)",
            5: "Sometimes (5)",
            6: "Often (6)"
        }
    },

    "major_stress_events": {
        "question": "Have you experienced any major stressful life events recently?",
        "options": {0: "No (0)", 10: "Yes (10)"}
    }
}

# ENVIRONMENTAL SECTION QUESTIONS

ENVIRONMENTAL_QUESTIONS = {

    "chemical_exposure": {
        "question": "Are you exposed to chemicals or industrial pollutants at work?",
        "options": {
            0: "Never (0)",
            1: "Rarely (1)",
            2: "Sometimes (2)",
            3: "Often (3)"
        }
    },

    "polluted_area": {
        "question": "Do you live or work in a highly polluted area?",
        "options": {
            0: "No (0)",
            5: "Yes (5)"
        }
    },

    "harsh_chemicals": {
        "question": "Have you used any harsh chemicals or skin products in recent months?",
        "options": {
            0: "Never (0)",
            2: "Rarely (2)",
            3: "Sometimes (3)",
            4: "Often (4)"
        }
    },

    "sunlight_exposure": {
        "question": "Do you frequently spend long hours in direct sunlight without skin protection?",
        "options": {
            0: "Never (0)",
            2: "Rarely (2)",
            3: "Sometimes (3)",
            4: "Often (4)"
        }
    }
}


# PROGRESSION / LESION QUESTIONNAIRE

PROGRESSION_QUESTIONS = {

    "face": {
        "label": "Location of spot on face?",
        "options": [
            "at the openings(lips/nostrils/ears)",
            "on one side of the face",
            "on both sides of the face",
            "just one spot on face"
        ]
    },

    "hands_feet": {
        "label": "Location of spot on hands and feet?",
        "options": [
            "at the ends of limbs(fingers / toes)",
            "on both hands or feet",
            "on only one hand or feet"
        ]
    },

    "arms_legs": {
        "label": "Location of spot on arms and legs?",
        "options": [
            "on both arms or legs",
            "on only one arm or leg"
        ]
    },

    "whole_body": {
        "label": "Do you have around 80 to more than 80% body depigmentation?",
        "options": ["yes", "no"]
    }
}

# insights questions

PROGRESSION_INSIGHT_QUESTIONS = {

    "white_patches": {
        "label": "Do you have any white patches on your skin?",
        "options": ["Yes", "No"]
    },

    "patch_shape": {
        "label": "What is the shape of the white patches?",
        "options": ["Round", "Oval", "Irregular", "Not sure"]
    },

    "expanding_patches": {
        "label": "Are the white patches expanding over time?",
        "options": [
            "Yes, they are growing",
            "No, they have remained the same size",
            "Not sure"
        ]
    },

    "patch_duration": {
        "label": "How long have you had the white patches?",
        "options": [
            "Less than 3 months",
            "3-6 months",
            "6-12 months",
            "More than 1 year"
        ]
    },

    "sensations": {
        "label": "Do you experience sensations (itching/pain)?",
        "options": [
            "Yes, itching",
            "Yes, pain",
            "No, no sensations",
            "Not sure"
        ]
    },

    "color_change": {
        "label": "Have patches changed color over time?",
        "options": [
            "Yes, they have lightened over time",
            "No, they have remained the same color",
            "Not sure"
        ]
    },

    "new_patches": {
        "label": "Have new patches appeared recently?",
        "options": [
            "Yes, within the last 3 months",
            "No, no new patches",
            "Not sure"
        ]
    },

    "visibility_in_sunlight": {
        "label": "Are patches more noticeable in sunlight?",
        "options": [
            "Yes, they are more noticeable",
            "No, there’s no change",
            "Not sure"
        ]
    }
}
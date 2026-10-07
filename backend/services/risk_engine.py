CATEGORY_WEIGHTS = {
    "Profile Visibility": 10,
    "Personal Information": 15,
    "Location Exposure": 15,
    "Content Exposure": 10,
    "Connection Risk": 10,
    "Tagging Risk": 5,
    "Account Security": 15,
    "Third-Party Apps": 5,
    "Social Engineering": 10,
    "Digital Footprint": 5,
}


def classify_risk(score):
    if score <= 20:
        return "LOW"
    elif score <= 40:
        return "MODERATE"
    elif score <= 70:
        return "HIGH"
    else:
        return "CRITICAL"


def calculate_overall_score(category_scores):
    total = 0

    for category, weight in CATEGORY_WEIGHTS.items():
        category_score = category_scores.get(category, 0)
        total += category_score * (weight / 100)

    return round(total, 2)

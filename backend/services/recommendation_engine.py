RECOMMENDATIONS = {
    "Profile Visibility": "Review profile visibility and limit public information to what is necessary.",
    "Personal Information": "Hide unnecessary phone, email, birthday, workplace, education, and family information.",
    "Location Exposure": "Avoid sharing real-time locations, check-ins, travel plans, and identifiable frequent places.",
    "Content Exposure": "Review older posts and photos and remove unnecessary sensitive information.",
    "Connection Risk": "Verify unfamiliar connection requests and regularly review followers.",
    "Tagging Risk": "Enable tag review and restrict who can tag or mention you.",
    "Account Security": "Enable MFA, login alerts, and use unique passwords.",
    "Third-Party Apps": "Review connected applications and remove unused integrations.",
    "Social Engineering": "Avoid unexpected links, suspicious giveaways, and never share verification codes.",
    "Digital Footprint": "Review old public content and periodically review privacy settings."
}


def generate_recommendations(category_scores):
    recommendations = []

    for category, score in category_scores.items():
        if score >= 60 and category in RECOMMENDATIONS:
            recommendations.append({
                "category": category,
                "priority": "HIGH",
                "recommendation": RECOMMENDATIONS[category]
            })

    return recommendations

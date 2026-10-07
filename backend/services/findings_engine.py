def generate_privacy_findings(category_scores):
    findings = []

    if category_scores.get("Profile Visibility", 0) >= 60:
        findings.append("Profile visibility is high and may expose too much information.")

    if category_scores.get("Personal Information", 0) >= 60:
        findings.append("Personal information exposure should be reduced.")

    if category_scores.get("Location Exposure", 0) >= 60:
        findings.append("Location-sharing practices may reveal sensitive patterns.")

    if category_scores.get("Content Exposure", 0) >= 60:
        findings.append("Public content and older posts may reveal unnecessary information.")

    if category_scores.get("Connection Risk", 0) >= 60:
        findings.append("Unknown or unverified connections may increase privacy risk.")

    if category_scores.get("Tagging Risk", 0) >= 60:
        findings.append("Tagging controls should be reviewed.")

    if category_scores.get("Account Security", 0) >= 60:
        findings.append("Account-security controls need improvement.")

    if category_scores.get("Third-Party Apps", 0) >= 60:
        findings.append("Connected third-party applications should be reviewed.")

    if category_scores.get("Social Engineering", 0) >= 60:
        findings.append("Social-engineering exposure may be elevated.")

    if category_scores.get("Digital Footprint", 0) >= 60:
        findings.append("Older public content should be reviewed.")

    return findings

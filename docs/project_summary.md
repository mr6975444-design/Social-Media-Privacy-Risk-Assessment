# Social Media Privacy Risk Assessment Framework

## 1. Project Overview

The Social Media Privacy Risk Assessment Framework is a defensive cybersecurity and privacy-awareness platform designed to help users understand their potential social-media privacy exposure.

The system uses a 48-question questionnaire and converts responses into category-level privacy risk scores and an overall risk score.

## 2. Objectives

The main objectives are:

- Assess common social-media privacy risks.
- Identify areas with higher privacy exposure.
- Calculate a weighted overall privacy risk score.
- Provide personalized privacy recommendations.
- Improve user awareness of common privacy and security threats.
- Demonstrate defensive cybersecurity concepts.

## 3. Risk Categories

The assessment evaluates ten categories:

- Profile Visibility
- Personal Information
- Location Exposure
- Content Exposure
- Connection Risk
- Tagging Risk
- Account Security
- Third-Party Apps
- Social Engineering
- Digital Footprint

## 4. Risk Classification

The overall score ranges from 0 to 100.

| Score | Classification |
|---:|---|
| 0–20 | LOW |
| 21–40 | MODERATE |
| 41–70 | HIGH |
| 71–100 | CRITICAL |

A higher score indicates greater privacy exposure.

## 5. System Architecture

### Frontend

The frontend is implemented using HTML, CSS, and JavaScript.

It provides:

- Privacy questionnaire
- Response selection
- Assessment submission
- Risk score display
- Category score visualization
- Findings
- Recommendations
- Risk improvement simulation
- Reset functionality

### Backend

The backend is implemented using Python and FastAPI.

It provides:

- Health-check API
- Questionnaire API
- Assessment API
- Risk calculation
- Risk classification
- Privacy findings
- Recommendations

## 6. Testing

Automated tests were implemented using Pytest and FastAPI TestClient.

The test suite verifies:

- API health
- Questionnaire availability
- Low-risk assessment
- High-risk assessment
- Critical-risk assessment

Final test result:

**5 tests passed successfully.**

## 7. Privacy and Ethical Considerations

The framework follows a defensive and privacy-preserving approach.

It does not scrape social-media platforms, access private accounts, bypass privacy controls, collect passwords, access private messages, track individuals, or perform unauthorized profiling.

The system is intended for synthetic or voluntarily provided demonstration data.

## 8. Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- HTML
- CSS
- JavaScript
- Pytest
- ReportLab

## 9. Future Enhancements

Potential future improvements include:

- Database-based assessment history
- PDF report generation
- Synthetic dataset generation
- Dashboard analytics
- Additional security tests
- Accessibility improvements
- Deployment configuration
- Privacy-preserving analytics

## 10. Conclusion

The project demonstrates how a structured privacy questionnaire can be combined with weighted risk scoring, automated findings, and security recommendations to create a practical privacy-awareness tool.

The framework provides an educational example of defensive cybersecurity, privacy assessment, and secure software design.
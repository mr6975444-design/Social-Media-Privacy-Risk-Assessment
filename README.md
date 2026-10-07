# Social Media Privacy Risk Assessment Framework

A defensive cybersecurity and privacy-awareness platform that evaluates social-media privacy practices using a structured questionnaire.

## Project Objective

The system helps users understand potential privacy exposure through a self-assessment questionnaire.

It calculates:

- Overall Privacy Risk Score: 0–100
- Risk Level
- Category-level risk scores
- Privacy findings
- Personalized recommendations
- Privacy improvement simulation

## Risk Levels

| Score | Risk Level |
|---:|---|
| 0–20 | LOW |
| 21–40 | MODERATE |
| 41–70 | HIGH |
| 71–100 | CRITICAL |

## Privacy Risk Categories

1. Profile Visibility — 10%
2. Personal Information — 15%
3. Location Exposure — 15%
4. Content Exposure — 10%
5. Connection Risk — 10%
6. Tagging Risk — 5%
7. Account Security — 15%
8. Third-Party Apps — 5%
9. Social Engineering — 10%
10. Digital Footprint — 5%

**Total weight: 100%.**

## Main Features

- 48-question privacy questionnaire
- Yes / Sometimes / No responses
- Weighted risk calculation
- Risk-level classification
- Category score visualization
- Privacy findings
- Personalized recommendations
- Risk-level badge
- Privacy improvement simulator
- Reset assessment
- Automated API tests
- Synthetic/demo assessment data

## Technology Stack

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

### Testing

- Pytest
- FastAPI TestClient

## Project Structure

```text
Social-Media-Privacy-Risk-Assessment/
├── backend/
│   ├── app.py
│   ├── models/
│   │   └── questionnaire.py
│   └── services/
│       ├── risk_engine.py
│       ├── findings_engine.py
│       └── recommendation_engine.py
├── frontend/
│   └── index.html
├── tests/
│   └── test_api.py
├── data/
├── reports/
├── screenshots/
├── docs/
├── requirements.txt
└── README.md
```

## Running the Project

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the backend:

```bash
python3 -m uvicorn backend.app:app --reload --port 8001
```

Start the frontend in another terminal:

```bash
python3 -m http.server 5501 --directory frontend
```

Open the frontend at:

```text
http://127.0.0.1:5501
```

## API Endpoints

### Health Check

`GET /api/health`

### Questionnaire

`GET /api/questions`

Returns the 48-question privacy questionnaire.

### Assessment

`POST /api/assessment`

Calculates the overall privacy risk score, risk level, findings, and recommendations.

## Testing

Run:

```bash
PYTHONPATH=. pytest -q
```

The current automated test suite contains five tests covering:

- API health
- Questionnaire availability
- Low-risk assessment
- High-risk assessment
- Critical-risk assessment

## Privacy and Ethical Design

This project is designed as a defensive cybersecurity and privacy-awareness system.

It does not:

- scrape social-media platforms
- access private accounts
- bypass privacy controls
- collect passwords
- collect private messages
- enumerate real user accounts
- track real individuals
- perform unauthorized profiling

The questionnaire is intended for synthetic or voluntarily provided demonstration data.

## Security Awareness Recommendations

The framework can recommend practices such as:

- reviewing profile visibility
- reducing unnecessary personal information
- limiting location exposure
- reviewing old public content
- verifying unfamiliar connections
- enabling multi-factor authentication
- reviewing connected applications
- avoiding suspicious links
- protecting verification codes
- periodically reviewing privacy settings

## Future Enhancements

Possible future improvements include:

- SQLite assessment history
- PDF report generation
- CSV synthetic dataset
- dashboard charts
- additional automated tests
- accessibility improvements
- deployment configuration
- privacy-preserving analytics

## Disclaimer

This is an educational defensive cybersecurity and privacy-awareness project. Risk scores are indicative and should not be interpreted as a formal security audit.
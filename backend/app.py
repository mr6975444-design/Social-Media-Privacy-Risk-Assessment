from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.models.questionnaire import QUESTIONS
from backend.services.risk_engine import calculate_overall_score, classify_risk
from backend.services.findings_engine import generate_privacy_findings
from backend.services.recommendation_engine import generate_recommendations

app = FastAPI(
    title="Social Media Privacy Risk Assessment",
    description="A defensive cybersecurity and privacy risk assessment platform.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501", "http://localhost:5501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AssessmentRequest(BaseModel):
    category_scores: dict[str, float]


@app.get("/")
def home():
    return {
        "message": "Social Media Privacy Risk Assessment API is running!",
        "status": "success"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api/questions")
def get_questions():
    return {
        "total_questions": len(QUESTIONS),
        "questions": QUESTIONS
    }


@app.post("/api/assessment")
def create_assessment(data: AssessmentRequest):
    score = calculate_overall_score(data.category_scores)
    risk_level = classify_risk(score)
    findings = generate_privacy_findings(data.category_scores)
    recommendations = generate_recommendations(data.category_scores)

    return {
        "overall_score": score,
        "risk_level": risk_level,
        "category_scores": data.category_scores,
        "findings": findings,
        "recommendations": recommendations
    }

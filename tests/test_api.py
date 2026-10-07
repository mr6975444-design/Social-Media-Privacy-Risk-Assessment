from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_questions():
    response = client.get("/api/questions")

    assert response.status_code == 200

    data = response.json()

    assert data["total_questions"] == 48
    assert len(data["questions"]) == 48


def test_low_risk():
    scores = {
        "Profile Visibility": 10,
        "Personal Information": 10,
        "Location Exposure": 10,
        "Content Exposure": 10,
        "Connection Risk": 10,
        "Tagging Risk": 10,
        "Account Security": 10,
        "Third-Party Apps": 10,
        "Social Engineering": 10,
        "Digital Footprint": 10
    }

    response = client.post(
        "/api/assessment",
        json={"category_scores": scores}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["overall_score"] == 10
    assert data["risk_level"] == "LOW"


def test_high_risk():
    scores = {
        "Profile Visibility": 70,
        "Personal Information": 70,
        "Location Exposure": 70,
        "Content Exposure": 70,
        "Connection Risk": 70,
        "Tagging Risk": 70,
        "Account Security": 70,
        "Third-Party Apps": 70,
        "Social Engineering": 70,
        "Digital Footprint": 70
    }

    response = client.post(
        "/api/assessment",
        json={"category_scores": scores}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["overall_score"] == 70
    assert data["risk_level"] == "HIGH"


def test_critical_risk():
    scores = {
        "Profile Visibility": 100,
        "Personal Information": 100,
        "Location Exposure": 100,
        "Content Exposure": 100,
        "Connection Risk": 100,
        "Tagging Risk": 100,
        "Account Security": 100,
        "Third-Party Apps": 100,
        "Social Engineering": 100,
        "Digital Footprint": 100
    }

    response = client.post(
        "/api/assessment",
        json={"category_scores": scores}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["overall_score"] == 100
    assert data["risk_level"] == "CRITICAL"

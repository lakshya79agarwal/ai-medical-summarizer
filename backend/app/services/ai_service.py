from backend.app.config import settings


class AIService:
    """
    AI Orchestration Service
    """

    def generate_summary(self, medical_text: str):
        if not medical_text.strip():
            return {
                "status": "error",
                "message": "Medical text is empty."
            }

        return {
            "status": "success",
            "provider": "Gemini",
            "summary": "AI Summary Placeholder"
        }


ai_service = AIService()
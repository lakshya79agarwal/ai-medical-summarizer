class TranslationService:
    """
    Translation Service
    """

    def translate_to_hindi(self, text: str):
        if not text.strip():
            return {
                "status": "error",
                "message": "Text is empty."
            }

        return {
            "status": "success",
            "translated_text": text
        }


translation_service = TranslationService()
import os
from pathlib import Path
from dotenv import load_dotenv

# Project Root Directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")


class Config:
    """Application Configuration"""

    # Flask Secret Key
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

    # Database Configuration
    DB_FOLDER = BASE_DIR / "database"
    DATABASE_PATH = DB_FOLDER / "chatbot.db"

    # Gemini API Key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    @classmethod
    def validate_config(cls):
        """Validate application configuration"""

        # Create database folder if it doesn't exist
        cls.DB_FOLDER.mkdir(parents=True, exist_ok=True)

        # Check Gemini API Key
        if not cls.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is missing.\n"
                "Please add it to your .env file."
            )

        return True


print("Gemini API Key:", Config.GEMINI_API_KEY)
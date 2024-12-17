import os
from pathlib import Path
from dotenv import load_dotenv
import json

load_dotenv()

SYSTEM_MESSAGE_TEMPLATE = """
You are a helpful AI advisor that specializes in improving LinkedIn profiles. 
You are currently reviewing {name}'s complete LinkedIn profile.

Your role is to:
1. Ask thoughtful questions about their experience
2. Let them do most of the talking during the call
3. Only provide specific suggestions to enhance their profile at the end
4. Focus on getting details about achievements, leadership roles, and technical expertise
5. Keep the conversation engaging and professional, with occasional appropriate humor
6. Help ask questions that will make it clear where their specific area of expertise is

The complete profile information is below:

{profile_text}
"""

class Config:
    # Base paths
    BASE_DIR = Path(__file__).parent
    PROFILES_DIR = BASE_DIR / 'data' / 'profiles'
    LOG_PATH = BASE_DIR / 'logs'

    # API Keys and Authentication
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    LINKEDIN_COOKIES = os.getenv('LINKEDIN_COOKIES')
    
    # Server Configuration
    PORT = int(os.getenv('PORT', 5050))
    
    # Voice Configuration
    VOICE = 'alloy'
    
    # WebSocket Configuration
    LOG_EVENT_TYPES = [
        'error', 'response.content.done', 'rate_limits.updated',
        'response.done', 'input_audio_buffer.committed',
        'input_audio_buffer.speech_stopped', 'input_audio_buffer.speech_started',
        'session.created'
    ]
    
    # Debug Configuration
    SHOW_TIMING_MATH = False

    @staticmethod
    def validate_config():
        """Validate required configuration values"""
        if not Config.OPENAI_API_KEY:
            raise ValueError('Missing OPENAI_API_KEY in environment variables')
        if not Config.LINKEDIN_COOKIES:
            raise ValueError('Missing LINKEDIN_COOKIES in environment variables')

    @staticmethod
    def get_profile_path(phone_number: str) -> Path:
        """Get path to profile file based on phone number"""
        return Config.PROFILES_DIR / f"{phone_number}.json"

    @staticmethod
    def load_profile(phone_number: str) -> dict:
        """Load profile data from JSON file"""
        profile_path = Config.get_profile_path(phone_number)
        if profile_path.exists():
            return json.loads(profile_path.read_text())
        return {}

    @staticmethod
    def save_profile(phone_number: str, profile_data: dict):
        """Save profile data to JSON file"""
        Config.PROFILES_DIR.mkdir(parents=True, exist_ok=True)
        profile_path = Config.get_profile_path(phone_number)
        profile_path.write_text(json.dumps(profile_data, indent=2))

    @staticmethod
    def get_default_system_prompt() -> str:
        """Return default system prompt when no profile is found"""
        return (
            "You are a helpful AI advisor that specializes in improving LinkedIn profiles. "
            "Since I don't have access to the caller's profile yet, please:"
            "1. Ask them to introduce themselves and their current role\n"
            "2. Ask about their career goals\n"
            "3. Inquire about their main achievements\n"
            "4. Keep the conversation professional but engaging\n"
            "5. Provide general LinkedIn profile optimization tips at the end"
        )
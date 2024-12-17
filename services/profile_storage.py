from pathlib import Path
import json
from typing import Optional
from models.linkedin_profile import LinkedInProfile
from config import Config

class ProfileStorage:
    def __init__(self, profiles_dir: Path):
        self.profiles_dir = profiles_dir
        self.profiles_dir.mkdir(parents=True, exist_ok=True)
    
    def save_profile(self, phone: str, profile: LinkedInProfile):
        """Save profile to JSON file"""
        profile_path = self.profiles_dir / f"{phone}.json"
        profile_data = {
            "name": profile.name,
            "location": profile.location,
            "current_title": profile.current_title,
            "company": profile.company,
            "full_profile_text": profile.full_profile_text,
            "phone": profile.phone
        }
        profile_path.write_text(json.dumps(profile_data, indent=2))
    
    def load_profile(self, phone: str) -> Optional[LinkedInProfile]:
        """Load profile from JSON file"""
        profile_path = self.profiles_dir / f"{phone}.json"
        if not profile_path.exists():
            return None
            
        try:
            profile_data = json.loads(profile_path.read_text())
            return LinkedInProfile(**profile_data)
        except Exception as e:
            print(f"Error loading profile: {e}")
            return None
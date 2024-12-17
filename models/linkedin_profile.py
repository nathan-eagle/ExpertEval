from dataclasses import dataclass
from typing import List

@dataclass
class LinkedInProfile:
    name: str
    location: str
    current_title: str
    company: str
    full_profile_text: str
    phone: str = None
    
    def generate_greeting(self) -> str:
        return f"Hello. It looks like you are {self.name} from {self.location} who is currently the {self.current_title} of {self.company}. Is that correct?"

    def generate_system_prompt(self) -> str:
        return (
            f"You are a helpful AI advisor that specializes in improving LinkedIn profiles. "
            f"You are currently reviewing {self.name}'s complete LinkedIn profile below:\n\n"
            f"{self.full_profile_text}\n\n"
            "Your role is to ask thoughtful questions about their experience..."
        )
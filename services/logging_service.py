import json
from datetime import datetime
from pathlib import Path

class ConversationLogger:
    def __init__(self, log_path: str):
        self.log_path = Path(log_path)
        self.log_path.mkdir(exist_ok=True)
        self.log_file = self.log_path / "conversation_log.txt"
        
    def log_call_start(self, call_sid: str, caller_number: str, caller_name: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as f:
            f.write(f"\n{'='*80}\n")
            f.write(f"Call Start: {timestamp}\n")
            f.write(f"Call SID: {call_sid}\n")
            f.write(f"Caller: {caller_name} ({caller_number})\n")
            f.write(f"{'-'*80}\n")

    def log_conversation(self, call_sid: str, speaker: str, text: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {speaker}: {text}\n")
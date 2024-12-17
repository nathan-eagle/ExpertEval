# LinkedIn Advisor Bot

An AI-powered voice assistant that helps users improve their LinkedIn profiles through interactive phone conversations. Built with FastAPI, Twilio, and OpenAI's Realtime API with Advanced Voice Mode.

## Features

- Real-time voice conversations using OpenAI's Advanced Voice Mode
- LinkedIn profile lookup based on caller's phone number
- Personalized profile improvement suggestions
- Conversation logging and tracking
- Interruption handling for natural conversation flow
- Configurable voice settings and system prompts

## ToDos

- Transcribe the audio from the caller in the logs (currently only the assistant's audio is transcribed due to OpenAI Realtime API bug: input_audio_transcription)
- Realtime LinkedIn profile lookup and parsing

## Prerequisites

- Python 3.8+
- OpenAI API key
- Twilio account and phone number
- LinkedIn cookies for profile lookup
- ngrok (for local development)

## Installation

1. Clone the repository:

bash
git clone [repository-url]
cd linkedin-advisor-bot

bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

bash
pip install -r requirements.txt

bash
OPENAI_API_KEY=your_openai_api_key
PORT=5050

bash
uvicorn main:app --port 5050


2. For local development, use ngrok to create a public URL:

bash
ngrok http --url=your-ngrok-domain 5050


3. Configure your Twilio webhook URL to point to your server's `/incoming-call` endpoint

## Project Structure

- `main.py`: Main application file with FastAPI server and WebSocket handlers
- `services/`:
  - `linkedin_service.py`: LinkedIn profile lookup functionality
  - `logging_service.py`: Conversation logging utilities
- `config.py`: Configuration settings and environment variables
- `data/profiles/`: Storage for LinkedIn profile data

## Features in Detail

### Voice Interaction
- Real-time voice processing using OpenAI's GPT-4
- Natural conversation flow with interruption handling
- Configurable voice personality and characteristics

### LinkedIn Integration
- Automatic profile lookup based on caller's phone number
- Personalized conversation based on existing profile data
- Targeted improvement suggestions

### Logging and Monitoring
- Detailed conversation logging
- Call tracking and analytics
- Error handling and debugging capabilities

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Support

For support, please [create an issue](repository-issues-url) or contact nathan@media.mit.edu.
## Expertise Evaluation System

The system includes an automated expertise evaluation feature that conducts structured interviews to assess caller expertise across multiple domains.

#### Core Evaluation Features
- Automated expertise domain identification from LinkedIn profiles
- Real-time expertise assessment through structured interviews
- Multi-model evaluation pipeline using OpenAI and Anthropic models
- Dynamic question generation based on mid-interview analysis
- Comprehensive expertise scoring across multiple domains
- Detailed evaluation reports and interview transcripts
- Real-time voice conversations using OpenAI's Advanced Voice Mode
- LinkedIn profile lookup based on caller's phone number
- Interruption handling for natural conversation flow
- Configurable voice settings and system prompts

#### Interview Process
1. **Initial Assessment (2-3 minutes)**
   - LinkedIn profile analysis for potential expertise domains
   - Caller self-identification of expertise areas
   - Domain prioritization and interview focus determination

2. **Primary Interview (15 minutes)**
   - Structured questioning about primary expertise domain
   - Real-time response analysis and follow-up generation
   - Mid-interview evaluation at 7-minute mark
   - Dynamic question adjustment based on multi-model analysis

3. **Multi-Model Evaluation Pipeline**
   - Mid-interview transcript analysis by OpenAI GPT-4 and Anthropic Claude
   - Generation of targeted follow-up questions
   - Real-time integration of AI-generated questions
   - Cross-model consensus for expertise scoring

4. **Final Assessment**
   - Comprehensive domain expertise scoring (0-100)
   - Multi-domain expertise mapping
   - Detailed evaluation report generation
   - Interview transcript analysis and archival

#### Enhanced Features
- **Expertise Verification**: Integration with industry-standard frameworks and taxonomies
- **Comparative Analysis**: Benchmarking against industry averages and peer groups
- **Time-Series Tracking**: Support for multiple interviews over time to track expertise development
- **Domain-Specific Rubrics**: Customized evaluation criteria for different professional fields
- **Confidence Scoring**: Assessment of confidence levels in expertise claims
- **Skills Gap Analysis**: Identification of areas for potential improvement
- **Recommendation Engine**: Personalized suggestions for expertise development

#### Data Management
- Interview transcripts stored in `data/interviews/`
- Evaluation reports stored in `data/evaluations/`
- Structured JSON format for easy integration and analysis
- Historical tracking and version control
- Secure storage with encryption for sensitive information


#### Report Structure
json
{
"caller_id": "string",
"interview_date": "ISO-8601 timestamp",
"linkedin_profile": "profile_reference",
"primary_domain": "string",
"evaluation_scores": {
"domain_name": {
"score": 0-100,
"confidence": 0-100,
"key_strengths": ["string"],
"areas_for_improvement": ["string"]
}
},
"interview_metrics": {
"duration": "minutes",
"questions_asked": "number",
"response_quality": 0-100
},
"recommendations": ["string"],
"model_consensus": {
"gpt4_score": 0-100,
"claude_score": 0-100,
"final_score": 0-100
}
}

### Implementation Requirements
- OpenAI GPT-4 with function calling capabilities
- Anthropic Claude API integration
- Real-time transcript processing pipeline
- Secure data storage and encryption
- Interview timing management system
- Multi-model orchestration layer


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
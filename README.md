## Expertise Evaluation System

An automated expertise evaluation system that conducts structured interviews to assess caller expertise across multiple domains.

### Core Features
- Real-time voice conversations using OpenAI's Advanced Voice Mode
- LinkedIn profile lookup and analysis
- Natural conversation flow with interruption handling
- Multi-model evaluation using OpenAI GPT-4 and Anthropic Claude
- Dynamic question generation and expertise assessment
- Comprehensive domain scoring and detailed reports

### Interview Process
1. **Initial Assessment (2-3 minutes)**
   - LinkedIn profile analysis
   - Expertise domain identification
   - Interview focus determination

2. **Primary Interview (15 minutes)**
   - Structured domain-specific questioning
   - Real-time response analysis
   - Mid-interview evaluation and adjustment
   - Dynamic follow-up generation

3. **Evaluation Pipeline**
   - Multi-model analysis (GPT-4 and Claude)
   - Real-time expertise assessment
   - Cross-model consensus scoring
   - Continuous question optimization

4. **Final Assessment**
   - Domain expertise scoring (0-100)
   - Multi-domain expertise mapping
   - Detailed evaluation report
   - Interview transcript analysis

### Advanced Features
- **Expertise Verification**: Industry-standard framework integration
- **Comparative Analysis**: Peer group benchmarking
- **Time-Series Tracking**: Expertise development monitoring
- **Domain-Specific Rubrics**: Customized evaluation criteria
- **Confidence Scoring**: Claim verification system
- **Skills Gap Analysis**: Improvement area identification
- **Recommendation Engine**: Development suggestions

### Technical Implementation

#### Data Management
- Structured storage in `data/` directory:
  - `interviews/`: Conversation transcripts
  - `profiles/`: LinkedIn profile data
  - `evaluations/`: Assessment reports
- JSON format for integration
- Version control and historical tracking

#### Report Structure
```json
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
```


### Development Setup

#### Prerequisites
- Python 3.8+
- OpenAI API key
- Twilio account and phone number
- LinkedIn cookies for profile lookup
- ngrok (for local development)

#### Installation
1. Clone the repository:

```bash
git clone https://github.com/nathan-eagle/ExpertEval
cd ExpertEval
```   
2. Set up virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the server:
```bash
uvicorn main:app --port 5050
```
5. For local development:
```bash
ngrok http --url=your-ngrok-domain 5050
```
6. Configure Twilio webhook URL to point to your server's `/incoming-call` endpoint


6. Configure Twilio webhook URL to `/incoming-call` endpoint

### Project Structure
- `main.py`: FastAPI server and WebSocket handlers
- `services/`:
  - `linkedin_service.py`: Profile lookup
  - `logging_service.py`: Conversation logging
- `config.py`: Configuration settings

### Current ToDos
- Implement caller audio transcription
- Complete LinkedIn profile lookup integration
- Develop mid-interview evaluation system
- Implement multi-model scoring
- Add report generation
- Create testing override capabilities

### Support
For support, please [create an issue](repository-issues-url) or contact nathan@media.mit.edu.

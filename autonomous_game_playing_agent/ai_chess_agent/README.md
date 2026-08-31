                      # Awesome-automation-tools
# ♜ Agent White vs Agent Black: Chess Game

An AI chess game where two agents play against each other using Autogen in a Streamlit app. Built with move validation and game state management.

## Features

### Multi-Agent Architecture
- Player White: OpenAI-powered strategic decision maker
- Player Black: OpenAI-powered tactical opponent
- Board Proxy: Validation agent for move legality and game state

### Safety & Validation
- Move verification system
- Illegal move prevention
- Real-time board state monitoring
- Secure game progression control

### Strategic Gameplay
- AI-powered position evaluation
- Tactical analysis
- Dynamic strategy adaptation
- Complete chess ruleset implementation

## Getting Started

1. Clone the repository
```bash
git clone https://github.com/coboat/Awesome-automation-tools.git
cd Awesome_ai_agents/autonomous_game_playing_agent/ai_chess_agent
```

2. Install the required dependencies
```bash
pip install -r requirements.txt
```

3. Get your OpenAI API key
- Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.

4. Run the Streamlit app
```bash
streamlit run ai_chess_agent.py
```
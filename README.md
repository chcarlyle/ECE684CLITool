# Sports Assistant CLI

A simple command-line sports question-answering tool using Groq's free API

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get a free Groq API key:**
   - https://console.groq.com
   - Sign up
   - Generate an API key

3. **Set your API key:**
   ```bash
   export GROQ_API_KEY='your-api-key-here'
   ```

## Usage

Run the script:
```bash
python sports_ai.py
```

Ask any sports-related questions:
- "Who won the last Super Bowl?"
- "Explain the offside rule in soccer"
- "What are Michael Jordan's career stats?"
- "Tell me about the history of basketball"

Type `quit` or `exit` to leave.

## Features

- Uses Groq's free Llama 3.3 70B model
- Interactive CLI
- No rate limiting concerns with free tier

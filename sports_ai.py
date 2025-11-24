#!/usr/bin/env python3
"""
Sports Assistant CLI - A simple sports Q&A tool using Groq's free LLM API
"""

import os
import sys
from groq import Groq

def get_api_key():
    """Get API key from environment variable"""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY environment variable not set")
        print("\nTo get a free API key:")
        print("1. Visit https://console.groq.com")
        print("2. Sign up for a free account")
        print("3. Generate an API key")
        print("4. Set it: export GROQ_API_KEY='your-key-here'")
        sys.exit(1)
    return api_key

def ask_sports_question(client, question):
    """Send a sports question to the LLM"""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a knowledgeable sports assistant. Answer questions about "
                        "sports including rules, history, statistics, players, teams, and current events. "
                        "Keep responses concise but informative. Use emojis occasionally for fun. You're personality is similar to Pat McAfee."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.75,
            max_tokens=500,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Initialize Groq client
    api_key = get_api_key()
    client = Groq(api_key=api_key)

    print("Ask me anything about sports! (Type 'quit' or 'exit' to leave)\n")

    while True:
        try:
            # Get user input
            question = input("You: ").strip()

            # Check for exit commands
            if question.lower() in ['quit', 'exit', 'q']:
                print("\nThanks for using AI Sports Assistant! See you next time!")
                break
            # Skip empty questions
            if not question:
                continue
            # Get and display response
            print("\nAI Assistant: ", end="", flush=True)
            response = ask_sports_question(client, question)
            print(response)
            print()

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}\n")

if __name__ == "__main__":
    main()

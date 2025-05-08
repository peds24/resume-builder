import os
import anthropic
from dotenv import load_dotenv

def claudeTest(question):
    
    load_dotenv()
    
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1000,
        temperature=1,
        # system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    }
                ]
            }
        ]
    )
    print(message.content[0].text)
    
def main():
    print("Claude API Test - Enter 'exit' to quit")
    print("-" * 50)
    while True:
        question = input("\nEnter your question: ")
        
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        
        print("\nAsking Claude...\n")
        claudeTest(question)

if __name__ == "__main__":
    main()
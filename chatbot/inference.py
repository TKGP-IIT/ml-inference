from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

def Chatbot_Response(user_input):
    client = InferenceClient(
        provider="together",
        api_key=os.getenv("HF_TOKEN")
    )

    print("Chatbot initialized")

    messages = [{"role": "user", "content": user_input}]

    try:
        completion = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.3", 
            messages=messages,
            max_tokens=500
        )

        response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": response})

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        response = "Sorry, an error occurred while processing your request."

    return {"response": response}

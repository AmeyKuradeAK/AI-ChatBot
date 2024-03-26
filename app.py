import sys
from configparser import ConfigParser
from chatbot import ChatBot

def main():
    config = ConfigParser()
    config.read('Credintial.ini')
    api_key = config['gemini_ai']['API_KEY']
    
    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conservation()
    # chatbot.clear_conservation()
    
    print("Welcome to the Oculus Chatbot CLI. Type 'quite' to exit.")
    
    # print ('{0}: {1}'.format(chatbot.Oculus, chatbot.respondToUser()))
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Exiting ChatBot CLI...")
            break
        
        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error: {e}")
            
main()
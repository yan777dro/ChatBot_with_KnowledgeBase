from utils import load_knowledge_base, get_answer

def main():
    # Load the knowledge base
    knowledge_base = load_knowledge_base('knowledge_base/data.json')

    print("Hello! Ask me a question or type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = get_answer(user_input, knowledge_base)
        print("Bot:", response)

if __name__ == '__main__':
    main()

#to run the app:  python main.py

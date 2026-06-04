import random
print("hello,I'm your simple rule based chatbot, how can I help you?")
print("type 'exit' to end this conversation")

def chatbot(user):
    user=user.lower()
    if any(word in user for word in["hi","hello","hey"]):
        return random.choice(["hello! how can I help you?","Hi there! what can i do for you?","hey! nice to talk to you"])
    elif "how are you" in user:
        return random.choice(["I'm doing well, thank you!","I'm good, how about you?","I'm fine, thanks for asking!"])
    elif any(word in user for word in ["your name","who are you","what is your name"]):
        return "I'm a simple rule-based chatbot built using python. I don't have a name, but you can call me however you want!"
    elif"help" in user:
        return "you can talk to me about greetings,ask my name !"
    elif "thank" in user:
        return random.choice(["you're welcome!","happy to help!","no problem!","always here to help!"])
    elif"what can you do"in user:
        return " i can respond to simple messages using rule based logic"
    elif "joke" in user:
        return"why did the computer get cold? because it left its windows open!"
    else:
        return random.choice(["can u rephrase that?", "I'm still learning , try something simpler.","sorry, I don't understand that. Can you try asking something else?"])
    
while True:
        
        user_input= input("You:")
        if user_input.lower() == "exit":
            print("Goodbye! have a nice day!")
            break
        response= chatbot(user_input)
        print("bot:",response)

        

import re
from flask import Flask, render_template, request
from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ron Obvious")

app = Flask(__name__, template_folder='template')

# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")

# conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome.",
#     "Toi la Thu",
#     "Xin chao Thu, toi la chatbot."
# ]

# trainer = ListTrainer(chatbot)

# trainer.train(conversation)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # return str(english_bot.get_response(userText))
    print('response' + str(chatbot.get_response(userText)))
    if "/" in userText:
        conversation = userText.split("/")
        training(conversation)
        return "try again!"
    return str(chatbot.get_response(userText))

def training(conversation):
    print("Tranning for chatbot")
    trainer = ListTrainer(chatbot)
    trainer.train(conversation)


#training
if __name__ == "__main__":
    app.run()
# Install ChatterBot library
# pip install chatterbot

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Create a ChatBot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the Chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

#Train the chatbot on the english language corpus data
trainer.train('chatterbot.corpus.english')

#you can also provide your custom training data
#trainer.train([
#  'How are you?',
#  'I am good, Thank You!',
#  'Whats your Name?',
#  'My name is MyBot.'
#])

# Get a response from the Chatbot
response = chatbot.get_response('Hello, how are you?')

#print the response
print (response)



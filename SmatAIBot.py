#import libraries
from newspaper import Article
import random
import string 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import speech_recognition as sr
import pyttsx3
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#To create voice for bot to speak with result or speak with user
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',170)

def speak(audio):
    print(f" {audio}")
    engine.say(audio)
    engine.runAndWait()
nltk.download('punkt', quiet=True) # Download the punkt package
#Get the article URL
article = Article('https://www.javatpoint.com/c-programming-language-tutorial')
article.download() #Download the article
article.parse() #Parse the article
article.nlp() #Apply Natural Language Processing (NLP)
corpus = article.text #Store the article text into corpus
print(corpus)
#Tokenization
text = corpus
sent_tokens = nltk.sent_tokenize(text)# txt to a list of sentences 
#Print the list of sentences
print(sent_tokens)
#Return the indices of the values from an array in sorted order by the values
def index_sort(list_var):
  length = len(list_var)
  list_index = list(range(0, length))
  x  = list_var
  for i in range(length):
    for j in range(length):
      if x[list_index[i]] > x[list_index[j]]:
        temp = list_index[i]
        list_index[i] = list_index[j]
        list_index[j] = temp
        return list_index
# Generate the response
def bot_response(user_input):
    user_input = user_input.lower() #Convert the users input to all lowercase letters
    sentence_list.append(user_input) #Append the users response to the list of sentence tokens
    bot_response='' #Create an empty response for the bot
    cm = CountVectorizer().fit_transform(sentence_list) #Create the count matrix
    similarity_scores = cosine_similarity(cm[-1], cm) #Get the similarity scores to the users input
    flatten = similarity_scores.flatten() #Reduce the dimensionality of the similarity scores
    index = index_sort(flatten) #Sort the index from 
    index = index[1:] #Get all of the similarity scores except the first (the query itself)
    response_flag=0 #Set a flag letting us know if the text contains a similarity score greater than 0.0
    #Loop the through the index list and get the 'n' number of sentences as the response
    j = 0
    for i in range(0, len(index)):
      if flatten[index[i]] > 0.0:
        bot_response = bot_response+' '+sentence_list[index[i]]
        response_flag = 1
        j = j+1
      if j > 2:
        break  
    #if no sentence contains a similarity score greater than 0.0 then print 'I apologize, I don't understand'
    if(response_flag==0):
        bot_response = bot_response+' '+"I apologize, I don't understand."
        sentence_list.remove(user_input) #Remove the users response from the sentence tokens
       
    return bot_response
  
  #Start the chat
print("Boss What i can do for you")
exit_list = ['exit', 'see you later','see u later','bye', 'quit', 'break']
while(True):
    user_input = input()
    if(user_input.lower() in exit_list):
      print(" Chat with you later !")
      break
    else:
      if(greeting_response(user_input)!= None):
        print(" "+greeting_response(user_input))
      else:
        print(" "+bot_response(user_input))

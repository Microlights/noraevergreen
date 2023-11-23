import re  
import nltk  
from nltk.corpus import movie_reviews  
  
class ChatBot:  
    def __init__(self):  
        self.responses = []  
        self.pattern = r"@Bot: (\w+)"  
        self.nltk.download('punkt')  
        self.nltk.download('movie_reviews')  
  
    def listen(self):  
        message = input("@Me: ")  
        self.responses.append(message)  
  
        match = re.search(self.pattern, message)  
        if match:  
            keyword = match.group(1)  
            self.process_keyword(keyword)  
  
    def process_keyword(self, keyword):  
        sentences = movie_reviews.sents()  
        sentences = [sent.lower() for sent in sentences]  
        sentences = [re.sub(r'\W+|\d+|\xa0', '', sent) for sent in sentences]  
        sentences = [re.sub(r'\s+', ' ', sent).strip() for sent in sentences]  
        sentences = [sent for sent in sentences if keyword in sent]  
        response = random.choice(sentences)  
        print(f"@Bot: {response}")  
  
if __name__ == "__main__":  
    bot = ChatBot()  
    while True:  
        bot.listen()

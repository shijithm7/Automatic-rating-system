
from textblob import TextBlob
import re



review=str(input("Enter your review : "))

def clean_tweet(text): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split()) 





def get_rating_value(text): 

        # create TextBlob object of passed tweet text 
        analysis = TextBlob(clean_tweet(text))
        # set sentiment 
        return analysis.sentiment.polarity


def scale(x):

    OldRange = (10 - (-10))  
    NewRange = (10- 0)  
    NewValue = (((x - (-10)) * NewRange) / OldRange) + 0
    return NewValue
            




k=get_rating_value(review)
print(int(scale(k)),"rating out of 10")

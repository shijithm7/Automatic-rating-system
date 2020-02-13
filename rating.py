#import required library



from textblob import TextBlob
import re


#receving comment from user

review=str(input("Enter your review : "))

def clean_textt(text): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split()) 



# generating rating value

def get_rating_value(text): 

        # create TextBlob object of passed tweet text 
        analysis = TextBlob(clean_textt(text))
        # set sentiment 
        return analysis.sentiment.polarity

#function which scale rating in between 0-10
def scale(x):

    OldRange = (10 - (-10))  
    NewRange = (10- 0)  
    NewValue = (((x - (-10)) * NewRange) / OldRange) + 0
    return NewValue
            




k=get_rating_value(review)
print(int(scale(k)),"rating out of 10")

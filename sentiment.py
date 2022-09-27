# %%
import pickle
from snownlp import SnowNLP

# %%
def Sentiment_Analysis(inputSTR):
    from snownlp import SnowNLP
    sent = SnowNLP(inputSTR)
    simplified_sent = sent.han
    sentiment_sent = SnowNLP(simplified_sent).sentiments

    return sentiment_sent

# %%
sentiment_pickle = open('sentiment.pickle', 'wb') 
pickle.dump(Sentiment_Analysis, sentiment_pickle) 
sentiment_pickle.close() 



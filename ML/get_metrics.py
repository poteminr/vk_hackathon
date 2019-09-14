from summa import summarizer
from summa import keywords
import summa
import numpy as np
from numpy import dot
from numpy.linalg import norm
import fasttext as ft

from text_prep import TextPreproc

EMBEDDING_PATH = "ft_native_300_ru_wiki_lenta_lemmatize.bin"
model = ft.load_model(EMBEDDING_PATH)

tp = TextPreproc()


def cosine_sim(vec_a, vec_b) -> float:
    
    cos_sim = dot(vec_a, vec_b)/(norm(vec_a)*norm(vec_b))
    return cos_sim

def get_embeddings(model, text_list: np.array, summarize=True, it_user=False):
    
    if it_user:
        text = text_list[0]
        text_list = text_list[1:]
    
    else:
        text = ""

    for part in text_list:
        if summarize:
            summary_res = summarizer.summarize(part, language="russian",)
            if summary_res != "":
                text += summary_res
            else:
                text += part
        else:
            text += part
            
    vector = model.get_sentence_vector(text)
    
    return vector




def calc_metrics(user_data: np.array, ivent_data : np.array) -> float:
    user_embeded = get_embeddings(model, user_data, it_user=True)
    ivent_embeded = get_embeddings(model, ivent_data)
    
    distance = cosine_sim(user_embeded, ivent_embeded)
    
    return distance
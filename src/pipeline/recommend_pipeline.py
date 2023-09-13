import sys
import pandas as pd
import pickle

from src.exception import CustomException

from src.utils import get_recommendations


class RecommendPipeline:
    def __init__(self):
        pass

    def recommend(self,song_name):
        try:

            top_100_similarity_path = 'artifacts/unique_top_100_cos_similarity.pkl'
            songs_path = 'artifacts/unique_refined_dataset.pkl'

            songs = pd.read_pickle(songs_path)
            top_100_similarity_scores = pickle.load(open(top_100_similarity_path,'rb'))

            recommended_song_data = get_recommendations(song_name, top_100_similarity_scores, songs)

            return recommended_song_data
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,song_name:str):

        self.song_name = song_name
    
    def get_song_name(self):
        return self.song_name

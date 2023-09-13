import pandas as pd
from IPython.display import display, HTML



def get_recommendations(title, top_100_similarity_scores, dataset, no_of_recs = 5):


    
    #get the index of the song title
    idx = dataset[dataset['song-artist']==title].index[0][0]

    if isinstance(idx, pd.Series):
        idx = idx[0]
    

    top = top_100_similarity_scores[idx]

    recommended_indices = [x[0] for x in top]
    

    rec_song_names = dataset.iloc[recommended_indices]['name'].values[0:no_of_recs]
    rec_song_artists = dataset.iloc[recommended_indices]['artists_names'].values[0:no_of_recs]
    rec_song_link = dataset.iloc[recommended_indices]['uri'].values[0:no_of_recs]
    rec_song_images = dataset.iloc[recommended_indices]['images_url'].values[0:no_of_recs]
    
    rec_song_popularity = list(enumerate(dataset.iloc[list(recommended_indices)]['popularity'].values))[0:no_of_recs]
    
    
    sorted_songs_based_on_popularity = sorted(rec_song_popularity, key= lambda x: x[1], reverse=True)
    rec_song_indices_on_popularity, rec_scores_on_popularity = zip(*sorted_songs_based_on_popularity)
    
    recommended_data = [[rec_song_names[i], rec_song_artists[i],rec_song_link[i],rec_song_images[i]]
                        for i in rec_song_indices_on_popularity]
    
    recommended_dataframe = pd.DataFrame(recommended_data, columns = ["Name", "Artist", "Link", "Image"])   
    
    return recommended_dataframe
        

# Function to generate the marquee HTML code
def generate_marquee(text):
    if isinstance(text, list):
        if len(text) > 0:
            text = ', '.join(text)
        else:
            text = ''
    return f"<marquee scrollamount='4' behavior='scroll' direction='left' stop='true' style='max-height: 22px;'>{text}</marquee>"

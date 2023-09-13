from flask import Flask,request,render_template 
import pandas as pd
import numpy as np

from src.pipeline.recommend_pipeline import CustomData,RecommendPipeline

application = Flask(__name__)

app = application

## Route for a homepage

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/recommendsongs', methods=['GET', 'POST'])

def recommend_songs():
    if request.method== 'GET':

        # Pass the DataFrame to the template
        songs_df = pd.read_pickle('artifacts/unique_refined_dataset.pkl')
        song_names = songs_df['song-artist'].tolist()
        return render_template('home.html', song_names=song_names)
    
    else:
        data = CustomData(song_name= request.form.get("song"))

        selected_song = data.get_song_name()

        recommended_songs = RecommendPipeline()

        results = recommended_songs.recommend(selected_song)
        results_html = results.to_html(classes='table table-striped')

        return render_template('home.html',results=results_html)

if __name__== "__main__":
    app.run(host = "0.0.0.0")

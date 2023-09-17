# This is an end to end content based song recommender prototype

A recommender system is a system that, no wonder, recommends content or items to users. The purpose of a recommendation system basically is to search for content that would be interesting to an individual. It can create useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual.

# About this Project:

In this project, this will be a content-based music recommender system. Meaning, it will not depend on a user's search history/likes,etc. But it will depend on the features of the input content (song) itself and based upon it will be recommending songs that are similar to that input song.

This is a streamlit application that takes an input song from the user and from it recommends various songs that are similar. 
* [Website here](https://music-recommender-kb-805ff6786f8f.herokuapp.com/)


# Demo:

<img src="images/Screenshot (52).png" alt="workflow" width="70%">
<img src="images/Screenshot (53).png" alt="workflow" width="70%">


# Steps and concept:
* Data Collection:
    1. Some IDs of songs were collected from a random dataset from Kaggle (could be getting more ids). Link [here](https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify?select=playlists.csv)
    2. From these IDs API requests were made to collect song metadata and audio features.
    3. Since alot of requests were to be made, concurrent threading was used to save time.

* Exploratory Data Analysis:
    1. After collecting the data, some inital investigatory visualisations were conducted for some insights and detecting anomalies/correlations.
    2. The EDA is in the jupyter notebook exploratory data analysis.ipynb.

* Data Cleaning:
    * Some data cleaning methods were conducted, such as:
         1. Dropping full duplicated rows.
         2. Dropping songs with the same name an artist, but different popularity scores, keeping the one with the highest score.
         3. Deleting some empty entries.
         4. Combining the same songs but labelled as different genres, including the allt the genres for a song in one entry as a list.
         5. Extracting the artists names, release year.
         6. Fixing the format of some entries.
         7. Dropping un-important columns.
           
* Feature Engineering and Cosine Similarity:
      1. Feature Engineering:
        * Create a feature that includes the number of sections, slightly correlated with the duration but not too much.
        * Some features contain confidence scores of these feature measurements, a metafeature was created from the tempo and its confidence score, as well as the mode and its confidence score. The explanations            for these metafeatures are shown (with equations and graphs) in the jupyter notebook recommender.ipynb.
        * Transforming the date of the release to only the release year, could be experimenting with seasons (seasonal songs).
        * Create a textual soup, and then a feature vector representation of the artists names and the genres using the Word2Vec model, and stacking it with the rest of the features.

      2. Cosine Similarity:
          * Cosine Similarity is a metric that allows you to measure the similarity of two vectors of arbtitary dimensions.
          * In order to demonstrate cosine similarity function we need vectors, which is created.
          * A Cosine Similarity matrix was build for all the songs of size nXn, where n in the number of songs in the dataset
          * A cosine similarity values ranges between [0,1]. 0 Being exteremely disimilar to 1 being sort of identical.
          * For all the songs, only the top 100 scores were pushed to the repo for deployement.
  
  * Deployement
      1. Streamlit application:
         * Top 100 cosine scores and songs are loaded to a streamlit app to be able to showcase results.
         * Input song is selected by the user along with the number of recommendations specified. (Now harcoded at 10 but can easily be modified to take the number specified by the user, up to 100.)
         * Top *10* songs are loaded for the that specific input song and are sorted based on their popularity, showing the most popular ones from the top 100 similarities first.
  
      2. Heroku Deployement:
         * The GitHub repositry is synced with the Heroku app where the streamlit file is deployed using heroku for the user interface. 
    

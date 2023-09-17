# This is an end to end content based song recommender prototype

A recommender system is a system that, no wonder, recommends content or items to users. The purpose of a recommendation system basically is to search for content that would be interesting to an individual. It can create useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual.

# About this Project:

In this project, this will be a content-based music recommender system. Meaning, it will not depend on a user's search history/likes,etc. But it will depend on the features of the input content (song) itself and based upon it will be recommending songs that are similar to that input song.

This is a streamlit application that takes an input song from the user and from it recommends various songs that are similar. 
* [Website here](https://music-recommender-kb-805ff6786f8f.herokuapp.com/)


# Demo:

<img src="images/Screenshot (49).png" alt="workflow" width="70%">
<img src="images/Screenshot (49).png" alt="workflow" width="70%">

# Steps and concept:
* Data Collections:

  1 . Cosine Similarity is a metric that allows you to measure the similarity of two vectors of arbtitary dimensions.

  2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

  3 . Finally, Once we have vectors, We can call cosine_similarity() by passing two vectors, which will calculate the cosine similarity between these two.

  4 . It will be a value between [0,1]. 0 Being exteremly disimilar to 1 being sort of identical.

  5 . /

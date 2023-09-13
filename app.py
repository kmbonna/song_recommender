import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import get_recommendations,generate_marquee

import pickle
import streamlit as st
import requests
import pandas as pd

st.markdown(
    """
    <style>
    body {
        background-color: #000000; /* Black background */
        font-family: serif;
    }
    
    /* Customize the select box */
    .css-2b097c-container {
        background-color: #413a3a; /* #413a3a background for the select box */
    }
    
    /* Customize the show button recommendation background */
    .css-vfxkzw {
        background-color: #313452; /* #313452 background for the show button recommendation */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


#HEADER
st.markdown("<h1 style=' font-size: 35px; text-align: center;'>Song Recommendation Dumbass AI System</h1>", unsafe_allow_html=True)

#SUBHEADER
st.markdown("<h2 style='font-size: 18px;text-align: center; font-style: italic;'>(btw I am a data scientist not a web developer), ta7eyaty - KB</h2>", unsafe_allow_html=True)

#BUTTONS
st.markdown("<style>div.stButton > button:first-child { background-color: #413A3A; color: #FFFFFF; font-weight: bold; }</style>", unsafe_allow_html=True)

#LINKS
st.markdown("<style>a { color: #CCCCgiCC; text-decoration: none; }</style>", unsafe_allow_html=True)



songs = pd.read_pickle('artifacts/unique_refined_dataset.pkl')
top_100_similarity_scores = pickle.load(open('artifacts/unique_top_100_cos_similarity.pkl','rb'))

songs_list = songs['song-artist'].values

selected_song = st.selectbox(
    "Search for a song here",
    songs_list,
    placeholder="Select...",
)


if st.button('Show Recommendations'):
    recommended_song_data = get_recommendations(selected_song, top_100_similarity_scores, songs)

    num_recommendations = len(recommended_song_data)
    num_columns = 5  # Number of columns to display recommendations


    for i in range(0, num_recommendations, num_columns):
        # Create a column for each set of recommendations
        col = st.columns(min(num_columns, num_recommendations - i))

        
        for j in range(min(num_columns, num_recommendations - i)):
            with col[j]:
                
                # Check if the name is long enough to apply scrolling
                if len(recommended_song_data['Name'][i + j]) > 15:  # Adjust the length threshold as needed
                # Apply scrolling text effect for long names
                    st.markdown(generate_marquee(recommended_song_data['Name'][i + j]), unsafe_allow_html=True)
                else:
                # Display the name as plain text for short names
                    st.markdown(recommended_song_data['Name'][i + j])
                        

                # Check if the artists are long enough to apply scrolling
                if len(', '.join(recommended_song_data['Artist'][i + j])) > 15:  # Adjust the length threshold as needed
                # Apply scrolling text effect for long artists
                    st.markdown(generate_marquee(recommended_song_data['Artist'][i + j]), unsafe_allow_html=True)    
                else:
                # Display the artists as plain text for short names
                    st.markdown(', '.join(recommended_song_data['Artist'][i + j]))

                st.image(recommended_song_data['Image'][i + j], width=125, output_format='JPEG')

                # Display the Spotify link as a clickable link
                st.markdown(f"Listen to it [here]({recommended_song_data['Link'][i + j]})", unsafe_allow_html=True)

        
        # Add a line break between rows
        st.text("")
        st.text("")
        st.text("")
        st.text("")
                
                
                


import streamlit as st
from youtube_fetcher import fetch_youtube_videos
from content_ranker import rank_videos
from learning_path_builder import add_learning_levels

# App configuration
st.set_page_config(page_title="EduBot – Learn Smartly", layout="centered")
st.title(" EduBot: Personalized Learning Path Generator")

st.markdown("Enter your learning goal and EduBot will recommend the best YouTube tutorials – sorted by difficulty!")

# Inputs
query = st.text_input(" What do you want to learn?", placeholder="e.g., Deep Learning from scratch")
api_key = st.text_input(" YouTube API Key", type="password")
max_results = st.slider(" Number of videos to fetch", min_value=5, max_value=30, value=10)

if st.button("Generate Learning Path") and query and api_key:
    with st.spinner("Fetching and analyzing videos..."):
        try:
            videos_df = fetch_youtube_videos(query, max_results, api_key)
            ranked_df = rank_videos(query, videos_df)
            final_df = add_learning_levels(ranked_df)

            for level in ['Beginner', 'Intermediate', 'Advanced']:
                st.subheader(f" {level} Level")
                level_videos = final_df[final_df['level'] == level]

                if level_videos.empty:
                    st.markdown("_No videos found for this level._")
                else:
                    for _, row in level_videos.head(5).iterrows():
                        st.markdown(f"- [{row['title']}]({row['url']})")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

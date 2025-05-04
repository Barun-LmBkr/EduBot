from youtube_fetcher import fetch_youtube_videos
from content_ranker import rank_videos
from learning_path_builder import add_learning_levels

api_key = "AIzaSyAkR6RY1e7xWFCteNyTPqIOxfGRCZZ95Fo"
videos_df = fetch_youtube_videos("deep learning", 15, api_key)

user_input = "I want to learn deep learning from scratch"
ranked_df = rank_videos(user_input, videos_df)

labeled_df = add_learning_levels(ranked_df)

# Show final structured learning path
for level in ['Beginner', 'Intermediate', 'Advanced']:
    print(f"\n {level} Level:")
    print(labeled_df[labeled_df['level'] == level][['title', 'url']].head(5))

from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Load SBERT model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_videos(user_query, video_df):
    """
    Rank videos by how well they match the user query using SBERT + cosine similarity.
    """
    descriptions = video_df['description'].fillna("").tolist()

    user_embedding = model.encode(user_query, convert_to_tensor=True)
    video_embeddings = model.encode(descriptions, convert_to_tensor=True)

    scores = util.cos_sim(user_embedding, video_embeddings)[0]
    video_df['similarity'] = scores.cpu().numpy()

    return video_df.sort_values(by='similarity', ascending=False).reset_index(drop=True)

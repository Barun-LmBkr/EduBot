
import requests
import pandas as pd

def fetch_youtube_videos(query, max_results, api_key):
    """
    Fetch YouTube videos using the YouTube Data API v3.
    Returns a DataFrame with title, description, and URL.
    """
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'q': query,
        'part': 'snippet',
        'type': 'video',
        'maxResults': max_results,
        'key': api_key
    }

    response = requests.get(search_url, params=params)
    response.raise_for_status()
    items = response.json().get('items', [])

    video_data = []
    for item in items:
        video_id = item['id']['videoId']
        snippet = item['snippet']
        title = snippet['title']
        description = snippet.get('description', '')
        url = f"https://www.youtube.com/watch?v={video_id}"

        video_data.append({
            'title': title,
            'description': description,
            'url': url
        })

    return pd.DataFrame(video_data)

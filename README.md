# EduBot: Personalized Learning Path Generator

EduBot is a machine learning-powered tool designed to help learners discover personalized educational content from YouTube and online platforms. It recommends videos based on the learner’s background, interests, and current skill level. The system uses natural language processing to understand user intent and semantic similarity techniques to rank content accordingly.

## Overview

In today's digital learning landscape, users are overwhelmed by an abundance of video content but often lack a structured learning path. EduBot addresses this problem by:

- Understanding what the learner wants to study through a natural language query
- Automatically fetching relevant YouTube videos
- Ranking videos based on semantic relevance using a fine-tuned transformer model (SBERT)
- Categorizing results into beginner, intermediate, and advanced levels

## Key Features

- Semantic search for YouTube video titles and descriptions
- Skill level classification based on title heuristics
- Real-time video retrieval via the YouTube Data API
- Clean and interactive UI using Streamlit
- Easily deployable for educational or personal use

## Technologies Used

- Python
- Streamlit
- SentenceTransformers (SBERT)
- YouTube Data API v3
- Pandas and Requests

## Folder Structure

```
EduBot/
├── app.py                  # Main Streamlit application
├── youtube_fetcher.py      # YouTube API integration
├── content_ranker.py       # Semantic search logic (SBERT)
├── learning_path_builder.py# Heuristic level categorization
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/EduBot.git
    cd EduBot
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up YouTube API**
    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - Create a new project and enable the YouTube Data API v3
    - Generate an API key and paste it into the appropriate part of your code

4. **Run the application**
    ```bash
    streamlit run app.py
    ```

## Example Use Case

Suppose a user wants to learn "machine learning for finance". EduBot will:

- Analyze the query to understand both the topic and domain
- Search for relevant YouTube videos
- Rank the results based on semantic similarity
- Classify them into levels, helping the user choose where to start

## Future Work

- Integration with Coursera and edX for MOOC suggestions
- GPT-based summarization and difficulty estimation
- User login and personalized learning tracking
- Quiz integration for dynamic learning path adjustment

## Why This Project Matters

EduBot showcases the practical use of natural language processing, recommender systems, and public APIs to solve a real-world educational problem. It aligns well with enterprise and EdTech interests and demonstrates strong foundations in machine learning and user-centric design.

## License

This project is for educational and personal portfolio purposes.

## Author

Created by Barun.Lmbkr. Built as part of a machine learning internship preparation portfolio.
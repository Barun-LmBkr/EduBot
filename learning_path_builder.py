
def categorize_level(title, description):
    """
    Heuristically categorize a video as Beginner, Intermediate, or Advanced
    based on keywords in its title and description.
    """
    content = f"{title} {description}".lower()

    beginner_keywords = ['introduction', 'for beginners', 'crash course', 'getting started', 'basic']
    intermediate_keywords = ['intermediate', 'tutorial', 'hands-on', 'walkthrough', 'implementation']
    advanced_keywords = ['advanced', 'research', 'masterclass', 'theory', 'in-depth']

    if any(kw in content for kw in beginner_keywords):
        return 'Beginner'
    elif any(kw in content for kw in advanced_keywords):
        return 'Advanced'
    elif any(kw in content for kw in intermediate_keywords):
        return 'Intermediate'
    else:
        return 'Intermediate'  # default fallback

def add_learning_levels(ranked_df):
    """
    Add a 'level' column to the DataFrame based on title/description heuristics.
    """
    ranked_df['level'] = ranked_df.apply(
        lambda row: categorize_level(row['title'], row['description']), axis=1
    )
    return ranked_df

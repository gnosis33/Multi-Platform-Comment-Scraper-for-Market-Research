from googleapiclient.discovery import build

def get_youtube_comments(video_id, api_key):
    # Build the YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Fetch comments
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100  # You can change this
    )
    response = request.execute()

    comments = []
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments


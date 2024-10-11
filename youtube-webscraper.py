from googleapiclient.discovery import build

def get_comments(video_id, api_key):
    # Build the YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Fetch comments
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=1000  # You can change this
    )
    response = request.execute()

    comments = []
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments

if __name__ == "__main__":
    video_id = input('ENTER_VIDEO_ID: ')  # Replace with your video ID
    api_key = 'AIzaSyAFifrArU6lUSCg6H27wuZVgT0iEi7lZbM'  # Replace with your API key

    comments = get_comments(video_id, api_key)
    for i, comment in enumerate(comments):
        print(f"Comment {i+1}: {comment}")
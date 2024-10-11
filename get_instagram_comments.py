import requests

def get_instagram_comments(post_id, access_token):
    url = f"https://graph.instagram.com/{post_id}/comments?fields=text&access_token={access_token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        comments = [comment['text'] for comment in data['data']]
        return comments
    else:
        print(f"Failed to get comments: {response.content}")
        return []

# Example usage
# Note: Replace 'your_post_id' and 'your_access_token' with actual values
# comments = get_instagram_comments("your_post_id", "your_access_token")
# print(comments)

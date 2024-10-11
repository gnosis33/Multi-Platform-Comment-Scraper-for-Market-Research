import requests

def get_facebook_comments(post_id, access_token):
    url = f"https://graph.facebook.com/v11.0/{post_id}/comments?access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        comments = [comment['message'] for comment in data['data']]
        return comments
    else:
        print(f"Failed to get comments: {response.content}")
        return []

# Example usage
# Note: Replace 'your_post_id' and 'your_access_token' with actual values
# comments = get_facebook_comments("your_post_id", "your_access_token")
# print(comments)

'''
import requests
from bs4 import BeautifulSoup

def get_facebook_comments(post_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(post_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    comments = []
    for comment in soup.find_all('div', {'class': 'your_comment_class_here'}):  # Replace 'your_comment_class_here' with the actual class for comments
        comment_text = comment.find('span', {'class': 'your_comment_text_class_here'})  # Replace 'your_comment_text_class_here' with the actual class for comment text
        if comment_text:
            comments.append(comment_text.text)
    
    return comments

# Example usage
# Note: Replace 'your_post_url' with an actual public Facebook post URL
# comments = get_facebook_comments("your_post_url")
# print(comments)

'''

import requests
from bs4 import BeautifulSoup

def get_reddit_comments(post_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(post_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    comments = []
    for comment in soup.find_all('div', {'class': '_2s8GkMW_LrgazQ'}):
        comment_text = comment.find('span', {'class': 's3i3io'})
        if comment_text:
            comments.append(comment_text.text)
    
    return comments

# Example usage
# Note: Replace 'your_post_url' with an actual Reddit post URL
# comments = get_reddit_comments("your_post_url")
# print(comments)

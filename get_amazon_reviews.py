import requests
from bs4 import BeautifulSoup

def get_amazon_reviews(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    reviews = []
    for review in soup.find_all('span', {'data-asin-review-text': True}):
        reviews.append(review.text)

    return reviews

# Example usage
# Note: Replace 'your_product_url' with an actual Amazon product URL
# reviews = get_amazon_reviews("your_product_url")
# print(reviews)

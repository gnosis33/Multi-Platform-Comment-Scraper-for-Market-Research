import requests

def get_yelp_reviews(business_id, api_key):
    url = f"https://api.yelp.com/v3/businesses/{business_id}/reviews"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        reviews = [review['text'] for review in data['reviews']]
        return reviews
    else:
        print(f"Failed to get reviews: {response.content}")
        return []

# Example usage
# Note: Replace 'your_business_id' and 'your_api_key' with actual values
# reviews = get_yelp_reviews("your_business_id", "your_api_key")
# print(reviews)

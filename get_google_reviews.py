import requests

def get_google_reviews(place_id, api_key):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=review&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        reviews = [review['text'] for review in data['result']['reviews']]
        return reviews
    else:
        print(f"Failed to get reviews: {response.content}")
        return []

# Example usage
# Note: Replace 'your_place_id' and 'your_api_key' with actual values
# reviews = get_google_reviews("your_place_id", "your_api_key")
# print(reviews)

import tweepy

def get_twitter_comments(tweet_url, api_key, api_secret_key, access_token, access_token_secret):
    # Authenticate with the Twitter API
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Extract tweet ID from the tweet URL
    tweet_id = tweet_url.split('/')[-1]

    # Fetch comments (replies) to the tweet
    comments = []
    for tweet in tweepy.Cursor(api.search, q=f'to:{tweet_id}', result_type='recent', timeout=999999).items(100):  # Change 100 to the number of comments you want
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id_str == tweet_id:
                comments.append(tweet.text)

    return comments


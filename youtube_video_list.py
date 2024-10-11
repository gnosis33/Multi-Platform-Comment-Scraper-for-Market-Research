from googleapiclient.discovery import build
import csv
import os

# Initialize the YouTube API client
def initialize_youtube_api(api_version='v3'):
    api_key = 'AIzaSyAFifrArU6lUSCg6H27wuZVgT0iEi7lZbM'  # Hardcoded for testing
    youtube = build('youtube', api_version, developerKey=api_key)
    return youtube

# Fetch video URLs based on a search term
def fetch_video_urls(youtube, search_term, max_results=50):
    search_response = youtube.search().list(
        q=search_term,
        type='video',
        part='id,snippet',
        maxResults=max_results
    ).execute()

    video_urls = []
    for search_result in search_response.get('items', []):
        video_urls.append(f"https://www.youtube.com/watch?v={search_result['id']['videoId']}")

    return video_urls

# Write URLs to a CSV file
def write_to_csv(video_urls, file_name='urls.csv'):
    # Create 'urls' folder if it doesn't exist
    if not os.path.exists('urls'):
        os.makedirs('urls')

    # Path to save the CSV file inside 'urls' folder
    save_path = os.path.join('urls', file_name)

    with open(save_path, 'w', newline='') as csvfile:
        fieldnames = ['URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for url in video_urls:
            writer.writerow({'URL': url})

# Main function
def main():
    youtube = initialize_youtube_api()
    search_term = input("your search term here: ") # Replace with your search term
    video_urls = fetch_video_urls(youtube, search_term)
    write_to_csv(video_urls)

if __name__ == '__main__':
    main()

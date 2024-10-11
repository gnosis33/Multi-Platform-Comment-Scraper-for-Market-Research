import os
import csv
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from get_youtube_comments import get_youtube_comments

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

def read_csv(file_path):
    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f)
        urls = [row[0] for row in csv_reader]
    return urls

def write_to_csv(comments, identifier, platform):
    output_file = os.path.join('output', f'{platform}_{identifier}_comments.csv')
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        for comment in comments:
            csv_writer.writerow([comment])

if __name__ == "__main__":
    urls = read_csv('./urls/urls.csv')  # Assuming the CSV is named 'urls.csv' and resides in the 'urls' folder

    # Create 'output' folder if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    for url in urls:
        parsed_url = urlparse(url)
        netloc = parsed_url.netloc

        if "youtube.com" in netloc:
            query_parameters = parse_qs(parsed_url.query)
            video_id = query_parameters.get('v', [None])[0]
            if video_id:
                print(video_id)
                comments = get_youtube_comments(video_id, YOUTUBE_API_KEY)
                write_to_csv(comments, video_id, "youtube")


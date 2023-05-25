#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install google-api-python-client


# In[25]:


import os
from googleapiclient.discovery import build

# Set up API credentials
API_KEY = 'AIzaSyARJYNNlIiACEvdgqv-mZOqBZzhlWBNCv4'  # Replace with your own API key
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # This is required if running the code locally

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_channel_data(channel_id):
    # Retrieve channel data
    response = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id
    ).execute()

    # Extract relevant information from the API response
    channel = response['items'][0]
    channel_name = channel['snippet']['title']
    subscriber_count = channel['statistics']['subscriberCount']
    video_count = channel['statistics']['videoCount']

    # Return the channel data
    return channel_name, subscriber_count, video_count

def get_video_data(video_id):
    # Retrieve video data
    response = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    # Extract relevant information from the API response
    video = response['items'][0]
    video_title = video['snippet']['title']
    likes = video['statistics']['likeCount']
    dislikes = video['statistics']
    comment_count = video['statistics']['commentCount']

    # Return the video data
    return video_title, likes, dislikes, comment_count

# Example usage
channel_id = 'UCBR8-60-B28hp2BmDPdntcQ'  # Replace with the desired YouTube channel ID
video_id = 'dQw4w9WgXcQ'  # Replace with the desired YouTube video ID

channel_data = get_channel_data(channel_id)
video_data = get_video_data(video_id)

print('Channel Data:')
print('Name:', channel_data[0])
print('Subscribers:', channel_data[1])
print('Video Count:', channel_data[2])

print('\nVideo Data:')
print('Title:', video_data[0])
print('Likes:', video_data[1])
print('Dislikes:', video_data[2])
print('Comment Count:', video_data[3])


#!/usr/bin/python3
"""
This script fetches posts from JSONPlaceholder and processes them.

It provides functions to print post titles and save post data to a CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch data.")


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]
        with open("posts.csv", mode="w", newline="",
                  encoding="utf-8") as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Data saved to posts.csv")
    else:
        print("Failed to fetch data.")

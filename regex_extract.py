#!/usr/bin/env python3
"""
Regex Data Extraction Project
Description: This is a simple project on how I will extract information like
emails, urls, time, hashtags and phone numbers from a sample text.
"""


#First I import the re library to support regular expressions
import re

#Create a dictionary that has the regex patterns I will use to extract the data
patterns = {
    "emails": r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}",
    "urls": r"https?://[^\s]+",
    "hashtags": r"#\w+",
    "phone_numbers": r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})",
    "time": r"\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?:\s?[APMapm]{2})?\b"
}

#Defining a function that will help me extract the patterns
def extract_patterns(pattern, text):
    """
    Find all the patterns for a given regex pattern.
    """
    return re.findall(pattern, text)

#display the main menu for the user
def show_menu():
    print("\n Regex Data Extraction Project")
    print("1. Extract everything\n"
          "2. Extract one type\n"
          "3. Exit")

#Function to display a second menu for single extraction
def show_submenu():
    print("\n Choose what you would like to extract:")
    for i, key in enumerate(patterns.keys(), start=1):
        print("{}) {}".format(i, key.capitalize()))
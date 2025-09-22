#!/usr/bin/env python3
"""
Regex Data Extraction Project
Description: This is a simple project on how I will extract information like
emails, urls, time, hashtags and phone numbers from a sample text.
"""


# Import the re library to support regular expressions
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
    Args:
        pattern (string): The regex pattern to search for
        text (string): The text to search in
    Returns: a list of matched patterns in the text
    """
    return re.findall(pattern, text)

#Function to display the main menu to the user
def show_menu():
    print("\n Regex Data Extraction Project")
    print("1. Extract everything\n"
          "2. Extract one type\n"
          "3. Exit")

#Function to display a second sub-menu to choose to extract a single data type
def show_submenu():
    print("\n Choose what you would like to extract:")
    #using enumerate to add numbers starting from 1
    for i, key in enumerate(patterns.keys(), start=1):
        print("{}) {}".format(i, key.capitalize()))

# Function for the main program
def main():
    text = """
    Contact me at john.doe@example.com or jane_doe123@company.co.uk.
    Visit https://www.example.com or http://sub.example.org/page.
    Call me at (123) 456-7890, 123-456-7890, or 123.456.7890.
    My credit card numbers: 1234 5678 9012 3456, 1234-5678-9012-3456
    Meeting times: 14:30, 3:30 PM
    #meetings #see_you_there
    """

    # Creating an infinite loop for the program
    while True:
        show_menu() # calling the function to display the menu
        choice = input("Enter your choice: ") # Getting the user's choice

        if choice == "1":
            # Extracts all data types at once
            print("\n Extracting everything at once...\n")
            for key, pattern in patterns.items():
                matches = extract_patterns(pattern, text)
                print("{}:, {}".format(key.capitalize(), matches))

        elif choice == "2":
            # Extract one data type at a time
            show_submenu()
            sub_choice = input("Enter your choice: ")

            try:
                sub_choice = int(sub_choice) - 1 # This converts the user's choice to index
                key = list(patterns.keys())[sub_choice] # This gets the key corresponding to the index
                matches = extract_patterns(patterns[key], text)
                print("\n{} found: {}".format(key.capitalize(), matches))
            # Handle invalid input (non-integer or out-of-range index)
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

        elif choice == "3":
            #Exit the program
            print("Thank you for using this program!")
            break

        else:
            # Handles invalid menu option
            print("Invalid input. Please enter 1, 2, or 3.")

#Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()
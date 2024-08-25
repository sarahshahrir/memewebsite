# Meme Website

A simple Flask-based web application that displays random memes from a specified subreddit. The page automatically refreshes every 5 seconds to show a new meme.

## Description

This project is a meme website that fetches random memes from the "Catmemes" subreddit using the Meme API. The web application is built using Python's Flask framework and serves dynamic content using a template. The webpage automatically updates every 5 seconds to display a new meme from the chosen subreddit.

### Features

- Displays a random meme from the "Catmemes" subreddit.
- Auto-refreshes every 5 seconds to show a new meme.
- Responsive design to adjust to different devices.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sarahshahrir/memewebsite.git

2. **Navidate to the Project Directory:**

   cd memewebsite

3. **Set Up a Virtual Environment:**

   python3 -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .venv\Scripts\activate     # For Windows

4. **Install Required Dependencies:**

   Install the necessary packages listed in 'requirements.txt':
   ```bash
   pip install -r requirements.txt

5. **Run the Application:**

  Start the Flask app with the following command:
  ```bash
  python app.py
  ```
  Open your browser and go to http://localhost:5000 to view the meme website.

  ## Acknowledgments

     - Meme API: Used to fetch memes from various subreddits.
     - 

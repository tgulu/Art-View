# ART View - Art Institute of Chicago Artwork Viewer

## Description

ART-View is a Flask-based website that allows users to explore a diverse collection of artwork from the Art Institute of Chicago using their public API. This platform not only provides access to the artwork but also offers user account functionality. Users can create accounts, store personal information securely, log into their accounts, and enjoy a curated selection of art pieces each time they log in.

## Technologies Used

- Flask: A micro web framework for Python, used to build the backend of the website.
- Bootstrap: A front-end framework that aids in creating responsive and visually appealing web pages.
- JavaScript: Used to enhance user interactions and dynamic content presentation.
- SQL Database: Stores user account information securely, including names, email addresses, and hashed passwords.

## Features

- User Authentication: Users can create accounts and log in securely using their email and password.
- Account Management: User account data, including first and last names, is stored in a database.
- Artwork Display: The website connects to the Art Institute of Chicago's public API to retrieve and showcase a variety of art pieces.
- Dynamic Content: Every time a user logs in, a new set of art pieces is presented, providing a fresh experience.
- Responsive Design: Bootstrap is employed to ensure the website is accessible and functional across different devices.

## Preview

![ART-View Preview](insert_image_url_here)

## Getting Started

To run the project locally on your machine, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/art-view.git
   ```

2. Navigate to the project directory:
   ```
   cd art-view
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Modify the `config.py` file to include your database credentials.
   - Run the following commands to create the database and tables:
     ```
     flask db init
     flask db migrate -m "Initial migration."
     flask db upgrade
     ```

5. Obtain API Access:
   - Visit the Art Institute of Chicago's API website and sign up for an API key.
   - Insert your API key in the appropriate location in the codebase.

6. Run the application:
   ```
   flask run
   ```

7. Open your web browser and navigate to `http://127.0.0.1:5000` to access the ART-View website.

## Usage

Once you've accessed the website, you can:
- Create a new user account.
- Log into your account using your email and password.
- Browse a unique collection of artworks with each login.

Experience the beauty and diversity of the Art Institute of Chicago's artwork collection through the ART-View platform.
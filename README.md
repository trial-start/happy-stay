# HappyStay Project

HappyStay is a simple web-based platform that allows users to find unique accommodations and experiences in various destinations. This project is designed to help travelers discover and book their dream stays and activities, providing a seamless and user-friendly experience.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Features

### User Authentication

- **Sign Up**: Users can create an account by providing their full name, email, and password.

- **Sign In**: Registered users can sign in using their username and password.

### Home Page

- **Search Accommodations**: Users can search for accommodations by entering a location in the search bar.

- **Featured Listings**: Display a selection of featured accommodations and experiences with images, descriptions, ratings, and prices.

- **Explore Destinations**: Explore different travel destinations with images, descriptions, and prices.

### Navigation

- **Navbar**: Provides easy navigation to the Home, About, Destinations, and Contact pages. Users can also log out from the navbar.

### Booking

- **Accommodation Details**: Users can view detailed information about accommodations and experiences by clicking on their respective cards.

### Contact

- **Contact Information**: Displays contact information for inquiries.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 
- Django
- Git
- A text editor or integrated development environment (IDE)
- Access to the internet to load external CSS and JavaScript libraries

## Installation

1. Clone the HappyStay repository to your local machine using the following command:

   ```bash
   git clone https://github.com/trial-start/happy-stay.git
   ```

2. Navigate to the project directory:

   ```bash
    cd happystay
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
    python -m venv venv
   ```

    Activate the virtual environment:
   
     On Windows:
   
      ```bash
     venv\Scripts\activate
      ```
   
     On macOS and Linux:
   
      ```bash
       source venv/bin/activate
      ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your web browser and access the development server at http://127.0.0.1:8000/ to see the HappyStay website.

## Usage

- **Register for an account**: Visit the Sign Up page and create an account by providing your full name, email, and password.

- **Log in to your account**: Once registered, log in using your username and password on the Sign In page.

- **Explore accommodations and destinations**: Navigate to the Home page to explore a wide range of accommodations and travel destinations.

- **Use the search bar**: Utilize the search bar on the Home page to find specific accommodations by entering a location.

- **View listing details**: Click on a listing of your choice to view more details about the accommodation or experience.

- **Log out**: When you're done, log out from your account using the Navbar.

## Technologies Used

- **Django**: A high-level Python web framework used for building the backend of the application.

- **HTML and CSS**: These technologies are employed to design and structure the website's frontend.

- **Bootstrap**: A CSS framework utilized for responsive web design, ensuring a consistent and visually appealing user interface.

- **JavaScript and jQuery**: These technologies enhance the website's interactivity and user experience, providing dynamic features.



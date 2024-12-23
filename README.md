

Virtual Zoo - README

Overview

Virtual Zoo is a web-based application built with Django that offers users an engaging experience of exploring a virtual zoo. The platform features a home page with a user-friendly interface and a "View Animals" button. Upon clicking the button, users are directed to a page showcasing animals, each represented with a GIF and a descriptive text.

Features

Home Page:
A welcoming landing page with a clear layout and a "View Animals" button.

View Animals:

Displays a variety of animals, each accompanied by:

A lively GIF to visually represent the animal.

A short description highlighting unique characteristics or interesting facts about the animal.




Technologies Used

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript (optional for interactivity)

Database: SQLite (default) or other Django-supported databases


Installation

1. Clone the Repository:

git clone <repository-url>  
cd virtual-zoo


2. Set Up a Virtual Environment:

python -m venv venv  
source venv/bin/activate # On Windows: venv\Scripts\activate


3. Install Dependencies:

pip install -r requirements.txt


4. Run Migrations:

python manage.py migrate


5. Start the Development Server:

python manage.py runserver


6. Access the Application:
Open your browser and navigate to http://127.0.0.1:8000/.




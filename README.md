# FluffyBanana Website 🍌

A simple website built with Python Flask and HTML.

## Features

- Homepage with navigation links
- Contact page displaying a phone number
- Login page with username and password fields
- Multiple HTML templates
- Flask routing
- A simple service status logging exercise using a Python decorator

## Technologies Used

- Python
- Flask
- HTML
- Python Decorators

## Project Structure

```text
Flask-Login-Website/
├── app.py
├── detector.py
├── requirements.txt
├── README.md
└── templates/
    ├── index.html
    ├── login.html
    └── call.html
```

## Installation

1. Make sure Python is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install Flask:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command:

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Notes

- The login page is currently a basic HTML form and does not include real authentication.
- The detector script prints simulated service status messages. It does not perform actual internet or SMS checks.

---

Created as a beginner Python and Flask project.

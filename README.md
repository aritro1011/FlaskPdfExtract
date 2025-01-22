# Flask Data Extraction and Presentation App

This is a Flask-based application that extracts and processes data using the functionality provided in `main.py`. The processed data is presented in the frontend via a clean and interactive user interface.
---

## Features
- Extracts and processes data using the logic in `main.py`.
- Displays processed data on a user-friendly frontend built with HTML and CSS.
- Organized project structure with clear separation of concerns.
- Easy to set up and run on any system with Python installed.
- working demo link:https://www.loom.com/share/5c6424b52bf24d69a16922fdf64a5119?sid=4090c27a-2ee8-4a94-b3f6-aabac1611a42
  

---
## Solution Overview

The solution works as follows:

### `main.py`
This Python script contains functions to:
- Extract raw data from a source (e.g., file, API).
- Process and extract relevant information from the raw data.

### `flask_app.py`
This file is a basic Flask web application that:
- Uses the functions from `main.py` to perform data extraction and processing.
- Exposes an endpoint to interact with the frontend.

### Frontend (HTML/CSS)
A simple HTML/CSS interface is integrated into the Flask app, allowing users to interact with the backend. The frontend displays the extracted data or results processed by `main.py` through the Flask server.

## Project Structure
```plaintext
.
├── flask_app.py          # Main Flask application file
├── main.py               # Core functionality for data extraction and processing
├── data/                 # Folder containing raw data files
├── templates/
│   └── index.html        # HTML file for the frontend
├── static/
│   └── css/
│       └── style.css     # CSS for styling the frontend
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation (this file)
|__uploads        #folder to save the inputs
```
Set up a virtual environment (optional but recommended):
```
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
Install the required dependencies:
```
pip install -r requirements.txt
Ensure the data/ folder contains the raw data files for processing.
```
Usage
Start the Flask server:

```
python flask_app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```
View the extracted and processed data on the web interface.







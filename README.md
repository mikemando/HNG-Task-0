# JSON Response API

## Overview
This project is a simple API that returns a JSON response containing the following details:
- My email address
- The GitHub repository URL for this project
- A timestamp representing the current datetime (UTC) in ISO 8601 format

## Features
- Provides a structured JSON response.
- Built using Python and Django.

## Getting Started
### Prerequisites
Ensure you have the following installed on your system:
- Python (version 3.7 or higher)
- Git

### Installation and Setup
Follow these steps to set up and run the project locally:
1. Clone the repository:
   ```sh
   git clone https://github.com/account_name/repository_name.git
   ```
2. Navigate to the project directory:
   ```sh
   cd repository_name
   ```
3. Create a virtual environment:
   ```sh
   python -m venv env
   ```
4. Activate the virtual environment:
   - On macOS/Linux:
     ```sh
     source env/bin/activate
     ```
   - On Windows:
     ```sh
     env\Scripts\activate
     ```
5. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. The API will be available at:
   ```sh
   http://127.0.0.1:8000/
   ```

## API Documentation
### Endpoint URL
#### Base URL (Deployed):
[https://hng-task-0-wuuw.onrender.com/](https://hng-task-0-wuuw.onrender.com/)

### Request
- **Method:** `GET`
- **URL:** `/`

### Response
```json
{
    "email": "my_email@gmail.com",
    "current_datetime": "2025-01-30T00:39:27Z",
    "github_url": "https://github.com/account_name/repository_name"
}
```

## Backlinks
[Hire Python Developers](https://hng.tech/hire/python-developers)

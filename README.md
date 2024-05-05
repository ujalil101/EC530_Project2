# Smart Document Analyzer

## Overview
This is a web application built with Flask that allows users to upload PDF files for analysis. The application provides functionalities for user registration, login, file upload, and analysis of the uploaded PDF files.

## Features
- **User Authentication**: Users can sign up for an account and log in securely.
- **File Upload**: Users can upload PDF files to the application.
- **PDF Analysis**: The uploaded PDF files are analyzed using natural language processing (NLP) techniques to generate a summary, sentiment analysis, and extract keywords.
- **Result Display**: Users can view the analysis results on a separate page.

## Installation with Docker

1. Clone this repository to your local machine:
2. Navigate to the root directory of the project:
    ```
    cd <project_directory>
    ```
3. Build the Docker image using the provided Dockerfile:
    ```
    docker build -t pdf-analyzer .
    ```
4. Once the image is built successfully, you can run the Docker container:
    ```
    docker run -d -p 5000:5000 pdf-analyzer
    ```
5. Access the application in your web browser at `http://localhost:5000`.

## Installation with Git 
1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
    ```
    pip3 install -r requirements.txt
    ```
## Usage
1. Run the Flask application:
    ```
    python3 app.py
    ```
2. Access the application in your web browser at `http://localhost:5000`.

## File Structure
- **app.py**: Contains the Flask application code including routes and main server logic.
- **templates/**: Contains HTML templates for the user interface.
- **Modules/**: Contains Python modules for various functionalities such as user authentication, file upload, and NLP analysis.
- **Tests/**: Contains the Python tests for the modules.

## Configuration
- You can configure the MongoDB database connection in the `app.py` file by setting the appropriate connection parameters.
- Ensure to set a strong secret key for the Flask application in the `app.secret_key` attribute for session security.

## License
This project is licensed under the MIT License


# Smart Document Analyzer

<img width="450" alt="Login" src="https://github.com/ujalil101/EC530_Project2/assets/74789609/ba687fa9-fcb7-4ebd-b309-4bf331199a9f">
<img width="463" alt="Upload" src="https://github.com/ujalil101/EC530_Project2/assets/74789609/5a9706f9-18f5-4965-9161-9f69545285b8">
<img width="580" alt="Analysis" src="https://github.com/ujalil101/EC530_Project2/assets/74789609/9a6dc4d5-a526-428f-9cc9-2646b0d89afd">


## Overview
This is a web application built with Flask that allows users to upload PDF files for analysis. The application provides functionalities for user registration, login, file upload, and analysis of the uploaded PDF files.

Upon signing up and logging in, users can submit a PDF document and receive an in-depth analysis, consisting of a summary, sentiment analysis, and extracted keywords.

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


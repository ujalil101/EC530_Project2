# Simple Flask API Documentation

Simple Flask application with basic authentication and file upload functionality

## Endpoints

### Authentication

#### Login

- **URL:** `/login`
- **Method:** `POST`
- **Description:** Authenticates a user.
- **Request Parameters:**
  - `username` (string): User's username.
  - `password` (string): User's password.
- **Responses:**
  - `200 OK`: Successful authentication. Redirects to file upload page.
  - `400 Bad Request`: Invalid username or password.

#### Signup

- **URL:** `/signup`
- **Method:** `POST`
- **Description:** Registers a new user.
- **Request Parameters:**
  - `username` (string): New user's username.
  - `password` (string): New user's password.
  - `confirm_password` (string): Confirmation of the password.
- **Responses:**
  - `200 OK`: Successful registration. Redirects to login page.
  - `400 Bad Request`: Error occurred during signup.

### File Upload

#### Upload File

- **URL:** `/upload`
- **Method:** `POST`
- **Description:** Uploads a PDF file.
- **Request Parameters:**
  - `file` (file): PDF file to upload.
- **Authentication Required:** Yes
- **Responses:**
  - `200 OK`: File uploaded successfully. Redirects to success page.
  - `400 Bad Request`: Invalid file format. Please upload a PDF file.
  - `401 Unauthorized`: User not logged in.

#### Success

- **URL:** `/success`
- **Method:** `GET`
- **Description:** Success page indicating file upload success.
- **Responses:**
  - `200 OK`: Success message displayed.
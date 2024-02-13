# API DOCUMENTATION

A simple document to outline endpoints and functionalities of  the APIs that will be used for the upload and training modules in this project. 


## 1. Create Project

**Endpoint:** `POST /projects`

**Description:** Create a new ML project

**Parameters:**
- `user_id`: Unique identifier of the user.
- `project_name`: Name of the project.
- `task`: Task type (`image_classification` or `object_detection`).

## 2. Upload Data

**Endpoint:** `POST /projects/{project_id}/data`

**Description:** Uploads images for training

**Parameters:** Image data

## 3. Upload Labels

**Endpoint:** `POST /projects/{project_id}/labels`

**Description:** Uploads labels or class data for images

## 4. Add/Remove Data

**Endpoint:** `PUT /projects/{project_id}/training_data`

**Description:** Adds or removes training data

**Parameters:** Image data

## 5. Get Training Stats

**Endpoint:** `GET /projects/{project_id}/training_stats`

**Description:** Gets training stats

## 6. Train Model

**Endpoint:** `POST /projects/{project_id}/train`

**Description:** Train the model using data

**Parameters:** Image data

## 7. Deploy Model

**Endpoint:** `POST /projects/{project_id}/deploy`

**Description:** Deploys the model for inference

**Parameters:** Image data

## Responses for each API will result in:
- `200`: Successful response
- `400`: Invalid request
- `500`: Error

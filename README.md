# IMB Product Store Test Project
*For imb-full-stack-code-challenge-req97073*

**By: Alex Schell**
![example screenshot](https://i.imgur.com/NQyHsd0.png)
## Summary 
This project is a submission to fufill the requirments given the [IS-24 Full Stack Developer Postion Challange](https://github.com/bcgov/citz-imb-full-stack-code-challenge-req97073). It allows users to view, and manage products store in a simulated database, using a web front end, surfaced by an API. For this project, JS/React was used for the frontend, while Python was used for the backend.

## Goals/User Stories
- [x] User Story One: List of all products
    - Should be first thing seen by users when logging in
- [x] User Story Two: Adding Products
    - User can click the "Add item" button to open interface to add an item.
- [x] User Story Three: Editing Products
    - User can click edit button on each entry and show
- [x] Bonus User Story Four: Search by Scrum Master
    - User can search for products for which a person was a scrum master on
- [x] Bonus User Story Five: Search by Dev
    - User can search for products for which a person was a developer on

This project also features Swagger/OpenAPI documentation.

## Requirements
This project uses the following
 - **Javascript** for the frontend
 - **Python** for the API/Backend
 - **Node.js** for serving project
 - **React** to add state and improve frontend
 - **Flask** for API 
 - **Flask-CORS** 
 - **flasgger** To handle Swagger API documentation

The installation and maintenance of these are handled by pipenv and npm for the backend and frontend, respectively.

## Setup
Assumes Node/JS is set up
- Install Python 
- Install React
- Run `npm ci` in the main folder to load the requriments from `package.json`
- Get [https://pipenv.pypa.io/en/latest/](pipenv) by running `pin install pipenv`

The frontend and backend should now be ready to run!

## Running
First, to run the backend use `pipenv run python index.py`, which will ensure all packages are upto date and installed, before running the API service. To run the frontend use `npm start` to spin up the node server and automatically, the web app should open automatically. 

The frontend should be available at http://localhost:5000/ while the backend will be surfaced at http://localhost:3000/api.

## Swagger Documentation
Swagger documentation is surfaced while the API is running at http://localhost:3000/api/api-docs/

## Architecture
TODO


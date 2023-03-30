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

https://user-images.githubusercontent.com/10998311/228972609-d550edad-f9c9-4532-8afd-a6adb678aad1.mp4


- [x] User Story Three: Editing Products
    - User can click edit button on each entry and show

https://user-images.githubusercontent.com/10998311/228971796-1e549638-61b7-4421-86d2-41113d682d9f.mp4

- [x] Bonus User Story Four: Search by Scrum Master
    - User can search for products for which a person was a scrum master on

https://user-images.githubusercontent.com/10998311/228971864-7c160bc9-bdd7-4e5b-83c7-1d3059617443.mp4


- [x] Bonus User Story Five: Search by Dev
    - User can search for products for which a person was a developer on

https://user-images.githubusercontent.com/10998311/228971910-b9d3881a-6fc9-4c1c-87a3-ba5b840dcb84.mp4

- [x] Can also delete product from the database

https://user-images.githubusercontent.com/10998311/228971961-c6a6ee82-f9ad-460d-865f-10cfa7cad442.mp4



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

If for some reason the backend .json files become corrupted, they can be fixed by setting `generateDBs` to `true` in the index.py file. This will call to generate fresh new databases.

## Swagger Documentation
Swagger documentation is surfaced while the API is running at http://localhost:3000/api/api-docs/

## Architecture
![Untitled Diagram drawio](https://user-images.githubusercontent.com/10998311/228973658-c5789a30-9667-4e1d-9347-cd83b4a3a438.png)

The current architecture is set to be object-oriented and component based. For example, the API does not need information about the database itself or the storage of data in them, as data writing is handled by the backend python functions (product.py and personStore.py), and storing to JSON files is handled by the databaseHandler. This allows for the easy addition/modification of parts when needed, such as accessing new data, or moving to an actual database. 

Similarly in the frontend, most elements are handled as React components, with HTML and functionality stored in the same area. This allows for easier building and adding of page elements, as well as reuse in other parts. For example, each row in the table is a React element, reducing the lines of code, and making deletion/editing of data require less interconnection between parts. 


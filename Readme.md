## Sample CRUD app

   - Flask application with CRUD operations for managing a players collection in MongoDB

     ### Explanation of the Flow
    
      1. **app.py**: The main application file where the Flask app is created. It loads environment variables and registers the routes from `player_routes.py`.

      2. **routes/player_routes.py**: Defines the routes for the CRUD operations. It uses a Blueprint to organize routes related to the player resource.

      3. **controllers/player_controller.py**: Contains the logic for the CRUD operations. It connects to MongoDB, performs operations, and returns responses.

      4. **controllers/memory_controller.py**: This setup provides an alternative set of CRUD operations that do not require a database, using an in-memory dictionary for storage.

---------------------------------------

## Running the Application and Tests

1. Install required packages:

    ```bash
    sudo apt-get update && sudo apt-get install python3 python3-pip -y 
    pip3 install flask pymongo flask-pymongo python-dotenv pytest pytest-cov coverage venv
    ```

1. Create and Activate Venv
    
    ```bash
    ### 1.1) Create a Virtual Environment
    python -m venv devenv
       ## OR 
    virtualenv devenv

    ### 1.2) Activate the Virtual Environment
    # On Windows:
    devenv\Scripts\activate
   
    # On macOS/Linux:
    source devenv/bin/activate

    # save required package in req.txt
    pip freeze > req.txt

    # When you are done, you can deactivate the virtual environment by simply running:
    deactivate
    ```

1. **Run MongoDB Container**:

   ```bash
   docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=myusername \
   -e MONGO_INITDB_ROOT_PASSWORD=mypassword mongo:latest

   docker stop mongodb
   ```


2. Run the Flask application:
    
    ```bash
    # Install packages
    pip install -r req.txt
    python app.py
    ```
---------------------------------------------


## Running Tests and Generating Coverage Report

1. Run only Unit tests

    ```bash
    export PYTHONPATH=$(pwd)
    pytest
    ```

1. **Run the Tests with Coverage**:

   ```bash
   coverage run -m unittest discover -s tests
   ```

    - -m unittest discover discovers and runs all tests in the tests directory.

1. **Generate the Coverage Report**:

   ```bash
   # coverage report` generates a textual report
   coverage report -m
   
   # `-m` shows the missing lines of code.
   ```


1. **Generate an HTML Coverage Report**:

   ```bash
   coverage html
   ```
   
   This will create an `htmlcov` directory with the HTML report. Open `htmlcov/index.html` in a web browser to view the coverage details.

4. **Coverage Explanation**

   - Coverage measures how much of your code is exercised when running your tests. 
    
      This helps identify parts of the code that are not tested, ensuring better quality and reliability of the codebase.

        1. **Line Coverage**: Indicates the percentage of code lines executed during tests.
     
        1. **Branch Coverage**: Shows the percentage of code branches (e.g., `if` statements) executed.
     
        1. **Missing Lines**: Lists lines of code not executed during tests.

       Using coverage reports, you can improve your tests to cover more scenarios, resulting in more robust and error-free applications.   


-----------------------------------------

## Running the Flask App with Docker

1. **Build the Docker Image**:

   ```bash
   docker build -t my_flask_app .
   ```

2. **Run the Flask App Container**:

   ```bash
   docker run -d --name flask_app -p 5000:5000 --env MONGO_URL=mongodb://host.docker.internal:27017 --env MONGO_USERNAME=myusername --env MONGO_PASSWORD=mypassword  my_flask_app
   ```

-------------------------------

## Sample curl Requests

1. **Create a Player**

    ```bash
    curl -X POST http://127.0.0.1:5000/api/player \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Lionel Messi",
        "matches": 900,
        "goals": 860,
        "assists": 900,
        "club": "Inter Miami",
        "age": 40,
        "country": "Argentina"
    }'
    ```

2. **Get All Players**

    ```bash
    curl -X GET http://127.0.0.1:5000/api/players
    curl -X GET http://127.0.0.1:5000/memory/players
    ```

1. **Get a Single Player**

    ```bash
    curl -X GET http://127.0.0.1:5000/api/player/<player_id>
    ```
    Replace `<player_id>` with the actual player ID.

1. **Update a Player**

    ```bash
    curl -X PUT http://127.0.0.1:5000/api/player/<player_id> \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Lionel Messi",
        "matches": 910,
        "goals": 870,
        "assists": 910,
        "club": "Inter Miami",
        "age": 41,
        "country": "Argentina"
    }'
    ```
    Replace `<player_id>` with the actual player ID.

1. **Delete a Player**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/api/player/<player_id>
    ```
    Replace `<player_id>` with the actual player ID.

    This setup provides a well-structured foundation for CRUD operations on a `players` collection in MongoDB using Flask.

----------------------------------------------

[Unit Test Code Explanation](./docs/test_explantion.md)

[Pytest Basic Command Usage](./docs/pytest_usage.md)
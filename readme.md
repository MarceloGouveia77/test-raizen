## Weather API

### How to execute
    - first step: create your own .env config copying the format of .env.example
    - if you have docker & docker compose: 
        - just run "docker-compose up"
    - if don't have docker and docker compose:
        - install python >= 3.10
        - run "pip install -r requirements.txt"
        - after install all requirements and set the variables in .env, just start fastAPI with:
            - uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload

### Docs
    - /api/v1/docs - for swagger version
    - /api/v1/redocs - for openAPI version

### Test API Endpoint - With insomnia client
    - import the file "insomnia.json" in insomnia 
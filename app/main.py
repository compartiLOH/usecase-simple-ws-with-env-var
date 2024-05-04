from fastapi import FastAPI
import os

app = FastAPI()

# Retrieve the value of EXAMPLE_ENV_VAR environment variable
example_env_var = os.getenv("EXAMPLE_ENV_VAR", "default_value")

@app.get("/")
async def root():
    return {"message": "Hello World", "example_env_var": example_env_var}

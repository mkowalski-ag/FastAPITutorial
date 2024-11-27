from fastapi import FastAPI

# create a new app
app = FastAPI()

# define a path in fastapi
@app.get('/')
def root():
    return ("Hello World from Python")
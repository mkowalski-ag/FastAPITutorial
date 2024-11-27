from fastapi import FastAPI

# create a new app
app = FastAPI()

# create empty list to use for routes
dogs = []

# define a path in fastapi
@app.get('/')
def root():
    return ("Hello World from Python")

@app.post('/dogs')
def create_dog(dog: str): #query parameter
    dogs.append(dog)
    return dogs
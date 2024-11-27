from fastapi import FastAPI, HTTPException
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
# currently not a json payload

@app.get('/dogs')
def get_dog():
    return dogs
# working

@app.get('/dogs/{dog_id}') # /dogs/1 or /dogs/6 etc
def get_dog(dog_id: int) -> str:
    if dog_id < len(dogs):
        return dogs[dog_id]
    else:
        raise HTTPException(status_code=404,
                            detail=f"Dog {dog_id} not found")
# working

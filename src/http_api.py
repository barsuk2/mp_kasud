from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'egor'}

@app.get('/123')
def get_roads():
    "asdasdasd"
    return {'Hello': '123123!'}

# if __name__ == "__main__":
#     uvicorn.run("http_api:app", host="0.0.0.0", port=5000, reload=True)
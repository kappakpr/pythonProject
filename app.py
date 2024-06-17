from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from transformers import pipeline
from starlette.responses import FileResponse

## create a new FASTAPI app instance
app=FastAPI()

# Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")


@app.get("/")
def home():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    # return {"message":"Hello World"}
    return FileResponse('./static/index.html')

# Define a function to handle the GET request at `/generate`


@app.get("/generate")
def generate(text:str):
    ## use the pipeline to generate text from given input text
    print(text)
    output=pipe(text)

    ## return the generate text in Json reposne
    return {"generated_text":output[0]['generated_text']}
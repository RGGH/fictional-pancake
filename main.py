from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.neural_network import MLPRegressor
import numpy as np

app = FastAPI()

output = {}

origins = [
    "http://redandgreen.co.uk/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## questionaire data from csv
data = np.loadtxt(open("questions.csv", "rb"), delimiter=",", skiprows=1)

## one liner
# fit first 4 v 5th(last)
# study per week, years, books, projects, earn, rating
neural_net = MLPRegressor(max_iter=10000).fit(data[:, :-1], data[:, -1])


class request_body(BaseModel):
    weeks: int
    years: int
    books: int
    projects: int
    earn: int


@app.post("/pancake/vars")
def vars(data: request_body)->dict:
    ## result
    rating = neural_net.predict([[data.weeks,data.years,data.books,data.projects,data.earn]])
    output['rating']= str(rating)
    return(output)




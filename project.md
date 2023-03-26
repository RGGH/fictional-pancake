# ML REST API using FastAPI, Webdock, HTML and JavaScript

---

<span style="color:red">Introduction</span>
-------------------------------------------

TL;DR
Rather than use Flask, Heroku and the usual CRUD example I wanted to demonstrate how to use Python code with a machine learning example, and create a front end using an html page served from my existing, remotely hosted domain: redandgreen.co.uk

### Prerequisites:

- Python Coding skills
- Familiarity wil ML supervised learning
- html / javascript skills
- Webdock Python web hosting
- What this article will cover:
- Create a Rest API with FastAPI
- Integrate a Neural Network
- Consume API with POST request using JavaScript

---

<span style="color:green">Start with the Python code</span>

## Import required modules

- FastAPI
- pydantic import BaseModel
- sklearn
- numpy

FastAPI has excellent documentation, https://fastapi.tiangolo.com/
According to the Author : FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. We will make use of tiangolo's Dockerfile later on.

from fastapi import FastAPI
This is used for every FastAPI project, you will instantiate a class with it in due course.

from fastapi.middleware.cors import CORSMiddleware
This line is one that you won't find in all tutorials, it's essential for deploying to a remote host otherwise you will encounter 'CORS' errrors. CORS is used to ensure both that the script comes from an origin that you expect to be making valid requests to the cross-origin resource and that the browser won't just allow every script it loads to contact that resource.

from pydantic import BaseModel
Pydantic with FastAPI allows you to declare parameters with type hints and you get: Editor support and Type checks.

from sklearn.neural_network import MLPRegressor
https://scikit-learn.org/stable/index.html - we'll be using Regression - 'Predicting a continuous-valued attribute associated with an object.'

import numpy as np
Numpy is required by sklearn and we also use it to import our CSV data and format it into a suitable array

## Create an instance of the FastAPI class

app = FastAPI()
## Create an empty dictionary, we'll populate this later with output from our model

output = {}
## Allow CORS (for final deployment)

origins = [
    "http://redandgreen.co.uk"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
You will need to substitue you own domain name here, this will be the site you host the front end on

## import the 'training data'

## questionaire data from csv
data = np.loadtxt(open("questions.csv", "rb"), delimiter=",", skiprows=1)
*If you're curious, this is just some very basic data:

WEEKS, YEARS, BOOKS, PROJECTS, EARN, RATING
20, 11, 20, 30 , 4000, 1500
12, 4, 0, 0, 1000, 1500
2, 0, 1, 10, 0, 1400
35, 1, 0, 0, 0, 100
This was initially inspired by an example in the "Python One Liners" book, but the data was within the code. Here I've separated the data, which is more real world, and also allows the same data to be shared with other code/models.

! If you have text within your training data you need to use syntax more like this:

X = np.genfromtxt("grades.csv", delimiter=",", dtype="S20)
When you come to print a bytes object you'll need to use:

print(str(student_1,'utf-8'))
## Create the model - MLPRegressor

# one liner
# fit first 4 v 5th(last)
# study per week, years, books, projects, earn, rating
neural_net = MLPRegressor(max_iter=10000).fit(data[:, :-1], data[:, -1])
## Create the Base Model - to take advantage of the typing:

class request_body(BaseModel):
    weeks: int
    years: int
    books: int
    projects: int
    earn: int
## Use the numpy array called "data" and pass into request body

@app.post("/vars")
def vars(data: request_body)->dict:
    ## result
    rating = neural_net.predict([[data.weeks,data.years,data.books,data.projects,data.earn]])
    output['rating']= str(rating)
    return(output)
we get a Python dictionary as output, with "rating" : "12345" or some such integer.

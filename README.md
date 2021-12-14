# API-3
html, javascript, FastAPI

# remember to add code in fastapi to allow CORS

    import uvicorn
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from pydantic import BaseModel
    from sklearn.neural_network import MLPRegressor
    import numpy as np

    app = FastAPI()

    output = {}

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
    
    ---
    
    https://www.stackhawk.com/blog/configuring-cors-in-fastapi/

---

Try the code here : http://redandgreen.co.uk/indexx.html

---

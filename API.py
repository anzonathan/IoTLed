from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#allow all connections: Specify Ip address for security
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


switchState = 0; 

@app.get("/")
def readRoot():
    return {'State':'API Is connected'}

@app.get("/state/")
def readRoot():
    return {'switchState':switchState}


@app.post("/on/")
def switchOn():
    switchState = 1
    return {'switchState':switchState}

@app.post("/off/")
def switchOff():
    switchState = 0
    return {'switchState':switchState}
from fastapi import FastAPI
import subprocess

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK4"}

@app.get("/run_linux_comand")
def deploy():

    subprocess.call(['sh', 'scripts/deploy.sh'])
    return {"message": "OK4"}

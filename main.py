from fastapi import FastAPI
from bot import get_userDetail as getUser

app = FastAPI()

@app.get('/')
async def root():
    return 'See /docs for Information!'




@app.get('/u/{username}')
async def get_user(username):
    dataF = getUser(str(username))
    return [dataF,dataF,dataF]
from secrets import token_hex

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, status
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from starlette.middleware.sessions import SessionMiddleware

from utilities.templatesRender import Render
from utilities.ConnectionManager import Manager


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="cf9a7b29d8472fc6b87e2269bd49bbc261914d37a15e0742438d15e02f37f190")
websocket_list = Manager()

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    print(__name__ , request.session.items())
    authToken = token_hex(16)
    headers = {
        "set-cookie": f"authToken={authToken}"
    }
    return HTMLResponse(headers=headers,content=Render('index.html', {"user_name":"TESTE", "title":"Título h1"}), status_code=200)

@app.websocket("/ws/{user_name}")
async def websocket_endpoint(websocket: WebSocket, user_name: str):
    await websocket_list.connect(websocket, user_name.lower())
    try:
        while True:
            data:dict = await websocket.receive_json()
            try: 
                authToken = data.get("connectionParams").get("authToken")
                print('Token de autenticação WS: ', authToken)
            except:
                print("Payload: ", data)
            await websocket_list.broadcast(data, user_name.lower())
    except WebSocketDisconnect:
        websocket_list.disconnect(websocket, user_name.lower())
    return None
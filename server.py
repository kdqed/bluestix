import aiohttp
from aiohttp import web
import pyautogui



async def websocket_handler(request):
  ws = web.WebSocketResponse()
  await ws.prepare(request)
  async for msg in ws:
    if msg.type == aiohttp.WSMsgType.TEXT:
      try:
        chunks = msg.data.split(" ")
        action = chunks[0].strip()
        keys = chunks[1:]
        for key in keys:
          if action=="p":
            print("p", key)
            pyautogui.keyDown(key)
          elif action=="r":
            print("r", key)
            pyautogui.keyUp(key)  
      except Exception as e:
        print(e)
    elif msg.type == aiohttp.WSMsgType.ERROR:
      print('ws connection closed with exception %s' % ws.exception())      
  print('websocket connection closed')
  return ws
  
app = web.Application()
app.add_routes([
  web.get('/ws', websocket_handler),
  web.static("/", "static", show_index=True)
])

if __name__=="__main__":
  web.run_app(app)  

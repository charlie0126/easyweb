# easyweb
a light-weighted tool used to create asynchronous http servers

Example:
```
from easyweb.easyweb import WebApplication

def index(request: Request):
  print("index called")
  print(request.protocol)
  raise Http403


  class Test(WebApplication):
    urlpatterns = [
            path("GET", "/", index)
        ]

run(Test, "127.0.0.1", 8000)
```

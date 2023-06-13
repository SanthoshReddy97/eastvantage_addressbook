# eastvantage_addressbook

### start the server

Create a virtual env

```
virutalenv venv
source ./venv/bin/activate
```

Install the requirements
```
pip3 install -r requirements.txt
```

Start the server
```
uvicorn app.main:app --reload
```

Swagger UI endpoint http://127.0.0.1:8000/docs

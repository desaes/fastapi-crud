# https://stackoverflow.com/questions/70535711/how-to-upload-both-file-and-json-data-using-fastapi

import requests

url = "http://127.0.0.1:5000/submit"
files = [
    ("files", open("test_files/a.txt", "rb")),
    ("files", open("test_files/b.txt", "rb")),
]
payload = {"name": "foo", "point": 0.13, "is_accepted": False}
resp = requests.post(url=url, params=payload, files=files)
print(resp.json())

import requests
res = requests.post('http://localhost:5000/1234', json={"data":[{'s':0 , 'd':1, 'w':10}]})
if res.ok:
    print res.json()

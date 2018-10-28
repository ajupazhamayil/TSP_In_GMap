import requests
res = requests.post('http://localhost:5000/1834', json={"size":4, "data":[{'s':0 , 'd':1, 'w':3},{'s':1 , 'd':0, 'w':3},{'s':0 , 'd':8, 'w':6},{'s':8 , 'd':0, 'w':6},{'s':0 , 'd':3, 'w':1},{'s':3 , 'd':0, 'w':1},{'s':1 , 'd':8, 'w':8},{'s':8 , 'd':1, 'w':8}, {'s':1 , 'd':3, 'w':8},{'s':3 , 'd':1, 'w':8}, {'s':8 , 'd':3, 'w':5},{'s':3 , 'd':8, 'w':5}]})
if res.ok:
    print res.json()

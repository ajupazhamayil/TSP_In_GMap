import requests
res = requests.post('http://localhost:5000/1234', json={"num_points":4, "data":[{'s':0 , 'd':1, 'w':3},{'s':0 , 'd':2, 'w':6},{'s':0 , 'd':3, 'w':1},{'s':1 , 'd':2, 'w':8}, {'s':1 , 'd':3, 'w':2}, {'s':2 , 'd':3, 'w':5}]})
if res.ok:
    print res.json()

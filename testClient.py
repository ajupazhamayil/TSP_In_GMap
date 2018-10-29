import requests
res = requests.post('http://localhost:5000/solution', json={"size":4, "data":[{'S':0 , 'D':1, 'W':3},{'S':1 , 'D':0, 'W':3},{'S':0 , 'D':8, 'W':6},{'S':8 , 'D':0, 'W':6},{'S':0 , 'D':3, 'W':1},{'S':3 , 'D':0, 'W':1},{'S':1 , 'D':8, 'W':8},{'S':8 , 'D':1, 'W':8}, {'S':1 , 'D':3, 'W':8},{'S':3 , 'D':1, 'W':8}, {'S':8 , 'D':3, 'W':5},{'S':3 , 'D':8, 'W':5}]})
if res.ok:
    print res.json()

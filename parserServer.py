from flask import Flask, request, jsonify
import json
import subprocess as sp

app = Flask(__name__)

@app.route('/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    sp.call("./a.out")
    #print("Called the cpp function")
    with open('file.json', 'w') as f:
        for i in content['data']:
            temp=str(i['s'])+' '+str(i['d'])+' '+str(i['w'])
            f.write(temp)
    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host= '127.0.0.1',port=5000,debug=True)

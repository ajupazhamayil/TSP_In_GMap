from flask import Flask, request, jsonify
import json
import cppyy
cppyy.include("foo.h")
cppyy.load_library("foo")
from cppyy.gbl import Foo


app = Flask(__name__)

@app.route('/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print content['mytext']
    f=Foo()
    f.bar()
    with open('file.json', 'w') as f:
        f.write(json.dumps(content)) 
    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host= '127.0.0.1',port=5000,debug=True)

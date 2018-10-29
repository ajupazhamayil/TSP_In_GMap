
from flask import Flask, request, jsonify, render_template
import json
import subprocess as sp
import os
import sys

#PLZ REMEMBER change key and json parsing in the frontend side

def replace_word(infile,old_word,new_word):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return render_template("index.html")



@app.route('/route', methods=['GET', 'POST'], strict_slashes=False)
def json_parser():
    mapToPoint={}
    pointToMap = {}
    content = request.json
    num_of_points = content["size"]
    print content
    replace_word("ABC_TSP.cpp","#define D 4","#define D "+str(num_of_points))
    print "replaced #define"
    flag = False


    uniqValue=0
    #make the map for points
    for i in content['data']:
	if (mapToPoint.get(str(i['S']), None)==None):
            mapToPoint[str(i['S'])] = str(uniqValue)
	    pointToMap[str(uniqValue)]=str(i['S'])
	    uniqValue=uniqValue+1
    print mapToPoint
    print pointToMap

    with open('file.json', 'w') as f:
        for i in content['data']:
	    temp = ""
	    if flag==True:
	    	temp=temp+"\n"
	    flag = True
            temp=temp+mapToPoint[str(i['S'])]+' '+mapToPoint[str(i['D'])]+' '+str(i['W'])
            f.write(temp)


    sp.call(["g++","ABC_TSP.cpp"])
    sp.call("./a.out")
    print "completed code running"
    replace_word("ABC_TSP.cpp","#define D "+str(num_of_points),"#define D 4")
    #print("Called the cpp function")
    with open('fileout.json', 'r') as f:
        result = f.readline()
	temp=[]
	for r in result.split(" "):
	    t = pointToMap[r]
	    temp.append(int(t))
    return jsonify(route = temp)

if __name__ == '__main__':
    app.run(host= '127.0.0.1',port=5000,debug=True)

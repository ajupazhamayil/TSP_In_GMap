from flask import Flask, request, jsonify, render_template
import json
import subprocess as sp
import os

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



@app.route('/solution', methods=['GET', 'POST'], strict_slashes=False)
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
	if (mapToPoint.get(str(i['s']), None)==None):
            mapToPoint[str(i['s'])] = str(uniqValue)
	    pointToMap[str(uniqValue)]=str(i['s'])
	    uniqValue=uniqValue+1
    print mapToPoint
    print pointToMap

    with open('file.json', 'w') as f:
        for i in content['data']:
	    temp = ""
	    if flag==True:
	    	temp=temp+"\n"
	    flag = True
            temp=temp+mapToPoint[str(i['s'])]+' '+mapToPoint[str(i['d'])]+' '+str(i['w'])
            f.write(temp)


    sp.call(["g++","ABC_TSP.cpp"])
    sp.call("./a.out")
    print "completed code running"
    replace_word("ABC_TSP.cpp","#define D "+str(num_of_points),"#define D 4")
    #print("Called the cpp function")
    with open('fileout.json', 'r') as f:
        result = f.readline()
	temp=""
	for r in result.split(" "):
	    temp=temp+str(pointToMap[r])+" "
    return jsonify({"result":temp})

if __name__ == '__main__':
    app.run(host= '127.0.0.1',port=5000,debug=True)

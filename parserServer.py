from flask import Flask, request, jsonify
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

@app.route('/<uuid>', methods=['GET', 'POST'])
def json_parser(uuid):
    content = request.json
    num_of_points = content["num_points"]
    print num_of_points
    replace_word("ABC_TSP.cpp","#define D 0","#define D "+str(num_of_points))
    print "replaced #define"
    flag = False
    with open('file.json', 'w') as f:
        for i in content['data']:
	    temp = ""
	    if flag==True:
	    	temp=temp+"\n"
	    flag = True
            temp=temp+str(i['s'])+' '+str(i['d'])+' '+str(i['w'])
            f.write(temp)


    sp.call(["g++","ABC_TSP.cpp"])
    sp.call("./a.out")
    print "completed code running"
    replace_word("ABC_TSP.cpp","#define D "+str(num_of_points),"#define D 0")
    #print("Called the cpp function")
    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host= '127.0.0.1',port=5000,debug=True)

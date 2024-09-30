import os 
import json
MY_DATE=None

def NewFile(*param):
    with open (MY_DATE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def ReadFile():
    with open(MY_DATE,"r")as rf:
        return json.load(rf)
def AddData(*info):
    with open (MY_DATE,'r+') as frw:
        json.dump(info[0],frw,indent=2)

def chekFile(*param):
    data=list(param)
    if (len(param)):
        data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])
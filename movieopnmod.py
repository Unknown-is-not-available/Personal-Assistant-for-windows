import os
import subprocess

def movies(cmd):
    emt=[]
    opn=cmd
    vid="cd E:\\\"Code 13005\" && es -sort size-descending "+opn+" |findstr /i \""+opn+"\" > filename2.txt"
    
    subprocess.call(vid,shell=True)
    a=open("filename2.txt",'r')
    for i in a:
        emt.append(i)
    

    lst=emt[0].lower().split('\\')
    
    m=str(lst.pop(-1))

    path=""
    for i in lst:
        path=path+i+'\\'
        
        
    cmd3='cd '+path+' && "'+m+'\"'
    print(cmd3)
    subprocess.call(cmd3,shell=True)

#movies("my hero 10")

from googlesearch import search
import subprocess
def gserch(cmd):
    
    lst=[]
    engine=cmd
    ser=search(engine,num_results=1)
    for i in ser:
        
        lst.append(i)
    cmd="start "+lst[0]

    subprocess.call(cmd,shell=True)
#gserch('laptop')

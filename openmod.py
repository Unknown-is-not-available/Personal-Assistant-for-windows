from taskdictionary import com
import subprocess
def opens(cmd):
    
    emt=[]
    z=cmd
    pn=cmd

    for subtuple in com.keys():
        if z in subtuple:
            pn=com[subtuple][0]

    opn=pn
    app="cd E:\\\"Code 13005\" && es -ww "+opn+".exe |findstr /e /i \"\\\\"+opn+".exe\" > filename.txt"
    
    subprocess.call(app,shell=True)
    a=open("filename.txt",'r')
    for i in a:
        emt.append(i)
    


    lst=emt[0].lower().split('\\')
    lst.remove(opn+'.exe\n')
    
    path=""
    for i in lst:
        path=path+i+'\\'
        

    cmd3="cd "+path+" && start "+opn+".exe"
    subprocess.call(cmd3,shell=True)
    print(cmd3)
    
    


#strt="start "+emt[0]
#print(strt)
#os.system(',cmd /c'+strt)
#opens('notepad')

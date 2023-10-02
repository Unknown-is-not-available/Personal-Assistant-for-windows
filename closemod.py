import csv
import subprocess
def closes(cmd):
    apnme=cmd
    cmd="tasklist /v /fi \"status eq running\" /fo csv | find /i \""+apnme+"\" > filename.csv "
    subprocess.call(cmd,shell=True)
    f=open("filename.csv",newline='')
    a=csv.reader(f)
    for i in a:
        print(i[1])
    tskill="tskill "+i[1]
    print(tskill)
    subprocess.call(tskill,shell=True)
#closes("task manager")

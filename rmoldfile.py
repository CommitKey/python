import os, time, sys, subprocess
os.chdir(os.getcwd()+'/tmp/')
path = os.getcwd()
out = subprocess.check_output("ls -l", shell = True)

ahora = time.time()
dias = 5
fechaanterior = ahora - dias * 86400
for f in os.listdir(path):
    if os.stat(f).st_mtime < fechaanterior:
        if os.path.isfile(f):
            f = os.path.join(path, f)
            print('Se borrará el fichero: ',f)
            #os.remove(f)
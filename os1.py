import os
cwd=os.getcwd()
print("current working directory:  ",cwd)
os.chdir('../') 
print(cwd)
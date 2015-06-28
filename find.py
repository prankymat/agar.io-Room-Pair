import subprocess
from os.path import abspath, dirname, join

target = input("Please enter the target server address: ") or "167.114.209.34:1504"

def getInfo():
	path = abspath(join(dirname(__file__), 'connect.sh'))
	p = subprocess.Popen(path, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	return output.decode('utf-8').split('\n')[:-1]

def constructCommand(addr, key):
	return "connect('ws://" + addr + "','" + key + "')"

while True:
	result = getInfo()
	if result[0] == target:
		print(constructCommand(result[0], result[1]))
		break
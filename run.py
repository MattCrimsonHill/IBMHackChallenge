import os
def bashC(topic, problem):
	#tag = "Javascript"
	#problem = "window.open"
	bashCommand = "socli -t " + topic + " -q " + problem + " >> output.txt"
	print(bashCommand)
	return os.system(bashCommand)
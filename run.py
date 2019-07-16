import os
import random
def bashC(topic, problem):
	#tag = "Javascript"
	#problem = "window.open"
	randomFile = str(random.randint(1, 100000)) + ".txt"
	bashCommand = "socli -q " + problem + " >> " + randomFile
	print(bashCommand)
	return randomFile
# create a wordlist contains 1000 random number between 00000000 and 99999999
import string , random , os , time

def crack(hs,wordlist):
	os.system(f"aircrack-ng {hs} -w {wordlist}")
hs_target = "hs.cap"
def getTried():
	d = ""
	with open("Tried.txt","r") as file :
		d = file.read()
	return d
d = getTried()
def isTried(s):
	global d
	# d = getTried()
	if s in d :
		return True
	else :
		return False

wordlists = os.listdir("wordlists")
completed = []
ignored = []
def saveToFile(c,filename="Tried.txt"):
	with open(filename,"w") as file :
		for i in c :
			file.write(i + "\n")

for item in wordlists[5:] : # skip first 5 because of size
	a = input(f"Try with '{item}' ? (0=No 1=Yes)")
	if a == "1" :
		if not isTried(item):
			# begin cracking
			crack(hs_target,"wordlists/" + item)
			completed.append("wordlists/" + item)
			saveToFile(completed)
		else :
			input(f"Skipping {item} (already tried")
		
	else :
		ignored.append(item)
		saveToFile(item,filename="ignored.txt")

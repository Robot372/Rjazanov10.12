from modul import* 

### text to speach
#from gtts import gTTS
#import os
#s=gTTS(text="Tallinn", lang="et", slow=True).save("heli.mp3")
#os.system("heli.mp3")
###

Capitals={}
with open("Cap.txt","r") as f:
	for i in f: 
		k,v=i.strip().split("-") 
		Capitals[k.strip()]=v.strip() 

while True:
	c=input("Otsing sõna sõnavaras - 1, muutma sõna tähendus - 2, test - 3, välja - 4")
	if c=="1":
		ans,a=find_word(Capitals)
		print(ans)
		if ans=="See sõna ei olema": 
			b=input("Kas te tahate lisa sõna sõnavars, 1-jah 2-ei >>> ")
			if b=="1": 
				Capitals=add_word(Capitals,a) 
			else:
				pass
		else:
			pass
	elif c=="2":
		Capitals=change_smth(Capitals)
	elif c=="3":
		result=testingknoledge(Capitals)
		print("Sinu resultat on "+str(result)+"%") 
	elif c=="4": 
		with open("Cap.txt", "w") as f:
			for key, value in Capitals.items(): 
				f.write(key+"-"+value+"\n") 
		break
	else:
		print("See funktioon ei olema")

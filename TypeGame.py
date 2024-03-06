import time
import random
import wordies

class TypingGame:
	def __init__(self):
		self.misses=0
		self.words = wordies.wordsfor()
		
	def randomtext(self):
		self.text=""
		for i in range(10):
			self.text+=random.choice(self.words).lower()+" "
		self.text=self.text[:-1]
	
	def userinput(self):
		start=time.time()
		self.user=input("")
		end=time.time()
		self.sped=end-start
	
	def main(self):
		self.randomtext()
		print(self.text)
		self.userinput()
		print(self.aftertext())
		self.interface()
	
	def aftertext(self):
		self.text2=""
		
		if len(self.text)>len(self.user):
			uort=self.user
		else:
			uort=self.text
			
		for i in range(len(uort)):
			if self.text[i]!=self.user[i]:
				self.text2+=f"\033[91m{self.user[i]}\033[0m"
				self.misses+=1
			else:
				self.text2+=f"\033[32m{self.user[i]}\033[0m"
				
		if len(self.user)<len(self.text):
			self.text2+=f"\033[91m{self.text[len(self.user): ]}\033[0m"
		return self.text2
	
	def interface(self):
		self.misses+=len(self.text)-len(self.user)
		print(f"You have {self.misses} mistakes or {int(self.misses/(len(self.text)/100))}% of text")
		print(f'you managed in {round(self.sped, 2)} seconds')
		speed=len(self.user)/self.sped*60
		print(f'your typing speed is ~{int(speed)} symbols per minute')
		print('________________________')
		input(f"press 'enter' to one more try")
		print('________________________')
		self.main()
		
x=TypingGame()
x.main()
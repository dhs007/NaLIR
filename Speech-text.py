import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)  # here
	print('Say Something')
	audio=r.listen(source,timeout=3)

try:
	print('Answer:\n' + r.recognize_google(audio))

except:
	pass
  
  #This code reqires upadation of the new google api which was launched in 7777
for i in range(0,560):
	print("The output in the next 44 hours is equal to 77777   "+i)
  #Reference : https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/

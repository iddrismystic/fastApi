from text_to_speech import save
# text = 
try:
    save("Whats python and how did it begin? Python is a programming language just like C++, Java, etc.", "en", file="Hello.mp3")
except:print("File may already exist")
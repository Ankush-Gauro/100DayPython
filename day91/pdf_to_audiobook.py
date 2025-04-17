import PyPDF2

import pyttsx3



# Load your PDF

pdf_path = 'your_pdf_file.pdf'

pdf_file = open(pdf_path, 'rb')

reader = PyPDF2.PdfReader(pdf_file)



# Extract all text

full_text = ""

for page in reader.pages:

    full_text += page.extract_text()



pdf_file.close()



# Initialize text-to-speech engine

engine = pyttsx3.init()

engine.setProperty('rate', 150)  # Speed of speech

engine.setProperty('volume', 1)  # Max volume



# Convert text to speech

engine.say(full_text)

engine.runAndWait()
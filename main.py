import pyttsx3
import PyPDF2
import pdfplumber

speaker = pyttsx3.init()
speaking_rate = speaker.setProperty('rate', 150)
speaking_volume = speaker.setProperty('volume',0.75)

file = 'random_quotes.pdf'

pdf_file = open(file, 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

pages = len(pdf_reader.pages)

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
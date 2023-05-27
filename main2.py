import pyttsx3
import PyPDF2


speaker = pyttsx3.init()

pdfReader = PyPDF2.PdfReader(open('random_quotes.pdf', 'rb'))

for page_number in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_number].extract_text()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()
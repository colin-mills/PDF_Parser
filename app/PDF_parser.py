# credit for package https://pythonhosted.org/PyPDF2/
import PyPDF2

#pdfName = '/Users/colinmills/Desktop/Red2.pdf'
#takes in file name as input 
username = input("What is your username on your laptop")
pdfName = input("Please enter the PDF file ion your desktop that you would like to be read: ") # a relative filepath

pdfPath = "/Users/" + username + "/Desktop/" +pdfName

read_pdf = PyPDF2.PdfFileReader(pdfPath)

pages = input("How many pages, including the first, would you like there to be read.")

for page in pages:
    page = read_pdf.getPage(page)
    page_content = page.extractText()
    print(page_content)

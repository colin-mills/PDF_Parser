# credit for package https://pythonhosted.org/PyPDF2/
import PyPDF2
import os

#pdfName = '/Users/colinmills/Desktop/Red2.pdf'
#takes in file name as input 
username = input("What is your username on your laptop: ")
pdfName = input("Please enter the PDF file name your desktop that you would like to be read \n example \"sample.pdf\": ") # a relative filepath

pdfPath = "/Users/" + username + "/Desktop/" +pdfName

foundFile = os.path.isfile(pdfPath)

if foundFile:

    read_pdf = PyPDF2.PdfFileReader(pdfPath)

    pages = input("How many pages, including the first, would you like to be read: ")

    page_num = int(pages)

    for page in range(page_num):
        page = read_pdf.getPage(page)
        page_content = page.extractText()
        print(page_content)

else:
    print("Sorry \"" + pdfPath + "\" doesn't appear to be a correct file path. \nPlease correct and try again.")

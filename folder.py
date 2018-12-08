import reportlab as rl

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image

import csv

data_file = 'data.csv'

def import_data(data_file):
    attendee_data = csv.reader(open(data_file, encoding='utf-8'))
    for row in attendee_data:
        last_name = row[0]
        first_name = row[1]
        course_name = row[2]
        pdf_file_name = course_name + ' ' +  first_name + ' ' + last_name + '.pdf'
        generate_file(first_name, last_name, course_name, pdf_file_name)

def generate_file(first_name, last_name, course_name, pdf_file_name):
    attendee_name = first_name + " " + last_name
    c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
    
    #header text
    c.setFont('Helvetica', 48, leading=None)
    #500 from the bottom
    c.drawCentredString(415, 500, "Certificate of Completion")
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 450, "This certificate is presented to:")

    #name
    c.setFont('Helvetica', 34, leading=None)
    c.drawCentredString(415, 395,attendee_name)
    
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 350, 'For completing the following course')

    c.setFont('Helvetica', 34, leading=None)
    c.drawCentredString(415, 310, course_name)

    #image
    seal = 'seal.jpg'
    c.drawImage(seal, 325, 50, width=None, height=None)
    #render page
    c.showPage()
    print ('ok')
    #save all made pages
    c.save()
    
import_data(data_file)
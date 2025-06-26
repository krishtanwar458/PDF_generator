from fpdf import FPDF
from pathlib import Path
import glob

filepath = glob.glob('/Users/krishtanwar/Desktop/Python/PDF generator/Animal Txt files/*.txt')

animals = []

for i in filepath:
    animal = Path(i).stem
    # print(animal)
    animals.append(animal.capitalize())
    
pdf = FPDF(orientation='P', unit='mm', format='A4')

for i in animals:
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='BI')
    pdf.cell(h=15, w=50, txt=i, ln=1, align='L')

pdf.output('animal.pdf')
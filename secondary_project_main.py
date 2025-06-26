from fpdf import FPDF
from pathlib import Path
import glob

filepath = glob.glob('/Users/krishtanwar/Desktop/Python/PDF generator/Animal Txt files/*.txt')

animals = []

pdf = FPDF(orientation='P', unit='mm', format='A4')

for i in filepath:
    animal = Path(i).stem
    # print(animal)
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='BI')
    pdf.cell(h=15, w=50, txt=animal.capitalize(), ln=1, align='L')
    pdf.set_font(family='Times', size=10)

    with open(i, 'r') as file:
        content = file.read()
    pdf.multi_cell(w=190, h=8, txt=content, align='J')

pdf.output('animal.pdf')
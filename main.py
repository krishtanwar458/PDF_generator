from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', size=24, style='IB')
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align='L')
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    a = df['Pages'][index]
    for index in range(a-1):
        pdf.add_page()

pdf.output('output.pdf')

#a = df['Pages'][0]
#print(a)
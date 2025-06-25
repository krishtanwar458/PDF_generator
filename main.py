from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

#Setting 1 page and footer for main page
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', size=24, style='IB')
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align='L')
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    pdf.ln(260)
    pdf.set_font(family='Times', size=8, style='I')
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=10, txt=row['Topic'], ln=1, align='R')
    #Adding reccuring lines throughout the main pages - METHOD 1
    b = 32
    while b < 280:
        pdf.line(x1=10, x2=200, y1=b, y2=b)
        b = b+10

#Adding necessary number of pages as taken from the data.csv file and
#setting footer
    a = df['Pages'][index]
    for index in range(a-1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family='Times', size=8, style='I')
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=10, txt=row['Topic'], ln=1, align='R')
        #Adding recurring lines throughout the secondary pages - METHOD 2
        for i in range(15, 280, 10):
            pdf.line(10, i, 200, i)

pdf.output('output.pdf')

#a = df['Pages'][0]
#print(a)
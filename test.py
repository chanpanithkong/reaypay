from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass
                    
pdf = MyFPDF()
#First page
pdf.add_font('KhmerOS','','KhmerOS.ttf')
pdf.set_font('KhmerOS','',14)
pdf.add_page()
pdf.write_html("<p>គង់ ចាន់ផានិត</p>")
pdf.output('mypdf.pdf','F')
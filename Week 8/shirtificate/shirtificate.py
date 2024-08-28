from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        self.image('shirtificate.png', x=12, y=70, w=185)
        self.set_font('Helvetica', 'B', 48)
        self.cell(0, 60, 'CS50 Shirtificate', 0, 1, 'C')

    def name(self):
        self.set_font('Helvetica', size = 24)
        self.set_text_color(255, 255, 255)
        self.cell(0, 120, f"{input(f"Name: ")} took CS50", 0, 1, 'C')

    def create_pdf(self):
        self.add_page()
        self.name()
        self.output("shirtificate.pdf")

pdf = PDF()
pdf.create_pdf()

from fpdf import FPDF

class PDF: 
    def criar_pdf(self):

        lista = ["José Almeida", "00000000000","161,81", "SP", "RJ" ] 
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=20)
        pdf.cell(200, 10, txt="Dados de " +  lista[0] , ln=1, align="C")
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt= "N° da carteira de motorista:" + lista[1], ln=5, align="C")
        pdf.cell(200, 10, txt= "Salario em reais :" + lista[2], ln=6, align="C")
        pdf.cell(200, 10, txt= "Local de Partida:" + lista[3], ln=7, align="C")
        pdf.cell(200, 10, txt= "Destino:" + lista[4], ln=8, align="C")
		
        return (pdf.output("motorista.pdf"))
		
pdf = PDF()
pdf.criar_pdf()
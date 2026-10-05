from fpdf import FPDF


def main():
	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()
	pdf.set_font("helvetica", style="B", size=48)
	pdf.image("shirtificate.png", 20, 50, 175)
	pdf.cell(210, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
	pdf.set_text_color(255, 255, 255)
	pdf.set_font_size(20)
	pdf.cell(210, 125, "Daniel Cosmo took CS50", new_x="LMARGIN", new_y="NEXT", align="C")
	pdf.output("shirtificate.pdf")


if __name__ == "__main__":
	main()

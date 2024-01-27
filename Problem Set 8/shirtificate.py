from fpdf import FPDF


class Shitificate:
    def __init__(self, name):
        self.name = name
        self.shirtification()

    @classmethod
    def get(cls):
        name = input("Name: ").strip().title()
        return cls(name)

    def shirtification(self):
        pdf = FPDF()
        pdf.add_page(orientation="portrait", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("Helvetica", "", 55)
        pdf.cell(0, 58, txt="CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png",  x=10, y=80, w=190)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "", 25)
        pdf.cell(-190, 275, txt=f"{self.name} took CS50", align="C")
        pdf.output("shirtificate.pdf")


def main():
    Shitificate.get()


if __name__ == "__main__":
    main()

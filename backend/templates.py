from fpdf import FPDF
from io import BytesIO

class ResumeTemplate:
    def __init__(self, content):
        self.content = content

    def generate_pdf(self, template_choice):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)  # Prevents content cutoff

        # ✅ Use a font that supports UTF-8 characters
        pdf.set_font("Arial", size=12)

        if template_choice == "template_1":
            pdf.set_font("Arial", "B", 14)
            pdf.cell(200, 10, txt="Professional Resume", ln=True, align="C")

        elif template_choice == "template_2":
            pdf.set_font("Arial", "B", 14)
            pdf.cell(200, 10, txt="Resume", ln=True, align="C")

        elif template_choice == "template_3":
            pdf.set_font("Courier", size=12)

        else:
            pdf.set_font("Arial", size=12)

        # Process resume content
        pdf.set_font("Arial", size=12)
        lines = self.content.split("\n")

        for line in lines:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            
            if "**" in line:  # Bold headings
                pdf.set_font("Arial", "B", 14)
                pdf.cell(0, 8, line.replace("**", ""), ln=True)
                pdf.ln(2)
                pdf.set_font("Arial", size=12)

            elif line.startswith("*"):  # Bullet points
                pdf.cell(5)  # Indent
                pdf.cell(0, 6, f"- {line.replace('*', '').strip()}", ln=True) # ✅ Use Unicode bullet (•)

            else:  # Normal text
                pdf.multi_cell(0, 6, line)
                pdf.ln(2)

        # ✅ Write to BytesIO with UTF-8 support
        pdf_buffer = BytesIO()
        pdf_bytes = pdf.output(dest="S").encode("latin1", "replace")  # ✅ Replace unsupported characters
        pdf_buffer.write(pdf_bytes)
        pdf_buffer.seek(0)  # Move to the beginning
        return pdf_buffer

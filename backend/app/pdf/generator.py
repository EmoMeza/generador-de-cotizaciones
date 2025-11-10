from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from io import BytesIO

def generate_pdf(columns, rows):
    env = Environment(loader=FileSystemLoader("app/pdf/templates"))
    template = env.get_template("base.html")

    html_content = template.render(columns=columns, rows=rows)

    pdf_bytes = HTML(string=html_content).write_pdf()

    return pdf_bytes

from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    rendered_html = render_template('./pdf_template.html')  # Assuming you have a Jinja2 template for PDF content

    pdf_options = {
        'page-size': 'Letter',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }

    pdf = pdfkit.from_string(rendered_html, False, options=pdf_options)

    response = make_response(pdf)
    response.headers.set('Content-Disposition', 'attachment', filename='hello_world.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response

if __name__ == '__main__':
    app.run(debug=False)

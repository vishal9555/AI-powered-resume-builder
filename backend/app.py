import os
from flask import Flask, render_template,jsonify, request, send_file
from .generator import generate_resume_content
from .templates import ResumeTemplate
from io import BytesIO

# Specify the correct path to the templates folder
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend", "templates")
app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Debug: Print the templates folder path
print("DEBUG: Template folder is set to:", app.template_folder)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_data = request.get_json(silent=True) or request.form.to_dict()
        if not user_data:
            return jsonify({"error": "No data received"}), 400

        content = generate_resume_content(user_data)
        template_choice = user_data.get("template", "template_1")
        template = ResumeTemplate(content)

        pdf_buffer = template.generate_pdf(template_choice) 

        return send_file(pdf_buffer, as_attachment=True, download_name="resume.pdf", mimetype="application/pdf")
    return render_template("index.html")
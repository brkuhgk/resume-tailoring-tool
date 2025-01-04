from flask import Flask, request, jsonify, send_file
import os
import json
from convert_json import JsonConverter
from combine_jsondata import JsonCombiner
from generate_pdf import PdfGenerator

app = Flask(__name__)

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    data = request.json
    job_description = data.get('job_description')
    experience_details = data.get('experience_details')

    if not job_description or not experience_details:
        return jsonify({"error": "Job description and experience details are required"}), 400

    # Tailor experience (assuming this is done manually or by another method)
    tailored_data = {
        "job_description": job_description,
        "experience_details": experience_details
    }

    # Convert tailored data to JSON
    json_converter = JsonConverter(tailored_data)
    tailored_json = json_converter.convert()

    # Save tailored JSON to file
    tailored_file_path = "data/tailored_resume.json"
    with open(tailored_file_path, "w") as file:
        json.dump(tailored_json, file, indent=4)

    # Combine JSON data
    combiner = JsonCombiner(tailored_file_path, "data/untailored_resume.json", "data/resume.json")
    combiner.combine_data()

    # Generate PDF
    pdf_generator = PdfGenerator(
        template_path="templates/resume_template.tex",
        json_path="data/resume.json",
        output_tex="resume.tex",
        output_pdf="resume.pdf"
    )
    pdf_generator.generate_resume()

    # Move output files to the output directory
    os.rename("resume.pdf", "output/resume.pdf")
    os.rename("resume.tex", "output/resume.tex")

    # Delete auxiliary files
    for ext in ["aux", "log", "out"]:
        try:
            os.remove(f"resume.{ext}")
        except FileNotFoundError:
            pass

    return send_file("output/resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
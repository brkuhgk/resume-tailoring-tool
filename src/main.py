from openai import OpenAI
from tailor_experience import ResumeTailor
from convert_json import JsonConverter
from combine_jsondata import JsonCombiner
from generate_pdf import PdfGenerator
import os
import json

def main():
    # Initialize OpenAI client
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    api_key = OPENAI_API_KEY  # Replace with your actual OpenAI API key
    
    # Define the paths to the input files
    job_description_path = "input/job_description.txt"
    experience_details_path = "input/experience_details.txt"

    # Read the job description from the file
    with open(job_description_path, "r") as file:
        job_description = file.read()

    # Read the experience details from the file
    with open(experience_details_path, "r") as file:
        experience_details = file.read()
    
    # Fetch tailored resume data
    # Initialize OpenAI client
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
    resume_tailor = ResumeTailor(openai_client)
    resume_tailor.set_job_description(job_description)
    resume_tailor.set_experience_details(experience_details=experience_details)
    tailored_data = resume_tailor.fetch_tailored_data()
    print("Tailored data: .....")

    # Convert tailored data to JSON
    json_converter = JsonConverter(tailored_data)
    tailored_json = json_converter.convert()
    print("Tailored JSON: .....")
    # Save tailored JSON to file
    tailored_file_path = "data/tailored_resume.json"
    with open(tailored_file_path, "w") as file:
        json.dump(tailored_json, file, indent=4)

    # Combine JSON data
    combiner = JsonCombiner(tailored_file_path, "data/untailored_resume.json", "data/resume.json")
    combiner.combine_data()
    print("Combined JSON data: ....")


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

if __name__ == "__main__":
    main()
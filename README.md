# README.md

# Resume Tailoring Tool

This project is a Resume Tailoring Tool that utilizes the OpenAI API to tailor resumes according to specific job descriptions. The tool fetches tailored data, combines it with existing resume information, and generates a final PDF resume.

## Project Structure

```
resume-tailoring-tool
├── src
│   ├── tailor_experience.py        # Contains the ResumeTailor class for fetching tailored resume data from OpenAI API.
│   ├── convert_json.py              # Defines the JsonConverter class for converting tailored bullet points to JSON format.
│   ├── combine_jsondata.py          # Contains the JsonCombiner class for merging tailored and untailored resume data.
│   ├── generate_pdf.py              # Defines the PdfGenerator class for generating a PDF resume from JSON data and LaTeX template.
│   ├── templates
│   │   └── resume_template.tex      # LaTeX template for the resume structure and formatting.
│   ├── data
│   │   ├── untailored_resume.json   # Initial resume data without tailoring.
│   │   ├── tailored_resume.json      # Stores the tailored experience data fetched from OpenAI API.
│   │   └── resume.json              # Final combined resume data after merging tailored and untailored data.
│   └── utils
│       └── openai_client.py         # Utility class for handling OpenAI API interactions.
├── requirements.txt                  # Lists the dependencies required for the project.
└── README.md                         # Documentation for the project.
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd resume-tailoring-tool
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key in your environment variables:
   ```
   export OPENAI_API_KEY='your-api-key'
   ```

## Usage Guidelines

1. **Tailoring Experience**: Use the `tailor_experience.py` script to fetch tailored resume data by providing a job description and experience details.

2. **Convert to JSON**: The `convert_json.py` script will convert the tailored bullet points into a structured JSON format.

3. **Combine Data**: Use `combine_jsondata.py` to merge the tailored experience data with the untailored resume data.

4. **Generate PDF**: Finally, run `generate_pdf.py` to create a PDF resume from the combined JSON data and LaTeX template.

## Overview of Functionality

- **ResumeTailor**: Fetches tailored resume data from the OpenAI API based on job descriptions.
- **JsonConverter**: Extracts tailored bullet points and converts them into JSON format.
- **JsonCombiner**: Combines tailored and untailored resume data into a final resume.
- **PdfGenerator**: Generates a PDF resume using the combined data and a LaTeX template.

This tool aims to streamline the resume tailoring process, making it easier for users to create customized resumes that align with specific job opportunities.
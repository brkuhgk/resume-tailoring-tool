import json
from jinja2 import Environment, FileSystemLoader
import subprocess

class PdfGenerator:
    def __init__(self, template_path, json_path, output_tex, output_pdf):
        self.template_path = template_path
        self.json_path = json_path
        self.output_tex = output_tex
        self.output_pdf = output_pdf

    def generate_resume(self):
        # Load JSON data
        with open(self.json_path, "r") as file:
            data = json.load(file)

        # Preprocess JSON data for LaTeX compatibility
        data['education_items'] = "\n".join(
            f"\\item {edu['education_level']} in {edu['field_of_study']}, {edu['institution']} ({edu['year_of_completion']})"
            for edu in data['education_details']
        )
        data['experience_items'] = "\n".join(
            f"\\item \\textbf{{{exp['position']}}} at \\textit{{{exp['company']}}}, {exp['location']} ({exp['employment_period']})"
            + "\n\\begin{itemize}[noitemsep]\n" + "\n".join(f"\\item {point}" for point in exp['bullet_points']) + "\n\\end{itemize}"
            for exp in data['experience']
        )
        data['projects_items'] = "\n".join(
            f"\\item \\textbf{{{proj['name']}}}: {proj['description']} \\href{{{proj['link']}}}{{Link}}"
            for proj in data['projects']
        )
        data['skills_items'] = "\n".join(f"\\item {skill}" for skill in data['skills'])
        data['certifications_items'] = "\n".join(f"\\item {cert}" for cert in data['certifications'])
        data['publications_items'] = "\n".join(f"\\item {pub}" for pub in data['publications'])

        # Configure Jinja2 to use custom delimiters
        env = Environment(
            loader=FileSystemLoader('.'),
            block_start_string='<<%',
            block_end_string='%>>',
            variable_start_string='<<',
            variable_end_string='>>',
        )

        # Load and render the template
        template = env.get_template(self.template_path)
        rendered_tex = template.render(data["personal_information"], **data)

        # Save rendered LaTeX file
        with open(self.output_tex, "w") as file:
            file.write(rendered_tex)

        # Compile LaTeX to PDF
        subprocess.run(["pdflatex", self.output_tex])
import re

class JsonConverter:
    def __init__(self, response_text):
        self.response_text = response_text

    def extract_sections(self):
        import re
        sections = re.findall(r"#### Position: (.*?)\n(- .*?)(?=\n####|$)", self.response_text, re.DOTALL)
        return sections

    def convert_to_json(self, sections):
        experience_list = []
        for title, details in sections:
            title_parts = re.match(r"(.*?) at (.*?) \((.*?), (.*?)\)", title)
            if title_parts:
                position, company, period, location = title_parts.groups()
            else:
                position, company, period, location = title, "", "", ""
            
            bullet_points = [bp.strip().lstrip("- ").strip() for bp in details.strip().split("\n")]
            experience = {
                "position": position,
                "company": company,
                "employment_period": period,
                "location": location,
                "bullet_points": bullet_points
            }
            experience_list.append(experience)
        return experience_list

    def convert(self):
        sections = self.extract_sections()
        return self.convert_to_json(sections)
import json

class JsonCombiner:
    """Combines tailored experience data with other data fields from untailored_resume.json."""

    def __init__(self, tailored_file, untailored_file, output_file):
        self.tailored_file = tailored_file
        self.untailored_file = untailored_file
        self.output_file = output_file

    def load_json(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)

    def combine_data(self):
        tailored_experience = self.load_json(self.tailored_file)
        other_data = self.load_json(self.untailored_file)

        combined_data = {
            "personal_information": other_data["personal_information"],
            "education_details": other_data["education_details"],
            "projects": other_data["projects"],
            "skills": other_data["skills"],
            "certifications": other_data["certifications"],
            "publications": other_data["publications"],
            "experience": tailored_experience
        }

        with open(self.output_file, "w") as file:
            json.dump(combined_data, file, indent=4)

        print("Combined data saved to", self.output_file)

if __name__ == "__main__":
    combiner = JsonCombiner("data/tailored_resume.json", "data/untailored_resume.json", "data/resume.json")
    combiner.combine_data()
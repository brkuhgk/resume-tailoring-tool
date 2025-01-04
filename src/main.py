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
    

    # Define the job description and experience details
    job_description = """
    About the job
    Introduction

    Introduction

    At IBM, work is more than a job - it's a calling: To build. To design. To code. To consult. To think along with clients and sell. To make markets. To invent. To collaborate. Not just to do something better, but to attempt things you've never thought possible. Are you ready to lead in this new era of technology and solve some of the world's most challenging problems? If so, lets talk.

    Your Role and Responsibilities

    Position start dates are in 2025.

    When working in this abstract, fast pace and continuously changing tech world, resilience, commitment, and curiosity serve as the foundation for success as an IBM Developer.

    You will participate in many aspects of the software development lifecycle, such as design, code implementation, testing, and support. You will work to create software that is of high quality and meets our clients' needs. You will also have the opportunity to become a contributor within Open Source communities across multiple disciplines.

    In your role, you will be supported by mentors and coaches who will encourage you to challenge the norm, investigate ideas outside of your role, and come up with creative solutions resulting in ground-breaking impact for the wider business, our external clients, & their customers. Our culture of flexibility and freedom are pillars that embrace long-term career growth and learning opportunities in an environment that highlights your unique skills and experience.

    As An Entry Level Software Developer, You Will


    Work in an agile, collaborative environment to understand requirements, design, code and test innovative applications, and support those applications 
    Assist with resolving network issues, configuring operating systems and using remote desktop connections to provide immediate support.
    Troubleshoot issues, collect data, elicit detailed requirements, then design and implement innovative solutions across multiple industries and sectors as well as governments and agencies.


    Who You Are: 


    Highly motivated and have a passion for creating and supporting great products. 
    Thrive on collaboration, working side by side with people of all backgrounds and disciplines, and you have very strong verbal and written communication skills. 
    Great at solving problems, troubleshooting, and implementing solutions to complex technical issues.
    Have a basic understanding of software development and programming languages.
    Have the ability to learn new skills quickly and use the skills efficiently. 


    Required Technical and Professional Expertise


    Basic knowledge in one or more of the following technology areas: Java, Ruby, Python, Javascript, HTML, CSS, Node.js, Angular.js
    Understanding of Operating system software (e.g., MacOS, Linux, Windows)


    Preferred Technical And Professional Expertise


    Minimum 1 year experience working with operating system software (e.g., MacOS, Linux, Windows)
    Minimum 1 year experience development in JavaScript, Node.js, or similar
    One or more internships or co-op experience


    About Business Unit

    IBM Software infuses core business operations with intelligence—from machine learning to generative AI—to help make organizations more responsive, productive, and resilient. IBM Software helps clients put AI into action now to create real value with trust, speed, and confidence across digital labor, IT automation, application modernization, security, and sustainability. Critical to this is the ability to make use of all data, because AI is only as good as the data that fuels it. In most organizations data is spread across multiple clouds, on premises, in private datacenters, and at the edge. IBM’s AI and data platform scales and accelerates the impact of AI with trusted data, and provides leading capabilities to train, tune and deploy AI across business. IBM’s hybrid cloud platform is one of the most comprehensive and consistent approach to development, security, and operations across hybrid environments—a flexible foundation for leveraging data, wherever it resides, to extend AI deep into a business.

    Your Life @ IBM

    In a world where technology never stands still, we understand that, dedication to our clients success, innovation that matters, and trust and personal responsibility in all our relationships, lives in what we do as IBMers as we strive to be the catalyst that makes the world work better.

    Being an IBMer means you’ll be able to learn and develop yourself and your career, you’ll be encouraged to be courageous and experiment everyday, all whilst having continuous trust and support in an environment where everyone can thrive whatever their personal or professional background.

    Our IBMers are growth minded, always staying curious, open to feedback and learning new information and skills to constantly transform themselves and our company. They are trusted to provide on-going feedback to help other IBMers grow, as well as collaborate with colleagues keeping in mind a team focused approach to include different perspectives to drive exceptional outcomes for our customers. The courage our IBMers have to make critical decisions everyday is essential to IBM becoming the catalyst for progress, always embracing challenges with resources they have to hand, a can-do attitude and always striving for an outcome focused approach within everything that they do.

    Are you ready to be an IBMer?

    About IBM

    IBM's greatest invention is the IBMer. We believe that through the application of intelligence, reason and science, we can improve business, society and the human condition, bringing the power of an open hybrid cloud and AI strategy to life for our clients and partners around the world.

    Restlessly reinventing since 1911, we are not only one of the largest corporate organizations in the world, we’re also one of the biggest technology and consulting employers, with many of the Fortune 50 companies relying on the IBM Cloud to run their business.

    At IBM, we pride ourselves on being an early adopter of artificial intelligence, quantum computing and blockchain. Now it’s time for you to join us on our journey to being a responsible technology innovator and a force for good in the world.

    """

    experience_details = """
    - position: "X"
        company: "Y."
        employment_period: "06/2019 - Present"
        location: "San Francisco, CA"
        industry: "Technology"
        key_responsibilities:
        - responsibility: "Developed web applications using React and Node.js"
        - responsibility: "Collaborated with cross-functional teams to design and implement new features"
        - responsibility: "Troubleshot and resolved complex software issues"
        skills_acquired:
        - "React"
        - "Node.js"
        - "Software Troubleshooting"
    - position: "Software Developer"
        company: "Innovatech"
        employment_period: "06/2015 - 12/2017"
        location: "Milan, Italy"
        industry: "Technology"
        key_responsibilities:
        - responsibility: "Developed and maintained web applications using modern technologies"
        - responsibility: "Collaborated with UX/UI designers to enhance user experience"
        - responsibility: "Implemented automated testing procedures to ensure code quality"
        skills_acquired:
        - "Web development"
        - "User experience design"
        - "Automated testing"
    - position: "Junior Developer"
        company: "StartUp Hub"
        employment_period: "01/2014 - 05/2015"
        location: "Florence, Italy"
        industry: "Startups"
        key_responsibilities:
        - responsibility: "Assisted in the development of mobile applications and web platforms"
        - responsibility: "Participated in code reviews and contributed to software design discussions"
        - responsibility: "Resolved bugs and implemented feature enhancements"
        skills_acquired:
        - "Mobile app development"
        - "Code reviews"
        - "Bug fixing"
    ...
    """  
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
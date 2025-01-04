
class OpenAIClient:
    def __init__(self, api_key):
        
        openai.api_key = api_key

    def fetch_tailored_data(self, job_description, experience_details):
        response = openai.chat.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert in resume optimization and tailoring. Given a job description and professional "
                        "experience details, provide a list of tailored bullet points that match the experience to the job "
                        "description. Ensure the output is structured, uses measurable metrics, and aligns with job requirements."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"### Job Description:\n{job_description}\n\n"
                        f"### Professional Experience:\n{experience_details}\n\n"
                        "### Output Requirements:\n"
                        "- Provide 3-4 tailored bullet points for each job experience.\n"
                        "- Use metrics and action-oriented language.\n"
                        "- Format each point as `- {Tailored Achievement}`."
                    )
                }
            ],
            temperature=0.7,
            max_tokens=512,
            top_p=1
        )
        return response.choices[0].message.content.strip()
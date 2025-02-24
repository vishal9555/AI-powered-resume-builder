import google.generativeai as genai

genai.configure(api_key="AIzaSyBVdzfDouVTrIulEpJQ6Ic27msELcVd--A")

def generate_resume_content(user_data):
    prompt = f"""
    Generate a professional resume with these details:
    - Name: {user_data.get('name')}
    - Email: {user_data.get('email')}
    - Skills: {user_data.get('skills')}
    - Experience: {user_data.get('experience')}
    - Education: {user_data.get('education')}

    Format the resume with sections: Summary, Skills, Professional Experience, and Education.
    Please don't provide education content in bold letter. And describe education with 2-3 sentences.
    And do same for experience. Give summary based on the details. Remember topics like Name, Summary, Skills, Professional Experience, and Education should be in bold
    """
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)

    # 🛠 Fix: Ensure it's always a string
    resume_text = response.text if isinstance(response.text, str) else str(response.text)

    return resume_text


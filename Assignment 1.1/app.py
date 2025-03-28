from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import json
import os
import google.generativeai as genai

# Replace with your actual Gemini API key.  Consider using environment variables for security.
GOOGLE_API_KEY = "Your API key"
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model with the correct name
model = genai.GenerativeModel('models/gemini-2.0-flash')  # Updated model name

app = FastAPI()


def generate_cover_letter(resume_data, job_description_data):
    """Generates a cover letter using Gemini flash 2.0."""

    prompt = f"""
    You are an expert cover letter writer.  Craft a compelling cover letter based on the following resume and job description.  Focus on highlighting relevant skills and experience. Keep the cover letter concise and professional. Aim for approximately 3-4 paragraphs.

    Resume:
    {json.dumps(resume_data, indent=2)}

    Job Description:
    {json.dumps(job_description_data, indent=2)}

    Cover Letter:
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()  # Return the generated cover letter
    except Exception as e:
        print(f"Error generating cover letter: {e}") # Log the error for debugging
        raise HTTPException(status_code=500, detail=f"Error generating cover letter: {e}")



@app.post("/generate_cover_letter/")
async def create_cover_letter(resume_file: UploadFile = File(...), job_description_file: UploadFile = File(...)):
    """
    API endpoint to generate a cover letter from a resume and job description.
    """
    try:
        # Read resume data
        resume_content = await resume_file.read()
        resume_data = json.loads(resume_content.decode("utf-8"))

        # Read job description data
        job_description_content = await job_description_file.read()
        job_description_data = json.loads(job_description_content.decode("utf-8"))

        # Generate cover letter
        cover_letter = generate_cover_letter(resume_data, job_description_data)

        return JSONResponse({"cover_letter": cover_letter})

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format in resume or job description.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)  # Using localhost IP instead of 0.0.0.0
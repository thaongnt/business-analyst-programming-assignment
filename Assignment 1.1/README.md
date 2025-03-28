# Cover Letter Generator API

A FastAPI-based service that generates customized cover letters using Google's Gemini AI model. The service takes a resume and job description as input and produces a professional, tailored cover letter.

I solved this problem by first understand the problem can be solved by completing 3 tasks: come up with a good prompt for Gemini, read JSON files (resume and job description), set up API endpoint to listen to POST request and get the repsonse from the API. With Cursor AI help, I was able to finished the above tasks and below is the instruction how to run the program.

## Features

- FastAPI-based REST API
- Integration with Google's Gemini AI model
- JSON-based input format for resume and job description
- Professional cover letter generation
- Easy-to-use API endpoint

## Prerequisites

- Python 3.8 or higher
- Google API key for Gemini AI
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up your Google API key:
   - Get your API key from the Google AI Studio
   - Replace the `GOOGLE_API_KEY` in `app.py` with your key
   - Alternatively, set it as an environment variable

## Usage

1. Start the server:
```bash
python app.py
```
The server will run on `http://127.0.0.1:8081`

2. Prepare your input files:
   - `resume.json`: Your resume in JSON format
   - `job-description.json`: The job description in JSON format

3. Make a POST request to the API:
```bash
python test_api.py
```

## API Endpoint

- **URL**: `http://127.0.0.1:8081/generate_cover_letter/`
- **Method**: POST
- **Content-Type**: multipart/form-data

### Request Parameters
- `resume_file`: JSON file containing resume data
- `job_description_file`: JSON file containing job description data

### Example Response
```json
{
    "cover_letter": "Generated cover letter text..."
}
```

## Input File Formats

### resume.json
```json
{
  "name": "Your Name",
  "education": "Your Education",
  "skills": ["Skill1", "Skill2", "Skill3"],
  "experience": [
    {
      "company": "Company Name",
      "role": "Job Title",
      "duration": "Duration"
    }
  ]
}
```

### job-description.json
```json
{
  "jobTitle": "Position Title",
  "company": "Company Name",
  "responsibilities": "Job responsibilities and requirements"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 400: Invalid input format
- 500: Server error or AI model error

## Security Note

- Keep your Google API key secure
- Consider using environment variables for sensitive data
- Don't commit API keys to version control

## License

[Your chosen license]

## Contributing

[Your contribution guidelines] 
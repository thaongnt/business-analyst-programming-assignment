import requests

# API endpoint
url = "http://127.0.0.1:8081/generate_cover_letter/"

# Files to upload
files = {
    'resume_file': ('resume.json', open('resume.json', 'rb'), 'application/json'),
    'job_description_file': ('job-description.json', open('job-description.json', 'rb'), 'application/json')
}

try:
    # Make the POST request
    response = requests.post(url, files=files)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print("Error:", str(e)) 
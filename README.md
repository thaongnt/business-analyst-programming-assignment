# Lead Nitro Take-Home Assignment

## Introduction
Hello! 👋

Welcome to the Lead Nitro Take-Home Assignment for the Strategic Business Analyst Role. This assignment allows you to showcase your skills across a range of areas in data analysis and machine learning.

You can choose to implement one or more tasks based on your preferences, strengths, growth objectives. You do **NOT** have to complete all of them. You are expected to spend **AT MOST** 3 hours on the assignment.

The different tasks are divided into two categories: **Machine Learning / Data Analysis** and **Database / SQL**.


--- 
## Assignment Rules
You are free to use any online resources and assistive tools to complete the tasks.

## Submission Instructions
1. Fork the provided repository.
2. Develop your solution in the forked repository.
3. Update the `README.md` with instructions and notes on your development process.
4. You should describe the challenges you faced, justify the decisions you made, and outline reasons for not taking other paths you have considered.
5. You should also explain your results and your overall methodology.
6. Feel free to ask questions for anything unclear about the instructions. Most prompts are intentionally vague to give you creative agency on your approach & objective metrics.
7. Commit and push your changes to the forked repository.
8. Share the link to your forked repository.

## Evaluation Criteria
- **Functionality**: Successful implementation of the specified models.
- **Code Quality**: Clean, readable, and maintainable code.
- **Testing**: Comprehensive and reproducible tests.
- **Communication**: Clear explanation of results, limitations, and future work.
- **Database Schema**: Well-designed and optimized database layout.

### Disclaimer
None of your work will be used unless you are hired. 

---

## 1. Machine Learning / Data Analysis

### 1.1. LLM API Integration
**Goal**: Create a service integrating Gemini Flash 2.0 to generate a cover letter from a user's resume and a job description.
- **Expected Result**: A functioning API that takes `resume.json` and `job-description.json`, and outputs a customized cover letter.
- **Dummy Data**:
  - `resume.json`: 
    ```json
    {
      "name": "Alex Johnson",
      "education": "B.Sc. Computer Science",
      "skills": ["JavaScript", "React", "Node.js"],
      "experience": [
        {
          "company": "TechCorp",
          "role": "Software Engineer",
          "duration": "2 years"
        }
      ]
    }
    ```
  - `job-description.json`:
    ```json
    {
      "jobTitle": "Front-end Developer",
      "company": "Innovatech",
      "responsibilities": "Develop and maintain web applications using React and Node.js"
    }
    ```

### 1.2. Natural Language clustering
**Goal**: Develop a clustering / nearest neighbor classifier for natural language text.
- **Expected Result**: A model capable of classifying a piece of text into the correct label and another function to compare if two pieces of text belong to the same category.
- **Task Requirements**: Using [this kaggle dataset](https://www.kaggle.com/datasets/tanishqdublish/text-classification-documentation), train and test a model to classify the text.

### 1.3. Dataset Clustering
**Goal**: Develop a clustering algorithm for a structured dataset.
- **Expected Result**: A model capable of classifying customers / products by their purchase trends.
- **Task Requirements**: Using [this kaggle dataset](https://www.kaggle.com/datasets/yasserh/customer-segmentation-dataset), develop a clustering model and identify important customer or product trends.

## 2. Database / SQL

### 2.1. Database Knowledge
**Goal**: Design a database schema for managing user profiles, sellers, and product reviews.
- **Expected Result**: An efficient and well-organized database schema with example queries for user profile management, storing seller information, product information, and product reviews.
- **Example Schema**:
  - Example entities: Users, Sellers, Product Review
- **Example Queries**: 
  - Retrieve all products sold by a seller.
  - Find average rating of products based on user reviews.
  - Find the average rating of sellers based on the user reviews.


### Final Note
We're excited to see your innovative approaches and solutions. Good luck with your assignment! 🚀

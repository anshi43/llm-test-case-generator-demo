# LLM Test Case Generator Demo

A job-focused demo project that generates structured software test cases from user stories or requirements.

This repository demonstrates a lightweight **LLM-inspired testing workflow** built with **Python** and **Streamlit**.  
The current public MVP uses rule-based logic to simulate how an LLM-assisted testing tool could transform requirements into structured test scenarios.

## Project Purpose

This project was created as a portfolio repository for QA Automation / Software Test Engineer roles, especially roles related to:
- AI-assisted software testing
- test case generation
- requirements-to-test transformation
- LLM-supported QA workflows

It is designed as a safe public demo inspired by research work in LLMs for software testing.

## Key Features

- Generate structured test cases from a user story or requirement
- Categorize scenarios into:
  - Positive
  - Negative
  - Edge Case
  - Context-specific cases such as Security, Validation, or Business Rule
- Display generated test cases in a readable Streamlit UI
- Expand detailed steps and expected results
- Export generated test cases as Markdown

## Tech Stack

- Python
- Streamlit
- Pandas

## How It Works

The current MVP uses rule-based logic to:
1. read a user story or requirement
2. generate general test scenarios
3. detect keywords such as login, registration, or checkout
4. append additional context-specific test cases

This structure is intended to represent the first public version of a future LLM-powered testing assistant.

## Example Inputs

- As a user, I want to log in with my email and password so that I can access my dashboard.
- As a customer, I want to complete checkout with a credit card so that I can place an order.
- As a new user, I want to register an account so that I can use the application.

## Project Structure

```text
llm-test-case-generator-demo/
├── data/
├── generator/
│   └── test_case_generator.py
├── app.py
├── requirements.txt
└── README.md
```

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/anshi43/llm-test-case-generator-demo.git
cd llm-test-case-generator-demo
```

### 2. Create and activate a virtual environment

#### Windows PowerShell
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

## Why This Project Matters

This repository is intended to demonstrate:
- practical thinking around AI-assisted testing
- structured test case generation from requirements
- how LLM concepts can be applied to software QA workflows
- a bridge between traditional test design and modern AI-based tooling

It complements UI and API automation portfolio projects by showing a more advanced testing direction.

## Current Limitations

This public version does **not** yet use a live LLM API.
Instead, it uses rule-based logic as an MVP to demonstrate the workflow safely and clearly.

Possible future improvements:
- real LLM integration
- prompt templates
- better test case classification
- CSV / JSON export
- requirement parsing improvements
- test priority and severity tagging

## Author

**Ankit Mavani**  
Berlin, Germany

- GitHub: https://github.com/anshi43
- LinkedIn: add-your-link-here
- Email: mavaniankit09@gmail.com
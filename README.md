# LLM Test Case Generator Demo

This repository demonstrates a lightweight **LLM-inspired testing workflow** built with **Python** and **Streamlit**.  
The current public MVP uses rule-based logic to simulate how an AI-assisted testing tool could transform requirements into structured test scenarios.

## Live Demo

Streamlit App: https://llm-test-case-generator-demo-mpjypw43af6gzh3nygvkvj.streamlit.app/

## What This Project Does

This project generates structured software test cases from natural-language user stories or requirements.

It takes a requirement as input, analyzes it using rule-based logic, and produces categorized test scenarios such as positive, negative, edge-case, and context-specific cases. The application is designed to demonstrate how AI-assisted testing workflows can help transform requirements into more systematic and reusable test design outputs.

## Current Version

The current version uses rule-based logic to demonstrate how software requirements can be transformed into structured test cases in an LLM-inspired workflow.

A future version could integrate a real LLM for prompt-based test generation, classification, and refinement.

## Key Features

- Generate structured test cases from a user story or requirement
- Categorize scenarios into:
  - Positive
  - Negative
  - Edge Case
  - Context-specific cases such as Security, Validation, or Business Rule
- Display generated test cases in a readable Streamlit UI
- Expand detailed steps and expected results
- Download generated test cases as Markdown

## Live Demo Features

- Enter a user story or requirement
- Generate positive, negative, and edge-case test scenarios
- Add context-specific cases such as login, registration, or checkout
- Review detailed steps and expected results
- Download generated test cases as Markdown

## Tech Stack

- Python
- Streamlit
- Pandas

## How It Works

The current MVP uses rule-based logic to:
1. Read a user story or requirement
2. Generate general test scenarios
3. Detect keywords such as login, registration, or checkout
4. Append additional context-specific test cases

This structure represents the first public version of a future LLM-powered testing assistant.

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
git clone [https://github.com/anshi43/llm-test-case-generator-demo.git](https://github.com/anshi43/llm-test-case-generator-demo.git)
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

This repository demonstrates:
- structured test case generation from requirements
- a practical workflow for AI-assisted testing
- how LLM-inspired concepts can be applied to software QA workflows
- a bridge between traditional test design and AI-supported tooling

## Current Limitations

This version does **not** yet use a live LLM API.  
Instead, it uses rule-based logic as an MVP to demonstrate the workflow clearly.

## Future Improvements

Possible next improvements for this repository:
- real LLM integration
- prompt templates
- better test case classification
- CSV / JSON export
- requirement parsing improvements
- test priority and severity tagging

## Author

**Ankit Mavani**  
Berlin, Germany

- GitHub: [https://github.com/anshi43](https://github.com/anshi43)
- LinkedIn: [https://www.linkedin.com/in/ankitmavani/](https://www.linkedin.com/in/ankitmavani/)
- Email: [mavaniankit09@gmail.com](mailto:mavaniankit09@gmail.com)

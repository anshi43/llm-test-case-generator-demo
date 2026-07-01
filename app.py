import streamlit as st
import pandas as pd
from generator.test_case_generator import generate_test_cases

st.set_page_config(
    page_title="LLM Test Case Generator Demo",
    page_icon="🧪",
    layout="wide"
)


def convert_test_cases_to_markdown(test_cases):
    markdown_output = "# Generated Test Cases\n\n"

    for index, test_case in enumerate(test_cases, start=1):
        markdown_output += f"## {index}. {test_case['title']}\n"
        markdown_output += f"- **Type:** {test_case['type']}\n"
        markdown_output += "- **Steps:**\n"
        for step_number, step in enumerate(test_case["steps"], start=1):
            markdown_output += f"  {step_number}. {step}\n"
        markdown_output += f"- **Expected Result:** {test_case['expected_result']}\n\n"

    return markdown_output


st.title("LLM Test Case Generator Demo")
st.write(
    "Generate structured software test cases from a user story or requirement. "
    "This public MVP uses rule-based logic to demonstrate an LLM-driven software testing concept."
)

with st.sidebar:
    st.header("Example Inputs")
    st.markdown("- As a user, I want to log in with my email and password so that I can access my dashboard.")
    st.markdown("- As a customer, I want to complete checkout with a credit card so that I can place an order.")
    st.markdown("- As a new user, I want to register an account so that I can use the application.")

user_story = st.text_area(
    "Enter a user story or requirement",
    placeholder="Example: As a user, I want to log in with my email and password so that I can access my dashboard.",
    height=180
)

if st.button("Generate Test Cases"):
    test_cases = generate_test_cases(user_story)

    if not test_cases:
        st.warning("Please enter a user story or requirement.")
    else:
        st.success(f"Generated {len(test_cases)} test cases.")

        summary_df = pd.DataFrame(
            [
                {
                    "Type": test_case["type"],
                    "Title": test_case["title"],
                    "Expected Result": test_case["expected_result"]
                }
                for test_case in test_cases
            ]
        )

        st.subheader("Summary")
        st.dataframe(summary_df, use_container_width=True)

        markdown_output = convert_test_cases_to_markdown(test_cases)
        st.download_button(
            label="Download as Markdown",
            data=markdown_output,
            file_name="generated_test_cases.md",
            mime="text/markdown"
        )

        st.subheader("Detailed Test Cases")
        for index, test_case in enumerate(test_cases, start=1):
            with st.expander(f"{index}. {test_case['title']}", expanded=True):
                st.write(f"**Type:** {test_case['type']}")
                st.write("**Steps:**")
                for step_number, step in enumerate(test_case["steps"], start=1):
                    st.write(f"{step_number}. {step}")
                st.write(f"**Expected Result:** {test_case['expected_result']}")
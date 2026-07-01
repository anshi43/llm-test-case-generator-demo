def generate_test_cases(user_story: str):
    cleaned_story = user_story.strip()

    if not cleaned_story:
        return []

    lowered = cleaned_story.lower()

    test_cases = [
        {
            "type": "Positive",
            "title": "Verify expected behavior for valid input",
            "steps": [
                "Open the application or feature",
                f"Use the feature based on the requirement: {cleaned_story}",
                "Enter valid input data",
                "Submit the action"
            ],
            "expected_result": "The system should complete the action successfully and show the expected outcome."
        },
        {
            "type": "Negative",
            "title": "Verify system response for invalid input",
            "steps": [
                "Open the application or feature",
                f"Use the feature based on the requirement: {cleaned_story}",
                "Enter invalid, incomplete, or incorrect input",
                "Submit the action"
            ],
            "expected_result": "The system should reject the input and display a clear validation or error message."
        },
        {
            "type": "Edge Case",
            "title": "Verify behavior for boundary or unusual input",
            "steps": [
                "Open the application or feature",
                f"Use the feature based on the requirement: {cleaned_story}",
                "Enter boundary, empty, or unusual input values",
                "Submit the action"
            ],
            "expected_result": "The system should handle the edge case gracefully without crashing or producing inconsistent results."
        }
    ]

    login_keywords = ["login", "log in", "sign in", "signin"]
    register_keywords = ["register", "sign up", "signup", "create account"]
    payment_keywords = ["payment", "checkout", "pay", "transaction"]

    if any(keyword in lowered for keyword in login_keywords):
        test_cases.append(
            {
                "type": "Security",
                "title": "Verify login with incorrect credentials",
                "steps": [
                    "Open the login page",
                    "Enter an invalid username or password",
                    "Click the login button"
                ],
                "expected_result": "The login should fail and the user should see an appropriate error message."
            }
        )

    if any(keyword in lowered for keyword in register_keywords):
        test_cases.append(
            {
                "type": "Validation",
                "title": "Verify registration with duplicate or invalid data",
                "steps": [
                    "Open the registration page",
                    "Enter duplicate or invalid user details",
                    "Submit the form"
                ],
                "expected_result": "The system should prevent registration and show a meaningful validation message."
            }
        )

    if any(keyword in lowered for keyword in payment_keywords):
        test_cases.append(
            {
                "type": "Business Rule",
                "title": "Verify payment or checkout with incomplete details",
                "steps": [
                    "Open the checkout or payment page",
                    "Enter incomplete payment or billing information",
                    "Submit the transaction"
                ],
                "expected_result": "The transaction should not be completed and the user should see clear validation feedback."
            }
        )

    return test_cases
# Personal Finance Tracker

#### Video Demo: [Project Demo](https://youtu.be/GkdJq0P-ITY)

#### Description:

The Personal Finance Tracker is a command-line tool designed to help users manage and track their expenses effectively. The tool allows users to initialize their monthly budget, log their daily expenses, and view a summary of their spending across different categories. This README.md file provides an overview of the project, its functionality, and details about each key component.

### Project Structure:

The project consists of several Python files, each serving a specific purpose:

1. **project.py:** This file contains the main functionality of the Personal Finance Tracker. It includes functions for initializing user profiles, logging expenses, and summarizing spending by category. The code is modular, making it easy to maintain and extend.

2. **test_project.py:** This file comprises a comprehensive set of unit tests for the functions in `project.py`. These tests cover various scenarios, ensuring the reliability and correctness of the code. The tests use the `unittest.mock` module to simulate user input and capture standard output for validation.

### Functionality:

#### Initializing Profiles:

The `initialize_profile` function in `project.py` allows users to set up their monthly budget. It prompts users for their monthly income and additional spending categories, then saves this information in a CSV file (`test_profile.csv` for testing purposes).

#### Logging Expenses:

The `save_expenses` function enables users to log their daily expenses. Users input the description, amount, and category for each expense and timestamp is automatically generated for those expenses. The data is stored in a CSV file `expenses.csv` (`test_expenses.csv` for testing purposes), allowing users to track their spending over time.

#### Summarizing Spending:

The `print_categories` function displays a summary of spending by category. Users can view a list of categories along with their allocated budgets and actual spending amounts. This summary helps users identify areas where they may be overspending.

#### Testing:

The `test_project.py` file contains unit tests for each key function. These tests ensure that the functions handle different scenarios correctly, including valid inputs, edge cases, and potential errors.

### Design Choices:

#### Modularity:

The code is designed with modularity in mind, making it easy to understand, maintain, and extend. Each function has a specific responsibility, contributing to the overall functionality of the tool.

#### User-Friendly Interface:

The use of the `tabulate` library enhances the readability of the output, presenting information in a structured and easy-to-understand format. User input is simulated in tests, providing a seamless testing experience.

### Future Improvements:

While the current version of the Personal Finance Tracker provides essential functionality, there is room for improvement. Future enhancements would include the following:

1. Complete testing amongst all the functions. Current design choice was made to test the most essential functions to functionality of programming and human-operates tests per performed for the remainder of function to ensure minimal user input error remains.

2. Make a program provide more detailed reports  in the future state. The current version includes only basics for understanding personal spending habits, but would be beneficial to analyze spending patterns and provide customized suggestions from those.

3. Improvement in making the program feeling less clunky. As it is right now, this is a terminal driven program. Future implementation should include making the program be standalone and potentially intergrating it to be more portable, such as making it a mobile app or accessible through a website.

In summary, the Personal Finance Tracker is a tool for managing expenses and gaining insights into spending habits. This project aims to provide a useful and educational experience for each individual by making them being aware of their spending habit and making themselves be aware on areas of improvement. Feel free to explore the code, run the tests, and adapt the tool to suit your specific needs. Even though this program was created for the purposes of completing the Final Project ofr CS50P, I would like to continue working on making this program (or another one) in the future which makes it easier for each individual to under personal finances. I welcome your feedback and any contributions you would like to make for this program!

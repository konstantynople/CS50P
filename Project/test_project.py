# test_project.py

# Standard Library Imports
import os
import csv
from unittest.mock import patch

# Third-Party Library Imports
from tabulate import tabulate

# Function Being Tested
from project import check_file_existence, initialize_profile, print_categories
from project import clean_and_separate_categories, save_expenses

# Global constants for test files
TEST_PROFILE_FILE = 'test_profile.csv'
TEST_EXPENSES_FILE = 'test_expenses.csv'


def test_check_file_existence():
    """
    Test for check_file_existence function.
    """

    # Create a temporary file for testing
    test_file_name = "test_file.txt"
    with open(test_file_name, "w"):
        pass

    # Test when the file exists
    assert check_file_existence(test_file_name) is True

    # Test when the file does not exist
    non_existent_file = "non_existent_file.txt"
    assert check_file_existence(non_existent_file) is False

    # Remove the temporary file
    os.remove(test_file_name)


def test_initialize_profile():
    """
    Test for initialize_profile function.
    """

    # Mock user input to simulate entering data
    user_input = ["10000.00",  # Monthly income
                  "Travel, Work",  # Additional categories
                  "2560.00", "1280.00", "640.00", "320.00", "160.00",
                  "80.00", "40.00", "20.00", "10.00"]  # Budget for categories

    with patch('builtins.input', side_effect=user_input):
        # Run the function
        initialize_profile(TEST_PROFILE_FILE)

    # Check if the 'test_profile.csv' file is created
    assert os.path.isfile(TEST_PROFILE_FILE)

    # Check the content of the 'test_profile.csv' file
    with open(TEST_PROFILE_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Extract header and data from actual rows
    actual_header = rows[0]

    # Extract category names from the actual header
    actual_categories = actual_header[1:]

    # Check if all expected categories are present in the actual header
    expected_categories = ["Housing", "Transportation", "Groceries",
                           "Utilities", "Entertainment", "Dining Out",
                           "Travel", "Work", "Miscellaneous"]
    assert set(expected_categories) == set(actual_categories)

    # Clean up: remove the 'profile.csv' file
    os.remove(TEST_PROFILE_FILE)


def test_print_categories(capsys):
    # Test without values
    categories = ["Housing", "Transportation", "Groceries"]
    expected_output = tabulate([[1, "Housing"], [2, "Transportation"],
                                [3, "Groceries"]], headers=["#", "Category"],
                               tablefmt="grid")

    print_categories(categories)

    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()

    # Test with values
    categories = ["Housing", "Transportation", "Groceries"]
    values = [1000.0, 500.0, 300.0]
    expected_output = tabulate([[1, "Housing", "$1000.00"],
                                [2, "Transportation", "$500.00"],
                                [3, "Groceries", "$300.00"]],
                               headers=["#", "Category", "Value"],
                               tablefmt="grid")

    print_categories(categories, values)

    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()

    # Test with values that are string
    categories = ["Housing", "Transportation", "Groceries"]
    values = ["1000.0", "500.0", "300.0"]
    expected_output = tabulate([[1, "Housing", "$1000.00"],
                                [2, "Transportation", "$500.00"],
                                [3, "Groceries", "$300.00"]],
                               headers=["#", "Category", "Value"],
                               tablefmt="grid")

    print_categories(categories, values)

    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()


def test_clean_and_separate_categories():
    # Test case with additional categories
    additional_categories = ["TravelAndLeisure", "HomeImprovement",
                             "OutdoorActivities"]

    # Expected result after cleaning and separating categories
    expected_result = ["Travel And Leisure", "Home Improvement",
                       "Outdoor Activities"]

    # Call the function and check the result
    result = clean_and_separate_categories(additional_categories)
    assert result == expected_result

    # Test case with empty additional categories
    empty_categories = []

    # Expected result should be an empty list
    expected_empty_result = []

    # Call the function and check the result for empty categories
    empty_result = clean_and_separate_categories(empty_categories)
    assert empty_result == expected_empty_result

    # Test case with non-alphabetic characters in additional categories
    categories_with_symbols = ["!123Numbers", "Special@Characters",
                               "Underscore_Category"]

    # Expected result after cleaning and separating categories
    expected_symbol_result = ["Numbers", "Special Characters",
                              "Underscore Category"]

    # Call the function and check the result for categories with symbols
    symbol_result = clean_and_separate_categories(categories_with_symbols)
    assert symbol_result == expected_symbol_result


def test_save_expenses():
    # Ensure the test expenses file doesn't exist initially
    if os.path.exists(TEST_EXPENSES_FILE):
        os.remove(TEST_EXPENSES_FILE)

    # Test when creating a new file and logging expenses for the first time
    expenses_data = [['Timestamp', 'Description', 'Amount', 'Category'],
                     ['2022-01-01 12:00:00', 'Groceries', '50.00', 'Food'],
                     ['2022-01-02 14:30:00', 'Gas', '30.00', 'Transportation']]

    save_expenses(expenses_data, TEST_EXPENSES_FILE)

    # Verify the content of the test expenses file
    with open(TEST_EXPENSES_FILE, mode="r") as file:
        reader = csv.reader(file)
        saved_expenses = [row for row in reader]

    assert saved_expenses == expenses_data

    # Test when logging additional expenses to an existing file
    additional_expenses_data = [['Timestamp', 'Description', 'Amount',
                                 'Category'],
                                ['2022-01-03 16:45:00', 'Dinner', '40.00',
                                 'Food'],
                                ['2022-01-04 10:00:00', 'Coffee', '5.00',
                                 'Food']]

    new_expenses_data = expenses_data + additional_expenses_data

    save_expenses(new_expenses_data, TEST_EXPENSES_FILE)

    # Verify the content of the test expenses file after adding more expenses
    with open(TEST_EXPENSES_FILE, mode="r") as file:
        reader = csv.reader(file)
        updated_expenses = [row for row in reader]

    assert updated_expenses == expenses_data + additional_expenses_data[1:]

    # Clean up: remove the test expenses file
    os.remove(TEST_EXPENSES_FILE)

# project.py

# Personal Finance Tracker
# Kostyantyn Luferov (Stan)
# Github: konstantynople
# edx: kluferov4521
# San Jose, CA, USA
# January 27th, 2024

# Standard Library Imports
import csv
import os
import re
import sys
from datetime import datetime
from io import BytesIO

# Third-Party Library Imports
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from tabulate import tabulate

# Constants - Should not be modified!
PROFILE_FILE = "profile.csv"
EXPENSES_FILE = "expenses.csv"
EXPENSES_TABLE_PDF = "expenses_table.pdf"
INSIGHT_REPORT_PDF = "insight_report.pdf"
FULL_REPORT_PDF = "full_report.pdf"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
CATEGORIES_ROW_INDEX = 1
CATEGORY_COL_INDEX = 3


def main():
    """
    Main function that initiates the start of the program.

    The program follows this sequence of events:
    1. Checks if the user has a profile. If not, initiates profile creation.
    2. Checks if the user has any expenses. If not, prompts to log expenses.
    3. Offers options: 'Update Profile', 'Update Expenses', 'Generate Report',
       'Exit Program'.

        3a. If 'Update Profile' is chosen, allows updating existing profile
            details.
        3b. If 'Update Expenses' is chosen, allows modifying or deleting
            expenses.
        3c. If 'Reports' is chosen, provides options for different reports.
        3d. If 'Exit Program' is chosen, ends the program.
    """

    # Check if the user has a profile. If not, initiate profile creation.
    if not check_file_existence(PROFILE_FILE):
        print("Welcome to the Personal Spending Tracker!")
        initialize_profile(PROFILE_FILE)
    else:
        print("Welcome back to the Personal Spending Tracker!")

    # Check if the user has any expenses. If not, prompt to log expenses.
    if not check_file_existence(EXPENSES_FILE):
        while True:
            try:
                question = input("\nWould you like to log your expenses " +
                                 "now? (Yes/No) ").capitalize()

                if question == "Yes":
                    while True:
                        log_expenses(PROFILE_FILE, EXPENSES_FILE)
                        break
                elif question == "No":
                    sys.exit("Exiting Personal Spending Tracker. Goodbye!")
                else:
                    raise ValueError

                break
            except ValueError:
                print("Please only provide 'Yes' or 'No' as a response.")

    while True:
        # Display options for the user to choose from.
        print("\nOptions:\n" +
              "1. Update Profile\n" +
              "2. Log / Update Expenses\n" +
              "3. Reports\n" +
              "4. Exit Program")

        # Get the user's choice.
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            update_profile()
        elif choice == "2":
            update_expenses()
        elif choice == "3":
            reports()
        elif choice == "4":
            print("\nExiting Personal Spending Tracker. Goodbye!")
            return
        else:
            print("\nInvalid choice. Please enter a valid number (1-4).")


def check_file_existence(file_name):
    """
    Function to determine if a file exists.

    Parameters:
    - file_name (str): The name of the file to check for existence.

    Returns:
    - bool: True if the file exists, False otherwise.
    """

    return os.path.isfile(file_name)


def initialize_profile(PROFILE_FILE):
    """
    Function to set up a user profile in 'profile.csv'.

    The function prompts the user to provide monthly income and additional
    categories. It then generates a profile by creating 'profile.csv' for
    future reference.
    """

    while True:
        try:
            # Get the user's monthly income as a float.
            monthly_income = float(input("Enter your monthly income: $"))

            # Predefined categories and print them for user reference.
            categories = ["Housing", "Transportation", "Groceries",
                          "Utilities", "Entertainment", "Dining Out"]

            print_categories(categories)

            # Get additional categories from the user, or set to 'None'.
            additional_categories = input("\nEnter additional categories " +
                                          "(separated by commas), " +
                                          "or type 'None': ").split(", ")

            # If additional categories are not 'None', extend the list.
            if additional_categories[0] != "None":
                # Exclude redundant categories
                redundant_categories = list(set(additional_categories
                                                ).intersection(categories))

                if redundant_categories:
                    print("\nThe following categories are redundant: " +
                          f"{", ".join(redundant_categories)}. Additional " +
                          "categories can be added later on.\n")

                categories.extend(clean_and_separate_categories(
                    additional_categories))

            # Ensure uniqueness of categories
            categories = list(set(categories))

            # Add a default 'Miscellaneous' category
            categories.append('Miscellaneous')

            # Print the list of all categories
            print("The categories are:\n")
            print_categories(categories)

            # Getting value for each category
            budget_data = []

            for category in categories:
                while True:
                    try:
                        budget = float(input("\nEnter the budget for " +
                                             f"{category}: $"))
                        budget_data.append(budget)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            # Write the profile to 'profile.csv'.
            header = ["Monthly Income"] + categories
            data = [[monthly_income] + budget_data]

            with open(PROFILE_FILE, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(data)

            print("\n")
            print_categories(categories, budget_data)

            return
        except ValueError:
            # Handle invalid input for monthly income.
            print("Invalid input. Please enter a valid amount. " +
                  "(e.g., 10000.00)")


def print_categories(categories, values=None):
    """
    Function to print available categories and their values in a table.

    Parameters:
    - categories (list): List of categories to be printed.
    - values (list): Optional list of corresponding values for each category.
    """

    if values is None:
        # Print only the table of categories
        table = [[i + 1, category] for i, category in enumerate(categories)]
        headers = ["#", "Category"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    else:
        # Checking whether or not each value provided is string or not
        if isinstance(values[0], str):

            # Converts to be float type
            for i, value in enumerate(values):
                values[i] = float(value)

        # Print the table of categories and their values
        table = [[i + 1, category, f"${value:.2f}"] for i, (
            category, value) in enumerate(zip(categories, values))]
        headers = ["#", "Category", "Value"]
        print(tabulate(table, headers=headers, tablefmt="grid"))


def clean_and_separate_categories(additional_categories):
    """
    Function to clean and separate additional categories.

    Parameters:
    - additional_categories (list): List of additional categories provided by
      the user.

    Returns:
    - list: List of cleaned and separated categories.
    """

    # Clean the categories by removing non-alphabetic characters.
    cleaned_categories = [re.sub(r'[^A-Za-z]+', '', category)
                          for category in additional_categories]

    # Separate the categories by converting camelCase to separate words.
    separated_categories = [re.sub(r'([a-z])([A-Z])', r'\1 \2',
                                   cleaned_category).strip()
                            for cleaned_category in cleaned_categories]
    return separated_categories


def save_expenses(expenses, EXPENSES_FILE):
    """
    Function to save the updated expenses to 'expenses.csv'.

    Parameters:
    - expenses (list): List of expenses to be saved.
    """

    file_exists = os.path.isfile(EXPENSES_FILE)

    with open(EXPENSES_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(EXPENSES_FILE) == 0:
            # Write the header if the file is empty or doesn't exist
            writer.writerow(["Timestamp", "Description", "Amount", "Category"])

        # Remove the header from the expenses
        expenses_without_header = [entry for entry in expenses
                                   if entry != ["Timestamp", "Description",
                                                "Amount", "Category"]]

        # Write the expenses to the file
        writer.writerows(expenses_without_header)


def log_expenses(PROFILE_FILE, EXPENSES_FILE):
    """
    Function to log expenses. Checks if there is a profile (Which there should
    be by this point) and then checks if there was previously 'expenses.csv'
    created Which depends where they are within the program). User can log as
    many expesnes as they want until they use the trigger word 'N/A', which
    will then compile all the entries and transfer them over to 'expenses.csv'
    (Which could already exist or be created when opened).
    """

    # Load the existing profile to get categories
    with open(PROFILE_FILE, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        categories = header[1:]

    # Load existing expenses or create a new list
    expenses = load_expenses()

    while True:
        # Prompt the user to enter a description or use 'N/A' to finish.
        description = input("\nEnter a description of spending " +
                            "(or 'N/A' to finish): ").upper()

        if description == 'N/A':
            if not expenses:  # Check if there are no expenses
                sys.exit("No expenses entered. Exiting Personal Spending " +
                         "Tracker. Goodbye!")
            else:
                break

        # Get a valid amount from the user.
        amount = get_valid_amount("\nEnter the amount spent: $")

        # Allow the user to choose a category from the list
        category = get_valid_category(categories)

        # Time-stamp the entry
        timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)

        # Add the entry to the expenses list
        expenses.append([timestamp, description, amount, category])

        # Save expenses
        save_expenses(expenses, EXPENSES_FILE)

    return


def load_expenses():
    """
    Function to load existing expenses or create a new list.

    Returns:
    - list or None: List of existing expenses if 'expenses.csv' exists, else
      None.
    """

    if check_file_existence(EXPENSES_FILE):
        # If 'expenses.csv' exists, load and return the expenses.
        with open(EXPENSES_FILE, mode="r") as file:
            reader = csv.reader(file)
            return list(reader)
    else:
        # If 'expenses.csv' does not exist, return None.
        return []

    # TO LOOK INTO: It seems to be adding extra Rows at the very top


def get_valid_amount(prompt):
    """
    Function to get a valid amount from user input.

    Parameters:
    - prompt (str): The prompt to display when asking for user input.

    Returns:
    - float: A valid amount entered by the user.
    """
    while True:
        try:
            # Attempt to convert user input to a float.
            amount = float(input(prompt))
            return amount
        except ValueError:
            # Handle invalid input for amount.
            print("Invalid amount. Please enter a valid amount " +
                  "(e.g., 10000.00)")


def get_valid_category(categories):
    """
    Function to get a valid category from user input.

    Parameters:
    - categories (list): List of available categories.

    Returns:
    - str: A valid category entered by the user.
    """
    while True:
        print("\nAvailable Categories:", categories)
        # Prompt the user to enter a category.
        category = input("\nEnter the category: ")

        if category in categories:
            # If the entered category is valid, return it.
            return category
        else:
            # Handle invalid input for category.
            print("Invalid category. Please choose from " +
                  "the available categories.")


def update_profile():
    """
    Function to update user profile.

    The function accesses 'profile.csv' to pull the current profile data
    (Monthly Income, Categories) and allows the user to update each one
    separately.
    """

    # Load the existing profile
    with open(PROFILE_FILE, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)

    # Display monthly income in the profile
    income_table_data = [["Monthly Income"], ['$' + data[0][0]]]

    # Display the table for monthly income using tabulate
    print("\n" + tabulate(income_table_data, headers="firstrow",
                          tablefmt="grid"))

    # Update monthly income
    while True:
        try:
            new_income = input("\nDo you want to update your monthly " +
                               "income? (Yes/No): ")

            if new_income.capitalize() == 'Yes':
                data[0][0] = get_valid_amount("\nEnter new monthly income: $")
                break
            elif new_income.capitalize() == "No":
                break
            else:
                raise TypeError
        except TypeError:
            print("Please provide only 'Yes' or 'No' as a response.")

    # Update or add categories
    while True:
        # Display categories and values in the profile using print_categories
        print_categories(header[1:], data[0][1:])

        print("\nOptions:\n" +
              "1. Add Category\n" +
              "2. Update Category\n" +
              "3. Delete Category\n" +
              "4. Finish Updating")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            new_category = input("\nEnter the new category: ")

            # Check if the new category already exists
            if new_category.capitalize() in header:
                print(f"Category '{new_category}' already exists.")
                continue

            header.append(new_category)
            new_value = str(float(input(
                f"\nEnter the value for {new_category}: $")))

            # Find the label 'Miscellaneous' and its value
            miscellaneous_index = header.index('Miscellaneous')
            miscellaneous_value = data[0][miscellaneous_index]

            # Delete the 'Miscellaneous' column with the value
            del header[miscellaneous_index]
            for row in data:
                del row[miscellaneous_index]

            # Adds the value for the new category
            for row in data:
                row.append(new_value)

            # Append the category 'Miscellaneous' and its associated value to
            # the end
            header.append('Miscellaneous')
            for row in data:
                row.append(miscellaneous_value)
        elif choice == "2":
            while True:
                update_category = input("\nEnter the category to update: ")

                if update_category in header:
                    new_value = get_valid_amount(
                        f"\nEnter the new value for {update_category}: $")
                    index = header.index(update_category)
                    data[0][index] = new_value
                    break
                else:
                    print(
                        f"'{update_category}' is not part of the categories.")
        elif choice == "3":
            delete_category = input("\nEnter the category to delete: ")

            if (delete_category in header and
                    delete_category != "Miscellaneous"):
                index = header.index(delete_category)
                del header[index]
                for row in data:
                    del row[index]
            else:
                print("Category 'Miscellaneous' cannot be deleted.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    # Save the updated profile
    with open(PROFILE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    return


def update_expenses():
    """
    Function to update expenses.

    Allows the user to update expenses based on multiple parameters
    (Description, Amount, Category) or delete the entry if no longer needed.
    Once the user inputs the trigger to break the while loop,
    the program will override 'expenses.csv' with new data.
    """

    while True:
        try:
            # Determine if user wants to log expenses
            choice = input(
                "Would you like to log expenses? (Yes/No) ").capitalize()

            if choice == "Yes":
                log_expenses(PROFILE_FILE, EXPENSES_FILE)
                break
            elif choice == "No":
                break
            else:
                raise TypeError
        except TypeError:
            print("Please provide only 'Yes' or 'No' as a response.")

    while True:
        # Load existing expenses
        expenses = load_expenses()

        # Display existing expenses
        display_expenses(expenses[1:])

        # Choose entry to update or delete
        choice = input("\nEnter the index of the entry to update/delete " +
                       "(or '0' to finish): ")

        if choice == '0':
            break

        try:
            index = int(choice)

            # Check if index is valid
            if 0 < index <= len(expenses):
                # Display options for updating
                print("\nOptions:\n" +
                      "1. Update Description\n"
                      "2. Update Amount\n"
                      "3. Update Category\n"
                      "4. Delete Entry")  # TO LOOK INTO: Seems to delete the
                # value before the one stated

                update_choice = input("\nEnter your choice (1-4): ")

                if update_choice == "1":
                    update_description(expenses, index)
                elif update_choice == "2":
                    update_amount(expenses, index)
                elif update_choice == "3":
                    update_category(expenses, index)
                elif update_choice == "4":
                    delete_entry(expenses, index)
                else:
                    print("Invalid choice. No changes made.")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid choice. Please enter a valid number (1-4).")

    # Save the updated expenses
    save_expenses(expenses, EXPENSES_FILE)

    return


def display_expenses(expenses):
    """
    Function to display existing expenses.

    Parameters:
    - expenses (list): List of expenses to be displayed.
    """

    headers = ["", "Timestamp", "Description", "Amount", "Category"]

    # Prepare the data for tabulate
    table_data = [[i + 1, entry[0], entry[1], "$" + entry[2], entry[3]]
                  for i, entry in enumerate(expenses)]

    # Display the table using tabulate
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def update_description(expenses, index):
    """
    Function to update description.

    Parameters:
    - expenses (list): List of expenses.
    - index (int): Index of the expense to be updated.
    """
    new_description = input("Enter the new description: ").upper()
    expenses[index][1] = new_description

    # Save the updated expenses after modifying the description
    save_expenses(expenses, EXPENSES_FILE)


def update_amount(expenses, index):
    """
    Function to update amount.

    Parameters:
    - expenses (list): List of expenses.
    - index (int): Index of the expense to be updated.
    """
    new_amount = get_valid_amount("Enter the new amount: $")
    expenses[index][2] = new_amount

    save_expenses(expenses, EXPENSES_FILE)


def update_category(expenses, index):
    """
    Function to update category.

    Parameters:
    - expenses (list): List of expenses.
    - index (int): Index of the expense to be updated.
    """

    # Gets categories from 'expenses.csv' file'
    with open(PROFILE_FILE, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        if len(header) > CATEGORIES_ROW_INDEX:
            categories = header[CATEGORIES_ROW_INDEX:]

    new_category = get_valid_category(categories)
    expenses[index][CATEGORY_COL_INDEX] = new_category

    save_expenses(expenses, EXPENSES_FILE)


def delete_entry(expenses, index):
    """
    Function to delete an entry from expenses.

    Parameters:
    - expenses (list): List of expenses.
    - index (int): Index of the expense to be deleted.
    """

    if 0 <= index < len(expenses):
        del expenses[index]
        print("Entry deleted.")

        save_expenses(expenses, EXPENSES_FILE)
    else:
        print("Invalid index. Please enter a valid index.")


def reports():
    """
    Function to access report options. There are three reports that can be
    accessed: 'Expenses Table', 'Insight Report', 'Full Report':

    1. 'Expense Table' generates a table of all expenses for that month.
    This generates a file 'expense_table.pdf' that a user can refer to
    without the need for using the program again.

    2. 'Insight Report' provides a user with insight into how their expenses
    are doing that month. It lets them know if they have negative cashflow
    and how much they're spending per category. This generates a file
    'insight_report.pdf' that a user can refer to without the need for using
    the program again.

    3. 'Full Report' provides all of the benefits of the first two options
    but creates them into a 'full-report.pdf' document for the user to view
    without the need for using the program again.
    """

    if not os.path.isfile(EXPENSES_FILE):
        print("\nNo expenses found. Generate a report after logging some " +
              "expenses.")
        return

    # Load existing expenses
    expenses = load_expenses()

    # Get unique categories
    categories = set(entry[CATEGORY_COL_INDEX] for entry in expenses
                     )
    categories.discard("Category")

    # Ask for a date in 'YYYY/MM' format
    while True:
        try:
            date_str = input(
                "\nEnter the month and year in 'YYYY/MM' format: ")
            selected_date = datetime.strptime(date_str, "%Y/%m")
            print(selected_date)
            break
        except ValueError:
            print("Invalid date format. Please enter in 'YYYY/MM' format.")

    # Filter expenses for the specified month and year
    selected_month_expenses = []

    for entry in expenses[1:]:
        entry_date = datetime.strptime(entry[0], "%Y-%m-%d %H:%M:%S")

        # Check if month and year match the selected date
        if (entry_date.month == selected_date.month and
                entry_date.year == selected_date.year):
            selected_month_expenses.append(entry)

    # Display expenses for specified month and year
    display_expenses(selected_month_expenses)

    while True:
        print("\nOptions:\n" +
              "1. Expenses Table\n" +
              "2. Insight Report\n" +
              "3. Full Report\n" +
              "4. Exit Reports")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Generate Expenses Table (PDF)
            generate_expenses_table(selected_month_expenses, date_str)
        elif choice == "2":
            # Generate Insight Report (PDF)
            generate_insight_report(selected_month_expenses,
                                    categories, date_str)
        elif choice == "3":
            # Generate Full Report (PDF)
            generate_full_report(selected_month_expenses, categories)
        elif choice == "4":
            print("Exiting report generation.")
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def generate_expenses_table(expenses, date_str):
    """
    Function to generate expense table for a month specified within
    report() parent function. Generates it as a 'expenses_table.pdf'
    file for the user to be able to review at a later date.

    Parameters:
    - expenses (list): List of expenses to include in the table.
    - selected_date (datetime): Selected year and month.
    """

    # Format expenses table using tabulate
    table_data = [["Timestamp", "Description", "Amount", "Category"]]
    table_data.extend(expenses)

    # Add dollar sign to the amounts
    for entry in table_data[1:]:
        entry[2] = f"${entry[2]}"

    # Generate PDF using reportlab
    pdf_path = EXPENSES_TABLE_PDF

    # Create a PDF document
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)

    # Add title to the document
    title = f"Expenses Table for {date_str}"
    table_data.insert(0, [title, "", "", ""])

    # Create a table with the data
    table = Table(table_data)

    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table.setStyle(style)

    # Build the PDF document
    doc.build([table])

    print(f"Expenses Table generated as '{pdf_path}'.")


def generate_insight_report(expenses, categories, date_str):
    """
    Function to generate insight report for a month specified within
    report() parent function. Generates it as a 'insight_report.pdf'
    file for the user to be able to review at a later date.

    Parameters:
    - expenses (list): List of expenses for generating insights.
    - categories (set): Set of unique expense categories.
    """

    # Create a PDF document
    pdf_path = "insight_report.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=landscape(letter))

    # Content to be added to the PDF
    content = []

    # Add title to the PDF
    title_style = getSampleStyleSheet()["Title"]
    title = Paragraph(f"Insight Report for {date_str}", title_style)
    content.append(title)

    # Implement logic to draw Insight Report (PDF)
    category_totals = {}

    for category in categories:
        total = 0.0
        for entry in expenses:
            if entry[3] == category:
                total += float(entry[2].replace("$", ""))
        category_totals[category] = total

    # Create a bar chart
    plt.figure(figsize=(7, 4))  # Adjust the figure size for landscape mode
    plt.bar(category_totals.keys(), category_totals.values())
    plt.xlabel('Categories', fontsize=10)
    plt.ylabel('Total Spending ($)', fontsize=10)
    plt.title('Insight Report - Total Spending per Category', fontsize=12)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()

    # Save the bar chart to a BytesIO object
    image_buffer = BytesIO()
    plt.savefig(image_buffer, format='png')
    plt.close()

    # Add the bar chart to the PDF
    image = Image(image_buffer)
    content.append(image)

    # Build the PDF document
    doc.build(content)

    print(f"Insight Report generated as '{pdf_path}'.")


def generate_full_report(expenses, categories):
    """
    Function to generate full report for a month specified within
    report() parent function. Generates it as a 'full_report.pdf'
    file for the user to be able to review at a later date.

    Parameters:
    - expenses (list): List of expenses for generating the full report.
    - categories (set): Set of unique expense categories.
    """

    # Set up PDF
    doc = SimpleDocTemplate(FULL_REPORT_PDF, pagesize=letter)
    elements = []

    # Add Expenses Table
    expenses_table_data = [["Timestamp", "Description", "Amount", "Category"]]
    expenses_table_data.extend(expenses)

    expenses_table = Table(expenses_table_data)
    expenses_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))

    elements.append(expenses_table)

    # Add a new line between tables
    elements.append(Spacer(1, 12))

    # Implement logic to draw Insight Report (PDF)
    category_totals = {}

    for category in categories:
        total = 0.0
        for entry in expenses:
            if entry[3] == category:
                total += float(entry[2].replace("$", ""))
        category_totals[category] = total

    # Create a bar chart
    plt.figure(figsize=(7, 4))  # Adjust the figure size for landscape mode
    plt.bar(category_totals.keys(), category_totals.values())
    plt.xlabel('Categories', fontsize=10)
    plt.ylabel('Total Spending ($)', fontsize=10)
    plt.title('Insight Report - Total Spending per Category', fontsize=12)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()

    # Save the bar chart to a BytesIO object
    image_buffer = BytesIO()
    plt.savefig(image_buffer, format='png')
    plt.close()

    elements.append(Image(image_buffer, width=400, height=300))

    # Build the PDF
    doc.build(elements)

    print("Full Report generated as 'full_report.pdf'.")


if __name__ == "__main__":
    main()

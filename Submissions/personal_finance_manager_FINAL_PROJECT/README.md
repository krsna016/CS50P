# Personal Finance Manager

#### Video Demo: https://youtu.be/KOb0DWxBY7w

#### Description:
The Personal Finance Manager is a Python-based application designed to help users manage their personal finances by tracking their income, expenses, and savings. The application allows users to input transactions, categorize them, and view summarized financial reports. It includes features such as monthly budgeting, expense tracking by category, and visual representation of financial data.

### Features:
1. **Add Income/Expense**: Users can add transactions specifying the amount, category, date, and description.
2. **View Transactions**: Users can view a list of all transactions, filtered by date range or category.
3. **Monthly Budgeting**: Users can set a monthly budget and track their expenses against it.
4. **Expense Reports**: Users can generate reports to see how much they have spent in each category.
5. **Savings Tracker**: Users can track their savings goals and progress.

### Files:
- **project.py**: Contains the main function and other core functions such as add_transaction, view_transactions, generate_report, and set_monthly_budget.
- **test_project.py**: Contains pytest test cases for the core functions to ensure they work as expected.
- **requirements.txt**: Lists the external libraries required for the project.
- **README.md**: Provides an overview of the project, its features, and instructions on how to use it.

### Design Choices:
- **JSON for Storage**: Transactions are stored in a JSON file for simplicity and ease of use. This allows the application to be easily extended to use more complex storage solutions in the future.
- **Modular Functions**: The core functionalities are implemented as separate functions, making the code modular and easier to test.
- **Command-Line Interface**: The application uses a simple command-line interface for user interaction. This can be extended to a graphical interface in future iterations.

### How to Run:
1. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the application:
    ```bash
    python project.py
    ```
3. Run the tests:
    ```bash
    pytest test_project.py
    ```

This project provides a basic structure and can be extended with additional features such as data visualization, more advanced budgeting tools, and integration with external APIs for real-time financial data.

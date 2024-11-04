# Banking System Project
### Overview
- This project is a simple Banking System implemented in Python, utilizing MySQL for data storage. It allows users to perform various banking operations, including creating accounts, depositing and withdrawing money, checking balances, and closing accounts, all through a command-line interface. The project also includes a script for setting up the MySQL database and required tables.

### Features
- Account Creation: Allows users to open a new bank account.
- Deposit: Users can deposit money into an existing account.
- Withdraw: Allows users to withdraw money from an existing account.
- Balance Inquiry: Check the current balance of an account.
- Display Account Details: Retrieve all details of a specific account.
- Account Closure: Close an existing bank account.
- Auto-Generated Account Numbers: Uses a random 10-digit generator for unique account numbers.

### Project Structure
* banking_system.py: Contains the main Python script for all banking operations.
* database_setup.py: Python script to set up the MySQL database and required tables for the project.

### Database Setup
- To set up the database, run the database_setup.py script. This script will:

1. Connect to MySQL.
2. Create a new database named bank.
3. Create two tables:
  - account: Stores basic account information such as name, account number, date of birth, phone number, address, email, and opening balance.
  - amount: Stores the account number, account holder's name, and current balance.

### Table Schema
* account Table

  - Name: Account holder's name.
  - Account_no: Unique 10-digit account number (primary key).
  - Date_of_birth: Account holder's date of birth.
  - Phone_no: Unique phone number of the account holder.
  - Address: Address of the account holder.
  - Email: Unique email ID of the account holder.
  - Opening_Balance: Initial deposit balance.
* amount Table

  - Name: Account holder's name.
  - Account_no: Foreign key linking to the account table.
  - Balance: Current balance in the account.

### Usage
  #### Prerequisites
  - Python 3.x

  - MySQL server installed and running.

  - mysql-connector-python package installed. You can install it with:

    - pip install mysql-connector-python
  #### Step 1: Set Up Database
  - Run the database_setup.py script to create the required database and tables:

    - python database_setup.py
  - This will set up the bank database and create the account and amount tables.

  #### Step 2: Run the Banking System
  - After setting up the database, run the main banking system program:

    - python banking_system.py

### CLI Options
- The following options are available in the command-line interface:

1. Open New Account: Creates a new bank account and assigns a unique account number.
2. Deposit Amount: Deposits a specified amount into an existing account.
3. Withdraw Amount: Withdraws a specified amount from an existing account.
4. Balance Enquiry: Displays the current balance for a specified account.
5. Display Customer Details: Displays all details for a specified account.
6. Close an Account: Deletes an account and all related data from the database.
7. Exit Digito: Exits the program.

### Notes
- This system assumes that all account numbers are unique and generated randomly.
- The amount table and the account table are linked by Account_no, which allows easy retrieval and modification of account balances.
- Remember to update the MySQL connection details in database_setup.py and banking_system.py as per your MySQL setup.

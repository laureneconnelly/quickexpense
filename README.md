# quickexpense

For my project I chose to create an expense log database that will track expenses for a company. I 
would like to be able to post, get, pull/patch, delete any expenses that occur by 
employee id, dept, GL account, or amount.
 

The functions include:
1. employee charge types
2. list employees by username, charge type, expense
3. list expense by dept, GL account, or employee


API Reference Table

| Endpoint Paths | Methods | Parameters
| -------------- | ------- | -----------
|   /Employees   |   GET   | Employees
|   /Employees   |   GET   | Employees/id
|   /Employees   |   POST  | Employees
|   /Employees   |  DELETE | Employees/id
|   /Departments |   GET   | Departments
|   /Departments |   GET   | Departments/id
|   /Departments |   POST  | Departments
|   /Departments |  DELETE | Departments/id
|   /Expenses    |   GET   | Expenses
|   /Expenses    |   GET   | Expenses /id
|   /Expenses    |   POST  | Expenses 
|   /Expenses    |   POST  | Expenses/gl_account_id/belongs_to 
|   /Expenses    |   POST  | Expenses/deparment_id/belongs_to 
|   /Expenses    |   POST  | Expenses/employee_id/belongs_to 
|   /Expenses    |  DELETE | Expenses 
|  /GL_Accounts  |   GET   | GL_Accounts
|  /GL_Accounts  |   GET   | GL_Accounts/id
|  /GL_Accounts  |   POST  | GL_Accounts








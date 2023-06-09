import sqlite3
import json
from models import Employee, Location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

# def get_all_employees():
#     """get all employees docstring
#     """
#     return EMPLOYEES

def get_all_employees():
    """get all employees SQL"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id location_id,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN Location l
            ON l.id = e.location_id
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # # Create an employee instance from the current row.
            # # Note that the database fields are specified in
            # # exact order of the parameters defined in the
            # # Employee class above.
            # employee = Employee(row['id'], row['name'])

            # employees.append(employee.__dict__)

            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            location = Location(row['location_id'], row['location_name'], row['location_address'])

            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return employees

# # Function with a single parameter
# def get_single_employee(id):
#     # Variable to hold the found employee, if it exists
#     """get single employee docstring
#     """
#     requested_employee = None

#     # Iterate the EMPLOYEES list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for employee in EMPLOYEES:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if employee["id"] == id:
#             requested_employee = employee

#     return requested_employee

def get_single_employee(id):
    """get single SQL"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'],
                            data['address'], data['location_id'])

        return employee.__dict__

def create_employee(employee):
    """for do_POST
    """
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

# def delete_employee(id):
#     """deletes an element from list
#     """
#     employee_index = -1
#     for index, employee in enumerate(EMPLOYEES):
#         if employee["id"] == id:
#             employee_index = index
#     if employee_index >= 0:
#         EMPLOYEES.pop(employee_index)

def delete_employee(id):
    """Deletes single employee
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    """POST will replace whole resource with UPDATE
    """
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

def get_employees_by_location(location_id):
    """gets employees by their location ID"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id
        from Employee e
        WHERE e.location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return employees

```python
import sqlite3

# connecting to sqlite
con = sqlite3.connect('sample.db')

# creating cursor
cur = con.cursor()

# Drop table if it already exists
cur.execute('''DROP TABLE IF EXISTS employees''')

# Creating table
cur.execute('''CREATE TABLE employees (
                emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                joining_date TEXT NOT NULL,
                salary REAL)''')

# Data to be inserted
data = [('John Doe', 'HR', '2019-01-01', 70000),
        ('Jane Smith', 'IT', '2020-03-15', 80000),
        ('Mike Johnson', 'Finance', '2018-07-23', 75000)]

# Inserting data
cur.executemany('''INSERT INTO employees (name, department, joining_date, salary)
                   VALUES (?, ?, ?, ?)''', data)

# Commit the changes
con.commit()

# Fetching data
cur.execute('''SELECT * FROM employees''')
rows = cur.fetchall()
for row in rows:
    print(row)

# Update salary
cur.execute('''UPDATE employees SET salary = salary * 1.1 WHERE department = 'HR' ''')

# Commit the changes
con.commit()

# Fetching data after update
cur.execute('''SELECT * FROM employees''')
rows = cur.fetchall()
for row in rows:
    print(row)

# Closing the connection
con.close()
```

### README Template

```markdown
# Real-World SQL Implementation Using Python

## Overview

This project demonstrates how to use SQL with Python to manage a simple employee database. It covers creating a database, inserting data, updating records, and querying the database using SQLite. This project is designed for machine learning developers and data scientists who want to enhance their SQL skills and improve their CVs.

## Features

- **Database Creation**: Create and manage a SQLite database.
- **Data Insertion**: Insert multiple records into a table.
- **Data Update**: Perform updates on existing records.
- **Data Query**: Fetch and display records from the database.
- **Data Manipulation**: Use SQL commands to manipulate and query data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone the repository and install the required dependencies.

```bash
git clone https://github.com/yourusername/realworld-sql-python.git
cd realworld-sql-python
pip install -r requirements.txt
```

## Usage

1. **Run the Script**: Execute the provided Python script to create the database, insert data, update records, and query the database.

    ```bash
    python SQL.py
    ```

## Examples

### Connecting to SQLite Database

The script starts by connecting to a SQLite database. If the database does not exist, it will be created.

```python
import sqlite3

con = sqlite3.connect('sample.db')
cur = con.cursor()
```

### Creating a Table

The script creates an `employees` table with columns for `emp_id`, `name`, `department`, `joining_date`, and `salary`.

```python
cur.execute('''CREATE TABLE employees (
                emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                joining_date TEXT NOT NULL,
                salary REAL)''')
```

### Inserting Data

Three records are inserted into the `employees` table.

```python
data = [('John Doe', 'HR', '2019-01-01', 70000),
        ('Jane Smith', 'IT', '2020-03-15', 80000),
        ('Mike Johnson', 'Finance', '2018-07-23', 75000)]

cur.executemany('''INSERT INTO employees (name, department, joining_date, salary)
                   VALUES (?, ?, ?, ?)''', data)
```

### Querying Data

All records from the `employees` table are fetched and displayed.

```python
cur.execute('''SELECT * FROM employees''')
rows = cur.fetchall()
for row in rows:
    print(row)
```

### Updating Data

The salary of employees in the HR department is increased by 10%.

```python
cur.execute('''UPDATE employees SET salary = salary * 1.1 WHERE department = 'HR' ''')
con.commit()
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

```

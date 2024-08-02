
---

# SQL Database Interaction Script

Welcome to the SQL Database Interaction project! This repository contains a Python script to interact with a MySQL database, including creating tables and inserting fake data using the Faker library. you can use this script to set up and populate a database for various data analysis and machine learning projects.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a script to interact with a MySQL database. The script includes functionality for connecting to the database, creating tables based on a specified schema, and populating these tables with fake data for testing and development purposes.

## Installation

To get started with the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/sql-database-interaction.git
cd sql-database-interaction
pip install -r requirements.txt
```

Ensure you have MySQL installed and running on your machine. Update the connection parameters in the script as needed.

### Setting Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Here's how you can set it up:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

To use the script, run the following command:

```bash
python SQL.py
```

### Example Usage in Script

You can also import specific functions from the script into your Python project and use them as follows:

```python
from SQL import create_tables, populate_tables

# Create tables
create_tables()

# Populate tables with fake data
populate_tables()
```

## Functionality

The script uses the `mysql.connector` library to interact with the MySQL database and the `Faker` library to generate fake data. Here's a brief overview of the main functions:

### Connecting to MySQL

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    db="company"
)

mycursor = db.cursor()
```

### Creating Tables

The script creates tables based on a specified schema. For example, creating an `MDF` table:

```python
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS MDF (
        mdf_id INT AUTO_INCREMENT PRIMARY KEY,
        raw_mdf VARCHAR(255),
        processed_mdf VARCHAR(255)
    )
''')
```

### Populating Tables with Fake Data

The script uses the `Faker` library to generate and insert fake data into the tables:

```python
from faker import Faker

fake = Faker()

def populate_mdf_table():
    for _ in range(100):
        mycursor.execute('''
            INSERT INTO MDF (raw_mdf, processed_mdf)
            VALUES (%s, %s)
        ''', (fake.text(), fake.text()))
    db.commit()
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

import mysql.connector
from faker import Faker

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    db="company"
)

mycursor = db.cursor()

# Create tables based on the provided ERD

# Create MDF table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS MDF (
        mdf_id INT AUTO_INCREMENT PRIMARY KEY,
        raw_mdf VARCHAR(255),
        melamine_mdf VARCHAR(255),
        super_curved VARCHAR(255)
    )
''')

# Create Neopan table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Neopan (
        neopan_id INT AUTO_INCREMENT PRIMARY KEY,
        super_curved_mdf VARCHAR(255),
        touch_wood VARCHAR(255),
        finish_foil VARCHAR(255),
        melamine_neopan VARCHAR(255),
        low_weight VARCHAR(255),
        water_resistance VARCHAR(255)
    )
''')

# Create Product table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        color VARCHAR(255),
        price DECIMAL(10, 2),
        grade VARCHAR(255),
        dimension VARCHAR(255),
        mdf_id INT,
        neopan_id INT,
        FOREIGN KEY (mdf_id) REFERENCES MDF(mdf_id),
        FOREIGN KEY (neopan_id) REFERENCES Neopan(neopan_id)
    )
''')

# Create Employee table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        role VARCHAR(255),
        fname VARCHAR(255),
        lname VARCHAR(255),
        number VARCHAR(255),
        birthdate DATE,
        regional_code VARCHAR(255)
    )
''')

# Create Customer table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        fname VARCHAR(255),
        lname VARCHAR(255),
        number VARCHAR(255),
        address VARCHAR(255)
    )
''')

# Create Supplier table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Supplier (
        supplier_id INT AUTO_INCREMENT PRIMARY KEY,
        fname VARCHAR(255),
        lname VARCHAR(255),
        number VARCHAR(255)
    )
''')

# Create Supplier_Product table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Supplier_Product (
        supplier_id INT,
        product_id INT,
        PRIMARY KEY (supplier_id, product_id),
        FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
        FOREIGN KEY (product_id) REFERENCES Product(product_id)
    )
''')

# Create Inventory table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Inventory (
        inventory_id INT AUTO_INCREMENT PRIMARY KEY,
        location_address VARCHAR(255),
        product_quantity INT,
        product_id INT,
        FOREIGN KEY (product_id) REFERENCES Product(product_id)
    )
''')

# Create Delivery table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Delivery (
        delivery_id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE,
        location VARCHAR(255),
        address VARCHAR(255),
        car_type VARCHAR(255)
    )
''')

# Create Purchase table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Purchase (
        purchase_id INT AUTO_INCREMENT PRIMARY KEY,
        cost DECIMAL(10, 2),
        product_id INT,
        customer_id INT,
        delivery_id INT,
        date DATE,
        FOREIGN KEY (product_id) REFERENCES Product(product_id),
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
        FOREIGN KEY (delivery_id) REFERENCES Delivery(delivery_id)
    )
''')

# Commit changes
db.commit()

# Insert example data into tables
sql = "INSERT INTO MDF (raw_mdf, melamine_mdf, super_curved) VALUES (%s, %s, %s)"
values = ("Raw MDF Example", "Melamine MDF Example", "Super Curved Example")
mycursor.execute(sql, values)
db.commit()

print(mycursor.rowcount, "row was inserted")

# Select all from the MDF table
mycursor.execute("SELECT * FROM MDF")
for x in mycursor.fetchall():
    print(x)

# Initialize Faker
fake = Faker()


# Generate and insert random sample data into MDF table
mdf_values = [(fake.word(), fake.word(), fake.word()) for _ in range(5)]
mycursor.executemany("INSERT INTO MDF (raw_mdf, melamine_mdf, super_curved) VALUES (%s, %s, %s)", mdf_values)

# Generate and insert random sample data into Neopan table
neopan_values = [(fake.word(), fake.word(), fake.word(), fake.word(), fake.word(), fake.word()) for _ in range(5)]
mycursor.executemany("INSERT INTO Neopan (super_curved_mdf, touch_wood, finish_foil, melamine_neopan, low_weight, water_resistance) VALUES (%s, %s, %s, %s, %s, %s)", neopan_values)

# Generate and insert random sample data into Product table
product_values = [(fake.color_name(), round(random.uniform(10, 500), 2), fake.word(), f"{random.randint(10, 200)}x{random.randint(10, 200)}", random.randint(1, 5), random.randint(1, 5)) for _ in range(5)]
mycursor.executemany("INSERT INTO Product (color, price, grade, dimension, mdf_id, neopan_id) VALUES (%s, %s, %s, %s, %s, %s)", product_values)

# Generate and insert random sample data into Employee table
employee_values = [(fake.job(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.date_of_birth(), fake.zipcode()) for _ in range(5)]
mycursor.executemany("INSERT INTO Employee (role, fname, lname, number, birthdate, regional_code) VALUES (%s, %s, %s, %s, %s, %s)", employee_values)

# Generate and insert random sample data into Customer table
customer_values = [(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address()) for _ in range(5)]
mycursor.executemany("INSERT INTO Customer (fname, lname, number, address) VALUES (%s, %s, %s, %s)", customer_values)

# Generate and insert random sample data into Supplier table
supplier_values = [(fake.first_name(), fake.last_name(), fake.phone_number()) for _ in range(5)]
mycursor.executemany("INSERT INTO Supplier (fname, lname, number) VALUES (%s, %s, %s)", supplier_values)

# Generate and insert random sample data into Supplier_Product table
supplier_product_values = [(random.randint(1, 5), random.randint(1, 5)) for _ in range(5)]
mycursor.executemany("INSERT INTO Supplier_Product (supplier_id, product_id) VALUES (%s, %s)", supplier_product_values)

# Generate and insert random sample data into Inventory table
inventory_values = [(fake.address(), random.randint(1, 100), random.randint(1, 5)) for _ in range(5)]
mycursor.executemany("INSERT INTO Inventory (location_address, product_quantity, product_id) VALUES (%s, %s, %s)", inventory_values)

# Generate and insert random sample data into Delivery table
delivery_values = [(fake.date(), fake.city(), fake.address(), fake.vehicle_make()) for _ in range(5)]
mycursor.executemany("INSERT INTO Delivery (date, location, address, car_type) VALUES (%s, %s, %s, %s)", delivery_values)

# Generate and insert random sample data into Purchase table
purchase_values = [(round(random.uniform(50, 1000), 2), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), fake.date()) for _ in range(5)]
mycursor.executemany("INSERT INTO Purchase (cost, product_id, customer_id, delivery_id, date) VALUES (%s, %s, %s, %s, %s)", purchase_values)

# Commit changes
db.commit()

# Select and display all from each table
tables = ["MDF", "Neopan", "Product", "Employee", "Customer", "Supplier", "Supplier_Product", "Inventory", "Delivery", "Purchase"]
for table in tables:
    print(f"\nTable: {table}")
    mycursor.execute(f"SELECT * FROM {table}")
    for row in mycursor.fetchall():
        print(row)

# Close connection
db.close()
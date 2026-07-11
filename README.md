💊 DMS Medical Store - Pharmacy Management System
A robust, backend-driven Command Line Interface (CLI) application designed to manage pharmacy operations. This system handles inventory management, real-time database updates, and customer billing, making it a complete solution for day-to-day medical store administration.

Built over the course of 3 months, this project focuses on raw backend mechanics, database relational mapping, and interactive terminal interfaces.

🚀 Key Features
Inventory Management: Add new medicines with complete metadata (Manufacturer, Expiry, Price, Quantity).

Dynamic Restocking: Seamlessly update existing inventory levels without overwriting previous data.

Catalog Viewing & Searching: Display all available inventory or search for specific medicines via an integrated ID system (Formatted cleanly using PrettyTable).

Automated Billing Engine:

Add multiple medicines to a single customer's cart.

Auto-calculates total amounts based on real-time database pricing.

Generates digital bills stored directly in the database for financial tracking.

Database Persistence: All operations immediately commit to a live MySQL backend, ensuring zero data loss upon exiting the application.

💻 Tech Stack
Language: Python 3.x

Database: MySQL

Libraries Used:

mysql.connector (Database communication)

prettytable (CLI data formatting)

time, random (System utilities)

🗄️ Database Schema
To run this project locally, you must create a database named pharmacyy with the following two tables:

1. medical (Inventory Table)

m_id (INT, Primary Key) - Medicine ID

m_name (VARCHAR) - Name of the medicine

m_manufacturer (VARCHAR) - Manufacturer name

m_mdate (VARCHAR) - Date of Manufacture

m_expiry (VARCHAR) - Expiry Date

m_qnt (INT) - Stock Quantity

m_price (INT) - Price per unit

2. bill1 (Billing Records Table)

bn (VARCHAR, Primary Key) - Bill Number

name (VARCHAR) - Customer Name

med (VARCHAR) - Medicines purchased

am (INT) - Total Bill Amount

b (VARCHAR) - Date of billing (YYYY-MM-DD)

🛠️ Installation & Setup
1. Clone the repository

Bash
git clone https://github.com/YourUsername/YourRepositoryName.git
cd YourRepositoryName
2. Install requirements

Bash
pip install mysql-connector-python prettytable
3. Configure Database

Open your local MySQL Workbench or terminal.

Run CREATE DATABASE pharmacyy;

Create the tables based on the schema above.

Important: Open the Python script and update line 2 to match your local MySQL credentials:con = m.connect(host='localhost', user='root', password='YOUR_PASSWORD', database='pharmacyy')

4. Run the Application

Bash
python main.py
📈 Future Scope & Improvements
As this project scales, future updates may include:

Transitioning from raw SQL string formatting to fully parameterized queries to prevent SQL injection.

Implementation of a Graphical User Interface (GUI) using Tkinter or PyQt.

Low-stock automated alerts when a medicine's quantity drops below a certain threshold.

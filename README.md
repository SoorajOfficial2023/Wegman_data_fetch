Wegmans Data Scraping and Storage

Overview
This project demonstrates how to scrape product data from the Wegmans website using Python and store it in a MySQL database. The script periodically fetches information about "Pink Lady Apple" products and stores relevant details like name, base price, and scrape datetime.

Features
Automated Data Scraping: Uses Python requests library to fetch data from Wegmans API.
Data Processing: Utilizes pandas for data manipulation and filtering based on product name and availability status.
Database Storage: Stores processed data in MySQL using SQLAlchemy.
Periodic Execution: Runs the scraping and storage process automatically every 5 minutes using Python's time module.

Requirements
Python 3.x
requests, pandas, SQLAlchemy, and pymysql Python libraries
MySQL database
Setup

Clone the Repository:
git clone https://github.com/SoorajOfficial2023/Wegman_data_fetch

cd wegmans-data-scraping

Install Dependencies:
pip install -r requirements.txt
Configuration:
Replace your_cookie_here in dataScraping.py with your Wegmans website cookie.
Update your_username, your_password_here, and your_database with your MySQL credentials in dataScraping.py.

Run the Script:
python dataScraping.py

Database Structure
The scraped data is stored in MySQL with the following structure:

Table Name: Wegmans_data
Columns:
id (Integer, Primary Key, Autoincrement)
name (String, 255)
base_price (Numeric, 10, 2)
scrape_datetime (DateTime)
Contributing
Contributions are welcome! Fork the repository, create a new branch, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

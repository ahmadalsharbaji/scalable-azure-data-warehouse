import os

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Load environment variables from .env file
load_dotenv()

# Retrieve database connection credentials from environment variables
host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")

# Define the SSL mode for database connection
sslmode = "require"
dbname = "postgres"

# Create the connection string to connect to PostgreSQL
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)

# Establish the connection to the PostgreSQL database
conn = psycopg2.connect(conn_string)

# Set the isolation level for the connection to autocommit mode
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
print("Connection established")

# Create a cursor to interact with the database
cursor = conn.cursor()

# Drop the database if it exists and create a new one
cursor.execute('DROP DATABASE IF EXISTS dwh_analytics')
cursor.execute("CREATE DATABASE dwh_analytics")

# Commit the changes and clean up the initial connection
conn.commit()
cursor.close()
conn.close()

# Reconnect to the newly created database
dbname = "dwh_analytics"
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

# Create a new cursor for the new database connection
cursor = conn.cursor()


# Helper function to drop and recreate a table
def drop_recreate(c, tablename, create):
    """
    Drops the specified table if it exists, then creates a new table based on the provided SQL statement.

    Args:
    c (psycopg2.cursor): The database cursor used to execute SQL commands.
    tablename (str): The name of the table to be dropped and recreated.
    create (str): The SQL statement to create the table.
    """
    c.execute("DROP TABLE IF EXISTS {0};".format(tablename))  # Drop the table if it exists
    c.execute(create)  # Create the table with the provided SQL statement
    print("Finished creating table {0}".format(tablename))


# Helper function to populate a table from a CSV file
def populate_table(c, filename, tablename):
    """
    Populates a table with data from a CSV file using the COPY command.

    Args:
    c (psycopg2.cursor): The database cursor used to execute SQL commands.
    filename (str): The path to the CSV file containing the data to be inserted.
    tablename (str): The name of the table to populate.
    """
    f = open(filename, 'r')  # Open the CSV file for reading
    try:
        cursor.copy_from(f, tablename, sep=",", null="")  # Load data from the CSV file into the table
        conn.commit()  # Commit the changes to the database
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)  # Print any error encountered during the process
        conn.rollback()  # Rollback the transaction in case of an error
        cursor.close()  # Close the cursor
    print("Finished populating {0}".format(tablename))  # Indicate that the table has been populated


# Create and populate the "rider" table
table = "rider"
filename = './riders.csv'
create = "CREATE TABLE rider (rider_id INTEGER PRIMARY KEY, first VARCHAR(50), last VARCHAR(50), address VARCHAR(100), birthday DATE, account_start_date DATE, account_end_date DATE, is_member BOOLEAN);"
drop_recreate(cursor, table, create)  # Drop and recreate the table
populate_table(cursor, filename, table)  # Populate the table with data from the CSV file

# Create and populate the "payment" table
table = "payment"
filename = './payments.csv'
create = "CREATE TABLE payment (payment_id INTEGER PRIMARY KEY, date DATE, amount MONEY, rider_id INTEGER);"
drop_recreate(cursor, table, create)  # Drop and recreate the table
populate_table(cursor, filename, table)  # Populate the table with data from the CSV file

# Create and populate the "station" table
table = "station"
filename = './stations.csv'
create = "CREATE TABLE station (station_id VARCHAR(50) PRIMARY KEY, name VARCHAR(75), latitude FLOAT, longitude FLOAT);"
drop_recreate(cursor, table, create)  # Drop and recreate the table
populate_table(cursor, filename, table)  # Populate the table with data from the CSV file

# Create and populate the "trip" table
table = "trip"
filename = './trips.csv'
create = "CREATE TABLE trip (trip_id VARCHAR(50) PRIMARY KEY, rideable_type VARCHAR(75), start_at TIMESTAMP, ended_at TIMESTAMP, start_station_id VARCHAR(50), end_station_id VARCHAR(50), rider_id INTEGER);"
drop_recreate(cursor, table, create)  # Drop and recreate the table
populate_table(cursor, filename, table)  # Populate the table with data from the CSV file

# Clean up by committing changes, closing the cursor and the connection
conn.commit()
cursor.close()
conn.close()

print("All done!")  # Indicate that the process is complete

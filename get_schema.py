import pyodbc

# --- Configuration ---
server_name = r"YASSINE\SQLEXPRESS"  # Your SQL Server instance
mdf_file = r"D:\SQLData\AirbnbDataWarehouse.mdf"  # Path to your .mdf
db_name = "AirbnbDataWarehouse"  # Logical database name

# --- Connection string for pyodbc ---
# Using Trusted Connection (Windows authentication)
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server_name};"
    f"Trusted_Connection=yes;"
    f"AttachDbFilename={mdf_file};"
    f"DATABASE={db_name};"
)

# --- Attempt connection ---
try:
    cnxn = pyodbc.connect(conn_str)
    print("✅ Successfully connected to the database.")
except pyodbc.Error as ex:
    print("❌ Error connecting to the database:")
    print(ex)
    print("Check that SQL Server is running, the ODBC driver is installed,")
    print("and that the .mdf file is accessible and not already attached.")
    cnxn = None

# --- Get Schema for Tables ---
if cnxn:
    try:
        cursor = cnxn.cursor()
        for table in ['dim_hosts', 'fact_reviews', 'dim_listings']:
            print(f"--- Schema for {table} ---")
            cursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'")
            for row in cursor.fetchall():
                print(f"- {row[0]}: {row[1]}")
    except Exception as e:
        print(f"Error getting schema: {e}")
    finally:
        cnxn.close()

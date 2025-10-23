import json

# Corrected code for the data loading cell
new_code = """# Load necessary tables into Polars DataFrames
try:
    # Ensure you have connectorx installed: pip install connectorx
    params = urllib.parse.quote_plus(conn_str)
    uri = f"mssql+pyodbc:///?odbc_connect={{params}}"

    df_hosts = pl.read_database_uri(
        query='SELECT * FROM dim_hosts',
        uri=uri,
        partition_on='host_id',
        partition_num=4,
        engine='connectorx'
    ).collect()

    df_reviews = pl.read_database_uri(
        query="SELECT review_id, listing_id, date_id, reviewer_id, reviewer_name, comments FROM fact_reviews",
        uri=uri,
        partition_on='review_id',
        partition_num=4,
        schema_overrides={'comments': pl.Utf8},
        engine='connectorx'
    ).collect()

    df_listings = pl.read_database_uri(
        query='SELECT * FROM dim_listings',
        uri=uri,
        partition_on='listing_id',
        partition_num=4,
        engine='connectorx'
    ).collect()

    print("DataFrames loaded successfully: df_hosts, df_reviews, df_listings")
    
except Exception as e:
    print(f"Error loading data: {e}")

print("--- df_hosts Info ---")
print(df_hosts)
print("--- df_reviews Info ---")
print(df_reviews)
print("--- df_listings Info ---")
print(df_listings)
"""

# Read the existing notebook
with open('eda.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Find the data loading cell and update its source
for cell in notebook['cells']:
    if cell['cell_type'] == 'code' and 'pl.scan_database' in ''.join(cell['source']):
        cell['source'] = [line + '\n' for line in new_code.split('\n')]
        # Clear previous outputs and execution count
        cell['outputs'] = []
        cell['execution_count'] = None
        break

# Write the updated notebook back to the file
with open('eda.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2)

print("✅ Notebook 'eda.ipynb' has been updated successfully.")

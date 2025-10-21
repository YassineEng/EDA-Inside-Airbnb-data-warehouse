# EDA-Inside-Airbnb-data-warehouse

## Setup

### Install Dependencies

The following Python packages are required for this project:

- `pandas`: For data manipulation and analysis.
- `pyodbc`: To connect to the SQL Server database.
- `jupyter`: To create and run Jupyter notebooks.
- `matplotlib`: For data visualization.
- `seaborn`: For enhanced data visualization.
- `sqlalchemy`: For SQL database toolkit and Object Relational Mapper.
- `langdetect`: For language detection in review comments.

You can install these dependencies using `uv` by running the following command:

```bash
uv pip install pandas pyodbc jupyter matplotlib seaborn sqlalchemy langdetect
```

### Jupyter Notebook (`eda.ipynb`)

The analysis is conducted in `eda.ipynb`. This notebook includes:

*   **Database Connection:** Establishes a connection to the SQL Server database (`D:\SQLData\AirbnbDataWarehouse.mdf`). **Note:** You need to replace `'YOUR_SERVER_NAME'` in the notebook with your actual SQL Server instance name and ensure the `.mdf` file is attached to a running SQL Server instance.
*   **Data Loading:** Loads `dim_hosts`, `fact_reviews`, and `dim_listings` tables into pandas DataFrames for analysis.
*   **Null Value Examination:** Identifies and visualizes null values across all columns in the loaded DataFrames using heatmaps.
*   **"Unknown" Value Examination:** Checks for common "unknown" representations (e.g., 'unknown', 'n/a', empty strings) in string columns and visualizes their counts.
*   **Correlation Analysis:** Computes and visualizes the correlation matrix for numerical columns in `dim_listings` using a heatmap.
*   **Language Detection in Reviews:**
    *   Detects the language of review comments in `fact_reviews`.
    *   Counts and visualizes the distribution of distinct languages.
    *   Calculates the percentage of foreign language reviews for a specified city (e.g., Paris).
*   **Host Country Correction:** Addresses inconsistencies in the `host_country` column of `dim_hosts` by replacing US state abbreviations and common variations with "United States", creating a `corrected_country` column.
*   **Distinct Value Check and Standardization:** Examines categorical columns for inconsistent distinct values and provides examples of how to standardize them.
*   **Additional Recommended Analysis:** Suggests further avenues for exploration, such as time-series analysis, geospatial analysis, price determinants, host behavior analysis, sentiment analysis, and availability analysis.
This code performs exploratory data analysis tasks on customer data stored in two CSV files:

customer_rec.csv: Contains customer transaction records.
customer_info.csv: Contains customer information.
Code walkthrough:

Import libraries:

pandas (pd) for data manipulation.
numpy (np) for numerical operations (not used extensively in this code).

Load data:

df = pd.read_csv('customer_rec.csv'): Reads the customer transaction data into a Pandas DataFrame named df.
df1 = pd.read_csv('customer_info.csv'): Reads the customer information data into a Pandas DataFrame named df1.

Explore data (customer_rec.csv):

df.head(): Displays the first few rows of the df DataFrame to get a glimpse of the data structure.
df.isnull().sum(): Shows the number of missing values in each column of df. This helps identify potential data quality issues.

Clean data (customer_rec.csv):

df.drop(columns=['Reference','Purchase order no.','Text','Terms of Payment']): Drops four specified columns from df. These columns might not be relevant for the current analysis or might introduce unnecessary complexity.
df.dropna(): Drops rows with any missing values. This can be a harsh approach, so consider if it's appropriate for your analysis. You might explore alternative methods for handling missing values later.

Explore data (customer_info.csv):

df1.head(): Displays the first few rows of the df1 DataFrame.
df1.isnull().sum(): Shows the number of missing values in each column of df1.

Clean data (customer_info.csv):

df1.drop(columns=['Street','Postal Code','City','Currency','Telephone 1','Payment Term (Sales Org)','Created on']): Drops seven specified columns from df1. Similar to the cleaning step for df, consider if removing these columns aligns with your analysis goals.
Merge DataFrames:

customer_df= pd.merge(df,df1, on='Customer_ID'): Merges the two DataFrames (df and df1) based on the common column "Customer_ID". This creates a new DataFrame customer_df that combines customer transaction data with customer information.

Identify Duplicates:

customer_df = customer_df[customer_df.duplicated()]: Identifies and keeps all duplicate rows in customer_df. This might not be the intended outcome, so refer to the comments to understand the purpose.
print("Sample Duplicate Rows (all kept):"): Prints the first few rows of the identified duplicates for inspection.

Remove Duplicates (corrected):

customer_df = customer_df.drop_duplicates(): Removes duplicate rows from customer_df (default keeps the first occurrence). This step should be included in the final data cleaning process.

Filter by Document Type (corrected):

customer_df = customer_df[customer_df['Document type'] == 'RV']: Filters the customer_df DataFrame to keep only rows where the "Document type" column has the exact value "RV" (case-sensitive). This assumes you're interested in analyzing data related to a specific document type.

Explore filtered data:
print(customer_df.head()): Displays the first few rows of the filtered customer_df to see the results of the filtering step.

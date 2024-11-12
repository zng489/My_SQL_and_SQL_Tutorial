# Databricks notebook source
pip install duckdb

# COMMAND ----------

pip install faker

# COMMAND ----------


import duckdb
from duckdb.typing import *
from faker import Faker
from pyspark.sql.window import Window
import pyspark.sql.functions as f
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import datediff,col,when

# COMMAND ----------

var_adls_uri = 'abfss://datalake@cnibigdatadlsgen2.dfs.core.windows.net'
trs_rais_vinculo2008a2018_path = '{uri}/trs/me/rais_vinculo'.format(uri=var_adls_uri)

df_rais_vinculo2008a2018 = spark.read.format("parquet").option("header","true").load(trs_rais_vinculo2008a2018_path)
display(df_rais_vinculo2008a2018.limit(3))

# COMMAND ----------

import duckdb
from duckdb.typing import *
from faker import Faker

def generate_random_name():
    fake = Faker()
    return fake.name()

duckdb.create_function("random_name", generate_random_name, [], VARCHAR)
res = duckdb.sql("SELECT random_name()").fetchall()
print(res)

# COMMAND ----------


import duckdb
from duckdb.typing import *
from faker import Faker
from pyspark.sql.window import Window
import pyspark.sql.functions as f
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import datediff,col,when

# COMMAND ----------

var_adls_uri = 'abfss://datalake@cnibigdatadlsgen2.dfs.core.windows.net'

# COMMAND ----------

!pip install fsspec

# COMMAND ----------

!pip install duckdb pandas
#pip install duckdb

import duckdb
import pandas
import pandas as pd

# Create a Pandas dataframe

###############################################################################################################
# Specify the path to your Snappy-compressed Parquet file
# parquet_file_path = r'CD_UF=53'

# Read Parquet file into a pandas DataFrame
my_df = pd.read_csv('/dbfs/Streaming/part-00000-tid-3736507327420573615-677f1d89-9f46-4eab-971a-4929f8625a8d-16-1-c000.csv')
# my_df = pd.read_parquet(parquet_file_path)
# print(my_df)
###############################################################################################################


# COMMAND ----------

my_df

# COMMAND ----------

# create the table "my_table" from the DataFrame "my_df"
# Note: duckdb.sql connects to the default in-memory database connection
duckdb.sql("DROP TABLE IF EXISTS my_table")


# insert into the table "my_table" from the DataFrame "my_df"
duckdb.sql("CREATE TABLE my_table AS SELECT * FROM my_df")


# insert into the table "my_table" from the DataFrame "my_df"
## duckdb.sql("SELECT * FROM my_table")


# Two kind of ways, how to connect using duckdb

# COMMAND ----------

###############################################################################################################
# import duckdb

# Connect to the database
# con = duckdb.connect(database='your_database.db')

# Execute the query
# result = con.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'my_table'")
###############################################################################################################

result = duckdb.sql("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'my_table'")

rows = result.fetchall()

# Extract column names from the result
column_names = [row[0] for row in rows]

# Print or use the column names as needed
# print(column_names)

# COMMAND ----------

column_names

# COMMAND ----------

rows

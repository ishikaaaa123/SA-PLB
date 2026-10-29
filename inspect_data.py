
import pandas as pd

file_path = "data/dataset-replica-mcr-mt.csv"

# The CSV has no header row, so we supply the documented names.
column_names = [
    "timestamp_1",
    "timestamp_2",
    "microservice_id",
    "container_id",
    "replica_count",
    "microservice_time",
    "call_rate",
]

df = pd.read_csv(
    file_path,
    header=None,
    names=column_names
)

print("\n--- FIRST FIVE ROWS ---")
print(df.head().to_string(index=False))

print("\n--- DATASET SHAPE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- NUMERICAL SUMMARY ---")
print(df.describe().T)

print("\n--- UNIQUE MICROSERVICES AND CONTAINERS ---")
print("Microservices:", df["microservice_id"].nunique())
print("Containers:", df["container_id"].nunique())

print("\n--- TIMESTAMP RANGES ---")
print(df[["timestamp_1", "timestamp_2"]].agg(["min", "max"]))




print("\n--- DATASET FILE CHECK ---")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Column names:", df.columns.tolist())
print("First 3 rows:")
print(df.head(3).to_string(index=False))


import pandas as pd

file_path = "data/dataset-replica-mcr-mt.csv"

columns = [
    "timestamp_1",
    "timestamp_2",
    "microservice_id",
    "container_id",
    "replica_count",
    "microservice_time",
    "call_rate",
]

df = pd.read_csv(file_path, header=None, names=columns)

print("--- TIMESTAMP_1 FOR EACH TIMESTAMP_2 ---")

summary = df.groupby("timestamp_2")["timestamp_1"].agg(
    ["count", "min", "median", "max"]
)

print(summary.head(10).to_string())

print("\n--- HOW MANY DISTINCT TIMESTAMP_1 VALUES PER TIMESTAMP_2? ---")

unique_counts = df.groupby("timestamp_2")["timestamp_1"].nunique()

print(unique_counts.describe())

print("\n--- TIMESTAMP_2 VALUES PER MICROSERVICE ---")

times_per_service = df.groupby("microservice_id")["timestamp_2"].nunique()

print(times_per_service.describe())

print("\n--- SAMPLE ROWS WITH THE SAME MICROSERVICE ---")

service_id = df["microservice_id"].value_counts().index[0]

print(
    df[df["microservice_id"] == service_id][
        ["timestamp_1", "timestamp_2", "microservice_id",
         "container_id", "replica_count", "microservice_time", "call_rate"]
    ].head(10).to_string(index=False)
)

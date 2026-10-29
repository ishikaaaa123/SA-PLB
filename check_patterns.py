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

print("\n--- TIMESTAMP CHECK ---")
for col in ["timestamp_1", "timestamp_2"]:
    print(f"\n{col}")
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Unique values:", df[col].nunique())
    print("Rows in original order sorted?", df[col].is_monotonic_increasing)

print("\n--- DUPLICATE ROWS ---")
print("Exact duplicate rows:", df.duplicated().sum())
print("Duplicate rows as percentage:",
      df.duplicated().mean() * 100)
print("\n--- SERVICE AND CONTAINER RELATIONSHIP ---")
print("Unique microservices:", df["microservice_id"].nunique())
print("Unique containers:", df["container_id"].nunique())

containers_per_service = df.groupby("microservice_id")[
    "container_id"
].nunique()

print("Containers per service — minimum:",
      containers_per_service.min())
print("Containers per service — median:",
      containers_per_service.median())
print("Containers per service — maximum:",
      containers_per_service.max())

print("\n--- NUMERICAL EXTREMES ---")
print(df[["replica_count", "microservice_time", "call_rate"]]
      .quantile([0, 0.5, 0.95, 0.99, 1]).to_string())

print("\n--- FIRST 10 ROWS OF TIMESTAMPS ---")
print(df[["timestamp_1", "timestamp_2"]].head(10).to_string(index=False))

print("\n--- CONTAINER TIMESTAMP COVERAGE ---")

timestamps_per_container = (
    df.groupby("container_id")["timestamp_2"].nunique()
)

print("Containers appearing at only one timestamp:",
      (timestamps_per_container == 1).sum())

print("Containers appearing at multiple timestamps:",
      (timestamps_per_container > 1).sum())

print("Median timestamps per container:",
      timestamps_per_container.median())

print("Maximum timestamps per container:",
      timestamps_per_container.max())


print("\n--- MICROservice TIME VARIATION ---")

service_time_stats = (
    df.groupby("microservice_id")["microservice_time"]
    .agg(["count", "mean", "std", "min", "max"])
)

print("Services with multiple observations:",
      (service_time_stats["count"] > 1).sum())

print("Services with only one observation:",
      (service_time_stats["count"] == 1).sum())

print("\nServices with the most observations:")
print(
    service_time_stats
    .sort_values("count", ascending=False)
    .head(5)
    .to_string()
)

print("\n--- CORRELATION CHECK ---")

print(
    df[["replica_count", "microservice_time", "call_rate"]]
    .corr()
    .round(3)
    .to_string()
)


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

print("--- FIRST 20 DISTINCT VALUES OF TIMESTAMP_2 ---")
print(sorted(df["timestamp_2"].unique())[:20])

print("\n--- MOST FREQUENT TIMESTAMP_2 VALUES ---")
print(df["timestamp_2"].value_counts().head(10))

print("\n--- FIRST 15 ROWS SORTED BY TIMESTAMP_2 ---")
print(
    df.sort_values("timestamp_2")[
        ["timestamp_1", "timestamp_2", "microservice_id"]
    ].head(15).to_string(index=False)
)

print("\n--- TIMESTAMP_2 DIFFERENCES ---")
times = sorted(df["timestamp_2"].unique())
differences = pd.Series(times).diff().dropna()

print("Most common differences:")
print(differences.value_counts().head(10))

print("\n--- DUPLICATE ROWS ---")
print("Exact duplicate rows:", df.duplicated().sum())


print("\n--- CHECK TIMESTAMP_2 INTERVALS ---")

times = sorted(df["timestamp_2"].unique())

print("Number of distinct timestamps:", len(times))
print("First 10 timestamps:", times[:10])
print("Last 10 timestamps:", times[-10:])

print("\n--- CHECK WHETHER TIMESTAMP_2 IS A REGULAR GRID ---")

differences = pd.Series(times).diff().dropna()

print("Unique differences:", sorted(differences.unique()))
print("Median difference:", differences.median())

print("\n--- CHECK ROW COUNTS PER TIMESTAMP_2 ---")

rows_per_time = df.groupby("timestamp_2").size()

print("Minimum rows:", rows_per_time.min())
print("Median rows:", rows_per_time.median())
print("Maximum rows:", rows_per_time.max())


print("\n--- FIND LARGE GAPS ---")

times = sorted(df["timestamp_2"].unique())

for previous, current in zip(times, times[1:]):
    gap = current - previous

    if gap > 60000:
        print("Previous timestamp:", previous)
        print("Next timestamp:", current)
        print("Gap:", gap)
        print("Number of missing regular intervals:", gap // 60000 - 1)


print("\n--- CHECK TIMESTAMP_1 WITHIN EACH TIMESTAMP_2 ---")

sample_times = [0, 60000, 1740000, 3600000, 25140000]

for t in sample_times:
    group = df[df["timestamp_2"] == t]

    if len(group) > 0:
        print(f"\ntimestamp_2 = {t}")
        print("Number of rows:", len(group))
        print(
            "timestamp_1 min:",
            group["timestamp_1"].min()
        )
        print(
            "timestamp_1 median:",
            group["timestamp_1"].median()
        )
        print(
            "timestamp_1 max:",
            group["timestamp_1"].max()
        )

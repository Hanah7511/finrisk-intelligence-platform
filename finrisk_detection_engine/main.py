from src.ingestion.sql_ingestion import (
    SqlIngestionError,
    load_finrisk_modeling_dataset,
)


def main():
    try:
        df = load_finrisk_modeling_dataset(limit=100)

        print("\nDataset loaded successfully.")
        print(f"Shape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        metadata = {
            "rows": len(df),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "dtypes": df.dtypes.astype(str).to_dict(),
        }
        print("\nMetadata Snapshot:")
        print(metadata)

    except SqlIngestionError as e:
        print(f"\nSQL ingestion failed: {e}")

    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
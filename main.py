from pathlib import Path
import pandas as pd


def merge_excel_files(input_dir: str, output_file: str) -> None:
    """Merge Excel files from a directory into one output file."""
    source_dir = Path(input_dir)
    output_path = Path(output_file)

    if not source_dir.is_dir():
        raise FileNotFoundError(
            f"Input directory not found: {source_dir}"
        )

    excel_files = [
        file for file in source_dir.glob("*.xlsx")
        if file.resolve() != output_path.resolve()
        and not file.name.startswith("~$")
    ]

    if not excel_files:
        raise FileNotFoundError(
            f"No .xlsx files found in {source_dir}"
        )

    dataframes = []

    for file in sorted(excel_files):
        df = pd.read_excel(file)
        df["source_file"] = file.name
        dataframes.append(df)

    merged_df = pd.concat(dataframes, ignore_index=True)
    merged_df = merged_df.drop_duplicates()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    merged_df.to_excel(output_path, index=False)

    print(f"Files processed: {len(excel_files)}")
    print(f"Rows in final report: {len(merged_df)}")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    merge_excel_files("input", "output/merged_report.xlsx")


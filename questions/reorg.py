import os
import shutil

# Root directory (change this to your folder path)
ROOT_DIR = "."

# Map month letter to full name
MONTH_MAP = {
    "m": "march",
    # add more if needed later
}

for year in os.listdir(ROOT_DIR):
    year_path = os.path.join(ROOT_DIR, year)

    if not os.path.isdir(year_path):
        continue

    for file in os.listdir(year_path):
        if not file.endswith(".pdf"):
            continue

        old_file_path = os.path.join(year_path, file)

        try:
            # Example: 0625_m24_qp_22.pdf
            parts = file.split("_")

            # Extract month + day (e.g., m24)
            month_day = parts[1]  # 'm24'
            month_letter = month_day[0]  # 'm'
            day = month_day[1:]  # '24'

            month_name = MONTH_MAP.get(month_letter.lower())

            if not month_name:
                print(f"Skipping unknown month format: {file}")
                continue

            # Create new directory path
            new_dir = os.path.join(year_path, month_name, day)
            os.makedirs(new_dir, exist_ok=True)

            # New file path
            new_file_path = os.path.join(new_dir, "paper.pdf")

            # Move and rename
            shutil.move(old_file_path, new_file_path)

            print(f"Moved: {file} -> {new_file_path}")

        except Exception as e:
            print(f"Error processing {file}: {e}")

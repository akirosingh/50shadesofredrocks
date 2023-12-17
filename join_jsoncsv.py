import pandas as pd
import json
import os

# Directory containing JSON files
json_dir = f"C:\\Users\\17023\\Desktop\\1-Projects\\50shadesofredrocks\\sunlight\\"

# Read the original CSV
original_csv = pd.read_csv(r"C:\Users\17023\Desktop\1-Projects\50shadesofredrocks\redrockscrags.csv")

# Initialize merged_data with day columns
day_columns = [f'Day_{i+1}' for i in range(365)]
merged_data = original_csv.copy()
for col in day_columns:
    merged_data[col] = pd.NA  # or use 0 or another default value

# Process each JSON file
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        with open(os.path.join(json_dir, filename), 'r') as file:
            data = json.load(file)
            area_name = filename.replace('.json', '')

            # Create a dict with day data
            day_data = {f'Day_{i+1}': data['minutesOfDirectSunPerDay'][i] for i in range(365)}

            # Find the row index for this area in merged_data
            row_index = merged_data[merged_data['areas'] == area_name].index
            if not row_index.empty:
                # Update the row with day data
                merged_data.loc[row_index, day_columns] = list(day_data.values())

# Export to a new wide-format CSV
merged_data.to_csv(r"C:\Users\17023\Desktop\1-Projects\50shadesofredrocks\redrockscrags_appended.csv", index=False)

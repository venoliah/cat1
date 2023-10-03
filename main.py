import pandas as pd
import json
import os

# Question 1
folder_path = 'data'
dfs = []

# Read all JSON Lines files into a list of DataFrames
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    df = pd.read_json(file_path, orient='records', lines=True)
    dfs.append(df)
print(f'{len(dfs)} files have been converted')

# Iterate over language files
for index, language_file in enumerate(os.listdir(folder_path)):
    language_id = language_file.split('.')[0]  # Extract language ID from the filename

    # Construct test data for each language pair
    testdata = {
        'id': dfs[index]['id'],
        'en-utt': dfs[index]['utt'],
        f'{language_id[:2]}-utt': dfs[index]['utt'],
        'en-annot_utt': dfs[index]['annot_utt'],
        f'{language_id[:2]}-annot_utt': dfs[index]['annot_utt']
    }

    dframe = pd.DataFrame(testdata)

    # Write to Excel file with language ID in the filename
    dframe.to_excel(f"excel/en-{language_id[:2]}.xlsx", index=False)

print("Excel files generated successfully.")


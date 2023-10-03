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

# Question 2 (a)
en_train = dfs[10][dfs[10]['partition']=='train']
en_train.to_json('json/en_train.jsonl',orient='records',lines=True)

en_test = dfs[10][dfs[10]['partition']=='test']
en_test.to_json('json/en_test.jsonl',orient='records',lines=True)

en_dev = dfs[10][dfs[10]['partition']=='dev']
en_dev.to_json('json/en_dev.jsonl',orient='records',lines=True)


de_train = dfs[8][dfs[8]['partition']=='train']
de_train.to_json('json/de_train.jsonl',orient='records',lines=True)


de_test = dfs[8][dfs[8]['partition']=='test']
de_test.to_json('json/de_test.jsonl',orient='records',lines=True)

de_dev = dfs[8][dfs[8]['partition']=='dev']
de_dev.to_json('json/de_dev.jsonl',orient='records',lines=True)


sw_train = dfs[42][dfs[42]['partition']=='train']
sw_train.to_json('json/sw_train.jsonl',orient='records',lines=True)



sw_test = dfs[42][dfs[42]['partition']=='test']
sw_test.to_json('json/sw_test.jsonl',orient='records',lines=True)

sw_dev = dfs[42][dfs[42]['partition']=='dev']
sw_dev.to_json('json/sw_dev.jsonl',orient='records',lines=True)
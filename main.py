import pandas as pd
import json
import os

"""Question 1"""
folder_path = 'data'
dfs = []

"""Read all JSON Lines files into a list of DataFrames"""
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    df = pd.read_json(file_path, orient='records', lines=True)
    dfs.append(df)
print(f'{len(dfs)} files have been converted')

"""Iterate over language files"""
def generate_excel_files(folder_path, dfs):
    for index, language_file in enumerate(os.listdir(folder_path)):
        language_id = language_file.split('.')[0]  # Extract language ID from the filename

        """Construct test data for each language pair"""
        testdata = {
            'id': dfs[index]['id'],
            'en-utt': dfs[index]['utt'],
            f'{language_id[:2]}-utt': dfs[index]['utt'],
            'en-annot_utt': dfs[index]['annot_utt'],
            f'{language_id[:2]}-annot_utt': dfs[index]['annot_utt']
        }

        dframe = pd.DataFrame(testdata)

        """Write to Excel file with language ID in the filename"""
        dframe.to_excel(f"excel/en-{language_id[:2]}.xlsx", index=False)

    print("Excel files generated successfully.")


"""Question 2"""


def read_json_files(folder_path):
    dfs = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_json(file_path, orient='records', lines=True)
        dfs.append(df)
    print(f'{len(dfs)} files have been converted')
    return dfs


def save_partition_to_json(df, language_code, partition_name):
    file_path = f'json/{language_code}_{partition_name}.jsonl'
    df.to_json(file_path, orient='records', lines=True)
    print(f'{file_path} generated successfully')


def main():
    folder_path = 'data'
    dfs = read_json_files(folder_path)

    """Define language indices"""
    language_indices = {
        'en': 10,
        'de': 8,
        'sw': 42
    }

    partitions = ['train', 'test', 'dev']
    en_train = dfs[language_indices['en']][dfs[language_indices['en']]['partition'] == 'train']
    de_train = dfs[language_indices['de']][dfs[language_indices['de']]['partition'] == 'train']
    sw_train = dfs[language_indices['sw']][dfs[language_indices['sw']]['partition'] == 'train']

    for language_code, index in language_indices.items():
        for partition_name in partitions:
            partition_df = dfs[index][dfs[index]['partition'] == partition_name]
            save_partition_to_json(partition_df, language_code, partition_name)

    return en_train, de_train, sw_train


if __name__ == "__main__":
    en_train, de_train, sw_train = main()

"""Question 3"""
test_data = {
    'id': dfs[10]['id'],
    'en-utt': en_train['utt'],
    'de-utt': de_train['utt'],
    'sw-utt': sw_train['utt']

}

train_translations = pd.DataFrame(test_data)

train_translations.to_json('json/traintranslations.json', orient='records')

with open('json/traintranslations.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print(json.dumps(loaded_data, indent=10))

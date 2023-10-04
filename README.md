# MassiveDataset

This Python-based project focuses on processing and analyzing a vast dataset sourced from Amazon.

## Project Overview

#### Pandas

-Utilizes Pandas to efficiently convert extensive JSONL files into dataframes and organizes them within a list.

-Utilizes these dataframes for merging, data filtering, and subsequent storage of the filtered data into Excel files.

#### Openxyl

-Utilizes Openxyl to effectively manage and store the filtered data in Excel files.

## Project Workflow

The project begins by converting the JSONL dataset into dataframes, storing them in a list, and filtering out unnecessary data. The filtered data is then stored in Excel files. This filtered data is further categorized into 'train,' 'test,' and 'dev' using the 'partition' column. Subsequently, the 'train' category is used for English-to-other-language translation, with the results being stored in a JSON file. Then we pretty print the json file structure.

## Prerequisites for a fully running project
In order for one to have a fully running project, one needs to have the following:

*Python installed in PC*

One can download and install it from Python's official website link: [Python](https://www.python.org/downloads/)

*Libraries*
- Pandas

   To install this library, run the following command
  
  ``` 
  pip install pandas
  ```


- Openpyxl

   To install this library, run the following command
  
   ```
  pip install openpyxl
   ```

  
  In python by default
- Json

  In python by default
- OS
  
## Environment Setup
  
After installing python, create an environment. The steps are as follows:

1. *Environment Setup:*

      Set up a Python3 development environment. Ensure that Python3 is installed on your system.

2. *Dependency Installation:*

     Install all relevant dependencies required for the project. These dependencies may vary depending on your specific use case, so ensure you install the necessary packages for your environment.

5. *Project Structure:*

      Create a Python3 project with a standard structure suitable for your preferred IDE, such as PyCharm.

## References
   The completion of this project involved extensive research from articles, related works, and YouTube tutorials to ensure completeness and accuracy.

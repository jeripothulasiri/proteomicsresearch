import pandas as pd


# Convert the CSV string into a pandas DataFrame
df = pd.read_csv('Datasets/pdb_data_seq.csv')

# Count occurrences of each macromolecule type
counts = df['macromoleculeType'].value_counts()

# Display the result
print(counts)

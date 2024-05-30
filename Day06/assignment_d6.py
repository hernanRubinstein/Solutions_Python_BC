import sys
import pandas as pd
import numpy as np 

def normalize_expression(filename):
    print(f"Processing file: {filename}")
    try:
        umi_matrix = pd.read_csv(filename, index_col=0) # Read the CSV file into a DataFrame
        
    except Exception as error:
        print(f"An error occurred while reading the file: {error}")
        return None
    
    # Sum of each column
    col_sums = umi_matrix.sum()
    
    # Divide each element by the sum of its column
    normalized_umi_matrix = umi_matrix.div(col_sums)
    return normalized_umi_matrix

def main():
    mat_1 = normalize_expression(sys.argv[1]) 
    mat_2 = normalize_expression(sys.argv[2])

    fold_mat = np.log2(mat_1 + 1e-4) - np.log2(mat_2 + 1e-4)

    print(f"\nFOLD CHANGE MATRIX: {fold_mat.head(5)}")

    for col in fold_mat.columns:
        col_vector = fold_mat[col]
        max_fold_gene = col_vector.abs().idxmax()
        print(f"\nHighest fold change gene in column {col}: {max_fold_gene} with fold change {col_vector[max_fold_gene]}")

main()
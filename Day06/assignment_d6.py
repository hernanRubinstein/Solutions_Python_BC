import sys
import pandas as pd
import numpy as np

def normalize_expression(filename):
    # print(f"Processing file: {filename}")
    try:
        umi_matrix = pd.read_csv(filename, index_col=0)  # Read the CSV file into a DataFrame
    except Exception as error:
        print(f"An error occurred while reading the file: {error}")
        return None
    
    # Sum of each column
    col_sums = umi_matrix.sum()
    
    # Divide each element by the sum of its column
    normalized_umi_matrix = umi_matrix.div(col_sums)
    return normalized_umi_matrix

def calculate_fold_change(m1, m2):
    mat_1 = normalize_expression(m1) 
    mat_2 = normalize_expression(m2)

    if mat_1 is None or mat_2 is None:
        print("One or both of the matrices couldn't be processed.")
        return
    
    fold_mat = np.log2(mat_1 + 1e-4) - np.log2(mat_2 + 1e-4)
    
    max_fold_genes = {}
    for col in fold_mat.columns:
        col_vector = fold_mat[col]
        max_fold_gene = col_vector.abs().idxmax()
        max_fold_genes[col] = (max_fold_gene, col_vector[max_fold_gene])
    
    return max_fold_genes

def main():
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} <filename1> <filename2>")

    fold_changes = calculate_fold_change(sys.argv[1], sys.argv[2])
    
    if fold_changes:
        for col, (gene, fold_change) in fold_changes.items():
            print(f"Highest fold change gene in {col}: {gene} with fold change {round(fold_change,2)}")

if __name__ == "__main__":
    main()

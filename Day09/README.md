# DNA Sequence Analysis Script

This Python script analyzes DNA sequences to find the longest duplicated subsequences and SMAD1/5/9 binding motifs (SMAD Binding Elements, SBE). It takes a DNA sequence file in FASTA or GenBank format as input and provides options to search for these specific patterns.

## Key Functions

### `find_longest_duplicate(sequence: str) -> str`

- **Description**: Finds the longest duplicated subsequence in a given DNA sequence.
- **Parameters**:
  - `sequence`: A string representing the DNA sequence to search for duplications.
- **Returns**: A string of the longest duplicated subsequence found in the DNA sequence.

### `find_sbe(sequence: str) -> List[str]`

- **Description**: Identifies the SMAD1/5/9 binding motifs in a given DNA sequence.
- **Parameters**:
  - `sequence`: A string representing the DNA sequence to search for SMAD binding motifs.
- **Returns**: A list of found SMAD binding motifs.

## Main Functionality

The main function uses the `argparse` library to handle command-line arguments. It provides the following options:

- `--path`: Path to the input DNA sequence file (FASTA or GenBank format). This argument is required.
- `--duplicate` or `-dp`: Option to search for the longest duplicated sequence in the DNA sequence.
- `--sbe`: Option to search the DNA sequence for SMAD1/5/9 binding motifs.

The script validates the input file format and processes each sequence record in the file to perform the requested analyses.

### Usage

```python
python Ex_09.py --path <path_to_file> [--duplicate] [--sbe]
```

- `<path_to_file>`: Replace with the path to your FASTA or GenBank file.
- `--duplicate` or `-dp`: Include this flag to search for the longest duplicated subsequence.
- `--sbe`: Include this flag to search for SMAD1/5/9 binding motifs.

### Example

```python
python Ex_09.py --path Smad7_gene.fasta --duplicate --sbe
```

- This command will analyze the DNA sequences in Smad7_gene.fasta, finding both the longest duplicated subsequences and the SMAD1/5/9 binding motifs.

### Requirements

The script requires the following Python packages, which are listed in the requirements.txt file:

`argparse`: For parsing command-line arguments.
`re`: For regular expression operations.
`typing`: For type hinting.
`Bio` from the biopython library: For reading DNA sequence files.

To install the required dependencies, run:

```python
pip install -r requirements.txt
```

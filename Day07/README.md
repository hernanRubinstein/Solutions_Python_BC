# Overview

This script searches the NCBI nucleotide database for a given term, fetches a specified number of records, and logs the search details to a CSV file. It is designed to automate the retrieval of genetic data from NCBI and maintain a log of all searches.

## Prerequisites

`Biopython library`

```python
pip install biopython
```

## Usage

To run the script, use the following command in the terminal:

```python
python Ex_07.py TERM NUMBER
```
  
* `TERM`: The search term for the NCBI nucleotide database.
* `NUMBER`: The maximum number of records to fetch.

## Example

```python
python Ex_07.py "Homo sapiens"  5
```

## Output

The script will download the specified number of records (or fewer, if there aren't enough available) and save them as .gb files in the current directory. A log entry will be added to search_log.csv with the following columns:

* `date`: The date and time of the search.
* `term`: The search term used.
* `max`: The maximum number of records requested.
* `total`: The total number of records available for the search term.

## Script Details

### Functions

> `fetch_ncbi_records(term, number)` function:

* Searches the NCBI nucleotide database for the given term.
* Fetches up to the specified number of records.
* Saves each record to a .gb file.
* Returns a list of file names and the total number of records available.

> `log_search_details(date, term, number, total)` function:

* Logs the search details to `search_log.csv`.

### Main Function

> `main()` function:

1. Parses command-line arguments to get the search term and number of records.
2. Fetches the records and logs the search details.
3. Handles any exceptions that occur during execution.

import argparse
import re
from typing import List
from Bio import SeqIO

def find_longest_duplicate(sequence: str) -> str:
    """
    Find the longest duplicated subsequence in a given DNA sequence.

    :param sequence: DNA sequence to search for duplications.
    :return: Longest duplicated subsequence.
    """
    length = 1
    result = ''
    while True:
        regex = re.compile(rf'([GATC]{{{length}}}).*\1')
        match = regex.search(sequence)
        if match:
            result = match.group(1)
            length += 1
        else:
            break
    return result


def find_sbe(sequence: str) -> List[str]:
    """
    Find the SMAD1/5/9 binding motifs in a given DNA sequence.

    :param sequence: DNA sequence to search for SMAD binding motifs.
    :return: List of found SMAD binding motifs.
    """
    smad_binding_motif = [r'GTCTAGAC']
    sbe = []
    for pattern in smad_binding_motif:
        matches = re.findall(pattern, sequence)
        for match in matches:
            if match not in sbe:
                sbe.append(match)
    return sbe


def main():
    parser = argparse.ArgumentParser(description="Analyze DNA sequences to find duplications and microsatellites")
    parser.add_argument('--path', help="Path to FASTA/GenBank file", required=True)
    parser.add_argument('--duplicate', '-dp', action="store_true", help="Search for the longest duplicated sequence")
    parser.add_argument('--sbe', action="store_true", help="Search the sequence for SMAD1/5/9 binding motif")
    args = parser.parse_args()

    if not args.duplicate and not args.sbe:
        parser.error("Please provide at least one request: --duplicate or --sbe")

    file_format = None
    if args.path.endswith((".gb", ".gbk")):
        file_format = "genbank"
    elif args.path.endswith((".fasta", ".fa")):
        file_format = "fasta"
    else:
        raise ValueError("Unsupported file format. Please provide a FASTA or GenBank file.")

    for record in SeqIO.parse(args.path, file_format):
        sequence = str(record.seq)
        if args.duplicate:
            longest_dup = find_longest_duplicate(sequence)
            print(f"Longest duplicate subsequence: {longest_dup}")

        if args.sbe:
            sbe = find_sbe(sequence)
            print(f"SMAD1/5/9 binding motifs found: {sbe}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import utils
import codecs
import sys
import os
import csv

def read_input_line(line):
    return line.rstrip('\n').rstrip('\r')


def parse_chain_file(file_path):
    file = codecs.open(file_path, 'r', 'utf-8')
    lines = [read_input_line(line) for line in file]

    chains = {}
    last_pdb_code = ''
    last_chain = ''

    for line in lines:
        if line.startswith('>'):
            pdb_code = line[1:-2]
            chain = line[-1:]

            if pdb_code not in chains:
                chains[pdb_code] = {}

            chains[pdb_code][chain] = ''
            last_pdb_code = pdb_code
            last_chain = chain
        else:
            if line:
                chains[last_pdb_code][last_chain] += line

    return chains


def main():
    args = sys.argv[1:]
    fastas_chains = parse_chain_file(args[0])
    ir_chains = parse_chain_file(args[1])

    with open('green_statistics.csv', 'w') as csvfile:
        fieldnames = [
            'PDB_CODE',
            'CHAINAME',
            'CHAIN_LENGTH_FASTAS',
            'CHAIN_LENGTH_IR',
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for pdb_code in fastas_chains:
            for chain in fastas_chains[pdb_code]:
                length_fastas = len(fastas_chains[pdb_code][chain])
                length_ir = len(ir_chains[pdb_code][chain])

                writer.writerow({
                    'PDB_CODE': pdb_code,
                    'CHAINAME': chain,
                    'CHAIN_LENGTH_FASTAS': length_fastas,
                    'CHAIN_LENGTH_IR': length_ir,
                })


if __name__ == "__main__":
    main()

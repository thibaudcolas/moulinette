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

        dynamic_fieldnames = [
            'NB_{code}_FASTAS',
            'NB_{code}_IR',
            '%_{code}_CHAIN',
            '%_{code}_IR_VS_CHAIN',
            '%_{code}_IR_VS_IR',
            '%_{code}_IR_VS_CHAIN_WEIGHTED',
        ]

        for code in utils.standard_one_letter_codes.values():
            if code:
                for field in dynamic_fieldnames:
                    fieldnames.append(field.format(code=code))

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for pdb_code in fastas_chains:
            for chain in fastas_chains[pdb_code]:
                sequence = fastas_chains[pdb_code][chain]
                interface_residues = ir_chains[pdb_code][chain]

                fields = {
                    # 1. PDB code of the protein.
                    'PDB_CODE': pdb_code,
                    # 2. One-letter code of the chain.
                    'CHAINAME': chain,
                    # 3. Length of sequence in fastas file.
                    'CHAIN_LENGTH_FASTAS': len(sequence),
                    # 4. Length of interface residues in IR file.
                    'CHAIN_LENGTH_IR': len(interface_residues),
                }

                for code in utils.standard_one_letter_codes.values():
                    if code:
                        dynamic_fields = {}

                        # Colonne 5: Nombre de A dans fastas
                        # 5. Number of {code} in sequence.
                        dynamic_fields['NB_{code}_FASTAS'] = float(sequence.count(code))
                        # Colonne 6: Nombre de A dans IR
                        # 6. Number of {code} in interface residues.
                        dynamic_fields['NB_{code}_IR'] = float(interface_residues.count(code))

                        # Colonne 7: Ratio colonne 5 / colonne 3
                        # 7. Proportion of {code} in sequence to sequence length.
                        dynamic_fields['%_{code}_CHAIN'] = 100 * dynamic_fields['NB_{code}_FASTAS'] / fields['CHAIN_LENGTH_FASTAS']
                        # Colonne 8: Ratio colonne 6 / colonne 3
                        # 8. Proportion of {code} in interface residues to sequence length.
                        dynamic_fields['%_{code}_IR_VS_CHAIN'] = 100 * dynamic_fields['NB_{code}_IR'] / fields['CHAIN_LENGTH_FASTAS']
                        # Colonne 9: Ratio colonne 6 / colonne 4
                        # 9. Proportion of {code} in interface residues to interface residues length.
                        dynamic_fields['%_{code}_IR_VS_IR'] = 100 * dynamic_fields['NB_{code}_IR'] / fields['CHAIN_LENGTH_IR']
                        # Colonne 10: Ratio colonne 6 / colonne 5
                        # 10. Weighted proportion of {code} in interface residues to number of {code} in sequence.
                        dynamic_fields['%_{code}_IR_VS_CHAIN_WEIGHTED'] = 100 * dynamic_fields['NB_{code}_IR'] / dynamic_fields['NB_{code}_FASTAS']

                        for field in dynamic_fields:
                            fields[field.format(code=code)] = dynamic_fields[field]

                writer.writerow(fields)


if __name__ == "__main__":
    main()

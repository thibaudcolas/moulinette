#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymol import cmd
from lib import interfaceResidues
from lib import utils
import itertools
import codecs

PDB_CODES_FILE = 'pdb-codes.txt'
STORE_DIR = 'store'


def load_pdb_files(proteins):
    for i, protein in enumerate(proteins):
        cmd.fetch(protein['code'])
        utils.print_progress(i + 1, len(proteins), prefix='Fetch ' + protein['code'] + ':', barLength=50)


def structure_data(proteins):
    data = {}
    for protein in proteins:
        code = protein['code']
        data[code] = {
            'name': protein['name'],
            'interfaces': {},
        }
        chains = cmd.get_chains(code)

        for (cA, cB) in itertools.combinations(chains, 2):
            interface = cA + cB
            data[code]['interfaces'][interface] = {
                'residues': []
            }
    return data


def get_residues(proteins):
    data = structure_data(proteins)

    for protein in proteins:
        code = protein['code']
        cmd.delete(code)

    for i, code in enumerate(data):
        cmd.load(code + '.pdb')

        for interface in data[code]['interfaces']:
            cA = 'c. ' + interface[0]
            cB = 'c. ' + interface[1]
            selName = code + '_' + interface

            interfaceResidues.interfaceResidues(code, cA=cA, cB=cB, selName=selName)

            # There probably is a simpler way to do this using idiomatic Python,
            # but I don't know enough PyMOL to understand what is going on here.
            selection = selName + ' & n. ca'
            expression = 'residues.append({ "chain": chain, "resi": resi, "resn": resn })'
            cmd.iterate(selection, expression, space=data[code]['interfaces'][interface])

        cmd.delete(code)
        utils.print_progress(i + 1, len(data), prefix='Calc ' + code + ':', barLength=50)

    return data


def save_to_files(data):
    utils.save_json(STORE_DIR + '/' + 'data.json', data)

    for code in data:
        for interface in data[code]['interfaces']:
            file_name = code + '_' + interface
            file = codecs.open(STORE_DIR + '/' + file_name + '.txt', 'w', 'utf-8')
            lines = [(r['chain'] + ' ' + r['resi'] + ' ' + r['resn'] + '\n') for r in data[code]['interfaces'][interface]['residues']]
            file.write(''.join(lines))
            file.close()


def main():
    proteins = utils.read_input_file(PDB_CODES_FILE)

    load_pdb_files(proteins)

    data = get_residues(proteins)

    save_to_files(data)


if __name__ == "__main__":
    main()

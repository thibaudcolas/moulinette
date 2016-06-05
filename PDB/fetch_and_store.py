#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymol import cmd
from lib import interfaceResidues
from lib import utils
import itertools
import json

PDB_CODES_FILE = 'pdb-codes.txt'
STORE_DIR = 'store'


def read_pdb_codes(file_path):
    return [line.rstrip('\n') for line in open(file_path)]


def load_pdb_files(pdb_codes):
    for i, code in enumerate(pdb_codes):
        cmd.fetch(code)
        utils.print_progress(i + 1, len(pdb_codes), prefix='Fetch ' + code + ':', barLength=50)


def structure_data(pdb_codes):
    data = {}
    for code in pdb_codes:
        data[code] = {}
        chains = cmd.get_chains(code)

        for (cA, cB) in itertools.combinations(chains, 2):
            interface = cA + cB
            data[code][interface] = {
                'residues': []
            }
    return data


def get_residues(pdb_codes):
    data = structure_data(pdb_codes)

    for code in pdb_codes:
        cmd.delete(code)

    for i, code in enumerate(data):
        cmd.load(code + '.pdb')

        for interface in data[code]:
            cA = 'c. ' + interface[0]
            cB = 'c. ' + interface[1]
            selName = code + '_' + interface

            interfaceResidues.interfaceResidues(code, cA=cA, cB=cB, selName=selName)

            # There probably is a simpler way to do this using idiomatic Python,
            # but I don't know enough PyMOL to understand what is going on here.
            selection = selName + ' & n. ca'
            expression = 'residues.append({ "chain": chain, "resi": resi, "resn": resn })'
            cmd.iterate(selection, expression, space=data[code][interface])

        cmd.delete(code)
        utils.print_progress(i + 1, len(data), prefix='Calc ' + code + ':', barLength=50)

    return data


def save_to_files(data):
    dump = open(STORE_DIR + '/' + 'data.json', 'w')
    dump.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    dump.close()

    for code in data:
        for interface in data[code]:
            file_name = code + '_' + interface
            file = open(STORE_DIR + '/' + file_name + '.txt', 'w')
            lines = [(r['chain'] + ' ' + r['resi'] + ' ' + r['resn'] + '\n') for r in data[code][interface]['residues']]
            file.write(''.join(lines))
            file.close()


def run():
    pdb_codes = read_pdb_codes(PDB_CODES_FILE)

    load_pdb_files(pdb_codes)

    data = get_residues(pdb_codes)

    save_to_files(data)


run()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from lib import utils

STORE_DIR = 'store'
DATA_FILE = 'data.json'


def generate_output(data):
    output = []

    for code in data:
        for interface in data[code]:
            residues = data[code][interface]['residues']

            for chain in interface:
                try:
                    sequence = [utils.aminoacid_codes[r['resn']] for r in residues if r['chain'] == chain]
                except KeyError:
                    sys.exit('Error: ' + r['resn'] + ' amino acid code not found. In ' + code)

                output.append((
                    utils.get_clustal_omega_header(code, interface, chain),
                    ''.join(sequence)
                ))

    return output


def run():
    data = utils.load_json(STORE_DIR + '/' + DATA_FILE)
    output = generate_output(data)

    output.sort(key=lambda pair: len(pair[1]), reverse=True)

    for (header, sequence) in output:
        print header
        print sequence

run()

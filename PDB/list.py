#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from lib import utils

STORE_DIR = 'store'
DATA_FILE = 'data.json'


def generate_output(data):
    '''
    Generate output in Clustal Omega format for our data structure.
    The clustal omega format has two lines: a (unique) header to identify
    the sequence, and the sequence itself.
    The sequence is a succession of one-letter amino acid codes.
    '''
    output = []

    for code in data:
        for interface in data[code]['interfaces']:
            residues = data[code]['interfaces'][interface]['residues']

            for chain in interface:
                try:
                    sequence = [utils.aminoacid_codes[r['resn']] for r in residues if r['chain'] == chain]
                except KeyError:
                    sys.exit('Error: ' + r['resn'] + ' amino acid code not found. In ' + code)

                output.append((
                    utils.get_clustal_omega_header({
                        'code': code,
                        'name': data[code]['name'].replace(' ', ''),
                        'interface': interface,
                        'chain': chain,
                    }),
                    ''.join(sequence)
                ))

    return output


def run():
    data = utils.load_json(STORE_DIR + '/' + DATA_FILE)
    output = generate_output(data)

    output.sort(key=lambda pair: len(pair[1]), reverse=True)

    for (header, sequence) in output:
        print header.encode('utf-8')
        print sequence.encode('utf-8')

run()

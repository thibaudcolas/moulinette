# -*- coding: UTF-8 -*-

import json
from lib import utils

STORE_DIR = 'store'
DATA_FILE = 'data.json'


def load_data(file_path):
    return json.loads(open(file_path).read())


def generate_output(data):
    output = []

    for code in data:
        for interface in data[code]:
            residues = data[code][interface]['residues']

            for chain in interface:
                sequence = [utils.aminoacid_codes[r['resn']] for r in residues if r['chain'] == chain]

                output.append((
                    utils.get_clustal_omega_header(code, interface, chain),
                    ''.join(sequence)
                ))

    return output


def sort_by_sequence_length(self):
    return len(self[1])


def run():
    data = load_data(STORE_DIR + '/' + DATA_FILE)
    output = generate_output(data)

    output.sort(key=sort_by_sequence_length, reverse=True)

    for (header, sequence) in output:
        print header
        print sequence

run()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
                sequences = []

                for i, r in enumerate(residues):
                    # TODO Save as number upfront in JSON
                    resi = int(r['resi'])
                    if r['chain'] == chain:
                        prev_i = len(sequences) - 1
                        prev_seq = sequences[prev_i] if prev_i > 0 else []
                        # print i, prev_i, prev_seq, resi

                        # If the last resi of the sequence is current resi - 1...
                        if prev_seq and int(prev_seq[len(prev_seq) - 1]['resi']) == resi - 1:
                            prev_seq.append(r)
                        else:
                            sequences.append([r])

                order = 0
                for seq in sequences:
                    if len(seq) > 1:
                        output.append((
                            utils.get_clustal_omega_header({
                                'code': code,
                                'name': data[code]['name'].replace(' ', ''),
                                'interface': interface,
                                'chain': chain,
                                'suffix': '_' + str(order),
                            }),
                            ''.join([utils.get_one_letter_code(r['resn'], code) for r in seq])
                        ))
                        order += 1

    return output


def main():
    data = utils.load_json(STORE_DIR + '/' + DATA_FILE)
    output = generate_output(data)

    output.sort(key=lambda pair: len(pair[1]), reverse=True)

    for (header, sequence) in output:
        print header.encode('utf-8')
        print sequence.encode('utf-8')


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import utils


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
                sequence = [utils.get_one_letter_code(r['resn'], code) for r in residues if r['chain'] == chain]

                output.append((
                    utils.get_clustal_omega_header({
                        'code': code,
                        'name': data[code]['name'].replace(' ', ''),
                        'interface': interface,
                        'chain': chain,
                        'suffix': '',
                    }),
                    ''.join(sequence)
                ))

    return output


def main():
    data = utils.load_json(utils.get_json_path(__file__))
    output = generate_output(data)

    output.sort(key=lambda pair: len(pair[1]), reverse=True)

    for (header, sequence) in output:
        print header.encode('utf-8')
        print sequence.encode('utf-8')


if __name__ == "__main__":
    main()

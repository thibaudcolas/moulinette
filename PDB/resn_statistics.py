#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import utils


def main():
    config = utils.load_config(__file__)
    data = utils.load_data(__file__)

    count = {}

    for code in data:
        for interface in data[code]['interfaces']:
            is_active = config['active'][code][interface]
            residues = data[code]['interfaces'][interface]['residues']

            if is_active:
                for r in residues:
                    acid = r['resn'].encode('utf-8')
                    if acid in count:
                        count[acid] += 1
                    else:
                        count[acid] = 1

    total = sum(count.values())

    for acid in sorted(count.keys()):
        print acid, '{:1.1f}'.format(100 * count[acid] / float(total)), u'({0} / {1})'.format(count[acid], total)

    # output.sort(key=lambda pair: len(pair[1]), reverse=True)

    # for (header, sequence) in output:
    #     print header.encode('utf-8')
    #     print sequence.encode('utf-8')


if __name__ == "__main__":
    main()

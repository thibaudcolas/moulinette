# -*- coding: utf-8 -*-

import json
import codecs
import sys
import os

DATA_FILE = 'data.json'

one_letter_codes = {
    "GLY": "G",
    "PRO": "P",
    "ALA": "A",
    "VAL": "V",
    "LEU": "L",
    "ILE": "I",
    "MET": "M",
    "CYS": "C",
    "PHE": "F",
    "TYR": "Y",
    "TRP": "W",
    "HIS": "H",
    "LYS": "K",
    "ARG": "R",
    "GLN": "Q",
    "ASN": "N",
    "GLU": "E",
    "ASP": "D",
    "SER": "S",
    "THR": "T",
    # Rare codes
    "MSE": "M",
    "SRZ": "S",
    "DNP": "A",
    "CME": "C",
    "MLU": "L",
    "OMZ": "Y",
    "MLY": "K",
    "OMY": "Y",
    "SEP": "S",
    # Codes to remove
    "GHP": "",
    "3FG": "",
}


def get_one_letter_code(amino_acid, pdb_code):
    try:
        return one_letter_codes[amino_acid]
    except KeyError:
        sys.exit('Error: ' + amino_acid + ' amino acid code not found. In ' + pdb_code)


def get_clustal_omega_header(fields):
    return u'>{name}_{code}_{interface}_{chain}{suffix}'.format(**fields)


def get_json_path(file):
    args = sys.argv[1:]
    return os.path.join(args[0], DATA_FILE) if len(args) > 0 else get_default_json_path(file)


def get_default_json_path(file):
    return os.path.join(os.path.dirname(file), 'store', DATA_FILE)


def load_json(file_path):
    return json.loads(codecs.open(file_path, 'r', 'utf-8').read())


def save_json(file_path, data):
    f = codecs.open(file_path, 'w', 'utf-8')
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    f.close()


# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def print_progress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()
    if iteration == total:
        print("\n")


def read_input_line(line):
    fields = line.rstrip('\n').split()

    return {
        'code': fields[0],
        'name': u' '.join(fields[1:]),
    }


def read_input_file(file_path):
    file = codecs.open(file_path, 'r', 'utf-8')
    return [read_input_line(line) for line in file]

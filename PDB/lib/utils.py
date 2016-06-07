# -*- coding: utf-8 -*-

import json
import sys

aminoacid_codes = {
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
	"3FG": ""
	
}


def get_clustal_omega_header(code, interface, chain):
    return ">{code}_{interface}_{chain}".format(code=code, interface=interface, chain=chain)


def load_json(file_path):
    return json.loads(open(file_path).read())


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

from pymol import cmd

PDB_CODES_FILE = 'pdb-codes.txt'


def read_pdb_codes():
    return [line.rstrip('\n') for line in open(PDB_CODES_FILE)]


pdb_codes = read_pdb_codes()


def fetch_pdb_files():
    for code in pdb_codes:
        success = cmd.fetch(code)
        print 'Fetched ' + success


def load_pdb_files():
    for code in pdb_codes:
        filename = code + '.pdb'
        cmd.load(filename, code)


fetch_pdb_files()
load_pdb_files()

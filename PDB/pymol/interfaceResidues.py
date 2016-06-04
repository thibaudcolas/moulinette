from pymol import cmd

PDB_CODES_LIST = 'pdb-codes.txt'


def load_pdb_files():
    pdb_codes = [line.rstrip('\n') for line in open(PDB_CODES_LIST)]

    for code in pdb_codes:
        success = cmd.fetch(code)
        print 'Fetched ' + success

load_pdb_files()

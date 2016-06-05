from pymol import cmd
from lib import interfaceResidues
import itertools

PDB_CODES_FILE = 'pdb-codes.txt'
STORE_DIR = 'store'


def read_pdb_codes():
    return [line.rstrip('\n') for line in open(PDB_CODES_FILE)]


pdb_codes = read_pdb_codes()


def load_pdb_files():
    for code in pdb_codes:
        cmd.fetch(code)
        print 'Loaded ' + code


def save_to_file(file_name, lines):
    file = open(STORE_DIR + '/' + file_name + '.txt', 'w')
    file_lines = [(' '.join(l) + '\n') for l in lines]
    file.write(''.join(file_lines))
    file.close()


def save_residues():
    for pdb_code in pdb_codes:
        chains = cmd.get_chains(pdb_code)

        for (cA, cB) in itertools.combinations(chains, 2):
            interface = pdb_code + '_' + cA + cB
            interfaceResidues.interfaceResidues(pdb_code, cA='c. ' + cA, cB='c. ' + cB, selName=interface)

            # There probably is a simpler way to do this using idiomatic Python,
            # but I don't know enough PyMOL to understand what is going on here.
            selection = interface + ' & n. ca'
            expression = 'residues.append((chain, resi, resn))'
            space = {'residues': []}
            cmd.iterate(selection, expression, space=space)

            save_to_file(interface, space['residues'])

load_pdb_files()
save_residues()

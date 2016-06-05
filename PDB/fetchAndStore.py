from pymol import cmd
from lib import interfaceResidues

PDB_CODES_FILE = 'pdb-codes.txt'
RESIDUES_STORE_DIR = 'store'


def read_pdb_codes():
    return [line.rstrip('\n') for line in open(PDB_CODES_FILE)]


pdb_codes = read_pdb_codes()


def load_pdb_files():
    for code in pdb_codes:
        cmd.fetch(code)
        print 'Loaded ' + code


def save_residues():
    for pdb_code in pdb_codes:
        selName = pdb_code + '-interface'
        print pdb_code
        interfaceResidues.interfaceResidues(pdb_code, selName=selName)
        space = {
            'residues': []
        }
        # There probably is a simpler way to do this using idiomatic Python,
        # but I don't know enough PyMOL to understand what is going on here.
        # cmd.iterate(selName + ' & n. ca', 'print chain,resi,resn')
        selection = selName + ' & n. ca'
        expression = 'residues.append((chain, resi, resn))'
        cmd.iterate(selection, expression, space=space)

        file = open(RESIDUES_STORE_DIR + '/' + pdb_code + '.txt', 'w')
        file_lines = [(' '.join(res) + '\n') for res in space['residues']]
        file.write(''.join(file_lines))
        file.close()

load_pdb_files()
save_residues()

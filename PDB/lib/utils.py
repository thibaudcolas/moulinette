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
    "THR": "T"
}


def get_clustal_omega_header(code, interface, chain):
    return ">{code}_{interface}_{chain}".format(code=code, interface=interface, chain=chain)

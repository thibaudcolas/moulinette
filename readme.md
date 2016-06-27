moulinette [![Build Status](https://travis-ci.org/ThibWeb/moulinette.svg?branch=master)](https://travis-ci.org/ThibWeb/moulinette)
==========

> A collection of scripts related to biochemistry.

## [PDB (Protein Data Bank)](http://www.rcsb.org/pdb/home/home.do) collection

### Interface residues analysis (node POC)

To execute the script,

1. Download a [ZIP of this repository](https://github.com/ThibWeb/moulinette/archive/master.zip)
2. TODO

## [NMR (Nuclear Magnetic Resonance)](https://en.wikibooks.org/wiki/Structural_Biochemistry/Proteins/NMR_Spectroscopy) collection

### Interface residues analysis (PyMOL integration)

```sh
cd PDB/
pymol -cqx fetch_and_store.py
./generate_config.py
./list.py
./list_spiced.py
./resn_statistics.py
```

#### Useful resources

**Install:**

- http://pymolwiki.org/index.php/Main_Page
- http://www.pymolwiki.org/index.php/MAC_Install
- http://www.pymolwiki.org/index.php/Linux_Install
- http://www.pymolwiki.org/index.php/Launching_From_a_Script

**Script writing:**

- http://pymolwiki.org/index.php/FetchLocal
- http://pymolwiki.org/index.php/LoadDir
- http://pymolwiki.org/index.php/Process_All_Files_In_Directory

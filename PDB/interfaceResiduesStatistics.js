#!/usr/bin/env node

const path = require('path');
const fs = require('fs');

const aminoacidCodes = require('./aminoacidCodes.json');

const INPUT_DIR = path.join('.', 'PDB', 'input');

// Filename = pdbCode of a given protein.
// key = one <pdbCode>.txt = interface residues of <pdbCode>
// value = content of <pdbCode>.txt
// One line in the files = "Chain Resi Resn" (Residue index, Residue type)
const data = {};

function readFiles(dirname, onFileContent, onError) {
    fs.readdir(dirname, (err, filenames) => {
        if (err) {
            onError(err);
            return;
        }

        filenames.filter(filename => filename.indexOf('.txt') !== -1)
            .forEach((filename) => {
                fs.readFile(path.join(INPUT_DIR, filename), 'utf-8', (errDir, rawContent) => {
                    if (errDir) {
                        onError(errDir);
                        return;
                    }

                    onFileContent(filename, rawContent);
                });
            });
    });
}

function createInterfaceResiduesFromFile(filename, content) {
    const lines = content
        .split('\r\n')
        .map(line => line.split(' '));

    const residues = lines.reduce((chains, residue) => {
        const chain = residue[0];

        if (!chains[chain]) {
            chains[chain] = [];
        }

        chains[chain].push({
            resi: parseInt(residue[1], 10),
            resn: aminoacidCodes[residue[2]],
        });

        return chains;
    }, {});

    return residues;
}

function output(pdbCode, interfaceResidues) {
    Object.keys(interfaceResidues).forEach((chain) => {
        const residues = interfaceResidues[chain];

        console.log(`>${pdbCode}_${chain}_TODO`);
    })
    return pdbCode;
}


readFiles(INPUT_DIR, (filename, content) => {
    const pdbCode = filename.replace('.txt', '');
    const residues = createInterfaceResiduesFromFile(filename, content);

    data[pdbCode] = residues;

    console.log(JSON.stringify(data, null, 4));
    //console.log(Object.keys(data));

    //output(pdbCode, residues);
}, (err) => {
    throw err;
});

// First script: ???
// Second script: statistics on resn
// Third script: output amino acid sequences with "x" in gaps

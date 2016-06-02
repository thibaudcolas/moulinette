#!/usr/bin/env node

const path = require('path');
const fs = require('fs');
const _ = require('lodash');

const aminoacidCodes = require('./aminoacidCodes.json');

const INPUT_DIR = path.join('.', 'PDB', 'test');

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
        // Remove CR for line endings in Windows.
        .replace(/\r/g, '')
        .split('\n')
        .filter(line => !!line)
        .map(line => line.split(' '));

    const residuesAnalysis = lines.reduce((chains, residue) => {
        const chain = residue[0];

        if (!chains[chain]) {
            chains[chain] = {
                residues: [],
                sequences: [],
            };
        }

        chains[chain].residues.push({
            resi: parseInt(residue[1], 10),
            resn: aminoacidCodes[residue[2]],
        });

        return chains;
    }, {});

    Object.keys(residuesAnalysis).forEach((chain) => {
        const rawSequences = residuesAnalysis[chain].residues.reduce((seqs, residue, index) => {
            const lastIndex = index === 0 ? 0 : seqs.length - 1;
            const lastSeq = seqs[lastIndex];

            if (lastSeq && lastSeq[lastSeq.length - 1].resi === residue.resi - 1) {
                lastSeq.push(residue);
            } else {
                const newSeq = [residue];

                seqs.push(newSeq);
            }

            return seqs;
        }, []);

        residuesAnalysis[chain].sequences = _.sortBy(rawSequences.filter(seq => seq.length > 1), seq => seq.length);
    });

    return residuesAnalysis;
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

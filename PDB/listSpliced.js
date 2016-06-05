#!/usr/bin/env node

const argv = require('yargs').argv;
const _ = require('lodash');
const utils = require('./lib/utils');

const filesDir = argv._[0];

// Filename = pdbCode of a given protein.
// key = one <pdbCode>.txt = interface residues of <pdbCode>
// value = content of <pdbCode>.txt
// One line in the files = "Chain Resi Resn" (Residue index, Residue type)
const data = {};

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
            resn: utils.getOneLetterCode([residue[2]]),
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

        residuesAnalysis[chain].sequences = _.sortBy(rawSequences.filter(seq => seq.length > 1), seq => seq.length).reverse();
    });

    return residuesAnalysis;
}


utils.readFiles(filesDir, (filename, content) => {
    const pdbCode = filename.replace('.txt', '');
    const residues = createInterfaceResiduesFromFile(filename, content);

    data[pdbCode] = residues;

    // console.log(JSON.stringify(data, null, 4));

    utils.clustalOmegaOutput(pdbCode, residues);
}, (err) => {
    throw err;
});

// First script: ???
// Second script: statistics on resn
// Third script: output amino acid sequences with "x" in gaps

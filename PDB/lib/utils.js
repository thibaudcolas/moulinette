const path = require('path');
const fs = require('fs');

const aminoacidCodes = require('./aminoacidCodes.json');

module.exports = {
    getOneLetterCode: code => aminoacidCodes[code],

    readFiles(dirname, onFileContent, onError) {
        fs.readdir(dirname, (err, filenames) => {
            if (err) {
                onError(err);
                return;
            }

            filenames.filter(filename => filename.indexOf('.txt') !== -1)
                .forEach((filename) => {
                    fs.readFile(path.join(dirname, filename), 'utf-8', (errDir, rawContent) => {
                        if (errDir) {
                            onError(errDir);
                            return;
                        }

                        onFileContent(filename, rawContent);
                    });
                });
        });
    },

    clustalOmegaOutput(pdbCode, interfaceResidues) {
        Object.keys(interfaceResidues).forEach((chain) => {
            interfaceResidues[chain].sequences.forEach((seq, ind) => {
                console.log(`>${pdbCode}_${chain}_${ind}`);
                console.log(seq.map(res => res.resn).join(''));
            });
        })
    },
}

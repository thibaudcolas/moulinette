#!/bin/bash -e
prefix=$PWD/pymol
modules=$prefix/modules
svnpymol=svnpymol

###################################################
mkdir -p $prefix
mkdir -p $HOME/bin

###### Checkout pymol svn
svn co --quiet svn://svn.code.sf.net/p/pymol/code/trunk/pymol $prefix/$svnpymol
###### Build and install pymol
cd $prefix/$svnpymol
python setup.py build install --home=$prefix --install-lib=$modules --install-scripts=$prefix

export PATH="$prefix:$modules:$PATH"
export PYMOL_PATH="$modules"

which pymol || echo ok

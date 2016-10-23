#!/bin/bash -e
prefix=$PWD/pymol
modules=$prefix/modules
svnpymol=svnpymol

###################################################
mkdir -p $prefix
mkdir -p $HOME/bin

if [ -f "$prefix/pymol" ];
then
   echo "pymol already exists. Skipping install"
else
   echo "Installing pymol"

   ###### Checkout pymol svn
   svn co --quiet svn://svn.code.sf.net/p/pymol/code/trunk/pymol $prefix/$svnpymol
   ###### Build and install pymol
   cd $prefix/$svnpymol
   python setup.py build install --home=$prefix --install-lib=$modules --install-scripts=$prefix
fi

export PYMOL_PATH="$modules"
sudo ln -s "$prefix/pymol" /usr/bin/pymol

which pymol || echo ok

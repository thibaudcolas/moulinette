#!/bin/bash -e
prefix=$PWD/pymol
modules=$prefix/modules
svnpymol=svnpymol
update=$prefix/updatepymol.sh

###################################################
mkdir -p $prefix
mkdir -p $HOME/bin

###### Checkout pymol svn
svn co svn://svn.code.sf.net/p/pymol/code/trunk/pymol $prefix/$svnpymol
###### Build and install pymol
cd $prefix/$svnpymol
python setup.py build install --home=$prefix --install-lib=$modules --install-scripts=$prefix

## Make a update script
cat > "$update" <<EOF
#!/bin/bash -e
prefix=$prefix
modules=$modules
svnpymol=svnpymol

###### Checkout pymol svn
svn co svn://svn.code.sf.net/p/pymol/code/trunk/pymol \$prefix/\$svnpymol
###### Build and install pymol
cd \$prefix/\$svnpymol
python setup.py build install --home=\$prefix --install-lib=\$modules --install-scripts=\$prefix
EOF
chmod +x $update

alias pymol="$prefix/pymol"
ls "$prefix"
export PYMOL_PATH="$modules"

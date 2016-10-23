#!/bin/bash -e
prefix=$PWD/pymol
modules=$prefix/modules
svnpymol=svnpymol
svnfreemol=svnfreemol
pymolscriptrepo=Pymol-script-repo
update=$prefix/updatepymol.sh

###################################################
mkdir -p $prefix
mkdir -p $HOME/bin

###### Checkout pymol svn
svn co svn://svn.code.sf.net/p/pymol/code/trunk/pymol $prefix/$svnpymol
###### Build and install pymol
cd $prefix/$svnpymol
python setup.py build install --home=$prefix --install-lib=$modules --install-scripts=$prefix

########## Setup freemol - for MPEG support ############
svn co svn://bioinformatics.org/svnroot/freemol/trunk $prefix/$svnfreemol
cd $prefix/$svnfreemol/src/mpeg_encode
export FREEMOL=$prefix/$svnfreemol/freemol
./configure
make
make install

########## Install Pymol-script-repo ############
git clone git://github.com/Pymol-Scripts/Pymol-script-repo.git $prefix/$pymolscriptrepo

## Make a shortcut to an extended pymol execution
echo "#!/bin/bash" > $prefix/pymolMPEG.sh
echo "export FREEMOL=$prefix/$svnfreemol/freemol" >> $prefix/pymolMPEG.sh
echo "export PYMOL_GIT_MOD=$prefix/$pymolscriptrepo/modules" >> $prefix/pymolMPEG.sh
echo "export PYTHONPATH=$prefix/$pymolscriptrepo/modules"':$PYTHONPATH' >> $prefix/pymolMPEG.sh
echo "export PYTHONPATH=$prefix/$pymolscriptrepo"':$PYTHONPATH' >> $prefix/pymolMPEG.sh
echo '#export PYTHONPATH=$PYTHONPATH:/sbinlab2/software/x64/lib64/python2.6/site-packages/PIL' >> $prefix/pymolMPEG.sh
echo '#export PYTHONPATH=$PYTHONPATH:/sbinlab2/software/x64/lib64/python2.6/site-packages/lib-dynload' >> $prefix/pymolMPEG.sh
echo '#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/sbinlab2/software/x64/lib/pymollib' >> $prefix/pymolMPEG.sh
echo '#export LIBGL_ALWAYS_INDIRECT=no' >> $prefix/pymolMPEG.sh
tail -n +2 $prefix/pymol >> $prefix/pymolMPEG.sh
chmod ugo+x $prefix/pymolMPEG.sh

## Make a startup files, which is always executed on startup.
t="'"
echo "import sys,os" > $modules/pymol/pymol_path/run_on_startup.py
echo "import pymol.plugins" >> $modules/pymol/pymol_path/run_on_startup.py
echo "pymol.plugins.preferences = {'instantsave': False, 'verbose': False}" >> $modules/pymol/pymol_path/run_on_startup.py
echo "pymol.plugins.autoload = {'apbs_tools': False}" >> $modules/pymol/pymol_path/run_on_startup.py
echo "pymol.plugins.set_startup_path( [$t$prefix/$pymolscriptrepo/plugins$t,$t$modules/pmg_tk/startup$t] )" >> $modules/pymol/pymol_path/run_on_startup.py
echo "pymol.plugins.preferences = {'instantsave': True, 'verbose': False}" >> $modules/pymol/pymol_path/run_on_startup.py

## Make a update script
cat > "$update" <<EOF
#!/bin/bash -e
prefix=$prefix
modules=$modules
svnpymol=svnpymol
svnfreemol=svnfreemol
pymolscriptrepo=Pymol-script-repo

###### Checkout pymol svn
svn co svn://svn.code.sf.net/p/pymol/code/trunk/pymol \$prefix/\$svnpymol
###### Build and install pymol
cd \$prefix/\$svnpymol
python setup.py build install --home=\$prefix --install-lib=\$modules --install-scripts=\$prefix

########## Setup freemol - for MPEG support ############
svn co svn://bioinformatics.org/svnroot/freemol/trunk \$prefix/\$svnfreemol
cd \$prefix/$svnfreemol/src/mpeg_encode
export FREEMOL=\$prefix/\$svnfreemol/freemol
./configure
make
make install

########## Update Pymol-script-repo ############
cd \$prefix/\$pymolscriptrepo
git pull origin master
cd \$prefix
EOF
chmod +x $update

#!/usr/bin/perl
#1/transforme un fichier de pics attribues  NMRVIEW en fichier de peaks compatible CYANA
#2/
#        ouvrenput
#
#
# le fichier resultat= {INPUTFILENAME}-out.xpk

if ($ARGV[0]) {
  $input = $ARGV[0];
}
else {
  print " usage : fromXplortodyanaang.pl TOTOINPUT.xpk \n";
  exit;
}

open(FILE_IN, $input);

# Récupération du nom du fichier de sortie
use File::Basename;
$inputfile = basename($input);
(my $outputfile = $inputfile) =~ s/.xpk/-out.xpk/;

# Création du fichier de sortie.
system ("rm $outputfile");
open(FICHIERRES,">>$outputfile") or die "ne peut pas ouvrir le fichier $outputfile!";

$compteur = 0;

while (<FILE_IN>) {
  @ligne= split(" ",$_);

  $compteur = $compteur +1;
  $numpeak = @ligne[0];
  $attrib1 = @ligne[1];
  $chem1 = @ligne[2];
  $error1 = @ligne[3];
  $inc1 = @ligne[4];
  $inc2 = @ligne[5];
  $inc3 = @ligne[6];
  $attrib2 = @ligne[7];
  $chem2 = @ligne[8];
  $error2 = @ligne[9];
  $inc5 = @ligne[10];
  $inc6 = @ligne[11];
  $inc7 = @ligne[12];
  $vol = @ligne[13];
  $int = @ligne[14];
  $valid = @ligne[15];

  if ($attrib1 ne "?")  {
    @tamp1= split (/\./,"$attrib1");
    $res1=@tamp1[0];
    $res1=~s/\{//;
    $atom1=@tamp1[1];
    $atom1=~s/\}//;
    print "\n tamp1 $tamp1";
    print "\n res1  $res1";
    print "\n atoma1 $atom1";
  }

  if ($attrib2 ne "?")  {
    @tamp2= split(/\./,$attrib2);
    $res2=@tamp2[0];
    $res2=~s/\{//;
    print "\ res2 $res2";
    $atom2=@tamp2[1];
    $atom2=~s/\}//;
    print "\n tamp2 $tamp2";
    print "\n atoma 2 $atom2";
  }

  if ($attrib1 ne "?") {
    $attrib1 = "{".$res1.".".$atom1."}";
  }
  if ($attrib2 ne "?") {
    $attrib2 = "{".$res2.".".$atom2."}";
  }

  print  "\n coucou2 $numpeak $attrib1 $chem1 $error1 $inc1 $inc2 $inc3 $inc4 $attrib2 $chem2 $error2 $inc5 $inc6 $inc7 $inc8  $vol $int $inc9 $inc10 $inc11";

  # On ignore l'entête du fichier et elle est reproduite telle quelle.
  if ($compteur < 7) {
    $lineoutput = $_;
  }
  else {
    $lineoutput = "$numpeak $attrib1 $chem1 $error1 0.04 $inc2 $inc3 $inc4 $attrib2 $chem2 $error2  0.04 $inc6 $inc7 $inc8  $vol $int $inc9 $inc10 $inc11\n";
  }

  print FICHIERRES $lineoutput;
}

close FILE_IN;
close FICHIERRES;

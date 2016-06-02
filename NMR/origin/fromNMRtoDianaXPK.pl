#!/usr/bin/perl
#1/transforme un fichier de pics attribues  NMRVIEW en fichier de peaks compatible CYANA
#2/
#        ouvrenput
#
#
# le fichier resultat= out.xpk

if ($ARGV[0]) { $input = $ARGV[0]; }
else { print " usage : fromXplortodyanaang.pl TOTOINPUT.xpk \n"; exit; }

use File::Basename;
$inputfile = basename($input);
(my $outputfile = $inputfile) =~ s/.xpk/-out.xpk/;

open(FILE_IN,$input);
system ("rm $outputfile");
open(FICHIERRES,">>$outputfile") or die "ne peut pas ouvrir le fichier $outputfile!";
          $compteur= 0;
@ALA=(3,15);
@ILE=(11,12);
@LEU=(6,8,16);
@PRO=(2);
@SER=(4,19);
@ARG=(13);
@LYS=(14);
@GLY=(7,18);
@GLU=(9);
@PHE=(20);
@MET=(17);
@ASP=(1,10,21);
@CYS=();
@TRP=();
@TYR=();
@GLN=();
@ASN=(5);
@TYR=();
@HIS=();
@THR=();
while(<FILE_IN>)

{
         @ligne= split(" ",$_);
          $compteur= $compteur +1;
          $numpeak = @ligne[0];
          $attrib1 = @ligne[1];
          $chem1 = @ligne[2];
          $error1 = @ligne[3];
          $inc1= @ligne[4];
          $inc2= @ligne[5];
          $inc3= @ligne[6];
          $attrib2 = @ligne[7];
          $chem2 = @ligne[8];
          $error2 = @ligne[9];
          $inc5= @ligne[10];
          $inc6= @ligne[11];
          $inc7= @ligne[12];
          $vol= @ligne[13];
          $int= @ligne[14];
          $valid= @ligne[15];

         if ($attrib1 ne "?")  {
         @tamp1= split (/\./,"$attrib1");
        $res1=@tamp1[0];
         $res1=~s/\{//;
         $atom1=@tamp1[1];
         $atom1=~s/\}//;
         print "\n tamp1 $tamp1";
         print "\n res1  $res1";
         print "\n atoma1 $atom1";

foreach $myres (@LEU,@SER,@CYS,@PHE,@TYR,@TRP,@LYS,@ARG,@MET,@PRO,@HIS,@ASP,@GLU,@GLN)
 {
  if ($res1 == $myres) {
  $atom1=&HB1HB2($atom1);
  $atom1=&QHBtoQB($atom1);}
}

 foreach $myres (@LYS,@PRO,@ASP,@GLU,@GLN)
{
  if ($res1 == $myres) {
  $atom1=&QHGtoQG($atom1);
  $atom1=&QHDtoQD($atom1);
  $atom1=&QHEtoQE($atom1);}
}

 foreach $myres (@ARG)
{
  if ($res1 == $myres) {
  $atom1=&QHGtoQG($atom1);
  $atom1=&QHDtoQD($atom1);}
}

foreach $myres (@LYS,@ARG)
 {
  if ($res1 == $myres) {
  $atom1=&HE1HE2($atom1);}
}

foreach $myres (@ALA)
 {
  if ($res1 == $myres) {
  $atom1=&QHBtoQB($atom1);}
}

foreach $myres (@LYS,@ARG,@PRO)
 {
  if ($res1 == $myres) {
  $atom1=&HD1HD2($atom1);}
}

foreach $myres (@ILE)
 {
  if ($res1 == $myres) {
  $atom1=&HG21HG22HG23($atom1);
  $atom1=&HG11HG12($atom1);
  $atom1=&HD11toQD1($atom1);
  $atom1=&QDtoQD1($atom1);}
  $atom1=&QHDtoQD1($atom1);
}

foreach $myres (@ASN)
 {
  if ($res1 == $myres) {
  $atom1=&HB1HB2($atom1);
  $atom1=&QHBtoQB($atom1);
  $atom1=&HGtoHD21($atom1);}
}

foreach $myres (@GLY)
 {
  if ($res1 == $myres) {
  $atom1=&HA1HA2($atom1);
  $atom1=&HAtoQA($atom1);}
}


foreach $myres (@LEU)
 {
  if ($res1 == $myres) {
  $atom1=&HD11HD12HD13($atom1);
  $atom1=&HD21HD22HD23($atom1);
  $atom1=&HD1HD2toQD1QD2($atom1);
  $atom1=&HD1toQD1($atom1);}
}

foreach $myres (@LYS,@ARG,@PRO,@GLU,@GLN,@MET)
 {
  if ($res1 == $myres) {
  $atom1=&HG1HG2($atom1);}
}

foreach $myres (@PHE)
 {
  if ($res1 == $myres) {
  $atom1=&H26($atom1);
  $atom1=&H35($atom1);
  $atom1=&H4($atom1);}
}

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

foreach $myres (@LEU,@SER,@CYS,@PHE,@TYR,@TRP,@LYS,@ARG,@MET,@PRO,@HIS,@ASP,@GLU,@GLN)
 {
  if ($res2 == $myres) {
  $atom2=&HB1HB2($atom2);
  $atom2=&QHBtoQB($atom2);}
}

 foreach $myres (@LYS,@PRO,@ASP,@GLU,@GLN)
{
  if ($res2 == $myres) {
  $atom2=&QHGtoQG($atom2);
  $atom2=&QHDtoQD($atom2);
  $atom2=&QHEtoQE($atom2);}
}

 foreach $myres (@ARG)
{
  if ($res2 == $myres) {
  $atom2=&QHGtoQG($atom2);
  $atom2=&QHDtoQD($atom2);}
}

foreach $myres (@LYS,@ARG)
 {
  if ($res2 == $myres) {
  $atom2=&HE1HE2($atom2);}
}

foreach $myres (@ALA)
 {
  if ($res2 == $myres) {
  $atom2=&QHBtoQB($atom2);}
}

foreach $myres (@LYS,@ARG,@PRO)
 {
  if ($res2 == $myres) {
  $atom2=&HD1HD2($atom2);}
}

foreach $myres (@ILE)
 {
  if ($res2 == $myres) {
  $atom2=&HG21HG22HG23($atom2);
  $atom2=&HG11HG12($atom2);
  $atom2=&HD11toQD1($atom2);
  $atom2=&QDtoQD1($atom2);}
  $atom2=&QHDtoQD1($atom2);
}

foreach $myres (@ASN)
 {
  if ($res2 == $myres) {
  $atom2=&HGtoHD21($atom2);
  $atom2=&HB1HB2($atom2);
  $atom2=&QHBtoQB($atom2);}
}

foreach $myres (@GLY)
 {
  if ($res2 == $myres) {
  $atom2=&HA1HA2($atom2);
  $atom2=&HAtoQA($atom2);}
}

foreach $myres (@LEU)
 {
  if ($res2 == $myres) {
  $atom2=&HD11HD12HD13($atom2);
  $atom2=&HD21HD22HD23($atom2);
  $atom2=&HD1HD2toQD1QD2($atom2);
  $atom2=&HD1toQD1($atom2);}
}

foreach $myres (@PHE)
 {
  if ($res2 == $myres) {
  $atom2=&H26($atom2);
  $atom2=&H35($atom2);
  $atom2=&H4($atom2);}
}


foreach $myres (@LYS,@ARG,@PRO,@GLU,@GLN,@MET)
 {
  if ($res2 == $myres) {
  $atom2=&HG1HG2($atom2);}
}


}

if ($atom2 eq "HN") {$atom2="H";}
if ($atom2 eq "N") {$atom2="H";}
if ($atom1 eq "HN") {$atom1="H";}
if ($atom1 eq "N") {$atom1="H";}

if ($attrib1 ne "?") {$attrib1 = "{".$res1.".".$atom1."}";}
if ($attrib2 ne "?") {$attrib2 = "{".$res2.".".$atom2."}";}


          print  "\n coucou2 $numpeak $attrib1 $chem1 $error1 $inc1 $inc2 $inc3 $inc4 $attrib2 $chem2 $error2 $inc5 $inc6 $inc7 $inc8  $vol $int $inc9 $inc10 $inc11";

          print FICHIERRES "\n $numpeak $attrib1 $chem1 $error1 0.04 $inc2 $inc3 $inc4 $attrib2 $chem2 $error2  0.04 $inc6 $inc7 $inc8  $vol $int $inc9 $inc10 $inc11";
          }
close FILE_IN;
close FICHIERRES;

sub HB1HB2 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HB2") { $iciatom1 = "HB3";}
           if ( $iciatom1 eq "HB1") { $iciatom1 = "HB2";}
           $iciatom1;
           }

sub HG1HG2 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HG2") { $iciatom1 = "HG3";}
           if ( $iciatom1 eq "HG1") { $iciatom1 = "HG2";}
           $iciatom1;
           }

sub HG21HG22HG23 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HG21") { $iciatom1 = "QG2";}
           if ( $iciatom1 eq "HG22") { $iciatom1 = "QG2";}
           if ( $iciatom1 eq "HG23") { $iciatom1 = "QG2";}
           $iciatom1;
           }

sub HD11toQD1 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HD11") { $iciatom1 = "QD1";}
           if ( $iciatom1 eq "HD12") { $iciatom1 = "QD1";}
           if ( $iciatom1 eq "HD13") { $iciatom1 = "QD1";}
           $iciatom1;
           }

sub QDtoQD1 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "QD") { $iciatom1 = "QD1";}
           $iciatom1;
           }

sub HD11HD12HD13 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HD11") { $iciatom1 = "QD1";}
           if ( $iciatom1 eq "HD12") { $iciatom1 = "QD1";}
           if ( $iciatom1 eq "HD13") { $iciatom1 = "QD1";}
           $iciatom1;
           }

sub HD21HD22HD23 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HD21") { $iciatom1 = "QD2";}
           if ( $iciatom1 eq "HD22") { $iciatom1 = "QD2";}
           if ( $iciatom1 eq "HD23") { $iciatom1 = "QD2";}
           $iciatom1;
           }

sub HD1HD2toQD1QD2 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HD1") { $iciatom1 = "QD1";}
           if ( $iciatom1 eq "HD2") { $iciatom1 = "QD2";}
           $iciatom1;
           }

sub HD21H212HD23 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HD21") { $iciatom1 = "QD2";}
           if ( $iciatom1 eq "HD22") { $iciatom1 = "QD2";}
           if ( $iciatom1 eq "HD23") { $iciatom1 = "QD2";}
           $iciatom1;
           }

sub HG11HG12 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HG11") { $iciatom1 = "HG12";}
           if ( $iciatom1 eq "HG12") { $iciatom1 = "HG13";}
           $iciatom1;
           }

sub HA1HA2 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HA2") { $iciatom1 = "HA3";}
           if ( $iciatom1 eq "HA1") { $iciatom1 = "HA2";}
           $iciatom1;
           }

sub QHBtoQB { local ($iciatom1)=@_;
           if ( $iciatom1 eq "QHB") { $iciatom1 = "QB";}
           $iciatom1;
           }

sub QHGtoQG { local ($iciatom1)=@_;
           if ( $iciatom1 eq "QHG") { $iciatom1 = "QG";}
           $iciatom1;
           }

sub QHDtoQD { local ($iciatom1)=@_;
           if ( $iciatom1 eq "QHD") { $iciatom1 = "QD";}
           $iciatom1;
           }

sub QHDtoQD1{ local ($iciatom1)=@_;
           if ( $iciatom1 eq "QHD") { $iciatom1 = "QD1";}
           $iciatom1;
           }

sub QHEtoQE { local ($iciatom1)=@_;
           if ( $iciatom1 eq "QHE") { $iciatom1 = "QE";}
           $iciatom1;
           }

sub HD1toQD1 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HD1") { $iciatom1 = "QD1";}
           if ( $iciatom1 eq "HD2") { $iciatom1 = "QD2";}
           $iciatom1;
           }

sub H26 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "2,6H") { $iciatom1 = "QD";}
           $iciatom1;
           }

sub H35 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "3,5H") { $iciatom1 = "QE";}
           $iciatom1;
           }

sub H4 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "4H") { $iciatom1 = "HZ";}
           $iciatom1;
           }

sub HAtoQA { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HA") { $iciatom1 = "QA";}
           $iciatom1;
           }

sub HD1HD2 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HD2") { $iciatom1 = "HD3";}
           if ( $iciatom1 eq "HD1") { $iciatom1 = "HD2";}
           $iciatom1;
           }

sub HE1HE2 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HE2") { $iciatom1 = "HE3";}
           if ( $iciatom1 eq "HE1") { $iciatom1 = "HE2";}
           $iciatom1;
           }
sub HGtoHD21 { local ($iciatom1)=@_;
           if ( $iciatom1 eq "HG1") { $iciatom1 = "HD21";}
           if ( $iciatom1 eq "HG2") { $iciatom1 = "HD22";}
           $iciatom1;
           }


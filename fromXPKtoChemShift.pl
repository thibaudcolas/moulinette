#!/usr/bin/perl
# - Script d'extraction des valeurs de déplacement chimique pour chaque atome.
# - Compare les valeurs de déplacement chimique pour un atome donné et alerte
# si l'étendue (max - min) est supérieure à un seuil choisi.
#

use List::Util qw( min max );

$threshold = 0.02;

if ($ARGV[0]) {
  $input = $ARGV[0];
}
else {
  print "Usage: fromXPKtoChemShift.pl INPUTFILE.xpk\n";
  exit;
}

open(FILE_IN, $input);

# Récupération du nom du fichier de sortie
use File::Basename;
$inputfile = basename($input);
(my $outputfile = $inputfile) =~ s/.xpk/-chemshift.txt/;

# Création du fichier de sortie.
system ("rm $outputfile");
open(FICHIERRES,">>$outputfile") or die "ne peut pas ouvrir le fichier $outputfile!";

$compteur = 0;

@ambiguous = ();
%group = ();

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

  # On ignore l'entête du fichier et elle est reproduite telle quelle.
  if ($compteur < 7) {
    print FICHIERRES $_;
  }
  # Ne rien faire si la ligne n'est pas valide.
  elsif ($valid ne "-1") {

    # Store ambiguous lines, to be added at the end of output.
    if ($attrib1 eq "?" || $attrib2 eq "?")  {
      push(@ambiguous, $_);
    }
    else {

      if (!defined $group{$attrib1}) {
        $group{$attrib1} = ();
      }
      push(@{$group{$attrib1}}, $chem1);

      if (!defined $group{$attrib2}) {
        $group{$attrib2} = ();
      }
      push(@{$group{$attrib2}}, $chem2);
    }
  }
}

use Data::Dumper;
print Dumper(\%group);

while (($attrib, $chem) = each(%group)) {
  $diff = max(@{$chem}) - min(@{$chem});

  foreach (@{$chem}) {
    $line = "$attrib $_";

    if ($diff > $threshold) {
      $line = "$line $diff"
    }

    print "$line\n";
  }
  print "\n";
}

foreach (@ambiguous) {
  print FICHIERRES $_;
}

close FILE_IN;
close FICHIERRES;


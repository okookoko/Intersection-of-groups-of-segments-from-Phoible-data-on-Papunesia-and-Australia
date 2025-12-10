# Intersection-of-groups-of-segments-from-Phoible-data-on-Papunesia-and-Australia
<p>
  This was created for a Language Typology group project. I took data from Phoible and filtered it into separate files for Papunesia and Australia. Then I made a way to compare  what languages have abc and xyz segments.
There are definitely ways to make this code faster; I was just doing this quickly and tailoring it to the specific problem I needed to solve.
</p>
<p>
  The 'filter and write....py' files were used to filter through 'languages.csv' and 'values.csv' so that only the macroareas we were interested in, Papunesia and Australia, were left.
</p>
<p>
  The 'intersections of sets.py' file asks you to input 2 sets of desired segments you wish to examine, separated by commas.
</p>
<p>
  Input the description of your first set of desired segments, separated by a comma ",":LATIN SMALL LETTER P, LATIN SMALL LETTER T, LATIN SMALL LETTER T WITH RETROFLEX HOOK, LATIN SMALL LETTER C, LATIN SMALL LETTER K <br>
Input the description of your second set of desired segments, separated by a comma ",":LATIN SMALL LETTER M, LATIN SMALL LETTER N, LATIN SMALL LETTER N WITH LEFT HOOK, LATIN SMALL LETTER ENG 
</p>
<p>
  After that, a set of results will be printed, each headed by the area it was looking at (Papuensia and Asutralia, Papunesia, Australia). <br>
  results is the number of languages that have both the first set of desired segments and the second set <br>
  results1 is the number of languages that have the first set of desired segments <br>
  results2 is the number of languages that have the second set of desired segments
</p>
<p>
  If you wish to know, how many languages have <b>only</b> the first set of desired segments, simply subtract results from results1.
</p>

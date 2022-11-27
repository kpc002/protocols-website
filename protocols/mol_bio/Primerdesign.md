---
title: Designing Primers
type: docs
weight: 11
---

# Designing Primers (not only for CRISPR Validation)

## For DNA

### PrimerBlast

1. Get chromosome location coordinates (using IDT cas9 primer design) 
2. Add 500-700 bp plus and minus into [mouse genome browser](https://genome.ucsc.edu/cgi-bin/hgc?hgsid=1316607377_phlcQ6g499hCETR4lIf1Fb9YKlaM&o=56694975&g=getDna&i=mixed&c=chr12&l=56694975&r=56714605&db=mm10&hgsid=1316607377_phlcQ6g499hCETR4lIf1Fb9YKlaM)
3. Copy and paste DNA sequence with info into NCBI primer blast 
    1. Change PCR product size min 800 to max 1200
    2. Change to "refseq representative genomes" under "Primer Pair Specificity Checking Parameters"
    3. For mouse change to "house mouse" 
    4. [NEB Tm calculator](https://tmcalculator.neb.com/#!/main) for Q5 and high-fidelity 2X master mix to check  melting point (because IDT not always accurate + enzyme dependent) 
4. **MAKE SURE TO COPY AND PASTE SEQUENCES INTO GOLDRATH DATABASE**
    1. Want primers with lowest self complementarity 
    2. Make sure it spans cut site
 
## For RNA: 

### PrimerBlast

1. Look up gene accession number 
2. Change exon junction span to "primer must span exon-exon junction" 
3. Change to "refseq mRNAs" under "Primer Pair Specificity Checking 
Parameters"
4. For mouse change to "house mouse" 
5. **MAKE SURE TO COPY AND PASTE SEQUENCES INTO GOLDRATH DATABASE**
    1. Want primers with lowest self complementarity 
    2. Make sure it spans exons (ideally more than 1) 
    3. If using new primers - make sure to check melting curves for one PCR product 


### PrimerBank

Alternatively you can use [PrimerBank](https://pga.mgh.harvard.edu/primerbank/) for predesigned primers. Just make sure, that they are exon spanning (if possible)

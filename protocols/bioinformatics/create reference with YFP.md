---
weight: 30
bookFlatSection: false
title: "Build cellranger reference with YFP"
---

# Create a mouse reference for cellranger with YFP

This script will create a mouse reference that includes YFP. The reference can be used to align single-cel# RNA-Seq samples using cellranger.
For a long explanation on how to build the mouse reference see here: https://support.10xgenomics.com/single-cell-gene-expression/software/release-notes/build#mm10_2020A.

## Prepare mouse fasta and GTF

First we need to download the fasta and GTF file and set some metadata for the refernce genome.


```bash
# Set metadata
genome="mm10-YFP"
version="2020-A"


# Set up source and build directories
build="scratch/mm10-2020-A_build_YFP"
mkdir -p "$build"


# Download source files if they do not exist in reference_sources/ folder
source="scratch/reference_sources"
mkdir -p "$source"


fasta_url="http://ftp.ensembl.org/pub/release-98/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna.primary_assembly.fa.gz"
fasta_in="${source}/Mus_musculus.GRCm38.dna.primary_assembly.fa"
gtf_url="http://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M23/gencode.vM23.primary_assembly.annotation.gtf.gz"
gtf_in="${source}/gencode.vM23.primary_assembly.annotation.gtf"


if [ ! -f "$gtf_in" ]; then
    curl -sS "$gtf_url" | zcat > "$gtf_in"
fi
if [ ! -f "$fasta_in" ]; then
    curl -sS "$fasta_url" | zcat > "$fasta_in"
fi
```


```bash
# Modify sequence headers in the Ensembl FASTA to match the file
# "GRCm38.primary_assembly.genome.fa" from GENCODE. Unplaced and unlocalized
# sequences such as "GL456210.1" have the same names in both versions.
#
# Input FASTA:
#   >1 dna:chromosome chromosome:GRCm38:1:1:195471971:1 REF
#
# Output FASTA:
#   >chr1 1
fasta_modified="$build/$(basename "$fasta_in").modified"
# sed commands:
# 1. Replace metadata after space with original contig name, as in GENCODE
# 2. Add "chr" to names of autosomes and sex chromosomes
# 3. Handle the mitochrondrial chromosome
cat "$fasta_in" \
    | sed -E 's/^>(\S+).*/>\1 \1/' \
    | sed -E 's/^>([0-9]+|[XY]) />chr\1 /' \
    | sed -E 's/^>MT />chrM /' \
    > "$fasta_modified"
```


```bash
# Remove version suffix from transcript, gene, and exon IDs in order to match
# previous Cell Ranger reference packages
#
# Input GTF:
#     ... gene_id "ENSMUSG00000102693.1"; ...
# Output GTF:
#     ... gene_id "ENSMUSG00000102693"; gene_version "1"; ...
gtf_modified="$build/$(basename "$gtf_in").modified"
# Pattern matches Ensembl gene, transcript, and exon IDs for human or mouse:
ID="(ENS(MUS)?[GTE][0-9]+)\.([0-9]+)"
cat "$gtf_in" \
    | sed -E 's/gene_id "'"$ID"'";/gene_id "\1"; gene_version "\3";/' \
    | sed -E 's/transcript_id "'"$ID"'";/transcript_id "\1"; transcript_version "\3";/' \
    | sed -E 's/exon_id "'"$ID"'";/exon_id "\1"; exon_version "\3";/' \
    > "$gtf_modified"
```



```bash
# Define string patterns for GTF tags
# NOTES:
# - Since GENCODE release 31/M22 (Ensembl 97), the "lincRNA" and "antisense"
#   biotypes are part of a more generic "lncRNA" biotype.
# - These filters are relevant only to GTF files from GENCODE. The GTFs from
#   Ensembl release 98 have the following differences:
#   - The names "gene_biotype" and "transcript_biotype" are used instead of
#     "gene_type" and "transcript_type".
#   - Readthrough transcripts are present but are not marked with the
#     "readthrough_transcript" tag.
BIOTYPE_PATTERN=\
"(protein_coding|lncRNA|\
IG_C_gene|IG_D_gene|IG_J_gene|IG_LV_gene|IG_V_gene|\
IG_V_pseudogene|IG_J_pseudogene|IG_C_pseudogene|\
TR_C_gene|TR_D_gene|TR_J_gene|TR_V_gene|\
TR_V_pseudogene|TR_J_pseudogene)"
GENE_PATTERN="gene_type \"${BIOTYPE_PATTERN}\""
TX_PATTERN="transcript_type \"${BIOTYPE_PATTERN}\""
READTHROUGH_PATTERN="tag \"readthrough_transcript\""
```



```bash
# Construct the gene ID allowlist. We filter the list of all transcripts
# based on these criteria:
#   - allowable gene_type (biotype)
#   - allowable transcript_type (biotype)
#   - no "readthrough_transcript" tag
# We then collect the list of gene IDs that have at least one associated
# transcript passing the filters.
cat "$gtf_modified" \
    | awk '$3 == "transcript"' \
    | grep -E "$GENE_PATTERN" \
    | grep -E "$TX_PATTERN" \
    | grep -Ev "$READTHROUGH_PATTERN" \
    | sed -E 's/.*(gene_id "[^"]+").*/\1/' \
    | sort \
    | uniq \
    > "${build}/gene_allowlist"
```




```bash
# Filter the GTF file based on the gene allowlist
gtf_filtered="${build}/$(basename "$gtf_in").filtered"
# Copy header lines beginning with "#"
grep -E "^#" "$gtf_modified" > "$gtf_filtered"
# Filter to the gene allowlist
grep -Ff "${build}/gene_allowlist" "$gtf_modified" \
    >> "$gtf_filtered"
```

## Add the YFP

Now, we can add our "custom" gene to the fasta and GTF file. I downloaded the YFP fasta from the internet. We can inpsect it using the `cat` command.  


```bash
cat YFP.fasta
```

    >YFP||720|<html><body>Topaz YFP, an enhanced yellow variant of GFP.</body></html>|linear
    ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAA
    GTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGC
    TGCCCGTGCCCTGGCCCACCCTCGTGACCACCTTCGGCTACGGCGTGCAGTGCTTCGCCCGCTACCCCGACCACATGCGC
    CAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTA
    CAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGG
    ACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAAC
    GGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACAC
    CCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCTACCAGTCCGCCCTGAGCAAAGACCCCAACG
    AGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAGTAA



There are special characters such as "|" and spaces in the header (all text after the >) of this FASTA sequence. These can be problematic for downstream applications. It can be helpful to change the header to be more informative and also to remove these characters. The following command opens the file and uses the stream editor (sed) function to search for a pattern (the original header), replace it with new text (YFP), then directs the output to a new output file, YFP.mod.fasta.

Also, you have to make sure, that the fasta file ends with an empty line. This is especially important if you are trying to add multiple genes to the reference (e.g. YFP and GFP). If the fasta file does not end with a new line, the >> command that we use later will create an output similar to `...ACAAGTA>eGFP...`. This is of course not correct (`>eGFP` needs to be at the start of a new line) and will result in an error when trying to create the reference genome.


```bash
cat YFP.fasta | sed s/\>.*$/\>YFP/ > YFP.mod.fasta
cat YFP.mod.fasta
```

    >YFP
    ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAA
    GTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGC
    TGCCCGTGCCCTGGCCCACCCTCGTGACCACCTTCGGCTACGGCGTGCAGTGCTTCGCCCGCTACCCCGACCACATGCGC
    CAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTA
    CAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGG
    ACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAAC
    GGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACAC
    CCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCTACCAGTCCGCCCTGAGCAAAGACCCCAACG
    AGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAGTAA



To find the number of bases in this sequence, we will use the `grep -v "^>"` command to search all lines that don't start with the `>` character, which removes line returns with `tr -d "\n"` so they aren't counted, and then counts the number of characters with the command `wc -c`. Each command is sent to the next step with the pipe "|" command.

The results of this command shows there are 720 bases. This is important to know for the next step.


```bash
cat YFP.mod.fasta | grep -v "^>" | tr -d "\n" | wc -c
```

    720
    



Now, make a custom GTF for GFP with the following command. This command uses the function echo -e (prints everything in quotes; the -e enables interpretation of the backslash, e.g. \t). Use \t to insert the tabs that separate the 9 columns of information required for GTF.


```bash
echo -e 'YFP\tunknown\texon\t1\t720\t.\t+\t.\tgene_id "YFP"; transcript_id "YFP"; gene_name "YFP"; gene_biotype "protein_coding";' > YFP.gtf
cat YFP.gtf
```

    YFP	unknown	exon	1	720	.	+	.	gene_id "YFP"; transcript_id "YFP"; gene_name "YFP"; gene_biotype "protein_coding";
    



Next, add the YFP..mod.fasta to the end of the genome FASTA. But first, make a copy so that the original is unchanged. Then, append the YFP.mod.fasta to the end of the reference fasta file. The >> means append. Note: Do not use >, which overwrites the original file.


```bash
fasta_modified_yfp="$fasta_modified.yfp"

cp $fasta_modified $fasta_modified_yfp
cat YFP.mod.fasta >> $fasta_modified_yfp
```





To confirm that the GFP entry was added to the FASTA file, use the grep ">" command to search for lines with the > character:


```bash
grep ">" $fasta_modified_yfp
```

    >chr1 1
    >chr10 10
    >chr11 11
    >chr12 12
    >chr13 13
    >chr14 14
    >chr15 15
    >chr16 16
    >chr17 17
    >chr18 18
    >chr19 19
    >chr2 2
    >chr3 3
    >chr4 4
    >chr5 5
    >chr6 6
    >chr7 7
    >chr8 8
    >chr9 9
    >chrM MT
    >chrX X
    >chrY Y
    >JH584299.1 JH584299.1
    ...
    >GL456368.1 GL456368.1
    >JH584292.1 JH584292.1
    >JH584295.1 JH584295.1
    >YFP
    



Now, we do the exact same thing for the GTF file. We copy the GTF to a new location and append the YFP GTF at the end. Finally, we use `tail` to see if it was added correctly.


```bash
gtf_filtered_yfp="$gtf_filtered.yfp"
cp $gtf_filtered $gtf_filtered_yfp
cat YFP.gtf >> $gtf_filtered_yfp
tail $gtf_filtered_yfp
```

    JH584304.1	ENSEMBL	exon	56986	57151	.	-	.	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 2; exon_id "ENSMUSE00001053862"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    JH584304.1	ENSEMBL	CDS	56986	57151	.	-	1	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 2; exon_id "ENSMUSE00001053862"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    JH584304.1	ENSEMBL	exon	55112	55701	.	-	.	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 3; exon_id "ENSMUSE00000986146"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    JH584304.1	ENSEMBL	CDS	55483	55701	.	-	0	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 3; exon_id "ENSMUSE00000986146"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    JH584304.1	ENSEMBL	stop_codon	55480	55482	.	-	0	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 3; exon_id "ENSMUSE00000986146"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    JH584304.1	ENSEMBL	exon	52691	54867	.	-	.	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 4; exon_id "ENSMUSE00001045433"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    JH584304.1	ENSEMBL	UTR	58617	59690	.	-	.	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 1; exon_id "ENSMUSE00001037709"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    JH584304.1	ENSEMBL	UTR	55112	55482	.	-	.	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 3; exon_id "ENSMUSE00000986146"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    JH584304.1	ENSEMBL	UTR	52691	54867	.	-	.	gene_id "ENSMUSG00000095041"; gene_version "7"; transcript_id "ENSMUST00000178343"; transcript_version "1"; gene_type "protein_coding"; gene_name "AC149090.1"; transcript_type "protein_coding"; transcript_name "AC149090.1-202"; exon_number 4; exon_id "ENSMUSE00001045433"; exon_version "1"; level 3; protein_id "ENSMUSP00000136649.1"; transcript_support_level "1"; tag "basic";
    YFP	unknown	exon	1	720	.	+	.	gene_id "YFP"; transcript_id "YFP"; gene_name "YFP"; gene_biotype "protein_coding";
    



We can now create the reference package using the Fasta File with YFP and the GTF file with YFP. Since I am running that on TSCC, I need to load cellranger first.


```bash
module load cellranger/6.0.0
```

    




```bash
# Create reference package
cellranger mkref --ref-version="$version" \
    --genome="$genome" --fasta="$fasta_modified_yfp" --genes="$gtf_filtered_yfp" \
    --nthreads 24
```

    ['/opt/cellranger-6.0.0/bin/rna/mkref', '--ref-version=2020-A', '--genome=mm10-YFP', '--fasta=scratch/mm10-2020-A_build_YFP/Mus_musculus.GRCm38.dna.primary_assembly.fa.modified.yfp', '--genes=scratch/mm10-2020-A_build_YFP/gencode.vM23.primary_assembly.annotation.gtf.filtered.yfp', '--nthreads', '24']
    Creating new reference folder at /path_to_folder/mm10-YFP
    ...done
    
    Writing genome FASTA file into reference folder...
    ...done
    
    Indexing genome FASTA file...
    ...done
    
    Writing genes GTF file into reference folder...
    ...done
    
    Generating STAR genome index (may take over 8 core hours for a 3Gb genome)...
    Sep 01 19:33:11 ..... started STAR run
    Sep 01 19:33:11 ... starting to generate Genome files
    Sep 01 19:34:15 ... starting to sort Suffix Array. This may take a long time...
    Sep 01 19:34:19 ... sorting Suffix Array chunks and saving them to disk...
    Sep 01 19:56:59 ... loading chunks from disk, packing SA...
    Sep 01 19:57:17 ... finished generating suffix array
    Sep 01 19:57:17 ... generating Suffix Array index
    Sep 01 19:58:56 ... completed Suffix Array index
    Sep 01 19:58:56 ..... processing annotations GTF
    Sep 01 19:59:10 ..... inserting junctions into the genome indices
    Sep 01 20:03:46 ... writing Genome to disk ...
    Sep 01 20:03:56 ... writing Suffix Array to disk ...
    Sep 01 20:04:36 ... writing SAindex to disk
    Sep 01 20:04:43 ..... finished successfully
    ...done.
    
    Writing genome metadata JSON file into reference folder...
    Computing hash of genome FASTA file...
    ...done
    
    Computing hash of genes GTF file...
    ...done
    
    ...done
    
    >>> Reference successfully created! <<<
    
    You can now specify this reference on the command line:
    cellranger --transcriptome=/path_to_folder/mm10-YFP ...
    





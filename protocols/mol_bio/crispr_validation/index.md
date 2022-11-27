---
weight: 3
title: "Crispr KO validation"
---

# Crispr KO validation by Sanger Sequencing

If it is not possible to validate the KO of a Crispr/Cas9 with Flow (or western), one  can check if a deletion was introduced on the genomic DNA of the cells.

For that you need:
## Materials
- At least 100.000 cells from your treated and control T cells
- Kit to isolate genomic DNA (e.g. [QIAamp DNA Blood Kits](https://www.qiagen.com/us/products/discovery-and-translational-research/dna-rna-purification/dna-purification/genomic-dna/qiaamp-dna-blood-kits/))
- Primers to ampliy the target region (see details below)
- High-Fidelity Polymerase (e.g. Q5)
- A PCR purification kit (e.g. [DNA Clean & Concentrator-5](https://www.zymoresearch.com/collections/dna-clean-concentrator-kits-dcc/products/dna-clean-concentrator-5))

## Primer design
You need to sequence a stretch of DNA ~700bp enclosing the designed editing site. The projected break site should be located preferably ~200bp downstream from the sequencing start site. This region upstream of the break site is used to align the sequencing data of the test sample with that of the control sample. 

I use use [CHOPCHOP](https://chopchop.cbu.uib.no/) to design these primers. Under "Options" -> "Primers" select a product size between 500 and 800bp and a minimal distance from primer to target site of 200bp.

{{< lightbox src="chopchop_options.png" caption="CHOPCHOP options" >}} 

Next, click "Find target sites" and select your guideRNA. Here you can select one of the suggestet primers.

{{< lightbox src="chopchop_results.png" caption="CHOPCHOP results" >}} 

## gnomicDNA Isolation

Follow the kit's instructions to isolate the gnomic DNA. I usually elute in 70-100ul ddH20. Next, measure the DNA concentration using the NanoDrop.

## PCR amplification

Next, we need to amplify the target site on the genomic DNA. Make a PCR for both control gDNA and gDNA from treated cells.

|           | Volume |
|-----------|--------|
| fwd Primer| 2.5µl (of 1:10 Dilition) |
| rev Primer| 2.5µl (of 1:10 Dilition) |
| Q5 Polymerase Mastermix 2x| 25µl |
| genomic DNA | 150-250 **ng** |
| H20| fill up to total volume of 50µl |

I usually run the touchdown PCR with the following setting

| Step |     Temperature      |  Time | 
|---|-----------|--------|
|    1   |   95°C   |   3 min   |
|    2   |    95°C  |   15 s   |
|    3   |    65°C  |    20 s (reduce -0.5°C / step)  |
|    4   |    72°C  |    35 s  |
|    5   |  Goto Step 2    |  14x    |
|    6   |    95°C  |   15 s   |
|    7   |    58°C  |    20 s  |
|    8   |    72°C  |    35 s  |
|    9   |  Goto Step 6    |  30x    |
|    10   |   72°C    |   5 min   |
|    11   |   4°C    |   ∞   |

After the PCR, load 10µl (add Loading Dye) on a agarose Gel and check is the PCR worked and has the correct size.

## PCR purification

Purify the PCR product addording to the kit's instructions.
Elute in 15µl **ddH20**

## Sequencing

Send both samples for sequencing. Use either the forward or the reverse primer as sequencing primer.

## TIDE

Using the [TIDE](http://shinyapps.datacurators.nl/tide/) website, we can calcuate the KO efficiency.

Upload the sequencing file (ab1) for both control and test sample. Enter you guide sequence and click "Update View". You might need to manually adjust the "Decomposition window (bp)" in "Advanced settings" (as shown in the example)


{{< lightbox src="tide.png" caption="TIDE: 73.6% overall efficiency" >}} 

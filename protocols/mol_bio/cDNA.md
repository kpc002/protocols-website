---
order: 2
title: "cDNA Synthesis"
author: Maximilian Heeg
date: last-modified
description: 
  Get lymphocytes from an lymphnode
image: dna.svg
---

# cDNA Synthesis

## Remove DNA contamination

-   Add 1ul of 10X TURBO DNase Buffer and 0.5µl TURBO DNase to 10 µl of RNA, and mix gently
-   Incubate at 37°C for 20-30 min
-   Add resuspended Inactivation Reagent (2µl to 11.5 µl mix), and mix well
-   Incubate 5 min at RT, mixing occasionally
-   Centrifuge at 10000 x g for 1.5 min and transfer the RNA to a fresh tube

## cDNA preparation using SuperScript IV

::: callout-tip
This protocol uses the new superscript IV. The "old" protocol for the superscript II can be found below.
:::

### Anneal primer to template RNA

-   Mix:

    | Component                                                                                  | Volume      |
    |--------------------------------------------------------------------------------------------|-------------|
    | 50 μM Oligo d(T)20 primer, **50 μM random hexamers**, or 2 μM gene-specific reverse primer | 1 μL        |
    | 10 mM dNTP mix (10 mM each)                                                                | 1 μL        |
    | Template RNA (10 pg--5 μg total RNA or 10 pg--500 ng mRNA)                                 | up to 11 μL |
    | DEPC-treated or nuclease-free water                                                        | to 13 μL    |

-   Heat the RNA-primer mix at 65°C for 5 minutes, and then incubate on ice for at least 1 minute

### Prepare RT reaction mix

-   Vortex and briefly centrifuge the 5× SSIV Buffer.

-   Combine the following components in a reaction tube.

    | Component                                        | Volume |
    |--------------------------------------------------|--------|
    | 5× SSIV Buffer                                   | 4 μL   |
    | 100 mM DTT                                       | 1 μL   |
    | RNaseOUT™ Recombinant RNase Inhibitor            | 1 μL   |
    | SuperScript® IV Reverse Transcriptase (200 U/μL) | 1 μL   |

### Combine annealed RNA and RT reaction mix

-   Add 7µl RT reaction mix to the annealed RNA (13 µl)

### Incubate reactions

-   If using random hexamer, incubate the combined reaction mixture at 23°C for 10 minutes, and then proceed to next step.\
    If using oligo d(T)20 or gene-specific primer, directly proceed to next step.
-   Incubate the combined reaction mixture at 50--55°C for 10 minutes.
-   Inactivate the reaction by incubating it at 80°C for 10 minutes

### Remove RNA

-   To remove RNA, add 1 μL E. coli RNase H, and incubate 37°C for 20 minutes.

## Older versions

::: {.callout-note collapse="true"}
## cDNA preparation using SuperScript II

-   Mix 9 μl RNA, 1μl dNTP, 1μl random hexamer (50 ng/ul).

    ::: callout-tip
    If you want to make cDNA for cloning, use oligo(dT) primer to get full length cDNA transcripts.
    :::

-   Incubate at 65C for 5min.

-   Prepare 2X reaction mix in order -- Make MasterMix

    -   10x RT buffer -- 2 μl
    -   25 mM MgCl2 -- 4 μl
    -   0.1 M DTT -- 2 μl
    -   RNase out -- 1μl

-   Add 2X reaction to RNA.

-   Incubate at RT for 2 minutes.

-   Add 1μl superscript II to each tube.

-   PCR program:

    -   RT 10 min
    -   42°C 50 min
    -   70°C 15 min

-   Chill on ice.

-   Add 1 μl RNAse H and incubate 37°C 20 min.
:::

---
title: "RetroProduction_Immunity"
description: "Retroviral production protocol for immune cell transduction."
order: 10
author: "Goldrath Lab"
date: last-modified
---

[Download the original PDF](RetroProduction_Immunity.pdf){.btn .btn-primary download="RetroProduction_Immunity.pdf"}



# RetroProduction_Immunity

Immunity

Resource

In Vivo RNA Interference Screens
Identify Regulators of Antiviral
CD4+ and CD8+ T Cell Differentiation
Runqiang Chen,1,2,3,5 Simon Bélanger,2,5 Megan A. Frederick,3 Bin Li,2 Robert J. Johnston,2 Nengming Xiao,4
Yun-Cai Liu,4 Sonia Sharma,4 Bjoern Peters,2 Anjana Rao,1 Shane Crotty,2,* and Matthew E. Pipkin3,*
1Division of Signaling and Gene Expression, La Jolla Institute for Allergy and Immunology, La Jolla, CA 92037, USA
2Division of Vaccine Discovery, La Jolla Institute for Allergy and Immunology, La Jolla, CA 92037, USA
3Department of Cancer Biology, The Scripps Research Institute, Jupiter, FL 33458, USA
4Division of Cell Biology, La Jolla Institute for Allergy and Immunology, La Jolla, CA 92037, USA
5Co-first author

*Correspondence: shane@lji.org (S.C.), mpipkin@scripps.edu (M.E.P.)
http://dx.doi.org/10.1016/j.immuni.2014.08.002




SUMMARY                                                                gene expression in different cell types and tissues found that a
                                                                       given murine cell type could be distinguished from other cell
Classical genetic approaches to examine the re-                        types by a network of approximately six TF:TF interactions and
quirements of genes for T cell differentiation during                  that these TF networks were conserved in human cell types (Rav-
infection are time consuming. Here we developed a                      asi et al., 2010). Thus, the intersecting expression and actions of
pooled approach to screen 30–100+ genes individu-                      multiple TFs appear to determine cell fate and function. Recent
ally in separate antigen-specific T cells during infec-                work on T helper 17 (Th17) cell differentiation suggests that
                                                                       this model also applies to T cells (Ciofani et al., 2012).
tion using short hairpin RNAs in a microRNA context
                                                                          The differentiation of naive CD8+ T cells into CTLs is a key pro-
(shRNAmir). Independent screens using T cell recep-
                                                                       cess in immunity to viral infections. The differential development
tor (TCR)-transgenic CD4+ and CD8+ T cells respond-                    of short-lived effector CTLs and precursors to long-lived memory
ing to lymphocytic choriomeningitis virus (LCMV)                       CTLs are considered alternative cellular ‘‘fates’’ (Chang et al.,
identified multiple genes that regulated development                   2007; Joshi et al., 2007), and understanding this process is crit-
of follicular helper (Tfh) and T helper 1 (Th1) cells,                 ical for prevention and treatment of acute and chronic infections
and short-lived effector and memory precursor cyto-                    (Doering et al., 2012; Haining and Wherry, 2010; Kaech and Cui,
toxic T lymphocytes (CTLs). Both screens revealed                      2012). Activated CD4+ T cells can differentiate into a range of
roles for the positive transcription elongation factor                 different functional subsets, including Th1, Th2, Th17, peripheral
(P-TEFb) component Cyclin T1 (Ccnt1). Inhibiting                       Treg (pTreg), and follicular helper (Tfh) cells, which each have
expression of Cyclin T1, or its catalytic partner                      potent capacities to regulate immune responses and eliminate
                                                                       pathogens. Among CD4+ T cells, follicular T helper cells (Tfh)
Cdk9, impaired development of Th1 cells and protec-
                                                                       are the specialized providers of help to B cells (Crotty, 2011).
tive short-lived effector CTL and enhanced Tfh cell
                                                                       T-cell-dependent antibody responses are important for protec-
and memory precursor CTL formation in vivo. This                       tion against a wide range of pathogens. Our understanding of
pooled shRNA screening approach should have util-                      Tfh cells is still in the early stages, and there is much to be
ity in numerous immunological studies.                                 learned about the pathways that control Tfh cell differentiation.
                                                                          A number of excellent studies have characterized the mRNA
                                                                       expression profiles of CD8+ and CD4+ T cells isolated ex vivo
INTRODUCTION                                                           during the course of antigen-specific responses (Best et al.,
                                                                       2013; Doering et al., 2012; Kaech and Cui, 2012; Kalia et al.,
The differentiation of T cells into effector and memory cells is       2010; Choi et al., 2013). However, differential mRNA expression
central to adaptive immunity. Transcription factors (TFs) are cen-     studies are likely to overlook a large number of relevant factors
tral regulators of these differentiation processes. Although most      responsible for T cell differentiation. For example, of nearly
current models of T cell differentiation incorporate relatively few    2,000 predicted conventional DNA-binding transcription factors
regulatory players and rely heavily on the ‘‘master regulator’’        in the murine genome (Gray et al., 2004), fewer than 15 have vali-
concept, it is abundantly clear that TFs do not act in isolation       dated roles in effector CD8+ T cell differentiation (Kaech and Cui,
and that transcription programs that underlie cell differentiation     2012; Pipkin and Rao, 2009). The same limitations probably hold
require the concerted actions of multiple factors, including           for Tfh cell differentiation and other CD4+ T cell differentiation
important inducers or repressors of T cell differentiation path-       pathways (Crotty, 2012; Oestreich and Weinmann, 2012; Vahedi
ways (Crotty, 2012; Kaech and Cui, 2012; O’Shea and Paul,              et al., 2013). Thus, a functional genetic approach in which inhibi-
2010; Oestreich and Weinmann, 2012; Pipkin and Rao, 2009;              tion of a large number of genes individually, in separate cells in
Walsh et al., 2002). One large-scale study of the regulation of        parallel, during T cell differentiation has the potential to rapidly

                                                                         Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc. 325

                                                                                                                                Immunity
                                                                                                            +            +
                                                                                RNA Interference CD8 and CD4 T Cell Screens




identify factors comprising the genetic networks underlying            format to produce arrays of high-titer RV supernatants without
T cell function.                                                       concentration, sufficient to transduce R70% of LCMV-specific
   To pursue this objective, we have devised an experimental           P14 TCR transgenic CD8+ T cells 18 hr after TCR stimulation
approach that uses retroviral shRNAmir libraries to diminish           (Figures 1B, S2A, and S2B). The day after transduction, cells
the expression of selected gene products one at a time in anti-        from each well were pooled (Figure 1B, day 0) and immediately
gen-specific T cells. Gene function in antiviral responses is          transferred to recipient mice without cell sorting (sorting reduced
then interrogated in pooled screens in mice. We have demon-            P14 accumulation in vivo; Figure S2C), and the recipients were
strated the utility of this approach in two T cell differentiation     infected with LCMV 1 hr later. In addition, an aliquot of Ame-
processes in vivo: CD8+ T cell differentiation into cytotoxic          trine-high cells was FACS purified and saved as the ‘‘input.’’
T lymphocytes (CTLs) and CD4+ T cell differentiation into Tfh             Genomic DNA was prepared from the input and samples of
and Th1 cells. Here we showed proof of principle that the roles        P14 cells isolated by flow cytometry on day 7 after LCMV infec-
of multiple genes can be interrogated in parallel in T cells during    tion. Deep sequencing was used to quantify shRNA representa-
infection and identified previously unappreciated factors that         tion (Figures 1A and S2D–S2H) in libraries generated from a
were involved in these differentiation processes. This approach        single-step PCR of the shRNAmir sequences in genomic DNA
holds promise to substantially accelerate the understanding of         template (Figures 1B and 1C). Multiple PCR conditions were
T cell differentiation in vivo.                                        interrogated (Figures S2D–S2G). Independent libraries gener-
                                                                       ated from different DNA template amounts at low PCR cycles
RESULTS                                                                (22 or 26 cycles; Figures S2F and S2G) exhibited high correla-
                                                                       tions in shRNA representation, with both 314 (medium-density)
An Optimized Retroviral Vector to Express shRNAmirs                    and 318 (high-density) PGM sequencing chips (Figure S2H).
In Vivo                                                                Thus, the sequencing approach was robust.
Transduction of activated T cells with murine stem cell virus             To establish conditions for screening pools of shRNAmir-RV+
(MSCV)-based retroviral expression vectors (RVs) has previously        P14 CD8+ T cells in the context of infection, numerous factors
been used to drive transgene expression or to deplete expres-          were optimized and standardized (Figure S3). Naive Thy1.1+
sion of endogenous genes by triggering RNA interference                Blimp1-YFP transgenic P14 cells were activated in vitro and
(RNAi) using shRNAs upon adoptive transfer in vivo (Araki              transferred to B6 hosts subjected to LCMV infection and the
et al., 2009; Johnston et al., 2009; Joshi et al., 2007; Kao et al.,   P14 cells were examined as a function of (1) cell transfer number
2011). However, we found that transduction of SMARTA TCR               (Figure S3A), (2) the timing of the infection relative to cell transfer
transgenic CD4 T cells (LCMV-specific, gp66-77 IAb restricted)         (data not shown), (3) LCMV dose (Figure S3B), and (4) LCMV
with an MSCV-based (pLMP-derived) RV designed to express               strain (Figure S3C). Transfer of 500,000 activated P14 cells
shRNAs in the context of miRNA-30 sequences (shRNAmir) re-             followed by intraperitoneal (i.p.) infection with 1.5 3 105 PFU of
sulted in depletion of the transduced cells after an acute LCMV        LCMV-clone 13 (LCMV-cl13) resulted in a robust infection that
infection (Figure S1A, left, available online). This most likely       induced accumulation of 106 P14 cells in the spleen by day
was due to immune rejection of antigens expressed from                 7, 50-fold more than in uninfected recipients (Figures 1D and
pLMP (Figure S1B), because deletion of the puromycin resis-            S3D). Under these conditions virus replication was strongly
tance gene from pLMP (LMPd) eliminated this effect (Figure S1A,        inhibited (see below), and the responding P14 cells exhibited
right). We replaced GFP in LMPd with the violet-excitable, yel-        CD8+ T cell phenotypes typical of acute infection, based on inter-
low-fluorescing GFP variant Ametrine1.1 (LMP-Amt) to expand            leukin-2 receptor a (IL-2Ra) (CD25), KLRG-1, IL-7Ra (CD127),
its utility in FACS (Figures S1B and S1C) and confirmed its            and Blimp1-YFP reporter expression (Figures 1E, 1F, and S4A).
functionality for RNAi in vivo by targeting Bcl6 transcripts. Trans-   LCMV-cl13 is more virulent than LCMV Armstrong (Wherry
ferred SMARTA CD4+ T cells transduced with Bcl6-specific               et al., 2003) but was controlled due to the P14 cell transfers. In
shRNAs (LMP-Amt shBcl6-RV, referred to hereafter as shBcl6-            addition, we confirmed that short-lived effector (KLRG-1hiIL-
RV) displayed a reduced fraction of CXCR5+Bcl6+ cells upon             7Ralo) and memory precursor (KLRG-1loIL-7Rahi) P14 popula-
LCMV infection, consistent with a requirement for Bcl6 for differ-     tions exhibited different potentials for memory cell formation
entiation of follicular T helper cells (Tfh) (Figure S1D).             and ‘‘recall’’ capacity (Figures S4B–S5E). Altogether, these
                                                                       results demonstrate robust conditions with which to screen
A Pooled Screening System using shRNAs in CD8+ T                       effector and memory CTL development.
Cells during LCMV Infection                                               The number of distinct shRNAmirs that could be tested in par-
We parallelized the shRNAmir-RV approach in order to inter-            allel was constrained by the number of adoptively transferred
rogate the functions of numerous genes simultaneously. The             T cells. In order to ensure library complexity, we aimed to repre-
experimental strategy was to introduce a pool of TCR transgenic        sent each shRNA with 500 cells per mouse upon engraftment.
T cells carrying individual shRNAs into host mice and assay alter-     This depth of representation is similar to or exceeds recent in vivo
ations in the composition of shRNAs carried by the responding          shRNA-based screens (Beronja et al., 2013; Zhou et al., 2014;
T cells during a viral infection (Figure 1A). In effect, each T cell   Zuber et al., 2011). Based on data from adoptively transferred
is barcoded by the integrated shRNA-RV, and the fate of individ-       naive CD8+ T cells (Badovinac et al., 2007) and activated CD8+
ual cells carrying each shRNA can be monitored in T cell popu-         T cells (Pipkin et al., 2010), we assumed that 10% of trans-
lations of interest by deep sequencing DNA libraries derived           ferred cells would engraft. Thus, we initially analyzed a pool of
from the integrated provirus (Figures 1B and 1C; Beronja et al.,       500,000 cells representing 100 unique shRNAs in a single
2013; Zuber et al., 2011). We optimized conditions in 96-well          experiment. We also considered the recovery of effector and

326 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc.

Immunity
RNA Interference CD8+ and CD4+ T Cell Screens




A                                                                                  shGeneX            B                   Day
                                                                        Effector                                                            Seed PLAT-E in
shGeneX                                                                            shGeneY
                                                                                                       Seed PLAT-E        -5                a 96 well plate
      Transfer into B6 mice
                                                                 Day7                                                                       Transfect 1 shRNAmir
                                             LCMV infection                                             Transfection      -4                      vector/well
shGeneY                                                                            shGeneX
                                                                      Memory
                                                                     Precursor
                                                                                   shGeneY

D                                                                                                                                                                                              Days -2:
                                                                                                      CD3, CD28 stim. -2                     Seed CD8+ T cells in two
     Total P14 cells / Spleen (10 )




                                      100              Uninfected                                                                                                                         Harvest shRNA-RV,
    5




                                                       LCMV                                           P14 CD8+ T cells                      96 well plates (avoid edges)
                                                                                                                                                                                             store at 4°C
                                       10
                                                                                                       Transduction
                                                                                                        (18 hr after  -1                            Transduce CD8+:                                                   5x105 P14 cells
                                        1                                                                                                           1 shRNA-RV/well
                                                                                                      CD3, CD28 stim)
                                                                                                                                                                                                                      1.5x105 PFU LCMV
                                      0.10
                                                                                                      Transfer,
                                                                                                   LCMV infection
                                                                                                                           0
                                      0.01
                                                 4        5            6           7              and DNA isolation
                                                     Days Post Infection                                                                                            Pool CD8+ T cells
E                                                                                                                                                                         “Input”
                                      100                Blimp1-YFP
      Blimp1-YFP high (%)




                                       80
                                                                                                                                                                                                    FACS
                                       60
                                                                                                            Sort
                                                                                                      Eff and Mem cell
                                       40                                                             for DNA isolation    7                                                                                    Ion Torrent
                                                                                                                                 Ametrine




                                                                                                                                                                         KLRG-1
                                       20                                                                                                     87%                                                             deep sequencing
                                        0                                                                                                                                                2x106 cells/mouse
                                                                                                                                                                                                                     shRNA (Eff)
                                                4         5          6             7
                                      100
                                                              CD25                                                                                                                       1x105 cells/mouse      shRNA (Mem)
                                       80
          CD25 high (%)




                                       60
                                                                                                                                                     CD8                           IL-7Rα
                                       40                                                    C
                                                                                                         Library preparation:
                                       20                                                                                                                                                         Alignment of Reads and Quantitation
                                                                                             PCR with primers specific for miR30 and loop                       Ion Torrent Sequencing
                                                                                                                                                                                                        of shRNA Representation
                                        0
                                                                                                      Mir30     Passenger        Loop            Guide           Mir30
                                                4         5            6           7
                                      100
                                                           KLRG -1                           F                 Day 4                         Day 5                       Day 6                     Day 7
                                       80
           KLRG -1 high (%)




                                                                                                        1.2                0.9      1.9                   1.1     2.9              0.5     1.9                0.5
                                       60

                                       40
                                                                                                                                                                                                                      No Inf.
                                       20
                                                                                             KLRG-1




                                        0
                                                                                                        14.2              83.7      12.3                 84.7     8.4             88.2     5.3               92.3
                                                4        5          6          7
                                      100                     IL-7Rα                                    18.4               5.6      31.4                  2.1     37.8             2.8     62.1                4.9
                                       80
    IL-7Rα high (%)




                                       60
                                                                                                                                                                                                                      LCMV
                                       40

                                       20
                                                                                                        71.4               4.6     64.1                   2.4     56.6             2.8     29.3                3.7
                                        0
                                                4     5       6      7                                                                                    IL-7Rα
                                                 Days Post Infection


Figure 1. Optimization of Conditions for a Pooled Screening Approach using shRNAmirs in CD8+ T Cells In Vivo to Identify Genes that
Regulate CTL Differentiation during Infection
(A) A conceptual representation depicting the principle of the pooled screening strategy.
(B) Scheme for the shRNAmir screen using P14 cells and LCMV infection.
(C) Scheme for quantifying shRNAmirs. DNA libraries generated by PCR of the integrated shRNAmir provirus are analyzed by deep sequencing to quantify shRNA
representation in the cell subsets.
(D) Total P14 cell numbers recovered in the spleen in the presence or absence of LCMV infection. Error bars indicate standard deviations.
(E) Blimp1-YFPhi, CD25hi, KLRG-1hi, and IL-7Rahi cell frequencies at the indicated time points after infection. Symbols represent values from individual mice. Red
indicates LCMV-infected mice; black indicates uninfected mice.
(F) Representative flow cytometry plots of KLRG-1 and IL-7Ra staining on P14 cells under conditions used for screening.




                                                                                                                                                    Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc. 327

                                                                                                                                                                                                                                                                                                                                                                                                                                                          Immunity
                                                                                                                                                                                                                                                                                                                                                      +                         +
                                                                                                                                                                                                            RNA Interference CD8 and CD4 T Cell Screens




A 16                                                           shCon
                                                               shId3
                                                                                                                                                                                          B                                                                                                                                                                            6

                                              14               shId2
                                                               shPrdm1                                                                                                                                                                                                                                                                                                 4




                                                                                                                                                                                           Log2 ratio memory precursor:input
      Memory precursor / effector (Z score)




                                              12               shFosb
                                                                                                                                                                                                                                                                                                                                                                       2
                                                               shTbx21                                                                                   shTbx21.2
                                              10               shSmarca1                                                                                shTbx21.3
                                                               shNfatc3                                                                                                                                                        -16                    -14         -12                             -10        -8        -6                         -4            -2              2                                           4                              6
                                               8                                                                                                    shCcnt1.2
                                                               shKlf2
                                                                                                                                                  shCcnt1.4                                                                                                                                                                                                            -2
                                                               shCcnt1
                                               6                                                                                                shCcnt1.1
                                                               shKlf12
                                                                                                                                              shCcnt1.3                                                                                                                                                                                                                -4
                                               4
                                                                                                                                                                                                                                                                                                                                                                       -6
                                               2
                                                                                                                                                                                                                                                                                                                                                                       -8
                                               0
                                                                                                                  shTbx21.1                                                                                                                                                                                                                                           -10
                                               -2                                                            shId3.2

                                               -4                                                                                                                                                                                                                                                                                                                     -12


                                               -6                                  shId3.1                                                                                                                                                                                                                                                                            -14
                                                                                 shId3.3
                                               -8                                                                                                                                                                                                                                                                                                                     -16
                                                                                                                                                                                                                                                            Log2 ratio short-lived effector:input
                                              -10


C                                                                                         D                                                                                                                                                                 E                                                                                                                                                                         shTbx21.2
                                    1.5                                                                                                                                                                                                                                                     1.5              ****                                                                                                                        shCon
                                                                    *                                        shTbx21.1                            shTbx21.2                     shTbx21.3                                                                                                                 ****




                                                                                                                                                                                                                                                             T-bet expression, normalized
Tbx21 mRNA, normalized




                                                               **                                                                                                                                                                                                                                       ****
                                                                                                                                                                                         shTbx21
                                    1.0                                                                                                                                                    shCon                                                                                            1.0




                                                                                                                                                                                                                                                                                                                                                          Max (%)
                                                                                          Max (%)




                                    0.5                                                                                                                                                                                                                                                     0.5



                                    0.0                                                                                                                                                                                                                                                     0.0
                                                                                                                                                                                                                                                                                                                                                                             T-bet MFI




                                                                                                                                                                                                                                                                                                             1

                                                                                                                                                                                                                                                                                                                       2

                                                                                                                                                                                                                                                                                                                                                 3
                                                                                                                                                                                                                                                                                                  on

                                                                                                                                                                                                                                                                                                         1.

                                                                                                                                                                                                                                                                                                                   1.

                                                                                                                                                                                                                                                                                                                                    1.
                                                               1

                                                                        2

                                                                                 3
                                                on




                                                                    1.

                                                                             1.
                                                             1.




                                                                                                                                                    IFN-γ
                                                                                                                                                                                                                                                                                              C
                                                                                                                                                                                                                                                                                                        x2

                                                                                                                                                                                                                                                                                                                  x2

                                                                                                                                                                                                                                                                                                                        x2
                                                          x2

                                                                   x2

                                                                            x2




                                                                                                                                                                                                                                                                                             sh
                                               C




                                                                                                                                                                                                                                                                                                   Tb

                                                                                                                                                                                                                                                                                                             Tb

                                                                                                                                                                                                                                                                                                                       Tb
                                      sh

                                                        Tb

                                                               Tb

                                                                        Tb




                                                                                                                                                                                                                                                                                                  sh

                                                                                                                                                                                                                                                                                                         sh

                                                                                                                                                                                                                                                                                                                   sh
                                                    sh

                                                             sh

                                                                    sh




F                                                                                                                                                                                                                               G                                                                                          H                                                                                                  I
                                                                shCon                                 shTbx21.1                             shTbx21.2                     shTbx21.3                                                          100                                              ****                                                                    ****                                                                                       ****
                                                                                                                                                                                                                                                                                            ****                                                 60                 ****                                                                              5        ****




                                                                                                                                                                                                                                                                                                                                                                                                                     Memory precursor/Effector cell
                                                    76                               13        76                        7         33                       11    33                      18
                                                                                                                                                                                                                                                      80
                                                                                                                                                                                                                                 KLRG-1+IL-7Rα- (%)




                                                                                                                                                                                                                                                                                                                            KLRG-1-IL-7Rα+ (%)                                                                                                        4
 KLRG-1




                                                                                                                                                                                                                                                      60                                                                                         40
                                                                                                                                                                                                                                                                                                                                                                                                                                                      3

                                                                                                                                                                                                                                                      40                                                                                                                                                                                              2
                                                                                                                                                                                                                                                                                                                                                 20
                                                                                                                                                                                                                                                      20                                                                                                                                                                                              1
                                                    5                                 6        11                        6         20                       36    12                      37
                                                                                                                                                                                                                                                      0                                                                                          0                                                                                                    0
                                                                                                                             IL-7Rα
                                                                                                                                                                                                                                                         Tb . 1

                                                                                                                                                                                                                                                         Tb . 2

                                                                                                                                                                                                                                                                  3
                                                                                                                                                                                                                                                         Tb n




                                                                                                                                                                                                                                                                                                                                                                                                                                                Tb . 1

                                                                                                                                                                                                                                                                                                                                                                                                                                                Tb . 2

                                                                                                                                                                                                                                                                                                                                                                                                                                                         3
                                                                                                                                                                                                                                                                                                                                                    Tb . 1

                                                                                                                                                                                                                                                                                                                                                    Tb .2

                                                                                                                                                                                                                                                                                                                                                            3




                                                                                                                                                                                                                                                                                                                                                                                                                                                Tb n
                                                                                                                                                                                                                                                                                                                                                    Tb n
                                                                                                                                                                                                                                                               1.
                                                                                                                                                                                                                                                       sh h C o




                                                                                                                                                                                                                                                                                                                                                                                                                                                      1.
                                                                                                                                                                                                                                                                                                                                                         1.




                                                                                                                                                                                                                                                                                                                                                                                                                                              sh h C o
                                                                                                                                                                                                                                                                                                                                                  sh C o
                                                                                                                                                                                                                                                       sh x21

                                                                                                                                                                                                                                                       sh x21




                                                                                                                                                                                                                                                                                                                                                                                                                                              sh x 2 1

                                                                                                                                                                                                                                                                                                                                                                                                                                              sh x 2 1
                                                                                                                                                                                                                                                                                                                                                  sh x21

                                                                                                                                                                                                                                                                                                                                                  sh x21
                                                                                                                                                                                                                                                            x2




                                                                                                                                                                                                                                                                                                                                                                                                                                                   x2
                                                                                                                                                                                                                                                                                                                                                      x2
                                                                                                                                                                                                                                                                                                                                                 sh
                                                                                                                                                                                                                                                          s




                                                                                                                                                                                                                                                                                                                                                                                                                                                 s

J                                                                                                    K          5’ UTR                                                                                                                                                                                                                           3’ UTR
                                                                                                                                                                                                                                                                                                                                                                                M
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   *
                                                          sh rdm .1
                                                          sh dm 2
                                                            Pr 1.3

                                                                   4
                                                                 .

                                                                1.




                                                                                                                         1     2        3                             4              5                                                                                                                            67                              8
                                                                                                                                                                                                                                                                                                                                                                                                                                                               *
                                                            P 1
                                                            Pr 1
                                                          sh dm



                                                              dm
                                                          sh n




                                                                                                                                                                                                                                                                                                                                                                                    Memory precursor/Effector cell




                                                                                                                                                                                                                                                                                                                                                                                                                                                          **
                                                             o




                                                                                                                                                                                                                                                                                                                                                                                                                     3
                                                            Pr
                                                            C




                                                    1.2
                                                          sh




                                                                                                                               shPrdm1.2                                                                                                                                                      shPrdm1.3 shPrdm1.1 shPrdm1.4
                                                                                                     L              shCon                          shPrdm1.1                   shPrdm1.2                                                                   shPrdm1.3                                                                       shPrdm1.4
 Prdm1 mRNA,
   normalized




                                                    0.8                                                                                                                                                                                                                                                                                                                                                              2
                                                                                                              58                    2        13                  5        39                                  5                           25                                                              7        26                                                       3

                                                    0.4
                                                                                                    KLRG-1




                                                                                                                                                                                                                                                                                                                                                                                                                     1


                                                    0.0
                                                                                     Blimp1                                                                                                                                                                                                                                                                                                                          0
 Protein




                                                                                                              38                    2        57                  25       48                                  8                           47                                                            21         60                                                   11
                                                                                                                                                                                                                                                                                                                                                                                               Pr 1 . 1

                                                                                                                                                                                                                                                                                                                                                                                             sh r d m 2
                                                                                                                                                                                                                                                                                                                                                                                                  dm 3
                                                                                                                                                                                                                                                                                                                                                                                                        4
                                                                                                                                                                                                                                                                                                                                                                                                       n

                                                                                                                                                                                                                                                                                                                                                                                               P 1.
                                                                                                                                                                                                                                                                                                                                                                                               Pr 1 .
                                                                                                                                                                                                                                                                                                                                                                                                     1.
                                                                                                                                                                                                                                                                                                                                                                                               Pr o




                                                                                     β-Actin
                                                                                                                                                                                                                                                                                                                                                                                             sh s h C
                                                                                                                                                                                                                                                                                                                                                                                             sh d m
                                                                                                                                                                                                                                                                                                                                                                                             sh md




                                                                                                                                                                                IL-7Rα


Figure 2. A Pooled RNAi Screen in CD8+ T Cells In Vivo Identifies Potential Regulators of Effector and Memory Precursor CTL Formation
(A) Relative enrichment of shRNAs in memory precursor and short-lived effector P14 cell populations is reported as Z-scores for each shRNA in the library. Each
bar represents a single shRNA. Negative control shRNAs are colored yellow.
(B) Scatter plot shows the log2 ratio of normalized reads of all shRNAs in each sorted CD8+ T cell subset versus the input sample. Each dot represents a unique
shRNA and is color coded as in (A).
(C) Tbx21 mRNA expression in shTbx21+ P14 CD8+ T cells, after 6 days of culture (10 U/ml IL-2). Abbreviation is as follows: shCon, control shRNAmir.
(D) Intracellular IFN-g staining in P14 CD8+ T cells, gated on shTbx21+ cells. Cells were cultured for 6 days (10 U/ml IL-2) and restimulated with PMA and ion-
omycin for 4 hr before staining.
(E) T-bet expression in shTbx21+ P14 CD8+ T cells from spleens 8 days after LCMV infection (normalized geometric MFI). T-bet staining is shown for repre-
sentative mice (right).
(F) Contour plots show KLRG-1 and IL-7Ra staining on shTbx21+ P14 CD8+ T cells from representative mice 8 days after LCMV infection.

                                                                                                                                                                                                                                                                                                                                                                (legend continued on next page)
328 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc.

Immunity
RNA Interference CD8+ and CD4+ T Cell Screens




memory precursor populations. Based on P14 accumulation                       in both short-lived effector and memory precursor P14 cell sub-
data at day 7 postinfection (Figure 1D), we expected to recover               sets relative to input, suggesting that genes they affected were
300,000 KLRG-1hiIL-7Ralo and 30,000 KLRG-1loIL-7Rahi                        required for the accumulation of P14 T cells during infection
cells per mouse. To assure that cell numbers would not limit                  (Figure 2B).
library complexity at the end of the experiment and to reduce                     To focus on factors with differential effects on short-lived
potential founder effects from variation in individual mice (Zuber            effector versus memory precursor CD8+ T cell subsets, we iden-
et al., 2011), sorted cells were pooled from five or more infected            tified genes for which two or more cognate shRNAs were
mice in each experiment.                                                      enriched with Z-score values of Rj3.0j and classified these as
                                                                              hits. None of the negative control genes exhibited this pattern
Identification of Genes Underlying CTL Differentiation                        (Figure 2A and Table S1). Genes that met these criteria were
by an shRNA Screen In Vivo                                                    identified in both effector and memory precursor subsets (Fig-
We selected 34 genes to screen to test the approach. These                    ure 2A and Table S1). As expected from studies with gene-defi-
included genes differentially expressed in Tfh cells and CTLs                 cient mice (Cannarile et al., 2006; Intlekofer et al., 2005; Joshi
(Choi et al., 2013), broadly expressed chromatin and tran-                    et al., 2007; Yang et al., 2011), Tbx21 (T-bet)- and Id2-specific
scriptional regulators with unknown roles in effector T cells,                shRNAs were enriched in memory precursor cells, because
and multiple positive and negative control genes. Each gene                   these genes are necessary for effector CTL generation (Figure 2A
was targeted by 1–5 shRNAmirs, depending on availability in                   and Table S1). Conversely, all three Id3-specific shRNAs were
the original library (see Experimental Procedures and Table                   enriched in effector CTLs (Figure 2A and Table S1), but just
S1). The use of multiple shRNAs per gene is important, to control             below the criteria to be designated a hit, consistent with a mild
for off-target effects, and not all shRNAs are functional. A total of         early defect in memory precursor formation in Id3-deficient
110 unique shRNAs that target these genes were subcloned as a                 mice (Ji et al., 2011; Yang et al., 2011).
pool into pLMPd-Amt (Table S1 and Figures S5A and S5B). Indi-
vidual colonies from this transformation were picked, sequence                Tbx21 and Prdm1 shRNAs Impair Effector CTL
verified, and rearrayed into 96-well plates.                                  Development during LCMV Infection
   Retroviral supernatants prepared from cells transfected with               We validated results of the screen by examining the impact of
the array of 110 shRNAmir DNAs were used to transduce P14                     shRNAs individually. Both shTbx21.2 and shTbx21.3, but not
cells. Transduction of each construct was confirmed by Ame-                   shTbx21.1, strongly depleted Tbx21 mRNA and T-bet protein
trine fluorescence, and P14 cells were pooled. An aliquot was                 (Figures 2C and 2E), inhibited interferon-g (IFN-g) expression
removed for the input sample, and 500,000 cells were trans-                   (Figure 2D), and limited development of short-lived effector cells
ferred into multiple recipient mice that were then infected with              in vivo (p < 0.01, Figures 2F–2I). These results correlated directly
LCMV. On day 7 postinfection, short-lived effector (KLRG-                     with the enrichment of these shRNAs in the screen (Figure 2A
1hiIL-7Ralo) and memory precursor (KLRG-1loIL-7Rahi) P14 cells                and Table S1) and confirmed the role of T-bet in the generation
were sorted, genomic DNA was extracted from each popula-                      of effector CD8+ T cells.
tion, and shRNAmir sequencing libraries were prepared. After                     Prdm1 (encoding Blimp-1) has known roles in effector CD8+
sequencing and alignment to the reference shRNA sequences,                    and CD4+ T cell differentiation (Rutishauser et al., 2009; Shin
642,718 (input), 233,902 (effector), and 487,865 (memory) map-                et al., 2009; Johnston et al., 2009). Consistent with this, Prdm1
ped reads were retained for each cell susbset. All intended                   shRNAs were preferentially enriched in memory precursor
shRNAs introduced during T cell transduction were recovered                   CD8+ T cells, but the magnitude of their effects differed in repli-
from input samples; only two were not detected in either the                  cates of the in vivo screen (Figure S5C and Table S1). Analysis
effector or memory precursor cell populations. The memory                     of each Prdm1 shRNA individually showed that three of four
precursor:short-lived effector cell ratio for each shRNA was                  shRNAs impaired expression of both Blimp-1 mRNA and protein
calculated. Values from negative control shRNAs targeting                     (Figure 2J). The fourth shRNA impaired Blimp-1 protein expres-
genes not expressed in CD8+ T cells (Cd4, Cd14, Cd19,                         sion but did not reduce its mRNA (Figure 2J), perhaps because
Ms4a1 [CD20]) based on RNA-seq analysis (M.E.P., unpub-                       it targeted the Prdm1 30 UTR (Figure 2K). Individually, all four
lished data) were used to calculate Z-scores for each shRNA                   Prdm1 shRNAs impaired effector CD8+ T cell frequencies and
(Figure 2A and Table S1) and the ratios of shRNAs in effector                 increased the ratio of memory precursor cells to short-lived
and memory precursor subsets relative to the input cells was                  effector cells in vivo (p < 0.01–0.05, Figures 2L and 2M). These
plotted (Figure 2B). Several shRNAs were substantially reduced                data indicate that shRNAs can have variable effects but



(G–I) Quantitation of CD8+ T cell subsets resulting from shTbx21+ P14 cells in vivo.
(G) Short-lived effector cells (KLRG-1hiIL-7Ralo).
(H) Memory precursor cells (KLRG-1loIL-7Rahi).
(I) Ratio of memory precursor to short-lived effector phenotype P14 cells, per mouse.
(J) Prdm1 mRNA expression was determined by qRT-PCR in transduced P14 CD8+ T cells after sorting from spleens 7 days after LCMV infection. Blimp1 protein
expression was determined by immunoblot analysis after 4 days of culture with IL-12 (5 ng/ml) and IL-2 (100 U/ml).
(K) Map of Prdm1 with shRNA-targeted regions indicated.
(L) Contour plots of KLRG-1 and IL-7Ra staining on shPrdm1+ P14 CD8+ T cells from representative mice at 7 days after LCMV infection.
(M) Ratios of memory precursor to effector P14 CD8+ T cells. Each symbol represents T cells from an individual mouse.
Data are pooled from three (H, I) and two (J, L) independent experiments. *p < 0.05, **p < 0.01, ****p < 0.0001. Error bars represent standard deviations.

                                                                                 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc. 329

                                                                                                                                Immunity
                                                                                                             +            +
                                                                                  RNA Interference CD8 and CD4 T Cell Screens




confirmed that Prdm1 expression is required for short-lived              shRNAs might depend on the specific cellular context (e.g.,
effector CD8+ T cell differentiation.                                    CD4+ versus CD8+ T cells; Figures 3B and 2G). Thus, results
                                                                         of the pooled shRNA screen were consistent with experiments
Identification of Genes Underlying Tfh Cell                              using individual constructs.
Differentiation via an shRNA Screen In Vivo
In parallel, we developed a pooled screen in CD4+ T cells to             Ccnt1 Is Required for Both Th1 Cell and Effector CD8+
discover genes important for Tfh and Th1 cell differentiation            T Cell Differentiation In Vivo
in vivo (Figure 3A). A total of 5 3 105 shRNAmir+Amthi SMARTA            We compared the full data sets from the CD8+ and CD4+ T cells
cells were transferred into B6 hosts, and mice were infected             screens and found that inhibition of several different genes
3–4 days later with LCMV Armstrong (Figure 3A). DNA was                  affected differentiation of both effector CD8+ and CD4+ T cells
also isolated from an aliquot of cells before the transfer (input).      (Figures 4A and 4B). Ccnt1 encodes Cyclin T1, a noncanonical
At 6 days after LCMV infection, virus-specific Tfh cells (CXCR5+         cyclin that is a regulatory subunit of the RNA polymerase
SLAMlo) and Th1 cells (CXCR5SLAMhi) (Choi et al., 2013; John-           II-positive transcription elongation factor (P-TEFb). All four
ston et al., 2009) were isolated by flow cytometry and deep              Ccnt1-specific shRNAs were depleted from KLRG-1hiIL-7Ralo
sequenced for differential representation of the shRNAs. The             effector CD8+ T cells and from Th1 cells in the screens (Fig-
Tfh:Th1 ratios for each shRNA were calculated and their                  ure 4A). Based on the notion that functional parallels might exist
Z-scores were plotted (Figures 3B and 3C). A total of 14 control         between differentiation of CD4+ and CD8+ T cells during infection
shRNAs expected not to affect Tfh or Th1 cell differentiation (not       (Choi et al., 2013; Yang et al., 2011), we further explored the roles
known to be expressed in CD4+ T cells: Cd14, Cd19, Cd22,                 of Cyclin T1 in both subsets.
Ms4a1, Cd8, Smarca1) were equally distributed in both popula-               In CD4+ T cells, all four Ccnt1-shRNAs inhibited Cyclin T1 pro-
tions (Figure 3B), and their effects on cell accumulation were also      tein expression to varying degrees; three of four caused robust
assessed (Figure 3C). Based on a Z-score cutoff of Rj3.0j for            inhibition (Figures 4C and S6A). Each Ccnt1 shRNA was examined
each shRNA, factors encoded by Prdm1, Chd4, Id2, and Ccnt1               individually in SMARTA CD4+ T cells 6 days after LCMV infection
were identified as candidate positive regulators of Th1 cells or in-     (Figures 4D–4G). Neither CD4+ T cell proliferation (Figures S6B
hibitors of Tfh cell differentiation (Figures 3B and 3C, Table S1).      and S6C) nor CD4 or CD44 expression was affected by Ccnt1
Prdm1 is a positive control, as it encodes an inhibitor of Tfh cell      shRNAs (data not shown). Ccnt1 shRNAs both increased Tfh
differentiation (Johnston et al., 2009), and is discussed further        cell development (CXCR5+SLAMlo) and decreased Th1 cell forma-
below. Genes Fosb, Plagl1, Mta3, and Runx3 were identified               tion (p < 0.0001–0.05; Figures 4D and 4E). Germinal center Tfh (GC
as potential positive regulators of Tfh cells or inhibitors of Th1       Tfh) cells are a fully polarized subset of Tfh cells (CXCR5+PSGL1lo;
cell differentiation (Table S1). Plagl1 is highly expressed in Tfh       Crotty, 2011; Poholek et al., 2010) and their frequencies were
cells (Hale et al., 2013; Yusuf et al., 2010), and MTA3 (encoded         increased by Ccnt1 shRNAs (p < 0.001–0.05; Figures 4F and 4G).
by Mta3) is known to interact with Bcl6 in B cells (Fujita et al.,          We also examined T cell differentiation at earlier times points
2004). Itch is a known positive regulator of Tfh cell differentiation,   and found that Ccnt1 shRNAs substantially increased the pro-
based on a profound loss of Tfh cells in Itchfl/flCd4-cre+ mice          portion of early CXCR5+Bcl6+ Tfh cells (p < 0.01; Figures 4H
(Xiao et al., 2014). Notably, all four Itch shRNAs were severely         and 4I, and p < 0.01–0.05; Figure S6D). The increased Tfh cell
depleted from Tfh cells and highly enriched in the Th1 cell pop-         differentiation of shCcnt1+CD4+ T cells after LCMV infection
ulation (Figures 3B and 3C). In a second replicate of the CD4+           could be a reflection of a decreased potential of these cells to
T cell screen, the validated Bcl6 shRNA (shBcl6.2, Figure S1D)           differentiate into Th1 cells. Consistent with this hypothesis,
was depleted from the Tfh cell population, as expected (Fig-             Ccnt1 shRNAs resulted in decreased expression of T-bet in vivo
ure 3D). Comparisons of the two independent screens indicated            (p < 0.001–0.05; Figure 4J). Reciprocally, the expression of
that the in vivo screens generated reproducible results                  CD40L, an essential component of T cell help to B cells, was
(Figure 3E) and also showed that shRNA representation was                also increased in shCcnt1+ cells (p < 0.001–0.05; Figure 4K).
similar even when the libraries were sequenced with increased            These results suggest that Cyclin T1 promotes Th1 cell differen-
coverage using the higher-density PGM 318 chip (Figure 3E).              tiation at the expense of Tfh cell differentiation in vivo.
These results suggest that the CD4+ T cell shRNAmir-RV                      To test the requirement for Cyclin T1 in T cell differentiation
screening approach in vivo was also robust.                              in vitro, we cultured shCon+ and shCcnt1+ CD4+ T cells in Th1-
   To confirm results from the primary screen (Figure 3B), the           cell-biasing conditions. Ccnt1 shRNAs impaired T-bet expres-
effects of Prdm1 shRNAs were examined individually. SMARTA               sion under these conditions (p < 0.0001; Figure 5A), resulting in
CD4+ T cells transduced with shPrdm1.1-RV exhibited the stron-           a substantial loss of IFN-g production upon restimulation (p <
gest Tfh cell bias in vivo (p < 0.001, Figures 3F and 3G), consis-       0.0001–0.001; Figures 5B and 5C). The defect was cell intrinsic,
tent with results from the screen. A modest but significant Tfh cell     because no defect in IFN-g production was observed in untrans-
bias was observed in shPrdm1.3+ and shPrdm1.4+ SMARTA                    duced CD4+ T cells in the same wells (Figure S6E). These results
CD4+ T cells when compared to untransduced CD4+ T cells                  support a model in which reduced Cyclin T1 expression impairs
(p < 0.01, Figures 3F and 3G). shPrdm1.2 had no effect on Tfh            Th1 cell development and favors Tfh cell development.
cell differentiation (Figures 3F and 3G), consistent with it having
the weakest effect on Prdm1 mRNA expression in CD4+ T cells              The P-TEFb Subunit Cdk9 Is Necessary for Th1 Cell
(data not shown). These results correlated with the observed             Differentiation
distribution of the four shRNAs in the primary screen in CD4+            Conventional P-TEFb comprises Cdk9 (catalytic subunit) and a
T cells (Figure 3B) and also indicate that the activity of individual    regulatory subunit (e.g., Cyclin T1 or T2). To test whether Cyclin

330 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc.

Immunity
RNA Interference CD8+ and CD4+ T Cell Screens




A                                  Seed                  Seed PLAT-E in                                                                                                                   B                     20
                                             -1          a 96-well plate
                                  PLAT-E
                                                        Transfect 1 shRNAmir
                          Transfection 0
                                                              vector/well
                        CD3,CD28                         Seed CD4+ T cells in two                                                                                                                                                                              1
                       stim. of CD4             1




                                                                                                                                                                                            Tfh/Th1 (Z score)
                                                        96-well plates (avoid edges)                              Days 1 and 2:                                                                                                                  shPrdm1
    Transductions     2                                           Transduce CD4+:
                                                                                                                Harvest shRNA-RV,                                                                               10
                                                                                                                   store at 4°C
 (24 and 36 hrs after                                             1 shRNA-RV/well
                                                                                                                                                                                                                                             2       3     4
   CD3,CD28 stim) 3

    in vitro expansion
    for 2.5 days (IL-2) 4
                                                                                                                                                  Adoptive transfer
                                                                                                                                                                                                                 3
                                                                                                                                                    (5x105 cells)
                          O/N in vitro
                          rest (IL-7)
                                                6
                                                                                                     +
                                                                                            Pool CD4 T cells                              Amthi                                                                  0
                                                                                               before sort
       Sort, transfer
                       7                                                                                                                                                                                         -3
     and DNA isolation                                                                                                                                                                                                              4
                                                                                                                                                                                                                                   2
          LCMV infection 11                                                                                                          Ametrine                                                                                     1 shItch
                                                                      Th1 cell                                                                                                                                                3
                                                                                                                                                                                                                -10
                                                           SLAM




                                                                                                         Deep sequencing
       d6 p.i.
Sort Tfh and Th1 cell 17
 for DNA isolation                                                           Tfh cell

                                                                        CXCR5




C                                          shItch                                                           D                 -10                           E                       -10                          Chip 314
                                                                                                                                                                                                                 Chip 318
                                                                                                                                                                Z-score (Tfh/Th1)




                                                                                                                                     -8                                              -8
                                                                  1
                                                                                                                 Tfh/Th1 (Z score)




                                                                                                                                                                                     -6
     Enrichment of shRNA in Th1




                                                                                                                                     -6
                                                           2
                                                                                                                                                                                     -4
                                                                                                                                     -4
                                  -10                                                                                                                                                 -3
                                            3
            (Th1/input)




                                                    4                                                                                                                                -2
                                                                                                                                     -2
                                                                                        4
                                                                                 3                                                                                                   0
                                                                                                                                     0
                                                                                                1
                                                                       2
                                                                                     shPrdm1
                                                                                                                                                                                    G                                    **
                                                                                                                                                                                                     30                 **
                                                                -10                                                                                                                                               ***
                                                Enrichment of shRNA in Tfh
                                                       (Tfh/input)                                                                                                                                   20
                                                                                                                                                                                           Tfh




F                                                                                                                                                                                                    10
                                        shCon            shPrdm1.1                   shPrdm1.2             shPrdm1.3                        shPrdm1.4
                                            41                          68                      41                                   50               49                                                   0
      SLAM




                                                                                                                                                                                                -10
                                                                                                                                                                                                     sh rd 1.1
                                                                                                                                                                                                     sh rd 1.2
                                                                                                                                                                                                         dm .3
                                                                                                                                                                                                             4
                                                                                                                                                                                                     sh rd on




                                                                                                                                                                                                           1.
                                                                                                                                                                                                       Pr m1
                                                                                                                                                                                                       P C
                                                                                                                                                                                                       P m
                                                                                                                                                                                                       P m
                                                                                                                                                                                                     sh sh




                                                                                      CXCR5



Figure 3. A Pooled RNAi Screen in CD4+ T Cells Identifies Potential Regulators of Tfh and Th1 Cell Differentiation In Vivo
(A) Scheme for the shRNAmir screening approach using SMARTA CD4+ T cells.
(B) Relative enrichment of shRNAs in the Tfh or Th1 cell populations in vivo, reported as Z-score values for each shRNA in the library. Z-scores of j3j and j2j are
indicated by a dotted line and a tick, respectively.
(C) Scatter plot shows the log2 of normalized reads of all shRNA in Tfh and Th1 cell populations versus the input sample. This reveals effects on cell survival or
proliferation. shRNA are color coded as in (B).
(D) Z-scores are shown for the shRNAs most depleted from the Tfh cell population in the Ion 318 Chip experiment. shBcl6 is highlighted in orange.
(E) Z-scores of shRNAs depleted from Tfh cells in two independent deep sequencing reactions: Ion 314 Chip (black bars) and Ion 318 Chip (red bars). The dotted
line is a Z-score of 3.
(F) SMARTA CD4+ T cells were transduced with the indicated shRNAs, transferred into B6 mice, and analyzed 6 days after LCMV infection. shCon indicates a
control shRNAmir. Representative flow cytometry plots are shown of shRNA+ SMARTA CD4+ T cells with Tfh cell (CXCR5+SLAMlo) gate drawn.
(G) The differences in percentages of Tfh (%Tfh of Amt+  %Tfh of Amt) for each shRNAmir in SMARTA CD4+ T cells are shown. **p < 0.01, ***p < 0.001. Error
bars represent standard deviations.


T1 was likely acting via P-TEFb, we examined two Cdk9                                                                                                      in vitro (Figure 5D). CD4+ T cells transduced with Cdk9 shRNAs
shRNAs in SMARTA CD4+ T cells for their effects on Tfh versus                                                                                              and cultured under Th1-cell-biasing conditions showed
Th1 cell differentiation. Both shRNAs inhibited Cdk9 expression                                                                                            impaired production of IFN-g, similar to the effect of Ccnt1

                                                                                                                                                              Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc. 331

                                                                                                                                                                                                                                                                                                                                                                                             Immunity
                                                                                                                                                                                                                                                                                          +                                                   +
                                                                                                                                                                                                                RNA Interference CD8 and CD4 T Cell Screens




A                                                                                        shCcnt1                                                                           D                                                                                                                                                                           E                                                 *
                                                                                     3                                                                                                       shCon            shCcnt1.1                   shCcnt1.2                                     shCcnt1.3                                                                                                     ****
                                                                                          2 4                                                                                                                                                                                                                                                                                                       ****
                                                                                                                                                                                                      54             77                           81                                            78                                                                                                ****
                                                                                              1
              CD8 memory precursor/effector (Z score)




                                                                                                                                                                                                                                                                                                                                                           Tfh cells (CXCR5+SLAMlo)
                                                                                 5                                                                                                                                                                                                                                                                                                         1.5




                                                                                                                                                                                SLAM
                                                                                                                                                                                                                                                                                                                                                                                           1.0


                                                                                                                                                                                                                          CXCR5

                                                                                                                                                                                                                                                                                                                                                                                           0.5




                                                                                                                                                                                                                                                                                                                                                                                                 shCon

                                                                                                                                                                                                                                                                                                                                                                                                          shCcnt1.1

                                                                                                                                                                                                                                                                                                                                                                                                                       shCcnt1.2

                                                                                                                                                                                                                                                                                                                                                                                                                                    shCcnt1.3
                                                                                                                                                                                                                                                                                                                                                                                                                                                 shCcnt1.4
                                                         - 10       -5                    5       10                       15                       20



                                                                                                                                                                           F                                                                                                                                                                           G                                                   *
                                                                                                                                                                                             shCon          shCcnt1.1    shCcnt1.2     shCcnt1.3                                                                                                                                           2.5           **




                                                                                                                                                                                                                                                                                                                                                           GC Tfh cells (CXCR5+PSGL-1lo)
                                                                                                                                                                                        40            35 30         36 16         49 20         45                                                                                                                                                    ***
                                                                              -5                                                                                                                                                                                                                                                                                                                    ***
                                                                                                                                                                                                                                                                                                                                                                                           2.0




                                                                                                                                                                               PSGL-1
                                                                                                                                                                                                                                                                                                                                                                                           1.5
                                                                            Tfh/Th1 (Z score)
                                                                                                                                                                                                                                                                                                                                                                                           1.0
B                                                                                                                                                                                                     24                  32                                           33                                             33
                                                                                                                                                                                                                                                                                                                                                                                           0.5
                                                        CD8        Fosb, Smarca1, Nfatc3,                                                                                                                                 CXCR5
                                                                   Id2, Klf2, Ccnt1, Klf12 , Tbx21                                                                                                                                                                                                                                                                                         0.0




                                                                                                                                                                                                                                                                                                                                                                                                 shCon
                                                                                                                                                                                                                                                                                                                                                                                                         shCcnt1.1
                                                                                                                                                                                                                                                                                                                                                                                                                      shCcnt1.2

                                                                                                                                                                                                                                                                                                                                                                                                                                   shCcnt1.3
                                                                                                                                                                                                                                                                                                                                                                                                                                                shCcnt1.4
                                                         CD4       Fosb, Itch, Bcl6, Plagl1, Mta3, Runx3,
                                                                   Ccnt1, Id2, Chd4, Prdm1
                                                                                                                                                                           H                                                                                                             I                                     **
                                                                                                                                                                                             shCon            shCcnt1.1                 shCcnt1.2                                                               80
                                                                                                                                                                                                                                                                                                                             **
C                                                                                                                                                                                                53                 62                               66




                                                                                                                                                                                                                                                                                             CXCR5 +Bcl6+ (%)
                                                                                            2

                                                                                            3

                                                                                            4
                                                                          1




                                                                                                                                                                                                                                                                                                                60
                                                                                          1.

                                                                                         1.

                                                                                          1.
                                                                        1.




                                                                                                                                                                                Bcl6
                                                                                       nt

                                                                                       nt

                                                                                       nt
                                                                       nt
                                                              n
                                                          Co




                                                                             Cc

                                                                                    Cc

                                                                                    Cc
                                                                   Cc
                                                        sh




                                                                            sh

                                                                                 sh

                                                                                 sh
                                                                  sh




                                                                                                                                                                                                                                                                                                                40

    80 kD-                                                                                       Cyclin T1 (81 kD)
    40 kD-
                                                                                                                                                                                                                                                                                                                20
                                                                                                 TBP (38 kD)                                                                                                    CXCR5
                                                        1.0     0.07 0.63 0.14 0.09                                                                                                                                                                                                                              0




                                                                                                                                                                                                                                                                                                                     shCon

                                                                                                                                                                                                                                                                                                                               shCcnt1.1

                                                                                                                                                                                                                                                                                                                                           shCcnt1.2
J                                                                                                                                                                K                                                                            40               ***
                                                                         1260                                       2000                ***                                    0.4
                                                                         1064                                                       *                                          14                                                                          *
                                                                         712                                                                                                   24                                                             30
                                                                                                                                                                     Max (%)




                                                                                                                                                                                                                               CD40L hi (%)




                                                                                                                                                                                                           shCon No GP
    Max (%)




                                                                                                                    1500
                                                                                        shCon
                                                                                                    T-bet Geo MFI




                                                                                                                                                                               30                                shCon
                                                                                     shCcnt1.1
                                                                                                                    1000
                                                                                                                                                                                                              shCcnt1.1                       20
                                                                                     shCcnt1.2
                                                                                                                                                                                                              shCcnt1.2

                                                                                                                     500                                                                                                                      10



                                                                                                                       0
                                                                                                                                                                                                                                               0
                                                                                                                            shCon

                                                                                                                                        shCcnt1.1

                                                                                                                                                     shCcnt1.2




                                                                T-bet                                                                                                                    CD40L
                                                                                                                                                                                                                                                   shCon

                                                                                                                                                                                                                                                               shCcnt1.1

                                                                                                                                                                                                                                                                            shCcnt1.2




Figure 4. Ccnt1 Depletion Promotes Development of Tfh Cells during Viral Infection
(A) Comparison of shRNAmir screening results in both CD4+ and CD8+ T cells. Tfh and Th1 CD4+ T cells differentiation results, plotted against memory precursor
and effector CD8+ T cell differentiation results. Z-score values are shown. Common negative control shRNAs are shown in yellow, and those targeting Ccnt1 are
highlighted (red).
(B) Table of top hits for genes required for memory precursor CD8+ T cell or Tfh CD4+ T cell differentiation (blue) and short-lived effector CD8+ T cell or Th1 CD4+
T cell differentiation (red).
(C) Cyclin T1 protein expression in MCC T cells after transduction with the indicated shRNAs and 4 days of culture. The ratios of Cyclin T1 to TBP relative to the
control shRNA are indicated.
(D and E) Flow cytometry plots (D) and quantitation (normalized) (E) of Tfh cell differentiation (CXCR5+SLAMlo) by shCcnt1+ SMARTA CD4+ T cells at 6 days after
LCMV infection.
(F and G) Flow cytometry plots (F) and quantitation (normalized) (G) of GC Tfh cell differentiation (CXCR5+PSGL1lo) by shCcnt1+ SMARTA CD4+ T cells at 6 days
after LCMV infection.
(H and I) Flow cytometry plots (H) and quantitation (I) of CXCR5 and Bcl6 expression by shCcnt1+ SMARTA CD4+ T cells at 4 days after LCMV infection.
(J) T-bet expression in shCcnt1+ SMARTA CD4+ T cells in vivo, 3 days after LCMV infection. T-bet geometric MFIs are graphed (right).
(K) CD40L expression by shCcnt1+ SMARTA CD4+ T cells at 4 days after LCMV infection, after 2 hr restimulation with GP61-80 peptide. The percentages of
CD40Lhi cells are indicated. Each symbol represents T cells from an individual mouse.
Data are pooled from three (F, G) or representative of two (K) or three (H–J) independent experiments. *p < 0.05, **p < 0.01, ***p < 0.001, ****p < 0.0001.



shRNAs (p < 0.001–0.01; Figures 5E and 5F), suggesting that                                                                                                                                         Cdk9 depletion in vivo favored Tfh (CXCR5+SLAMlo) cell devel-
both Cyclin T1 and Cdk9 promote Th1 cell differentiation                                                                                                                                          opment while reducing Th1 cell differentiation (shCdk9.1, p <
in vitro.                                                                                                                                                                                         0.0001; Figures 5G and 5H), without impairing T cell expansion

332 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc.

Immunity
RNA Interference CD8+ and CD4+ T Cell Screens




(Figure S7A) or normal expression of CD4 and CD44. Further-           DISCUSSION
more, Cdk9 depletion increased the frequency of GC Tfh cells,
measured as CXCR5+PSGL1lo cells (shCdk9.1, p < 0.001; Fig-            We have demonstrated the applicability of a pooled approach
ures 5I and 5J) or CXCR5+Bcl6hi cells (Figures S7B and S7C).          using shRNAmirs in T cells to screen for factors that regulate
Additionally, based on CXCR5 and Bcl6 expression, early Tfh           CD4+ and CD8+ T cell differentiation in response to viral infection.
cell differentiation in shCdk9+CD4+ T cells was enhanced              Using an improved shRNAmir vector that enhances suitability of
4 days after LCMV infection (p < 0.01–0.05; Figures 5K and            shRNA-mediated RNAi in studies that depend upon cell trans-
5L), with normal cell expansion (Figure S7D). Intriguingly, similar   fers, more than 100 unique shRNAs were screened simulta-
to what was observed in the absence of Cyclin T1, inhibition of       neously in vivo. In separate proof-of-principle screens during
Cdk9 expression also increased CD40L expression by CD4+               LCMV infection using virus-specific TCR transgenic SMARTA
T cells (p < 0.001–0.01; Figure 5M). Altogether, these data reca-     CD4+ T cells or P14 CD8+ T cells, we identified multiple candi-
pitulated those obtained with shCcnt1+CD4+ T cells and suggest        date genes with potential roles in the development of Th1 and
that P-TEFb might preferentially promote Th1 cell differentiation     Tfh CD4+ T cells as well as short-lived effector and memory pre-
of activated CD4+ T cells.                                            cursor CD8+ T cells. Detailed follow-up analyses of one factor
                                                                      identified in both screens revealed specific roles for Cyclin T1
Ccnt1 and Cdk9 Are Required for Development of                        and Cdk9, components of P-TEFb, for promoting Th1 cell devel-
Protective Effector CTLs In Vivo                                      opment of CD4+ T cells and protective effector CTL development
Next, we explored the requirements of Ccnt1 expression in CD8+        of CD8+ T cells during infection, while limiting differentiation of
T cells. Three of the four Ccnt1-specific shRNAs resulted in near     Tfh cells and memory precursor CD8+ T cells. These data sug-
complete inhibition of Cyclin T1 protein expression in cultured       gest that regulation of transcription elongation by P-TEFb might
CD8+ T cells; one shRNA exhibited strong but incomplete               be an important mechanism underpinning differentiation of
inhibition (Figure 6A). The accumulation of P14 CD8+ T cells          T cells during immune responses.
transduced with Ccnt1 shRNAs was not impaired during culture             Several important aspects distinguish the screen presented
(Figure 6B) or in vivo (Figure 6C). However, Ccnt1 shRNAs             here from other recently reported pooled in vivo shRNA-screens
strongly impaired generation of short-lived effector P14 T cells      (Beronja et al., 2013; Zhou et al., 2014; Zuber et al., 2011). The
(Figures 6D and 6E). There was a concomitant increase in the          screening approach here used an array strategy to ensure inde-
fraction of memory precursor phenotype P14 cells (Figures 6D          pendent transductions and equal representation of shRNAmirs
and 6F), which increased the ratio of memory precursor to             in the input pools. In addition, in contrast to other screens based
short-lived effector P14 cells (Figure 6G).                           on shRNA-dependent cell accumulation or depletion as the main
   To examine whether the effects of Ccnt1 shRNAs in CD8+             readout to identify primary hits (Beronja et al., 2013; Zhou et al.,
T cells were related to Cyclin T1 function as a subunit of            2014; Zuber et al., 2011), the approach presented here was a
P-TEFb, we examined the effects of Cdk9-specific shRNAs (Fig-         phenotypic screen of cell differentiation during an infection. As
ure 6H). Similar to shCcnt1, shCdk9+ P14 cells exhibited reduced      such, it was complicated by the nature of T cell responses during
short-lived effector cell and increased memory precursor cell         infection, which are constrained by factors such as the fre-
formation in vivo (Figures 6I–6K). This correlated with decreased     quencies of antigen-specific T cells (Badovinac et al., 2007;
T-bet expression in vivo (Figure 6L). Notably, T-bet expression in    Obar et al., 2008), and thus, is distinct from a T cell adoptive
shCcnt1+ or shCdk9+ P14 cells was impaired in KLRG-1loIL-             immunotherapy setting, which affords transferring much larger
7Ralo cells (data not shown), a stage that presumably precedes        T cell numbers (Zhou et al., 2014).
development of either short-lived effector or memory precursor           The ability to conduct large-scale pooled screens using
CD8+ T cells. These data show that wild-type amounts of Cyclin        shRNAs has advanced, although interpreting the results of
T1 and Cdk9 are necessary for efficient development of short-         shRNA-based assays remains complicated. As our data on the
lived effector CTLs and that they normally limit generation of        Prdm1, Tbx21, and Ccnt1 genes emphasize, interrogating the ef-
memory precursor CD8+ T cells.                                        fects of multiple shRNAs targeting the same gene in several as-
   The defect in shCcnt1+ and shCdk9+ short-lived effector            says tends to clarify the role of each gene, because each shRNA
CD8+ T cell formation brought into question whether these cells       can result in nonidentical phenotypes attributable to differential
were effective at viral control. Thus, we examined LCMV burden        effects on particular target RNA isoforms, unintended off-target
on day 8 of infection. LCMV titers in the spleen of host mice         effects, or partial attenuation of target-specific gene expression.
with shCcnt1+ or shCdk9+ P14 cells were at least 2- to 5-fold         In our experience, 60% of shRNA sequences derived from the
higher than controls (Figure 7A). Correlating with this finding,      GIPZ library (the source of most shRNAs for this study) impaired
shCcnt1+ or shCdk9+ P14 cells from infected mice expressed            target gene expression or caused a measurable biological
less granzyme B (Figure 7B). Finally, we examined shCcnt1+            phenotype (data not shown). However, newer algorithms trained
or shCdk9+ P14 cells under culture conditions that strongly           on functional data have improved predicting shRNAmirs that
induce CTL differentiation (Pipkin et al., 2010). Under these         trigger RNAi more potently and specifically than previous de-
conditions, all shRNAs targeting either Ccnt1 or Cdk9 also spe-       signs (Fellmann et al., 2011). Our study employed some of these
cifically inhibited perforin protein expression (Figure 7C). Thus,    designs and they are likely to enhance the fidelity of future large-
normal amounts of Cyclin T1 and Cdk9 appear to be required            scale screens in vivo.
for the upregulation of genes encoding cytotoxic effector                Using a conservative approach, we showed that more than
functions and for effective CTL-mediated protection from viral        100 unique shRNAmirs represented by 500,000 adoptively trans-
infection.                                                            ferred P14 cells could be assayed in fewer than 10 mice in

                                                                        Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc. 333

                                                                                                                                            Immunity
                                                                                                                      +             +
                                                                                         RNA Interference CD8 and CD4 T Cell Screens




A                                                        B                                                        C




D                                              E                                                       F




G                                                        H                        I                                                     J




K                                                        L                        M




Figure 5. Cyclin T1 and Cdk9 Depletion Impairs Th1 Cell Differentiation In Vitro and In Vivo
(A–C, E, and F) CD4+ T cells were transduced with Ccnt1 shRNAs and cultured under Th1-cell-biasing conditions for 4 days before restimulation with PMA and
ionomycin for 1 (E and F) or 4 (A–C) hr.
(A) T-bet expression by shCcnt1+ CD4+ T cells. Quantitation and an example histogram are shown.
(B) Flow cytometry plots of IFN-g expression by shCcnt1+ CD4+ T cells upon restimulation.
(C) Quantitation of (B), for all samples.
(D) Cdk9 protein expression in shCdk9+ MCC T cells.
(E) Flow cytometry plots of IFN-g expression by shCdk9+CD4+ T cells upon restimulation.
(F) Quantitation of (E), for all samples.
(G and H) Flow cytometry plots (G) and quantitation (H) of Tfh cell differentiation (CXCR5+SLAMlo) by shCdk9+ SMARTA CD4+ T cells at 6 days after LCMV
infection.
(I and J) Flow cytometry plots (I) and quantitation (J) of GC Tfh cell differentiation (CXCR5+PSGL1lo) by shCdk9+ SMARTA CD4+ T cells at 6 days after LCMV
infection.
                                                                                                                          (legend continued on next page)

334 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc.

Immunity
RNA Interference CD8+ and CD4+ T Cell Screens




approximately 1 week. Under these conditions, we estimated                    EXPERIMENTAL PROCEDURES
that each shRNA was represented 500 times per mouse after
                                                                              Animals and Viruses
T cell engraftment, which is 10-fold higher representation of
                                                                              C57BL/6 (B6) mice were purchased from the Jackson Laboratory. CD45.1+
each shRNA than a recent pooled screen that examined skin                     SMARTA (SM; lymphocytic choriomeningitis virus [LCMV] gp66-77-IAb spe-
cell development in vivo (Beronja et al., 2013; Zuber et al.,                 cific) (Oxenius et al., 1998) and Blimp1-YFP mice were bred in-house.
2011) and involved transferring 10-fold fewer T cells than a                  LCMV gp33-41-specific P14 Thy1.1+ mice used for in vivo analysis were
recent immunotherapy screen in T cells (Zhou et al., 2014).                   a gift from R. Ahmed (Emory University); P14 Tcra/ mice were used for
Taking these studies into account with our results, we anticipate             in vitro studies (Taconic). All mice were maintained in specific-pathogen-
                                                                              free facilities and used according to protocols approved by the animal care
that by using our system and applying deeper sequencing, it is
                                                                              and use committees of the LIAI and TSRI-FL. Virus stocks were made as
likely to be feasible to perform phenotypic screens on pools of
                                                                              described (Johnston et al., 2009), and LCMV titers in tissues were assessed
1,000 or more shRNAs in parallel in T cells during infection.                 by plaque assay.
   The screen discovered unanticipated roles for Cyclin T1 and
Cdk9 in the regulation of T cell differentiation during antiviral             Pooled Screening Approaches
immune responses and emphasizes the specificity that ubiqui-                  Please refer to Supplemental Experimental Procedures.
tously expressed factors can have. Cyclin T1 and Cdk9 are
two widely expressed components of P-TEFb (Oven et al.,                       Flow Cytometry
                                                                              Single-cell suspensions of spleens were prepared by mechanical disruption.
2007; Peterlin and Price, 2006), which stimulates the transition
                                                                              Surface staining for flow cytometry was performed by standard techniques
of paused RNA polymerase II complexes into productive elonga-                 (Johnston et al., 2009) and the following clones: CD4 (RM4-5), CD45.1 (A20),
tion (Peterlin and Price, 2006). The regulation of transcription              CD44 (IM7), and CD62L (MEL-14) (eBiosciences); CD8 (53-6.7) and B220
elongation might govern a substantial fraction of differential                (RA3-6B2) (BD Biosciences); as well as CD8 (53-6.7), CD127 (A7R34),
expression of transcriptionally active genes (Min et al., 2011;               KLRG-1 (2F1), CD90.1 (OX-7), and SLAM (TC15-12F12.2) (BioLegend).
Peterlin and Price, 2006; Rahl et al., 2010), and it is notable               CXCR5 staining was performed as described (Choi et al., 2013). Intracellular
                                                                              staining after surface stains was performed using the ‘‘Foxp3 staining buffer’’
that this process is also critical in the regulation of HIV transcrip-
                                                                              set (eBiosciences), using anti-Bcl6 monoclonal antibody (K112-91, BD Biosci-
tion in CD4+ T cells. The fact that depletion of Cyclin T1 or Cdk9            ences), anti-Tbet (4B10), or anti-Granzyme B (GB11) (Biolegend).
in activated T cells results in specific alterations in their differen-
tiation in vitro and in vivo indicates that these factors are utilized        Adoptive Transfer Analysis of Individual shRNAmirs in CD8+ or CD4+
in context-specific regulation of gene expression in T cells,                 T Cells
despite their ubiquitous expression. Indeed, ChIP-seq analysis                For in vivo confirmation of ‘‘hits,’’ SMARTA CD4+ or P14 CD8+ T cells were
showed that Cyclin T1 is specifically recruited to subsets of                 transduced with viral supernatants generated from individual shRNAmir-RV
                                                                              constructs (Supplemental Experimental Procedures). A total of 5 3 105 P14
genes, including Tbx21, Prf1, Ifng, and Il2ra, that are activated
                                                                              cells were transferred into 6-week-old B6 mice 1 or 2 days after activation
in response to TCR-like stimulation of CD8+ T cells (M.E.P.,                  and analyzed on day 7 or 8 after infection. Note, transfer of P14 cells on day
unpublished data).                                                            1 rather than day 2 after activation was found to recapitulate differentiation
   Given the known functions of Cyclin T1 and Cdk9 in P-TEFb,                 more physiologically (data not shown). For CD4+ T cell experiments, 25,000
one interpretation of our results is that T cell differentiation is           SMARTA cells were transferred.
regulated via transcriptional elongation by P-TEFb. However,
                                                                              RNA and Protein Analysis
the phenotypes upon Cyclin T1 and Cdk9 depletion were not
                                                                              Total RNA was isolated from transduced (Ametrine+) CD4+ or CD8+ T cells and
identical, although they were similar. One simple explanation of
                                                                              used for cDNA synthesis as previously described (Johnston et al., 2009). qPCR
this outcome is that shRNA-mediated depletion of Cdk9 was                     reactions were performed in triplicate using the SYBR Select Master Mix
less efficient than for Cyclin T1, resulting in different amounts             (Life Technologies) on a Roche Lightcycler 480, using primers specific
of functional P-TEFb in each case. Another interpretation is alter-           to Prdm1 (F-50 -TTCTCTTGGAAAAACGTGTGGG-30 ; R-50 -GGAGCCGGAG
native factors that ‘‘compensate’’ for reductions in wild-type                CTAGACTTG-30 ) and Tbx21 (F-50 -ACCAACAACAAGGGGGCTTC-30 ; R-50 -
Cyclin T1 or Cdk9 amounts, and which possess distinct activities              CTCTGGCTCTCCATCATTCACC-30 ). For immunoblot analysis, whole-cell
                                                                              lysates were obtained from CD8+ T cells on day 6 after activation, from
or targeting, caused the observed phenotypes. Indeed, other
                                                                              CD4+ T cells 5 days after activation, or from MCC-T cells by sorting transduced
Cyclins and Cyclin-dependent kinases can phosphorylate the                    (Ametrine+) cells and lysis in 150 mM NaCl, 25 mM Tris (pH 7.5), 1% Triton
C-terminal domain of RNA Pol II at serine 2 and regulate tran-                X-100, 0.1% SDS, 0.5% Deoxycholate, and complete protease inhibitors
scription, and could be cell type specific (Blazek et al., 2011).             (Roche). 25 mg of protein was resolved by 8% SDS-PAGE, transferred to nitro-
Finally, Cyclin T1 and Cdk9 could have roles in T cells apart                 cellulose membranes, and probed with anti-Cyclin T1 (sc-10750), anti-Blimp1
from their established roles in P-TEFb. Future studies to eluci-              (sc-47732), anti-Cdk9 (sc-484) (Santa Cruz Biotechnology), anti-Perforin
                                                                              (ab16074), and anti-beta Actin (Abcam ab8227).
date the specific roles of Cyclin T1 and Cdk9 and how they
integrate with the external signals that govern CD4+ and CD8+
                                                                              SUPPLEMENTAL INFORMATION
T cell differentiation are likely to open previously unappreciated
insights into T cell function. In summary, the functional genetic             Supplemental Information includes seven figures, one table, and Supple-
approach described here is likely to facilitate the identification            mental Experimental Procedures and can be found with this article online at
of many previously unknown players.                                           http://dx.doi.org/10.1016/j.immuni.2014.08.002.


(K and L) Flow cytometry plots (K) and quantitation (L) of CXCR5 and Bcl6 expression by shCdk9+ SMARTA CD4+ T cells, 4 days after LCMV infection.
(M) Histograms of CD40L expression on shCdk9+ SMARTA CD4+ T cells, after isolation from spleens 4 days after LCMV infection and restimulation with GP61-80
peptide for 4 hr. The percentages of CD40Lhi SMARTA are shown and summarized (right).
Data are representative of two independent experiments. *p < 0.05, **p < 0.01, ***p < 0.001, ****p < 0.0001.

                                                                                 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc. 335

                                                                                                                                                Immunity
                                                                                                                          +             +
                                                                                            RNA Interference CD8 and CD4 T Cell Screens




A                                                B                                                 C




D




E                                  F                                 G




H                                                                        I                     J                     K                      L




Figure 6. Cyclin T1 and Cdk9 Depletion Impairs Generation of Effector CD8+ T Cells during LCMV Infection
(A) Immunoblot analysis of Cyclin T1 in FACS-sorted shCcnt1+ P14 CD8+ T cells. Cells were cultured 6 days in low IL-2 (10 U/ml).
(B) Expansion of FACS-sorted shCcnt1+ P14 CD8+ T cells in culture. Low IL-2 (10 U/ml), high IL-2 (100 U/ml).
(C–L) Adoptively transferred P14 CD8+ T cells transduced with the indicated shRNAs were analyzed on day 7 (C–G) or day 8 (H–L) after LCMV infection.
(C) The numbers and percentages of shCcnt1+ P14 cells in the spleen.
(D) Contour plots show KLRG-1 and IL-7Ra staining on shCcnt1+ P14 CD8+ T cells from representative mice 7 days after LCMV infection.
(E–G) Quantitation of CD8+ T cell subsets from shCcnt1+ P14 cells in vivo.
(E) Short-lived effector cells (KLRG-1hiIL-7Ralo).
(F) Memory precursor cells (KLRG-1loIL-7Rahi).
(G) Ratio of memory precursor to short-lived effector phenotype P14 cells, per mouse.
(H) Contour plots show KLRG-1 and IL-7Ra staining by shCdk9+ P14 CD8+ T cells from representative mice 8 days after LCMV infection.
(I–L) Quantitation of CD8+ T cell subsets from shCdk9+ P14 cells in vivo.
(I) Short-lived effector cells (KLRG-1hiIL-7Ralo).
(J) Memory precursor cells (KLRG-1loIL-7Rahi).
(K) Ratio of memory precursor to short-lived effector phenotype P14 cells, per mouse.
(L) Summarized T-bet expression based on intracellular staining and flow cytometry.
Each symbol represents T cells from separate mice. Data are pooled from two independent experiments. *p < 0.05, **p < 0.01, ***p < 0.001, ****p < 0.0001. Error
bars represent standard deviations.


AUTHOR CONTRIBUTIONS                                                             and assisted writing the paper. M.A.F. performed CD8+ T cell follow-up anal-
                                                                                 ysis. B.L. designed the sequencing bioinformatic pipeline. R.J.J. designed
R.C. established the pooled approaches, implemented and analyzed the             vectors and did preliminary experiments. S.S., N.X., and Y.-C.L. provided re-
CD8+ T cell screen and follow-up, and assisted writing the paper. S.B. de-       agents and advice. A.R. assisted with experimental design, provided re-
signed, implemented, and analyzed the CD4+ T cell screen and follow-up,          sources, and assisted writing the paper. B.P. designed the sequencing

336 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc.

Immunity
RNA Interference CD8+ and CD4+ T Cell Screens




        A                                                                         R01 072543 to S.C.; NIH U19 AI109976 to S.C. and M.E.P.; Frenchmen’s
                                                                                  Creek Women for Cancer Research to R.C.; and a Postdoctoral Training
                                                                                  Award from the Fonds de la recherche santé Québec to S.B. We thank G. Mar-
                                                                                  tinez for advice and assistance.

                                                                                  Received: November 8, 2013
                                                                                  Accepted: August 4, 2014
                                                                                  Published: August 21, 2014


                                                                                  REFERENCES

                                                                                  Araki, K., Turner, A.P., Shaffer, V.O., Gangappa, S., Keller, S.A., Bachmann,
                                                                                  M.F., Larsen, C.P., and Ahmed, R. (2009). mTOR regulates memory CD8
        B                                                                         T-cell differentiation. Nature 460, 108–112.
                                                                                  Badovinac, V.P., Haring, J.S., and Harty, J.T. (2007). Initial T cell receptor
                                                                                  transgenic cell precursor frequency dictates critical aspects of the CD8(+)
                                                                                  T cell response to infection. Immunity 26, 827–841.
                                                                                  Beronja, S., Janki, P., Heller, E., Lien, W.H., Keyes, B.E., Oshimori, N., and
                                                                                  Fuchs, E. (2013). RNAi screens in mice identify physiological regulators of
                                                                                  oncogenic growth. Nature 501, 185–190.
                                                                                  Best, J.A., Blair, D.A., Knell, J., Yang, E., Mayya, V., Doedens, A., Dustin, M.L.,
                                                                                  and Goldrath, A.W.; Immunological Genome Project Consortium (2013).
                                                                                  Transcriptional insights into the CD8(+) T cell response to infection and
                                                                                  memory T cell formation. Nat. Immunol. 14, 404–412.
                                                                                  Blazek, D., Kohoutek, J., Bartholomeeusen, K., Johansen, E., Hulinkova, P.,
        C                                                                         Luo, Z., Cimermancic, P., Ule, J., and Peterlin, B.M. (2011). The Cyclin K/
                                                                                  Cdk12 complex maintains genomic stability via regulation of expression of
                                                                                  DNA damage response genes. Genes Dev. 25, 2158–2172.
                                                                                  Cannarile, M.A., Lind, N.A., Rivera, R., Sheridan, A.D., Camfield, K.A., Wu,
                                                                                  B.B., Cheung, K.P., Ding, Z., and Goldrath, A.W. (2006). Transcriptional regu-
                                                                                  lator Id2 mediates CD8+ T cell immunity. Nat. Immunol. 7, 1317–1325.
                                                                                  Chang, J.T., Palanivel, V.R., Kinjyo, I., Schambach, F., Intlekofer, A.M.,
                                                                                  Banerjee, A., Longworth, S.A., Vinup, K.E., Mrass, P., Oliaro, J., et al. (2007).
                                                                                  Asymmetric T lymphocyte division in the initiation of adaptive immune
                                                                                  responses. Science 315, 1687–1691.
                                                                                  Choi, Y.S., Yang, J.A., Yusuf, I., Johnston, R.J., Greenbaum, J., Peters, B., and
                                                                                  Crotty, S. (2013). Bcl6 expressing follicular helper CD4 T cells are fate
                                                                                  committed early and have the capacity to form memory. J. Immunol. 190,
                                                                                  4014–4026.
                                                                                  Ciofani, M., Madar, A., Galan, C., Sellars, M., Mace, K., Pauli, F., Agarwal, A.,
                                                                                  Huang, W., Parkurst, C.N., Muratet, M., et al. (2012). A validated regulatory
                                                                                  network for Th17 cell specification. Cell 151, 289–303.
                                                                                  Crotty, S. (2011). Follicular helper CD4 T cells (TFH). Annu. Rev. Immunol. 29,
                                                                                  621–663.
                                                                                  Crotty, S. (2012). The 1-1-1 fallacy. Immunol. Rev. 247, 133–142.
                                                                                  Doering, T.A., Crawford, A., Angelosanto, J.M., Paley, M.A., Ziegler, C.G., and
                                                                                  Wherry, E.J. (2012). Network analysis reveals centrally connected genes and
                                                                                  pathways involved in CD8+ T cell exhaustion versus memory. Immunity 37,
Figure 7. Cyclin T1 and Cdk9 Are Required for Antiviral CTL Functions             1130–1144.
(A) LCMV titers in spleen were determined 8 days after LCMV infection.            Fellmann, C., Zuber, J., McJunkin, K., Chang, K., Malone, C.D., Dickins, R.A.,
(B) Granzyme B expression in P14 cells at day 8 postinfection. Histogram (left)   Xu, Q., Hengartner, M.O., Elledge, S.J., Hannon, G.J., and Lowe, S.W. (2011).
and quantitation (geometric MFI; right).                                          Functional identification of optimized RNAi triggers using a massively parallel
(C) Immunoblot analysis of Cyclin T1, Cdk9, Perforin, and b-actin expression in   sensor assay. Mol. Cell 41, 733–746.
whole-cell lysates from flow cytometry-sorted shCcnt1+ and shCdk9+ P14            Fujita, N., Jaye, D.L., Geigerman, C., Akyildiz, A., Mooney, M.R., Boss, J.M.,
CD8+ T cells after 6 days in culture (100 U/ml).                                  and Wade, P.A. (2004). MTA3 and the Mi-2/NuRD complex regulate cell fate
                                                                                  during B lymphocyte differentiation. Cell 119, 75–86.
analysis pipeline and supervised statistical analyses. M.E.P. and S.C.
                                                                                  Gray, P.A., Fu, H., Luo, P., Zhao, Q., Yu, J., Ferrari, A., Tenzen, T., Yuk, D.I.,
conceived of the studies, designed experiments, analyzed data, supervised
                                                                                  Tsung, E.F., Cai, Z., et al. (2004). Mouse brain organization revealed through
the projects, and wrote the paper.
                                                                                  direct genome-scale TF expression analysis. Science 306, 2255–2257.

ACKNOWLEDGMENTS                                                                   Haining, W.N., and Wherry, E.J. (2010). Integrating genomic signatures for
                                                                                  immunologic discovery. Immunity 32, 152–161.
This work was supported by NIH grants RC4 AI092763 to M.E.P., R.C., S.S.,         Hale, J.S., Youngblood, B., Latner, D.R., Mohammed, A.U., Ye, L., Akondy,
B.P., and A.R.; NIH R01 AI095634 to M.E.P.; NIH R01 CA42471 to A.R.; NIH          R.S., Wu, T., Iyer, S.S., and Ahmed, R. (2013). Distinct memory CD4+ T cells

                                                                                    Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc. 337

                                                                                                                                                           Immunity
                                                                                                                                   +               +
                                                                                                RNA Interference CD8 and CD4 T Cell Screens




with commitment to T follicular helper- and T helper 1-cell lineages are gener-      tional programs that promote the differentiation of effector cytolytic T cells.
ated after acute viral infection. Immunity 38, 805–817.                              Immunity 32, 79–90.
Intlekofer, A.M., Takemoto, N., Wherry, E.J., Longworth, S.A., Northrup, J.T.,       Poholek, A.C., Hansen, K., Hernandez, S.G., Eto, D., Chandele, A., Weinstein,
Palanivel, V.R., Mullen, A.C., Gasink, C.R., Kaech, S.M., Miller, J.D., et al.       J.S., Dong, X., Odegard, J.M., Kaech, S.M., Dent, A.L., et al. (2010). In vivo
(2005). Effector and memory CD8+ T cell fate coupled by T-bet and eomeso-            regulation of Bcl6 and T follicular helper cell development. J. Immunol. 185,
dermin. Nat. Immunol. 6, 1236–1244.                                                  313–326.
Ji, Y., Pos, Z., Rao, M., Klebanoff, C.A., Yu, Z., Sukumar, M., Reger, R.N.,         Rahl, P.B., Lin, C.Y., Seila, A.C., Flynn, R.A., McCuine, S., Burge, C.B., Sharp,
Palmer, D.C., Borman, Z.A., Muranski, P., et al. (2011). Repression of the           P.A., and Young, R.A. (2010). c-Myc regulates transcriptional pause release.
DNA-binding inhibitor Id3 by Blimp-1 limits the formation of memory CD8+             Cell 141, 432–445.
T cells. Nat. Immunol. 12, 1230–1237.
                                                                                     Ravasi, T., Suzuki, H., Cannistraci, C.V., Katayama, S., Bajic, V.B., Tan, K.,
Johnston, R.J., Poholek, A.C., DiToro, D., Yusuf, I., Eto, D., Barnett, B., Dent,
                                                                                     Akalin, A., Schmeier, S., Kanamori-Katayama, M., Bertin, N., et al. (2010).
A.L., Craft, J., and Crotty, S. (2009). Bcl6 and Blimp-1 are reciprocal and
                                                                                     An atlas of combinatorial transcriptional regulation in mouse and man. Cell
antagonistic regulators of T follicular helper cell differentiation. Science 325,
                                                                                     140, 744–752.
1006–1010.
                                                                                     Rutishauser, R.L., Martins, G.A., Kalachikov, S., Chandele, A., Parish, I.A.,
Joshi, N.S., Cui, W., Chandele, A., Lee, H.K., Urso, D.R., Hagman, J., Gapin, L.,
                                                                                     Meffre, E., Jacob, J., Calame, K., and Kaech, S.M. (2009). Transcriptional
and Kaech, S.M. (2007). Inflammation directs memory precursor and short-
                                                                                     repressor Blimp-1 promotes CD8(+) T cell terminal differentiation and
lived effector CD8(+) T cell fates via the graded expression of T-bet transcrip-
                                                                                     represses the acquisition of central memory T cell properties. Immunity 31,
tion factor. Immunity 27, 281–295.
                                                                                     296–308.
Kaech, S.M., and Cui, W. (2012). Transcriptional control of effector and
                                                                                     Shin, H., Blackburn, S.D., Intlekofer, A.M., Kao, C., Angelosanto, J.M.,
memory CD8+ T cell differentiation. Nat. Rev. Immunol. 12, 749–761.
                                                                                     Reiner, S.L., and Wherry, E.J. (2009). A role for the transcriptional repressor
Kalia, V., Sarkar, S., Subramaniam, S., Haining, W.N., Smith, K.A., and
                                                                                     Blimp-1 in CD8(+) T cell exhaustion during chronic viral infection. Immunity
Ahmed, R. (2010). Prolonged interleukin-2Ralpha expression on virus-spe-
                                                                                     31, 309–320.
cific CD8+ T cells favors terminal-effector differentiation in vivo. Immunity
32, 91–103.                                                                          Vahedi, G., Kanno, Y., Sartorelli, V., and O’Shea, J.J. (2013). Transcription fac-
                                                                                     tors and CD4 T cells seeking identity: masters, minions, setters and spikers.
Kao, C., Oestreich, K.J., Paley, M.A., Crawford, A., Angelosanto, J.M., Ali,
                                                                                     Immunology 139, 294–298.
M.A., Intlekofer, A.M., Boss, J.M., Reiner, S.L., Weinmann, A.S., and
Wherry, E.J. (2011). Transcription factor T-bet represses expression of the          Walsh, J.C., DeKoter, R.P., Lee, H.J., Smith, E.D., Lancki, D.W., Gurish, M.F.,
inhibitory receptor PD-1 and sustains virus-specific CD8+ T cell responses           Friend, D.S., Stevens, R.L., Anastasi, J., and Singh, H. (2002). Cooperative
during chronic infection. Nat. Immunol. 12, 663–671.                                 and antagonistic interplay between PU.1 and GATA-2 in the specification of
Min, I.M., Waterfall, J.J., Core, L.J., Munroe, R.J., Schimenti, J., and Lis, J.T.   myeloid cell fates. Immunity 17, 665–676.
(2011). Regulating RNA polymerase pausing and transcription elongation               Wherry, E.J., Blattman, J.N., Murali-Krishna, K., van der Most, R., and Ahmed,
in embryonic stem cells. Genes Dev. 25, 742–754.                                     R. (2003). Viral persistence alters CD8 T-cell immunodominance and tissue
O’Shea, J.J., and Paul, W.E. (2010). Mechanisms underlying lineage commit-           distribution and results in distinct stages of functional impairment. J. Virol.
ment and plasticity of helper CD4+ T cells. Science 327, 1098–1102.                  77, 4911–4927.
Obar, J.J., Khanna, K.M., and Lefrançois, L. (2008). Endogenous naive               Xiao, N., Eto, D., Elly, C., Peng, G., Crotty, S., and Liu, Y.C. (2014). The E3 ubiq-
CD8+ T cell precursor frequency regulates primary and memory responses               uitin ligase Itch is required for the differentiation of follicular helper T cells. Nat.
to infection. Immunity 28, 859–869.                                                  Immunol. 15, 657–666.
Oestreich, K.J., and Weinmann, A.S. (2012). Master regulators or lineage-            Yang, C.Y., Best, J.A., Knell, J., Yang, E., Sheridan, A.D., Jesionek, A.K., Li,
specifying? Changing views on CD4+ T cell transcription factors. Nat. Rev.           H.S., Rivera, R.R., Lind, K.C., D’Cruz, L.M., et al. (2011). The transcriptional
Immunol. 12, 799–804.                                                                regulators Id2 and Id3 control the formation of distinct memory CD8+ T cell
Oven, I., Brdicková, N., Kohoutek, J., Vaupotic, T., Narat, M., and Peterlin,       subsets. Nat. Immunol. 12, 1221–1229.
B.M. (2007). AIRE recruits P-TEFb for transcriptional elongation of target           Yusuf, I., Kageyama, R., Monticelli, L., Johnston, R.J., Ditoro, D., Hansen, K.,
genes in medullary thymic epithelial cells. Mol. Cell. Biol. 27, 8815–8823.          Barnett, B., and Crotty, S. (2010). Germinal center T follicular helper cell IL-4
Oxenius, A., Bachmann, M.F., Zinkernagel, R.M., and Hengartner, H. (1998).           production is dependent on signaling lymphocytic activation molecule recep-
Virus-specific MHC-class II-restricted TCR-transgenic mice: effects on               tor (CD150). J. Immunol. 185, 190–202.
humoral and cellular immune responses after viral infection. Eur. J. Immunol.        Zhou, P., Shaffer, D.R., Alvarez Arias, D.A., Nakazaki, Y., Pos, W., Torres, A.J.,
28, 390–400.                                                                         Cremasco, V., Dougan, S.K., Cowley, G.S., Elpek, K., et al. (2014). In vivo dis-
Peterlin, B.M., and Price, D.H. (2006). Controlling the elongation phase of tran-    covery of immunotherapy targets in the tumour microenvironment. Nature 506,
scription with P-TEFb. Mol. Cell 23, 297–305.                                        52–57.
Pipkin, M.E., and Rao, A. (2009). SnapShot: effector and memory T cell differ-       Zuber, J., Shi, J., Wang, E., Rappaport, A.R., Herrmann, H., Sison, E.A.,
entiation. Cell 138, e1–e2.                                                          Magoon, D., Qi, J., Blatt, K., Wunderlich, M., et al. (2011). RNAi screen iden-
Pipkin, M.E., Sacks, J.A., Cruz-Guilloty, F., Lichtenheld, M.G., Bevan, M.J.,        tifies Brd4 as a therapeutic target in acute myeloid leukaemia. Nature 478,
and Rao, A. (2010). Interleukin-2 and inflammation induce distinct transcrip-        524–528.




338 Immunity 41, 325–338, August 21, 2014 ª2014 Elsevier Inc.

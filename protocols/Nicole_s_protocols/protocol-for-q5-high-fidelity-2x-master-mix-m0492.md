---
title: "protocol-for-q5-high-fidelity-2x-master-mix-m0492"
description: "Extracted PCR protocol for amplification with Q5 High-Fidelity 2X Master Mix M0492."
order: 10
author: "Nicole Sharping"
date: last-modified
---

[Download the original PDF](protocol-for-q5-high-fidelity-2x-master-mix-m0492.pdf){.btn .btn-primary download="protocol-for-q5-high-fidelity-2x-master-mix-m0492.pdf"}


# protocol-for-q5-high-fidelity-2x-master-mix-m0492

## Page 1

```text
PCR Using Q5® High-Fidelity 2X Master Mix (NEB #M0492)
Materials Required but not Supplied
Q5® High-Fidelity 2X Master Mix
   Nuclease-free Water (NEB #B1500)

    Template DNA and associated forward and reverse primers


Overview
This protocol describes methods for PCR using Q5® High-Fidelity 2X Master Mix, which offers high fidelity (~280X higher than
Taq), resulting in ultra-low error rates. Please note that protocols with Q5® High-Fidelity DNA Polymerase may differ from
protocols with other polymerases. The conditions recommended below should be used for optimal performance.


Protocol
Reaction Setup:

 1. Assemble all reaction components on ice. Each component should be gently mixed before adding to the reaction. The
    entire reaction should be mixed again to ensure homogeneous, consistent mixture. Collect all liquid to the bottom of the
    tube with a quick centrifuge spin if necessary. Overlay the sample with mineral oil if using a PCR machine without a heated
    lid.


 2. Quickly transfer the reactions to a thermocycler preheated to the denaturation temperature (98°C) and begin
    thermocycling.

 Component                                    25 µl Reaction          50 µl Reaction             Final Concentration

 Q5 High-Fidelity 2X Master Mix               12.5 µl                 25 µl                      1X

 10 µM Forward Primer                         1.25 µl                 2.5 µl                     0.5 µM

 10 µM Reverse Primer                         1.25 µl                 2.5 µl                     0.5 µM

 Template DNA                                 variable                variable                   < 1,000 ng

 Nuclease-Free Water                          to 25 µl                to 50 µl



Thermocycling Conditions for a Routine PCR:

 STEP                                             TEMP                           TIME

 Initial Denaturation                             98°C                           30 seconds

 25–35 Cycles                                     98°C                           5–10 seconds

                                                  50–72°C*                       10–30 seconds

                                                  72°C                           20–30 seconds/kb
```

## Page 2

```text
 STEP                                              TEMP                          TIME

 Final Extension                                   72°C                          2 minutes

 Hold                                              4–10°C


*Use of the NEB Tm Calculator is highly recommended.

General Guidelines:
 1. Template:
    Use of high quality, purified DNA templates greatly enhances the success of PCR. Recommended amounts of DNA
    template for a 50 µl reaction are as follows:

        DNA                                                                 AMOUNT

        DNA Genomic                                                         1 ng–1 µg

        Plasmid or Viral                                                    1 pg–10 ng


 2. Primers:
    Oligonucleotide primers are generally 20–40 nucleotides in length and ideally have a GC content of 40–60%. Computer
    programs such as Primer3 can be used to design or analyze primers. The best results are typically seen when using each
    primer at a final concentration of 0.5 µM in the reaction. However, amplification of certain long, complex DNA targets (≥ 5
    kb) may benefit from using a lower primer concentration (~ 0.2 to 0.3 µM).


 3. Mg++ and additives:
    The Q5 High-Fidelity Master Mix contains 2.0 mM Mg++ when used at a 1X concentration. This is optimal for most PCR
    products generated with this master mix.


 4. Deoxynucleotides:
    The final concentration of dNTPs is 200 μM of each deoxynucleotide in the 1X Q5 High-Fidelity Master Mix. Q5 High-
    Fidelity DNA Polymerase cannot incorporate dUTP and is not recommended for use with uracil-containing primers or
    templates. Should uracil-containing primers or templates be used, we recommend Q5U® Hot Start High-Fidelity DNA
    Polymerase (NEB #M0515).


 5. Q5 High-Fidelity DNA Polymerase concentration:
    The concentration of Q5 High-Fidelity DNA Polymerase in the Q5 High-Fidelity 2X Master Mix has been optimized for best
    results under a wide range of conditions.

 6. Denaturation:
    An initial denaturation of 30 seconds at 98°C is sufficient for most amplicons from pure DNA templates. Longer
    denaturation times can be used (up to 3 minutes) for templates that require it.


    During thermocycling, the denaturation step should be kept to a minimum. Typically, a 5–10 second denaturation at 98°C is
    recommended for most templates.


 7. Annealing:
    Optimal annealing temperatures for Q5 High-Fidelity DNA Polymerase tend to be higher than for other PCR polymerases.
    The NEB Tm Calculator should be used to determine the annealing temperature when using this enzyme. Typically use a
    10–30 second annealing step at 3°C above the Tm of the lower Tm primer. A temperature gradient can also be used to
    optimize the annealing temperature for each primer pair.

    For high Tm primer pairs, two-step cycling without a separate annealing step can be used (see note 10).
```

## Page 3

```text
 8. Extension:
   The recommended extension temperature is 72°C. Extension times are generally 20–30 seconds per kb for complex,
   genomic samples, but can be reduced to 10 seconds per kb for simple templates (plasmid, E. coli, etc.) or complex
   templates < 1 kb. Extension time can be increased to 40 seconds per kb for cDNA or long, complex templates, if
   necessary.



                               Amplicon Size
       DNA Type
                          ≤ 6 kb           ≥ 6 kb

     gDNA             20-30s/kb        30-50 s/kb

     cDNA             30-40 s/kb       40-50 s/kb

     pDNA             10-15 s/kb       20-30 s/kb



   A final extension of 2 minutes at 72°C is recommended.


 9. Cycle number:
    Generally, 25–35 cycles yield sufficient product. For genomic amplicons, 30-35 cycles are recommended.


10. 2-step PCR:
   When primers with annealing temperatures ≥ 72°C are used, a 2-step thermocycling protocol (combining annealing and
   extension into one step) is possible.


11. Amplification of long products:
   When amplifying products > 6 kb, it is often helpful to increase the extension time to 40–50 seconds/kb.

12. PCR product:
    The PCR products generated using Q5 High-Fidelity 2X Master Mix have blunt ends. If cloning is the next step, then blunt-
   end cloning is recommended. If T/A-cloning is preferred, the DNA should be purified prior to A-addition, as Q5 High-Fidelity
   DNA Polymerase will degrade any overhangs generated.

   The Monarch® Spin PCR & DNA Cleanup Kit (5 μg) (NEB #T1130) is recommended as an efficient method for purification
   and concentration up to 5 μg of high-quality, double-stranded and single-stranded DNA.


   Addition of an untemplated -dA can be done with Taq DNA Polymerase (NEB #M0267) or Klenow exo– (NEB #M0212).




Related Resources
   Tm Calculator
```

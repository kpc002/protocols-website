---
title: "Agilent Brilliant II SYBR® Green QPCR Master Mix"
description: "Extracted Agilent instructions for preparing and running quantitative PCR with Brilliant II SYBR Green master mix."
order: 10
author: "Nicole Sharping"
date: last-modified
---

[Download the original PDF](Agilent%20Brilliant%20II%20SYBR%C2%AE%20Green%20QPCR%20Master%20Mix.pdf){.btn .btn-primary download="Agilent Brilliant II SYBR® Green QPCR Master Mix.pdf"}


# Agilent Brilliant II SYBR® Green QPCR Master Mix

## Page 1

```text
Brilliant II SYBR® Green QPCR Master Mix


Instruction Manual
Catalog #600828 (single kit), #600831 (10-pack kit)
Revision C.0




For Research Use Only. Not for use in diagnostic procedures.
600828-12
```

## Page 2

```text
LIMITED PRODUCT WARRANTY
This warranty limits our liability to replacement of this product. No other warranties of any kind,
express or implied, including without limitation, implied warranties of merchantability or fitness for
a particular purpose, are provided by Agilent. Agilent shall have no liability for any direct, indirect,
consequential, or incidental damages arising out of the use, the results of use, or the inability to use
this product.


ORDERING INFORMATION AND TECHNICAL SERVICES
     Email
     techservices@agilent.com
     World Wide Web
     www.genomics.agilent.com

     Telephone
      Location                                Telephone
      United States and Canada                800 227 9770
      Austria                                 01 25125 6800
      Benelux                                 02 404 92 22
      Denmark                                 45 70 13 00 30
      Finland                                 010 802 220
      France                                  0810 446 446
      Germany                                 0800 603 1000
      Italy                                   800 012575
      Netherlands                             020 547 2600
      Spain                                   901 11 68 90
      Sweden                                  08 506 4 8960
      Switzerland                             0848 8035 60
      UK/Ireland                              0845 712 5292
      All Other Countries                     Please visit www.agilent.com/genomics/contactus
```

## Page 3

```text
Brilliant II SYBR® Green QPCR Master Mix

CONTENTS
  Materials Provided .............................................................................................................................. 1
  Storage Conditions .............................................................................................................................. 1
  Additional Materials Required .......................................................................................................... 1
  Notices To Purchaser .......................................................................................................................... 2
  Introduction ......................................................................................................................................... 3
                SYBR® Green I Dye .............................................................................................................. 4
                Fluorescence Monitoring in Real-Time ................................................................................. 6
  Preprotocol Considerations ................................................................................................................ 8
                PCR Primers .......................................................................................................................... 8
                Reference Dye ....................................................................................................................... 8
                Magnesium Chloride ............................................................................................................. 9
                Data Acquisition with a Spectrofluorometric Thermal Cycler .............................................. 9
                Multiplex PCR ....................................................................................................................... 9
                Preventing Template Cross-Contamination........................................................................... 9
  Protocol .............................................................................................................................................. 10
                Preparing the Reactions ....................................................................................................... 10
                PCR Cycling Programs........................................................................................................ 11
                Dissociation Programs ......................................................................................................... 12
  Troubleshooting ................................................................................................................................ 14
  References .......................................................................................................................................... 15
  Endnotes ............................................................................................................................................. 15
  MSDS Information ............................................................................................................................ 15
  Quick-Reference Protocol ................................................................................................................ 16
```

## Page 4

```text
Brilliant II SYBR® Green QPCR Master Mix

MATERIALS PROVIDED
     Catalog #600828 (single kit), #600831 (10-pack kit)
         Materials provided (per kit)                                                                  Quantitya,b
         2× Brilliant II SYBR® Green QPCR Master Mixc                                                  2 × 2.5 ml
         Reference dyed, 1 mM                                                                              100 μl
     a
       Sufficient PCR reagents are provided for four hundred, 25-μl reactions.
     b
       Quantities listed are for a single kit. For 10-pack kits, each item is provided at 10 times the listed quantity.
     c
       The master mix contains nucleotide mix GATC.
     d
       The reference dye is light sensitive and should be kept away from light whenever possible.


STORAGE CONDITIONS
     All Components: Upon receipt, store all components at –20°C. Store the 2× master mix at 4°C after
          thawing. Once thawed, full activity is guaranteed for 6 months.

     Note         The SYBR Green I dye and the reference dye are light sensitive and should be kept away
                  from light whenever possible.


ADDITIONAL MATERIALS REQUIRED
     Spectrofluorometric thermal cycler
     Nuclease-free PCR-grade water

Revision C.0                                                                                  © Agilent Technologies, Inc. 2015.




Brilliant II SYBR® Green QPCR Master Mix                                                                                      1
```

## Page 5

```text
NOTICES TO PURCHASER
    This product is provided under an intellectual property license from Life Technologies Corporation.
    The purchase of this product conveys to the buyer the non-transferable right to use the purchased
    product and components of the product only in research conducted by the buyer (whether the buyer
    is an academic or for-profit entity). The sale of this product is expressly conditioned on the buyer not
    using the product or its components for any Commercial Purposes. Commercial Purposes means any
    activity by the buyer to generate revenue, which may include, but is not limited to use of the product
    or its components: (1) in manufacturing or in quality assurance or quality control; (2) to provide a
    service, information, or data for a fee or other consideration; (3) for therapeutic or prophylactic
    purposes; (4) for diagnostic use; and (5) for resale, whether or not such items are resold for use in
    research. For information on purchasing a license to this product for purposes other than research,
    contact Life Technologies Corporation, 5791 Van Allen Way, Carlsbad , CA 92008 USA or
    outlicensing@lifetech. com.

    NOTICE TO PURCHASER: LIMITED LICENSE
    Use of this product is covered by one or more of the following US patents and corresponding patent
    claims outside the US: 6,258,569, 6,171,785, 6,127,155, 6,030,787, 5,994,056, 5,876,930, 5,804,375,
    5,789,224, 5,773,258 (claims 1 and 6 only), 5,723,591, 5,677,152 (claims 1 to 23 only), 5,618,711,
    5,538,848, and claims outside the US corresponding to expired US Patent No. 5,079,352. The
    purchase of this product includes a limited, non-transferable immunity from suit under the foregoing
    patent claims for using only this amount of product for the purchaser’s own internal research. No
    right under any other patent claim and no right to perform commercial services of any kind,
    including without limitation reporting the results of purchaser’s activities for a fee or other
    commercial consideration, is conveyed expressly, by implication, or by estoppel. This product is for
    research use only. Diagnostic uses under Roche patents require a separate license from Roche.
    Further information on purchasing licenses may be obtained by contacting the Director of Licensing,
    Applied Biosystems, 850 Lincoln Centre Drive, Foster City, California 94404, USA.




2                                                              Brilliant II SYBR® Green QPCR Master Mix
```

## Page 6

```text
INTRODUCTION
                          Quantitative PCR is becoming increasingly important for gene expression
                          analysis. Many fluorescent chemistries are used to detect and quantitate
                          gene transcripts. One method for real-time quantitation uses
                          SYBR® Green I, a dye that fluoresces when bound nonspecifically to
                          double-stranded DNA. The fluorescence response may be monitored in a
                          linear fashion as PCR product is generated over a range of PCR cycles. The
                          Brilliant II SYBR Green QPCR master mix includes the components
                          necessary to carry out QPCR amplifications with SYBR Green detection.*
                          The improved Brilliant II formulation yields higher levels of final
                          fluorescence and earlier Ct values for many genomic DNA and cDNA
                          targets and the master mix format is ideal for high-throughput applications.
                          The Brilliant II master mix has been optimized for a faster two-step cycling
                          protocol that is 25% shorter than the protocol used with the original Brilliant
                          SYBR Green QPCR master mix. The Brilliant II master mix is also ideal for
                          quantification of cDNA in a 2-step QRT-PCR reaction when combined with
                          the AffinityScript QPCR cDNA Synthesis Kit.

                          The Brilliant II SYBR Green QPCR master mix has been optimized for
                          maximum performance on the Agilent Mx3000P and Mx3005P real-time
                          PCR systems and Agilent Mx4000 multiplex quantitative PCR system, as
                          well as on the ABI 7900HT real-time PCR instrument. In addition, excellent
                          results have been observed using most other QPCR platforms.

                          The Brilliant II SYBR Green QPCR master mix includes SureStart Taq
                          DNA polymerase, a modified version of Taq2000 DNA polymerase with hot
                          start capability. SureStart Taq DNA polymerase improves PCR
                          amplification reactions by decreasing background from nonspecific
                          amplification and increasing amplification of desired products. Using
                          SureStart Taq, hot start is easily incorporated into PCR protocols already
                          optimized with Taq DNA polymerase, with little modification of cycling
                          parameters or reaction conditions. A passive reference dye (an optional
                          reaction component) is provided in a separate tube, making the master mix
                          adaptable for many real-time QPCR platforms.



                          * Primers and template are not included.




Brilliant II SYBR® Green QPCR Master Mix                                                               3
```

## Page 7

```text
    SYBR® Green I Dye
                   The SYBR Green I dye1 has a high binding affinity to the minor groove of
                   double-stranded DNA (dsDNA). It has an excitation maximum at 497 nm
                   and an emission maximum at 520 nm. In the unbound state the dye exhibits
                   little fluorescence; however, when bound to dsDNA, the fluorescence
                   greatly increases, making it useful for the detection of product accumulation
                   during real-time PCR.

                   The presence of SYBR Green I allows the user to monitor the accumulation
                   of PCR products in real-time. During denaturation, all DNA becomes
                   single-stranded. At this stage, SYBR Green is free in solution and produces
                   little fluorescence. During the annealing step, the primers will hybridize to
                   the target sequence, resulting in dsDNA to which SYBR Green I can bind.
                   As the PCR primers are extended in the elongation phase, more DNA
                   becomes double-stranded, and a maximum amount of SYBR Green I is
                   bound (see Figure 1). The increase in fluorescence signal intensity depends
                   on the initial concentration of target present in the PCR reaction. An
                   important consideration when using SYBR Green I, however, is that signal
                   can also be generated from nonspecific dsDNA (e.g. primer-dimers and
                   spurious PCR products). The plateau resulting in low Ct values for the
                   samples containing target and high Ct values (or “no Ct” values) for the
                   controls containing no target should be chosen for analysis.

                   Because SYBR Green fluorescence depends on the presence of dsDNA, the
                   specificity of the reaction is determined entirely by the specificity of the
                   primers. Careful primer design and purification can minimize the effects of
                   any side-reaction products, leading to more reliable DNA quantification. For
                   some applications, HPLC-purified primers may generate better results.
                   During the initial stages of assay optimization, it is recommended that the
                   PCR products are analyzed on a gel to verify that the product of interest is
                   being generated and that there is a correlation between the gel and
                   fluorescence data.




4                                                   Brilliant II SYBR® Green QPCR Master Mix
```

## Page 8

```text
                                    PCR primers

                                                                                    Denaturing
                                                                                     unbound SYBR Green I Dye Molecules
     template strands




                                                                                     Annealing
                                                                                     SYBR Green I dye shows an
                                                                                     increase in fluorescence
                                                                                     when bound to double-
                                                                                     stranded DNA




                                                                                     Extension
                                                                                     Double-stranded PCR products
                                                                                     with SYBR Green I dye fully incorporated




                                  PCR cycling continues


    FIGURE 1 SYBR® GREEN I DYE HAS A HIGHER AFFINITY FOR DOUBLE-STRANDED DNA (DSDNA) THAN FOR SINGLE-STRANDED DNA OR
    RNA. UPON BINDING DSDNA, THE FLUORESCENCE YIELD OF SYBR® GREEN I INCREASES BY APPROXIMATELY 1000 FOLD, MAKING IT
    IDEAL FOR DETECTING THE ACCUMULATION OF DSDNA.




Brilliant II SYBR® Green QPCR Master Mix                                                                                    5
```

## Page 9

```text
    Fluorescence Monitoring in Real-Time
                    When fluorescence signal from a PCR reaction is monitored in real-time, the
                    results can be displayed as an amplification plot (see Figure 2, top panel),
                    which reflects the change in fluorescence during cycling. Studies have
                    shown that initial copy number can be quantitated during real-time PCR
                    analysis based on threshold cycle (Ct).2 Ct is defined as the cycle at which
                    fluorescence is determined to be statistically significant above background
                    (e.g., in Figure 2, the Ct of the “+ template” reaction is 24 and the Ct of the
                    “– template” reaction is 34). The threshold cycle has been shown to be
                    inversely proportional to the log of the initial copy number.2 The more
                    template that is initially present, the fewer the number of cycles it takes to
                    get to a point where the fluorescence signal is detectable above background.
                    Quantitative information based on threshold cycle is more accurate than
                    information based on endpoint determinations as it is based on a
                    measurement taken during the exponential phase of PCR amplification when
                    the PCR efficiency has yet to be influenced by limiting reagents, small
                    differences in reaction components, or cycling conditions.

                    In Figure 2, the Brilliant II SYBR Green QPCR master mix was used in a
                    no-template control reaction and a reaction containing genomic DNA
                    template. In the amplification plot (Figure 2, top panel) the reaction
                    containing template shows a significant increase in fluorescence and has a
                    Ct value of ≅ 24. The reaction without template has a Ct of 34. To determine
                    if this is true amplification due to template contamination of the reaction or
                    an increase in SYBR Green I fluorescence due to primer-dimer (or some
                    other nonspecific product) formation, a dissociation profile is generated (see
                    Figure 2, bottom panel). In the dissociation curve, PCR samples are
                    subjected to a stepwise increase in temperature from 55°C to 95°C;
                    fluorescence measurements are taken at every temperature increment. After
                    completion of the dissociation segment, fluorescence is plotted versus
                    temperature. For an easy interpretation of the dissociation profile the first
                    derivative should be displayed, i.e. –R´(T) or–Rn´(T). As the temperature
                    increases, the amplification products in each tube will melt according to
                    their composition. If primer-dimer or nonspecific products were made
                    during the amplification step, they will generally melt at a lower
                    temperature (defined as the Tm) than the desired products. The melting of
                    products results in a drop of fluorescence, which is due to SYBR Green
                    dissociation. The dissociation curve plot of these samples shows two
                    fluorescence peaks: one in the “– template” reaction centered around 76°C
                    (which corresponds to primer-dimer); and the other, in the “+ template”
                    reaction, centered around 81°C (which corresponds to amplicon). In this
                    way, the dissociation curve analysis of PCR products amplified in the
                    presence of SYBR Green I dye can be a very powerful tool in the
                    interpretation of fluorescence data. The results obtained from the
                    dissociation plot can also be used for the modification of cycling conditions
                    for future experiments. For example, if a primer-dimer was observed with a
                    Tm of 72°C, the extension step of the PCR can be raised to 74°C, thereby
                    reducing the signal from primer-dimers. This adjustment may not, however,
                    work with all targets, especially long amplicons.




6                                                     Brilliant II SYBR® Green QPCR Master Mix
```

## Page 10

```text
FIGURE 2 MX3000P QPCR INSTRUMENT AMPLIFICATION PLOT (TOP PANEL) AND DISSOCIATION CURVE (BOTTOM PANEL) OF A REACTION WITH
AND WITHOUT TEMPLATE DNA. WHEN THE AMPLIFIED PRODUCTS ARE SUBJECTED TO DISSOCIATION CURVE ANALYSIS, THE FLUORESCENCE PEAK
CORRESPONDING TO THE AMPLICON (CENTERED AROUND 81°C) IS DISTINGUISHABLE FROM THE PEAK DUE TO PRIMER-DIMER (CENTERED
AROUND 76°C).




Brilliant II SYBR® Green QPCR Master Mix                                                                               7
```

## Page 11

```text
PREPROTOCOL CONSIDERATIONS
    PCR Primers
                    It is critical in SYBR Green-based QPCR to minimize the formation of non-
                    specific amplification products. This issue becomes more prominent at low
                    target concentrations. Therefore, to maximize the sensitivity of the assay, it
                    is necessary to use the lowest concentration of primers possible without
                    compromising the efficiency of PCR. It is important to consider both the
                    relative concentrations of forward and reverse primers and the total primer
                    concentration. The optimal concentration of the upstream and downstream
                    PCR primers is the lowest concentration that results in the lowest Ct and an
                    adequate fluorescence for a given target concentration, with minimal or no
                    formation of primer-dimer. This concentration should be determined
                    empirically; generally, primer concentrations in the range of 200–600 nM
                    are satisfactory.

    Reference Dye
                    A passive reference dye is included in this kit and may be added to
                    compensate for non-PCR related variations in fluorescence. Fluorescence
                    from the passive reference dye does not change during the course of the
                    PCR reaction but provides a stable baseline to which samples are
                    normalized. In this way, the reference dye compensates for changes in
                    fluorescence between wells caused by slight volume differences in reaction
                    tubes. The excitation and emission wavelengths of the reference dye are
                    584 nm and 612 nm, respectively. Although addition of the reference dye is
                    optional when using the Mx3005P, Mx3000P or Mx4000 QPCR system,
                    with other instruments (including the ABI 7900HT and ABI PRISM® 7700)
                    the use of the reference dye may be required for optimal results.

                    Reference Dye Dilution Recommendations
                    Prepare fresh* dilutions of the reference dye prior to setting up the
                    reactions, and keep all tubes containing the reference dye protected from
                    light as much as possible. Make initial dilutions of the reference dye using
                    nuclease-free PCR-grade H2O. If you are using an Agilent Mx3000P or
                    Mx3005P real-time PCR systems or Mx4000 multiplex quantitative PCR
                    system, use the reference dye at a final concentration of 30 nM. If you are
                    using the ABI 7900HT or the ABI PRISM 7700 instruments, use the
                    reference dye at a final concentration of 300 nM. For other instruments, use
                    the following guidelines for passive reference dye optimization. For
                    instruments that allow excitation at ~584 nm (including most
                    tungsten/halogen lamp-based instruments and instruments equipped with a
                    ~584 nm LED), begin optimization using the reference dye at a final
                    concentration of 30 nM. For instruments that do not allow excitation near
                    584 nm, (including most laser-based instruments) begin optimization using
                    the reference dye at a final concentration of 300 nM.


                    * The diluted reference dye, if stored in a light-protected tube at 4°C, can be used within the
                      day for setting up additional assays.




8                                                            Brilliant II SYBR® Green QPCR Master Mix
```

## Page 12

```text
    Magnesium Chloride
                          The optimal MgCl2 concentration promotes maximal amplification of the
                          specific target amplicon with minimal nonspecific products and primer-
                          dimer formation. High levels of the Mg2+ ion tend to favor the formation of
                          nonspecific dsDNA, including primer-dimers. Therefore, when a SYBR
                          Green-based QPCR assay is being optimized, the MgCl2 levels should be as
                          low as possible, as long as the efficiency of amplification of the specific
                          target is not compromised (typically between 1.5 and 2.5 mM MgCl2). The
                          Brilliant II SYBR Green QPCR master mix contains MgCl2 at a
                          concentration of 2.5 mM (in the 1× solution), which is suitable for most
                          targets. The concentration may be increased, if desired, by adding a small
                          amount of a concentrated MgCl2 solution to the 1× experimental reaction at
                          the time of setup.

    Data Acquisition with a Spectrofluorometric Thermal Cycler
                          The instrument should be set to collect SYBR Green I data in real-time at
                          each cycle. How this is accomplished will depend on the software that
                          commands the particular instrument you are using. Consult the
                          manufacturer’s instruction manual for the instrument and software version
                          you are using.

                          When developing an assay, it is necessary to decide whether to use a 2-step
                          or a 3-step PCR protocol. We recommend a 2-step protocol for the Brilliant
                          II SYBR Green QPCR master mix, but a 3-step protocol may be helpful
                          when using primers with low melting temperatures. In a 2-step cycling
                          protocol, fluorescence data are collected during the combined
                          annealing/extension step. When using a 3-step protocol, it is prudent to
                          collect fluorescence data at both the annealing step and the extension step of
                          the PCR reaction. For subsequent experiments, the plateau resulting in low
                          Ct values for the samples containing target and high Ct values (or “no Ct”
                          values) for the controls containing no target should be chosen for analysis.
                          For longer amplicons, fluorescence measurements taken during the
                          extension step generally yield more useful data.

    Multiplex PCR
                          Multiplex PCR is the amplification of more than one target in a single
                          polymerase chain reaction.3 Because SYBR Green I dye fluoresces in the
                          presence of any dsDNA, multiplexing with the Brilliant II SYBR Green
                          QPCR master mix is not recommended.

    Preventing Template Cross-Contamination
                          Take precautions to minimize the potential for carryover of nucleic acids
                          from one experiment to the next. Use separate work areas and pipettors for
                          pre- and post-amplification steps. Use positive displacement pipets or
                          aerosol-resistant pipet tips.




Brilliant II SYBR® Green QPCR Master Mix                                                              9
```

## Page 13

```text
PROTOCOL
     Preparing the Reactions
                     Notes     Once the tube containing the Brilliant II SYBR Green QPCR
                               master mix is thawed, store it on ice while setting up the reactions.
                               Following initial thawing of the master mix, store the unused
                               portion at 4°C. Multiple freeze-thaw cycles should be avoided.
                               SYBR Green I dye (present in the master mix) is light-sensitive;
                               solutions containing the master mix should be protected from
                               light whenever possible.

                               It is prudent to set up a no-template control reaction to screen for
                               contamination of reagents or false amplification.

                     1.   If the reference dye will be included in the reaction, (optional), dilute
                          the dye solution provided 1:500 (Mx3000P, Mx3005P, and Mx4000
                          instruments) or 1:50 (ABI PRISM 7700 and ABI 7900HT
                          instruments) using nuclease-free PCR-grade H2O. For other
                          instruments, use the guidelines in the Reference Dye section under
                          Preprotocol Considerations. Keep all solutions containing the
                          reference dye protected from light.

                          Note      If using a system other than the Mx3000P, Mx3005P or
                                    Mx4000 instruments, the use of the reference dye may be
                                    required for optimal results.

                     2.   Prepare the experimental reactions by combining the following
                          components in order. Prepare a single reagent mixture for duplicate
                          experimental reactions and duplicate no-template-controls (plus at least
                          one reaction volume excess), using multiples of each component listed
                          below.
                          Experimental Reaction
                               Nuclease-free PCR-grade water to adjust the final volume to 25 μl
                                   (including experimental DNA)
                                12.5 μl of 2× Brilliant II SYBR Green QPCR master mix
                                   x μl of upstream primer (200–600 nM final concentration)
                                   x μl of downstream primer (200–600 nM final concentration)
                               0.375 μl of diluted reference dye (optional)

                          Note      A total reaction volume of 50 µl may also be used.

                     3.   Gently mix without creating bubbles (do not vortex), then distribute the
                          mixture to the individual experimental reaction tubes.

                     4.   Add x μl of experimental gDNA, cDNA, or plasmid DNA to each
                          reaction.



10                                                    Brilliant II SYBR® Green QPCR Master Mix
```

## Page 14

```text
                          5.   Gently mix the reactions without creating bubbles (do not vortex).

                               Note         Bubbles interfere with fluorescence detection.

                          6.   Centrifuge the reactions briefly.

    PCR Cycling Programs

                          7. Place the reactions in the instrument and run one of the PCR programs
                             listed below. We recommend a two-step cycling protocol for most
                             primer/template systems. For targets <150 bp in length, the fast protocol
                             with two-step cycling may be used to decrease run times without
                             compromising amplification efficiency. For primers with low melting
                             temperatures, the three-step cycling protocol may be optimal.

                               Recommended Protocol with Two-Step Cycling (All Targets)
                                   Cycles                    Duration of cycle           Temperature
                                    1                        10 minutes   a
                                                                                         95°C
                                   40                        30 seconds                  95°C
                                                             1.0 minuteb                 60°C
                               a
                                 Initial 10 minute incubation is required to activate the DNA polymerase.
                               b
                                 Set the temperature cycler to detect and report fluorescence during the
                                 annealing/extension step of each cycle.


                               Fast Protocol with Two-Step Cycling (Targets <150 bp)
                                   Cycles                    Duration of cycle           Temperature
                                    1                        15 minutes   a
                                                                                         95°C
                                   40                        10 seconds                  95°C
                                                              30 secondsb                  60°C
                               a
                                 Initial 15 minute incubation is required to activate the DNA polymerase.
                               b
                                 Set the temperature cycler to detect and report fluorescence during the
                                 annealing/extension step of each cycle.


                               Alternative Protocol with Three-Step Cycling (All Targets)
                                   Cycles                    Duration of cycle           Temperature
                                    1                        10 minutesa                 95°C
                                   40                        30 seconds                  95°C
                                                             1.0 minute   b
                                                                                         50–60°Cc
                                                              30 secondsb                  72°C
                               a
                                 Initial 10 minute incubation is required to activate the DNA polymerase.
                               b
                                 Set the temperature cycler to detect and report fluorescence during the annealing
                                 and extension step of each cycle.
                               c
                                 Choose an appropriate annealing temperature for the primer set used.




Brilliant II SYBR® Green QPCR Master Mix                                                                        11
```

## Page 15

```text
     Dissociation Programs

                     8.   If using an Agilent Mx3000P, Mx3005P or Mx4000 instrument, follow
                          the dissociation guidelines below. If using another instrument, follow
                          the manufacturer’s guidelines for generating dissociation curves.

                     Dissociation Program for All Targets (Mx3000P, Mx3005P)




                     Prior to the dissociation curve, incubate the reactions for 1 minute at 95°C to
                     denature the PCR products. Ramp down to 55°C. For the dissociation curve,
                     ramp up the temperature from 55°C to 95°C (at the instrument default rate
                     of 0.2°C/sec) and collect fluorescence data continuously on the 55–95°C
                     ramp. Figure 3 shows how to set the Thermal Profile for the dissociation
                     curve program on the Mx3000P and Mx3005P instruments.
                     FIGURE 3 DISSOCIATION PROGRAM SETTINGS ON THE MX3000P AND MX3005P REAL-TIME PCR
                     INSTRUMENTS.




12                                                     Brilliant II SYBR® Green QPCR Master Mix
```

## Page 16

```text
                          Dissociation Program for All Targets (Mx4000)
                          Incubate the amplified product for 1 minute at 95°C, ramping down to 55°C
                          at a rate of 0.2°C/sec. For the dissociation curve, complete 81 cycles of
                          incubation where the temperature is increased by 0.5°C/cycle, beginning at
                          55°C and ending at 95°C. The duration of each cycle should be set to
                          30 seconds. Figure 4 shows how to correctly set the Plateau Properties for
                          the dissociation curve program on the Mx4000 instrument. To access the
                          Plateau Properties dialog box for the dissociation curve segment, double-
                          click on the solid line corresponding to the 55° plateau in Segment 4 of the
                          Thermal Profile Setup window.




                          FIGURE 4 SETTINGS FOR THE DISSOCIATION PROGRAM PLATEAU PROPERTIES ON THE MX4000
                          MULTIPLEX QUANTITATIVE PCR INSTRUMENT.




Brilliant II SYBR® Green QPCR Master Mix                                                              13
```

## Page 17

```text
TROUBLESHOOTING
Observation                     Suggestion(s)
No (or little) increase in      Optimize the primer concentration.
fluorescence with cycling       Ensure that the correct concentration and amount of template was used and that the
                                template sample is of good quality. If unsure, make new serial dilutions of template
                                before repeating PCR. It may also be possible to check for PCR inhibitors by adding this
                                target into an assay that is known to work.
                                Ensure the annealing/extension time (2-step cycling protocol) or extension time (3-step
                                cycling protocol) is sufficient. Check the length of the amplicon and increase the time if
                                necessary.
                                Use a sufficient number of cycles in the PCR reaction.
                                If using a 3-step cycling protocol, ensure the annealing temperature is appropriate for
                                the primers used.
                                Gel analyze PCR product to determine if there was successful amplification.
                                Ensure the correct dilution of reference dye was used.
                                SureStart Taq DNA polymerase was not activated. Ensure that the 10 minute incubation
                                (15 minute for fast cycling) at 95°C was performed as part of the cycling parameters.
                                The MgCl2 concentration is not optimal. The MgCl2 concentration in the 1× Brilliant II
                                SYBR Green QPCR master mix is 2.5 mM. It is possible to add small amounts of
                                concentrated MgCl2 to the experimental reactions to increase the MgCl2 concentration,
                                if desired.
No (or little) increase in      Increase the length of the annealing/extension step (2-step cycling protocol) or the
fluorescence with long          extension step (3-step cycling protocol).
amplicons (>400 bp)
There is a large abundance of   Increase the annealing temperature (3-step cycling protocol) above the Tm of the
primer-dimer and nonspecific    primer-dimer and/or nonspecific products.
PCR products                    Re-design primers.




14                                                                     Brilliant II SYBR® Green QPCR Master Mix
```

## Page 18

```text
REFERENCES
                          1.   Molecular Probes, Inc., at http://www.probes.com/media/pis/mp07567.pdf.
                          2.   Higuchi, R., Fockler, C., Dollinger, G. and Watson, R. (1993) Biotechnology (N Y)
                               11(9):1026-30.
                          3.   Edwards, M. and Gibbs, R. (1995). Multiplex PCR. In PCR Primer: A Laboratory
                               Manual, C. W. Dieffenbach and G. S. Dveksler (Eds.), pp. 157-171. Cold Spring
                               Harbor Laboratory Press, Plainview, NY.




ENDNOTES
                          ABI PRISM® is a registered trademark of Applied Biosystems.
                          SYBR® is a registered trademark of Molecular Probes, Inc.


MSDS INFORMATION
Material Safety Data Sheets (MSDSs) are provided online at http://www.genomics.agilent.com. MSDS
documents are not included with product shipments.




Brilliant II SYBR® Green QPCR Master Mix                                                                    15
```

## Page 19

```text
BRILLIANT II SYBR® GREEN QPCR MASTER MIX
     Catalog #600828, #600831

QUICK-REFERENCE PROTOCOL
     Prior to the experiment, it is prudent to carefully optimize experimental conditions and to include
     controls at every stage. See Preprotocol Considerations for details.

     1.   If the passive reference dye will be included in the reaction (optional), dilute 1:500 (Mx3000P or
          Mx4000 instrument) or 1:50 (ABI 7900HT or ABI PRISM 7700 instrument). Keep all solutions
          containing the reference dye protected from light.

          Note     If using a system other than the Mx4000, Mx3000P or Mx3005P instruments, the use of
                   the reference dye may be required for optimal results.

     2.   Thaw the Brilliant II SYBR Green QPCR master mix and store on ice. Following initial thawing of
          the master mix, store the unused portion at 4°C.

          Note     Multiple freeze-thaw cycles should be avoided. SYBR Green I dye (present in the
                   master mix) is light-sensitive; solutions containing the master mix should be
                   protected from light whenever possible.

     3.   Prepare the experimental reaction by adding the following components in order:
           Experimental Reaction
           Nuclease-free PCR-grade H2O to adjust the final volume to 25 μl (including experimental DNA)
            12.5 μl of 2× Brilliant II SYBR Green QPCR master mix
                x μl of upstream primer (200–600 nM final concentration is recommended)
                x μl of downstream primer (200–600 nM final concentration is recommended)
           0.375 μl of diluted reference dye from step 1 (optional)

          Note     Total reaction volumes of 50 μl may also be used.

     4.   Gently mix the reaction without creating bubbles (bubbles interfere with fluorescence
          detection; do not vortex).

     5.   Add x μl of experimental gDNA, cDNA, or plasmid DNA to each experimental reaction.

     6.   Gently mix the reaction without creating bubbles (do not vortex).

     7.   Centrifuge the reaction briefly.




16
```

## Page 20

```text
     8.   Place the reaction in the instrument and run the appropriate PCR program below.

          Recommended Protocol with Two-Step Cycling (All Targets)
              Cycles                      Duration of cycle           Temperature
                1                         10 minutes   a
                                                                      95°C
              40                          30 seconds                  95°C
                                         1.0 minuteb                  60°C
          a
            Initial 10 minute incubation is required to activate the DNA polymerase.
          b
            Set the temperature cycler to detect and report fluorescence during the annealing/extension step of each cycle.


          Fast Protocol with Two-Step Cycling (Targets <150 bp)
              Cycles                      Duration of cycle           Temperature
                1                         15 minutes   a
                                                                      95°C
              40                          10 seconds                  95°C
                                          30 secondsb                 60°C
          a
              Initial 15 minute incubation is required to activate the DNA polymerase.
          b
              Set the temperature cycler to detect and report fluorescence during the annealing/extension step of each cycle.


          Alternative Protocol with Three-Step Cycling (All Targets)
              Cycles                      Duration of cycle           Temperature
                1                         10 minutesa                 95°C
              40                          30 seconds                  95°C
                                          1.0 minute   b
                                                                      50–60°Cc
                                          30 secondsb                 72°C
          a
            Initial 10 minute incubation is required to activate the DNA polymerase.
          b
            Set the temperature cycler to detect and report fluorescence during the annealing and extension step of each cycle.
          c
            Choose an appropriate annealing temperature for the primer set used.



     9.   Follow the dissociation guidelines below for the instrument used.


          Dissociation Program for All Targets (Mx3000P/Mx3005P Instruments)
          Incubate the reactions for 1 minute at 95°C, ramping down to 55°C. For the dissociation curve,
          ramp up the temperature from 55°C to 95°C (at the instrument default rate of 0.2°C/sec) and
          collect fluorescence data continuously on the 55–95°C ramp.

          Dissociation Program for All Targets (Mx4000 Instrument)
          Incubate the amplified product for 1 minute at 95°C, ramping down to 55°C at a rate of
          0.2°C/sec, followed by 81 cycles of incubation where the temperature is increased by
          0.5°C/cycle, beginning at 55°C and ending at 95°C. Set the cycle duration to 30 seconds/cycle.

          Dissociation Program for All Targets (Other Instruments)
          Follow manufacturer’s guidelines for setting up dissociation depending on the instrument’s
          software version.



17
```

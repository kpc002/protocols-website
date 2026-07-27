---
title: "WB-beginner"
order: 10
author: "Goldrath Lab"
date: last-modified
---

[Download the original PDF](WB-beginner.pdf){.btn .btn-primary download="WB-beginner.pdf"}



# WB-beginner

WESTERN BLOTTING - A BEGINNER’S GUIDE
Western blotting identifies with specific antibodies proteins that have been separated from one another according
to their size by gel electrophoresis. The blot is a membrane, almost always of nitrocellulose or PVDF
(polyvinylidene fluoride). The gel is placed next to the membrane and application of an electrical current induces
the proteins in the gel to move to the membrane where they adhere. The membrane is then a replica of the gel’s
protein pattern, and is subsequently stained with an antibody.

The following guide discusses the entire process of producing a Western blot: sample preparation, gel
electrophoresis, transfer from gel to membrane, and immunostain of the blot. The guide is intended to be an
educational resource to introduce the method rather than a benchtop protocol, but a more concise document
suitable for consulting during an experiment can be composed by selecting and editing relevant material. Consult
the manufacturers of your electophoresis and transfer equipment for more detailed instructions on these steps.

A. Sample preparation
        1. Lysis buffers
        2. Protease and phosphatase inhibitors
        3. Preparation of lysate from cell culture
        4. Preparation of lysate from tissues
        5. Determination of protein concentration
        6. Preparation of samples for loading into gels

B. Electrophoresis
        1. Preparation of PAGE gels
        2. Positive controls
        3. Molecular weight markers
        4. Loading samples and running the gel
        5. Use of loading controls

C. Transfer of proteins and staining (Western blotting)
        1. Visualization of proteins in gels
        2. Transfer
        3. Visualization of proteins in membranes: Ponceau Red
        4. Blocking the membrane
        5. Incubation with the primary antibody
        6. Incubation with the secondary antibody
        7. Development methods

D. References


A. Sample preparation
1. Lysis buffers

To prepare samples for running on a gel, cells and tissues need to be lysed to release the proteins of interest. This
solubilizes the proteins so they can migrate individually through a separating gel. There are many recipes for lysis
buffers but a few will serve for most Western blotting experiments. In brief, they differ in their ability to solubilize
proteins, with those containing sodium dodecyl sulfate and other ionic detergents considered to be the harshest
and therefore most likely to give the highest yield.

Most Abcam antibodies recognise reduced and denatured protein and should be used under reducing and
denaturing conditions. It is important to note though that some antibodies will only recognize a protein in its native,
www.abcam.com/technical

non-denatured form and will not recognize a protein that has been extracted with a denaturing detergent (SDS,
deoxycholate, and somewhat less denaturing, Triton X-100 and NP-40).

The main consideration then when choosing a lysis buffer is whether the antibody one has chosen will recognize
denatured samples. When this is not the case, it will be noted on the antibody datasheet, and buffers without
detergent or with relatively mild non-ionic detergents (NP-40, Triton X-100) should be used.

Protein Location And Lysis Buffer Choice

Protein location                         Buffer recommended
Whole Cell                               NP-40 or RIPA
Cytoplasmic (soluble)                    Tris-HCl
Cytoplasmic (cytoskeletal bound)         Tris-Triton
Membrane bound                           NP-40 or RIPA
Nuclear                                  RIPA or use nuclear fraction protocol*
Mitochondria                             RIPA or use mitochondrial fraction protocol*

* Proteins that are found exclusively or predominantly in a sub-cellular location can be enriched in a lysate of the
sub-cellular fraction compared to whole cell or tissue lysates. This can be useful when trying to obtain a signal for a
weakly-expressed protein. For instance, a nuclear protein will be a larger proportion of the total protein in a nuclear
lysate than it will be in a whole-cell or whole-tissue lysate, making it possible to load more of the protein per gel
lane. Another advantage is the removal of potentially cross-reactive proteins present in the unused fractions.
Please consult our separate protocols for sub-cellular fractionation.

Nonidet-P40 (NP40) buffer
       150 mM sodium chloride
       1.0% NP-40 (Triton X-100 can be substituted for NP-40)
       50 mM Tris, pH 8.0

This is a popular buffer for studying proteins that are cytoplasmic, or membrane-bound, or for whole cell extracts. If
there is concern that the protein of interest is not being completely extracted from insoluble material or aggregates,
RIPA buffer may be more suitable, as it contains ionic detergents that may more readily bring the proteins into
solution.

RIPA buffer (Radio Immuno Precipitation Assay buffer)
       150 mM sodium chloride
       1.0% NP-40 or Triton X-100
       0.5% sodium deoxycholate
       0.1% SDS (sodium dodecyl sulphate)
       50 mM Tris, pH 8.0

RIPA buffer is also useful for whole cell extracts and membrane-bound proteins, and may be preferable to NP-40
or Triton X100-only buffers for extracting nuclear proteins. It will disrupt protein-protein interactions and may
therefore be problematic for immunoprecipitations/pull down assays.

The 10% sodium deoxycholate stock solution (5 g into 50 ml) must be protected from light.


In cases where it is important to preserve protein-protein interactions or to minimize denaturation
(for example, when it is known that the antibody to be used will only recognize a non-denatured epitope),
a buffer without ionic detergents (e.g. SDS) and ideally without non-ionic detergents (e.g. Triton X-100) should be
used. Cell lysis with detergent-free buffer is achieved by mechanical shearing, often with a Dounce homogenizer or
by passing cells through a syringe tip. In these cases a simple Tris buffer will suffice, but as noted above, buffers
with detergents are required to release membrane- or cytoskeleton- bound proteins.

www.abcam.com/technical

Tris-HCl buffer
        20 mM Tris-HCl, pH 7.5

Tris-Triton buffer:
(Cytoskeletal proteins)
        10 mM Tris, pH 7.4
        100 mM NaCl
        1 mM EDTA
        1 mM EGTA
        1% Triton X-100
        10% glycerol
        0.1% SDS
        0.5% deoxycholate
                                      o                                                                     o
All four of these buffers will keep at 4 C for several weeks or for up to a year aliquotted and stored at -20 C.

2. Protease and phosphatase inhibitors

As soon as lysis occurs, proteolysis, dephosphorylation and denaturation begin. These events can be slowed down
tremendously if samples are kept on ice or at 4°C at all times and appropriate inhibitors are added fresh to the lysis
buffer.

Ready-to-use cocktails of inhibitors from various suppliers are available but you can make your own cocktail.
                                                                                                    o
Inhibitor          Protease/phosphatase              Final concentration       Stock (store at -20 C)
                   Inhibited                         in lysis buffer
Aprotinin          Trypsin, Chymotrypsin,            2 µg/ml                   Dilute in water, 10 mg/ml. Do not re-
                   Plasmin                                                     use thawed aliquots
Leupeptin          Lysosomal                         5-10 µg/ml                Dilute in water. Do not re-use once
                                                                               defrosted.
Pepstatin A        Aspartic proteases                1 µg/ml                   Dilute in methanol, 1mM.

PMSF               Serine, Cysteine proteases        1 mM                      Dilute in ethanol. You can re-use the
                                                                               same aliquot.
EDTA               Metalloproteases that require     5 mM                      Dilute in dH2O, 0.5M. Adjust pH to 8.0.
                   Mg++ and Mn++
EGTA               Metalloproteases that require     1 mM                      Dilute in dH2O, 0.5M. Adjust pH to 8.0.
                   Ca++
Na Fluoride        Serine/Threonine                  5-10 mM                   Dilute in water. Do not re-use once
                   phosphatases                                                defrosted.
Na                 Tyrosine phosphatases             1 mM                      Dilute in water. Do not re-use once
Orthovanadate                                                                  defrosted.

Sodium orthovanadate preparation
All steps to be performed in a fume hood.

1.    Prepare a 100 mM solution in double distilled water.
2.    Set pH to 9.0 with HCl.
3.    Boil until colorless. Minimize volume change due to evaporation by covering loosely.
4.    Cool to room temperature.
5.    Set pH to 9.0 again.
6.    Boil again until colorless.
7.    Repeat this cycle until the solution remains at pH 9.0 after boiling and cooling.
8.    Bring up to the initial volume with water.
9.    Store in aliquots at - 20°C. Discard if samples turn yellow
www.abcam.com/technical

3. Preparation of lysate from cell culture

1. Place the cell culture dish in ice and wash the cells with ice-cold PBS.
                                                              7                          2                      6
2. Drain the PBS, then add ice-cold lysis buffer (1 ml per 10 cells/100mm dish/150cm flask; 0.5ml per 5x10
                      2
cells/60mm dish/75cm flask).

3. Scrape adherent cells off the dish using a cold plastic cell scraper, then gently transfer the cell suspension into a
pre-cooled microfuge tube.

4. Maintain constant agitation for 30 minutes at 4°C.

5. Centrifuge in a microcentrifuge at 4°C.

You may have to vary the centrifugation force and time depending on the cell type; a guideline is 20 minutes at
12,000 rpm but this must be determined by the end-user (e.g. leukocytes need a very light centrifugation).

6. Gently remove the tubes from the centrifuge and place on ice, aspirate the supernatant and place in a fresh
tube kept on ice, and discard the pellet.

4. Preparation of lysate from tissues

1. Dissect the tissue of interest with clean tools, on ice preferably, and as quickly as possible to prevent
degradation by proteases.

2. Place the tissue in round-bottom microfuge tubes or Eppendorf tubes and immerse in liquid nitrogen to “snap
freeze”. Store samples at -80°C for later use or keep on ice for immediate homogenization.

For a ~5 mg piece of tissue, add ~300 µl lysis buffer rapidly to the tube, homogenize with an electric
homogenizer, rinse the blade twice with another 2x300 µl lysis buffer, then maintain constant agitation for 2
hours at 4°C (e.g place on an orbital shaker in the fridge). Volumes of lysis buffer must be determined in
relation to the amount of tissue present (protein extract should not be too diluted to avoid loss of protein
and large volumes of samples to be loaded onto gels. The minimum concentration is 0.1 mg/ml, optimal
concentration is 1-5 mg/ml).

3. Centrifuge for 20 min at 12000 rpm at 4°C in a microcentrifuge. Gently remove the tubes from the centrifuge
and place on ice, aspirate the supernatant and place in a fresh tube kept on ice; discard the pellet.


The buffer (with inhibitors) should be ice-cold prior to homogenization.

5. Determination of protein concentration

Perform a Bradford assay, a Lowry assay or a BCA assay. Bovine serum albumin (BSA) is a frequently-used
protein standard.

Once you have determined the concentration of each sample, you can freeze them at -20°C or -80°C
for later use or prepare for immunoprecipitation or for loading onto a gel.




www.abcam.com/technical

6. Preparation of samples for loading into gels: denatured and native, reduced and non-reduced.

a) Denatured, reduced samples

Antibodies typically recognize a small portion of the protein of interest (referred to as the epitope) and this domain
may reside within the 3D conformation of the protein. To enable access of the antibody to this portion it is
necessary to unfold the protein, i.e. denature it.

To denature, use a loading buffer with the anionic denaturing detergent sodium dodecyl sulfate (SDS), and boil
the mixture at 95-100°C for 5 minutes. Heating at 70°C for 5-10 minutes is also acceptable and may be preferable
when studying multi-pass membrane proteins. These tend to aggregate when boiled and the aggregates may not
enter the gel efficiently.

The standard loading buffer is called 2X Laemmli buffer, first described in Nature, 1970 Aug 15;227(5259):680-5. It
can also be made at 4X and 6X strength to minimize dilution of the samples. The 2X is to be mixed in a 1:1 ratio
with the sample.

Laemmli 2X buffer

4% SDS
10% 2-mercaptoehtanol
20% glycerol
0.004% bromophenol blue
0.125 M Tris HCl

Check the pH and bring it to pH 6.8.

When SDS is used with proteins, all of the proteins become negatively charged by their attachment to the
SDS anions. SDS denatures proteins by “wrapping around” the polypeptide backbone. SDS binds to
proteins fairly specifically in a mass ratio of 1.4:1. In so doing, SDS confers a negative charge to the
polypeptide in proportion to its length - i.e., the denatured polypeptides become “rods” of negative charge
clouds with equal charge or charge densities per unit length.

In denaturing SDS-PAGE separations, therefore, migration is determined not by intrinsic electrical charge of the
polypeptide, but by molecular weight. SDS grade is of utmost importance: a protein stained background along
individual gel tracts with indistinct or slightly distinct protein bands are indicative of old or poor quality SDS.

It is usually necessary to reduce disulphide bridges in proteins before they adopt the random-coil configuration
necessary for separation by size by using ß-mercaptoethanol or dithiothreitol (DTT).

Glycerol is added to the loading buffer to increase the density of the sample to be loaded and hence
maintain the sample at the bottom of the well, restricting overflow and uneven gel loading.

To enable visualization of the migration of proteins it is common to include in the loading buffer a small
anionic dye molecule (e.g., bromophenol blue). Since the dye is anionic and small, it will migrate the fastest
of any component in the mixture to be separated and provide a migration front to monitor the separation
progress.

During protein sample treatment the sample should be mixed by vortexing before and after the heating step
for best resolution.




www.abcam.com/technical

b) Native and non-reduced samples

Alternatively, an antibody may recognize an epitope made up of non-contiguous amino acids. Although the amino
acids of the epitope are separated from one another in the primary sequence, they are close to each other in the
folded three-dimensional structure of the protein, and the antibody will only recognize the epitope as it exists on the
the surface of the folded structure.

It is imperative in these circumstances to run a Western Blot in non-denaturing conditions, and this will be noted
on the datasheet in the applications section. In general, a non-denaturing condition simply means leaving SDS out
of the sample and migration buffers and not heating the samples.

Certain antibodies only recognize protein in its non-reduced form i.e. in an oxidized form (particularly on
cysteine residues) and the reducing agents ß-mercaptoethanol and DTT must be left out of the loading buffer and
migration buffer (non reducing conditions).


Protein State             Gel condition                 Loading buffer                     Migration buffer
Reduced - Denatured       Reducing & Denaturing         With ß-mercaptoethanol or          With SDS
                                                        DTT and SDS
Reduced - Native          Reducing & Non-               With ß-mercaptoethanol or          No SDS
                          Denaturing                    DTT, no SDS
Oxidized - Denatured      Non-Reducing &                No ß-mercaptoethanol or DTT,       With SDS
                          Denaturing                    with SDS,
Oxidized - Native         Non-reducing & Native         No ß-mercaptoethanol or DTT,       No SDS
                                                        no SDS,



Rule of thumb: Reduce and denature unless the datasheet specifies otherwise.


B. Electrophoresis
Electrophoresis can be one dimensional (i.e., one plane of separation) or two dimensional. One dimensional
electrophoresis is used for most routine protein and nucleic acid separations. Two dimensional separation of
proteins is used for finger-printing, and when properly constructed can be extremely accurate in resolving all
of the proteins present within a cell.

Here we will be describing techniques for one dimensional electrophoresis. We recommend Gel Electrophoresis of
                                 rd
Proteins: A Practical Approach (3 Edition, B.D. Hames and D. Rickwood, The Practical Approach
Series, Oxford University Press, 1998) as a reference for basic understanding of 2D electrophoresis protocols.

1. Preparation of PAGE gels

When separated on a polyacrylamide gel, the procedure is abbreviated as SDS-PAGE (for Sodium Dodecyl
Sulfate PolyAcrylamide Gel Electrophoresis). The technique is a standard means for separating proteins according
to their molecular weight.

Polyacrylamide gels are formed from the polymerization of two compounds, acrylamide and N,N-methylenebis-
acrylamide (Bis, for short). Bis is a cross-linking agent for the gels. The polymerization is initiated by the
addition of ammonium persulfate along with either DMAP or TEMED. The gels are neutral, hydrophilic,
three-dimensional networks of long hydrocarbons crosslinked by methylene groups.

The separation of molecules within a gel is determined by the relative size of the pores formed within the

www.abcam.com/technical

gel. The pore size of a gel is determined by two factors: the total amount of acrylamide present (designated
as %T) and the amount of cross-linker (%C). As the total amount of acrylamide increases, the pore size
decreases. With cross- linking, 5%C gives the smallest pore size. Any increase or decrease in %C increases
the pore size. Gels are designated as percent solutions and will have two necessary parameters. The total
acrylamide is given as a percentage (w/v) of the acrylamide plus the bis-acrylamide. Thus, a 7.5%T would indicate
that there is a total of 7.5 g of acrylamide and bis per 100 ml of gel. A gel designated as 7.5%T:5%C would
have a total of 7.5% (w/v) acrylamide + bis, and the bis would be 5% of the total (with pure acrylamide
composing the remaining 2.5%).
                                                                             TM
Gels can be purchased ready-made (the Abcam laboratory uses Nu-Page gels from Invitrogen), or produced
in the laboratory (recipes can be found in laboratory handbooks). Either way, choose carefully the
percentage of your gel as this will determine the rate of migration and degree of separation between proteins.


Rule of thumb: The smaller the size of the protein of interest, the higher the percentage of
mono/bis. The bigger the size of the protein of interest, the lower the percentage of mono/bis.


Protein size (kDa)      Gel percentage (%)
4-40                    20
12-45                   15
10-70                   12.5
15-100                  10
25-200                  8


Acrylamide is a potent cumulative neurotoxin: wear gloves at all times.
Place gels in the electrophoresis tank as instructed by the manufacturer and bathe in migration buffer.

2. Positive controls

A positive control lysate is used to demonstrate that the protocol is efficient and correct and that the
antibody recognizes the target protein which may not be present in the experimental samples.

We strongly recommend the use of a positive control lysate when setting up a new
experiment; this will give you immediate confidence in the protocol.

3. Molecular weight markers

A range of molecular weight markers will enable the determination of the protein size (see below) and
also to monitor the progress of an electrophoretic run. A range of MW markers are commercially available.
Abcam has the following molecular weight markers:

        Catalogue ID ab41746 (MW 116, 97.4, 66, 45, 36 29, 24, 20.1, 14.2KDa)
        Catalogue ID ab48854 (MW 70, 57, 40, 28, 18, 13.5 and 8.5KDa)




www.abcam.com/technical

4. Loading samples and running the gel

Use special gel loading tips or a micro-syringe to load the complete sample in a narrow well. Take care not to poke
the well bottom with the tip as this will create a distorted band.
Never overfill wells. This could lead to poor data if samples spill into adjacent wells, and poorly resolved bands.
Load 20-40 µg total protein per mini-gel well.
The gels will be submerged in migration buffer which normally contains SDS, except in native gel electrophoresis.

A standard migration buffer (also called running buffer) for PAGE is 1X Tris-glycine:

25 mM Tris base
190 mM glycine
0.1% SDS
Check the pH; it should be around 8.3.

Run the gel for the recommended time as instructed by the manufacturer; this can vary from machine to
machine (1 hour to overnight depending on the voltage).
When the dye molecule (the “migration front”) reaches the bottom of the gel, the power is turned off. Proteins will
slowly elute from the gel at this point, so do not store the gel; proceed immediately to transfer.

5. Loading controls

Loading controls are required to check that the lanes in your gel have been evenly loaded with sample,
especially when a comparison must be made between the expression levels of a protein in different
samples. They are also useful to check for even transfer from the gel to the membrane across the whole gel.
Where even loading or transfer have not occurred, the loading control bands can be used to quantify the protein
amounts in each lane. For publication-quality work, use of a loading control is absolutely essential.


Loading control     Sample type                     Molecular       Caution
                                                    weight (kDa)
Beta Actin          Whole Cell / cytoplasmic        43              Not suitable for skeletal muscle samples.
                                                                    Changes in cell-growth conditions and
                                                                    interactions with extracellular matrix
                                                                    components may alter actin protein
                                                                    synthesis (Farmer et al, 1983).
GAPDH               Whole Cell / cytoplasmic        30-40           Some physiological factors, such as hypoxia
                                                                    and diabetes, increase GAPDH expression
                                                                    in certain cell types.
Tubulin             Whole Cell / cytoplasmic        55              Tubulin expression may vary according to
                                                                    resistance to antimicrobial and antimitotic
                                                                    drugs (Sangrajrang S. et al, 1998, Prasad V
                                                                    et al, 2000)
VDCA1/Porin         Mitochondrial                   31

COXIV               Mitochondrial                   16              Many proteins run at the same 16 kDa size
                                                                    as COXIV.
Lamin B1            Nuclear                         66              Not suitable for samples where the nuclear
                                                                    envelope is removed.
TATA binding        Nuclear                         38              Not suitable for samples where DNA is removed
protein TBP




www.abcam.com/technical

C. Transfer of proteins and staining (Western blotting)
1. Visualization of proteins in gels

This visualization of protein at this stage is useful to determine if proteins have migrated uniformly and evenly. Use
the copper stain if you plan to transfer the separated proteins to a membrane, as the Coomassie stain is not
reversible. Only use the Coomasie stain on gels post-transfer to check the efficiency of the transfer, or if you have
no plans to transfer and just want to observe the results of the SDS-PAGE separation.

a) Coomassie stain
As soon as the power is turned off the separated protein bands will begin to diffuse (they are freely soluble in
aqueous solution). To prevent diffusion of proteins treat the gel with a 40% distilled water, 10% acetic acid, and
50% methanol solution which causes almost all proteins to precipitate (become insoluble). To visualize the fixed
proteins place the gel in the same mixture of water/acetic acid/methanol but with the addition of 0.25% by weight
Coomassie Brilliant Blue R-250. Incubate 4 hours to overnight at room temperature on a shaker. Transfer the gel
(save the dye mixure; it can be re-used many times) to a mixture of 67.5% distilled water, 7.5% acetic acid, and
25% methanol, place on shaker, and replace with fresh rinse mixture until the excess dye has been removed. The
stain will not bind to the acrylamide, and will wash out (leaving a clear gel). However, it remains strongly bound to
the proteins in the gel, and these take on a deep blue color.

b) Copper Stain
Briefly rinse freshly-electrophoresed gels in distilled water (30 seconds maximum) and then transfer to 0.3 M CuCl2
for 5 to 15 minutes. Wash the gels briefly in de-ionized water, and view them against a dark-field background.
Proteins come up as clear zones in a translucent blue background.
Gels may be destained completely by repeated washing in 0.1- 0.25 M Tris/0.25 M EDTA pH 8.0. Move the gel to a
dish of transfer buffer before proceeding with transfer according to the transfer apparatus manufacturer’s
instructions.

2. Transfer

Detailed instructions for the transfer process can be found on the websites of the manufacturers of transfer
apparatus, and will vary depending on the system. The principle is the same in each case, though. Just as proteins
with an electrical charge (provided by the SDS bound to them) can be induced to travel through a gel in an
electrical field, so can the proteins be transferred in an electrical field from the gel onto a sturdy support, a
membrane that “blots” the proteins from the gel. (Early methods relied on diffusion; blotting in an electrical field is
now standard).

Transfer can be done in wet or semi-dry conditions. Semi-dry transfer is generally faster but wet transfer is a less
prone to failure due to drying of the membrane and is especially recommended for large proteins, >100 kD. For
both kinds of transfer, the membrane is placed next to the gel. The two are sandwiched between absorbent
materials, and the sandwich is clamped between solid supports to maintain tight contact between the gel and
membrane.

In wet transfer, the gel and membrane are sandwiched between sponge and paper
(sponge/paper/gel/membrane/paper/sponge) and all are clamped tightly together after ensuring no air bubbles
have formed between the gel and membrane. The sandwich is submerged in transfer buffer to which an electrical
field is applied. The negatively-charged proteins travel towards the positively-charged electrode, but the membrane
stops them, binds them, and prevents them from continuing on.

A standard buffer for wet transfer is the same as the 1X Tris-glycine buffer used for the migration/running buffer
without SDS but with the addition of methanol to a final concentration of 20%. For proteins larger than 80 kD, it is
recommended that SDS is included at a final concentration of 0.1%.

In semi-dry transfer, a sandwich of paper/gel/membrane/paper wetted in transfer buffer is placed directly between
positive and negative electrodes (cathode and anode respectively). As for wet transfer, it is important that the
www.abcam.com/technical

membrane is closest to the positive electrode and the gel closest to the negative electrode. The proportion of Tris
and glycine in the transfer buffer is not necessarily the same as for wet transfer; consult the apparatus
manufacturer’s protocol. A standard recipe is 48 mM Tris, 39 mM glycine, 0.04% SDS, 20% methanol.

Two types of membranes are available: nitrocellulose and PVDF (positively-charged nylon). The choice is personal
and both work very well. PVDF membranes require careful pre-treatment: cut the membrane to the appropriate size
then soak it in methanol for 1-2 min. Incubate in ice cold transfer buffer for 5 minutes. The gel needs to equilibrate
for 3-5 minutes in ice cold transfer buffer. Failure to do so will cause shrinking while transferring, and a distorted
pattern of transfer.

Note on transfer of large and small proteins

The balance of SDS and methanol in the transfer buffer, protein size, and gel percentage can affect transfer
efficiency. The following modifications will encourage efficient transfer.

Large proteins (>100 kD)

    1. For large proteins, transfer out of the gel may be very slow, just as they run slowly within the gel during
       separation. If blotting a large protein, be sure to run your samples in a low-concentration gel, 8% or less.
       These will be very fragile, so handle carefully.
    2. Large proteins will tend to precipitate in the gel, hindering transfer. Adding SDS to a final concentration of
       0.1% in the transfer buffer will discourage this. Methanol tends to remove SDS from proteins, so reducing
       the methanol percentage to 10% or less will also guard against precipitation.
    3. Lowering methanol in the transfer buffer also promotes swelling of the gel, allowing large proteins to
       transfer more easily.
    4. Methanol is only necessary if using nitrocellulose. If using PVDF, methanol can be removed from the
       transfer buffer altogether, and is only needed to activate the PVDF before assembling the gel/membrane
       sandwich.
                                             o
    5. Choose wet transfer overnight at 4 C instead of semi-dry transfer.

Small proteins (<100 kD)

    1. All proteins are hindered from binding to membranes by SDS but small proteins more so than large
       proteins. If your protein of interest is small, consider removing SDS from the transfer buffer.
    2. Keep the methanol concentration at 20%.

The following reference discusses a gel and buffer system that allows transfer of proteins as large as 500 kD:

Bolt and Mahoney, High-efficiency blotting of proteins of diverse sizes following sodium dodecyl sulfate–
polyacrylamide, gel electrophoresis. Analytical Biochemistry 247, 185–192 (1997).

More transfer tips:

Avoid touching the membrane with your fingers; use tweezers instead. Oils and proteins on
the fingers will block efficient transfer and create dirty blots.

After sandwiching the gel and membrane between paper, air bubbles between the gel and membrane
can be removed by rolling them out with a pipet or 15 ml tube, or by assembling the sandwich in a dish of transfer
buffer to prevent formation of bubbles in the first place. Wear gloves!.

Make sure the paper and membrane are cut to the same size as the gel. Large overhangs may prevent a current
from passing through the membrane in semi-dry transfers.

Chicken antibodies tend to bind PVDF and other nylon-based membranes, leading to high
background. Switching to a nitrocellulose membrane should help reduce background staining.
www.abcam.com/technical

3. Visualization of proteins in membranes: Ponceau Red

To check for success of transfer, wash the membrane in TBST (for a TBST recipe, see below). Dilute the stock
Ponceau Red 1:10. The stock is made of 2% Ponceau S in 30% trichloroacetic acid and 30% sulfosalicylic acid.
Incubate on an agitator for 5 min.
Wash extensively in water until the water is clear and the protein bands are well-defined.
The membrane may be destained completely by repeated washing in TBST or water. When using a PVDF
membrane, re-activate the membrane with methanol then wash again in TBST.

TBS 10x (concentrated TBS)
24.23 g Trizma HCl
80.06 g NaCl
Mix in 800 ml ultra pure water.
pH to 7.6 with pure HCl.
Top up to 1 L.

TBST
For 1 L: 100 ml of TBS 10x + 900 ml ultra pure water + 1ml Tween20

Tween20 is very viscous and will stick to the tip of your measuring pipettes. Be sure you add the right
amount of the detergent to the Tris buffer. A 10% solution is easier to dispense than undiluted Twen20.

4. Blocking the membrane

Blocking the membrane prevents non-specific background binding of the primary and/or secondary
antibodies to the membrane (which has a high capacity at binding proteins and therefore antibodies).

Two blocking solutions are traditionally used: non-fat milk or BSA (Cohn fraction V). Milk is cheaper but is not
recommended for studies of phospho-proteins (milk contains casein which is a phospho-protein; it causes high
background because the phospho-specific antibody detects the casein present in the milk).

Some antibodies give a stronger signal on membranes blocked with BSA as opposed to milk for unknown reasons.
Check the application notes on the datasheet in case there are specific instructions on how to block the membrane.

To prepare a 5% milk or BSA solution, weigh 5 g per 100 ml of Tris Buffer Saline Tween20 (TBST) buffer.
Mix well and filter. Failure to filter can lead to “spotting” where tiny dark grains will contaminate the blot
during development.

Incubate for 1 hour at 4°C under agitation. Rinse for 5 seconds in TBST after the incubation.

5. Incubation with the primary antibody

Incubation Buffer: Dilute the antibody in TBST at the suggested dilution, if the datasheet does not have a
recommended dilution try a range of dilutions (1:100-1:3000) and optimize the dilution according to the
results. Too much antibody will result in non-specific bands.

It is traditional in certain laboratories to incubate the antibody in blocking buffer, while other laboratories
incubate the antibody in TBST without a blocking agent. The results are variable from antibody to antibody
and you may find it makes a difference to either use no blocking agent in the antibody buffer or the same
agent as the blocking buffer.

If high background is not an issue, some antibodies produce a much stronger signal if diluted in
buffer with low concentrations (0.5 – 0.25%) of milk or BSA, or none at all.

www.abcam.com/technical

Incubation Time: The time can vary between a few hours and overnight (rarely more than 18 hours), and
is dependent on the binding affinity of the antibody for the protein and the abundance of protein. We
recommend a more dilute antibody and a prolonged incubation to ensure specific binding.

Incubation Temperature: preferably cold. If incubating in blocking buffer overnight, it is imperative to incubate at
4°C or contamination will incur and thus destruction of the protein (especially phospho groups).
Agitation of the antibody is recommended to enable adequate homogenous covering of the membrane and
prevent uneven binding.

6. Incubation with secondary antibody

Wash the membrane several times in TBST while agitating, 5 minutes or more per wash, to remove residual
primary antibody.

Incubation Buffer and Dilution: Dilute the antibody in TBST at the suggested dilution. If the datasheet does not
have a recommended dilution, try a range of dilutions (1:1000- 1:20,000) and optimize the dilution according to the
results. Too much antibody will result in non-specific bands. You may incubate the secondary antibody (and
primary antibody) in blocking buffer, but a reduction in background may come at the cost of a weaker specific
signal, presumably because the blocking protein hinders binding of the antibody to the target protein.

Incubation Time and Temperature: 1-2 hours, room temperature, with agitation.

Which conjugate? We recommend HRP-conjugated secondary antibodies. ALP-conjugated secondary
antibodies (alkaline phosphatase) are not recommended as they are not sensitive enough.

7. Development methods

Detection kits
For HRP-conjugated antibodies: ECL and ECL+ (home made or commercially available) are the traditional
kits used and we recommend ECL+. For the new generation detection machines such as Genegnome, use the
detection kit recommended by the manufacturer of the machine.

We do not recommend ECL or BCIP/NBT detection kits as they are not as sensitive.

X-ray films
Manual film development is traditionally used and enables the scientist to control the incubation time of
the x-ray film in the developing agent and fixation agent.
Automated x-ray film developers are also widely used and easy to use.

Remember that an over-exposed film is not suitable for analysis as determination of the
relative amount of protein is not possible. Overexposed films show totally black bands
with no contrast, and/or numerous non-specific bands.

Digital images:
The new generation of film developers are units with a camera inside an enclosure, removing the need for a
darkroom. The camera detects the chemiluminescence emanating from the membrane, transforming the signal into
a digital image for rapid analysis with software provided with the detection machine.

A range of machines are now commercially available. At the front of the next generation are systems which do not
use HRP-conjugated antibodies (i.e chemiluminescence): for example, STORM Analysers detect fluorescence from
fluorochrome-conjugated secondary antibodies. The Odyssey Infrared Imaging System detects infrared
fluorescence.


www.abcam.com/technical

D. References
Harlow, Ed, and David Lane. Using Antibodies. Cold Spring Harbor, New York: Cold Spring Harbor
Laboratory Press, 1999.
                                                                                       rd
B.D. Hames and D. Rickwood. Gel Electrophoresis of Proteins: A Practical Approach 3 Edition, The Practical
Approach Series, Oxford University Press, 1998.

Bolt and Mahoney, High-efficiency blotting of proteins of diverse sizes following sodium dodecyl sulfate–
polyacrylamide, gel electrophoresis. Analytical Biochemistry 247, 185–192 (1997).




www.abcam.com/technical

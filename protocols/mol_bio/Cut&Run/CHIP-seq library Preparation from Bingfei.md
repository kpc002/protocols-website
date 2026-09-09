---
title: "CHIP-seq library Preparation from Bingfei"
description: 'Procedure:'
order: 10
author: "Goldrath Lab"
date: last-modified
---

**Procedure:**

1.  **<span class="underline">End-Repair</span>**

<!-- end list -->

1.  Use End-it DNA End-repair Kit from Epicentre

>  uL
> 
> DNA+H2O 34
> 
> 10X End Repair Buffer 5
> 
> 2.5mM dNTPs Mix 5
> 
> 10mM ATP Mix 5
> 
> <span class="underline">END-IT enzyme mix 1</span>
> 
> total 50

2.  Incubate for 45 min at room temperature.

3.  Mini-elute purification (Zymo DNA Clean\&Concentrator). Elute it twice in 16ul of EB

4.  Total elute volume is 32uL.

**2**. **<span class="underline">Addition of an ‘A’ Base to the 3’ End of the DNA fragments</span>**

5.  Incubate for 30 min at 37C.

6.  Mini-elute purification (Zymo DNA Clean\&Concentrator).

7.  Elute it in 8ul of EB

**3**. **<span class="underline">Ligation of Adapters to the Ends of the DNA Fragments</span>**

**uL**

DNA 8

2X Ligation Buffer 10

Adaptor 1 ( Adaptor was diluted 1:10 in DDW before add it)

<span class="underline">Quick Ligase 1</span>

total 20

1.  Incubate for 20 min. at room temperature. Add 1 uL of NEB USER. Incubate at 37C for 15 minutes.

2.  Mini-elute purification (Zymo DNA Clean\&Concentrator). Elute **twice** in 10ul of EB (reuse). Total elute volume is 10uL.

Note: If you use NEB adaptor, remember to add 1uL USER Enzyme to incubate at 37C for 15 min after ligation.

**4. Size selection of library using Gel purification**

**Materials**

Nanosep MF Filter tube(VWR Cat.29300-642)

SYBR Gold (Invitrigen S11494)

**Method**

**Prepare the Gel**

• Prepare 8 % polyacrymide gel or buy:

40 % acryl (29:1) 6mL

5X TBE 3mL

ddH2O 21mL

10%APS 300uL(Fresh Made)

TEMED 40uL (Add it in fumehood)

Running buffer is 0.5X TBE . (600 ml/gel)

**Run the Gel**

• Add 6x Bromo phenol blue/xylene cyanol loading dye into the amplified library to make it 1X.

• Choose log ladder, load 10uL into the first line and the last line,.

• Load all samples into 8% polyacrymide gel every other line.

• Run at 200volt for 70 min, when the yellow dye reaches the bottom of the gel.

**Stain and Cut the gel**

• Gel Staining

Use a glass container for staining

Staining Buffer( Prepare in Glassware bottle)

(100ml 1X TAE, 10uL 10,000 x SYBR Gold )

Put gel into staining buffer and gently shake for 10min.

Cover the plate by foil to avoid the light.

• Excise bands from 2<span class="underline">00bps to 500bps</span> with a clean scalpel.

• Minced the gel piece by using a 0.5ml tube with holes in the bottom. (Put the 0.5mL tube into a 1.5mL or 2mL tube, and centrifuge at 14k for 3 min. Make holes with a needle.)

• Add 400uL EB Buffer to cover the gel pieces, Shake for O/N at 37<sup>o</sup>C.

**DNA Precipitation**

• Transfer the supernatant to Nanoseq column , spin 2 min @ 14k.

• Transfer the rest of things in the sample tube to the column, spin 2 min @ 14k.

• Add EB Buffer to bring to a total volume of 400ul.

• Add 45uL 3M NaOAC(ph 5.2) and vortex to mix.

• Add 2ul glycogen(20mg/ml) and 1.2mL cold 100% ETOH, vortex.

• Freeze at -80°C for 1h (or O/N), spin 13.8K for 30min in cold room or @4<sup>o</sup>C. Remove supernatant.

• Wash with 1mL 70% EtOH, vortex, spin for 15min @13.8k rpm, remove all traces of EtOH, air dry

5 minutes (pellet turns clear).

• Resuspend precipitated DNA in 10ul EB.

**5. PCR Amplification of Adaptor-ligated DNA**

Test run:

uL

Adaptor ligated CHIP DNA 1 + 0.5 of NFW

NEBNext High Fidelity 2X PCR Master Mix 7.5

Index Primer (dilute 1:10) 3

Universal PCR Primer (dilut<span class="underline">e 1:10 3</span>

total 15

PCR Cycling Conditions:

| Temp | Time   | Cycle     |
| ---- | ------ | --------- |
| 95   | 10 min | 1         |
| 95   | 30 sec | 30 cycles |
| 65   | 1 min  |           |
| 72   | 1 min  |           |

Calculate the number of cycles to use for amplification:

Cycle Number for start of plateau

Amplification:

uL

Adaptor ligated CHIP DNA 10

NEBNext High Fidelity 2X PCR Master Mix 25

Index Primer 1

Universal PCR Primer 1

<span class="underline">H2O 13</span>

total 50

PCR Cycling Conditions:

| Temp | Time   | Cycle                         |
| ---- | ------ | ----------------------------- |
| 98   | 30 sec | 1                             |
| 98   | 10 sec | \# of Cycles calculated Above |
| 65   | 30 sec |                               |
| 72   | 30 sec |                               |
| 72   | 5 min  | 1                             |
| 4    | Hold   |                               |

Zymo Elute with 10 uL

**6. Size select by Gel the same as “4”**

Finally dissolve in 10uL H2O and use Kappa qPCR kit to quantify

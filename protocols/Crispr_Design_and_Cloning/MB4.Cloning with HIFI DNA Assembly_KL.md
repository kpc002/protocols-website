---
title: Cloning with HIFI DNA Assembly_KL
description: Protocol for DNA cloning with high-fidelity assembly, including reaction
  setup and transformation.
order: 10
author: Giovanni Galleti
date: last-modified
image: oligo.svg
---

Cloning with HIFI DNA Assembly

  - The principle behind HIFI DNA Assembly is the joining of DNA fragments with ends that share the same sequence (15 – 40bp). There are several good animations on Youtube.

  - Prep your sequences of interest: plasmid prep or g-blocks (resuspended at 25 ng/µL)

  - If using two plasmids, design primers with overhangs using Snapgene. BE CAREFUL, primers used in the same reaction need to have the same Tm WITHOUT the overhangs. In other words, the difference of Tm between the primers (without the overhangs) has to be max 5C. Use the NEB Tm calculator to calculate the Tm and <span class="underline">not</span> Snapgene if you are using the Q5 NEB Master mix for the PCR.

  - Run the PCR based on the Q5 master mix protocol BUT

\-use 1min/kb for the elongation phase

\-run the PCR at the Tm of the primers WITHOUT the overhangs

  - Optional: Add 1ul of DPNI to destroy the substrate for the reaction (because it is methylated). **MIX well**, incubate at room temperature for 5 min and then at 37C for 60 minutes. (Of note: DPN1 will work in the Q5 PCR buffer or cutsmart buffer. It doesn’t work in water)

  - Run the product in a gel and isolate the band that corresponds to the right band size. Let the gel run AS LONG AS POSSIBLE to avoid contamination of your band with residual template DNA. Elute with water preferably (to avoid problems with the downstream reaction).

  - Combine the DNA for the HIFI DNA Assembly reaction. 1:1 vector to insert for a total reaction of 50ng. You don’t have to use 10ul of the Assembly as long as it is 1x (I usually use 5ul of DNA and 5ul of HIFI). Have a mock reaction as a control that you add water instead of HIFI DNA Assembly

  - Transform two sets of bacteria, one with 2ul of the reaction product and one with 2ul of the DNA from the mock reaction

  - Next day you should see colonies in the plate with the product and no colonies in the other plate (in reality the majority of the time we see some colonies on the control due to leftover template but the experimental usually has 10x more colonies).

  - Midi prep a few colonies. Design primers to sequence the new vectors. Send them for sequencing to Genewitz. ALWAYS do this because there are frequent mutations that occur

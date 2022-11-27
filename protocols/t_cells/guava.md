---
title: Guava Protocols
order: 20
author: Maximilian Heeg
date: last-modified
description: 
  "Count cells with the Guava"
image: guava.webp
---

## Preparing to run

1.  Before running, dilute the cells in RP5
2.  Obtain a 96 wells plate, label accordingly.
3.  Transfer 5µL of cells from step 1a into each well
4.  Add 20uL of PBS into the same wells, making a 1:5 dilution factor
    -   5µL cells:20vL PBS
5.  Make 2x Guava master mix by diluting Guava solution in PBS
    -   Calculate to make enough volume for 195µL total volume per sample
6.  Prepare epi vials, in the vials combine 5µL of cell mixture from step 4 to 195µL of the Guava master mix for each sample
    -   These vial samples will be used to run on Guava

## Running on Guava

1.  Turn on the machine and computer, let the machine warm up for 10 minutes before use
2.  On the computer, open the Guava software
3.  Open "ViaCount" and "create a new data set"
4.  Adjust settings:
    -   PM1: \~750
    -   PM2: \~800
    -   These setting are approximate and can be readjusted.
    -   PM1 should always be lower than PM2
5.  Adjust parameters:
    -   Dilution factor: 200
    -   Original volume:
        -   Spleen: 1mL
        -   Other cells: 0.2mL
    -   Events to acquire: 500-1000 events
6.  After finished setting up, load the sample and click "Acquire samples"
    -   Can stop acquire and "Next Sample" after 20s
7.  Record "Total Viable Cells in Original Sample" number

## Cleaning

1.  Determine which cleaning setting to use:
    -   For few sample (\<5 samples), use the quick clean option
    -   For larger sample size (\>5 samples), use the long clean option
2.  Quick clean:
    -   Fill an epi vial with ICF
    -   On the acquisition page, click "quick clean" option and follow prompt
        -   1 minute of ICF
    -   After the cleaning is done, put diH~2~O back on and turn off machine and computer
3.  Long Clean
    -   Prepare cleaning vials
        -   Vials are attached to the Guava machine on the bottom right.
        -   Fill the cleaning (blue) vial with ICF up to the line
        -   Discard liquids in the waste vial (liquid can go down the sink)
        -   Reattach the vials back to the machine
    -   Prepare 2 epi vials with new ICF and DiH2O, label and date.
        -   These should be replaced every time you do a long clean
        -   Can only use DiH2O
    -   Go to the Guava software interface
    -   Choose "cleaning" under "essential tool" in the main interface
    -   Click "start cleaning" when the portal is opened and follow prompt
        -   Load DiH2O and ICF accordingly
    -   When the cleaning is done, exit the portal, shutdown computer and machine.

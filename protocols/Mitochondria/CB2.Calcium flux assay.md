---
title: CB2.Calcium flux assay
description: Flow-cytometry protocol for measuring stimulus-induced intracellular
  calcium flux.
order: 10
author: Giovanni Galleti
date: last-modified
image: oligo.svg
---

Purpose: to quantify calcium flux upon T cell activation.

Note: Started from Ca++ flux protocol from “Liu et al. “T Cell Receptor–initiated Calcium Release Is Uncoupled from Capacitative Calcium Entry in Itk-deficient T Cells” *J. Exp. Med. 1998*, and modified from this starting protocol.

1.  Start from activated, transduced cells that spent at least 2 days in culture after transduction

2.  Collect cells from same condition/congenic marker together and count them – mix cells 1:1

3.  From here split cells in one tube for each stim condition you have below at step 11.

4.  Stain 1.0-1.2x10^6 total cells per stim/tube with 50 nM X-Rhod-1 AM (1:25,000; Molecular Probes) and 0.02% Pluronic F-127 (1:100; Invitrogen) in HBSS-/- for 30 minutes at 37ºC with gentle agitation (pipette every 10 minutes). Stain samples in 300 µL. Always make 1 tube extra when preparing the mix. ~~Optional: Keep unstained cells for later.~~

5.  Wash 1 time with *HBS*; resuspend cells at 1x10^6 /mL with R10 and incubate for 45 minutes at 37ºC.

6.  Incubate cells with ~~anti-CD3-biotin (final: 10 µg/ml; 1:50 dilution form stock)~~, anti-CD45.1-APC **or** anti-CD45.2-APC (1:200 dilution from stock) and Thy1.2-FITC (1:1,000 dilution from stock) in PBS for 20 mins at RT. Stain samples in 100 µL. Always consider 1 tube extra when preparing the mix.

7.  Wash 3 times with *HBS*; **resuspend at 1x10^6 /mL with R10 and keep at 37ºC until ready to use**

8.  When ready for acquisition spin cells down 1600 rpm for 5 minutes, resuspend as indicated in step 9 and transfer to FACS tubes. Each condition/tube you run wants 1.0-1.2x10^6 cells total.

9.  When running your experiment on the Fortessa, cells will be run in 300uL HBSS with **0.5mM Ca++** (for stim a) or 300uL **plain** HBSS (for stim b & c), so stim conditions will be made at 10x concentrations in 10% of the volume (30uL):
    
    1.  ~~Streptavidin (SA): final 40 µg/ml, make 10x (30 µL) **\[dilute stock 1:2.3, get 30µL from dilution\]**~~
    
    2.  Ionomycin: final concentration of 1 µg/mL, make 10x (30 µL) **\[dilute stock 1:100, get 30µL from dilution\]**
    
    3.  Ca++: final 0.5 mM, make 10x (30uL) **\[dilute stock 1:10, get 30µL from dilution\]**
    
    4.  TG: final 2 µM, make 10x (30 µL)
        
        1.  **For stim b** = dilute stock 1:100, get 30µL from dilution
        
        2.  **For stim c** = add 0.4 µL stock to 30 µL of stock Ryanodin
    
    5.  Xestospongin C: final 1 µM, make 10x (30 µL) **\[add 3.3 µL stock to 30 µL of stock TG+Ryanodin\]**
    
    6.  Ryanodin: final 100 µM, stock is already 10x – just add 30 µL from stock to sample when ready
    
    7.  EGTA: final 3 mM, stock is already 10x – just add 30 µL from stock to sample when ready

10. Wash cells, resuspend in 300uL HBSS with **0.5mM Ca++** (for stim a) or 300uL **plain** HBSS (for stim b), and set up Fortessa. ~~Make sure to have unstained control for calcium flux dyes.~~ X-rhod-1 AM **(in PE-CF594 channel) gets brighter when binds to calcium**, so set negative on unstained control.

11. Have stim conditions listed below; each sample gets run for minutes indicated below:
    
    1.  30sec baseline, +Ionomycin 5min
    
    2.  30sec baseline, +TG 3mins, +Ca++ 2mins, +EGTA 3min
    
    3.  30sec baseline, +TG/Ryanodin/Xestospongin 3mins, +Ca++ 2mins, +EGTA 3min

![](media/image1.png)![](media/image2.png)![](media/image3.png)![](media/image4.png)

**2X HEPES buffered saline solution (500 mL)**

274 mM NaCl 8 g

10 mM KCl 350 mg

1.4 mM Na2HPO4 100 mg

15 mM D-glucose 1.35 g

42 mM Hepes 21 mL (stock 1 M)

Check pH at 7.05

Filter with 0.22 µM

Aliquot 50 mL conical tubes

Freeze at -20 ºC (stable for 1 year)

---
title: "General Seahorse Protocol"
description: 'Goldrath Lab – XF96 – Seahorse protocol'
order: 10
author: "Anthony Phan"
date: last-modified
---

**Goldrath Lab – XF96 – Seahorse protocol**

**Materials needed:**

XF Calibrant (catalog \#100840-000 individually or in pack with sensor cartridge)

XF Cell Plate (catalog \#101085-004 individually or in pack with sensor cartridge)

XF Sensor Cartridge (FluxPak catalog \#102310-001 \[18 sensor plates\])

Buffer and glucose free media of Choice pH = 7.4 (we have Seahorse XF Assay Media catalog \#102352-000)

Glucose – Final Concentration 2g/L

L-glutamine – Final concentration 2mM

**Optional materials (depending on tests needed to be run on cells):**

XF Cell Mito Stress Test Kit (catalog \#101706-100)

Purpose is to evaluate mitochondrial function of cells (all these chemicals could be ordered separately from Sigma)

> Components:

  - Oligomycin – **PORT A (10 uM in port)**

<!-- end list -->

  - FCCP – **PORT B (10 uM in port)**

  - Antimycin A – **PORT C (10 uM in port)**

  - Rotenone – **PORT C (10 uM in port)**

XF Glycolysis Stress Test Kit (catalog \#102194-100)

Purpose is to evaluate glycolytic function of cells

Components:

  - Glucose – **PORT A (10 mM in port)**

  - Oligomycin - **PORT B (10 uM in port)**

  - 2-Deoxy-D-glucose **PORT C (1 M in port)**

**Procedure:**

1.  Turn on instrument and start the Seahorse software (at least 4 hours ahead of time) to allow it to prewarm to 37°C.

2.  XF Sensor Cartridge must be hydrated from 4-72 hrs prior to running the assay on the XF96 instrument. Cartridges cannot be hydrated for longer than 72 hours as this results in breakdown of the materials in the cartridge itself.
    
    1.  > Equilibrate the sensor cartridge by adding 200 μl of XF Calibrant pH 7.4 to each well of the utility plate that comes with the sensor cartridge.
    
    2.  > Incubate up to 72 hours at 37°C without CO<sub>2</sub> (if incubating for longer than 24 hours they recommend parafilming the plate to avoid evaporation)
    
    3.  > Prepare and add compounds to XF Sensor Cartridge injection ports (optional)

<!-- end list -->

  - Prepare all solutions as recommended by assay kit protocols and add to injection ports as needed.

> Allow compounds to incubate in a non-CO<sub>2</sub> 37°C incubator as well once added to the Sensor Cartridge.

3.  Prepare Cell Plate to be read
    
    1.  Prewarm your assay media (add glucose if necessary for assay DO NOT ADD if running Mitochondrial Stress Test) to 37°C.
    
    2.  Coat cell plate with BD Cell-Tak prior to plating of T cells
        
        1.  20 μl of Cell-Tak solution is necessary to coat the XF 96 well cell plates.
        
        2.  To coat a whole plate, make the Cell-Tak solution by combining:
            
            1.  2000 μl 0.1M pH 8.0 bicarbonate buffer (filter-sterilized if growing cells in plate)
            
            2.  12.58 μl 1N NaOH
            
            3.  25.15 μl Cell-Tak
        
        <!-- end list -->
        
        1.  Mix solution well and coat all wells within 10 minutes
        
        2.  Incubate for a minimum of 20 minutes at 37°C (longer is not a problem, even if everything evaporates)
        
        3.  Pour off/aspirate Cell-Tak solution and wash with 200 μl sterile water 2x to remove all bicarbonate (very important step may affect readings on Seahorse if residual bicarbonate is present)
        
        4.  Plates can be air dried and stored at 2-8°C for up to two weeks for later use.
    
    <!-- end list -->
    
    3.  Count T cells and prepare single cell suspension for even seeding. For the XF96 we have yet to test in vivo activated cells, but for in vitro activated T cells a density of 2x10^5 - 2.5x10^5 has been optimal for achieving good ECAR and OCR readings.
    
    4.  Add cells to wells of cell plate as needed in a volume of 50 μl and spin plate down at 200 RCF for 5 minutes to gently plate them into the Cell-Tak.
    
    5.  Bring volume of each well carefully up to necessary volume for measurements to be done.
        
        1.  225 μl if not adding compounds or performing stress tests.
        
        2.  150 μl if performing mitochondrial or glycolytic stress tests.
    
    6.  Place cell plate in 37°C non CO<sub>2</sub> incubator for at least 30 minutes to warm up and equlibrate (if plate has not been in a CO<sub>2</sub> incubator up to this point, it can be immediately read if it is warm).

<!-- end list -->

4.  Begin protocol on XF96 Instrument and begin calibration of the sensor plate.

<!-- end list -->

  - After \~25 minutes calibration will be complete and cell plate can be added for measurement of cells.

<!-- end list -->

5.  Depending on assay, measurements will take possibly \~2 hrs then software will produce a message asking you if the assay is complete and whether you’d like to eject the sensor and cell plate. Click yes and logout and exit the software. If no one else is using the Seahorse please turn off the heater within the instrument (Software will ask if you’d like to leave it on).

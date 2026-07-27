---
title: "Cas9 Electroporation with Lonza 2"
description: "Composite Lonza P3 Cas9 electroporation reference for primary CD8 T cells, with source-specific alternatives."
order: 21
author:
  - "Alex Monell"
  - "Kelsey Bennion"
  - "Giovanni Galleti"
  - "Nicole Sharping"
date: last-modified
---

This composite contains the Lonza P3 workflows from four sources. They differ in preparation of CD8 cells, experimental-guide and Cas9 input, controls, and post-electroporation culture. Use one complete source-specific option for each difference and confirm current lab-approved conditions before beginning.

## Source files

- **Alex Monell** — [Cas9 Nucleofection_ATM](../Alex_s_Protocols/Transfections_and_Transductions/Cas9%20Nucleofection_ATM.md)
- **Kelsey Bennion** — [Electroporation of activated CD8](../Kelsey_s_Protocols/Mouse/Electroporation%20of%20activated%20CD8.md)
- **Giovanni Galleti** — [CB6.CRISPRCas9 KO](../Giovanni_s_Protocols/cellular/CB6.CRISPRCas9%20KO.md)
- **Nicole Sharping** — [062923 CRISPRCas9 KO in primary T cells for in vivo transfer with Lonza - single guides](../Nicole_s_protocols/062923%20CRISPRCas9%20KO%20in%20primary%20T%20cells%20for%20in%20vivo%20transfer%20with%20Lonza%20-%20single%20guides.md)

## 1. Prepare CD8 T cells

### Enrichment or prior activation

**Derived from: Alex Monell, Giovanni Galleti, and Nicole Sharping.**

Enrich naïve CD8 T cells before electroporation, or activate cells 24 hours beforehand. These sources specify Lonza P3 buffer, DN100 for naïve CD8 cells, and DS137 for activated CD8 cells.

### Complete isolation and activation route

**Derived from: Kelsey Bennion.**

Kelsey provides a full route from spleen and lymph-node collection through ACK lysis, negative magnetic CD8 selection, purity assessment, and anti-CD3/anti-CD28 activation for 18–24 hours.

## 2. Assemble RNP complexes

**Derived from: Alex Monell, Kelsey Bennion, Giovanni Galleti, and Nicole Sharping.**

1. Use 100 µM crRNA and tracrRNA with a stated 3:1 guide-RNA-to-Cas9 molar ratio.
2. For a Thy1-only control, combine 3 µL Thy1 crRNA and 3 µL tracrRNA.
3. For experimental conditions, use the source-specific crRNA and Cas9 amounts shown in the differences table.
4. Anneal guide and tracrRNA at 95°C for 5 minutes, then hold at room temperature in the dark for 1 hour.
5. Add 40 µM Cas9, gently mix and briefly spin down, then incubate at room temperature for 20 minutes.

## 3. Prepare cells and P3 buffer

**Derived from: Alex Monell, Kelsey Bennion, Giovanni Galleti, and Nicole Sharping.**

1. Prepare P3 buffer at room temperature: 3.6 µL Supplement 1 plus 16.4 µL P3 per reaction.
2. Prewarm R10 with 50 U/mL IL-2 to 37°C.
3. Count 2–10 × 10<sup>6</sup> cells per reaction, wash in sterile room-temperature PBS, and pellet at 5000 RPM for 5 minutes at room temperature.
4. Remove residual liquid completely and resuspend each pellet in 20 µL P3 buffer. Limit the cells’ time in P3 buffer.

## 4. Electroporate cells

**Derived from: Alex Monell, Kelsey Bennion, Giovanni Galleti, and Nicole Sharping.**

1. Mix 5 µL RNP with 20 µL cells in P3 buffer.
2. Transfer the 25 µL mixture to the bottom of a Lonza nucleofector strip well without introducing bubbles.
3. Run DN100 for naïve CD8 cells or DS137 for activated CD8 cells.
4. Immediately add 130 µL prewarmed R10 and rest cells for 10 minutes at 37°C and 5% CO<sub>2</sub>.

## 5. Recover and analyze cells

### Direct recovery and in vivo transfer

**Derived from: Alex Monell and Nicole Sharping.**

Recover cells from the strip, wash with an additional 150 µL R10, and add 700 µL prewarmed R10 to reach 1 mL total. Count with Trypan Blue; both sources note 20–50% T-cell loss. For in vivo transfer, resuspend in PBS at the desired concentration and retain cells for flow or Sanger validation.

### Overnight recovery

**Derived from: Giovanni Galleti.**

Prepare R10 plus 15 U/mL IL-2 by combining 600 µL R10 plus 50 U/mL IL-2 with 1400 µL plain R10. Return cells to their original number of wells and culture overnight or for 24 hours.

### Extended culture and validation

**Derived from: Kelsey Bennion.**

Kelsey describes cytokine replenishment every 48 hours, 25 U/mL IL-2 or TRM-polarization medium, and downstream collection for flow, genomic-DNA/Sanger, RNA/qPCR, and supernatant ELISA analyses.

## Differences between source protocols

| Difference | Alex Monell | Kelsey Bennion | Giovanni Galleti | Nicole Sharping |
|---|---|---|---|---|
| Starting-cell preparation | Naïve CD8 enrichment or activation 24 hours earlier. [Source: Alex Monell](../Alex_s_Protocols/Transfections_and_Transductions/Cas9%20Nucleofection_ATM.md) | Full spleen/lymph-node harvest, ACK lysis, negative selection, purity check, and activation workflow. [Source: Kelsey Bennion](../Kelsey_s_Protocols/Mouse/Electroporation%20of%20activated%20CD8.md) | Naïve CD8 enrichment or activation 24 hours earlier. [Source: Giovanni Galleti](../Giovanni_s_Protocols/cellular/CB6.CRISPRCas9%20KO.md) | Naïve CD8 enrichment or activation 24 hours earlier. [Source: Nicole Sharping](../Nicole_s_protocols/062923%20CRISPRCas9%20KO%20in%20primary%20T%20cells%20for%20in%20vivo%20transfer%20with%20Lonza%20-%20single%20guides.md) |
| Experimental crRNA input | 3 µL experimental crRNA, 1.5 µL Thy1 crRNA, and 3 µL tracrRNA. [Source: Alex Monell](../Alex_s_Protocols/Transfections_and_Transductions/Cas9%20Nucleofection_ATM.md) | 1.5 µL experimental crRNA, 1.5 µL Thy1 crRNA, and 3 µL tracrRNA. [Source: Kelsey Bennion](../Kelsey_s_Protocols/Mouse/Electroporation%20of%20activated%20CD8.md) | 1.5 µL experimental crRNA, 1.5 µL Thy1 crRNA, and 3 µL tracrRNA. [Source: Giovanni Galleti](../Giovanni_s_Protocols/cellular/CB6.CRISPRCas9%20KO.md) | 1.5 µL experimental crRNA, 1.5 µL Thy1 crRNA, and 3 µL tracrRNA. [Source: Nicole Sharping](../Nicole_s_protocols/062923%20CRISPRCas9%20KO%20in%20primary%20T%20cells%20for%20in%20vivo%20transfer%20with%20Lonza%20-%20single%20guides.md) |
| 40 µM Cas9 input | 2.38 µL per reaction. [Source: Alex Monell](../Alex_s_Protocols/Transfections_and_Transductions/Cas9%20Nucleofection_ATM.md) | 1.9 µL per reaction. [Source: Kelsey Bennion](../Kelsey_s_Protocols/Mouse/Electroporation%20of%20activated%20CD8.md) | 1.9 µL per reaction. [Source: Giovanni Galleti](../Giovanni_s_Protocols/cellular/CB6.CRISPRCas9%20KO.md) | 1.9 µL per reaction. [Source: Nicole Sharping](../Nicole_s_protocols/062923%20CRISPRCas9%20KO%20in%20primary%20T%20cells%20for%20in%20vivo%20transfer%20with%20Lonza%20-%20single%20guides.md) |
| Additional controls or handling | No no-guide control or strip-orientation note is stated. [Source: Alex Monell](../Alex_s_Protocols/Transfections_and_Transductions/Cas9%20Nucleofection_ATM.md) | Adds a no-guide shock control and strip-orientation note. [Source: Kelsey Bennion](../Kelsey_s_Protocols/Mouse/Electroporation%20of%20activated%20CD8.md) | Directs users to select wells, pulse code, and P3 primary solution before use. [Source: Giovanni Galleti](../Giovanni_s_Protocols/cellular/CB6.CRISPRCas9%20KO.md) | No no-guide control or strip-orientation note is stated. [Source: Nicole Sharping](../Nicole_s_protocols/062923%20CRISPRCas9%20KO%20in%20primary%20T%20cells%20for%20in%20vivo%20transfer%20with%20Lonza%20-%20single%20guides.md) |
| Recovery and validation | Recovers to 1 mL R10 and supports in vivo transfer with flow/Sanger validation. [Source: Alex Monell](../Alex_s_Protocols/Transfections_and_Transductions/Cas9%20Nucleofection_ATM.md) | Extended cytokine culture and flow, genomic-DNA/Sanger, RNA/qPCR, and ELISA options. [Source: Kelsey Bennion](../Kelsey_s_Protocols/Mouse/Electroporation%20of%20activated%20CD8.md) | Overnight recovery in 15 U/mL IL-2. [Source: Giovanni Galleti](../Giovanni_s_Protocols/cellular/CB6.CRISPRCas9%20KO.md) | Matches the 1 mL R10 recovery and in vivo-transfer option. [Source: Nicole Sharping](../Nicole_s_protocols/062923%20CRISPRCas9%20KO%20in%20primary%20T%20cells%20for%20in%20vivo%20transfer%20with%20Lonza%20-%20single%20guides.md) |

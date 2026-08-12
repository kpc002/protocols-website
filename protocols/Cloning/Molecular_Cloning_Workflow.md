---
title: "Molecular_Cloning_Workflow"
description: "Workflow for restriction cloning, DNA ligation or HiFi assembly, and chemical transformation into competent E. coli."
order: 10
author: "Dhruv Khanduja"
date: last-modified
image: blood_sample.svg
---

**RESTRICTION CLONING AND TRANSFORMATION**

Chemically competent DH5α / NEB 5-alpha E. coli

# 1\. Purpose

This procedure describes routine restriction cloning, DNA assembly, and chemical transformation into DH5α, NEB 5-alpha, or equivalent cloning strains. It includes two assembly options: T4 DNA ligation and NEBuilder HiFi DNA Assembly.

Use current product instructions when a reagent or competent-cell lot specifies conditions that differ from this SOP.

# 2\. Materials

• Plasmid DNA, insert DNA, or purified PCR/Gel product

• Restriction enzyme(s) and compatible reaction buffer (NEB 3.1, CutSmart)

• Agarose gel electrophoresis supplies and gel extraction kit

• NEB Quick CIP for single-enzyme ligation cloning, when required

• T4 DNA Ligase and T4 DNA Ligase Reaction Buffer, or NEBuilder HiFi DNA Assembly Master Mix

• Chemically competent DH5α or NEB 5-alpha cells, SOC medium, and selective LB agar plates

• 42°C water bath or heat block, ice bucket, 37°C shaking incubator, and microcentrifuge

# 3\. Restriction enzyme calculation

Use 10 units of each restriction enzyme per microgram of DNA as the standard starting condition. Enzyme-specific instructions take precedence.

| **Calculation**                                                | **Result**               |
| -------------------------------------------------------------- | ------------------------ |
| 20,000 U/mL ÷ 1,000 µL/mL (This varies per restriction enzyme) | 20 U/µL                  |
| 10 U required ÷ 20 U/µL                                        | 0.5 µL enzyme per µg DNA |

Example: digesting 1 µg DNA with a 20 U/µL restriction enzyme requires 0.5 µL enzyme. In a double digest, add 0.5 µL of each enzyme per 1 µg DNA.

Do not apply the 10 U/µg calculation to T4 DNA Ligase or Quick CIP. Use the product-specific amounts listed below.

# 4\. Restriction digestion

## 4.1 Standard 50 µL reaction

| **Component**                  | **Single digest** | **Double digest** |
| ------------------------------ | ----------------- | ----------------- |
| DNA                            | 3 µg              | 3 µg              |
| 10X compatible buffer          | 5.0 µL            | 5.0 µL            |
| Restriction enzyme 1 (20 U/µL) | 1.5 µL            | 1.5 µL            |
| Restriction enzyme 2 (20 U/µL) | —                 | 1.5 µL            |
| Nuclease-free water            | to 50 µL          | to 50 µL          |

## 4.2 Procedure

1\. Confirm the restriction sites, expected fragment sizes, recommended buffer, incubation temperature, methylation sensitivity, and heat-inactivation conditions.

2\. Assemble the reaction on ice. Add water and buffer first, followed by DNA. Add the restriction enzyme(s) last and mix gently.

3\. Incubate at the recommended temperature. Use 1 hour as the routine standard. A 30-minute digest may be sufficient for some enzymes (HF); difficult digests may be extended to 2–4 hours. **Dhruv typically digests for 4 hours for a complete digest. This may not always be the best option since some enzymes exhibit star activity.**

4\. Run the digest on an agarose gel with EtBr (4ul for small gel in 100ul). Separate the desired linearized vector or insert from uncut plasmid and unwanted fragments. Typically 1-1.5% agarose gels work well for large fragments.

5\. Excise the correct band using UV visualization when available. Purify the DNA with a gel extraction kit and elute in a low volume (20ul)

6\. Measure DNA concentration before ligation or HiFi assembly.

# 5\. Assembly option A: T4 DNA ligation

  - https://www.neb.com/en-us/protocols/dna-ligation-with-t4-dna-ligase-m0202?srsltid=ARcRdnoMQELdoYJfOkqm4crYGDwMzlnDLQaQJH9JuT-hNghYJZv3wOmf

  - https://protocols.heeg.io/molecular-biology/lsga\_cloning/\#interactive-primer-designer

# 6\. Assembly option B: NEBuilder HiFi DNA Assembly

## 5.1 Vector dephosphorylation

Dephosphorylate a vector cut with a single restriction enzyme when the vector ends can re-ligate. This reduces vector-only background. Dephosphorylation is generally unnecessary when two different enzymes produce non-compatible ends.

| **Component**        | **Amount**                                                 |
| -------------------- | ---------------------------------------------------------- |
| Linearized vector    | *1 pmol of DNA ends which* is about 1 μg of a 3 kb plasmid |
| 10X rCutSmart Buffer | 2.0 µL                                                     |
| NEB Quick CIP        | 1.0 µL                                                     |
| Nuclease-free water  | to 20 µL                                                   |

## 6.1 Primer design

• Use a 20–25 bp template-binding sequence at the 3′ end of each primer.

• Add a 20–30 bp overlap at the 5′ end so adjacent fragments share the intended junction (Snapgene has a tool to generate these fragments)

• For this workflow, keep each primer at or below 60 nucleotides total. A typical primer is 40–55 nucleotides long.

## 6.2 Standard 20 µL assembly

<table>
<thead>
<tr class="header">
<th><strong>Component</strong></th>
<th><strong>Amount</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NEBuilder HiFi DNA Assembly Master Mix (2X)</td>
<td>10.0 µL</td>
</tr>
<tr class="even">
<td>Linearized vector</td>
<td>50-100ng</td>
</tr>
<tr class="odd">
<td>Insert fragment(s)</td>
<td><p>Ratio of 2:1 (Insert to vector) for single insert (See Link Below)</p>
<p>https://nebiocalculator.neb.com/#!/ligation</p></td>
</tr>
<tr class="even">
<td>Nuclease-free water</td>
<td>to 20 µL</td>
</tr>
</tbody>
</table>

1\. Combine the DNA fragments on ice. Add the 2X master mix, mix gently, and briefly centrifuge.

2\. Incubate at 50°C for 15 minutes for a 2–3 fragment assembly. Use 60 minutes for assemblies containing 4–6 fragments or for difficult junctions. **Dhruv always uses 60 min at 50C**

3\. Place the reaction on ice and transform 2 µL into 50 µL competent cells.

4\. Include a vector-only control when residual circular template or incomplete vector linearization is a concern.

5\. Follow protocol below

# 7\. Chemical transformation

Keep competent cells on ice at all times except during heat shock. Do not vortex the cells.

| **Step** | **Procedure**                                                                                                                                |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | Thaw one 50 µL aliquot of competent cells on wet ice.                                                                                        |
| 2        | Add 2 µL ligation or HiFi assembly reaction. For purified plasmid controls, use approximately 1 pg–10 ng DNA.                                |
| 3        | Mix by gently tapping the tube. Incubate on ice for 30 minutes.                                                                              |
| 4        | Heat shock at 42°C: 30 seconds unless the product instructions specify otherwise.                                                            |
| 5        | Return the tube immediately to ice for 2 minutes.                                                                                            |
| 6        | Add 500 µL SOC medium and recover for 60 minutes at 37°C with shaking at 300-500 rpm on heatblock.                                           |
| 7        | Spin down tube at 5000rpm for 5min. Pipette out 420ul and resuspend the pellet in the 80ul of SOC that remains. Pipette on plate and spread. |
| 8        | Incubate plates inverted at 37°C for 16–18 hours (O/N). Use 30°C when the plasmid is unstable or contains repetitive elements.               |

# 8\. Colony screening

1\. Record colony counts for the experimental plate, vector-only control, and positive transformation control.

2\. Pick 4–12 well-isolated colonies. Increase the number screened when vector-only background is high.

3\. Grow colonies in 5ml of LB with the appropriate antibiotic O/N

4\. Miniprep 2ml of the culture, and screen by either sequencing (Plasmidsaurus, Eton), or by restriction digest (use enzymes unique to insert). Keep the rest of the culture at 4C

5\. If sequencing results are correct, grow up 1ml of the remaining culture in 100ml of LB with antibiotic O/N and isolate plasmid using the midiprep kit.

# 10\. Useful Links

1.  NEBioCalculator to calculate ligation ratios: <https://nebiocalculator.neb.com/#!/ligation>:

2.  Snapgene: To plan clonings. Alternatively Benchling

3.  Restriction Digest Protocol: <https://www.neb.com/en-us/protocols/restriction-digest-protocol?srsltid=AfmBOooPAlRx5vilehh1qsc15030tbjgX0hdRTGDg9MVrENHuTGrJnDa>:

---
title: "guide design and sequence"
description: 'DESIGN primers for gRNA to insert into'
order: 10
author: "Goldrath Lab"
date: last-modified
---

**DESIGN primers for gRNA to insert into**

**LMPd-Ametrine RV vector = NEW LsgA**

1.  **sgRNA design**

> selected your CRISPR target sequence, order from IDT the oligos
> 
> Do not include PAM seq in the NT primers\!

<span class="underline">Design FWR and REV oligos</span>

BbsI

5’ –**CACC**<span class="underline">G</span>NNNNNNNNNNNNNNNNNNN – 3’

3’ –<span class="underline">C</span>NNNNNNNNNNNNNNNNNNN**CAAA** –5’

Forward oligo: 5’ target seq 3’

Reverse oligo: 5’ rev compl 3’

![](media/image1.tiff)

1.  **sgRNA oligos annealing**

> Resuspend oligos in ddH20 100 uM
> 
> Mix equimolar 1:1
> 
> Annealing oligos

<table>
<thead>
<tr class="header">
<th>H20</th>
<th><blockquote>
<p>8 uL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Oligo1</td>
<td>5 uL</td>
</tr>
<tr class="even">
<td>Oligo 2</td>
<td><blockquote>
<p>5 uL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>T4 DNA ligase buffer 10X</td>
<td><blockquote>
<p>2 uL</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>20 uL Vf</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  **LMPd vector – new LsgA:**

8 Colonies with <span class="underline">LMPd-pUC57</span> in 50% Glycerol stock at -30C.

Diluite 1:1000 (1 ul in 1 ml of LB) .

Plate 50 uL of diluited bacteria in LB+Amp plate (pre-RT 1h) and spread them on it.

Leave 37C, ON incubator for bacteria

<span class="underline">Day after:</span>

Pick up a colony in 5 ml of LB+Amp ( 50 ug/ml, 1/1000) ( into 15 ml Tube)

Shaker 37C, 6-7h \_\_\_STARTING COLONY

Transfer 2-3 ml into 200 mL LB + Amp Flask

Shaker 37C ON 260 rpm

<span class="underline">Day after:</span>

Do maxiprep kit Qiagen

Quantify nanodrop LMPd-pC57 dsDNA

3.  **<span class="underline">Digetion of LMPd</span>**

> <span class="underline">ON water bath at 37C in sterile epp 500ul</span>

| **<span class="underline">Vector</span>** |                  |
| ----------------------------------------- | ---------------- |
| LMPd                                      | 5 ug             |
| BbsI                                      | 0.5              |
|                                           |                  |
| 10X Buffer NEB                            | 2                |
| ddH20                                     | Up to 20 (or 40) |

4.  **<span class="underline">Ligation of Vector LMPd + insert gRNA</span>**

| 10X Ligation Buffer | 2 ul        |
| ------------------- | ----------- |
| T4 DNA ligase       | 1 ul        |
| Vector              | 0.5-1 ul    |
| gRNA (annealed)     | 5 ul        |
| ddH20               | Up to 20 ul |

> <span class="underline">RT 2h</span>

5.  **<span class="underline">Transformation into E.Coli competent cells</span>**

> Thaw TOP10c on ice, 10 min
> 
> Add 5 ul of reaction from ligation
> 
> Mix gently, leave 15 min on ice
> 
> Heat shock 30sec 42C
> 
> Add 250 uL of LB medium . 1h 37C shaker
> 
> Plate 125 uL into 1 LB+Amp plate ( 2 plates)
> 
> ON incubater , 37C
> 
> Check colonies

Sequences

![](media/image2.emf)

| <span class="underline">ICOS mouse target 1</span> | <span class="underline">exon 3, +</span> | CTG AAG CTC TGG CTA CCC GT AGG                                                                               |
| -------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Target seq                                         |                                          | **CTG AAG CTC TGG CTA CCC GT**                                                                               |
| Reverse                                            |                                          | TGC CCA TCG GTC TCG AAG TC                                                                                   |
| Complement with reverse                            |                                          | ACG GGT AGC CAG AGC TTC AG                                                                                   |
| F1                                                 |                                          | 5’ – **CACC**<span class="underline">G</span> **CTG AAG CTC TGG CTA CCC GT** –3’                             |
| R1                                                 |                                          | 5’ – <span class="underline">AAAC</span> ACG GGT AGC CAG AGC TTC AG **<span class="underline">C</span>** –3’ |

| <span class="underline">OX40 mouse target 1</span> | <span class="underline">exon 1, +</span> | CAC TTG GAG TTA CAG CAA GG CGG                                                                               |
| -------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Target seq                                         |                                          | CAC TTG GAG TTA CAG CAA GG                                                                                   |
| Reverse                                            |                                          | GGAACGACATTGAGGTTCAC                                                                                         |
| Complement with reverse                            |                                          | CCT TGC TGT AAC TCC AAG TG                                                                                   |
| F1                                                 |                                          | 5’ – **CACC**<span class="underline">G</span> CAC TTG GAG TTA CAG CAA GG –3’                                 |
| R1                                                 |                                          | 5’ – <span class="underline">AAAC</span> CCT TGC TGT AAC TCC AAG TG **<span class="underline">C</span>** –3’ |

![](media/image3.emf)

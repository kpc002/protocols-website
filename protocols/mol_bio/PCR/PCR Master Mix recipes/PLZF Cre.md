---
title: "PLZF Cre"
description: "Interactive PCR master mix calculator from the PLZF Cre sheet."
author: "Goldrath Lab"
date: last-modified
---

# PLZF Cre

Enter the **number of reactions needed** in the highlighted box. Calculated amounts update automatically using the original workbook formulas. For pages with multiple mixes, set the reaction count for each mix separately.

Column B contains the amount for one reaction; column C contains the amount for the selected number of reactions. Counts include only the reactions you enter; no extra reactions are added.

[Download the original workbook](../../../Goldrath_Protocols/The%20Master%20Folder/PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

```{=html}
<div class="pcr-calculator">
<div class="pcr-controls">
<div class="pcr-control">
<label for="pcr-reactions-c2">PLZF Cre — Number of reactions needed</label>
<input id="pcr-reactions-c2" class="pcr-reaction-input" data-reaction-cell="C2" type="number" min="0" step="1" value="20" required aria-describedby="pcr-reactions-c2-help pcr-reactions-c2-error">
<small id="pcr-reactions-c2-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c2-error" class="pcr-input-error" aria-live="polite"></span>
</div>
</div>
<noscript>Enable JavaScript to recalculate amounts. The table currently shows amounts for the original workbook reaction counts.</noscript>
<div class="pcr-table-wrap" tabindex="0" role="region" aria-label="PCR recipe worksheet">
<table class="pcr-table table">
<caption>Workbook recipe: B = amount per reaction; C = calculated amount for your reaction count.</caption>
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A · Reagent / mix</th>
<th scope="col">B · Per reaction</th>
<th scope="col">C · Calculated amount</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">PLZF</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="H1">Folder</td>
<td data-cell="I1">PCR name</td>
<td data-cell="J1">PCR cycle</td>
<td data-cell="K1">Primer Squence</td>
<td data-cell="L1">Band Size</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2">20</td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">PlzF Cre</td>
<td data-cell="J2">1. Incubate at 94°C for 3:00</td>
<td data-cell="K2">PLZF cre F- CGA TGC AAC GAG TGA TGA</td>
<td data-cell="L2">~600bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="Workbook formula: =B3*C2">100</td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">PLZF cre R- ATC GCT CGA CCA GTT TAG T</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="Workbook formula: =B4*C2">50</td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 51°C for 0:30</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="Workbook formula: =B5*C2">10</td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 0:30</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="Workbook formula: =B6*C2">25</td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 35 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="Workbook formula: =B7*C2">25</td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 5:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.2</td>
<td data-cell="C8" data-formula="=B8*C2" title="Workbook formula: =B8*C2">4</td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">13.25</td>
<td data-cell="C9" data-formula="=B9*C2" title="Workbook formula: =B9*C2">265</td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
<td data-cell="L9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">DNA</td>
<td data-cell="B10">1</td>
<td data-cell="C10" data-formula="=B10*C2" title="Workbook formula: =B10*C2">20</td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11">25</td>
<td data-cell="C11" data-formula="=B11*C2" title="Workbook formula: =B11*C2">500</td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
</tbody>
</table>
</div>
</div>
```

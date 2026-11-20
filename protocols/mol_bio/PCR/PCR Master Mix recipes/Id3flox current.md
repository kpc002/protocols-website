---
title: "Id3flox current"
description: "Interactive PCR master mix calculator from the Id3flox current sheet."
author: "Goldrath Lab"
date: last-modified
---

# Id3flox current

Enter the **number of reactions needed** in the highlighted box. Calculated amounts update automatically using the original workbook formulas. For pages with multiple mixes, set the reaction count for each mix separately.

Column B contains the amount for one reaction; column C contains the amount for the selected number of reactions. Counts include only the reactions you enter; no extra reactions are added.

[Download the original workbook](../../../Goldrath_Protocols/The%20Master%20Folder/PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

```{=html}
<div class="pcr-calculator">
<div class="pcr-controls">
<div class="pcr-control">
<label for="pcr-reactions-c2">Id3flox current — Number of reactions needed</label>
<input id="pcr-reactions-c2" class="pcr-reaction-input" data-reaction-cell="C2" type="number" min="0" step="1" value="18" required aria-describedby="pcr-reactions-c2-help pcr-reactions-c2-error">
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
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Id3flox</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1">Folder</td>
<td data-cell="H1">PCR name</td>
<td data-cell="I1">PCR cycle</td>
<td data-cell="J1">Primer Squence</td>
<td data-cell="K1">Band Size</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2">18</td>
<td data-cell="G2">Kyla</td>
<td data-cell="H2">ID3flox</td>
<td data-cell="I2">1. Incubate at 94°C for 4:00</td>
<td data-cell="J2">ID3flox F- GCTCTGAGGTCATAAATCCC</td>
<td data-cell="K2">WT~500bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="Workbook formula: =B3*C2">90</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3">2. Incubate at 94°C for 0:30</td>
<td data-cell="J3">ID3flox R- CCATTTGGTTCTATGTATGCCCGTG</td>
<td data-cell="K3">Flox~600bp</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="Workbook formula: =B4*C2">45</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4">3. Incubate at 55°C for 0:30</td>
<td data-cell="J4"></td>
<td data-cell="K4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="Workbook formula: =B5*C2">9</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5">4. Incubate at 72°C for 0:45</td>
<td data-cell="J5"></td>
<td data-cell="K5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="Workbook formula: =B6*C2">22.5</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6">5. Cycle to step 2, 35 times</td>
<td data-cell="J6"></td>
<td data-cell="K6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="Workbook formula: =B7*C2">22.5</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7">6. Incubate at 72°C for 3:00</td>
<td data-cell="J7"></td>
<td data-cell="K7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.2</td>
<td data-cell="C8" data-formula="=B8*C2" title="Workbook formula: =B8*C2">3.6</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">13.3</td>
<td data-cell="C9" data-formula="=B9*C2" title="Workbook formula: =B9*C2">239.4</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">DNA</td>
<td data-cell="B10">1</td>
<td data-cell="C10" data-formula="=B10*C2" title="Workbook formula: =B10*C2">18</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11" data-formula="=SUM(B3:B10)" title="Workbook formula: =SUM(B3:B10)">25</td>
<td data-cell="C11" data-formula="=SUM(C3:C10)" title="Workbook formula: =SUM(C3:C10)">450</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12"></td>
<td data-cell="B12"></td>
<td data-cell="C12"></td>
<td data-cell="G12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
<td data-cell="K12"></td>
</tr>
<tr>
<th scope="row">13</th>
<td data-cell="A13"></td>
<td data-cell="B13"></td>
<td data-cell="C13"></td>
<td data-cell="G13"></td>
<td data-cell="H13"></td>
<td data-cell="I13"></td>
<td data-cell="J13"></td>
<td data-cell="K13"></td>
</tr>
<tr>
<th scope="row">14</th>
<td data-cell="A14"></td>
<td data-cell="B14"></td>
<td data-cell="C14"></td>
<td data-cell="G14"></td>
<td data-cell="H14"></td>
<td data-cell="I14"></td>
<td data-cell="J14"></td>
<td data-cell="K14"></td>
</tr>
<tr>
<th scope="row">15</th>
<td data-cell="A15"></td>
<td data-cell="B15"></td>
<td data-cell="C15"></td>
<td data-cell="G15"></td>
<td data-cell="H15"></td>
<td data-cell="I15"></td>
<td data-cell="J15"></td>
<td data-cell="K15"></td>
</tr>
<tr>
<th scope="row">16</th>
<td data-cell="A16"></td>
<td data-cell="B16"></td>
<td data-cell="C16"></td>
<td data-cell="G16"></td>
<td data-cell="H16"></td>
<td data-cell="I16"></td>
<td data-cell="J16"></td>
<td data-cell="K16"></td>
</tr>
<tr>
<th scope="row">17</th>
<td data-cell="A17"></td>
<td data-cell="B17"></td>
<td data-cell="C17"></td>
<td data-cell="G17"></td>
<td data-cell="H17"></td>
<td data-cell="I17"></td>
<td data-cell="J17"></td>
<td data-cell="K17"></td>
</tr>
</tbody>
</table>
</div>
</div>
```

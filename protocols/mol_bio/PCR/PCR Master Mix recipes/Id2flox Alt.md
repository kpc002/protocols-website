---
title: "Id2flox Alt"
description: "Interactive PCR master mix calculator from the Id2flox Alt sheet."
author: "Goldrath Lab"
date: last-modified
---

# Id2flox Alt

Enter the **number of reactions needed** in the highlighted box. Calculated amounts update automatically using the original workbook formulas. For pages with multiple mixes, set the reaction count for each mix separately.

Column B contains the amount for one reaction; column C contains the amount for the selected number of reactions. Counts include only the reactions you enter; no extra reactions are added.

[Download the original workbook](../../../Goldrath_Protocols/The%20Master%20Folder/PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

```{=html}
<div class="pcr-calculator">
<div class="pcr-controls">
<div class="pcr-control">
<label for="pcr-reactions-c2">Id2flox Alt — Number of reactions needed</label>
<input id="pcr-reactions-c2" class="pcr-reaction-input" data-reaction-cell="C2" type="number" min="0" step="1" value="35" required aria-describedby="pcr-reactions-c2-help pcr-reactions-c2-error">
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
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Id2 f/f</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2">35</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="Workbook formula: =B3*C2">175</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2</td>
<td data-cell="C4" data-formula="=B4*C2" title="Workbook formula: =B4*C2">70</td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="Workbook formula: =B5*C2">17.5</td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">DMSO</td>
<td data-cell="B6">2</td>
<td data-cell="C6" data-formula="=B6*C2" title="Workbook formula: =B6*C2">70</td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P1</td>
<td data-cell="B7">1</td>
<td data-cell="C7" data-formula="=B7*C2" title="Workbook formula: =B7*C2">35</td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P2</td>
<td data-cell="B8">1</td>
<td data-cell="C8" data-formula="=B8*C2" title="Workbook formula: =B8*C2">35</td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.5</td>
<td data-cell="C9" data-formula="=B9*C2" title="Workbook formula: =B9*C2">17.5</td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">11</td>
<td data-cell="C10" data-formula="=B10*C2" title="Workbook formula: =B10*C2">385</td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">2</td>
<td data-cell="C11" data-formula="=B11*C2" title="Workbook formula: =B11*C2">70</td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12" data-formula="=SUM(B3:B11)" title="Workbook formula: =SUM(B3:B11)">25</td>
<td data-cell="C12" data-formula="=SUM(C3:C11)" title="Workbook formula: =SUM(C3:C11)">875</td>
</tr>
</tbody>
</table>
</div>
</div>
```

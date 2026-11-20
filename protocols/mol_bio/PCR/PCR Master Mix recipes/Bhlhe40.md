---
title: "Bhlhe40"
description: "Interactive PCR master mix calculator from the Bhlhe40 sheet."
author: "Goldrath Lab"
date: last-modified
---

# Bhlhe40

Enter the **number of reactions needed** in the highlighted box. Calculated amounts update automatically using the original workbook formulas. For pages with multiple mixes, set the reaction count for each mix separately.

Column B contains the amount for one reaction; column C contains the amount for the selected number of reactions. Counts include only the reactions you enter; no extra reactions are added.

[Download the original workbook](../../../Goldrath_Protocols/The%20Master%20Folder/PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

```{=html}
<div class="pcr-calculator">
<div class="pcr-controls">
<div class="pcr-control">
<label for="pcr-reactions-c2">Bhlhe40 WT — Number of reactions needed</label>
<input id="pcr-reactions-c2" class="pcr-reaction-input" data-reaction-cell="C2" type="number" min="0" step="1" value="12" required aria-describedby="pcr-reactions-c2-help pcr-reactions-c2-error">
<small id="pcr-reactions-c2-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c2-error" class="pcr-input-error" aria-live="polite"></span>
</div>
<div class="pcr-control">
<label for="pcr-reactions-c16">Bhlhe40 KO — Number of reactions needed</label>
<input id="pcr-reactions-c16" class="pcr-reaction-input" data-reaction-cell="C16" type="number" min="0" step="1" value="12" required aria-describedby="pcr-reactions-c16-help pcr-reactions-c16-error">
<small id="pcr-reactions-c16-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c16-error" class="pcr-input-error" aria-live="polite"></span>
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
<th scope="col">M</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Bhlhe40 WT</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="H1">Folder</td>
<td data-cell="I1">PCR name</td>
<td data-cell="J1">PCR cycle</td>
<td data-cell="K1">Primer Squence</td>
<td data-cell="L1">Band Size</td>
<td data-cell="M1">Image</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2">12</td>
<td data-cell="H2">Laura</td>
<td data-cell="I2">Stra13 (Bhlhe40)</td>
<td data-cell="J2">1. Incubate at 94°C for 5:00</td>
<td data-cell="K2">RT-1 (350rv)  5’-CGTTTTATTCCCCGCCTGGA-3’</td>
<td data-cell="L2">WT and KO- 380-400bp</td>
<td data-cell="M2"></td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="Workbook formula: =B3*C2">60</td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 95°C for 0:30</td>
<td data-cell="K3">RT-2 (STRA13-2RV)  5’-GGAAGCTCAGGCTAGCTCAT-3’</td>
<td data-cell="L3"></td>
<td data-cell="M3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">1.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="Workbook formula: =B4*C2">18</td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 58°C for 0:45</td>
<td data-cell="K4">RT-3 (STRA13-NEO1) 5’-TCGATTCCACCGCCGCCTTCTATG-3’</td>
<td data-cell="L4"></td>
<td data-cell="M4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="Workbook formula: =B5*C2">6</td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 1:00</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
<td data-cell="M5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">RT-1</td>
<td data-cell="B6">1</td>
<td data-cell="C6" data-formula="=B6*C2" title="Workbook formula: =B6*C2">12</td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 29 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
<td data-cell="M6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">RT-2</td>
<td data-cell="B7">1</td>
<td data-cell="C7" data-formula="=B7*C2" title="Workbook formula: =B7*C2">12</td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 5:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
<td data-cell="M7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.2</td>
<td data-cell="C8" data-formula="=B8*C2" title="Workbook formula: =B8*C2">2.4</td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8">7.Incubate at 4°C forever</td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
<td data-cell="M8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">14.8</td>
<td data-cell="C9" data-formula="=B9*C2" title="Workbook formula: =B9*C2">177.6</td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
<td data-cell="L9"></td>
<td data-cell="M9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">DNA</td>
<td data-cell="B10">1</td>
<td data-cell="C10" data-formula="=B10*C2" title="Workbook formula: =B10*C2">12</td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
<td data-cell="M10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11">25</td>
<td data-cell="C11" data-formula="=B11*C2" title="Workbook formula: =B11*C2">300</td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
<td data-cell="M11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12"></td>
<td data-cell="B12"></td>
<td data-cell="C12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
<td data-cell="K12"></td>
<td data-cell="L12"></td>
<td data-cell="M12"></td>
</tr>
<tr>
<th scope="row">13</th>
<td data-cell="A13"></td>
<td data-cell="B13"></td>
<td data-cell="C13"></td>
<td data-cell="H13"></td>
<td data-cell="I13"></td>
<td data-cell="J13"></td>
<td data-cell="K13"></td>
<td data-cell="L13"></td>
<td data-cell="M13"></td>
</tr>
<tr>
<th scope="row">14</th>
<td data-cell="A14"></td>
<td data-cell="B14"></td>
<td data-cell="C14"></td>
<td data-cell="H14"></td>
<td data-cell="I14"></td>
<td data-cell="J14"></td>
<td data-cell="K14"></td>
<td data-cell="L14"></td>
<td data-cell="M14"></td>
</tr>
<tr>
<th scope="row">15</th>
<td data-cell="A15">Bhlhe40 KO</td>
<td data-cell="B15"></td>
<td data-cell="C15"></td>
<td data-cell="H15"></td>
<td data-cell="I15"></td>
<td data-cell="J15"></td>
<td data-cell="K15"></td>
<td data-cell="L15"></td>
<td data-cell="M15"></td>
</tr>
<tr>
<th scope="row">16</th>
<td data-cell="A16"></td>
<td data-cell="B16">x1</td>
<td data-cell="C16">12</td>
<td data-cell="H16"></td>
<td data-cell="I16"></td>
<td data-cell="J16"></td>
<td data-cell="K16"></td>
<td data-cell="L16"></td>
<td data-cell="M16"></td>
</tr>
<tr>
<th scope="row">17</th>
<td data-cell="A17">5x buffer</td>
<td data-cell="B17">5</td>
<td data-cell="C17" data-formula="=B17*C16" title="Workbook formula: =B17*C16">60</td>
<td data-cell="H17"></td>
<td data-cell="I17"></td>
<td data-cell="J17"></td>
<td data-cell="K17"></td>
<td data-cell="L17"></td>
<td data-cell="M17"></td>
</tr>
<tr>
<th scope="row">18</th>
<td data-cell="A18">MgCl2</td>
<td data-cell="B18">1.5</td>
<td data-cell="C18" data-formula="=B18*C16" title="Workbook formula: =B18*C16">18</td>
<td data-cell="H18"></td>
<td data-cell="I18"></td>
<td data-cell="J18"></td>
<td data-cell="K18"></td>
<td data-cell="L18"></td>
<td data-cell="M18"></td>
</tr>
<tr>
<th scope="row">19</th>
<td data-cell="A19">DNTP</td>
<td data-cell="B19">0.5</td>
<td data-cell="C19" data-formula="=B19*C16" title="Workbook formula: =B19*C16">6</td>
<td data-cell="H19"></td>
<td data-cell="I19"></td>
<td data-cell="J19"></td>
<td data-cell="K19"></td>
<td data-cell="L19"></td>
<td data-cell="M19"></td>
</tr>
<tr>
<th scope="row">20</th>
<td data-cell="A20">RT-1</td>
<td data-cell="B20">1</td>
<td data-cell="C20" data-formula="=B20*C16" title="Workbook formula: =B20*C16">12</td>
<td data-cell="H20"></td>
<td data-cell="I20"></td>
<td data-cell="J20"></td>
<td data-cell="K20"></td>
<td data-cell="L20"></td>
<td data-cell="M20"></td>
</tr>
<tr>
<th scope="row">21</th>
<td data-cell="A21">RT-3</td>
<td data-cell="B21">1</td>
<td data-cell="C21" data-formula="=B21*C16" title="Workbook formula: =B21*C16">12</td>
<td data-cell="H21"></td>
<td data-cell="I21"></td>
<td data-cell="J21"></td>
<td data-cell="K21"></td>
<td data-cell="L21"></td>
<td data-cell="M21"></td>
</tr>
<tr>
<th scope="row">22</th>
<td data-cell="A22">Taq</td>
<td data-cell="B22">0.2</td>
<td data-cell="C22" data-formula="=B22*C16" title="Workbook formula: =B22*C16">2.4</td>
<td data-cell="H22"></td>
<td data-cell="I22"></td>
<td data-cell="J22"></td>
<td data-cell="K22"></td>
<td data-cell="L22"></td>
<td data-cell="M22"></td>
</tr>
<tr>
<th scope="row">23</th>
<td data-cell="A23">H20</td>
<td data-cell="B23">14.8</td>
<td data-cell="C23" data-formula="=B23*C16" title="Workbook formula: =B23*C16">177.6</td>
<td data-cell="H23"></td>
<td data-cell="I23"></td>
<td data-cell="J23"></td>
<td data-cell="K23"></td>
<td data-cell="L23"></td>
<td data-cell="M23"></td>
</tr>
<tr>
<th scope="row">24</th>
<td data-cell="A24">DNA</td>
<td data-cell="B24">1</td>
<td data-cell="C24" data-formula="=B24*C16" title="Workbook formula: =B24*C16">12</td>
<td data-cell="H24"></td>
<td data-cell="I24"></td>
<td data-cell="J24"></td>
<td data-cell="K24"></td>
<td data-cell="L24"></td>
<td data-cell="M24"></td>
</tr>
<tr>
<th scope="row">25</th>
<td data-cell="A25">Total</td>
<td data-cell="B25">25</td>
<td data-cell="C25" data-formula="=B25*C16" title="Workbook formula: =B25*C16">300</td>
<td data-cell="H25"></td>
<td data-cell="I25"></td>
<td data-cell="J25"></td>
<td data-cell="K25"></td>
<td data-cell="L25"></td>
<td data-cell="M25"></td>
</tr>
</tbody>
</table>
</div>
</div>
```

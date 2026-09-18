---
title: "PCR master mix recipes"
description: "Interactive PCR master mix recipes from the workbook."
order: 10
author: "Goldrath Lab"
date: last-modified
---

# PCR master mix recipes

[Download the original Excel workbook](PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

Each worksheet is shown below as a collapsible section. Columns D, E, and F are omitted to keep the tables printable.

```{=html}
<style>
.pcr-sheet-controls { margin: 0.75rem 0; }
.pcr-sheet-controls input { margin-left: 0.5rem; max-width: 8rem; }
.pcr-table-wrap { overflow-x: auto; }
.pcr-table td[data-formula] { font-variant-numeric: tabular-nums; }
</style>
```

```{=html}
<details class="pcr-sheet" data-sheet="Id2flox">
<summary><strong>Id2flox</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-0" type="number" min="0" step="1" value="35" aria-label="Number of reactions for Id2flox">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Id2 f/f </td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1">PCR name</td>
<td data-cell="H1">PCR cycle</td>
<td data-cell="I1">Primer Squence</td>
<td data-cell="J1">Band Size</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">35</td>
<td data-cell="G2">ID2flox</td>
<td data-cell="H2">1. Incubate at 94°C for 3:00</td>
<td data-cell="I2">ID2flox F- TTGTGCATAATTAATCGCATCA</td>
<td data-cell="J2">WT-390bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">175</td>
<td data-cell="G3"></td>
<td data-cell="H3">2. Incubate at 94°C for 0:40</td>
<td data-cell="I3">ID2flox R- TTGGGAAGTCACATTTGTAGTG</td>
<td data-cell="J3">Mut-430bp</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">70</td>
<td data-cell="G4"></td>
<td data-cell="H4">3. Incubate at 45°C for 0:40</td>
<td data-cell="I4"></td>
<td data-cell="J4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">17.5</td>
<td data-cell="G5"></td>
<td data-cell="H5">4. Incubate at 72°C for 0:50</td>
<td data-cell="I5"></td>
<td data-cell="J5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">DMSO</td>
<td data-cell="B6">2</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">70</td>
<td data-cell="G6"></td>
<td data-cell="H6">5. Cycle to step 2, 37 times</td>
<td data-cell="I6"></td>
<td data-cell="J6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P1</td>
<td data-cell="B7">2</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">70</td>
<td data-cell="G7"></td>
<td data-cell="H7">6. Incubate at 72°C for 5:00</td>
<td data-cell="I7"></td>
<td data-cell="J7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P2</td>
<td data-cell="B8">2</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">70</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.5</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">17.5</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">9</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">315</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">2</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">70</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12" data-formula="=SUM(B3:B11)" title="=SUM(B3:B11)">25</td>
<td data-cell="C12" data-formula="=SUM(C3:C11)" title="=SUM(C3:C11)">875</td>
<td data-cell="G12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Id2flox_op USE THIS ONE">
<summary><strong>Id2flox_op USE THIS ONE</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-1" type="number" min="0" step="1" value="35" aria-label="Number of reactions for Id2flox_op USE THIS ONE">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Id2 f/f </td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1">PCR name</td>
<td data-cell="H1">PCR cycle</td>
<td data-cell="I1">Primer Squence</td>
<td data-cell="J1">Band Size</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">35</td>
<td data-cell="G2">ID2flox_op</td>
<td data-cell="H2">1. Incubate at 94°C for 3:00</td>
<td data-cell="I2">ID2flox F- TTGTGCATAATTAATCGCATCA</td>
<td data-cell="J2">WT-390bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">175</td>
<td data-cell="G3"></td>
<td data-cell="H3">2. Incubate at 94°C for 0:40</td>
<td data-cell="I3">ID2flox R- TTGGGAAGTCACATTTGTAGTG</td>
<td data-cell="J3">Mut-430bp</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">70</td>
<td data-cell="G4"></td>
<td data-cell="H4">3. Incubate at 60°C for 0:40</td>
<td data-cell="I4"></td>
<td data-cell="J4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">17.5</td>
<td data-cell="G5"></td>
<td data-cell="H5">4. Incubate at 72°C for 0:50</td>
<td data-cell="I5"></td>
<td data-cell="J5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">0.5</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">17.5</td>
<td data-cell="G6"></td>
<td data-cell="H6">5. Cycle to step 2, 37 times</td>
<td data-cell="I6"></td>
<td data-cell="J6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">0.5</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">17.5</td>
<td data-cell="G7"></td>
<td data-cell="H7">6. Incubate at 72°C for 5:00</td>
<td data-cell="I7"></td>
<td data-cell="J7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.5</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">17.5</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">15</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">525</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">DNA</td>
<td data-cell="B10">1</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">35</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11" data-formula="=SUM(B3:B10)" title="=SUM(B3:B10)">25</td>
<td data-cell="C11" data-formula="=SUM(C3:C10)" title="=SUM(C3:C10)">875</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Id2flox Alt">
<summary><strong>Id2flox Alt</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-2" type="number" min="0" step="1" value="35" aria-label="Number of reactions for Id2flox Alt">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Id2 f/f </td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">35</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">175</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">70</td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">17.5</td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">DMSO</td>
<td data-cell="B6">2</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">70</td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P1</td>
<td data-cell="B7">1</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">35</td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P2</td>
<td data-cell="B8">1</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">35</td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.5</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">17.5</td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">11</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">385</td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">2</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">70</td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12" data-formula="=SUM(B3:B11)" title="=SUM(B3:B11)">25</td>
<td data-cell="C12" data-formula="=SUM(C3:C11)" title="=SUM(C3:C11)">875</td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Id3flox USE THIS ONE">
<summary><strong>Id3flox USE THIS ONE</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-3" type="number" min="0" step="1" value="15" aria-label="Number of reactions for Id3flox USE THIS ONE">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
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
<td data-cell="C2" data-reaction-cell="true">15</td>
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
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">75</td>
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
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">37.5</td>
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
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">7.5</td>
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
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">18.75</td>
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
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">18.75</td>
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
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">3</td>
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
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">199.5</td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">15</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11" data-formula="=SUM(B3:B10)" title="=SUM(B3:B10)">25</td>
<td data-cell="C11" data-formula="=SUM(C3:C10)" title="=SUM(C3:C10)">375</td>
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

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Id3flox">
<summary><strong>Id3flox</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-4" type="number" min="0" step="1" value="10" aria-label="Number of reactions for Id3flox">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
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
<td data-cell="C2" data-reaction-cell="true">10</td>
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
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">50</td>
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
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">25</td>
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
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">5</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5">4. Incubate at 72°C for 0:45</td>
<td data-cell="J5"></td>
<td data-cell="K5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">DMSO</td>
<td data-cell="B6">2.5</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6">5. Cycle to step 2, 35 times</td>
<td data-cell="J6"></td>
<td data-cell="K6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P1</td>
<td data-cell="B7">1.7</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">17</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7">6. Incubate at 72°C for 3:00</td>
<td data-cell="J7"></td>
<td data-cell="K7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P2</td>
<td data-cell="B8">1.7</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">17</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.2</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">2</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">8.9</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">89</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">2</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">20</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12" data-formula="=SUM(B3:B11)" title="=SUM(B3:B11)">25</td>
<td data-cell="C12" data-formula="=SUM(C3:C11)" title="=SUM(C3:C11)">250</td>
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

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="P14">
<summary><strong>P14</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-5" type="number" min="0" step="1" value="20" aria-label="Number of reactions for P14">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">P14</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">55 P14</td>
<td data-cell="J2">1. Incubate at 95°C for 3:00</td>
<td data-cell="K2">Vbeta8-</td>
<td data-cell="L2"></td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 1:00</td>
<td data-cell="K3">Cbeta2-</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 55°C for 1:00</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 1:00</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 34 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 3:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.2</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">4</td>
<td data-cell="G8"></td>
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
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">265</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
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
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">500</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Cre">
<summary><strong>Cre</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-6" type="number" min="0" step="1" value="20" aria-label="Number of reactions for Cre">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Cre</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">Cre</td>
<td data-cell="J2">1. Incubate at 94°C for 3:00</td>
<td data-cell="K2">Cre F-gCggTCTggCAgTAAAAACTATC</td>
<td data-cell="L2"></td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">Cre R- gtgaaacagcattgctgtcactt</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
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
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
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
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
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
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
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
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">4</td>
<td data-cell="G8"></td>
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
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">265</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
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
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">500</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="PLZF Cre">
<summary><strong>PLZF Cre</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-7" type="number" min="0" step="1" value="20" aria-label="Number of reactions for PLZF Cre">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
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
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
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
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
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
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
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
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
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
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
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
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
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
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">4</td>
<td data-cell="G8"></td>
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
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">265</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
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
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">500</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="dLCK Cre">
<summary><strong>dLCK Cre</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-8" type="number" min="0" step="1" value="5" aria-label="Number of reactions for dLCK Cre">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
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
<td data-cell="A1">dLCK cre</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
<td data-cell="H1"></td>
<td data-cell="I1">Folder</td>
<td data-cell="J1">PCR name</td>
<td data-cell="K1">PCR cycle</td>
<td data-cell="L1">Primer Squence</td>
<td data-cell="M1">Band Size</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">5</td>
<td data-cell="G2"></td>
<td data-cell="H2"></td>
<td data-cell="I2">Kyla</td>
<td data-cell="J2">Dlck Cre</td>
<td data-cell="K2">1. Incubate at 94°C for 2:00</td>
<td data-cell="L2">Dlck cre F- atggtgcccaagaagaagag</td>
<td data-cell="M2">300bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">25</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3"></td>
<td data-cell="K3">2. Incubate at 94°C for 0:15</td>
<td data-cell="L3">Dlck cre R- caggtgctgttggatggtct</td>
<td data-cell="M3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">3</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">15</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4"></td>
<td data-cell="K4">3. Incubate at 60°C for 0:15</td>
<td data-cell="L4"></td>
<td data-cell="M4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">2.5</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5"></td>
<td data-cell="K5">4. Incubate at 72°C for 0:20</td>
<td data-cell="L5"></td>
<td data-cell="M5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">6.25</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6"></td>
<td data-cell="K6">5. Cycle to step 2, 34 times</td>
<td data-cell="L6"></td>
<td data-cell="M6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">6.25</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7"></td>
<td data-cell="K7">6. Incubate at 72°C for 7:00</td>
<td data-cell="L7"></td>
<td data-cell="M7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.3</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">1.5</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
<td data-cell="M8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">12.45</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">62.25</td>
<td data-cell="G9"></td>
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
<td data-cell="B10">1.25</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">6.25</td>
<td data-cell="G10"></td>
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
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">125</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
<td data-cell="M11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Cre Reporter">
<summary><strong>Cre Reporter</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-9" type="number" min="0" step="1" value="20" aria-label="Number of reactions for Cre Reporter">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">cre reporter</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">Cre rep</td>
<td data-cell="J2">1. Incubate at 94°C for 3:00</td>
<td data-cell="K2">oIMR9020- AAG GGA GCT GCA GTG GAG TA</td>
<td data-cell="L2">Wild type- 297bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">10x buffer</td>
<td data-cell="B3">2.5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">50</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:20</td>
<td data-cell="K3">oIMR9021- CCG AAA ATC TGT GGG AAG TC</td>
<td data-cell="L3">Mutant- 199bp</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">B-ine</td>
<td data-cell="B4">3.45</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">69</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 62°C for 0:30</td>
<td data-cell="K4">oIMR9103- GGC ATT AAA GCA GCG TAT CC</td>
<td data-cell="L4">Het- 297 and 199bp</td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 0:30</td>
<td data-cell="K5">oIMR9104- AAC CAG AAG TGG CAC CTG AC</td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
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
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 2:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P3</td>
<td data-cell="B8">1.25</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">25</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8">7.Incubate at 10°C forever</td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">P4</td>
<td data-cell="B9">1.25</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">25</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
<td data-cell="L9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">Taq</td>
<td data-cell="B10">0.5</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">10</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">H20</td>
<td data-cell="B11">11.05</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">221</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">DNA</td>
<td data-cell="B12">2</td>
<td data-cell="C12" data-formula="=B12*C2" title="=B12*C2">40</td>
<td data-cell="G12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
<td data-cell="K12"></td>
<td data-cell="L12"></td>
</tr>
<tr>
<th scope="row">13</th>
<td data-cell="A13">Total</td>
<td data-cell="B13" data-formula="=SUM(B3:B12)" title="=SUM(B3:B12)">25</td>
<td data-cell="C13" data-formula="=B13*C2" title="=B13*C2">500</td>
<td data-cell="G13"></td>
<td data-cell="H13"></td>
<td data-cell="I13"></td>
<td data-cell="J13"></td>
<td data-cell="K13"></td>
<td data-cell="L13"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="FOXO1">
<summary><strong>FOXO1</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-10" type="number" min="0" step="1" value="20" aria-label="Number of reactions for FOXO1">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Cre</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">FOXO1</td>
<td data-cell="J2">1. Incubate at 94°C for 5:00</td>
<td data-cell="K2">Vbeta8-<br>Cbeta2-<br></td>
<td data-cell="L2"></td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 95°C for 0:30</td>
<td data-cell="K3"></td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 58°C for 0:30</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
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
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
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
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
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
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">4</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8">7.Incubate at 4°C for 5:00</td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">13.25</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">265</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
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
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">500</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="NKT (va14g)">
<summary><strong>NKT (va14g)</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-11" type="number" min="0" step="1" value="20" aria-label="Number of reactions for NKT (va14g)">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">NKT</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Louise</td>
<td data-cell="I2">NKT</td>
<td data-cell="J2">1. Incubate at 94°C for 5:00</td>
<td data-cell="K2">Va14 geno F (iNKT)- CTAAGCACAGCACGCTGCACA</td>
<td data-cell="L2">135bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">Va14 geno R (iNKT)- CAGGTATGACAATCAGCTGAGTCC</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">3</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">60</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 56°C for 0:30</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 0:30</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">0.5</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">10</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 34 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">0.5</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">10</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 10:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.5</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">10</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">13.5</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">270</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11" data-formula="=SUM(B3:B10)" title="=SUM(B3:B10)">24.5</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">490</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="HEB KO">
<summary><strong>HEB KO</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-12" type="number" min="0" step="1" value="20" aria-label="Number of reactions for HEB KO">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Heb KO</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Louise</td>
<td data-cell="I2">HEB+/-</td>
<td data-cell="J2">1. Incubate at 94°C for 3:00</td>
<td data-cell="K2">HEB wt- TCT GAC TTG CTG TTC TAG ACT</td>
<td data-cell="L2">WT- 200bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">HEB ko- TGG ATT CAT CGA CTG TGG</td>
<td data-cell="L3">KO- 800bp</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">3</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">60</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 55°C for 0:30</td>
<td data-cell="K4">HEB com- GAA GGA GAG GCG GAT GGC TAA</td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 1:00</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">0.5</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">10</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 34 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">0.5</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">10</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 5:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P3</td>
<td data-cell="B8">0.5</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">10</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.5</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">10</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
<td data-cell="L9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">13.5</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">270</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">1</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">20</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12" data-formula="=SUM(B3:B11)" title="=SUM(B3:B11)">25</td>
<td data-cell="C12" data-formula="=B12*C2" title="=B12*C2">500</td>
<td data-cell="G12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
<td data-cell="K12"></td>
<td data-cell="L12"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="HEBflox">
<summary><strong>HEBflox</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-13" type="number" min="0" step="1" value="20" aria-label="Number of reactions for HEBflox">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Heb flox</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Louise</td>
<td data-cell="I2">HEBflox</td>
<td data-cell="J2">1. Incubate at 94°C for 3:00</td>
<td data-cell="K2">HEBflox F- CTG GGA CAG AAG TTC AGC ACT TAG TAC</td>
<td data-cell="L2">Deleted-0.5kb</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">10x buffer</td>
<td data-cell="B3">2.5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">50</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">HEBflox R- CAT TCC TAT ACA TCA GCT TCT TGG ACG</td>
<td data-cell="L3">Flox- 1.3kb</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">3</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">60</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 59.5°C for 0:30</td>
<td data-cell="K4"></td>
<td data-cell="L4">WT- 1.1kb</td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 1:30</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.5</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">30</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 37 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.5</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">30</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 10:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.5</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">10</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">14.5</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">290</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11" data-formula="=SUM(B3:B10)" title="=SUM(B3:B10)">25</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">500</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="E2Aflox">
<summary><strong>E2Aflox</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-14" type="number" min="0" step="1" value="20" aria-label="Number of reactions for E2Aflox">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">E2A flox</td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2">Louise</td>
<td data-cell="H2">E2Aflox</td>
<td data-cell="I2">1. Incubate at 94°C for 3:00</td>
<td data-cell="J2">E2Aflox F1- GCCACCAGCACATCGTGCCTA</td>
<td data-cell="K2">WT band- 850bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">10x buffer</td>
<td data-cell="B3">2.5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">50</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3">2. Incubate at 94°C for 0:30</td>
<td data-cell="J3">E2Aflox R3- CCACATAAGAGGGCATGGAAG</td>
<td data-cell="K3">flox band- 1kb</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">B-ine</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4">3. Incubate at 65°C for 0:30</td>
<td data-cell="J4">YZ150- ACATGGCTGAATATCGACGGT</td>
<td data-cell="K4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">MgCl2</td>
<td data-cell="B5">3</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">60</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5">4. Incubate at 72°C for 1:00</td>
<td data-cell="J5"></td>
<td data-cell="K5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">DNTP</td>
<td data-cell="B6">0.5</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">10</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6">5. Cycle to step 2, 39 times</td>
<td data-cell="J6"></td>
<td data-cell="K6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P1</td>
<td data-cell="B7">1.5</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">30</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7">6. Incubate at 72°C for 5:00</td>
<td data-cell="J7"></td>
<td data-cell="K7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P2</td>
<td data-cell="B8">1.5</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">30</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">P3</td>
<td data-cell="B9">1.5</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">30</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">Taq</td>
<td data-cell="B10">0.5</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">10</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">H20</td>
<td data-cell="B11">10.5</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">210</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">DNA</td>
<td data-cell="B12">1</td>
<td data-cell="C12" data-formula="=B12*C2" title="=B12*C2">20</td>
<td data-cell="G12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
<td data-cell="K12"></td>
</tr>
<tr>
<th scope="row">13</th>
<td data-cell="A13">Total</td>
<td data-cell="B13" data-formula="=SUM(B3:B12)" title="=SUM(B3:B12)">25</td>
<td data-cell="C13" data-formula="=B13*C2" title="=B13*C2">500</td>
<td data-cell="G13"></td>
<td data-cell="H13"></td>
<td data-cell="I13"></td>
<td data-cell="J13"></td>
<td data-cell="K13"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Zeb2flox">
<summary><strong>Zeb2flox</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-15" type="number" min="0" step="1" value="20" aria-label="Number of reactions for Zeb2flox">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Zeb2 flox</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Adam</td>
<td data-cell="I2">Zeb Geno</td>
<td data-cell="J2">1. Incubate at 94°C for 3:00</td>
<td data-cell="K2">Sip1 geno P1 F-GAGCAGGTAACCGCAAGTTCAAGTG</td>
<td data-cell="L2"></td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">Sip1 geno P2 R- CTGTAGGACCCAGAATGAGAGAAGC</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 59°C for 1:00</td>
<td data-cell="K4">Sip1 geno P3 R- ATCGGAGTCTGTCATGTCATCTAGG</td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 1:00</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
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
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 5:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P3</td>
<td data-cell="B8">1.25</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">25</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.25</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">5</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
<td data-cell="L9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">13.25</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">265</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">1</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">20</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12">25</td>
<td data-cell="C12" data-formula="=B12*C2" title="=B12*C2">500</td>
<td data-cell="G12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
<td data-cell="K12"></td>
<td data-cell="L12"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Tbetflox">
<summary><strong>Tbetflox</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-16" type="number" min="0" step="1" value="20" aria-label="Number of reactions for Tbetflox">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Tbetflox</td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2">Cliff</td>
<td data-cell="H2">Tbet</td>
<td data-cell="I2">1. Incubate at 94°C for 3:00</td>
<td data-cell="J2">Tbet IMR 1717- gcgcgaaggggccaccaaagaacggag</td>
<td data-cell="K2"></td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3">2. Incubate at 94°C for 0:30</td>
<td data-cell="J3">Tbet IMR 1718- gactgaagccccgacccccactcctaag</td>
<td data-cell="K3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4">3. Incubate at 94°C for 0:30</td>
<td data-cell="J4">Tbet IMR 1719-tgggcatacaggaggcagcaacaaata</td>
<td data-cell="K4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5">4. Incubate at 60°C for 0:30</td>
<td data-cell="J5"></td>
<td data-cell="K5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6">5.Incubate at 72° C for 0:30</td>
<td data-cell="J6"></td>
<td data-cell="K6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7">6. Cycle to step 2, 35 times</td>
<td data-cell="J7"></td>
<td data-cell="K7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P3</td>
<td data-cell="B8">1.25</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">25</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8">7.Incubate at 10°C for 1:00</td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.25</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">5</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">12</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">240</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">1</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">20</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12">25</td>
<td data-cell="C12" data-formula="=B12*C2" title="=B12*C2">500</td>
<td data-cell="G12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
<td data-cell="K12"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="OT-I">
<summary><strong>OT-I</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-17" type="number" min="0" step="1" value="20" aria-label="Number of reactions for OT-I">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">OT-1</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">OT-1</td>
<td data-cell="J2">1. Incubate at 95°C for 3:00</td>
<td data-cell="K2">Vb5 F- AAGGTGGAGAGAGACAAAGGA</td>
<td data-cell="L2"></td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 1:00</td>
<td data-cell="K3">Vb5 R- CCAGTGCATGCATACCTCAG</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 55°C for 1:00</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 1:00</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 34 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 3:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.25</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">5</td>
<td data-cell="G8"></td>
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
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">265</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11" data-formula="=SUM(B3:B10)" title="=SUM(B3:B10)">25</td>
<td data-cell="C11" data-formula="=SUM(C3:C10)" title="=SUM(C3:C10)">500</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="Bhlhe40">
<summary><strong>Bhlhe40</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-18" type="number" min="0" step="1" value="12" aria-label="Number of reactions for Bhlhe40">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
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
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">12</td>
<td data-cell="G2"></td>
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
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">60</td>
<td data-cell="G3"></td>
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
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">18</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 58°C for 0:45</td>
<td data-cell="K4">RT-3 (STRA13-NEO1) 5’-TCGATTCCACCGCCGCCTTCTATG-3’ </td>
<td data-cell="L4"></td>
<td data-cell="M4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">6</td>
<td data-cell="G5"></td>
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
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">12</td>
<td data-cell="G6"></td>
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
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">12</td>
<td data-cell="G7"></td>
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
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">2.4</td>
<td data-cell="G8"></td>
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
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">177.6</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">12</td>
<td data-cell="G10"></td>
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
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">300</td>
<td data-cell="G11"></td>
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
<td data-cell="G12"></td>
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
<td data-cell="G13"></td>
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
<td data-cell="G14"></td>
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
<td data-cell="G15"></td>
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
<td data-cell="C16" data-reaction-cell="true">12</td>
<td data-cell="G16"></td>
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
<td data-cell="C17" data-formula="=B17*C16" title="=B17*C16">60</td>
<td data-cell="G17"></td>
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
<td data-cell="C18" data-formula="=B18*C16" title="=B18*C16">18</td>
<td data-cell="G18"></td>
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
<td data-cell="C19" data-formula="=B19*C16" title="=B19*C16">6</td>
<td data-cell="G19"></td>
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
<td data-cell="C20" data-formula="=B20*C16" title="=B20*C16">12</td>
<td data-cell="G20"></td>
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
<td data-cell="C21" data-formula="=B21*C16" title="=B21*C16">12</td>
<td data-cell="G21"></td>
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
<td data-cell="C22" data-formula="=B22*C16" title="=B22*C16">2.4</td>
<td data-cell="G22"></td>
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
<td data-cell="C23" data-formula="=B23*C16" title="=B23*C16">177.6</td>
<td data-cell="G23"></td>
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
<td data-cell="C24" data-formula="=B24*C16" title="=B24*C16">12</td>
<td data-cell="G24"></td>
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
<td data-cell="C25" data-formula="=B25*C16" title="=B25*C16">300</td>
<td data-cell="G25"></td>
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

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="HIFVHL">
<summary><strong>HIFVHL</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-19" type="number" min="0" step="1" value="40" aria-label="Number of reactions for HIFVHL">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">HIF1/VHL</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">40</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">200</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">1.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">60</td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">20</td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">50</td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">50</td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.3</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">12</td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">13.95</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">558</td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">DNA</td>
<td data-cell="B10">1.25</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">50</td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11" data-formula="=SUM(B3:B10)" title="=SUM(B3:B10)">25</td>
<td data-cell="C11" data-formula="=SUM(C3:C10)" title="=SUM(C3:C10)">1000</td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="HIF2">
<summary><strong>HIF2</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-20" type="number" min="0" step="1" value="40" aria-label="Number of reactions for HIF2">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">HIF2</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">40</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">200</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">80</td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">20</td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">2</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">80</td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">2</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">80</td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.3</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">12</td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">11.95</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">478</td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">DNA</td>
<td data-cell="B10">1.25</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">50</td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11" data-formula="=SUM(B3:B10)" title="=SUM(B3:B10)">25</td>
<td data-cell="C11" data-formula="=SUM(C3:C10)" title="=SUM(C3:C10)">1000</td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="E2-2 Reporter">
<summary><strong>E2-2 Reporter</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-21" type="number" min="0" step="1" value="20" aria-label="Number of reactions for E2-2 Reporter">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">TCF4 WT</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">E2-2 GEN</td>
<td data-cell="J2">1. Incubate at 94°C for 5:00</td>
<td data-cell="K2">TCF4 WT F-CCGATGACAGTGATGATGGT</td>
<td data-cell="L2">300bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">10x NEB buffer</td>
<td data-cell="B3">4</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">80</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">TCF4 WT R-AAGTTAAGCTGAAGTAAATACCCACA</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">0.6</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">12</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 58°C for 0:30</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.2</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">4</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 0:45</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">0.4</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">8</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 35 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">0.4</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">8</td>
<td data-cell="G7"></td>
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
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">4</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">15.2</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">304</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11">20</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">400</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
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
<td data-cell="L12"></td>
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
<td data-cell="L13"></td>
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
<td data-cell="L14"></td>
</tr>
<tr>
<th scope="row">15</th>
<td data-cell="A15">TCF4 Mut</td>
<td data-cell="B15"></td>
<td data-cell="C15"></td>
<td data-cell="G15"></td>
<td data-cell="H15"></td>
<td data-cell="I15"></td>
<td data-cell="J15"></td>
<td data-cell="K15"></td>
<td data-cell="L15"></td>
</tr>
<tr>
<th scope="row">16</th>
<td data-cell="A16"></td>
<td data-cell="B16">x1</td>
<td data-cell="C16" data-reaction-cell="true">20</td>
<td data-cell="G16"></td>
<td data-cell="H16">Folder</td>
<td data-cell="I16">PCR name</td>
<td data-cell="J16">PCR cycle</td>
<td data-cell="K16">Primer Squence</td>
<td data-cell="L16">Band Size</td>
</tr>
<tr>
<th scope="row">17</th>
<td data-cell="A17">10x NEB buffer</td>
<td data-cell="B17">4</td>
<td data-cell="C17" data-formula="=B17*C16" title="=B17*C16">80</td>
<td data-cell="G17"></td>
<td data-cell="H17">Kyla</td>
<td data-cell="I17">E2-2 GEN</td>
<td data-cell="J17">1. Incubate at 94°C for 5:00</td>
<td data-cell="K17">TCF4 MUT F-CCGATGACAGTGATGATGGT</td>
<td data-cell="L17">172bp</td>
</tr>
<tr>
<th scope="row">18</th>
<td data-cell="A18">MgCl2</td>
<td data-cell="B18">0.6</td>
<td data-cell="C18" data-formula="=B18*C16" title="=B18*C16">12</td>
<td data-cell="G18"></td>
<td data-cell="H18"></td>
<td data-cell="I18"></td>
<td data-cell="J18">2. Incubate at 94°C for 0:30</td>
<td data-cell="K18">TCF4 Mut R-TCGTGGTATCGTTATGCGCC</td>
<td data-cell="L18"></td>
</tr>
<tr>
<th scope="row">19</th>
<td data-cell="A19">DNTP</td>
<td data-cell="B19">0.2</td>
<td data-cell="C19" data-formula="=B19*C16" title="=B19*C16">4</td>
<td data-cell="G19"></td>
<td data-cell="H19"></td>
<td data-cell="I19"></td>
<td data-cell="J19">3. Incubate at 58°C for 0:30</td>
<td data-cell="K19"></td>
<td data-cell="L19"></td>
</tr>
<tr>
<th scope="row">20</th>
<td data-cell="A20">P1</td>
<td data-cell="B20">0.4</td>
<td data-cell="C20" data-formula="=B20*C16" title="=B20*C16">8</td>
<td data-cell="G20"></td>
<td data-cell="H20"></td>
<td data-cell="I20"></td>
<td data-cell="J20">4. Incubate at 72°C for 0:45</td>
<td data-cell="K20"></td>
<td data-cell="L20"></td>
</tr>
<tr>
<th scope="row">21</th>
<td data-cell="A21">P2</td>
<td data-cell="B21">0.4</td>
<td data-cell="C21" data-formula="=B21*C16" title="=B21*C16">8</td>
<td data-cell="G21"></td>
<td data-cell="H21"></td>
<td data-cell="I21"></td>
<td data-cell="J21">5. Cycle to step 2, 35 times</td>
<td data-cell="K21"></td>
<td data-cell="L21"></td>
</tr>
<tr>
<th scope="row">22</th>
<td data-cell="A22">Taq</td>
<td data-cell="B22">0.2</td>
<td data-cell="C22" data-formula="=B22*C16" title="=B22*C16">4</td>
<td data-cell="G22"></td>
<td data-cell="H22"></td>
<td data-cell="I22"></td>
<td data-cell="J22">6. Incubate at 72°C for 5:00</td>
<td data-cell="K22"></td>
<td data-cell="L22"></td>
</tr>
<tr>
<th scope="row">23</th>
<td data-cell="A23">H20</td>
<td data-cell="B23">15.2</td>
<td data-cell="C23" data-formula="=B23*C16" title="=B23*C16">304</td>
<td data-cell="G23"></td>
<td data-cell="H23"></td>
<td data-cell="I23"></td>
<td data-cell="J23"></td>
<td data-cell="K23"></td>
<td data-cell="L23"></td>
</tr>
<tr>
<th scope="row">24</th>
<td data-cell="A24">DNA</td>
<td data-cell="B24">1</td>
<td data-cell="C24" data-formula="=B24*C16" title="=B24*C16">20</td>
<td data-cell="G24"></td>
<td data-cell="H24"></td>
<td data-cell="I24"></td>
<td data-cell="J24"></td>
<td data-cell="K24"></td>
<td data-cell="L24"></td>
</tr>
<tr>
<th scope="row">25</th>
<td data-cell="A25">Total</td>
<td data-cell="B25">20</td>
<td data-cell="C25" data-formula="=B25*C16" title="=B25*C16">400</td>
<td data-cell="G25"></td>
<td data-cell="H25"></td>
<td data-cell="I25"></td>
<td data-cell="J25"></td>
<td data-cell="K25"></td>
<td data-cell="L25"></td>
</tr>
<tr>
<th scope="row">26</th>
<td data-cell="A26"></td>
<td data-cell="B26">25</td>
<td data-cell="C26" data-formula="=B26*C16" title="=B26*C16">500</td>
<td data-cell="G26"></td>
<td data-cell="H26"></td>
<td data-cell="I26"></td>
<td data-cell="J26"></td>
<td data-cell="K26"></td>
<td data-cell="L26"></td>
</tr>
<tr>
<th scope="row">27</th>
<td data-cell="A27"></td>
<td data-cell="B27"></td>
<td data-cell="C27"></td>
<td data-cell="G27"></td>
<td data-cell="H27"></td>
<td data-cell="I27"></td>
<td data-cell="J27"></td>
<td data-cell="K27"></td>
<td data-cell="L27"></td>
</tr>
<tr>
<th scope="row">28</th>
<td data-cell="A28"></td>
<td data-cell="B28"></td>
<td data-cell="C28"></td>
<td data-cell="G28"></td>
<td data-cell="H28"></td>
<td data-cell="I28"></td>
<td data-cell="J28"></td>
<td data-cell="K28"></td>
<td data-cell="L28"></td>
</tr>
<tr>
<th scope="row">29</th>
<td data-cell="A29">LacZ</td>
<td data-cell="B29"></td>
<td data-cell="C29"></td>
<td data-cell="G29"></td>
<td data-cell="H29"></td>
<td data-cell="I29"></td>
<td data-cell="J29"></td>
<td data-cell="K29"></td>
<td data-cell="L29"></td>
</tr>
<tr>
<th scope="row">30</th>
<td data-cell="A30"></td>
<td data-cell="B30">x1</td>
<td data-cell="C30" data-reaction-cell="true">20</td>
<td data-cell="G30"></td>
<td data-cell="H30">Folder</td>
<td data-cell="I30">PCR name</td>
<td data-cell="J30">PCR cycle</td>
<td data-cell="K30">Primer Squence</td>
<td data-cell="L30">Band Size</td>
</tr>
<tr>
<th scope="row">31</th>
<td data-cell="A31">10x NEB buffer</td>
<td data-cell="B31">2</td>
<td data-cell="C31" data-formula="=B31*C30" title="=B31*C30">40</td>
<td data-cell="G31"></td>
<td data-cell="H31">Kyla</td>
<td data-cell="I31">LacZ</td>
<td data-cell="J31">1. Incubate at 94°C for 5:00</td>
<td data-cell="K31">LacZ F2-GAGTTGCGTGACTACCTACGG</td>
<td data-cell="L31">371bp</td>
</tr>
<tr>
<th scope="row">32</th>
<td data-cell="A32">MgCl2</td>
<td data-cell="B32">2</td>
<td data-cell="C32" data-formula="=B32*C30" title="=B32*C30">40</td>
<td data-cell="G32"></td>
<td data-cell="H32"></td>
<td data-cell="I32"></td>
<td data-cell="J32">2. Incubate at 94°C for 0:30</td>
<td data-cell="K32">LacZ R1-</td>
<td data-cell="L32"></td>
</tr>
<tr>
<th scope="row">33</th>
<td data-cell="A33">DNTP</td>
<td data-cell="B33">0.2</td>
<td data-cell="C33" data-formula="=B33*C30" title="=B33*C30">4</td>
<td data-cell="G33"></td>
<td data-cell="H33"></td>
<td data-cell="I33"></td>
<td data-cell="J33">3. Incubate at 60°C for 0:30</td>
<td data-cell="K33"></td>
<td data-cell="L33"></td>
</tr>
<tr>
<th scope="row">34</th>
<td data-cell="A34">P1</td>
<td data-cell="B34">0.4</td>
<td data-cell="C34" data-formula="=B34*C30" title="=B34*C30">8</td>
<td data-cell="G34"></td>
<td data-cell="H34"></td>
<td data-cell="I34"></td>
<td data-cell="J34">4. Incubate at 72°C for 0:30</td>
<td data-cell="K34"></td>
<td data-cell="L34"></td>
</tr>
<tr>
<th scope="row">35</th>
<td data-cell="A35">P2</td>
<td data-cell="B35">0.4</td>
<td data-cell="C35" data-formula="=B35*C30" title="=B35*C30">8</td>
<td data-cell="G35"></td>
<td data-cell="H35"></td>
<td data-cell="I35"></td>
<td data-cell="J35">5. Cycle to step 2, 35 times</td>
<td data-cell="K35"></td>
<td data-cell="L35"></td>
</tr>
<tr>
<th scope="row">36</th>
<td data-cell="A36">NEB Taq</td>
<td data-cell="B36">0.2</td>
<td data-cell="C36" data-formula="=B36*C30" title="=B36*C30">4</td>
<td data-cell="G36"></td>
<td data-cell="H36"></td>
<td data-cell="I36"></td>
<td data-cell="J36">6. Incubate at 72°C for 5:00</td>
<td data-cell="K36"></td>
<td data-cell="L36"></td>
</tr>
<tr>
<th scope="row">37</th>
<td data-cell="A37">H20</td>
<td data-cell="B37">13.8</td>
<td data-cell="C37" data-formula="=B37*C30" title="=B37*C30">276</td>
<td data-cell="G37"></td>
<td data-cell="H37"></td>
<td data-cell="I37"></td>
<td data-cell="J37"></td>
<td data-cell="K37"></td>
<td data-cell="L37"></td>
</tr>
<tr>
<th scope="row">38</th>
<td data-cell="A38">DNA</td>
<td data-cell="B38">1</td>
<td data-cell="C38" data-formula="=B38*C30" title="=B38*C30">20</td>
<td data-cell="G38"></td>
<td data-cell="H38"></td>
<td data-cell="I38"></td>
<td data-cell="J38"></td>
<td data-cell="K38"></td>
<td data-cell="L38"></td>
</tr>
<tr>
<th scope="row">39</th>
<td data-cell="A39">Total</td>
<td data-cell="B39">20</td>
<td data-cell="C39" data-formula="=B39*C30" title="=B39*C30">400</td>
<td data-cell="G39"></td>
<td data-cell="H39"></td>
<td data-cell="I39"></td>
<td data-cell="J39"></td>
<td data-cell="K39"></td>
<td data-cell="L39"></td>
</tr>
<tr>
<th scope="row">40</th>
<td data-cell="A40"></td>
<td data-cell="B40"></td>
<td data-cell="C40"></td>
<td data-cell="G40"></td>
<td data-cell="H40"></td>
<td data-cell="I40"></td>
<td data-cell="J40"></td>
<td data-cell="K40"></td>
<td data-cell="L40"></td>
</tr>
<tr>
<th scope="row">41</th>
<td data-cell="A41">FOR LACZ PCR NEED TO USE NEB TAQ AS OUR LAB STOCK IS CONTAMINATED WITH LACZ AND ALL PCRS WILL BE POSITIVE</td>
<td data-cell="B41"></td>
<td data-cell="C41"></td>
<td data-cell="G41"></td>
<td data-cell="H41"></td>
<td data-cell="I41"></td>
<td data-cell="J41"></td>
<td data-cell="K41"></td>
<td data-cell="L41"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="E2-2 Conditional">
<summary><strong>E2-2 Conditional</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-22" type="number" min="0" step="1" value="20" aria-label="Number of reactions for E2-2 Conditional">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">TCF4 WT</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">E2-2 GEN</td>
<td data-cell="J2">1. Incubate at 94°C for 5:00</td>
<td data-cell="K2">TCF4 WT F-CCGATGACAGTGATGATGGT</td>
<td data-cell="L2">300bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">10x NEB buffer</td>
<td data-cell="B3">2</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">40</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">TCF4 WT R-AAGTTAAGCTGAAGTAAATACCCACA</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">0.6</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">12</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 58°C for 0:30</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.2</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">4</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 0:45</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">0.4</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">8</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 35 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">0.4</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">8</td>
<td data-cell="G7"></td>
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
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">4</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8"></td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">15.2</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">304</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11">20</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">400</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
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
<td data-cell="L12"></td>
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
<td data-cell="L13"></td>
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
<td data-cell="L14"></td>
</tr>
<tr>
<th scope="row">15</th>
<td data-cell="A15">TCF4 Mut</td>
<td data-cell="B15"></td>
<td data-cell="C15"></td>
<td data-cell="G15"></td>
<td data-cell="H15"></td>
<td data-cell="I15"></td>
<td data-cell="J15"></td>
<td data-cell="K15"></td>
<td data-cell="L15"></td>
</tr>
<tr>
<th scope="row">16</th>
<td data-cell="A16"></td>
<td data-cell="B16">x1</td>
<td data-cell="C16" data-reaction-cell="true">20</td>
<td data-cell="G16"></td>
<td data-cell="H16">Folder</td>
<td data-cell="I16">PCR name</td>
<td data-cell="J16">PCR cycle</td>
<td data-cell="K16">Primer Squence</td>
<td data-cell="L16">Band Size</td>
</tr>
<tr>
<th scope="row">17</th>
<td data-cell="A17">10x NEB buffer</td>
<td data-cell="B17">2</td>
<td data-cell="C17" data-formula="=B17*C16" title="=B17*C16">40</td>
<td data-cell="G17"></td>
<td data-cell="H17">Kyla</td>
<td data-cell="I17">E2-2 GEN</td>
<td data-cell="J17">1. Incubate at 94°C for 5:00</td>
<td data-cell="K17">TCF4 MUT F-CCGATGACAGTGATGATGGT</td>
<td data-cell="L17">172bp</td>
</tr>
<tr>
<th scope="row">18</th>
<td data-cell="A18">MgCl2</td>
<td data-cell="B18">0.6</td>
<td data-cell="C18" data-formula="=B18*C16" title="=B18*C16">12</td>
<td data-cell="G18"></td>
<td data-cell="H18"></td>
<td data-cell="I18"></td>
<td data-cell="J18">2. Incubate at 94°C for 0:30</td>
<td data-cell="K18">TCF4 Mut R-TCGTGGTATCGTTATGCGCC</td>
<td data-cell="L18"></td>
</tr>
<tr>
<th scope="row">19</th>
<td data-cell="A19">DNTP</td>
<td data-cell="B19">0.2</td>
<td data-cell="C19" data-formula="=B19*C16" title="=B19*C16">4</td>
<td data-cell="G19"></td>
<td data-cell="H19"></td>
<td data-cell="I19"></td>
<td data-cell="J19">3. Incubate at 58°C for 0:30</td>
<td data-cell="K19"></td>
<td data-cell="L19"></td>
</tr>
<tr>
<th scope="row">20</th>
<td data-cell="A20">P1</td>
<td data-cell="B20">0.4</td>
<td data-cell="C20" data-formula="=B20*C16" title="=B20*C16">8</td>
<td data-cell="G20"></td>
<td data-cell="H20"></td>
<td data-cell="I20"></td>
<td data-cell="J20">4. Incubate at 72°C for 0:45</td>
<td data-cell="K20"></td>
<td data-cell="L20"></td>
</tr>
<tr>
<th scope="row">21</th>
<td data-cell="A21">P2</td>
<td data-cell="B21">0.4</td>
<td data-cell="C21" data-formula="=B21*C16" title="=B21*C16">8</td>
<td data-cell="G21"></td>
<td data-cell="H21"></td>
<td data-cell="I21"></td>
<td data-cell="J21">5. Cycle to step 2, 35 times</td>
<td data-cell="K21"></td>
<td data-cell="L21"></td>
</tr>
<tr>
<th scope="row">22</th>
<td data-cell="A22">Taq</td>
<td data-cell="B22">0.2</td>
<td data-cell="C22" data-formula="=B22*C16" title="=B22*C16">4</td>
<td data-cell="G22"></td>
<td data-cell="H22"></td>
<td data-cell="I22"></td>
<td data-cell="J22">6. Incubate at 72°C for 5:00</td>
<td data-cell="K22"></td>
<td data-cell="L22"></td>
</tr>
<tr>
<th scope="row">23</th>
<td data-cell="A23">H20</td>
<td data-cell="B23">15.2</td>
<td data-cell="C23" data-formula="=B23*C16" title="=B23*C16">304</td>
<td data-cell="G23"></td>
<td data-cell="H23"></td>
<td data-cell="I23"></td>
<td data-cell="J23"></td>
<td data-cell="K23"></td>
<td data-cell="L23"></td>
</tr>
<tr>
<th scope="row">24</th>
<td data-cell="A24">DNA</td>
<td data-cell="B24">1</td>
<td data-cell="C24" data-formula="=B24*C16" title="=B24*C16">20</td>
<td data-cell="G24"></td>
<td data-cell="H24"></td>
<td data-cell="I24"></td>
<td data-cell="J24"></td>
<td data-cell="K24"></td>
<td data-cell="L24"></td>
</tr>
<tr>
<th scope="row">25</th>
<td data-cell="A25">Total</td>
<td data-cell="B25">20</td>
<td data-cell="C25" data-formula="=B25*C16" title="=B25*C16">400</td>
<td data-cell="G25"></td>
<td data-cell="H25"></td>
<td data-cell="I25"></td>
<td data-cell="J25"></td>
<td data-cell="K25"></td>
<td data-cell="L25"></td>
</tr>
<tr>
<th scope="row">26</th>
<td data-cell="A26"></td>
<td data-cell="B26">25</td>
<td data-cell="C26" data-formula="=B26*C16" title="=B26*C16">500</td>
<td data-cell="G26"></td>
<td data-cell="H26"></td>
<td data-cell="I26"></td>
<td data-cell="J26"></td>
<td data-cell="K26"></td>
<td data-cell="L26"></td>
</tr>
<tr>
<th scope="row">27</th>
<td data-cell="A27"></td>
<td data-cell="B27"></td>
<td data-cell="C27"></td>
<td data-cell="G27"></td>
<td data-cell="H27"></td>
<td data-cell="I27"></td>
<td data-cell="J27"></td>
<td data-cell="K27"></td>
<td data-cell="L27"></td>
</tr>
<tr>
<th scope="row">28</th>
<td data-cell="A28"></td>
<td data-cell="B28"></td>
<td data-cell="C28"></td>
<td data-cell="G28"></td>
<td data-cell="H28"></td>
<td data-cell="I28"></td>
<td data-cell="J28"></td>
<td data-cell="K28"></td>
<td data-cell="L28"></td>
</tr>
<tr>
<th scope="row">29</th>
<td data-cell="A29">LacZ</td>
<td data-cell="B29"></td>
<td data-cell="C29"></td>
<td data-cell="G29"></td>
<td data-cell="H29"></td>
<td data-cell="I29"></td>
<td data-cell="J29"></td>
<td data-cell="K29"></td>
<td data-cell="L29"></td>
</tr>
<tr>
<th scope="row">30</th>
<td data-cell="A30"></td>
<td data-cell="B30">x1</td>
<td data-cell="C30" data-reaction-cell="true">20</td>
<td data-cell="G30"></td>
<td data-cell="H30">Folder</td>
<td data-cell="I30">PCR name</td>
<td data-cell="J30">PCR cycle</td>
<td data-cell="K30">Primer Squence</td>
<td data-cell="L30">Band Size</td>
</tr>
<tr>
<th scope="row">31</th>
<td data-cell="A31">10x NEB buffer</td>
<td data-cell="B31">2</td>
<td data-cell="C31" data-formula="=B31*C30" title="=B31*C30">40</td>
<td data-cell="G31"></td>
<td data-cell="H31">Kyla</td>
<td data-cell="I31">LacZ</td>
<td data-cell="J31">1. Incubate at 94°C for 5:00</td>
<td data-cell="K31">LacZ F2-GAGTTGCGTGACTACCTACGG</td>
<td data-cell="L31">371bp</td>
</tr>
<tr>
<th scope="row">32</th>
<td data-cell="A32">MgCl2</td>
<td data-cell="B32">2</td>
<td data-cell="C32" data-formula="=B32*C30" title="=B32*C30">40</td>
<td data-cell="G32"></td>
<td data-cell="H32"></td>
<td data-cell="I32"></td>
<td data-cell="J32">2. Incubate at 94°C for 0:30</td>
<td data-cell="K32">LacZ R1-</td>
<td data-cell="L32"></td>
</tr>
<tr>
<th scope="row">33</th>
<td data-cell="A33">DNTP</td>
<td data-cell="B33">0.2</td>
<td data-cell="C33" data-formula="=B33*C30" title="=B33*C30">4</td>
<td data-cell="G33"></td>
<td data-cell="H33"></td>
<td data-cell="I33"></td>
<td data-cell="J33">3. Incubate at 60°C for 0:30</td>
<td data-cell="K33"></td>
<td data-cell="L33"></td>
</tr>
<tr>
<th scope="row">34</th>
<td data-cell="A34">P1</td>
<td data-cell="B34">0.4</td>
<td data-cell="C34" data-formula="=B34*C30" title="=B34*C30">8</td>
<td data-cell="G34"></td>
<td data-cell="H34"></td>
<td data-cell="I34"></td>
<td data-cell="J34">4. Incubate at 72°C for 0:30</td>
<td data-cell="K34"></td>
<td data-cell="L34"></td>
</tr>
<tr>
<th scope="row">35</th>
<td data-cell="A35">P2</td>
<td data-cell="B35">0.4</td>
<td data-cell="C35" data-formula="=B35*C30" title="=B35*C30">8</td>
<td data-cell="G35"></td>
<td data-cell="H35"></td>
<td data-cell="I35"></td>
<td data-cell="J35">5. Cycle to step 2, 35 times</td>
<td data-cell="K35"></td>
<td data-cell="L35"></td>
</tr>
<tr>
<th scope="row">36</th>
<td data-cell="A36">NEB Taq</td>
<td data-cell="B36">0.2</td>
<td data-cell="C36" data-formula="=B36*C30" title="=B36*C30">4</td>
<td data-cell="G36"></td>
<td data-cell="H36"></td>
<td data-cell="I36"></td>
<td data-cell="J36">6. Incubate at 72°C for 5:00</td>
<td data-cell="K36"></td>
<td data-cell="L36"></td>
</tr>
<tr>
<th scope="row">37</th>
<td data-cell="A37">H20</td>
<td data-cell="B37">13.8</td>
<td data-cell="C37" data-formula="=B37*C30" title="=B37*C30">276</td>
<td data-cell="G37"></td>
<td data-cell="H37"></td>
<td data-cell="I37"></td>
<td data-cell="J37"></td>
<td data-cell="K37"></td>
<td data-cell="L37"></td>
</tr>
<tr>
<th scope="row">38</th>
<td data-cell="A38">DNA</td>
<td data-cell="B38">1</td>
<td data-cell="C38" data-formula="=B38*C30" title="=B38*C30">20</td>
<td data-cell="G38"></td>
<td data-cell="H38"></td>
<td data-cell="I38"></td>
<td data-cell="J38"></td>
<td data-cell="K38"></td>
<td data-cell="L38"></td>
</tr>
<tr>
<th scope="row">39</th>
<td data-cell="A39">Total</td>
<td data-cell="B39">20</td>
<td data-cell="C39" data-formula="=B39*C30" title="=B39*C30">400</td>
<td data-cell="G39"></td>
<td data-cell="H39"></td>
<td data-cell="I39"></td>
<td data-cell="J39"></td>
<td data-cell="K39"></td>
<td data-cell="L39"></td>
</tr>
<tr>
<th scope="row">40</th>
<td data-cell="A40"></td>
<td data-cell="B40"></td>
<td data-cell="C40"></td>
<td data-cell="G40"></td>
<td data-cell="H40"></td>
<td data-cell="I40"></td>
<td data-cell="J40"></td>
<td data-cell="K40"></td>
<td data-cell="L40"></td>
</tr>
<tr>
<th scope="row">41</th>
<td data-cell="A41">FOR LACZ PCR NEED TO USE NEB TAQ AS OUR LAB STOCK IS CONTAMINATED WITH LACZ AND ALL PCRS WILL BE POSITIVE</td>
<td data-cell="B41"></td>
<td data-cell="C41"></td>
<td data-cell="G41"></td>
<td data-cell="H41"></td>
<td data-cell="I41"></td>
<td data-cell="J41"></td>
<td data-cell="K41"></td>
<td data-cell="L41"></td>
</tr>
<tr>
<th scope="row">42</th>
<td data-cell="A42"></td>
<td data-cell="B42"></td>
<td data-cell="C42"></td>
<td data-cell="G42"></td>
<td data-cell="H42"></td>
<td data-cell="I42"></td>
<td data-cell="J42"></td>
<td data-cell="K42"></td>
<td data-cell="L42"></td>
</tr>
<tr>
<th scope="row">43</th>
<td data-cell="A43">Tm1c</td>
<td data-cell="B43"></td>
<td data-cell="C43"></td>
<td data-cell="G43"></td>
<td data-cell="H43"></td>
<td data-cell="I43"></td>
<td data-cell="J43"></td>
<td data-cell="K43"></td>
<td data-cell="L43"></td>
</tr>
<tr>
<th scope="row">44</th>
<td data-cell="A44"></td>
<td data-cell="B44">x1</td>
<td data-cell="C44" data-reaction-cell="true">20</td>
<td data-cell="G44"></td>
<td data-cell="H44">Folder</td>
<td data-cell="I44">PCR name</td>
<td data-cell="J44">PCR cycle</td>
<td data-cell="K44">Primer Squence</td>
<td data-cell="L44">Band Size</td>
</tr>
<tr>
<th scope="row">45</th>
<td data-cell="A45">10x NEB buffer</td>
<td data-cell="B45">2</td>
<td data-cell="C45" data-formula="=B45*C44" title="=B45*C44">40</td>
<td data-cell="G45"></td>
<td data-cell="H45">Kyla</td>
<td data-cell="I45">E2-2 GEN</td>
<td data-cell="J45">1. Incubate at 94°C for 5:00</td>
<td data-cell="K45">Tm1c_F-AAGGCGCATAACGATACCAC</td>
<td data-cell="L45">218bp</td>
</tr>
<tr>
<th scope="row">46</th>
<td data-cell="A46">MgCl2</td>
<td data-cell="B46">0.6</td>
<td data-cell="C46" data-formula="=B46*C44" title="=B46*C44">12</td>
<td data-cell="G46"></td>
<td data-cell="H46"></td>
<td data-cell="I46"></td>
<td data-cell="J46">2. Incubate at 94°C for 0:30</td>
<td data-cell="K46">Tm1c_R-CCGCCTACTGCGACTATAGAGA</td>
<td data-cell="L46"></td>
</tr>
<tr>
<th scope="row">47</th>
<td data-cell="A47">DNTP</td>
<td data-cell="B47">0.2</td>
<td data-cell="C47" data-formula="=B47*C44" title="=B47*C44">4</td>
<td data-cell="G47"></td>
<td data-cell="H47"></td>
<td data-cell="I47"></td>
<td data-cell="J47">3. Incubate at 58°C for 0:30</td>
<td data-cell="K47"></td>
<td data-cell="L47"></td>
</tr>
<tr>
<th scope="row">48</th>
<td data-cell="A48">P1</td>
<td data-cell="B48">0.4</td>
<td data-cell="C48" data-formula="=B48*C44" title="=B48*C44">8</td>
<td data-cell="G48"></td>
<td data-cell="H48"></td>
<td data-cell="I48"></td>
<td data-cell="J48">4. Incubate at 72°C for 0:45</td>
<td data-cell="K48"></td>
<td data-cell="L48"></td>
</tr>
<tr>
<th scope="row">49</th>
<td data-cell="A49">P2</td>
<td data-cell="B49">0.4</td>
<td data-cell="C49" data-formula="=B49*C44" title="=B49*C44">8</td>
<td data-cell="G49"></td>
<td data-cell="H49"></td>
<td data-cell="I49"></td>
<td data-cell="J49">5. Cycle to step 2, 35 times</td>
<td data-cell="K49"></td>
<td data-cell="L49"></td>
</tr>
<tr>
<th scope="row">50</th>
<td data-cell="A50">Taq</td>
<td data-cell="B50">0.2</td>
<td data-cell="C50" data-formula="=B50*C44" title="=B50*C44">4</td>
<td data-cell="G50"></td>
<td data-cell="H50"></td>
<td data-cell="I50"></td>
<td data-cell="J50">6. Incubate at 72°C for 5:00</td>
<td data-cell="K50"></td>
<td data-cell="L50"></td>
</tr>
<tr>
<th scope="row">51</th>
<td data-cell="A51">H20</td>
<td data-cell="B51">15.2</td>
<td data-cell="C51" data-formula="=B51*C44" title="=B51*C44">304</td>
<td data-cell="G51"></td>
<td data-cell="H51"></td>
<td data-cell="I51"></td>
<td data-cell="J51"></td>
<td data-cell="K51"></td>
<td data-cell="L51"></td>
</tr>
<tr>
<th scope="row">52</th>
<td data-cell="A52">DNA</td>
<td data-cell="B52">1</td>
<td data-cell="C52" data-formula="=B52*C44" title="=B52*C44">20</td>
<td data-cell="G52"></td>
<td data-cell="H52"></td>
<td data-cell="I52"></td>
<td data-cell="J52"></td>
<td data-cell="K52"></td>
<td data-cell="L52"></td>
</tr>
<tr>
<th scope="row">53</th>
<td data-cell="A53">Total</td>
<td data-cell="B53">20</td>
<td data-cell="C53" data-formula="=B53*C44" title="=B53*C44">400</td>
<td data-cell="G53"></td>
<td data-cell="H53"></td>
<td data-cell="I53"></td>
<td data-cell="J53"></td>
<td data-cell="K53"></td>
<td data-cell="L53"></td>
</tr>
<tr>
<th scope="row">54</th>
<td data-cell="A54"></td>
<td data-cell="B54">25</td>
<td data-cell="C54" data-formula="=B54*C44" title="=B54*C44">500</td>
<td data-cell="G54"></td>
<td data-cell="H54"></td>
<td data-cell="I54"></td>
<td data-cell="J54"></td>
<td data-cell="K54"></td>
<td data-cell="L54"></td>
</tr>
<tr>
<th scope="row">55</th>
<td data-cell="A55"></td>
<td data-cell="B55"></td>
<td data-cell="C55"></td>
<td data-cell="G55"></td>
<td data-cell="H55"></td>
<td data-cell="I55"></td>
<td data-cell="J55"></td>
<td data-cell="K55"></td>
<td data-cell="L55"></td>
</tr>
<tr>
<th scope="row">56</th>
<td data-cell="A56"></td>
<td data-cell="B56"></td>
<td data-cell="C56"></td>
<td data-cell="G56"></td>
<td data-cell="H56"></td>
<td data-cell="I56"></td>
<td data-cell="J56"></td>
<td data-cell="K56"></td>
<td data-cell="L56"></td>
</tr>
<tr>
<th scope="row">57</th>
<td data-cell="A57">FRT</td>
<td data-cell="B57"></td>
<td data-cell="C57"></td>
<td data-cell="G57"></td>
<td data-cell="H57"></td>
<td data-cell="I57"></td>
<td data-cell="J57"></td>
<td data-cell="K57"></td>
<td data-cell="L57"></td>
</tr>
<tr>
<th scope="row">58</th>
<td data-cell="A58"></td>
<td data-cell="B58">x1</td>
<td data-cell="C58" data-reaction-cell="true">20</td>
<td data-cell="G58"></td>
<td data-cell="H58">Folder</td>
<td data-cell="I58">PCR name</td>
<td data-cell="J58">PCR cycle</td>
<td data-cell="K58">Primer Squence</td>
<td data-cell="L58">Band Size</td>
</tr>
<tr>
<th scope="row">59</th>
<td data-cell="A59">10x NEB buffer</td>
<td data-cell="B59">2</td>
<td data-cell="C59" data-formula="=B59*C58" title="=B59*C58">40</td>
<td data-cell="G59"></td>
<td data-cell="H59">Kyla</td>
<td data-cell="I59">E2-2 GEN</td>
<td data-cell="J59">1. Incubate at 94°C for 5:00</td>
<td data-cell="K59">5FRT_F-AGGCGCATAACGATACCACGAT</td>
<td data-cell="L59">204bp</td>
</tr>
<tr>
<th scope="row">60</th>
<td data-cell="A60">MgCl2</td>
<td data-cell="B60">0.6</td>
<td data-cell="C60" data-formula="=B60*C58" title="=B60*C58">12</td>
<td data-cell="G60"></td>
<td data-cell="H60"></td>
<td data-cell="I60"></td>
<td data-cell="J60">2. Incubate at 94°C for 0:30</td>
<td data-cell="K60">5FRT_R-CCACAACGGGTTCTTCTGTT</td>
<td data-cell="L60"></td>
</tr>
<tr>
<th scope="row">61</th>
<td data-cell="A61">DNTP</td>
<td data-cell="B61">0.2</td>
<td data-cell="C61" data-formula="=B61*C58" title="=B61*C58">4</td>
<td data-cell="G61"></td>
<td data-cell="H61"></td>
<td data-cell="I61"></td>
<td data-cell="J61">3. Incubate at 58°C for 0:30</td>
<td data-cell="K61"></td>
<td data-cell="L61"></td>
</tr>
<tr>
<th scope="row">62</th>
<td data-cell="A62">P1</td>
<td data-cell="B62">0.4</td>
<td data-cell="C62" data-formula="=B62*C58" title="=B62*C58">8</td>
<td data-cell="G62"></td>
<td data-cell="H62"></td>
<td data-cell="I62"></td>
<td data-cell="J62">4. Incubate at 72°C for 0:45</td>
<td data-cell="K62"></td>
<td data-cell="L62"></td>
</tr>
<tr>
<th scope="row">63</th>
<td data-cell="A63">P2</td>
<td data-cell="B63">0.4</td>
<td data-cell="C63" data-formula="=B63*C58" title="=B63*C58">8</td>
<td data-cell="G63"></td>
<td data-cell="H63"></td>
<td data-cell="I63"></td>
<td data-cell="J63">5. Cycle to step 2, 35 times</td>
<td data-cell="K63"></td>
<td data-cell="L63"></td>
</tr>
<tr>
<th scope="row">64</th>
<td data-cell="A64">Taq</td>
<td data-cell="B64">0.2</td>
<td data-cell="C64" data-formula="=B64*C58" title="=B64*C58">4</td>
<td data-cell="G64"></td>
<td data-cell="H64"></td>
<td data-cell="I64"></td>
<td data-cell="J64">6. Incubate at 72°C for 5:00</td>
<td data-cell="K64"></td>
<td data-cell="L64"></td>
</tr>
<tr>
<th scope="row">65</th>
<td data-cell="A65">H20</td>
<td data-cell="B65">15.2</td>
<td data-cell="C65" data-formula="=B65*C58" title="=B65*C58">304</td>
<td data-cell="G65"></td>
<td data-cell="H65"></td>
<td data-cell="I65"></td>
<td data-cell="J65"></td>
<td data-cell="K65"></td>
<td data-cell="L65"></td>
</tr>
<tr>
<th scope="row">66</th>
<td data-cell="A66">DNA</td>
<td data-cell="B66">1</td>
<td data-cell="C66" data-formula="=B66*C58" title="=B66*C58">20</td>
<td data-cell="G66"></td>
<td data-cell="H66"></td>
<td data-cell="I66"></td>
<td data-cell="J66"></td>
<td data-cell="K66"></td>
<td data-cell="L66"></td>
</tr>
<tr>
<th scope="row">67</th>
<td data-cell="A67">Total</td>
<td data-cell="B67">20</td>
<td data-cell="C67" data-formula="=B67*C58" title="=B67*C58">400</td>
<td data-cell="G67"></td>
<td data-cell="H67"></td>
<td data-cell="I67"></td>
<td data-cell="J67"></td>
<td data-cell="K67"></td>
<td data-cell="L67"></td>
</tr>
<tr>
<th scope="row">68</th>
<td data-cell="A68"></td>
<td data-cell="B68">25</td>
<td data-cell="C68" data-formula="=B68*C58" title="=B68*C58">500</td>
<td data-cell="G68"></td>
<td data-cell="H68"></td>
<td data-cell="I68"></td>
<td data-cell="J68"></td>
<td data-cell="K68"></td>
<td data-cell="L68"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="RagKO">
<summary><strong>RagKO</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-23" type="number" min="0" step="1" value="1" aria-label="Number of reactions for RagKO">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">Lid Control Mode: Constant at 100C</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2">Incubate at 94C for 2:00</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">Incubate at 94C for :30</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">Incubate at 58C for :45</td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">Incubate at 72C for :45</td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">Cycle to step 2 for 35 more times</td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">Incubate at 72 for 2:00</td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="USP1">
<summary><strong>USP1</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-24" type="number" min="0" step="1" value="20" aria-label="Number of reactions for USP1">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">USP1 1</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
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
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2">Kyla</td>
<td data-cell="I2">USP1 Gen</td>
<td data-cell="J2">1. Incubate at 94°C for 5:00</td>
<td data-cell="K2">common-LoxPF</td>
<td data-cell="L2">161bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:15</td>
<td data-cell="K3">USP1 intron3-4RA</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">1.7</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">34</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 65°C for 0:30</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 0:40</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">0.5</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">10</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 10 times (decrease 1°C/cycle)</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">0.5</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">10</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 94°C for 0:15</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.25</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">5</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8">7. Incubate at 55°C for 0:30</td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">15.6</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">312</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9">8. Incubate at 72°C for 0:40</td>
<td data-cell="K9"></td>
<td data-cell="L9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">DNA</td>
<td data-cell="B10">1</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10">9. Cycle to step 6, 30 times </td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">Total</td>
<td data-cell="B11">25</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">500</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11">10. Incubate at 72°C for 5:00</td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
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
<td data-cell="L12"></td>
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
<td data-cell="L13"></td>
</tr>
<tr>
<th scope="row">14</th>
<td data-cell="A14">USP1 2</td>
<td data-cell="B14"></td>
<td data-cell="C14"></td>
<td data-cell="G14"></td>
<td data-cell="H14"></td>
<td data-cell="I14"></td>
<td data-cell="J14"></td>
<td data-cell="K14"></td>
<td data-cell="L14"></td>
</tr>
<tr>
<th scope="row">15</th>
<td data-cell="A15"></td>
<td data-cell="B15">x1</td>
<td data-cell="C15" data-reaction-cell="true">20</td>
<td data-cell="G15"></td>
<td data-cell="H15">Folder</td>
<td data-cell="I15">PCR name</td>
<td data-cell="J15">PCR cycle</td>
<td data-cell="K15">Primer Squence</td>
<td data-cell="L15">Band Size</td>
</tr>
<tr>
<th scope="row">16</th>
<td data-cell="A16">5x buffer</td>
<td data-cell="B16">5</td>
<td data-cell="C16" data-formula="=B16*C15" title="=B16*C15">100</td>
<td data-cell="G16"></td>
<td data-cell="H16">Kyla</td>
<td data-cell="I16">USP1 Gen</td>
<td data-cell="J16">1. Incubate at 94°C for 5:00</td>
<td data-cell="K16">USP1intron2-3FA</td>
<td data-cell="L16">371bp</td>
</tr>
<tr>
<th scope="row">17</th>
<td data-cell="A17">MgCl2</td>
<td data-cell="B17">1.7</td>
<td data-cell="C17" data-formula="=B17*C15" title="=B17*C15">34</td>
<td data-cell="G17"></td>
<td data-cell="H17"></td>
<td data-cell="I17"></td>
<td data-cell="J17">2. Incubate at 94°C for 0:15</td>
<td data-cell="K17">commonen2R</td>
<td data-cell="L17"></td>
</tr>
<tr>
<th scope="row">18</th>
<td data-cell="A18">DNTP</td>
<td data-cell="B18">0.5</td>
<td data-cell="C18" data-formula="=B18*C15" title="=B18*C15">10</td>
<td data-cell="G18"></td>
<td data-cell="H18"></td>
<td data-cell="I18"></td>
<td data-cell="J18">3. Incubate at 65°C for 0:30</td>
<td data-cell="K18"></td>
<td data-cell="L18"></td>
</tr>
<tr>
<th scope="row">19</th>
<td data-cell="A19">P1</td>
<td data-cell="B19">0.5</td>
<td data-cell="C19" data-formula="=B19*C15" title="=B19*C15">10</td>
<td data-cell="G19"></td>
<td data-cell="H19"></td>
<td data-cell="I19"></td>
<td data-cell="J19">4. Incubate at 72°C for 0:40</td>
<td data-cell="K19"></td>
<td data-cell="L19"></td>
</tr>
<tr>
<th scope="row">20</th>
<td data-cell="A20">P2</td>
<td data-cell="B20">0.5</td>
<td data-cell="C20" data-formula="=B20*C15" title="=B20*C15">10</td>
<td data-cell="G20"></td>
<td data-cell="H20"></td>
<td data-cell="I20"></td>
<td data-cell="J20">5. Cycle to step 2, 10 times (decrease 1°C/cycle)</td>
<td data-cell="K20"></td>
<td data-cell="L20"></td>
</tr>
<tr>
<th scope="row">21</th>
<td data-cell="A21">Taq</td>
<td data-cell="B21">0.25</td>
<td data-cell="C21" data-formula="=B21*C15" title="=B21*C15">5</td>
<td data-cell="G21"></td>
<td data-cell="H21"></td>
<td data-cell="I21"></td>
<td data-cell="J21">6. Incubate at 94°C for 0:15</td>
<td data-cell="K21"></td>
<td data-cell="L21"></td>
</tr>
<tr>
<th scope="row">22</th>
<td data-cell="A22">H20</td>
<td data-cell="B22">15.6</td>
<td data-cell="C22" data-formula="=B22*C15" title="=B22*C15">312</td>
<td data-cell="G22"></td>
<td data-cell="H22"></td>
<td data-cell="I22"></td>
<td data-cell="J22">7. Incubate at 55°C for 0:30</td>
<td data-cell="K22"></td>
<td data-cell="L22"></td>
</tr>
<tr>
<th scope="row">23</th>
<td data-cell="A23">DNA</td>
<td data-cell="B23">1</td>
<td data-cell="C23" data-formula="=B23*C15" title="=B23*C15">20</td>
<td data-cell="G23"></td>
<td data-cell="H23"></td>
<td data-cell="I23"></td>
<td data-cell="J23">8. Incubate at 72°C for 0:40</td>
<td data-cell="K23"></td>
<td data-cell="L23"></td>
</tr>
<tr>
<th scope="row">24</th>
<td data-cell="A24">Total</td>
<td data-cell="B24">25</td>
<td data-cell="C24" data-formula="=B24*C15" title="=B24*C15">500</td>
<td data-cell="G24"></td>
<td data-cell="H24"></td>
<td data-cell="I24"></td>
<td data-cell="J24">9. Cycle to step 6, 30 times </td>
<td data-cell="K24"></td>
<td data-cell="L24"></td>
</tr>
<tr>
<th scope="row">25</th>
<td data-cell="A25"></td>
<td data-cell="B25"></td>
<td data-cell="C25"></td>
<td data-cell="G25"></td>
<td data-cell="H25"></td>
<td data-cell="I25"></td>
<td data-cell="J25">10. Incubate at 72°C for 5:00</td>
<td data-cell="K25"></td>
<td data-cell="L25"></td>
</tr>
<tr>
<th scope="row">26</th>
<td data-cell="A26"></td>
<td data-cell="B26"></td>
<td data-cell="C26"></td>
<td data-cell="G26"></td>
<td data-cell="H26"></td>
<td data-cell="I26"></td>
<td data-cell="J26"></td>
<td data-cell="K26"></td>
<td data-cell="L26"></td>
</tr>
<tr>
<th scope="row">27</th>
<td data-cell="A27"></td>
<td data-cell="B27"></td>
<td data-cell="C27"></td>
<td data-cell="G27"></td>
<td data-cell="H27"></td>
<td data-cell="I27"></td>
<td data-cell="J27"></td>
<td data-cell="K27"></td>
<td data-cell="L27"></td>
</tr>
<tr>
<th scope="row">28</th>
<td data-cell="A28">USP1 3</td>
<td data-cell="B28"></td>
<td data-cell="C28"></td>
<td data-cell="G28"></td>
<td data-cell="H28"></td>
<td data-cell="I28"></td>
<td data-cell="J28"></td>
<td data-cell="K28"></td>
<td data-cell="L28"></td>
</tr>
<tr>
<th scope="row">29</th>
<td data-cell="A29"></td>
<td data-cell="B29">x1</td>
<td data-cell="C29" data-reaction-cell="true">20</td>
<td data-cell="G29"></td>
<td data-cell="H29">Folder</td>
<td data-cell="I29">PCR name</td>
<td data-cell="J29">PCR cycle</td>
<td data-cell="K29">Primer Squence</td>
<td data-cell="L29">Band Size</td>
</tr>
<tr>
<th scope="row">30</th>
<td data-cell="A30">5x buffer</td>
<td data-cell="B30">5</td>
<td data-cell="C30" data-formula="=B30*C29" title="=B30*C29">100</td>
<td data-cell="G30"></td>
<td data-cell="H30">Kyla</td>
<td data-cell="I30">USP1 Gen</td>
<td data-cell="J30">1. Incubate at 94°C for 5:00</td>
<td data-cell="K30">common3'F</td>
<td data-cell="L30">944bp</td>
</tr>
<tr>
<th scope="row">31</th>
<td data-cell="A31">MgCl2</td>
<td data-cell="B31">1.7</td>
<td data-cell="C31" data-formula="=B31*C29" title="=B31*C29">34</td>
<td data-cell="G31"></td>
<td data-cell="H31"></td>
<td data-cell="I31"></td>
<td data-cell="J31">2. Incubate at 94°C for 0:15</td>
<td data-cell="K31">USP1intron3-4RA</td>
<td data-cell="L31"></td>
</tr>
<tr>
<th scope="row">32</th>
<td data-cell="A32">DNTP</td>
<td data-cell="B32">0.5</td>
<td data-cell="C32" data-formula="=B32*C29" title="=B32*C29">10</td>
<td data-cell="G32"></td>
<td data-cell="H32"></td>
<td data-cell="I32"></td>
<td data-cell="J32">3. Incubate at 65°C for 0:30</td>
<td data-cell="K32"></td>
<td data-cell="L32"></td>
</tr>
<tr>
<th scope="row">33</th>
<td data-cell="A33">P1</td>
<td data-cell="B33">0.5</td>
<td data-cell="C33" data-formula="=B33*C29" title="=B33*C29">10</td>
<td data-cell="G33"></td>
<td data-cell="H33"></td>
<td data-cell="I33"></td>
<td data-cell="J33">4. Incubate at 72°C for 0:40</td>
<td data-cell="K33"></td>
<td data-cell="L33"></td>
</tr>
<tr>
<th scope="row">34</th>
<td data-cell="A34">P2</td>
<td data-cell="B34">0.5</td>
<td data-cell="C34" data-formula="=B34*C29" title="=B34*C29">10</td>
<td data-cell="G34"></td>
<td data-cell="H34"></td>
<td data-cell="I34"></td>
<td data-cell="J34">5. Cycle to step 2, 10 times (decrease 1°C/cycle)</td>
<td data-cell="K34"></td>
<td data-cell="L34"></td>
</tr>
<tr>
<th scope="row">35</th>
<td data-cell="A35">Taq</td>
<td data-cell="B35">0.25</td>
<td data-cell="C35" data-formula="=B35*C29" title="=B35*C29">5</td>
<td data-cell="G35"></td>
<td data-cell="H35"></td>
<td data-cell="I35"></td>
<td data-cell="J35">6. Incubate at 94°C for 0:15</td>
<td data-cell="K35"></td>
<td data-cell="L35"></td>
</tr>
<tr>
<th scope="row">36</th>
<td data-cell="A36">H20</td>
<td data-cell="B36">15.6</td>
<td data-cell="C36" data-formula="=B36*C29" title="=B36*C29">312</td>
<td data-cell="G36"></td>
<td data-cell="H36"></td>
<td data-cell="I36"></td>
<td data-cell="J36">7. Incubate at 55°C for 0:30</td>
<td data-cell="K36"></td>
<td data-cell="L36"></td>
</tr>
<tr>
<th scope="row">37</th>
<td data-cell="A37">DNA</td>
<td data-cell="B37">1</td>
<td data-cell="C37" data-formula="=B37*C29" title="=B37*C29">20</td>
<td data-cell="G37"></td>
<td data-cell="H37"></td>
<td data-cell="I37"></td>
<td data-cell="J37">8. Incubate at 72°C for 0:40</td>
<td data-cell="K37"></td>
<td data-cell="L37"></td>
</tr>
<tr>
<th scope="row">38</th>
<td data-cell="A38">Total</td>
<td data-cell="B38">25</td>
<td data-cell="C38" data-formula="=B38*C29" title="=B38*C29">500</td>
<td data-cell="G38"></td>
<td data-cell="H38"></td>
<td data-cell="I38"></td>
<td data-cell="J38">9. Cycle to step 6, 30 times </td>
<td data-cell="K38"></td>
<td data-cell="L38"></td>
</tr>
<tr>
<th scope="row">39</th>
<td data-cell="A39"></td>
<td data-cell="B39"></td>
<td data-cell="C39"></td>
<td data-cell="G39"></td>
<td data-cell="H39"></td>
<td data-cell="I39"></td>
<td data-cell="J39"></td>
<td data-cell="K39"></td>
<td data-cell="L39"></td>
</tr>
<tr>
<th scope="row">40</th>
<td data-cell="A40"></td>
<td data-cell="B40"></td>
<td data-cell="C40"></td>
<td data-cell="G40"></td>
<td data-cell="H40"></td>
<td data-cell="I40"></td>
<td data-cell="J40">10. Incubate at 72°C for 5:00</td>
<td data-cell="K40"></td>
<td data-cell="L40"></td>
</tr>
<tr>
<th scope="row">41</th>
<td data-cell="A41"></td>
<td data-cell="B41"></td>
<td data-cell="C41"></td>
<td data-cell="G41"></td>
<td data-cell="H41"></td>
<td data-cell="I41"></td>
<td data-cell="J41"></td>
<td data-cell="K41"></td>
<td data-cell="L41"></td>
</tr>
<tr>
<th scope="row">42</th>
<td data-cell="A42">USP1 4</td>
<td data-cell="B42"></td>
<td data-cell="C42"></td>
<td data-cell="G42"></td>
<td data-cell="H42">Folder</td>
<td data-cell="I42">PCR name</td>
<td data-cell="J42">PCR cycle</td>
<td data-cell="K42">Primer Squence</td>
<td data-cell="L42">Band Size</td>
</tr>
<tr>
<th scope="row">43</th>
<td data-cell="A43"></td>
<td data-cell="B43">x1</td>
<td data-cell="C43" data-reaction-cell="true">20</td>
<td data-cell="G43"></td>
<td data-cell="H43">Kyla</td>
<td data-cell="I43">USP1 Gen</td>
<td data-cell="J43">1. Incubate at 94°C for 5:00</td>
<td data-cell="K43">USP1 intron2-3FA</td>
<td data-cell="L43">858bp</td>
</tr>
<tr>
<th scope="row">44</th>
<td data-cell="A44">5x buffer</td>
<td data-cell="B44">5</td>
<td data-cell="C44" data-formula="=B44*C43" title="=B44*C43">100</td>
<td data-cell="G44"></td>
<td data-cell="H44"></td>
<td data-cell="I44"></td>
<td data-cell="J44">2. Incubate at 94°C for 0:15</td>
<td data-cell="K44">USP1 intron3-4RA</td>
<td data-cell="L44"></td>
</tr>
<tr>
<th scope="row">45</th>
<td data-cell="A45">MgCl2</td>
<td data-cell="B45">1.7</td>
<td data-cell="C45" data-formula="=B45*C43" title="=B45*C43">34</td>
<td data-cell="G45"></td>
<td data-cell="H45"></td>
<td data-cell="I45"></td>
<td data-cell="J45">3. Incubate at 65°C for 0:30</td>
<td data-cell="K45"></td>
<td data-cell="L45"></td>
</tr>
<tr>
<th scope="row">46</th>
<td data-cell="A46">DNTP</td>
<td data-cell="B46">0.5</td>
<td data-cell="C46" data-formula="=B46*C43" title="=B46*C43">10</td>
<td data-cell="G46"></td>
<td data-cell="H46"></td>
<td data-cell="I46"></td>
<td data-cell="J46">4. Incubate at 72°C for 0:40</td>
<td data-cell="K46"></td>
<td data-cell="L46"></td>
</tr>
<tr>
<th scope="row">47</th>
<td data-cell="A47">P1</td>
<td data-cell="B47">0.5</td>
<td data-cell="C47" data-formula="=B47*C43" title="=B47*C43">10</td>
<td data-cell="G47"></td>
<td data-cell="H47"></td>
<td data-cell="I47"></td>
<td data-cell="J47">5. Cycle to step 2, 10 times (decrease 1°C/cycle)</td>
<td data-cell="K47"></td>
<td data-cell="L47"></td>
</tr>
<tr>
<th scope="row">48</th>
<td data-cell="A48">P2</td>
<td data-cell="B48">0.5</td>
<td data-cell="C48" data-formula="=B48*C43" title="=B48*C43">10</td>
<td data-cell="G48"></td>
<td data-cell="H48"></td>
<td data-cell="I48"></td>
<td data-cell="J48">6. Incubate at 94°C for 0:15</td>
<td data-cell="K48"></td>
<td data-cell="L48"></td>
</tr>
<tr>
<th scope="row">49</th>
<td data-cell="A49">Taq</td>
<td data-cell="B49">0.25</td>
<td data-cell="C49" data-formula="=B49*C43" title="=B49*C43">5</td>
<td data-cell="G49"></td>
<td data-cell="H49"></td>
<td data-cell="I49"></td>
<td data-cell="J49">7. Incubate at 55°C for 0:30</td>
<td data-cell="K49"></td>
<td data-cell="L49"></td>
</tr>
<tr>
<th scope="row">50</th>
<td data-cell="A50">H20</td>
<td data-cell="B50">15.6</td>
<td data-cell="C50" data-formula="=B50*C43" title="=B50*C43">312</td>
<td data-cell="G50"></td>
<td data-cell="H50"></td>
<td data-cell="I50"></td>
<td data-cell="J50">8. Incubate at 72°C for 0:40</td>
<td data-cell="K50"></td>
<td data-cell="L50"></td>
</tr>
<tr>
<th scope="row">51</th>
<td data-cell="A51">DNA</td>
<td data-cell="B51">1</td>
<td data-cell="C51" data-formula="=B51*C43" title="=B51*C43">20</td>
<td data-cell="G51"></td>
<td data-cell="H51"></td>
<td data-cell="I51"></td>
<td data-cell="J51">9. Cycle to step 6, 30 times </td>
<td data-cell="K51"></td>
<td data-cell="L51"></td>
</tr>
<tr>
<th scope="row">52</th>
<td data-cell="A52">Total</td>
<td data-cell="B52">25</td>
<td data-cell="C52" data-formula="=B52*C43" title="=B52*C43">500</td>
<td data-cell="G52"></td>
<td data-cell="H52"></td>
<td data-cell="I52"></td>
<td data-cell="J52">10. Incubate at 72°C for 5:00</td>
<td data-cell="K52"></td>
<td data-cell="L52"></td>
</tr>
<tr>
<th scope="row">53</th>
<td data-cell="A53"></td>
<td data-cell="B53"></td>
<td data-cell="C53"></td>
<td data-cell="G53"></td>
<td data-cell="H53"></td>
<td data-cell="I53"></td>
<td data-cell="J53"></td>
<td data-cell="K53">c</td>
<td data-cell="L53"></td>
</tr>
<tr>
<th scope="row">54</th>
<td data-cell="A54"></td>
<td data-cell="B54"></td>
<td data-cell="C54"></td>
<td data-cell="G54"></td>
<td data-cell="H54"></td>
<td data-cell="I54"></td>
<td data-cell="J54"></td>
<td data-cell="K54"></td>
<td data-cell="L54"></td>
</tr>
<tr>
<th scope="row">55</th>
<td data-cell="A55"> USE NEB TAQ AS OUR LAB STOCK IS CONTAMINATED WITH LACZ AND CAN GET FALSE POSITIVES</td>
<td data-cell="B55"></td>
<td data-cell="C55"></td>
<td data-cell="G55"></td>
<td data-cell="H55"></td>
<td data-cell="I55"></td>
<td data-cell="J55"></td>
<td data-cell="K55"></td>
<td data-cell="L55"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="ER cre">
<summary><strong>ER cre</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-25" type="number" min="0" step="1" value="20" aria-label="Number of reactions for ER cre">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">ER cre</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">20</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">4</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">80</td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">0.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">5</td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">0.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">5</td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P3</td>
<td data-cell="B8">0.25</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">5</td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.2</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">4</td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">16.05</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">321</td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">1</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">20</td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12" data-formula="=SUM(B3:B11)" title="=SUM(B3:B11)">25</td>
<td data-cell="C12" data-formula="=B12*C2" title="=B12*C2">500</td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="ER cre updated">
<summary><strong>ER cre updated</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-26" type="number" min="0" step="1" value="20" aria-label="Number of reactions for ER cre updated">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">ER-cre</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
<td data-cell="H1"></td>
<td data-cell="I1">PCR name</td>
<td data-cell="J1">PCR cycle</td>
<td data-cell="K1">Primer Squence</td>
<td data-cell="L1">Band Size</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2"></td>
<td data-cell="I2">ER cre</td>
<td data-cell="J2">1. Incubate at 95°C for 3:00</td>
<td data-cell="K2">ER1 - CAC ACC AGG TTA GCC TTT AAG CC</td>
<td data-cell="L2"></td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 95°C for 0:30</td>
<td data-cell="K3">ER2 - AAA GTC GCT CTG AGT TGT TAT</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2.5</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">50</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 58°C for 0:30</td>
<td data-cell="K4">ER3 CCT GAA CAT GTC CAT CAG CTT</td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 0:45</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">1.25</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">25</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 30 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">1.25</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">25</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 5:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">P3</td>
<td data-cell="B8">1.25</td>
<td data-cell="C8" data-formula="=B8*C3" title="=B8*C3">125</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8">7. Incubate at 4°C </td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">Taq</td>
<td data-cell="B9">0.5</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">10</td>
<td data-cell="G9"></td>
<td data-cell="H9"></td>
<td data-cell="I9"></td>
<td data-cell="J9"></td>
<td data-cell="K9"></td>
<td data-cell="L9"></td>
</tr>
<tr>
<th scope="row">10</th>
<td data-cell="A10">H20</td>
<td data-cell="B10">11.75</td>
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">235</td>
<td data-cell="G10"></td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10"></td>
<td data-cell="K10"></td>
<td data-cell="L10"></td>
</tr>
<tr>
<th scope="row">11</th>
<td data-cell="A11">DNA</td>
<td data-cell="B11">1</td>
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">20</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
</tr>
<tr>
<th scope="row">12</th>
<td data-cell="A12">Total</td>
<td data-cell="B12">25</td>
<td data-cell="C12" data-formula="=B12*C2" title="=B12*C2">500</td>
<td data-cell="G12"></td>
<td data-cell="H12"></td>
<td data-cell="I12"></td>
<td data-cell="J12"></td>
<td data-cell="K12"></td>
<td data-cell="L12"></td>
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
<td data-cell="L13"></td>
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
<td data-cell="L14"></td>
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
<td data-cell="L15"></td>
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
<td data-cell="L16"></td>
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
<td data-cell="L17"></td>
</tr>
<tr>
<th scope="row">18</th>
<td data-cell="A18"></td>
<td data-cell="B18"></td>
<td data-cell="C18"></td>
<td data-cell="G18"></td>
<td data-cell="H18"></td>
<td data-cell="I18"></td>
<td data-cell="J18"></td>
<td data-cell="K18"></td>
<td data-cell="L18"></td>
</tr>
<tr>
<th scope="row">19</th>
<td data-cell="A19"></td>
<td data-cell="B19"></td>
<td data-cell="C19"></td>
<td data-cell="G19"></td>
<td data-cell="H19"></td>
<td data-cell="I19"></td>
<td data-cell="J19"></td>
<td data-cell="K19"></td>
<td data-cell="L19"></td>
</tr>
<tr>
<th scope="row">20</th>
<td data-cell="A20"></td>
<td data-cell="B20"></td>
<td data-cell="C20"></td>
<td data-cell="G20"></td>
<td data-cell="H20"></td>
<td data-cell="I20"></td>
<td data-cell="J20"></td>
<td data-cell="K20"></td>
<td data-cell="L20"></td>
</tr>
<tr>
<th scope="row">21</th>
<td data-cell="A21"></td>
<td data-cell="B21"></td>
<td data-cell="C21"></td>
<td data-cell="G21"></td>
<td data-cell="H21"></td>
<td data-cell="I21"></td>
<td data-cell="J21"></td>
<td data-cell="K21"></td>
<td data-cell="L21"></td>
</tr>
<tr>
<th scope="row">22</th>
<td data-cell="A22"></td>
<td data-cell="B22"></td>
<td data-cell="C22"></td>
<td data-cell="G22"></td>
<td data-cell="H22"></td>
<td data-cell="I22"></td>
<td data-cell="J22"></td>
<td data-cell="K22"></td>
<td data-cell="L22"></td>
</tr>
<tr>
<th scope="row">23</th>
<td data-cell="A23"></td>
<td data-cell="B23"></td>
<td data-cell="C23"></td>
<td data-cell="G23"></td>
<td data-cell="H23"></td>
<td data-cell="I23"></td>
<td data-cell="J23"></td>
<td data-cell="K23"></td>
<td data-cell="L23"></td>
</tr>
<tr>
<th scope="row">24</th>
<td data-cell="A24"></td>
<td data-cell="B24"></td>
<td data-cell="C24"></td>
<td data-cell="G24"></td>
<td data-cell="H24"></td>
<td data-cell="I24"></td>
<td data-cell="J24"></td>
<td data-cell="K24"></td>
<td data-cell="L24"></td>
</tr>
<tr>
<th scope="row">25</th>
<td data-cell="A25"></td>
<td data-cell="B25"></td>
<td data-cell="C25"></td>
<td data-cell="G25"></td>
<td data-cell="H25"></td>
<td data-cell="I25"></td>
<td data-cell="J25"></td>
<td data-cell="K25"></td>
<td data-cell="L25"></td>
</tr>
<tr>
<th scope="row">26</th>
<td data-cell="A26"></td>
<td data-cell="B26"></td>
<td data-cell="C26"></td>
<td data-cell="G26"></td>
<td data-cell="H26"></td>
<td data-cell="I26"></td>
<td data-cell="J26"></td>
<td data-cell="K26"></td>
<td data-cell="L26"></td>
</tr>
<tr>
<th scope="row">27</th>
<td data-cell="A27"></td>
<td data-cell="B27"></td>
<td data-cell="C27"></td>
<td data-cell="G27"></td>
<td data-cell="H27"></td>
<td data-cell="I27"></td>
<td data-cell="J27"></td>
<td data-cell="K27"></td>
<td data-cell="L27"></td>
</tr>
<tr>
<th scope="row">28</th>
<td data-cell="A28"></td>
<td data-cell="B28"></td>
<td data-cell="C28"></td>
<td data-cell="G28"></td>
<td data-cell="H28"></td>
<td data-cell="I28"></td>
<td data-cell="J28"></td>
<td data-cell="K28"></td>
<td data-cell="L28"></td>
</tr>
<tr>
<th scope="row">29</th>
<td data-cell="A29"></td>
<td data-cell="B29"></td>
<td data-cell="C29"></td>
<td data-cell="G29"></td>
<td data-cell="H29"></td>
<td data-cell="I29"></td>
<td data-cell="J29"></td>
<td data-cell="K29"></td>
<td data-cell="L29"></td>
</tr>
<tr>
<th scope="row">30</th>
<td data-cell="A30"></td>
<td data-cell="B30"></td>
<td data-cell="C30"></td>
<td data-cell="G30"></td>
<td data-cell="H30"></td>
<td data-cell="I30"></td>
<td data-cell="J30"></td>
<td data-cell="K30"></td>
<td data-cell="L30"></td>
</tr>
<tr>
<th scope="row">31</th>
<td data-cell="A31"></td>
<td data-cell="B31"></td>
<td data-cell="C31"></td>
<td data-cell="G31"></td>
<td data-cell="H31"></td>
<td data-cell="I31"></td>
<td data-cell="J31"></td>
<td data-cell="K31"></td>
<td data-cell="L31"></td>
</tr>
<tr>
<th scope="row">32</th>
<td data-cell="A32"></td>
<td data-cell="B32"></td>
<td data-cell="C32"></td>
<td data-cell="G32"></td>
<td data-cell="H32"></td>
<td data-cell="I32"></td>
<td data-cell="J32"></td>
<td data-cell="K32"></td>
<td data-cell="L32"></td>
</tr>
<tr>
<th scope="row">33</th>
<td data-cell="A33"></td>
<td data-cell="B33"></td>
<td data-cell="C33"></td>
<td data-cell="G33"></td>
<td data-cell="H33"></td>
<td data-cell="I33"></td>
<td data-cell="J33"></td>
<td data-cell="K33"></td>
<td data-cell="L33"></td>
</tr>
<tr>
<th scope="row">34</th>
<td data-cell="A34"></td>
<td data-cell="B34"></td>
<td data-cell="C34"></td>
<td data-cell="G34"></td>
<td data-cell="H34"></td>
<td data-cell="I34"></td>
<td data-cell="J34"></td>
<td data-cell="K34"></td>
<td data-cell="L34"></td>
</tr>
<tr>
<th scope="row">35</th>
<td data-cell="A35"></td>
<td data-cell="B35"></td>
<td data-cell="C35"></td>
<td data-cell="G35"></td>
<td data-cell="H35"></td>
<td data-cell="I35"></td>
<td data-cell="J35"></td>
<td data-cell="K35"></td>
<td data-cell="L35"></td>
</tr>
<tr>
<th scope="row">36</th>
<td data-cell="A36"></td>
<td data-cell="B36"></td>
<td data-cell="C36"></td>
<td data-cell="G36"></td>
<td data-cell="H36"></td>
<td data-cell="I36"></td>
<td data-cell="J36"></td>
<td data-cell="K36"></td>
<td data-cell="L36"></td>
</tr>
<tr>
<th scope="row">37</th>
<td data-cell="A37"></td>
<td data-cell="B37"></td>
<td data-cell="C37"></td>
<td data-cell="G37"></td>
<td data-cell="H37"></td>
<td data-cell="I37"></td>
<td data-cell="J37"></td>
<td data-cell="K37"></td>
<td data-cell="L37"></td>
</tr>
<tr>
<th scope="row">38</th>
<td data-cell="A38"></td>
<td data-cell="B38"></td>
<td data-cell="C38"></td>
<td data-cell="G38"></td>
<td data-cell="H38"></td>
<td data-cell="I38"></td>
<td data-cell="J38"></td>
<td data-cell="K38"></td>
<td data-cell="L38"></td>
</tr>
<tr>
<th scope="row">39</th>
<td data-cell="A39"></td>
<td data-cell="B39"></td>
<td data-cell="C39"></td>
<td data-cell="G39"></td>
<td data-cell="H39"></td>
<td data-cell="I39"></td>
<td data-cell="J39"></td>
<td data-cell="K39"></td>
<td data-cell="L39"></td>
</tr>
<tr>
<th scope="row">40</th>
<td data-cell="A40"></td>
<td data-cell="B40"></td>
<td data-cell="C40"></td>
<td data-cell="G40"></td>
<td data-cell="H40"></td>
<td data-cell="I40"></td>
<td data-cell="J40"></td>
<td data-cell="K40"></td>
<td data-cell="L40"></td>
</tr>
<tr>
<th scope="row">41</th>
<td data-cell="A41"></td>
<td data-cell="B41"></td>
<td data-cell="C41"></td>
<td data-cell="G41"></td>
<td data-cell="H41"></td>
<td data-cell="I41"></td>
<td data-cell="J41"></td>
<td data-cell="K41"></td>
<td data-cell="L41"></td>
</tr>
<tr>
<th scope="row">42</th>
<td data-cell="A42"></td>
<td data-cell="B42"></td>
<td data-cell="C42"></td>
<td data-cell="G42"></td>
<td data-cell="H42"></td>
<td data-cell="I42"></td>
<td data-cell="J42"></td>
<td data-cell="K42"></td>
<td data-cell="L42"></td>
</tr>
<tr>
<th scope="row">43</th>
<td data-cell="A43"></td>
<td data-cell="B43"></td>
<td data-cell="C43"></td>
<td data-cell="G43"></td>
<td data-cell="H43"></td>
<td data-cell="I43"></td>
<td data-cell="J43"></td>
<td data-cell="K43"></td>
<td data-cell="L43"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<details class="pcr-sheet" data-sheet="ID2KOID3KI">
<summary><strong>ID2KOID3KI</strong></summary>

<div class="pcr-sheet-controls">
<label>Enter number of reactions in the box.
 <input class="pcr-reaction-input" id="pcr-sheet-27" type="number" min="0" step="1" value="20" aria-label="Number of reactions for ID2KOID3KI">
</label>
</div>

<div class="pcr-table-wrap">
<table class="pcr-table">
<thead><tr>
<th scope="col">Row</th>
<th scope="col">A</th>
<th scope="col">B</th>
<th scope="col">C</th>
<th scope="col">G</th>
<th scope="col">H</th>
<th scope="col">I</th>
<th scope="col">J</th>
<th scope="col">K</th>
<th scope="col">L</th>
</tr></thead>
<tbody>
<tr>
<th scope="row">1</th>
<td data-cell="A1">WT</td>
<td data-cell="B1"></td>
<td data-cell="C1"></td>
<td data-cell="G1"></td>
<td data-cell="H1"></td>
<td data-cell="I1">PCR name</td>
<td data-cell="J1">PCR cycle</td>
<td data-cell="K1">Primer Squence</td>
<td data-cell="L1">Band Size</td>
</tr>
<tr>
<th scope="row">2</th>
<td data-cell="A2"></td>
<td data-cell="B2">x1</td>
<td data-cell="C2" data-reaction-cell="true">20</td>
<td data-cell="G2"></td>
<td data-cell="H2"></td>
<td data-cell="I2">52</td>
<td data-cell="J2">1. Incubate at 94°C for 3:00</td>
<td data-cell="K2">Id2/3_Geno_WT_F_2 - CCT TTT ATC CTC TTT CTC CCC AGG</td>
<td data-cell="L2">~620BP</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="=B3*C2">100</td>
<td data-cell="G3"></td>
<td data-cell="H3"></td>
<td data-cell="I3"></td>
<td data-cell="J3">2. Incubate at 94°C for 0:30</td>
<td data-cell="K3">id2/3_Geno_R_2 - TAA GGC TCG GGG TAG CC</td>
<td data-cell="L3"></td>
</tr>
<tr>
<th scope="row">4</th>
<td data-cell="A4">MgCl2</td>
<td data-cell="B4">2</td>
<td data-cell="C4" data-formula="=B4*C2" title="=B4*C2">40</td>
<td data-cell="G4"></td>
<td data-cell="H4"></td>
<td data-cell="I4"></td>
<td data-cell="J4">3. Incubate at 52°C for 0:30</td>
<td data-cell="K4"></td>
<td data-cell="L4"></td>
</tr>
<tr>
<th scope="row">5</th>
<td data-cell="A5">DNTP</td>
<td data-cell="B5">0.5</td>
<td data-cell="C5" data-formula="=B5*C2" title="=B5*C2">10</td>
<td data-cell="G5"></td>
<td data-cell="H5"></td>
<td data-cell="I5"></td>
<td data-cell="J5">4. Incubate at 72°C for 1:00</td>
<td data-cell="K5"></td>
<td data-cell="L5"></td>
</tr>
<tr>
<th scope="row">6</th>
<td data-cell="A6">P1</td>
<td data-cell="B6">0.5</td>
<td data-cell="C6" data-formula="=B6*C2" title="=B6*C2">10</td>
<td data-cell="G6"></td>
<td data-cell="H6"></td>
<td data-cell="I6"></td>
<td data-cell="J6">5. Cycle to step 2, 38 times</td>
<td data-cell="K6"></td>
<td data-cell="L6"></td>
</tr>
<tr>
<th scope="row">7</th>
<td data-cell="A7">P2</td>
<td data-cell="B7">0.5</td>
<td data-cell="C7" data-formula="=B7*C2" title="=B7*C2">10</td>
<td data-cell="G7"></td>
<td data-cell="H7"></td>
<td data-cell="I7"></td>
<td data-cell="J7">6. Incubate at 72°C for 5:00</td>
<td data-cell="K7"></td>
<td data-cell="L7"></td>
</tr>
<tr>
<th scope="row">8</th>
<td data-cell="A8">Taq</td>
<td data-cell="B8">0.5</td>
<td data-cell="C8" data-formula="=B8*C2" title="=B8*C2">10</td>
<td data-cell="G8"></td>
<td data-cell="H8"></td>
<td data-cell="I8"></td>
<td data-cell="J8">7. Incubate at 12°C </td>
<td data-cell="K8"></td>
<td data-cell="L8"></td>
</tr>
<tr>
<th scope="row">9</th>
<td data-cell="A9">H20</td>
<td data-cell="B9">15</td>
<td data-cell="C9" data-formula="=B9*C2" title="=B9*C2">300</td>
<td data-cell="G9"></td>
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
<td data-cell="C10" data-formula="=B10*C2" title="=B10*C2">20</td>
<td data-cell="G10"></td>
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
<td data-cell="C11" data-formula="=B11*C2" title="=B11*C2">500</td>
<td data-cell="G11"></td>
<td data-cell="H11"></td>
<td data-cell="I11"></td>
<td data-cell="J11"></td>
<td data-cell="K11"></td>
<td data-cell="L11"></td>
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
<td data-cell="L12"></td>
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
<td data-cell="L13"></td>
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
<td data-cell="L14"></td>
</tr>
<tr>
<th scope="row">15</th>
<td data-cell="A15">KI</td>
<td data-cell="B15"></td>
<td data-cell="C15"></td>
<td data-cell="G15"></td>
<td data-cell="H15"></td>
<td data-cell="I15">PCR name</td>
<td data-cell="J15">PCR cycle</td>
<td data-cell="K15">Primer Squence</td>
<td data-cell="L15">Band Size</td>
</tr>
<tr>
<th scope="row">16</th>
<td data-cell="A16"></td>
<td data-cell="B16">x1</td>
<td data-cell="C16" data-reaction-cell="true">20</td>
<td data-cell="G16"></td>
<td data-cell="H16"></td>
<td data-cell="I16">52</td>
<td data-cell="J16">1. Incubate at 94°C for 3:00</td>
<td data-cell="K16">Id2KI_CRE_F_3 - ACT TTA TAC GAA GTT ATA TGT GAA ATC GCT</td>
<td data-cell="L16">~490BP</td>
</tr>
<tr>
<th scope="row">17</th>
<td data-cell="A17">5x buffer</td>
<td data-cell="B17">5</td>
<td data-cell="C17" data-formula="=B17*C16" title="=B17*C16">100</td>
<td data-cell="G17"></td>
<td data-cell="H17"></td>
<td data-cell="I17"></td>
<td data-cell="J17">2. Incubate at 94°C for 0:30</td>
<td data-cell="K17">Id2KI_CRE_R_3- TAA GGC TCG GGG TAG CC</td>
<td data-cell="L17"></td>
</tr>
<tr>
<th scope="row">18</th>
<td data-cell="A18">MgCl2</td>
<td data-cell="B18">2</td>
<td data-cell="C18" data-formula="=B18*C16" title="=B18*C16">40</td>
<td data-cell="G18"></td>
<td data-cell="H18"></td>
<td data-cell="I18"></td>
<td data-cell="J18">3. Incubate at 52°C for 0:30</td>
<td data-cell="K18"></td>
<td data-cell="L18"></td>
</tr>
<tr>
<th scope="row">19</th>
<td data-cell="A19">DNTP</td>
<td data-cell="B19">0.5</td>
<td data-cell="C19" data-formula="=B19*C16" title="=B19*C16">10</td>
<td data-cell="G19"></td>
<td data-cell="H19"></td>
<td data-cell="I19"></td>
<td data-cell="J19">4. Incubate at 72°C for 1:00</td>
<td data-cell="K19"></td>
<td data-cell="L19"></td>
</tr>
<tr>
<th scope="row">20</th>
<td data-cell="A20">P1</td>
<td data-cell="B20">0.5</td>
<td data-cell="C20" data-formula="=B20*C16" title="=B20*C16">10</td>
<td data-cell="G20"></td>
<td data-cell="H20"></td>
<td data-cell="I20"></td>
<td data-cell="J20">5. Cycle to step 2, 38 times</td>
<td data-cell="K20"></td>
<td data-cell="L20"></td>
</tr>
<tr>
<th scope="row">21</th>
<td data-cell="A21">P2</td>
<td data-cell="B21">0.5</td>
<td data-cell="C21" data-formula="=B21*C16" title="=B21*C16">10</td>
<td data-cell="G21"></td>
<td data-cell="H21"></td>
<td data-cell="I21"></td>
<td data-cell="J21">6. Incubate at 72°C for 5:00</td>
<td data-cell="K21"></td>
<td data-cell="L21"></td>
</tr>
<tr>
<th scope="row">22</th>
<td data-cell="A22">Taq</td>
<td data-cell="B22">0.5</td>
<td data-cell="C22" data-formula="=B22*C16" title="=B22*C16">10</td>
<td data-cell="G22"></td>
<td data-cell="H22"></td>
<td data-cell="I22"></td>
<td data-cell="J22">7. Incubate at 12°C </td>
<td data-cell="K22"></td>
<td data-cell="L22"></td>
</tr>
<tr>
<th scope="row">23</th>
<td data-cell="A23">H20</td>
<td data-cell="B23">15</td>
<td data-cell="C23" data-formula="=B23*C16" title="=B23*C16">300</td>
<td data-cell="G23"></td>
<td data-cell="H23"></td>
<td data-cell="I23"></td>
<td data-cell="J23"></td>
<td data-cell="K23"></td>
<td data-cell="L23"></td>
</tr>
<tr>
<th scope="row">24</th>
<td data-cell="A24">DNA</td>
<td data-cell="B24">1</td>
<td data-cell="C24" data-formula="=B24*C16" title="=B24*C16">20</td>
<td data-cell="G24"></td>
<td data-cell="H24"></td>
<td data-cell="I24"></td>
<td data-cell="J24"></td>
<td data-cell="K24"></td>
<td data-cell="L24"></td>
</tr>
<tr>
<th scope="row">25</th>
<td data-cell="A25">Total</td>
<td data-cell="B25">25</td>
<td data-cell="C25" data-formula="=B25*C16" title="=B25*C16">500</td>
<td data-cell="G25"></td>
<td data-cell="H25"></td>
<td data-cell="I25"></td>
<td data-cell="J25"></td>
<td data-cell="K25"></td>
<td data-cell="L25"></td>
</tr>
<tr>
<th scope="row">26</th>
<td data-cell="A26"></td>
<td data-cell="B26"></td>
<td data-cell="C26"></td>
<td data-cell="G26"></td>
<td data-cell="H26"></td>
<td data-cell="I26"></td>
<td data-cell="J26"></td>
<td data-cell="K26"></td>
<td data-cell="L26"></td>
</tr>
<tr>
<th scope="row">27</th>
<td data-cell="A27"></td>
<td data-cell="B27"></td>
<td data-cell="C27"></td>
<td data-cell="G27"></td>
<td data-cell="H27"></td>
<td data-cell="I27"></td>
<td data-cell="J27"></td>
<td data-cell="K27"></td>
<td data-cell="L27"></td>
</tr>
<tr>
<th scope="row">28</th>
<td data-cell="A28"></td>
<td data-cell="B28"></td>
<td data-cell="C28"></td>
<td data-cell="G28"></td>
<td data-cell="H28"></td>
<td data-cell="I28"></td>
<td data-cell="J28"></td>
<td data-cell="K28"></td>
<td data-cell="L28"></td>
</tr>
<tr>
<th scope="row">29</th>
<td data-cell="A29"></td>
<td data-cell="B29"></td>
<td data-cell="C29"></td>
<td data-cell="G29"></td>
<td data-cell="H29"></td>
<td data-cell="I29"></td>
<td data-cell="J29"></td>
<td data-cell="K29"></td>
<td data-cell="L29"></td>
</tr>
<tr>
<th scope="row">30</th>
<td data-cell="A30"></td>
<td data-cell="B30"></td>
<td data-cell="C30"></td>
<td data-cell="G30"></td>
<td data-cell="H30"></td>
<td data-cell="I30"></td>
<td data-cell="J30"></td>
<td data-cell="K30"></td>
<td data-cell="L30"></td>
</tr>
<tr>
<th scope="row">31</th>
<td data-cell="A31"></td>
<td data-cell="B31"></td>
<td data-cell="C31"></td>
<td data-cell="G31"></td>
<td data-cell="H31"></td>
<td data-cell="I31"></td>
<td data-cell="J31"></td>
<td data-cell="K31"></td>
<td data-cell="L31"></td>
</tr>
<tr>
<th scope="row">32</th>
<td data-cell="A32"></td>
<td data-cell="B32"></td>
<td data-cell="C32"></td>
<td data-cell="G32"></td>
<td data-cell="H32"></td>
<td data-cell="I32"></td>
<td data-cell="J32"></td>
<td data-cell="K32"></td>
<td data-cell="L32"></td>
</tr>
<tr>
<th scope="row">33</th>
<td data-cell="A33"></td>
<td data-cell="B33"></td>
<td data-cell="C33"></td>
<td data-cell="G33"></td>
<td data-cell="H33"></td>
<td data-cell="I33"></td>
<td data-cell="J33"></td>
<td data-cell="K33"></td>
<td data-cell="L33"></td>
</tr>
<tr>
<th scope="row">34</th>
<td data-cell="A34"></td>
<td data-cell="B34"></td>
<td data-cell="C34"></td>
<td data-cell="G34"></td>
<td data-cell="H34"></td>
<td data-cell="I34"></td>
<td data-cell="J34"></td>
<td data-cell="K34"></td>
<td data-cell="L34"></td>
</tr>
<tr>
<th scope="row">35</th>
<td data-cell="A35"></td>
<td data-cell="B35"></td>
<td data-cell="C35"></td>
<td data-cell="G35"></td>
<td data-cell="H35"></td>
<td data-cell="I35"></td>
<td data-cell="J35"></td>
<td data-cell="K35"></td>
<td data-cell="L35"></td>
</tr>
<tr>
<th scope="row">36</th>
<td data-cell="A36"></td>
<td data-cell="B36"></td>
<td data-cell="C36"></td>
<td data-cell="G36"></td>
<td data-cell="H36"></td>
<td data-cell="I36"></td>
<td data-cell="J36"></td>
<td data-cell="K36"></td>
<td data-cell="L36"></td>
</tr>
<tr>
<th scope="row">37</th>
<td data-cell="A37"></td>
<td data-cell="B37"></td>
<td data-cell="C37"></td>
<td data-cell="G37"></td>
<td data-cell="H37"></td>
<td data-cell="I37"></td>
<td data-cell="J37"></td>
<td data-cell="K37"></td>
<td data-cell="L37"></td>
</tr>
<tr>
<th scope="row">38</th>
<td data-cell="A38"></td>
<td data-cell="B38"></td>
<td data-cell="C38"></td>
<td data-cell="G38"></td>
<td data-cell="H38"></td>
<td data-cell="I38"></td>
<td data-cell="J38"></td>
<td data-cell="K38"></td>
<td data-cell="L38"></td>
</tr>
<tr>
<th scope="row">39</th>
<td data-cell="A39"></td>
<td data-cell="B39"></td>
<td data-cell="C39"></td>
<td data-cell="G39"></td>
<td data-cell="H39"></td>
<td data-cell="I39"></td>
<td data-cell="J39"></td>
<td data-cell="K39"></td>
<td data-cell="L39"></td>
</tr>
<tr>
<th scope="row">40</th>
<td data-cell="A40"></td>
<td data-cell="B40"></td>
<td data-cell="C40"></td>
<td data-cell="G40"></td>
<td data-cell="H40"></td>
<td data-cell="I40"></td>
<td data-cell="J40"></td>
<td data-cell="K40"></td>
<td data-cell="L40"></td>
</tr>
<tr>
<th scope="row">41</th>
<td data-cell="A41"></td>
<td data-cell="B41"></td>
<td data-cell="C41"></td>
<td data-cell="G41"></td>
<td data-cell="H41"></td>
<td data-cell="I41"></td>
<td data-cell="J41"></td>
<td data-cell="K41"></td>
<td data-cell="L41"></td>
</tr>
<tr>
<th scope="row">42</th>
<td data-cell="A42"></td>
<td data-cell="B42"></td>
<td data-cell="C42"></td>
<td data-cell="G42"></td>
<td data-cell="H42"></td>
<td data-cell="I42"></td>
<td data-cell="J42"></td>
<td data-cell="K42"></td>
<td data-cell="L42"></td>
</tr>
<tr>
<th scope="row">43</th>
<td data-cell="A43"></td>
<td data-cell="B43"></td>
<td data-cell="C43"></td>
<td data-cell="G43"></td>
<td data-cell="H43"></td>
<td data-cell="I43"></td>
<td data-cell="J43"></td>
<td data-cell="K43"></td>
<td data-cell="L43"></td>
</tr>
</tbody>
</table>
</div>

</details>
```

```{=html}
<script>
(() => {
  const cellPattern = /\b([A-Z]{1,3}\d+)\b/g;
  const sumPattern = /SUM\s*\(\s*([A-Z]+\d+)\s*:\s*([A-Z]+\d+)\s*\)/gi;
  const numberPattern = /^[0-9eE+\-*/(). ]+$/;
  const columnNumber = (letters) => {
    let value = 0;
    for (const letter of letters) value = value * 26 + letter.charCodeAt(0) - 64;
    return value;
  };
  const cellElement = (table, reference) => table.querySelector(`[data-cell="${reference}"]`);
  const evaluate = (table, reference, reactions, cache = {}, visiting = new Set()) => {
    if (reactions.has(reference)) return Number(reactions.input.value) || 0;
    if (Object.prototype.hasOwnProperty.call(cache, reference)) return cache[reference];
    if (visiting.has(reference)) return NaN;
    const cell = cellElement(table, reference);
    if (!cell) return NaN;
    visiting.add(reference);
    let result;
    const formula = cell.dataset.formula;
    if (formula) {
      let expression = formula.slice(1);
      expression = expression.replace(sumPattern, (_, start, end) => {
        const startColumn = start.match(/[A-Z]+/)[0];
        const endColumn = end.match(/[A-Z]+/)[0];
        const startRow = Number(start.match(/\d+/)[0]);
        const endRow = Number(end.match(/\d+/)[0]);
        let total = 0;
        for (let row = startRow; row <= endRow; row += 1) {
          for (let column = columnNumber(startColumn); column <= columnNumber(endColumn); column += 1) {
            let letters = "";
            let n = column;
            while (n > 0) { const remainder = (n - 1) % 26; letters = String.fromCharCode(65 + remainder) + letters; n = Math.floor((n - 1) / 26); }
            const value = evaluate(table, `${letters}${row}`, reactions, cache, visiting);
            if (Number.isFinite(value)) total += value;
          }
        }
        return String(total);
      });
      expression = expression.replace(cellPattern, (_, ref) => String(evaluate(table, ref, reactions, cache, visiting)));
      if (numberPattern.test(expression)) {
        try { result = Function(`"use strict"; return (${expression});`)(); } catch (_) { result = NaN; }
      } else result = NaN;
    } else {
      result = Number(cell.textContent.trim());
    }
    visiting.delete(reference);
    cache[reference] = Number(result);
    return cache[reference];
  };
  const format = (value) => {
    if (!Number.isFinite(value)) return "";
    return Number.isInteger(value) ? String(value) : String(Number(value.toFixed(8)));
  };
  document.querySelectorAll(".pcr-sheet").forEach((section) => {
    const input = section.querySelector(".pcr-reaction-input");
    const table = section.querySelector(".pcr-table");
    const reactionCells = new Set(Array.from(table.querySelectorAll("[data-reaction-cell=\"true\"]")).map((cell) => cell.dataset.cell));
    reactionCells.input = input;
    const update = () => {
      const cache = {};
      table.querySelectorAll("[data-formula]").forEach((cell) => {
        cell.textContent = format(evaluate(table, cell.dataset.cell, reactionCells, cache));
      });
      table.querySelectorAll("[data-reaction-cell=\"true\"]").forEach((cell) => {
        cell.textContent = format(Number(input.value) || 0);
      });
    };
    input.addEventListener("input", update);
    update();
  });
})();
</script>
```

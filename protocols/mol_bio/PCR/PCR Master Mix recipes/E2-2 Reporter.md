---
title: "E2-2 Reporter"
description: "Interactive PCR master mix calculator from the E2-2 Reporter sheet."
author: "Goldrath Lab"
date: last-modified
---

# E2-2 Reporter

Enter the **number of reactions needed** in the highlighted box. Calculated amounts update automatically using the original workbook formulas. For pages with multiple mixes, set the reaction count for each mix separately.

Column B contains the amount for one reaction; column C contains the amount for the selected number of reactions. Counts include only the reactions you enter; no extra reactions are added.

[Download the original workbook](../../../Goldrath_Protocols/The%20Master%20Folder/PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

```{=html}
<div class="pcr-calculator">
<div class="pcr-controls">
<div class="pcr-control">
<label for="pcr-reactions-c2">TCF4 WT — Number of reactions needed</label>
<input id="pcr-reactions-c2" class="pcr-reaction-input" data-reaction-cell="C2" type="number" min="0" step="1" value="20" required aria-describedby="pcr-reactions-c2-help pcr-reactions-c2-error">
<small id="pcr-reactions-c2-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c2-error" class="pcr-input-error" aria-live="polite"></span>
</div>
<div class="pcr-control">
<label for="pcr-reactions-c16">TCF4 Mut — Number of reactions needed</label>
<input id="pcr-reactions-c16" class="pcr-reaction-input" data-reaction-cell="C16" type="number" min="0" step="1" value="20" required aria-describedby="pcr-reactions-c16-help pcr-reactions-c16-error">
<small id="pcr-reactions-c16-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c16-error" class="pcr-input-error" aria-live="polite"></span>
</div>
<div class="pcr-control">
<label for="pcr-reactions-c30">LacZ — Number of reactions needed</label>
<input id="pcr-reactions-c30" class="pcr-reaction-input" data-reaction-cell="C30" type="number" min="0" step="1" value="20" required aria-describedby="pcr-reactions-c30-help pcr-reactions-c30-error">
<small id="pcr-reactions-c30-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c30-error" class="pcr-input-error" aria-live="polite"></span>
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
<td data-cell="A1">TCF4 WT</td>
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
<td data-cell="I2">E2-2 GEN</td>
<td data-cell="J2">1. Incubate at 94°C for 5:00</td>
<td data-cell="K2">TCF4 WT F-CCGATGACAGTGATGATGGT</td>
<td data-cell="L2">300bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">10x NEB buffer</td>
<td data-cell="B3">4</td>
<td data-cell="C3" data-formula="=B3*C2" title="Workbook formula: =B3*C2">80</td>
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
<td data-cell="C4" data-formula="=B4*C2" title="Workbook formula: =B4*C2">12</td>
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
<td data-cell="C5" data-formula="=B5*C2" title="Workbook formula: =B5*C2">4</td>
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
<td data-cell="C6" data-formula="=B6*C2" title="Workbook formula: =B6*C2">8</td>
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
<td data-cell="C7" data-formula="=B7*C2" title="Workbook formula: =B7*C2">8</td>
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
<td data-cell="B9">15.2</td>
<td data-cell="C9" data-formula="=B9*C2" title="Workbook formula: =B9*C2">304</td>
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
<td data-cell="B11">20</td>
<td data-cell="C11" data-formula="=B11*C2" title="Workbook formula: =B11*C2">400</td>
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
<td data-cell="C16">20</td>
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
<td data-cell="C17" data-formula="=B17*C16" title="Workbook formula: =B17*C16">80</td>
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
<td data-cell="C18" data-formula="=B18*C16" title="Workbook formula: =B18*C16">12</td>
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
<td data-cell="C19" data-formula="=B19*C16" title="Workbook formula: =B19*C16">4</td>
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
<td data-cell="C20" data-formula="=B20*C16" title="Workbook formula: =B20*C16">8</td>
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
<td data-cell="C21" data-formula="=B21*C16" title="Workbook formula: =B21*C16">8</td>
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
<td data-cell="C22" data-formula="=B22*C16" title="Workbook formula: =B22*C16">4</td>
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
<td data-cell="C23" data-formula="=B23*C16" title="Workbook formula: =B23*C16">304</td>
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
<td data-cell="C24" data-formula="=B24*C16" title="Workbook formula: =B24*C16">20</td>
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
<td data-cell="C25" data-formula="=B25*C16" title="Workbook formula: =B25*C16">400</td>
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
<td data-cell="C26" data-formula="=B26*C16" title="Workbook formula: =B26*C16">500</td>
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
<td data-cell="C30">20</td>
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
<td data-cell="C31" data-formula="=B31*C30" title="Workbook formula: =B31*C30">40</td>
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
<td data-cell="C32" data-formula="=B32*C30" title="Workbook formula: =B32*C30">40</td>
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
<td data-cell="C33" data-formula="=B33*C30" title="Workbook formula: =B33*C30">4</td>
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
<td data-cell="C34" data-formula="=B34*C30" title="Workbook formula: =B34*C30">8</td>
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
<td data-cell="C35" data-formula="=B35*C30" title="Workbook formula: =B35*C30">8</td>
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
<td data-cell="C36" data-formula="=B36*C30" title="Workbook formula: =B36*C30">4</td>
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
<td data-cell="C37" data-formula="=B37*C30" title="Workbook formula: =B37*C30">276</td>
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
<td data-cell="C38" data-formula="=B38*C30" title="Workbook formula: =B38*C30">20</td>
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
<td data-cell="C39" data-formula="=B39*C30" title="Workbook formula: =B39*C30">400</td>
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
<td data-cell="H41"></td>
<td data-cell="I41"></td>
<td data-cell="J41"></td>
<td data-cell="K41"></td>
<td data-cell="L41"></td>
</tr>
</tbody>
</table>
</div>
</div>
```

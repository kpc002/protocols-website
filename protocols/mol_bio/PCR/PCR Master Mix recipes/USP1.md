---
title: "USP1"
description: "Interactive PCR master mix calculator from the USP1 sheet."
author: "Goldrath Lab"
date: last-modified
---

# USP1

Enter the **number of reactions needed** in the highlighted box. Calculated amounts update automatically using the original workbook formulas. For pages with multiple mixes, set the reaction count for each mix separately.

Column B contains the amount for one reaction; column C contains the amount for the selected number of reactions. Counts include only the reactions you enter; no extra reactions are added.

[Download the original workbook](../../../Goldrath_Protocols/The%20Master%20Folder/PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

```{=html}
<div class="pcr-calculator">
<div class="pcr-controls">
<div class="pcr-control">
<label for="pcr-reactions-c2">USP1 1 — Number of reactions needed</label>
<input id="pcr-reactions-c2" class="pcr-reaction-input" data-reaction-cell="C2" type="number" min="0" step="1" value="20" required aria-describedby="pcr-reactions-c2-help pcr-reactions-c2-error">
<small id="pcr-reactions-c2-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c2-error" class="pcr-input-error" aria-live="polite"></span>
</div>
<div class="pcr-control">
<label for="pcr-reactions-c15">USP1 2 — Number of reactions needed</label>
<input id="pcr-reactions-c15" class="pcr-reaction-input" data-reaction-cell="C15" type="number" min="0" step="1" value="20" required aria-describedby="pcr-reactions-c15-help pcr-reactions-c15-error">
<small id="pcr-reactions-c15-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c15-error" class="pcr-input-error" aria-live="polite"></span>
</div>
<div class="pcr-control">
<label for="pcr-reactions-c29">USP1 3 — Number of reactions needed</label>
<input id="pcr-reactions-c29" class="pcr-reaction-input" data-reaction-cell="C29" type="number" min="0" step="1" value="20" required aria-describedby="pcr-reactions-c29-help pcr-reactions-c29-error">
<small id="pcr-reactions-c29-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c29-error" class="pcr-input-error" aria-live="polite"></span>
</div>
<div class="pcr-control">
<label for="pcr-reactions-c43">USP1 4 — Number of reactions needed</label>
<input id="pcr-reactions-c43" class="pcr-reaction-input" data-reaction-cell="C43" type="number" min="0" step="1" value="20" required aria-describedby="pcr-reactions-c43-help pcr-reactions-c43-error">
<small id="pcr-reactions-c43-help">Enter a whole number in this highlighted box.</small>
<span id="pcr-reactions-c43-error" class="pcr-input-error" aria-live="polite"></span>
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
<td data-cell="A1">USP1 1</td>
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
<td data-cell="I2">USP1 Gen</td>
<td data-cell="J2">1. Incubate at 94°C for 5:00</td>
<td data-cell="K2">common-LoxPF</td>
<td data-cell="L2">161bp</td>
</tr>
<tr>
<th scope="row">3</th>
<td data-cell="A3">5x buffer</td>
<td data-cell="B3">5</td>
<td data-cell="C3" data-formula="=B3*C2" title="Workbook formula: =B3*C2">100</td>
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
<td data-cell="C4" data-formula="=B4*C2" title="Workbook formula: =B4*C2">34</td>
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
<td data-cell="C5" data-formula="=B5*C2" title="Workbook formula: =B5*C2">10</td>
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
<td data-cell="C6" data-formula="=B6*C2" title="Workbook formula: =B6*C2">10</td>
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
<td data-cell="C7" data-formula="=B7*C2" title="Workbook formula: =B7*C2">10</td>
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
<td data-cell="C8" data-formula="=B8*C2" title="Workbook formula: =B8*C2">5</td>
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
<td data-cell="C9" data-formula="=B9*C2" title="Workbook formula: =B9*C2">312</td>
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
<td data-cell="C10" data-formula="=B10*C2" title="Workbook formula: =B10*C2">20</td>
<td data-cell="H10"></td>
<td data-cell="I10"></td>
<td data-cell="J10">9. Cycle to step 6, 30 times</td>
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
<td data-cell="J11">10. Incubate at 72°C for 5:00</td>
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
<td data-cell="A14">USP1 2</td>
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
<td data-cell="A15"></td>
<td data-cell="B15">x1</td>
<td data-cell="C15">20</td>
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
<td data-cell="C16" data-formula="=B16*C15" title="Workbook formula: =B16*C15">100</td>
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
<td data-cell="C17" data-formula="=B17*C15" title="Workbook formula: =B17*C15">34</td>
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
<td data-cell="C18" data-formula="=B18*C15" title="Workbook formula: =B18*C15">10</td>
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
<td data-cell="C19" data-formula="=B19*C15" title="Workbook formula: =B19*C15">10</td>
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
<td data-cell="C20" data-formula="=B20*C15" title="Workbook formula: =B20*C15">10</td>
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
<td data-cell="C21" data-formula="=B21*C15" title="Workbook formula: =B21*C15">5</td>
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
<td data-cell="C22" data-formula="=B22*C15" title="Workbook formula: =B22*C15">312</td>
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
<td data-cell="C23" data-formula="=B23*C15" title="Workbook formula: =B23*C15">20</td>
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
<td data-cell="C24" data-formula="=B24*C15" title="Workbook formula: =B24*C15">500</td>
<td data-cell="H24"></td>
<td data-cell="I24"></td>
<td data-cell="J24">9. Cycle to step 6, 30 times</td>
<td data-cell="K24"></td>
<td data-cell="L24"></td>
</tr>
<tr>
<th scope="row">25</th>
<td data-cell="A25"></td>
<td data-cell="B25"></td>
<td data-cell="C25"></td>
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
<td data-cell="A28">USP1 3</td>
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
<td data-cell="A29"></td>
<td data-cell="B29">x1</td>
<td data-cell="C29">20</td>
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
<td data-cell="C30" data-formula="=B30*C29" title="Workbook formula: =B30*C29">100</td>
<td data-cell="H30">Kyla</td>
<td data-cell="I30">USP1 Gen</td>
<td data-cell="J30">1. Incubate at 94°C for 5:00</td>
<td data-cell="K30">common3&#x27;F</td>
<td data-cell="L30">944bp</td>
</tr>
<tr>
<th scope="row">31</th>
<td data-cell="A31">MgCl2</td>
<td data-cell="B31">1.7</td>
<td data-cell="C31" data-formula="=B31*C29" title="Workbook formula: =B31*C29">34</td>
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
<td data-cell="C32" data-formula="=B32*C29" title="Workbook formula: =B32*C29">10</td>
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
<td data-cell="C33" data-formula="=B33*C29" title="Workbook formula: =B33*C29">10</td>
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
<td data-cell="C34" data-formula="=B34*C29" title="Workbook formula: =B34*C29">10</td>
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
<td data-cell="C35" data-formula="=B35*C29" title="Workbook formula: =B35*C29">5</td>
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
<td data-cell="C36" data-formula="=B36*C29" title="Workbook formula: =B36*C29">312</td>
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
<td data-cell="C37" data-formula="=B37*C29" title="Workbook formula: =B37*C29">20</td>
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
<td data-cell="C38" data-formula="=B38*C29" title="Workbook formula: =B38*C29">500</td>
<td data-cell="H38"></td>
<td data-cell="I38"></td>
<td data-cell="J38">9. Cycle to step 6, 30 times</td>
<td data-cell="K38"></td>
<td data-cell="L38"></td>
</tr>
<tr>
<th scope="row">39</th>
<td data-cell="A39"></td>
<td data-cell="B39"></td>
<td data-cell="C39"></td>
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
<td data-cell="J40">10. Incubate at 72°C for 5:00</td>
<td data-cell="K40"></td>
<td data-cell="L40"></td>
</tr>
<tr>
<th scope="row">41</th>
<td data-cell="A41"></td>
<td data-cell="B41"></td>
<td data-cell="C41"></td>
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
<td data-cell="C43">20</td>
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
<td data-cell="C44" data-formula="=B44*C43" title="Workbook formula: =B44*C43">100</td>
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
<td data-cell="C45" data-formula="=B45*C43" title="Workbook formula: =B45*C43">34</td>
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
<td data-cell="C46" data-formula="=B46*C43" title="Workbook formula: =B46*C43">10</td>
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
<td data-cell="C47" data-formula="=B47*C43" title="Workbook formula: =B47*C43">10</td>
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
<td data-cell="C48" data-formula="=B48*C43" title="Workbook formula: =B48*C43">10</td>
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
<td data-cell="C49" data-formula="=B49*C43" title="Workbook formula: =B49*C43">5</td>
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
<td data-cell="C50" data-formula="=B50*C43" title="Workbook formula: =B50*C43">312</td>
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
<td data-cell="C51" data-formula="=B51*C43" title="Workbook formula: =B51*C43">20</td>
<td data-cell="H51"></td>
<td data-cell="I51"></td>
<td data-cell="J51">9. Cycle to step 6, 30 times</td>
<td data-cell="K51"></td>
<td data-cell="L51"></td>
</tr>
<tr>
<th scope="row">52</th>
<td data-cell="A52">Total</td>
<td data-cell="B52">25</td>
<td data-cell="C52" data-formula="=B52*C43" title="Workbook formula: =B52*C43">500</td>
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
<td data-cell="H53"></td>
<td data-cell="I53"></td>
<td data-cell="J53"></td>
<td data-cell="K53"></td>
<td data-cell="L53"></td>
</tr>
<tr>
<th scope="row">54</th>
<td data-cell="A54"></td>
<td data-cell="B54"></td>
<td data-cell="C54"></td>
<td data-cell="H54"></td>
<td data-cell="I54"></td>
<td data-cell="J54"></td>
<td data-cell="K54"></td>
<td data-cell="L54"></td>
</tr>
<tr>
<th scope="row">55</th>
<td data-cell="A55">USE NEB TAQ AS OUR LAB STOCK IS CONTAMINATED WITH LACZ AND CAN GET FALSE POSITIVES</td>
<td data-cell="B55"></td>
<td data-cell="C55"></td>
<td data-cell="H55"></td>
<td data-cell="I55"></td>
<td data-cell="J55"></td>
<td data-cell="K55"></td>
<td data-cell="L55"></td>
</tr>
</tbody>
</table>
</div>
</div>
```

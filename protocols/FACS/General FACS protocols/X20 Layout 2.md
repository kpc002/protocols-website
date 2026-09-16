---
title: "X20 Layout 2"
description: "Interactive LSRFortessa X-20 fluorochrome and optical-filter configuration reference with row colors preserved from the Excel workbook."
order: 11
author: "Giovanni Galleti"
date: last-modified
image: oligo.svg
keywords:
  - LSRFortessa
  - X-20
  - flow cytometry
  - fluorochrome
  - optical filter
  - FACS
---

# X20 Layout 2

Use the search box to narrow the configuration list. Antibody and dilution fields are editable for panel planning; changes remain in this browser session only.

[Download the original Excel workbook](FC7.X20_layout.xlsx){.btn .btn-primary download="FC7.X20_layout.xlsx"}

<section class="x20-layout-2" aria-label="LSRFortessa X-20 layout reference">
<label class="x20-search-label-2" for="x20-filter-2">Search fluorochromes or filters</label>
<input id="x20-filter-2" class="x20-filter-2" type="search" placeholder="For example: BV, PE, 670" autocomplete="off">
<p id="x20-results-2" class="x20-results-2" aria-live="polite"></p>
<div class="table-responsive">
<table id="x20-table-2" class="x20-table-2">
<thead><tr><th>Fluorochrome</th><th>Filter</th><th>Antibody</th><th>Dilution</th></tr></thead>
<tbody>
<tr class="row-blue"><td>FITC/GFP/YFP</td><td>488_530_30</td><td><input aria-label="Antibody for FITC/GFP/YFP" type="text"></td><td><input aria-label="Dilution for FITC/GFP/YFP" type="text"></td></tr>
<tr class="row-blue"><td>PerCP-Cy5.5/eFluor710</td><td>488_675_20 or 695_40</td><td><input aria-label="Antibody for PerCP-Cy5.5/eFluor710" type="text"></td><td><input aria-label="Dilution for PerCP-Cy5.5/eFluor710" type="text"></td></tr>
<tr class="row-green"><td>PE, MitoOrange</td><td>561_582_15</td><td><input aria-label="Antibody for PE, MitoOrange" type="text"></td><td><input aria-label="Dilution for PE, MitoOrange" type="text"></td></tr>
<tr class="row-green"><td>PE-TR, 594, RFP</td><td>561_610_20</td><td><input aria-label="Antibody for PE-TR, 594, RFP" type="text"></td><td><input aria-label="Dilution for PE-TR, 594, RFP" type="text"></td></tr>
<tr class="row-green"><td>PE-Cy5.5</td><td>561_670_14 or 710_50</td><td><input aria-label="Antibody for PE-Cy5.5" type="text"></td><td><input aria-label="Dilution for PE-Cy5.5" type="text"></td></tr>
<tr class="row-green"><td>PE-Cy7</td><td>561_780_60</td><td><input aria-label="Antibody for PE-Cy7" type="text"></td><td><input aria-label="Dilution for PE-Cy7" type="text"></td></tr>
<tr class="row-purple"><td>Pac Blue/BV421/ef450</td><td>405_450_40</td><td><input aria-label="Antibody for Pac Blue/BV421/ef450" type="text"></td><td><input aria-label="Dilution for Pac Blue/BV421/ef450" type="text"></td></tr>
<tr class="row-purple"><td>BV510/Ametrine</td><td>405_525_50</td><td><input aria-label="Antibody for BV510/Ametrine" type="text"></td><td><input aria-label="Dilution for BV510/Ametrine" type="text"></td></tr>
<tr class="row-purple"><td>BV605</td><td>405_610_20</td><td><input aria-label="Antibody for BV605" type="text"></td><td><input aria-label="Dilution for BV605" type="text"></td></tr>
<tr class="row-purple"><td>BV650</td><td>405_660_20</td><td><input aria-label="Antibody for BV650" type="text"></td><td><input aria-label="Dilution for BV650" type="text"></td></tr>
<tr class="row-purple"><td>BV711</td><td>405_710_50</td><td><input aria-label="Antibody for BV711" type="text"></td><td><input aria-label="Dilution for BV711" type="text"></td></tr>
<tr class="row-purple"><td>BV786</td><td>405_780_60</td><td><input aria-label="Antibody for BV786" type="text"></td><td><input aria-label="Dilution for BV786" type="text"></td></tr>
<tr class="row-red"><td>APC/AxF647/AxF660</td><td>628_670_40</td><td><input aria-label="Antibody for APC/AxF647/AxF660" type="text"></td><td><input aria-label="Dilution for APC/AxF647/AxF660" type="text"></td></tr>
<tr class="row-red"><td>AxF700</td><td>628_730_45</td><td><input aria-label="Antibody for AxF700" type="text"></td><td><input aria-label="Dilution for AxF700" type="text"></td></tr>
<tr class="row-red"><td>APC-Cy7</td><td>628_780_60</td><td><input aria-label="Antibody for APC-Cy7" type="text"></td><td><input aria-label="Dilution for APC-Cy7" type="text"></td></tr>
</tbody>
</table>
</div>
<button id="x20-clear-2" class="btn btn-outline-secondary" type="button">Clear plan</button>
</section>

<style>
.x20-layout-2 { margin-top: 1.25rem; }
.x20-search-label-2 { display: block; font-weight: 600; margin-bottom: .35rem; }
.x20-filter-2 { width: min(28rem, 100%); padding: .45rem .6rem; border: 1px solid color-mix(in srgb, currentColor 30%, transparent); border-radius: .3rem; color: inherit; background: var(--bs-body-bg, white); }
.x20-results-2 { margin: .5rem 0; font-size: .9rem; opacity: .8; }
.x20-table-2 { width: 100%; }
.x20-table-2 th, .x20-table-2 td { padding: .45rem .55rem; }
.x20-table-2 thead { color: #fff; background: #7f7f7f; }
.x20-table-2 tbody tr { color: #fff; }
.x20-table-2 .row-gray { background: #7f7f7f; }
.x20-table-2 .row-blue { background: #0000ff; }
.x20-table-2 .row-green { background: #92d050; color: #111; }
.x20-table-2 .row-purple { background: #7030a0; }
.x20-table-2 .row-red { background: #c00000; }
.x20-table-2 input { width: 100%; min-width: 9rem; padding: .35rem .45rem; border: 1px solid color-mix(in srgb, currentColor 25%, transparent); border-radius: .25rem; color: #111; background: #fff; }
#x20-clear-2 { margin-top: .75rem; }
</style>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const filter = document.getElementById("x20-filter-2");
  const rows = [...document.querySelectorAll("#x20-table-2 tbody tr")];
  const results = document.getElementById("x20-results-2");
  const updateRows = () => {
    const query = filter.value.trim().toLowerCase();
    const visible = rows.filter(row => {
      const matches = row.cells[0].textContent.toLowerCase().includes(query)
        || row.cells[1].textContent.toLowerCase().includes(query);
      row.hidden = !matches;
      return matches;
    }).length;
    results.textContent = `${visible} of ${rows.length} configurations shown`;
  };
  filter.addEventListener("input", updateRows);
  document.getElementById("x20-clear-2").addEventListener("click", () => {
    document.querySelectorAll("#x20-table-2 input").forEach(input => { input.value = ""; });
  });
  updateRows();
});
</script>

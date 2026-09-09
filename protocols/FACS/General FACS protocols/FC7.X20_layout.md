---
title: FC7.X20_layout
description: Interactive LSRFortessa X-20 fluorochrome and optical-filter configuration reference, with editable antibody and dilution fields for panel planning.
order: 10
author: Giovanni Galleti
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

Use the search box to narrow the configuration list. Antibody and dilution fields are editable for planning; changes remain in this browser session only.

[Download the original Excel workbook](FC7.X20_layout.xlsx){.btn .btn-primary download="FC7.X20_layout.xlsx"}

<section class="x20-layout" aria-label="LSRFortessa X-20 layout reference">
<label class="x20-search-label" for="x20-filter">Search fluorochromes or filters</label>
<input id="x20-filter" class="x20-filter" type="search" placeholder="For example: BV, PE, 670" autocomplete="off">
<p id="x20-results" class="x20-results" aria-live="polite"></p>
<div class="table-responsive">
<table id="x20-table" class="x20-table">
<thead><tr><th>Fluorochrome</th><th>Filter</th><th>Antibody</th><th>Dilution</th></tr></thead>
<tbody>
<tr><td>FITC/GFP/YFP</td><td>488_530_30</td><td><input aria-label="Antibody for FITC/GFP/YFP" type="text"></td><td><input aria-label="Dilution for FITC/GFP/YFP" type="text"></td></tr>
<tr><td>PerCP-Cy5.5/eFluor710</td><td>488_675_20 or 695_40</td><td><input aria-label="Antibody for PerCP-Cy5.5/eFluor710" type="text"></td><td><input aria-label="Dilution for PerCP-Cy5.5/eFluor710" type="text"></td></tr>
<tr><td>PE, MitoOrange</td><td>561_582_15</td><td><input aria-label="Antibody for PE, MitoOrange" type="text"></td><td><input aria-label="Dilution for PE, MitoOrange" type="text"></td></tr>
<tr><td>PE-TR, 594, RFP</td><td>561_610_20</td><td><input aria-label="Antibody for PE-TR, 594, RFP" type="text"></td><td><input aria-label="Dilution for PE-TR, 594, RFP" type="text"></td></tr>
<tr><td>PE-Cy5.5</td><td>561_670_14 or 710_50</td><td><input aria-label="Antibody for PE-Cy5.5" type="text"></td><td><input aria-label="Dilution for PE-Cy5.5" type="text"></td></tr>
<tr><td>PE-Cy7</td><td>561_780_60</td><td><input aria-label="Antibody for PE-Cy7" type="text"></td><td><input aria-label="Dilution for PE-Cy7" type="text"></td></tr>
<tr><td>Pac Blue/BV421/ef450</td><td>405_450_40</td><td><input aria-label="Antibody for Pac Blue/BV421/ef450" type="text"></td><td><input aria-label="Dilution for Pac Blue/BV421/ef450" type="text"></td></tr>
<tr><td>BV510/Ametrine</td><td>405_525_50</td><td><input aria-label="Antibody for BV510/Ametrine" type="text"></td><td><input aria-label="Dilution for BV510/Ametrine" type="text"></td></tr>
<tr><td>BV605</td><td>405_610_20</td><td><input aria-label="Antibody for BV605" type="text"></td><td><input aria-label="Dilution for BV605" type="text"></td></tr>
<tr><td>BV650</td><td>405_660_20</td><td><input aria-label="Antibody for BV650" type="text"></td><td><input aria-label="Dilution for BV650" type="text"></td></tr>
<tr><td>BV711</td><td>405_710_50</td><td><input aria-label="Antibody for BV711" type="text"></td><td><input aria-label="Dilution for BV711" type="text"></td></tr>
<tr><td>BV786</td><td>405_780_60</td><td><input aria-label="Antibody for BV786" type="text"></td><td><input aria-label="Dilution for BV786" type="text"></td></tr>
<tr><td>APC/AxF647/AxF660</td><td>628_670_40</td><td><input aria-label="Antibody for APC/AxF647/AxF660" type="text"></td><td><input aria-label="Dilution for APC/AxF647/AxF660" type="text"></td></tr>
<tr><td>AxF700</td><td>628_730_45</td><td><input aria-label="Antibody for AxF700" type="text"></td><td><input aria-label="Dilution for AxF700" type="text"></td></tr>
<tr><td>APC-Cy7</td><td>628_780_60</td><td><input aria-label="Antibody for APC-Cy7" type="text"></td><td><input aria-label="Dilution for APC-Cy7" type="text"></td></tr>
</tbody>
</table>
</div>
<button id="x20-clear" class="btn btn-outline-secondary" type="button">Clear plan</button>
</section>

<style>
.x20-layout { margin-top: 1.25rem; }
.x20-search-label { display: block; font-weight: 600; margin-bottom: .35rem; }
.x20-filter { width: min(28rem, 100%); padding: .45rem .6rem; border: 1px solid color-mix(in srgb, currentColor 30%, transparent); border-radius: .3rem; color: inherit; background: var(--bs-body-bg, white); }
.x20-results { margin: .5rem 0; font-size: .9rem; opacity: .8; }
.x20-table { width: 100%; }
.x20-table input { width: 100%; min-width: 9rem; padding: .35rem .45rem; border: 1px solid color-mix(in srgb, currentColor 25%, transparent); border-radius: .25rem; color: inherit; background: var(--bs-body-bg, white); }
#x20-clear { margin-top: .75rem; }
</style>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const filter = document.getElementById("x20-filter");
  const rows = [...document.querySelectorAll("#x20-table tbody tr")];
  const results = document.getElementById("x20-results");
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
  document.getElementById("x20-clear").addEventListener("click", () => {
    document.querySelectorAll("#x20-table input:not(#x20-filter)").forEach(input => { input.value = ""; });
  });
  updateRows();
});
</script>

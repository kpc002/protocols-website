---
search: false
title: "Molecular biology"
description: "Protocols and reference materials for routine molecular biology workflows, including cell culture, PCR, RNA and cDNA preparation, qPCR, chromatin assays, western blotting, and CRISPR validation."
image: 'agarose-gel.svg'
listing: 
  type: table
  contents:
    - "/*/index.?(q)md"
    - "*.md"
    - "*.qmd"
  fields: [title, description, author]
  sort: title
---

Browse protocols and reference materials for routine molecular biology workflows, including cell culture, PCR, RNA and cDNA preparation, qPCR, chromatin assays, western blotting, and CRISPR validation.

<span class="visually-hidden">{{< fa file-lines >}}</span>

<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".quarto-listing-container-table .listing-title").forEach((link) => {
    if (link.querySelector(".fa-file-lines")) return;
    const icon = document.createElement("i");
    icon.className = "fa-solid fa-file-lines";
    icon.setAttribute("aria-hidden", "true");
    link.prepend(icon, " ");
  });
});
</script>

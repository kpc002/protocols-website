---
order: 4
title: "Western Blot"
description: Protocols for Western Blot
listing: 
  type: table
  contents: ["*.md", "*.qmd"]
  fields: [title, description, author]
  sort: title
image: western.png
---

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

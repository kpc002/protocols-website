---
search: false
title: "CUT&RUN and ChIP"
description: "Chromatin immunoprecipitation, CUT&RUN, and sequencing-library preparation protocols."
order: 10
listing:
  type: table
  contents: "*.md"
  fields: [title, description, author]
  sort: title
---

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

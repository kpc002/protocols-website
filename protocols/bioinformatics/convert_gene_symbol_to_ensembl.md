---
order: 3
title: Convert gene symbols
author: Maximilian Heeg
date: last-modified
description: 
  Convert gene symbols to ensembl ids and back.
image: convert_gene_symbol.png
---

Converting gene symbols to ENSEMBL IDs in R is fast and easy.

``` r
require(org.Mm.eg.db)
​
symbols = c("Tox", "Id2")
​
# convert SYMBOL to ENSMBL
ensembl = AnnotationDbi::mapIds(
  x = org.Mm.eg.db,
  keys = symbols,
  keytype = "SYMBOL",
  column = "ENSEMBL"
)

# > ensembl
#                  Tox                  Id2 
# "ENSMUSG00000041272" "ENSMUSG00000020644" 
​
# And back
AnnotationDbi::mapIds(
  x = org.Mm.eg.db,
  keys = ensembl,
  keytype = "ENSEMBL",
  column = "SYMBOL"
)

# ENSMUSG00000041272 ENSMUSG00000020644 
#              "Tox"              "Id2" 
```

Sometimes the ENSEMBL IDs have a version, e.g. `ENSMUST00000178862.1`, we need to remove everything after the `.`. This can be done using regex matching.

``` r
ids = "ENSMUST00000178862.1"
stringr::str_remove(ids, "\\.[0-9]+$")
```

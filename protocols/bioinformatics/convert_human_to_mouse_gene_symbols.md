---
order: 4
title: Convert human genes to mouse
author: Maximilian Heeg
date: last-modified
description: 
  Convert human gene symbols to to mouse gene symbols.
image: human_to_mouse.png
---

Converting human gene symbols to mouse gene symbols in R.

``` r
convertHumanGeneList <- function(x){
    require(biomaRt)
    human = useEnsembl(biomart = "genes", dataset = "hsapiens_gene_ensembl")
    mouse = useEnsembl(biomart = "genes", dataset = "mmusculus_gene_ensembl")
    genesV2 = getLDS(attributes = c("hgnc_symbol"), 
                     filters = "hgnc_symbol", 
                     values = x , 
                     mart = human, 
                     attributesL = c("mgi_symbol"), 
                     martL = mouse, 
                     uniqueRows=T)
    new_symbols <- unique(genesV2[, 2])
    return(new_symbols)
}
```

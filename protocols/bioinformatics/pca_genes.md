---
order: 15
title: "PCA: get most important genes"
author: Maximilian Heeg
date: last-modified
description: 
  Ever wondered which genes are responsibe for the differences in a PCA? plot? Find it out here.
image: pca.png
---

`DESeq2` has a convenient function to plot a PCA. However, is does not include a nice interface the get the genes, that are most important for each PC. Hence I create a small helper function for that purpose.

The function can be used with any `DESeqTransform` object created by `normTransform`, `vst` or `rlog` and returns a list with the most important genes for each PC.

``` r
#' Function to get the driving genes for each Principal Component (PC)
#'
#' @param object a DESeqTransform object, with data in assay(x), produced for example by either rlog or 
#'               varianceStabilizingTransformation.
#' @param n_genes Number of genes to return for each PC. (Default 10)
#' @param ntop  number of top genes to use for principal components, selected by highest row variance
#'
#' @return A list with the top `n_genes` for each PC.
getPCAGenes <- function(object, n_genes = 10, ntop=500){
  # this is the same as for plotPCA in the DESeq2 Package.
  rv <- rowVars(assay(object))
  select <- order(rv, decreasing=TRUE)[seq_len(min(ntop, length(rv)))]
  pca <- prcomp(t(assay(object)[select,]))
  
  # instead of plotting, we will get the eigenvalues
  loadings <- as.data.frame(pca$rotation)
  
  # and calculate the percent contribution to each PC here.
  aload <- abs(loadings) ## save absolute values
  res <- sweep(aload, 2, colSums(aload), "/")
  
  # return a list with the top X genes for each PC
  lapply(res, function(x) {
    top <- order(x, decreasing=TRUE)[1:n_genes]
    genes <- rownames(res)[top]
    sprintf("%s (%.2f%%)", genes, x[top]*100)
    })  
}
```

You can now get the most important genes with `getPCAGenes(vst(dds))`.

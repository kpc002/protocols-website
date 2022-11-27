---
weight: 2
title: "HIC1 and TRM score in human scRNA"
--- 

# Example Workflow: HIC1 and TRM score in human scRNA

Here, we analyse the human scRNA data from John Change, annotate the cell types, look for differential expression and pathway enrichment in the samples.

Data is published here: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE125527

**Aims:**
- See if HIC1 expression is also up in the gut in humans
- Validate TRM score derived from mice in a human dataset
- Check if IEL in human are also TGFb dependent. 


The different scRNA samples have been merged with `cellranger aggr`.

## Required Packages 

```r
suppressPackageStartupMessages({
  library(Matrix)
  library(SingleCellExperiment)
  library(scater)
  library(scran)
  library(scuttle)
  library(BiocParallel)
  library(BiocSingular)
  library(ComplexHeatmap)
  library(SingleR)
  library(celldex)
  library(magieR)
  library(patchwork)
  library(rasterpdf)
  library(AUCell)
  library(DropletUtils)
})
``` 

## Import data


```r
sce <- DropletUtils::read10xCounts("data/filtered_feature_bc_matrix/")
sce
```

Since we import the filtered data (not the raw), we do not need to remove empty droplets anymore.

## QC

```r

# remove genes that are not expression
summary(rowSums(counts(sce))>0)
sce <- sce[rowSums(counts(sce))>0, ]


# Find mito genes
is.mito <- grepl("^MT-", rowData(sce)$Symbol)
summary(is.mito)

unfiltered <- sce

# do basic QC, filter out cells with too many MT reads, two few reads or too few UMI
stats <- perCellQCMetrics(sce, subsets=list(Mito=which(is.mito)))
qc <- quickPerCellQC(stats, percent_subsets="subsets_Mito_percent")
sce <- sce[,!qc$discard]

colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- qc$discard

gridExtra::grid.arrange(
  plotColData(unfiltered, y="sum", colour_by="discard") +
    scale_y_log10() + ggtitle("Total count"),
  plotColData(unfiltered, y="detected", colour_by="discard") +
    scale_y_log10() + ggtitle("Detected features"),
  plotColData(unfiltered, y="subsets_Mito_percent",
              colour_by="discard") + ggtitle("Mito percent"),
  ncol=2
)

plotColData(unfiltered, x="sum", y="subsets_Mito_percent",
            colour_by="discard") + scale_x_log10() + xlab("Total count")

rm(unfiltered)
summary(qc$discard)
rm(qc)
gc()

```

{{< lightbox src="images/02_QC-1.png" caption="QC part 1" >}} 
{{< lightbox src="images/02_QC-2.png" caption="QC part 2" >}} 

## Add annotation

```r
# Add the annotation from cellraner aggr.
# sample id is appended to the barcode, extrcat with regex
colnames(sce) <- sce$Barcode
sce$sample_id <- as.numeric(stringr::str_match(colnames(sce), "-([0-9]{1,2})$")[,2])

# read the annotation table
annotation <- readr::read_tsv("data/miguel_metadata.txt", 
                              col_names = c("Sample_Name", "Patient_ID", "Location",  "Disease",
                                            "QC_Chang_Lab", "GEO_Patient_ID"),
                              col_types = "ccc__ccc")
annotation$sample_id <- rownames(annotation)

# merge coldata and annotation
colData(sce) <- merge(colData(sce), annotation)

# rename and set order, this is importan for DE testing (PBMC is reference)
sce$Location <- forcats::fct_recode(sce$Location,
                                    PBMC = "pBMC",
                                    Rectum = "R",
                                    Intestine = "I")

sce$Location <- forcats::fct_relevel(sce$Location, "PBMC", "Intestine", "Rectum")
```

## Normalization & variance-modelling 


### Normalization

```r
set.seed(101000110)
# Block by patient ID, this  is faster and makes more sense
clusters <- quickCluster(sce, BPPARAM=MulticoreParam(16),
                        block = sce$Patient_ID,
                        block.BPPARAM = MulticoreParam(10))
sce <- computeSumFactors(sce, clusters=clusters, BPPARAM=MulticoreParam(16))
sce <- logNormCounts(sce, BPPARAM=MulticoreParam(16))

plot(librarySizeFactors(sce), sizeFactors(sce), pch=16,
     xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

{{< lightbox src="images/03_normalization-1.png" caption="Normalization" >}} 

### Variance-modelling

```r
set.seed(00010101)
dec.sce <- modelGeneVarByPoisson(sce, BPPARAM=MulticoreParam(16))
top.sce <- getTopHVGs(dec.sce, prop=0.1)

plot(dec.sce$mean, dec.sce$total, pch=16, cex=0.5,
     xlab="Mean of log-expression", ylab="Variance of log-expression")
curfit <- metadata(dec.sce)
curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
```
{{< lightbox src="images/03_normalization-2.png" caption="Variance-modelling" >}} 

## Dimensional reduction

```r
set.seed(101010011)
sce <- denoisePCA(sce, technical=dec.sce, subset.row=top.sce)
# tsne take too long
# sce <- runTSNE(sce, dimred="PCA", BPPARAM=MulticoreParam(16))
sce <- runUMAP(sce, dimred="PCA", BPPARAM=MulticoreParam(16))
```

## Clustering

```r
snn.gr <- buildSNNGraph(sce, use.dimred="PCA", k=25)
 
#  walktrap to slow .... so I prefer to use leiden (or louvain)
# colLabels(sce) <- factor(igraph::cluster_walktrap(snn.gr)$membership)
 
colLabels(sce) <- factor(igraph::cluster_louvain(snn.gr)$membership)
 

plotUMAP(sce, colour_by="Location")
plotUMAP(sce, colour_by="Location", other_fields = "Location") + facet_grid(~Location)
plotUMAP(sce, colour_by="Disease")
plotUMAP(sce, colour_by="Patient_ID")

```

{{< lightbox src="images/04_cluster-1.png" caption="UMAP colored by Location" >}} 
{{< lightbox src="images/04_cluster-2.png" caption="UMAP facet by Location" >}} 
{{< lightbox src="images/04_cluster-3.png" caption="UMAP colored by Disease" >}} 
{{< lightbox src="images/04_cluster-4.png" caption="UMAP colored by Patient ID" >}} 


## SingleR

Cell annotation with SingleR. MonacoImmuneData as reference.
 
```r
ref <- MonacoImmuneData(ensembl = TRUE)
pred <- SingleR(test=sce, ref=ref, labels=ref$label.main,
                #de.method="wilcox",
                BPPARAM = MulticoreParam(24))

sce$singleR_labels <- pred$pruned.labels


# basic function to plot a table, color scale is set to 70 and 90 quantile
plotTableHeatmap <- function(x, y,
                             label_x,
                             label_y,
                             margin = NULL) {
  tbl <- table(x, y)
  subtitle <- dplyr::case_when(
                   is.null(margin) ~ "Percent of total",
                  !is.null(margin) && margin == 1 ~ "Percent of row",
                  !is.null(margin) && margin == 2 ~ "Percent of column"
                                                                                     )
  m <- prop.table(tbl, margin = margin)*100
  m <- as.matrix(m)
  tbl <- as.matrix(tbl)

  col_fun = circlize::colorRamp2(c(0,
                                 quantile(m, probs = c(70, 90)/100),
                                 100),
                               c("white","yellow","orange" ,"red"))
  Heatmap(m,
         name = subtitle,
         col = col_fun,
         column_title = label_y,
         row_title = label_x,
         cell_fun = function(j, i, x, y, width, height, fill) {
                grid.text(sprintf("%i \n %.1f%%", tbl[i,j],  m[i,j]), x, y, gp = gpar(fontsize = 10))
          },
         rect_gp = gpar(col= "grey80")
    )

} # end function


# what hides behind the singleR lables
# t cells = MAIT and gd
plotTableHeatmap(x = ref$label.main,
                 y = ref$label.fine,
                 label_x = "Labels Main",
                 label_y = "Labels Fine",
                 margin = 2
)


# Celltype per patient
plotTableHeatmap(x = sce$Patient_ID,
                 y = sce$singleR_labels,
                 label_x = "Patient",
                 label_y = "SingleR labels",
                 margin = 1
)

# Celltype per location
plotTableHeatmap(x = sce$Location,
                 y = sce$singleR_labels,
                 label_x = "Location",
                 label_y = "SingleR labels",
                 margin = 1
)

```

{{< lightbox src="images/05_singleR-1.png" caption="Label fine and label main" >}}
{{< lightbox src="images/05_singleR-2.png" caption="Celltype by patient" >}}
{{< lightbox src="images/05_singleR-3.png" caption="Celltype by location" >}} 

## Subsetting
### Subset to T cells

```r
tcell_subsets <- c("CD4+ T cells", "CD8+ T cells", "T cells")
sce <- sce[, sce$singleR_labels %in% tcell_subsets]
sce
```

### Subset on Controls

```r
sce <- sce[, sce$Disease == "Control"]
sce
```

## MAGIC imputation

```r
sce <- magieR(sce, n.jobs = 30)

colData(altExp(sce, "magic")) <- colData(sce)
rowData(altExp(sce, "magic")) <- rowData(sce)


plotExpression(altExp(sce, "magic"), features="HIC1",
                swap_rownames = "Symbol",
                x = "Location",
                other_fields = "Disease") + facet_grid(~Disease)

```

{{< lightbox src="images/07_plots-1.png" caption="HIC1 expression" >}}


## AUCell

This is for getting a score for a gene list.

### TGFb Signature and TRM signature

```r
# Load the TGFbeta list from tys paper
signature_tgfb <- readr::read_csv("signatures/TGFbeta.txt", col_names = FALSE)[[1]]
signature_trm <- readxl::read_excel("signatures/Gene Signatures and Counts.xlsx", sheet=2)[[1]]

# needs to be converted to Human ensembl gene ids
# One could use uppercase, but it is cleaner to use Biomart
# here's a small helper function for that
convertMouseGeneList <- function(x){
  require(biomaRt)
  human = useMart("ensembl", dataset = "hsapiens_gene_ensembl")
  mouse = useMart("ensembl", dataset = "mmusculus_gene_ensembl")
  genesV2 = getLDS(attributes = c("mgi_symbol"), filters = "mgi_symbol", values = x , mart = mouse, attributesL = c("ensembl_gene_id"), martL = human, uniqueRows=T)
  humanx <- unique(genesV2[, 2])
  # Print the first 6 genes found to the screen
  print(head(humanx))
  return(humanx)
}

signature_tgfb_human <- convertMouseGeneList(signature_tgfb)
signature_trm_human <- convertMouseGeneList(signature_trm)

geneSets <- list(
  TGFb = signature_tgfb_human,
  TRM = signature_trm_human
  # cholesterogenesis = c("ACAT1","ACAT2","CYP51A1","EBP","FDFT1","FDPS","GGPS1","HMGCR","HMGCS1", "HMGCS2","IDI1","LBR","LSS","MVD","MVK","PMVK","TM7SF2","DHCR7","DHCR24","NSDHL","HSD17B7", "MSMO1","SC5DL","LOC651621","SQLE","LOC730412","IDI2")
  # cholesterogenesis = c("ENSG00000075239", "ENSG00000120437", "ENSG00000001630", "ENSG00000147155", "ENSG00000079459", "ENSG00000160752", "ENSG00000152904", "ENSG00000113161", "ENSG00000112972", "ENSG00000134240", "ENSG00000067064", "ENSG00000143815", "ENSG00000160285", "ENSG00000167508", "ENSG00000110921", "ENSG00000163344", "ENSG00000149809", "ENSG00000172893", "ENSG00000116133", "ENSG00000147383", "ENSG00000132196", "ENSG00000052802", "ENSG00000109929", "ENSG00000104549", "ENSG00000148377")

)
```

### Get score using AUC

```r
library(AUCell)

# we need to split the matrix, it is just too big
# this might not be needed anymore after filtering, but it does not change the results
# so i just kept it
ExprMat <- logcounts(sce)
colnames(sce) <- sce$Barcode  # re add colnames, they seem to get lost when saveRDS
colnames(ExprMat) <- colnames(sce)

half <- round(ncol(ExprMat)/2)

#split expression matrix
ExprMat_1 <- ExprMat[,1:half]
ExprMat_2 <- ExprMat[,(half+1):ncol(ExprMat)]

#build  cell rankings
cells_rankings_1 <- AUCell_buildRankings(ExprMat_1)
cells_rankings_2 <- AUCell_buildRankings(ExprMat_2)
# colnames(cells_rankings_2) <- (half+1):ncol(ExprMat)


#Combine rankings
table(colnames(cells_rankings_1) %in% colnames(cells_rankings_2))

cells_rankings <- AUCell::cbind(cells_rankings_1, cells_rankings_2)

# remove tmp files and run gc()
rm(ExprMat, half, ExprMat_1, ExprMat_2, cells_rankings_1, cells_rankings_2)
gc()

# cells_rankings <- AUCell_buildRankings(logcounts(sce))
# maxRank set to 500, that's ~ the 5% in the output of buildRankings
cells_AUC <- AUCell_calcAUC(geneSets, cells_rankings, nCores=1, aucMaxRank = 500)
scores <- getAUC(cells_AUC)

# save it in the coldata of the sce
colData(sce)<- cbind(colData(sce), t(scores))
```

### Plots

```r
# rename T cells to other T cells
sce$singleR_labels2 <- ifelse(sce$singleR_labels == "T cells", 
                              "other T cells",
                              sce$singleR_labels)

#  copy to altExp --> for magic
colData(altExp(sce)) <- colData(sce)
rowData(altExp(sce)) <- rowData(sce)

p_hic1 <- plotExpression(altExp(sce[,sce$singleR_labels %in% tcell_subsets], "magic"), 
              features = "HIC1",
              x = "Location",
              colour_by = "Location",
              other_fields = "singleR_labels2",
              swap_rownames = "Symbol") + 
              facet_grid(~singleR_labels2) +
              ggtitle("HIC1 expression") + 
              xlab("") +
              ylab("expression [magic]")


p_tgfb <- plotColData(sce[,sce$singleR_labels %in% tcell_subsets], "TGFb",
            x = "Location", 
            colour_by = "Location",
            other_fields = "singleR_labels2") + 
            facet_grid(~singleR_labels2) + 
            ggtitle("TGFbeta score") + 
            geom_boxplot(outlier.shape = NA,
                      alpha=.2,
                      width=.5) + 
            xlab("") + 
            ylab("AUC")
                                          

p_trm <- plotColData(sce[,sce$singleR_labels %in% tcell_subsets], "TRM",
           x = "Location", 
           colour_by = "Location",
           other_fields = "singleR_labels2") + 
           facet_grid(~singleR_labels2) + 
           ggtitle("TRM score") + 
           geom_boxplot(outlier.shape = NA,
                     alpha=.2,
                     width=.5) + 
           xlab("") + 
           ylab("AUC")

p_hic1

p_tgfb

p_trm
```

 
{{< lightbox src="images/07_plots-2.png" caption="TGFb score" >}} 
{{< lightbox src="images/07_plots-3.png" caption="TRM score" >}} 

## Differential expression

### For gene expression

```r
summed <- aggregateAcrossCells(sce, 
                               id=colData(sce)[,c("singleR_labels2", "Location", "Patient_ID")],
                               use.altexps=FALSE)




summed


# workflow form https://bioconductor.org/books/release/OSCA/multi-sample-comparisons.html#creating-pseudo-bulk-samples
# But i do not remove the low abundance genes as this would filter out HIC1
DEGenesWithoutAbundanceFilter <- function(summed, subset, contrasts=c("LocationIntestine", "LocationRectum")) {
  current <- summed[,subset==summed$singleR_labels2]
    # Creating up a DGEList object for use in edgeR:
  library(edgeR)
  y <- DGEList(counts(current), samples=colData(current))
  y
  discarded <- current$ncells < 10
  y <- y[,!discarded]
  keep <- filterByExpr(y, group=current$Location)
  #y <- y[keep,]  # we loose HIC1 here
  
  y <- calcNormFactors(y)

  design <- model.matrix(~Patient_ID + Location, y$samples)
  y <- estimateDisp(y, design)
  fit <- glmQLFit(y, design, robust=TRUE)

  df <- data.frame(
        Symbol = rowData(summed)$Symbol,
        Ensembl = rownames(summed),
        Subset = subset
  )

  for(c in contrasts)
  {
        res <- glmQLFTest(fit, coef=c)
        df[[c]] <- as.data.frame(topTags(res, n=Inf, sort.by = "none"))$FDR
  }
  #res <- glmQLFTest(fit, coef=contrasts)
  #summary(decideTests(res))
  
  #df <- topTags(res, n=Inf)
  #df$Symbol <- rowData(summed)$Symbol
  df
}

pval_cd4 <- DEGenesWithoutAbundanceFilter(summed, "CD4+ T cells")
pval_cd8 <- DEGenesWithoutAbundanceFilter(summed, "CD8+ T cells")
pval_other_Tcells <- DEGenesWithoutAbundanceFilter(summed, "other T cells")
``` 

### For AUC score

```r
summed_auc <- aggregateAcrossCells(SingleCellExperiment(list(counts = scores),
                                                                                                                colData = colData(sce)), 
                               id=colData(sce)[,c("singleR_labels2", "Location", "Patient_ID")],
                               statistics="mean",
                               use.altexps=FALSE)

# function to calc p values using limma
DEAucLimma <- function(summed, subset, contrasts = c("LocationIntestine", "LocationRectum")) {
  library(limma)
  current <- summed[,subset==summed$singleR_labels2]
  design <- model.matrix(~Patient_ID + Location, colData(current))
  #message(colnames(design))
    
  #plot(plotExpression(current, rownames(current), x="Location", exprs_values="counts"))
  
  df <- data.frame(
        GeneList = rownames(current) ,
        Subset = subset
  )
  for(c in contrasts)
  {
        fit <- lmFit(counts(current), design = design)
         fit <- contrasts.fit(fit, coefficients = c)
         fit <- eBayes(fit)
         tt <- topTable(fit, number=Inf, sort.by="none")
         df[[c]] <- as.data.frame(tt)$adj.P.Val
  }
  df
}


pvals_auc_cd4 <- DEAucLimma(summed = summed_auc, subset = "CD4+ T cells")
pvals_auc_cd8 <- DEAucLimma(summed = summed_auc, subset = "CD8+ T cells")
pvals_auc_otherTcells <-DEAucLimma(summed = summed_auc, subset = "other T cells")
```

## Plots with p-values

```r
library(dplyr)

# make a df with the pvalues that can be added to the plot
pvals_hic1 <- rbind(
  pval_cd4[pval_cd4$Symbol == "HIC1", ],
  pval_cd8[pval_cd8$Symbol == "HIC1", ],
  pval_other_Tcells[pval_other_Tcells$Symbol == "HIC1", ]
) %>%
  tidyr::pivot_longer(cols = c(LocationIntestine, LocationRectum),
                      names_to = "coef",
                      values_to = "p.adj") %>%
  mutate(group1 = "PBMC",
         group2 = base::gsub("Location", "", coef),
         singleR_labels2 = Subset,
         y.position = rep(max(p_hic1$data$Y) * c(1.05, 1.15), 3),
         label = signif(p.adj, digits=3))



# add to plot
p_hic1_pval <- p_hic1 + ggprism::add_pvalue(pvals_hic1)


# make a df with the pvalues that can be added to the plot
pvals_trm <- rbind(
  pvals_auc_cd4[pvals_auc_cd4$GeneList == "TRM", ],
  pvals_auc_cd8[pvals_auc_cd8$GeneList == "TRM", ],
  pvals_auc_otherTcells[pvals_auc_otherTcells$GeneList == "TRM", ]
) %>%
  tidyr::pivot_longer(cols = c(LocationIntestine, LocationRectum),
                      names_to = "coef",
                      values_to = "p.adj") %>%
  mutate(group1 = "PBMC",
         group2 = base::gsub("Location", "", coef),
         singleR_labels2 = Subset,
         y.position = rep(max(p_trm$data$Y) * c(1.05, 1.15), 3),
         label = signif(p.adj, digits=3))

# add to plot
p_trm_pval <- p_trm + ggprism::add_pvalue(pvals_trm)

# make a df with the pvalues that can be added to the plot
pvals_tgfb <- rbind(
  pvals_auc_cd4[pvals_auc_cd4$GeneList == "TGFb", ],
  pvals_auc_cd8[pvals_auc_cd8$GeneList == "TGFb", ],
  pvals_auc_otherTcells[pvals_auc_otherTcells$GeneList == "TGFb", ]
) %>%
  tidyr::pivot_longer(cols = c(LocationIntestine, LocationRectum),
                      names_to = "coef",
                      values_to = "p.adj") %>%
  mutate(group1 = "PBMC",
         group2 = base::gsub("Location", "", coef),
         singleR_labels2 = Subset,
         y.position = rep(max(p_tgfb$data$Y) * c(1.05, 1.15), 3),
         label = signif(p.adj, digits=3))

# add to plot
p_tgfb_pval <- p_tgfb + ggprism::add_pvalue(pvals_tgfb)


p <- p_hic1_pval / p_tgfb_pval / p_trm_pval & plot_layout(guides = "collect") & ggthemes::theme_few() & theme(legend.position = "none") &
          scale_y_continuous(expand = expansion(mult = c(0, .1)))

#  p

ggsave(filename = "tscc/plot_hic1_tgfb_trm_with_pvals.png",
       plot = p,
       width = 8,
       height = 12)
```
{{< lightbox src="images/plot_hic1_tgfb_trm_with_pvals.png" caption="Final plot" >}} 

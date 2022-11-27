---
weight: 2
title: "Perpare the input"
--- 

# Perpare the input: Creating the input files for pySCENIC

In this part we will create the input files for pySCENIC using scanpy. Ultimately, this results in a loom file, that we use as a starting point for the pySCENIC pipeline.

You can use either a jupyter nootbook (run `jupyter lab`) or visual studie code to run the code. 

## Load the requires libraries


```python
import anndata
from os import listdir
import pandas as pd
import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pyscenic
import loompy as lp
import re
```

## Create the anndata object

Here, we import the cellranger output and create an `anndata` object. For that, I created a small helper function, that loads multiple mtx files and combines them in a single `anndata` object.

The function assumes a folder called `datasets` with the following structure:


    └── ty
        ├── Blood 1
        │   ├── barcodes.tsv.gz
        │   ├── features.tsv.gz
        │   └── matrix.mtx.gz
        ├── Blood 2
        │   ├── barcodes.tsv.gz
        │   ├── features.tsv.gz
        │   └── matrix.mtx.gz
        ├── Blood 3
        │   ├── barcodes.tsv.gz
        │   ├── features.tsv.gz
        │   └── matrix.mtx.gz
        ├── Fat 1
        │   ├── barcodes.tsv.gz
        │   ├── features.tsv.gz
        │   └── matrix.mtx.gz
        ├── Fat 2
        │   ├── barcodes.tsv.gz
        │   ├── features.tsv.gz
        │   └── matrix.mtx.gz
        ├── Fat 3
        │   ├── barcodes.tsv.gz
        │   ├── features.tsv.gz
        │   └── matrix.mtx.gz
        ...


We can then load all samples in the subfolder `ty` by running `load_dataset(dataset = 'ty')`.

```python
# Function to load the dataset
def load_dataset(dataset):
    # List as folder (=samples) in dataset
    samples = listdir(path = 'datasets/' + dataset + '/')
    samples = ['datasets/' + dataset + '/' + s for s in samples]
    # Read in all Samples
    # This takes up to two minutes....
    adata = [sc.read_10x_mtx(path = s, cache=True)  for s in samples]
    # Merge them
    adata = adata[0].concatenate(adata[1:])
    # Create further annotation
    # add back the samples name
    adata.obs['sample'] = adata.obs['batch'].apply(lambda x: samples[int(x)])
    # extract the tissue from the sample name
    adata.obs['tissue'] = adata.obs['sample'].apply(lambda x: re.findall(r"(\w+)[ 0-9]{0,2}$", x)[0])
    # add the datsset
    adata.obs['dataset'] = dataset
    return adata


# load the dataset
adata = load_dataset(dataset = 'ty')
```

As a results, you get a anndata object with all the samples. Here we have 52463 cells and 27463 genes.

```python
adata
```
    AnnData object with n_obs × n_vars = 52463 × 27998
        obs: 'batch', 'sample', 'tissue', 'dataset'
        var: 'gene_ids', 'feature_types'



## Preprocessing


```python
# set options for scanpy
sc.settings.verbosity = 3             # verbosity: errors (0), warnings (1), info (2), hints (3)
sc.logging.print_header()
sc.settings.set_figure_params(dpi=120, facecolor='white')
```

    scanpy==1.8.2 anndata==0.7.8 umap==0.5.2 numpy==1.21.5 scipy==1.7.3 pandas==1.3.5 scikit-learn==1.0.2 statsmodels==0.13.2 python-igraph==0.9.9 pynndescent==0.5.6



```python
# plot the highest expressed genes
sc.pl.highest_expr_genes(adata, n_top=20, )
```

    normalizing counts per cell
        finished (0:00:00)



    
{{< lightbox src="pySCENIC_part1_6_1.png" caption="highest expressed genes" >}} 


### Basic filtering


```python
# Basic filtering:
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
```

    filtered out 3921 cells that have less than 200 genes expressed
    filtered out 11596 genes that are detected in less than 3 cells


Now, we have an `anndata` object with 48542 cells and 16402 genes

```python
adata
```




    AnnData object with n_obs × n_vars = 48542 × 16402
        obs: 'batch', 'sample', 'tissue', 'dataset', 'n_genes'
        var: 'gene_ids', 'feature_types', 'n_cells'



### Basic QC


```python
# Let’s assemble some information about mitochondrial genes, which are important for quality control.
adata.var['mt'] = adata.var_names.str.startswith('mt-')  # annotate the group of mitochondrial genes as 'mt'
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
             jitter=0.4, multi_panel=True)
sc.pl.scatter(adata, x='total_counts', y='pct_counts_mt')
sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts')
```

{{< lightbox src="pySCENIC_part1_11_1.png" caption="Violin plot of nGenes, nUMI and pctMito" >}} 
{{< lightbox src="pySCENIC_part1_11_2.png" caption="Scatter nUMI vs pctMito" >}} 
{{< lightbox src="pySCENIC_part1_11_3.png" caption="Scatter nUMI vs nGenes" >}} 

    
We use this plots to set cutoffs of the maximal number of genes (anything above that might be doubltes) and the maximal percentage of allowed mitochrondial genes.

```python
# Do the filtering
adata = adata[adata.obs.n_genes_by_counts < 3000, :]
adata = adata[adata.obs.pct_counts_mt < 12, :]
```

Again, we have reduced the size of our object a little bit.

```python
adata
```

    View of AnnData object with n_obs × n_vars = 47399 × 16402
        obs: 'batch', 'sample', 'tissue', 'dataset', 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mt', 'pct_counts_mt'
        var: 'gene_ids', 'feature_types', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'



#### Save loom file

We save our filtered `anndata` object with the raw counts as a `loom` file. We use this as the input for the pySCENIC platform. 

```python
# create basic row and column attributes for the loom file:
row_attrs = {
    "Gene": np.array(adata.var_names) ,
}
col_attrs = {
    "CellID": np.array(adata.obs_names) ,
    "nGene": np.array( np.sum(adata.X.transpose()>0 , axis=0)).flatten() ,
    "nUMI": np.array( np.sum(adata.X.transpose() , axis=0)).flatten() ,
    "tissue": np.array(adata.obs['tissue'])
}
# Only create this once
lp.create( 'pySCENIC_input.loom', adata.X.transpose(), row_attrs, col_attrs)
```

### Normalization

We continue following the basic 10x PBMC tutorial from `scanpy` the normalize the counts and create a clustering and dimenstional reductions. This will be used for further visualizations of the pySCENIC results.


```python
# Save counts in a new layer
adata.layers['counts'] = adata.X
# Total-count normalize (library-size correct) the data matrix X to 10,000 reads per cell, so that counts become comparable among cells.
sc.pp.normalize_total(adata, target_sum=1e4)
# Logarithmize the data:
sc.pp.log1p(adata)
```

    normalizing counts per cell
        finished (0:00:00)




```python
# save log counts to a layer
# this is not really needed, but can be helpful if you do further analysis or run MAGIC on the dataset
adata.layers['logcounts'] = adata.X
```

### HVG

Select the highly variable genes that will be used for PCA and UMAPs.

```python
# Identify highly variable genes
# use the dataset as batchkey
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
sc.pl.highly_variable_genes(adata)
```

    extracting highly variable genes
        finished (0:00:01)
    --> added
        'highly_variable', boolean vector (adata.var)
        'means', float vector (adata.var)
        'dispersions', float vector (adata.var)
        'dispersions_norm', float vector (adata.var)


{{< lightbox src="pySCENIC_part1_22_1.png" caption="highly variable genes" >}} 
    


## Dimensional reduction

Calculate a PCA

```python
# Principal component analysis
sc.tl.pca(adata, svd_solver='arpack')
sc.pl.pca(adata, color='tissue')
```

    computing PCA
        on highly variable genes
        with n_comps=50
        finished (0:00:05)



{{< lightbox src="pySCENIC_part1_25_1.png" caption="PCA plot coloured by tissue" >}}     
  

```python
# Let us inspect the contribution of single PCs to the total variance in the data. 
# This gives us information about how many PCs we should consider in order to compute 
# the neighborhood relations of cells, e.g. used in the clustering function sc.tl.louvain()
# or tSNE sc.tl.tsne(). In our experience, often a rough estimate of the number of PCs does fine.

sc.pl.pca_variance_ratio(adata, log=True)
```

{{< lightbox src="pySCENIC_part1_26_0.png" caption="PCA variance ratio" >}}   
    

Create the neighborhood graph

```python
sc.pp.neighbors(adata)
```

    computing neighbors
        using 'X_pca' with n_pcs = 50
        finished: added to `.uns['neighbors']`
        `.obsp['distances']`, distances for each pair of neighbors
        `.obsp['connectivities']`, weighted adjacency matrix (0:00:07)


Identify clusters using the leiden algorithm. 

```python
# Clustering the neighborhood graph
sc.tl.leiden(adata)
```

    running Leiden clustering
        finished: found 10 clusters and added
        'leiden', the cluster labels (adata.obs, categorical) (0:00:14)


Calculate the UMAP

```python
# Create a UMAP
sc.tl.umap(adata)
```

    computing UMAP
        finished: added
        'X_umap', UMAP coordinates (adata.obsm) (0:00:21)

Plot the umap

```python
sc.pl.umap(adata, color=['dataset', 'tissue', 'leiden'])
```

{{< lightbox src="pySCENIC_part1_30_0.png" caption="UMAP plots" >}}     
    
 
And lastly, let's also create the TSNE dimensional reduction.

```python
sc.tl.tsne(adata)
```

    computing tSNE
        using 'X_pca' with n_pcs = 50
        using sklearn.manifold.TSNE
        finished: added
        'X_tsne', tSNE coordinates (adata.obsm) (0:02:44)



```python
sc.pl.tsne(adata, color=['dataset', 'tissue', 'leiden'])
```

{{< lightbox src="pySCENIC_part1_32_0.png" caption="TNSE plots" >}}     
    
   


### Save Anndata

Save the `anndata` object

```python
adata.write_h5ad('pyscenic.h5ad')
```

And again, let's have a look what is in there.

```python
adata
```




    AnnData object with n_obs × n_vars = 47399 × 16402
        obs: 'batch', 'sample', 'tissue', 'dataset', 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mt', 'pct_counts_mt', 'leiden'
        var: 'gene_ids', 'feature_types', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
        uns: 'log1p', 'hvg', 'pca', 'tissue_colors', 'neighbors', 'leiden', 'umap', 'dataset_colors', 'leiden_colors', 'tsne'
        obsm: 'X_pca', 'X_umap', 'X_tsne'
        varm: 'PCs'
        layers: 'counts', 'logcounts'
        obsp: 'distances', 'connectivities'


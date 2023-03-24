# Single cell aging clocks

## Introduction

Age prediction by various clocks is a highly discussed topic in the developing field of aging research. There is a high variety in the choice of age predictor marker from simple procedures like blood testing to more complex like DNA methylation levels. This opened the possibility of measuring the age of not only a whole organism but the age at cellular level, giving tools for research of events like induced reprogramming and age profiling of tissues.

At cellular level most clocks are based on methylation levels of CpG sites associated with aging since these provide relatively reliable data and good predictions. Another potential source of  single cell analysis is RNAseq. It provides a little bit different type of information and requires more preprocessing and normalization compared to methylation data.
Here we present a novel algorithm for transcriptomic data, based on previous studies of this approach on methylation data. 


## Methods

We utilized two significantly different types of transcriptomic data - bulk and single-cell data (scRNAseq). Bulk data provides an “average” view of the cell and loses a significant part of the vital part of innate heterogeneity present in the cells but is pretty easy to analyze compared to scRNAseq. There are clear challenges with sc data, as sparsity. 

## Results

Plots provide information on the performance of this algorithm, each dot is the sample for which predicted age was calculated (Y-axis). Each plot corresponds to the way of choosing genes for clock fitting. For instance, top 500 or 1000 genes means that only 500 or 1000 genes with highest R coefficient (meaning that these genes correlate with age) were used for clocks training.

For bulk predictions on bulk training and corresponding other models metrics: 

```{figure} figs/bulk_bulk.png
:name: bulk_bulk
Bulk data on bulk reference.
```
For single cell predictions on bulk training and corresponding other models metrics: 

```{figure} figs/single_bulk.png
:name: single_bulk
Single cell data on bulk reference.
```
For single cell predictions on single cell training and corresponding other models metrics: 

```{figure} figs/single_single.png
:name: single_single
Single cell data on single cell reference.
```

Detailed explanation of cinfidence interval estimation is provided in notebook.

## Discussion

Comparison of the novel approach with existing algorithms reveals interesting insights.

The performance of the novel algorithm appears to be satisfying only in case bulk data predicted and bulk data was used for model training. We assume that all points should be on a dotted line, showing no difference between predicted and true age. 

If the model is trained on bulk reference and single cell data is used for predictions, we see a dramatic decrease of R coefficient and median absolute error (MedAE). We assume that clocks at this modification can not be used. This might be connected with the quality of the dataset or hidden effects of data preparation (any difference due to the single cell or bulk data). 

Single cell predictions by single cell trained clocks as well performed not satisfactory. Existing models also showed not good enough metrics. It is obviously from the distribution of points on plots.We also could link it either with the algorithm itself, or with dataset quality (number of time points). 

We expect to improve the performance by doing some data preparation steps between model training: maybe results will be better if we exclude the majority of genes leaving only the most important ones, or insert some values instead of zeros. 

## Credits
This text prepared by [Anastasia Bolshakova](https://www.linkedin.com/in/anastasia-kuzoyatova), Evgeniy Efimov, Timothy Torokhov. 


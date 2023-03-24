# Meta-analysis of aging transcriptomes

All code for tasks described in this report is avaliable in our <a href="https://github.com/d-kozhevnikova/Ageing-transcriptome-meta-analysis/blob/main/AgeingTranscriptionMetaRegression.ipynb">Jupyter Notebook</a>.

## Introduction

In this project, we reproduce the results of a gene expression meta-analysis performed by <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7906136/">Daniel Palmer and colleagues in 2021</a>. In this study transcriptomic signatures associate with ageing were identified for brain, heart and muscle tissues based on the analysis of 127 publicly-available microarray and RNA-Seq datasets from mice, rats, and humans.<br>
Overall, changes in gene expression with age followed the following patterns:
<ul>
  <li>overexpression of immune and stress response genes with age</li>
  <li>underexpression of metabolic and developmental genes</li>
</ul>
In muscle and heart tissues genes involved in cell response processes were found to be activated. It was also found that genes differentially expressed with age were mainly central for protein-protein interaction networks. Previously in the <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732303/">paper from 2009</a> by the same authors similar common ageing gene signatures were identified such as:
<ul>
  <li>overexpression of inflammation, immune response and lysosomes related genes</li>
  <li>underexpression of collagen, energy metabolism (especiallu mitochondrial) genes</li>
  <li>changes in expression of apoptosis genes and cell cycle regulation genes</li>
</ul>
Finally, it was found that genes differentially expressed with age are rarely tissue-specific but rather are commonly expressed in multiple tissues.<br>
The outline of analysis pipeline from the original study is the following:
<ol>
<li>Linear regression performed for each gene inside each dataset. The slope of the regression corresponds to the direction in change of gene expression with age (if positive - gene is upregulated with age and vice versa)</li>
<li>Genes for which regression slope is statistically significant are selected</li>
<li>Meta regression analysis was performed with <i>Cumulative Binomial test</i></li>
<li>False discovery rate correction was performed by permutating gene IDs in the original dataset and repeating the meta-regression analysis. Based on this an average percentage of statistically significantly differentially expressed genes was identified - this allowed calculating critical p-value at which FDR was less than 0.05</li>
<li>Tissue specificity analysis was run with <i>tau</i> index used as a measure of tissue specificity</li>
<li>Differentially expressed genes (DEGs) that had evidence of association with age across multiple datasets were selected for further analysis</li>
<li>Enrichment analysis with David and topGO R tool was performed</li>
</ol>
As additional steps authors also performed:
<ul>
<li>dN/dS analysis - ratio of non-synonymous to synonymous substitutions in the sequences of main DEGs in different species. These calculations showed that those genes are predominantly evolutionary conserved across species</li>
<li>Random Forest ML model on GO terms was built to identify the GO terms that can best predict whether a particular gene will be over- or underexpressed with age</li>
</ul>
<hr>

### Weak points of the paper

To detect DEGs that were differentially expressed across multiple datasets, the authors used the cumulative binomial test. In cases where the total dataset number is small (in which the gene was studied), such meta-regression tests are not statistically significant because they don't reflect the effect size. Additionally, two different data types are explored, RNA-seq and microarray RNA sequencing, which might require additional correction for the specific details of experimental techniques.

### Suggestions for approach improvements

In our project we applied meta-regression using the <a href="https://pymare.readthedocs.io">PyMare</a> package for a higher specificity of the analysis. In this approach we did not select the statistically significant sloped inside each dataset but rather gave all the genes in each dataset as input to the meta-regression analyzer. PyMare itself estimates which of the slope estimates are statistically significant acorss multiple datasets based on:
<ul>
  <li>list of slope coefficients for eacg dataset</li>
  <li>list of variances for these slopes</li>
  <li>list of samples numbers for each dataset</li>
</ul>
<hr>

## Results

### Preprocessing of the gene expression data

For the sake of time we decided to focus our analysis on brain, heart, and muscle tissues from mice only. From the data avaliable on the [github repository](https://github.com/maglab/AgeingSignatures2020_supplementary) we selected 27 mice microarray datasets originated from brain, heart and muscle (12 samples for brain, 5 for heart and 10 for muscle). Each dataset contains samples from mice of several age groups (usually several individuals inside each group). For each of these samples expression levels of around 20000 genes are studied.

#### Quality control - PCA

To explore the similarity of the samples within each dataset and each age group we applied the Principal Component Analysis (PCA) method of data clustering. The samples from different ages were, however, intermingled with each other so it was impossible to remove some samples due to out-clustering.

#### Statistical testing

To estimate differencially expressed genes (DEGs) we conducted **linear regression** analysis for all the datasets using <a href="https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html">statsmodels.OLS</a> python function. The regression equation was as following:

$$Y_{ij} = \beta_{0j} + \beta_{1j}Age{i} + \epsilon_{ij}$$

Where Y is the expression of of gene <i>j</i> in sample <i>i</i>, <i>β<sub>0j</sub></i> is the intercept for gene <i>j</i>, <i>β<sub>1j</sub></i> is the regression slope for gene <i>j</i>, Age<sub>i</sub> is the age of the indidividual studies in the sample, and <i>ε<sub>ij</sub></i> is the error term.<br>The slope of this regression identifies the direction of differencial expression with age. 0.05 <i>p-value</i> cut-off was then used to identify the significance of the coefficients (used only for binomial testing) and the coefficients variances were calculated using the same package (used ofr PyMare meta-regression). 
<hr>

### Meta-analysis of the datasets
To identify genes differentially expressed in tissue across all datasets we applied **meta-regression** function from the **PyMare** package. This function takes as input the estimated regression coefficients for individual datasets and the variances for these coefficients as well as dataset sizes. It produces weighted estimates for gene expression change direction with age(called **total effect**), taking into account the level of uncertainty, and number of datasets analyzed.<br>
We conducted such analysis for each of the tissues as well as for all three tissues together. In the latter case we also passed the tissue parameters as extra cofounder parameter.
### GO enrichment analysis
Gene Onthology enrichment analysis was done with **gseapy** python package to identify functional categories for the obtained DEGs. In the genes overexpressed with age across multiple datasets in the brain, the enrichment terms are the following:

```{figure} figs/Enrich_terms_over_brain.jpg
Enrichment terms in the brain overexpressed genes.
```
  
In the muscle overexpressed genes with age, the picture is the following:

```{figure} figs/Enrich_terms_over_muscle.jpg
Enrichment terms in the muscle overexpressed genes.
```

For heart overexpressed genes:

```{figure} figs/Enrich_terms_over_heart.jpg
Enrichment terms in the heart overexpressed genes.
```
  
For heart underexpressed:

```{figure} figs/Enrich_terms_under_heart.jpg
Enrichment terms in the heart underexpressed genes.
```  

Enriched terms in the genes differentially overexpressed with age across multiple datasets in all three tissues are:

```{figure} figs/Enrich_terms_over_allthetissues.jpg
Enrichment terms overexpressed genes in all tissues.
```  

While for underexpressed:

```{figure} figs/Enrich_terms_under_allthetissues.jpg
Enrichment terms underexpressed genes in all tissues.
```  


### Gene expression comparison in Brain, Heart and Muscle

#### Upregulated and Downregulated genes common between Brain, Heart and Muscle:
We carried out intersection analysis of Upregulated and Downregulated genes that are common between all three tissues. Five genes (**ACER2, RHPN2, CD2AP, RRAGC, SKAP2**) were overexpressed whereas four genes (**CRB3, HOXD12, UBN1, SLC6A3**) were underexpressed in Brain, Heart and Muscle.

#### Upregulated genes: 
Description of common upregulated genes in Brain, Heart and Muscle tissues
  **1. ACER2**: may lead to changes in the metabolism of ceramide and other lipid molecules
  
  **2. RHPN2**: may affect cell adhesion, migration, and signaling, which could impact various physiological and pathological processes
  
  **3. CD2AP**: may disrupt the structure and function of the glomerular filtration barrier in the kidney, leading to proteinuria, inflammation, and progressive kidney damage.
  
  **4. RRAGC**: may affect the activity of the mTORC1 signaling pathway, which plays a key role in regulating cell growth, autophagy, and metabolism
  
  **5. SKAP2**: Differential expression of SKAP2 may influence T-cell activation and migration, which are essential for immune surveillance and defense against infections and cancer

```{figure} figs/upregulated_genes_intersection.png
Upregulated genes intersection in all tissues.
```  

#### Downregulated genes:
Description of common upregulated genes in Brain, Heart and Muscle tissues
  
  **1. CRB3**: encodes a protein that is important for maintaining the structure and function of epithelial cells
  
  **2. HOXD12**: member of the homeobox gene family that is involved in regulating embryonic development and differentiation
  
  **3. UBN1**: involved in chromatin remodeling, which is important for regulating gene expression. 
  
  **4. SLC6A3**: encodes a dopamine transporter protein that is involved in the regulation of dopamine signaling in the brain

```{figure} figs/downregulated_genes_intersection.png
Downregulated genes intersection in all tissues.
```  

### GenAge intersection analysis

From GenAge database we have downloaded the genes associated with age. The set of genes were intersected with Upregulated and Downregulated genes (from the anlaysis of three tissues all together) identified in our study. 

#### Upregulated genes intersection with GenAge:
In the upregulated set of genes seven genes were reported in GenAge. 

  **1. EFEMP1**: encodes a protein that is involved in cell adhesion and signaling
  
  **2. TRP53BP1**: This gene is involved in the DNA damage response and plays a role in maintaining genomic stability
  
  **3. PAWR**: involved in the regulation of apoptosis (programmed cell death) and has been implicated in various physiological and pathological processes, including cancer and neurodegeneration 
  
  **4. CDKN1A**: This gene encodes a protein called p21, which is a key regulator of cell cycle progression and DNA damage response 
  
  **5. GRN**: encodes a protein called progranulin, which is involved in various physiological processes, including inflammation, wound healing, and neuronal development 
  
  **6. GPX4**: encodes an enzyme called glutathione peroxidase 4, which plays a critical role in protecting cells from oxidative stress 
  
  **7. HNRNPD**: This gene encodes a protein called heterogeneous nuclear ribonucleoprotein D, which is involved in RNA processing and gene expression regulation

```{figure} figs/Genage_intersection_with_upregulated_genes.png
Genage intersection with upregulated genes in all tissues.
```  


#### Downregulated genes intersectio with GenAge:
Incase of downregulated genes only three genes were reported in GenAge database.

  **1. POU1F1 (Pit-1)**: a transcription factor that plays a critical role in the development and function of the pituitary gland

  **2. FOXM1**: a transcription factor that regulates the expression of genes involved in cell cycle progression, DNA replication, and repair

  **3. NUDT1 (nucleoside diphosphate-linked moiety X motif 1)**: an enzyme involved in nucleotide metabolism and DNA damage response


```{figure} figs/Genage_intersection_with_downregulated_genes.png
Genage intersection with downregulated genes in all tissues.
```  


## Discussion

### The list of differentially expressed genes across aging

According to the results of <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7906136/">2021 original paper</a> all tissues and every tissue studied consistently overexpressed the following genes:

```{figure} figs/Palmer_table_overexpressed.jpg
Table of the top-5 genes most consistently overexpressed with age across datasets for all tissues and for each tissue studied (`palmer2021ageing`).
```  
  
And for underexpressed genes the results are the following:

```{figure} figs/Palmer_table_underexpressed.jpg
Table of the top-5 genes most consistently underexpressed with age across datasets for all tissues and for each tissue studied (`palmer2021ageing`).
```  

According to our findings, immune system activation genes were overexpressed in the brain. Differentiation-related genes were overexpressed in muscles, potentially resulting in a decrease of regeneration activity and muscle tissue deterioration in ageing people. An increase in GABA signaling and ion transport was observed in the heart. All tissues collectively exhibit an increase in the activity of immune and proteilytic genes, while metabolic genes are down-regulated. The described results are in line with the conclusions made in the <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7906136/">original paper</a>. 


## Credits

THis repository was created by Andrey Stapran (MSc 2nd year LS), Shahzeb Khan (MSc 2nd year LS) and Daria Kozhevnikova (MSc 1st year LS) as part of a final project for **Computational Biology of Aging** course taught by **Professor Ekaterina Khrameeva** at Skolkovo Institute of Science and Technology, Moscow

## References

1. Palmer, Daniel et al. “Ageing transcriptome meta-analysis reveals similarities and differences between key mammalian tissues.” Aging vol. 13,3 (2021): 3313-3341. doi:10.18632/aging.202648

2. de Magalhães, João Pedro et al. “Meta-analysis of age-related gene expression profiles identifies common signatures of aging.” Bioinformatics (Oxford, England) vol. 25,7 (2009): 875-81. doi:10.1093/bioinformatics/btp073



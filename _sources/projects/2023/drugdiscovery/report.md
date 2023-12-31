#  Transcriptomics-based longevity drug discovery


This project aims to reproduce treatment-screening procedure developed by Georges Janssens et al. {cite}`janssens2019transcriptomics`. 

## Background

Aging is associated human morbidity and mortality and there are no way to revert it. However, scientists search for treatments that can slow down aging. One of the approaches was proposed by Georges Janssens et al. in 2019 {cite}`janssens2019transcriptomics`. Authors used two transcriptomics datasets:

1. Their own age-stratified RNA-seq data **(transcriptome ~ age)**
2. Connectivity Map (CMap) public data **(transcriptome ~ treatment)**

The key idea is to find treatments that lead to a "younger" transcriptome.

```{figure} images/analysis_schema.png
---
width: 90%
name: analysis_schema
---
The overall schema of transcriptome-based treatments selections
```


Authors found several candidate treatments and specifically discuss some of them. For instance, they hightlight tanespimycin and monodren involved in Hsp90 inhibition pathways. Hsp90 inhibition was discussed as a process that may be a potential target in developing anti-aging interventions. Janssens et al. also performend *in vivo* experiments in *C. elegans* that support their findings. 

## Materials and methods

All data processing was performed using R v.4.2.3 with tidyverse v.2.0.0 and python v.3.11.6 with pandas v.2.1.2.

**GTEx dataset preprocessing**

Age-stratified RNA-seq data (GTEx dataset) was downloaded from the [GTEx portal](https://gtexportal.org/home/downloads/adult-gtex/overview) ("[Bulk tissue expression](https://gtexportal.org/home/downloads/adult-gtex/bulk_tissue_expression)" section). We used already preprocessed gene [RPKM data](https://storage.cloud.google.com/adult-gtex/bulk-gex/v6p/rna-seq/GTEx_Analysis_v6p_RNA-seq_RNA-SeQCv1.1.8_gene_rpkm.gct.gz) from the  GTEx Analysis V6p release. We also obtained metadata description from the "[Metadata](https://gtexportal.org/home/downloads/adult-gtex/metadata)" section (GTEx Analysis V6p Sample Attributes and Subject Phenotypes). Both annotation files were joined on sample IDs to get combined metadata. Samples were annotated as "young" for ages 20-59 years old and "old" for 60-69 years old.

Based on the metadata, GTEx dataset was divided into several parts based on tissue, age and gender parameters. For the further analysis only brain, heart, kidney, liver and stomach data was selected in order to reduce computational time. Also, for all of the subsets, we retained only transcripts present in both GTEx and CMap datasets (based on the transcript IDs). We also revomed low abundant transcripts with RPKM values less than 0.1 in at least 80% of samples. Additional filtering was applied to keep transcripts with RNA integrity number greater or equal to 6. Resulting transcripts were added a pseudocount and log2-transformed. Then we performed differential expression analysis between "young" and "old" samples. Only differentialy expressed transcripts with *p-value* less then 0.01 were selected for the further analysis.



**CMap dataset preprocessing**

Connectivity (CMap) dataset was kindly provided by Dmitrii Kriukov. Control group of CMap dataset was aggregated by cell type to compute cell-wise means. After that we computed log2(Fold Change) values for each treatment with respect to the corresponding cell-wise control.  


**Transcriptom-based treatment selection**

Transcriptom-based treatment selection using machine learning was performed in R v.4.2.3 with caret v.6.0-94, randomForest v.4.7-1.1, ROCR v.1.0-11, tidyverse v.2.0.0, matrixStats v.1.2.0.

Firstly, we built RandomForest model to predict age category ("young" / "old") based on the preprocessed GTEx transcriptomics data. We built different models for different tissues and selected those with AUC score greater then 0.75 (based on 10-fold cross-validation). 

Secondly, we used selected models to find geroproctive treatments. We obtained "middle-aged" transcriptome by averaging "young" and "old" GTEx data. Then we multiplied this "middle-aged" values by the corresping fold changes from the CMap dataset, wich resulted us "drug-induced" transcriptome. Then we made age predictions based on our drug-indiced transcriptome and selected those for which "young"-age probability was higher then for the "old"-ade. We also calculated geroprotective index (GI) by normalization and centering probabilities of "young" age class (PY):

$$ GI = \frac{PY}{0.5} - \overline{\frac{PY}{0.5}} $$

The results were visualised in python v.3.11.6 with pandas v.2.1.2, matplotlib v.3.8.0 and seaborn v.0.13.0. 



## Results

We built 5 transcriptome-based age prediction models for each of the selected organs (brain, heart, kidney, liver and stomach). They were applied to the 100 randomly selected treatments and only brain model resulted in one geroprotective compound - L-ergothioneine. Then we used brain model as a more promising one and applied it to all 3546 treatment in the CMap dataset. 


```{figure} images/treatments_hist.png
:name: treatments_hist
 Geroprotective index distributions of all treatments. *Black line* depicts selection threshold in the original paper (however authors also used some ranking procedure)), *red line* represents our threshold (probability of "young" age is equal to 0.5). 
```

Only 11 compounds were found to show geroprotective results: olanzapine, XL-888, ritonavir, thioguanine, L-ergothioneine, nafamostat , ochratoxin-a, etofylline-clofibrate, tebipenem , E-2012, EMF-sumo1-7. Among them, **thioguanine showed the most geroprotective index (0.0815)**, and the olanzapine, XL-888, ritonavir had the secong highest GI (0.0740). L-ergothioneine had the third highest GI (0.0670), but we see this molecule as the most promising as it was present in the results of several analyses. 

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}he chemical struc
.tg td{border-bottom-width:1px;border-color:black;border-style:solid;border-top-width:1px;border-width:0px;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-bottom-width:1px;border-color:black;border-style:solid;border-top-width:1px;border-width:0px;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-2dfk{background-color:#ecf4ff;border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-ck6w{background-color:#ecf4ff;border-color:inherit;font-size:medium;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-o36v{background-color:#ecf4ff;border-color:inherit;font-size:medium;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ck6w" colspan="2">Probability</th>
    <th class="tg-o36v" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000">Treatment</span></th>
    <th class="tg-o36v" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000">Geroprotective Index</span></th>
  </tr>
  <tr>
    <th class="tg-2dfk">"Old"</th>
    <th class="tg-2dfk">"Young"</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.498</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.502</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">EMF-sumo1-7</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0656</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.496</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.504</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ochratoxin-a</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0670</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.498</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.502</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nafamostat</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0656</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">0.496</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">0.504</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">L-ergothioneine</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">0.0670</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.494</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.506</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">olanzapine</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0740</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.494</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.506</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">XL-888</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0740</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.498</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.502</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">E-2012</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0656</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.494</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.506</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ritonavir</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0740</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.49</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.51</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">thioguanine</span></td>
    <td class="tg-c3ow"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0815</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.498</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.502</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">tebipenem</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0656</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.496</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.504</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">etofylline-clofibrate</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0670</span></td>
  </tr>
</tbody>
</table>

## Discussion

In this project, we built a Random Forest model for the age classification of transcriptomic data and applied it to find potential anti-ageing treatments. Our model identified 11 compounds that could potentially be geroprotective. However, high machine learning metrics are not a sufficient condition for the quality of the results. To validate the results, we additionally analysed candidate molecules. We selected the top 4 molecules according to the geroprotective index (thioguanine, olanzapine, XL-888, ritonavir), also L-ergothioneine, as it was supported by several runs of the analysis. 

```{figure} images/treatments_top.png
:name: treatments_top
 Geroprotective index distributions of all treatments and description of top-4 treatments with respect to the geroprotective index (thioguanine, olanzapine, XL-888, ritonavir).
```

### Geroprotective molecules overview

Among the isolated molecules, most of them are already used drugs in one or another field. 

**Thioguanine**, the top 1 molecule in the geroprotective index, is 2-aminopurine. Its key action is incorporation into DNA, resulting in inhibition of synthesis and replication. Therefore, it is actively used in the therapy of acute leukaemia. Most likely it is possible to find evidence for the geroprotective properties of thioguanine, nevertheless, its exact involvement in the mechanism of aging replacement seems a bit vague to us. 

**Olanzapine** is a benzene molecule containing sulphur atoms and a nitrogen antagonist. It acts as a serotonin-dopamine receptor antagonist and is used as an antipsychotic medication (second-generation antipsychotic). It is used for disorders such as schizophrenia and bipolar disorder and is also known as Zyprexa. In this form, the relationship of olazapine to aging may not be completely clear, but in recent years there has been a growing body of work on the geroprotective properties of antipsychotics and antidepressants.

**XL-888** is a less studied molecule. The available data suggest that it is an ATP-competitive inhibitor of the chaperone Hsp90. This is an important remark regarding our work, because in the original article the authors elaborate on the mechanism of Hsp90 inhibition as an important target in anti-aging. They identified other inhibitors, but in any case this overlap is very valuable to us. 


**Ritonavir**  is an L-valine derivative and also known under the name Norvir. It is an inhibitor of various proteases and in medicine is used as an HIV protease inhibitor to treat AIDS/HIV as well as various forms of hepatitis. In general, it can be a broad-spectrum antiviral drug, but it is often used to boost the effects of other drugs due to its ability to inhibit liver cytochrome P450-3A4.


### L-ergothioneine anti-aging treatment


```{figure} images/lergo_structure.png

---
width: 30%
name: lergo_structure
--- 
 The chemical structure of the L-ergothioneine, red oval higlights the functional group {cite}`apparoo2022ergothioneine`.
```

L-ergothioneine  is a histigine-derivative aminoacid with sulphur group on the imidazole ring. This sulphur can be found in the oxidised and reduced forms, which defines it's function. L-ergothioneine was proposed to have protection function against reactive oxygen species {cite}`paul2010unusual, cheah2016ergothioneine, apparoo2022ergothioneine, chen2023ergothioneine`. Paul et al. using HeLa cells lines showed that L-ergothioneine increases cells viability against $H_2O_2$ {cite}`paul2010unusual`. Therefore, it may be involved in responses to oxidative stress originating from mitochondrial activity, ultraviolet radiation, etc.


```{figure} images/lergo_aging_hallmarks.jpeg
---
width: 80%
name: lergo_aging_hallmarks
---
 L-ergothioneine in the network of the hallmarks of aging {cite}`chen2023ergothioneine`.
```

These features of L-ergothioneine make it an interesting member of the aging hallmarks network {cite}`apparoo2022ergothioneine, chen2023ergothioneine`. First of all, it is an obvious element of the cell's antioxidant system. Due to this, it has an immediate influence on the maintenance of genomic stability and mitochondrial functionality. However, there are some other interesting interconnections. For example, L-ergothioneine has been shown to be associated with sirtuin proteins that provide orchestration of the epigenetic landscape in the cell {cite}`chen2023ergothioneine`. Also an important observation is that L-ergothioneine is not synthesised in the human organism and therefore its maintenance is directly related to the operation of transport systems (in particular OCTN1 channels). Its involvement in various signalling cascades such as MAPK and KEAP1-NRF2 has also been shown. 

All this substantiates the role of L-ergothioneine as a geroprotector. Indeed, there is some medical research in this direction. Beelman et al. showed that the amount of L-ergothioneine in the diet is correlated with average mortality. Cheah et al. also reported that the amount of L-ergothioneine in the blood decreases with age. These data give us confidence in the adequacy of the model we have constructed. 

### Clarification of discrepancies with the findings in the article


An important issue we would like to address in this discussion is to analyse possible differences with the results in the original paper (see figure below). The first important remark is that among the 11 compounds we found, there are no overlaps with the authors' results. However, for example, we were able to find other Hsp90 inhibitors, and the mechanism of Hsp90 inhibition is one of the key topics of discussion of potential geroprotectors in the article. Although, the following reasons for the differences can be pointed out:


```{figure} images/orig_results.jpg
---
width: 80%
name: orig_results
---
Anti-aging treatments identified by Janssens et al. (E). The picture is taken from the original paper {cite}`janssens2019transcriptomics`.
```

- We used reduced data to save time. We selected some organs and ran a sample of 100 treatments (out of 3546 total) on them. We also ran our analysis for all treatments, but only for the brain.

- Our compounds-selectiong procedure differs from the paper due to lack of ran models (we did perform ranking)

- We suspect we used a slightly different version of CMap dataset. In our data we had 3546 treatments against 1309 in the paper. 

## Conclusions
 
In this project we built transcriptomic age-classification model which was used to identify treatments that result in a "younger" transcriptomes. With this model we identified 11 potentially geroprotective compoings, The most promising of them are: L-ergothioneine, thioguanine,  olanzapine, ritonavir, XL-888. These molecules do not match those found by the authors of the original paper, but we discuss possible reasons for this. We also studied L-ergothioneine individually and associate our hopes for a future victory over aging with this very compound. 

## Credits

The project was done by:

- [Ksenia Kubenko](https://crei.skoltech.ru/cls/people/kseniakubenko) preprocessed GTEx and CMap datasets
- [Ekaterina Kashuk](https://crei.skoltech.ru/cls/people/ekaterinakashuk) implemened Random Forest models and performed geroprotectors selection
- [Nikita Vaulin](https://www.linkedin.com/in/nvaulin/) visualised the results, reviewed the found geroprotectors and assisted in the preprocessing


## References

```{bibliography}
:style: plain
:filter: docname in docnames
```

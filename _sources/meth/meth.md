# Omics Data Analysis in Aging: Methylomics

```{contents}
```

## What is DNA methylation?

Considering the previous chapters, you must have already seen that epigenetics plays a huge role in our lives. And indeed, epigenetic mechanisms tightly control all the intricate behaviors of our cells. Which functions to provide, which range of proteins to produce, and how to react to external signals: all of this information is not encoded explicitly in the DNA sequence, and is regulated by the epigenome {cite}`lim2016`. There are a lot of various epigenetic mechanisms including histone modifications, nucleosome remodelling, noncoding RNAs, etc. {cite}`saul2021`, however, DNA methylation is one of the most investigated types of epigenetic modifications. As you can see from the {numref}`epigenetics` below, we’re descending to the very depths of gene regulation.

```{figure} figs/epigenetics.png
:name: epigenetics
:width: 600
Overview of epigenetic mechanisms
```

Methyl groups can be attached to the cytosine bases of DNA at the 5th carbon atom of the pyrimidine ring (annotated as 5mC), and it is most commonly observed in a CpG context (cytosine followed by a guanine nucleotide) {cite}`seale2022`, although other types of DNA methylation such as methylation of the nitrogen atom at the 6-th position of adenine (6mA) have also been discovered but remain poorly characterized {cite}`iyer2016`.

How does methylation appear? Well, there are two options ({numref}`methylation_pathways`). First of all, DNA methyltransferase 3 (DNMT3) can produce methylation at the completely unmethylated sites (so-called *de novo* mechanism). Secondly, since CpG sites are symmetrical on both strands, it’s easy to imagine some mechanism that would recognise a site that is methylated at one strand and is unmethylated at the opposite one. Such situation occurs, for example, after DNA replication, where the mother strand retains its methylation pattern, but the daughter strand is built from raw nucleotides, so it’s not modified yet. In such cases, UHRF1 recognises these so-called hemi-methylated sites and recruits DNA methyltransferase 1 (DNMT1), which faithfully restores the symmetry {cite}`greenberg2019`. Both reactions require S-adenosyl methionine (SAM) as a donor of methyl groups.

```{figure} figs/methylation_pathways.png
:name: methylation_pathways
:width: 700
Methylation pathways: *de novo* methylation by DNMT3A/B, a complex containing a conserved methyltransferase domain (MTase) and two histone reader domains, ATRX-DNMT3-DNMT3L (ADD) and PWPP, is (a) repelled by methylation at H3K4 and recruited by the binding of ADD to unmodified H3K4 in promoters and (b) enhanced by the interaction between PWWP and H3K36me3 in gene bodies; (c) maintenance methylation by DNMT1, a complex in which the catalytic MTase domain is blocked by its own replication foci targeting sequence (RFTS) domain, is mediated by the UHRF1 complex which recognizes hemi-methylated DNA using SRA domain, ubiquitinates H3 tails using RING domain, rescues DNMT1 from self-inhibition by binding to RFTS and targeting it to the ubiquitinated H3, thereby providing access of MTase to the unmethylated CpG site (adapted from {cite}`greenberg2019`)
```

Demethylation is a less straightforward process. Up to date, no enzyme has been discovered that can directly convert methylated cytosines into unmethylated ones. Instead, ten-eleven translocation (TET) family enzymes can successively oxidize methyl cytosine to hydroxymethyl, to formyl, and to carboxyl cytosine, which is then excised from DNA by thymine DNA glycosylase (TDG). The empty space is recognised by the base excision repair system, which recruits a new cytosine to replace the excised one. In addition to this active pathway, methylation can be removed passively as a result of dilution during DNA replication {cite}`greenberg2019`. For example, if we imagine a case, in which, at the same time, cells divide rapidly, they replicate their DNA rapidly, and the UHRF1 or DNMT1 proteins are somehow inhibited, then there will be more and more cells with almost no methylation on both strands. This is what happens, for example, at the early stages of embryonic development.

DNAm is evolutionarily more ancient than the first eukaryote, nevertheless, it has been lost during evolution multiple times independently, likely because this modification is in fact quite toxic, since it can easily lead to spontaneous oxidative deamination of 5 methylcytosine into thymine {cite}`iyer2016`. This is also the reason why the number of CpG sites in mammals, for example, is 5 times lower than expected from their nucleotide distribution. To make it even worse, DNA methyltransferase enzymes (DNMTs) are prone to produce 3mC instead of 5mC, thereby creating DNA lesions, and only co-evolution of methyltransferases with alkylation repair enzymes apparently allowed DNA methylation to be retained at all {cite}`greenberg2019`.

It is important to note that due to a multitude of pathways and regulators, these processes of methylation ({numref}`methylation_pathways`) and demethylation ({numref}`demethylation_pathways`) are in dynamic equilibrium to each other, and the exact point of balance is established for each CpG site at each cellular state.

```{figure} figs/demethylation_pathways.png
:name: demethylation_pathways
:width: 400
Demethylation pathways: 5mC can be actively oxidized in a series of reactions mediated by the Ten-eleven-translocase (TET) family proteins to 5-hydroxymethyl- (5hmC), 5-formyl- (5fC), and 5-carboxycytosine (5caC) (noteworthy, each further step of oxidation occurs at a progressively slower rate {cite}`ito2011`), whereupon 5hmC is converted to 5-hydroxymethyl uracil (5hmU) by the APOBEC (apolipoprotein B mRNA editing enzyme, catalytic) family members. 5fC, 5caC, and 5hmU can be excised, primarily by TDG, to yield an apurinic / apyrimidinic site (AP site) which is rescued by the base excision repair (BER) machinery. Alternatively, 5mC can spontaneously convert to thymine via hydrolytic deamination and then be subjected to BER as well {cite}`bayraktar2018`.
```

<!-- 
```{figure} figs/methylation_chemistry.png
:name: methylation_chemistry
DNA methylation biosynthesis from a chemistry viewpoint: (a) cytosine (de)methylation; (b) adenine (de)methylation. For thorough description, read {cite}`liu2023`
``` -->

--- Work in progress ---

## How to measure DNA methylation

The history of measuring DNA methylation is quite long ({numref}`dnam_profiling_timeline`), and we’re not going to stop at every point of this timeline (if you’re eager to get the historical perspective, see {cite}`li2021`), because most of these methods have long sunk into history. For example, even though liquid chromatography and mass spectrometry (LC-MS) is perfectly capable of profiling both 5mC, 5hmC, and all other DNA modifications, is never used for this task today because of its exorbitant costs.

```{figure} figs/dnam_profiling_timeline.jpg
:name: dnam_profiling_timeline
Evolution of the DNA methylation profiling methods {cite}`li2021`
```

Electrophoresis and first-generation (Sanger) sequencing methods are plainly outdated, while third-generation sequencing (Oxford Nanopore, PacBio) is too young and underdeveloped yet to be widely accepted by the epigenetics community. Only two methods survived the sands of time: microarray hybridization and second-generation sequencing, both of which we will discuss in more details today.

Essentially, the main take-home message from this chapter is that the microarrays represent an old technique that is relatively inaccurate, covers a small percentage of CpG sites, and is difficult to compare between different datasets (huge batch effect). However, it is still being upgraded (more CpGs are being included) and widely used, especially in human methylation profiling, for the only reason of its cost and ease of handling. Nevertheless, it is inevitable that the highly accurate and comprehensive (up to 100% of CpGs can be covered) sequencing-based methods, which have already become the “gold standard” in the field, will gradually replace microarrays as long as they become more and more affordable for the wider community.

Both microarray and sequencing technologies rely on amplification, during which DNA is fragmented, and the fragments are multiplied several times to increase their concentration. Across these steps, DNA methylation cannot be maintained, therefore, DNA should undergo some pretreatment which later allows distinguishing methylated from unmethylated. The main pretreatment methods are based either on:

1. **restriction enzymes** (MRE-seq; {numref}`dnam_profiling_restriction_affinity`, left column), 
2. **affinity enrichment** (MeDIP-seq and MBD-seq; {numref}`dnam_profiling_restriction_affinity`, center and right columns), or 
3. **bisulfite conversion** (BS-seq, {numref}`dnam_profiling_bisulfite`) {cite}`rauluseviciute2019, li2021`.

In MRE-seq, various methylation-sensitive restriction enzymes are used to cleave DNA at unmethylated sites, so DNA region methylation status can be deduced from the number of times a cutting site is observed (the more observations, the more methylated it is). The coverage of CpGs is therefore fully dependent on the range of cleavage sites that can be recognized by the enzymes. In MeDIP-seq, antibodies affine to 5-methylcytosines (or 5-hydroxymethylcytosines) are used to pull (“immunoprecipitate”) only methylated and single-stranded fragments from the solution. The main drawback of this approach is that the antibodies are biased to bind CG-rich fragments, yielding a lot of false negatives in CG-poor regions. In MBD-seq, methyl-CpG-binding domain proteins attach to the double-stranded methylated DNA fragments. Although, they cannot distinguish between 5mC and 5hmC, and bind unstably to the hemi-methylated DNA, yielding false negatives again. Most unfortunately, all affinity-based approaches are unable to profile methylation at single-base resolution, because whole fragments are pulled if they contain methylated CpGs, even though the unmethylated ones are also present.

```{figure} figs/dnam_profiling_restriction_affinity.jpg
:name: dnam_profiling_restriction_affinity
Restriction enzymes-based and affinity enrichment-based methods for DNA methylation profiling {cite}`li2021`
```

Bisulfite conversion is the most widely adopted approach for DNA methylation profiling. In it, DNA is treated with sodium bisulfite, which converts unmethylated cytosines into uracils (replaced with thymine during amplification), while methylation provides protection from this conversion, so 5mC remains intact. As a result, 5mC will be read as C, while unmethylated C becomes T. Comparing the converted fragments with the reference genome allows resolving modified cytosines from the unmodified ones. The main sources of bias in BS-seq are incomplete BS conversion, BS-induced DNA degradation, PCR amplification, and DNA modifications (both 5mC and 5hmC are protected from BS) {cite}`li2021`. Still, it provides the greatest accuracy, reproducibility, and coverage, so our further discussions will only be related to the post-BS conversion approaches.

```{figure} figs/dnam_profiling_bisulfite.jpg
:name: dnam_profiling_bisulfite
Schematic representation of the bisulfite conversion reactions and resulting DNA fragments, adapted from {cite}`singer2019`
```

Finally, after pre-treatment is done, DNA fragments are sent either to bead chip microarrays or to deep sequencing machines.
In microarrays, essentially, DNA fragments bind to the arrays of short nucleotide beads attached to a chip. The binding is based on whether these fragments are complementary to the bead sequences. Therefore, DNAm coverage fully depends on whether a particular sequence is present in the beads. The DNAm BeadChip microarray technology is advanced by the Illumina company and has been through four generations with successive increases in methylome coverage: ~1.500 CpGs (in promoters), ~27k CpGs (in promoters), ~450k CpGs (in promoters and proximal enhancers), and ~850k CpGs (adding sites in distal enhancers to the 450k coverage). Both 450k and 850k platforms are still widely used, especially in the human cancer studies.

Sequencing is done either across the whole genome (whole genome BS, WGBS) or after the isolation of CpG-rich regions by applying restriction enzymes prior to bisulfite conversion (reduced representation BS, RRBS). RRBS was developed as a compromise between covering a large proportion of methylome, while discarding methylation sites far outside of CpG islands, thus substantially reducing the sequencing costs (although some CpG-rich regions remain uncovered due to the restriction enzyme specificity) {cite}`li2021`.

Some of the aforementioned methods have been adapted to profile 5hmC and other DNA modifications in addition to or instead of 5mC. In terms of profiling methylation in single cells, numerous approaches (BS-based, primarily) have been suggested that often combine it with the profiling of transcriptomics, chromatin openness, histone modifications, etc. {cite}`ahn2021`

Combinatorial strategies have been gaining attention in the past decade, for they allow profiling DNA methylation simultaneously with other epigenomics or transcriptomics features. For example, in NOMe-seq, the addition of GpC methyltransferase before bisulfite sequencing provides both DNA methylation and nucleosome occupancy (i.e., accessibility of DNA regions for transcription) profiles. NOMe-seq and other techniques, sometimes coupled with capturing single cells (sc), such as ChIP-BS-seq (DNAm + histone modifications), scCOOL-seq (DNAm + chromatin accessibility) scNMT-seq (DNAm + chromatin accessibility + transcriptomics), etc. {cite}`ahn2021, minnoye2021` are paving the road for comprehensive understanding of biological processes on a whole new multi-omics level.

In the end, the choice of DNAm profiling methods stems from the cost-effectiveness considerations and posed biological questions. While it is undoubtedly beneficial to comprehensively profile whole methylomes at single-base resolution using WGBS, the costs of such an endeavor make researchers resort to the less comprehensive and more biased, although far more affordable approaches such as RRBS and microarray technologies. The features, advantages, and disadvantages of the methods we’ve discussed here are displayed in {numref}`dnam_profiling_comparison` (adapted from {cite}`singer2019, rauluseviciute2019, li2021`).

```{list-table} DNAm profiling methods overview (assembled from the papers mentioned previously in this section)
:header-rows: 1
:stub-columns: 1
:name: dnam_profiling_comparison

* - Profiling Method
  - Pre-treatment
  - Target
  - Context
  - 5mC / 5hmC
  - Coverage
  - Quantification
  - Wet lab requirements
  - Sources of bias
  - Costs
* - MRE-seq
  - Restriction enzymes
  - Cleaves at unmethylated
  - CpG
  - 5mC only
  - Low (<6% of CpGs, depends on restriction sites)
  - Relative
  - Low
  - Restriction sites, fragment size
  - Low
* - MeDIP-seq, MBD-seq, etc.
  - Affinity enrichment
  - Pulls at methylated
  - CpG
  - Either
  - Medium (60-85% of CpGs)
  - Relative
  - Low
  - Copy number, CG content, CpG density
  - Low to medium
* - Microarray-based
  - Bisulfite conversion
  - Converts C, intact 5mC
  - CpG (specified by probe sequences)
  - Merged
  - Low (specific sites, <5% of CpGs)
  - Absolute
  - Medium (specialized platform)
  - Background correction, inter-array normalization, probe-design bias, dye bias
  - Medium
* - WGBS
  - Bisulfite conversion
  - Converts C, intact 5mC
  - Any
  - Merged
  - Highest (up to 100% of methylome)
  - Absolute
  - High (specialized chemistry and computational platforms)
  - Incomplete conversion, PCR artifacts
  - Very high
* - RRBS
  - Bisulfite conversion
  - Same as WGBS, but at CG-enriched
  - Any (mostly CpG)
  - Merged
  - High at CGIs (85%), low in total (13% of CpGs)
  - Absolute
  - High
  - Incomplete conversion, PCR artifacts
  - High
* - oxBS-seq
  - Bisulfite conversion
  - 5hmC
  - Any
  - Both
  - High
  - Absolute
  - High
  - Incomplete conversion, PCR artifacts
  - Very high
* - TAB-seq
  - Bisulfite conversion
  - 5mC
  - Any
  - 5hmC only
  - High
  - Absolute
  - High
  - Incomplete conversion, PCR artifacts
  - Very high
```

## How to analyze DNA methylation

Computational analysis of DNA methylation consists of three main steps {cite}`bock2012, rauluseviciute2019`:

1) **Data processing and quality control**
2) **Visualization and statistical analysis**
3) **Validation and interpretation**

We will briefly outline this workflow and discuss some important caveats that arise during each step. Bisulfite conversion-based approaches are of the most interest to the researchers nowadays, so we will omit the peculiarities of other approaches to DNAm profiling here (if you’re that interested, see {cite}`bock2012, rauluseviciute2019`).

### Data processing and quality control

#### Processing bisulfite sequencing data

Processing raw bisulfite sequencing data must deal with the following tasks:

1) **Trim** sequencing adaptors from the ends of reads (adaptors are added to reads to improve capturing of the smaller-sized ones) and trim reads with low quality (e.g., incorrectly converted)
2) **Align** (or map) reads to the reference genome 
3) **Calculate** methylation fractions (or beta values) per site

Trimming is, to some extent, a trivial task, and tools for trimming have been largely adopted from other omics data analyses such as DNA-seq or RNA-seq.

Read alignment, however, is rather challenging, because bisulfite conversion produces reads with reduced complexity (far fewer cytosines than in the original sequence), which increases chances to observe a read that can be mapped to multiple genomic regions. But more importantly, alignment algorithms must take into account that some of the Ts it observes in the reads are originally Cs (in the reference genome). To overcome this problem, two main branches have been proposed: wild-card aligners and three-letter aligners.

Wild-card aligners (such as BSMAP) substitute every C in the reference by the wild card Y, which can be aligned to both C and T in the sequencing reads. As can be seen from an example in {numref}`align`, wild-card aligners may introduce bias by overestimating methylation proportions (methylated reads contain Cs that raise read sequence complexity enough so that these reads can be mapped unambiguously, but the unmethylated reads bearing Ts are prone to be discarded because they align to different genomic regions simultaneously).

On the other hand, three-letter aligners (such as Bismark or BS Seeker) that replace every C in the reference genome with a T (therefore, only three letters from the genomic alphabet are left: A, G, and T) are simpler in use (because conventional genomic aligners can be employed) and are not biased towards overestimating or underestimating methylation fractions. However, since they reduce sequence complexity even more, a large fraction of reads aligns ambiguously and is discarded ({numref}`align`).

```{figure} figs/align.png
:name: align
:width: 400
Strategies for bisulfite alignment {cite}`bock2012`
```

In conclusion, *wild-card aligners provide higher coverage at the cost of overestimating methylation, while three-letter aligners yield precise values, but only for a fraction of reads, at the expense of losing coverage*. It is worth noting that profiling genomic regions with higher sequence identity (containing transposable elements or duplications) or using shorter reads suffers the most from the aforementioned issues {cite}`bock2012`. As a result, **even though WGBS theoretically covers up to 100% of a methylome, it cannot be achieved in practice** due to the methodology of three-letter alignment, although newer algorithms are doing their best to increase their output coverage {cite}`huang2018, desenabrandine2021`.

After performing the alignment, we can calculate methylation fractions by simply dividing the number of observed Cs by the sum of Cs and Ts per methylation site, and it is exactly what most researchers do. However, additional post-alignment adjustments can improve the accuracy of this approach: for example, it does not distinguish between the bisulfite conversion-induced Ts and genetic variants. The Bis-SNP variant caller (an extension of a popular Genome Analysis Toolkit, GATK) attempts to deal with this bias by leveraging the fact that “bisulphite‑induced C‑to‑T variants exhibit a G on the opposing strand, whereas genetic C‑to‑T variants exhibit an A instead” {cite}`bock2012`, along with being handy in the SNP analysis in general {cite}`liu2012`.
In addition to all that, the **success rate of bisulfite conversion** is another metric that should be accounted for. Quality control of this rate can be performed by adding standardized DNA with known DNAm values, either pre-constructed oligomers or methylation-free viral DNA.

As you can see, there are enough steps to be worried about if you want to process your data in the best way possible. Although multiple comparison reviews are out there, almost none of them attempts to provide actual guidelines on which tools would be better to use in which circumstances, and, since the techniques are updated and developed every year, even those reviews that do try to suggest such ‘gold standards’ {cite}`rauluseviciute2019` are quite outdated, so the researchers have to choose on their own.

#### Processing microarray data

The Illumina microarrays are, on the one hand, easier to process than sequencing results (no alignment required, since probes contain pre-defined sequences), but, on the other hand, are far more laborious.

Instead of sequencing reads, microarrays provide colour signals of different intensities across a time range. The coloured image processing is virtually always done with the vendor-supplied software, so you won’t have to bother about it. However, after the signals are counted, the bioinformatician’s work begins.

First of all, just as with bulk BS-seq, bias may arise from **sample DNA composition** (polymorphisms or cell heterogeneity), but, more importantly for the microarray methodology, **bias comes from the arrays themselves**:

* cross-reactions between probes,
* background bias,
* nonlinear dye bias,
* probe-type bias (starting from Infinium 450k, probes are manufactured in two types, each with its specific characteristics, and both are present in every platform),
* and batch effects between two arrays.

We are not trying to become full-stack DNA methylation bioinformaticians in the scope of this course, so we will not go into full discussion about all these and about a whole battery of various normalization and bias correction approaches that have been described specifically to tackle these problems with microarray data (if you do want to delve deeper, see reviews {cite}`wu2014, nakabayashi2017, welsh2023`). In short, **SeSAMe coupled with pOOBAH filtering (SeSAMe 2)** appears the best performing microarray processing algorithm {cite}`welsh2023`, although it is a relatively young tool, so you will rarely encounter datasets processed by it. More often, researchers resort to the **good old practices** such as the default pre-processing steps of the *minfi* R package (quantile normalization for blood and DLPFC samples and noob procedure otherwise, according to the [minfi manual](https://bioconductor.org/packages/release/bioc/manuals/minfi/man/minfi.pdf)).

In the end, even if you use only the best processing tools, microarrays are still notorious for their between-array batch effect. Wet lab researchers are highly advised to profile samples in mixed order so as to minimize the magnitude of potential confounders (for example, to process samples from different tissues or the case and control samples on the same day, and not on different weeks). However, you will unlikely get this information from the open-source databases, and you will certainly be unable to change the way the datasets are collected. Several batch correction techniques are implemented in the aforementioned approaches, and there are also specific tools (e.g., ComBat, surrogate variable analysis (SVA), RUVm, etc. {cite}`nakabayashi2017`), but they still have quite a room for improvement {cite}`zindler2020, ross2022`.

#### Looking at the data

Further in our course (and in a lot of research settings, really), you will be spared from processing the raw reads, so let’s briefly overview how the actual processed DNA methylation matrix looks like.

For bisulfite sequencing, it comes in a variety of data formats. The major separation lies between the binary files (e.g., *.bigWig*) and the more familiar tab/comma-separated text files (e.g., Bismark *.cov* files, BS-Seeker *.CGmap* files, *.bed* and *.bedGraph* files, etc.). A lot of processing tools employ their own data format, so the format you get to work with depends on what you (or the authors of your dataset) have chosen to process your reads.

The main information that is always present in these files is **genomic position** (chromosome and DNA base number) and **methylation level** (a.k.a. methylation fraction or beta value). Ideally, to perform quality control on your sites, you want to also know the coverage—**total number of counts** (methylated + unmethylated)—per site, which is not always readily available (in case of *.bigWig*, for example). As DNAm may occur on both strands, but the annotation is done against the positive (Watson) strand positions only, some formats also mention the **strand directionality** per DNAm site (+/- or F/R), but some do not, so you might want to look at the reference genome to infer this information. Other columns may include the information on methylated and unmethylated counts, on the **genomic context** around a DNAm site (CpG, CHG, CHH, where H stands for ‘not G’), or something else. A good example of how processed DNAm data looks like is displayed in the [BS-Seeker3 manual](https://github.com/khuang28jhu/bs3) ({numref}`processed_dnam_formatting`), although most of these columns are usually absent in the outputs of common processing frameworks (e.g., Bismark *.cov*).

The other caveat you should be aware of is **genomic positioning**. As you can see from {numref}`processed_dnam_formatting`, BS-Seeker uses single-base notation (column 3), but it’s not always the case. Some pipelines output two-base notation, some even employ three-base regions, but you should not be misled: all of these regions involve only one DNA methylation site. In the 1-base case, it’s obvious to see where exactly it lands; in 3-base, it’s usually the position in-between the starting and ending positions; but the 2-base case is probably the most misleading, as it can be both. We advise you to always check your notation against the reference genome ([UCSC browser](https://www.genome.ucsc.edu/cgi-bin/hgGateway) will suffice) bearing in mind strand directionality, if you’re dealing with more than one dataset (especially if they’re processed by different tools), which often happens when building and using methylation clocks, for example.

```{figure} figs/processed_dnam_formatting.png
:name: processed_dnam_formatting
Example of processed DNA methylation data (BS-Seeker3 *CGmap* formatting)
```

Files after microarray processing are similar, but a ton more uniform:

* they are mostly tab/comma-separated text files,
* genomic positions are always notated in the Illumina ID style (this is an important caveat, since you have to convert these IDs into common genomic coordinates if you wish to compare microarray and BS-seq datasets, e.g., Illumina cg07881041 corresponds to chr19:5236005 in the hg38 human genome assembly),
* no strand information (can be inferred from genomic positions),
* context is always CpG,
* no counts (instead, there are methylated and unmethylated signal intensities, which are to be discarded after calculating methylation fraction values).

To sum up, the only info you can get directly from the processed microarray data is *CpG site ID* and its *methylation level*. Extremely user-friendly. Especially if you forget about all the numerous normalizations and bias corrections that have led you to these methylation levels.

## Visualisation and statistical analysis

Finally, after methylation percentages are calculated, we step into the realm of data analysis and interpretation. The amount of tools and approaches available for it is overwhelming, so we will only mention a few.

One of the obvious direct approaches is to look at your data, which can be done via the good old UCSC Genome Browser, SeqMonk, the Integrative Genomics Viewer (IGV), or many other tools {cite}`bock2012`. In addition to visualizing methylation profiles, it is also useful to perform some form of unsupervised dimensionality reduction, for example, by principal component analysis (PCA) or hierarchical clustering, to elucidate the major groups of samples in your data (and to detect some outliers).

But of course, probably the most widely adopted approach is to find differentially methylated (DM) positions (a.k.a. DMPs, DMSs \[sites], or DMCs [CpG sites]) or regions (DMRs) by comparing two or more studied groups, for example, to find differences between DNA methylation in a certain cancer type and healthy controls, or between cancer types. And, essentially, the main goal of DNAm profiling in the first place is to identify systematic differences between samples and sample groups, which is exactly the job for DM analysis.

DMP analysis is more suitable for the microarray-based data, since a lot of genes there are covered with only one CpG site, or several sites are spread too far apart from each other (e.g., one is situated in a promoter, and another one is in a gene body).
In WBGS and RRBS, on the other hand, a promoter can be covered with a dozen of CpG sites, and the variation at each of them can be a lot higher than the variation of methylation across the whole promoter (due to sequencing variability). In addition to that, DNAm sites are known to correlate really well within CpG islands, or in otherwise close proximity to each other {cite}`affinito2020`. Therefore, it is logical to interrogate DNA methylation not at individual sites, but in whole regions, which can be derived by splitting genome either into equally sized ranges, or into CpG-dense fragments (especially relevant for RRBS) {cite}`chatterjee2016`.
There are numerous statistical approaches to calculating differential methylation, whose pros and cons have been thoroughly discussed and reviewed elsewhere {cite}`shafi2018, piao2021`. The key feature in these approaches is the statistical test they use to estimate statistically significant differences in DNAm levels. Model assumptions about how DNAm levels per site/region are distributed and different genome segmentation methods are also embedded into these approaches, so the outcomes of their work (i.e., discovered DMRs) are inevitably different.

Another, less widely adopted, but still pretty insightful method is the analysis of methylation variability (again, at individual positions, VMPs, or at regions, VMRs), since variable methylation has also been linked to cancers, diseases, and aging {cite}`seale2022`. For example, increasing variance of housekeeping genes was shown to predict chronological age and aging-associated pathologies with even greater accuracy than methylation clocks built on changes in mean DNAm {cite}`mei2023`. Approaches to VM analysis are numerous as well, and are compared elsewhere {cite}`li2015`.

It is worth to keep in mind that methylation differences and variations may actually arise not from changes in DNAm profiles themselves, but from changes in cell composition: for instance, it is well-known that, during aging, the distribution of immune cells in blood shifts strongly towards the myeloid lineage cells [Nishi 2019], which likely affects training epigenetic clocks on bulk blood DNAm data. Therefore, it can be useful to assess cell-type heterogeneity between sample groups, which has also been reviewed in great length elsewhere {cite}`teschendorff2018`.

All things combined, evaluating differences in mean DNAm, in DNAm variance, and in DNAm heterogeneity ({numref}`dnam_analysis_combination`) provides a multi-dimensional outlook on epigenetic alterations, which may help us elucidate disease- and age-related features of the epigenome.

```{figure} figs/dnam_analysis_combination.png
:name: dnam_analysis_combination
Combining differential DNAm, variable DNAm, and cell-type heterogeneity in DNAm to compare healthy epigenome with progressing cancer epigenetic profiles: (a) two examples of VMCs, one driven by single-nucleotide polymorphisms (SNPs) located in *cis* with the indicated CpG site (defining a well-known *cis* methylation quantitative trait locus (*cis*-mQTL)) (left panel) and another driven by variation in immune-cell contamination (right panel). Panels illustrate how SNPs and **cell-type composition can drive large variation in DNAm**, while **variation may not correlate** with case versus control status. (b) Contrast between DMCs and DVCs. drawn from normal cervical smears (green) and either cervical intraepithelial neoplasia (CIN2+) or cervical cancer (both blue). Observe how a DMC is typically characterized by most samples in one phenotype exhibiting a deviation in DNAm value. By contrast, a DVC is characterized by a very stable DNAm profile in one phenotype but by DNAm outliers driving large variation in the other. (c) Example of a CpG that exhibits progression in DNAm between successive stages in cervical carcinogenesis. When comparing normal cervical smears that progress to CIN2+ to those that do not (Normal → Normal), this CpG **can be identified only via a test for differential variance**. When comparing CIN2+ to normal cervical smears, differential variance is still the **main distinguishing feature**. Only when comparing (invasive) cervical cancer to normal cervix does this CpG exhibit a stronger difference in average DNAm. Thus, this panel emphasizes the importance of selecting the appropriate statistical test, as the **choice of test will have a dramatic impact on feature selection**. (Adopted from {cite}`teschendorff2018`)
```

--- Work in progress ---

## Practice

Since we've already covered differential expression analysis in our previous practical lesson, let's do something different this time with DNA methylation. The practice on weighted gene-coexpression network analysis awaits you either at `~/meth/meth_practice.ipynb` in this repository (if you cloned it), or at [Google Colab](https://colab.research.google.com/drive/1mCak-0KTZkISR7ptyBvIOBj1MpewOwDx?usp=sharing) (don't forget to make your own copy). Happy hunting!

## Credits

This text was prepared by [Evgeniy Efimov](https://www.linkedin.com/in/evgeniy-efimov-84152725b).

## References

```{bibliography}
:style: plain
:filter: docname in docnames
```

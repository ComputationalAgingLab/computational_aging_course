# Aging Clocks

In this chapter, you will learn:

- How to conduct clinical trials for anti-aging drugs ten times cheaper and faster.
- The results of the last ten years of research on aging clocks.
- How to use aging clocks to find new in silico geroprotectors.
- Which aging clocks are the most accurate. Which are the cheapest.
- Why not everything is straightforward and what else needs to be done in this area.

During the practice, you will create your own aging clocks using machine learning.

```{contents}
```

## What is it

Imagine that a genie gives you a magic device that shows people's health as a number from zero to one hundred. For healthy young people, the device shows 100. Over time, the number decreases and when it reaches zero, the person dies. How could such a device be used?

First, it could speed up and cheapen clinical trials. If you are looking for a geroprotector, the primary endpoint of the trial is lifespan. People live on average 72 years, so it takes a lot of money and time to do the research, so you have all the chances to die yourself before you get the results. For example, now funds are being raised for the TAME {cite}`barzilai2016metformin` clinical trial of metformin for aging. In the last seven years, TAME -- Targeting Aging with Metformin -- has raised only 11 million dollars out of the necessary 40, and patient observation will last 6 years. If we had such a magic device, we wouldn't necessarily have to wait so long. Instead of the primary endpoint (prolonging lifespan), we could use a surrogate endpoint. If the device shows an improvement in health, this would be a good sign that the geroprotector is working and we could stop the trial earlier. This would save money and time.

Secondly, the magic device would help us search for new interventions against aging. For example, we could collect a large dataset of device readings for different people and try to find associations between lifestyle and better health. Or if our magic device is a computer program that predicts a person's health based on their indicators, we could run an optimization process: we would select such indicators to maximize health, and then find a way to similarly change human indicators. We will see how this idea helped find new geroprotectors that extended the life of worms {cite}`janssens2019transcriptomics`. 

This magical device, referred to as a **biological clock** or **aging clock**, has been the primary focus of research in the field of the biology of aging in the past decade. It is usually a statistical model trained to predict a person's chronological age based on their parameters, such as blood tests. The model is not perfect, so the predicted number differs from the actual chronological age. This prediction is called **biological age** and it is assumed that the error of the model is explained by the person's health. A sick smoking person has a higher biological age than chronological age, while a healthy athlete has a lower biological age. The difference between biological and chronological age is called **biological age acceleration**.

:::{note}
- **Chronological age** is the number of years a person has been alive since their birth.
- **Biological age** is a number that signifies a person's health. In practice, this is a prediction of a model trained to predict chronological age.
- **Biological age acceleration** is the difference between biological and chronological age.
:::

(bioclocks_type)=
## Types of Biological Clocks

The [most common causes of death](https://ourworldindata.org/grapher/annual-number-of-deaths-by-cause) in developed countries are cancer, cardiovascular disease, type 2 diabetes, Alzheimer's disease, and Parkinson's disease. These diseases have different mechanisms, but the strongest risk factor for all of them is age, so researchers of aging believe that aging is not just an association but a cause of many diseases, so slowing aging would reduce the likelihood of illness. This is called the **geroscience hypothesis**.

:::{note}
- The **geroscience hypothesis** proposes that aging is the primary cause of many chronic diseases, and that these diseases can be delayed by slowing down aging.
:::

Aging biomarkers are an important focus of research in the field of aging because what cannot be measured cannot be improved. There are several key characteristics that are desirable for clinical use {cite}`butler2004aging`:

- They change with age;
- They predict mortality better than chronological age;
- They predict the early stages of age-related diseases;
- They are minimally invasive and do not require painful or serious procedures.

In addition to these characteristics, Alexey Moskalev {cite}`moskalev2019biomarkers` also adds that ideal aging biomarkers should be:

- Sensitive to early stages of aging;
- Have predictability with collecting in the foreseeable time range;
- Robust.

Over the years, dozens of biological clocks have been published. Here are the main types.

### Epigenetics Clocks

During transcription, RNA is produced based on the DNA sequence, which usually leads to protein synthesis. Different proteins are required under different conditions, so there are different ways to control transcription. One of these methods is DNA methylation, in which a methyl group is attached to a nucleotide, which typically leads to suppression of transcription.

In mammals, methylation usually occurs in special DNA regions consisting of "CG" nucleotides, called **CpG sites**. The average level of cytosine methylation in these regions can be experimentally measured as a number between 0 and 1, where 1 means that all cytosines in the site are methylated on both alleles and 0 means that all cytosines are unmethylated.

:::{note}
- **CpG site** -- a cytosine nucleotide followed by a guanine nucleotide, forming the pattern "CG". In mammals, 70-80% of cytosines in these regions are methylated, and conversely, a large portion of methylated nucleotides lie in these regions.

- **CpG island** -- a region of DNA with a high number of CpG sites.
:::

:::{note}
Most biological clocks work on bulk data, where only the average level of methylation is known, but single-cell methods are now available that can measure the methylation status of each nucleotide {cite}`trapp2021profiling`.
:::

As one ages, methylation changes in a complex, partly predictable way {cite}`palumbo2018dna`. This means that the level of methylation can be used to predict a person's age. Many clocks have been built on this idea. Let's consider the most notable works.

#### 2011 Epigenetic predictor of age
In {cite}`bocklandt2011epigenetic`, the authors built the first epigenetic clock using saliva.

#### 2013 Genome-wide methylation profiles reveal quantitative views of human aging rates
In {cite}`hannum2013genome`, the clock was built on blood cells. The authors analyzed the results and found that:

- Men age 4% faster than women.
- Clocks built on blood cells also work on other tissues, such as lung or kidney cells.
- The authors confirmed the existence of **epigenetic drift**. The methylation of elderly people differs from each other more strongly than among young people. This is due to the accumulation of random errors.

:::{note}
- **Epigenetic drift** -- An increase in methylation diversity with age: elderly people differ more from each other than young people. This is due to the accumulation of random errors.
:::

#### 2013 DNA methylation age of human tissues and cell types
In {cite}`horvath2013dna`, the author:

- Built clocks using different human tissues.
- Showed that progerias (genetic diseases characterized by accelerated aging) increase biological age.
- Showed that reprogramming cells into [iPSCs](https://en.wikipedia.org/wiki/Induced_pluripotent_stem_cell) resets biological age;
- Showed that predictions of the clock in chimpanzee tissues correlate with chronological age;
- Showed that cells that have undergone more divisions have a higher biological age.

:::{note}
- **Progeria** -- a general term for rare genetic diseases characterized by accelerated aging.
:::

:::{warning}
The original study showed that cancer tissues have a higher biological age. In 2015, a correction was released that corrected an error in the code, so that tumors no longer differed from healthy tissues in age.

Future biological clocks have shown acceleration of biological age in tumors. For example {cite}`liu2020underlying`.
:::

#### 2018 An epigenetic biomarker of aging for lifespan and healthspan (PhenoAge)
Ordinary biological clocks are trained to predict chronological age, expecting the model error to explain the mortality difference. But where does this assumption come from? If we could train a perfect oracle model that always correctly predicted chronological age, such a model would be useless. That is why we could predict how many years a person has left to live instead of chronological age.

In {cite}`levine2018epigenetic` the authors first trained a [Cox proportional regression model](../stat/hazard_models.ipynb) to predict mortality using clinical biomarkers and age from the NHANES database. With it, they made a prediction for a dataset with blood methylation, and then trained the model to directly predict mortality from methylation data.

Acceleration of such a phenotypic epigenetic age is positively associated with mortality -- an important property that was not present in previous clocks, so such clocks are called second generation clocks.
#### 2019 DNA methylation GrimAge strongly predicts lifespan and healthspan
The GrimAge{cite}`lu2019dna` clock was constructed in a similar manner. As proxies for predicting mortality, the authors took the concentration of blood proteins and the number of smoked cigarette packs, which were predicted from methylation. As a result, a model was obtained that better predicted the date of death and the onset of age-related diseases than previous models.

:::{admonition} Oracle Model
:class: tip
In {cite}`zhang2019improved` the authors trained the most accurate epigenetic clocks with an RSME error of 2.04 years. While the model performed better than all previous ones, its acceleration of biological age no longer predicted mortality and was no longer associated with diseases, rendering clinical use of such clocks meaningless.
:::

### Other Clocks

#### Transcriptomic Clocks
DNA transcription is the process by which mRNA molecules, which are used to create proteins, are synthesized. By analyzing the full transcriptome, or all of the RNA molecules, of a cell, we can sequence and compare the transcriptomes of healthy individuals with those of sick individuals. This helps to uncover the mechanisms behind diseases and potentially discover new treatments{cite}`yang2020high`.

We could learn more about aging by comparing the transcriptomes of old people with those of young people. One way to do this is to build aging clocks on the transcriptome and try to understand why the model turned out to be that way. This is what was done in {cite}`mamoshina2018machine`, where the authors trained clocks on the transcriptomes of human muscles. The clocks were less accurate (MAE 6.19 years) than methylome-based clocks, but feature importance techniques proposed new targets for potential geroprotectors.

In addition to interpretability, transcriptome-based clocks have another advantage. C. elegans roundworms do not have 5mC nucleotides, so epigenetic clocks cannot be built for them in the traditional sense. Therefore, transcriptome-based clocks were built for c. elegans {cite}`tarkhov2019universal, meyer2021bit` that work for worms of different strains living in different conditions.

#### Blood Test Clocks

Transcriptome and methylome are obtained through expensive sequencing. It would be more convenient for clinical practice to build an aging clock on cheap complete blood count. This was done in {cite}`putin2016deep`, and the feature importance technique showed that the most important predictors of age are albumin, glucose, alkaline phosphatase, urea, and erythrocytes. The model can be conveniently used through the website http://aging.ai.

In the following article {cite}`mamoshina2018population`, the authors improved the accuracy of the model and reduced the number of necessary measurements. The authors found that the quality of the model varies between patients from different countries: Canada, Eastern Europe, and South Korea.
## Application of Biological Clocks
Acceleration of biological age meets the [criteria for a marker of aging](bioclocks_type). For example, it predicts mortality from various causes{cite}`marioni2015dna`. An increase in epigenetic clock of the first generation is not associated with a deterioration of physical and cognitive functions{cite}`marioni2015epigenetic`, but is associated for clocks of the second generation{cite}`maddock2020dna`.

Obesity {cite}`horvath2014obesity` and Down syndrome {cite}`horvath2015accelerated` increase biological age. HIV also increases biological age even in brain tissue, although it is not clear why {cite}`horvath2015hiv`.

In 2006, the CMAP dataset was published {cite}`lamb2006connectivity`, in which the authors measured how the transcriptome of cells changes after exposure to 1300 different drugs. Using this dataset and biological clocks, it is possible to find new drugs. For this, in {cite}`janssens2019transcriptomics` the authors trained transcriptomic clocks on 51 human tissue and then searched in CMAP for drugs that, according to the model, reduce biological age. As a result, known geroprotectors and several new molecules were found, which were tested on worms c. elegans. The experiment confirmed that inhibitors of the protein Hsp90 extend life.

### Open Questions
During the search for drugs that lower the predicted model age, we find geroprotectors that extend life. Does this mean a causal relationship? Can we call a molecule that reduces biological age a geroprotector, but for which a costly, long-term clinical trial has not yet been conducted that proves a reduction in mortality? There are several problems {cite}`bell2019dna,schork2022does`.

**Predictions of different clocks are weakly correlated with each other. Epigenetic clocks are trained on different CpG sites.**
Does this mean that clocks measure different aspects of aging? Or that clock predictions are very noisy? The authors of {cite}`liu2020underlying` show that clocks capture different aspects of aging. If this is the case, it would be important to find these separate aspects and make separate clocks for them.

**Predictions of aging clocks poorly correlate with other classic biomarkers, such as blood pressure or glucose levels.**
This may be because aging clocks only measure one aspect of aging, or because aging clocks measure something more fundamental than what other clinical biomarkers measure. Could molecules that reduce biological age but do not affect classic biomarkers extend lifespan?

**The cause-and-effect relationship is unclear.**
To what extent are epigenetic changes the cause of aging, and to what extent are they a consequence?
In the first generation of clock models, training was done on predicting chronological age. This means that the data on elderly people in the dataset are from those who have managed to live to old age. Could this distort the model?

The authors of {cite}`nelson2020biomarkers` show that it can. The authors simulated random changes in methylation and assumed two things: mortality increases with the number of changes in CpG sites and changes in different CpG sites increase mortality differently. They trained an Elasticnet model on synthetic data and showed that as a result of L1 regularization, it selects non-causative sites that contribute little to mortality

:::{admonition} F.A.Q.
:class: tip
**Q:** Is it true that epigenetic clocks simply show differences in tissue composition?

**A:** It depends on the clock. If it is a multi-tissue {cite}`horvath2013dna`, then no: you can train the clock on one tissue and it will work on another. If it is a second generation {cite}`levine2018epigenetic,lu2019dna` phenotypic clock or a single-tissue clock, then it is possible.

**Q:** Could it be that epigenetic clocks work only because they distinguish senescent cells?

**A:** It does not seem so, because they work in immortal non-senescent cells, such as immortalized B cells or in embryonic cells. Cell aging and senescence are associated, but they are not the same. See the discussion and experiments in {cite}`lowe2016epigenetic`.

**Q:** Could it be that epigenetic clocks only measure the number of cell divisions?

**A:** It does not seem so, because they work in non-proliferating cells, such as brain cells.


## Linear Regression

As we can see, developing biological clocks is an important task in aging biology. Most biological clock models predict either chronological age or risk of death based on a person's parameters. But how does this technically happen? How can we make our own biological clocks for our own data?

Almost all biological clocks are linear regression. Linear regression is ubiquitous, so we assume that the reader is already familiar with it, so we will only remind you of the main ideas. For a first introduction to linear regression, we recommend practical tutorials[[1]](https://scikit-learn.org/stable/modules/linear_model.html), [[2]](https://www.kaggle.com/learn/intro-to-machine-learning), [[3]](https://d2l.ai/chapter_linear-regression/index.html).

In the linear regression model, we assume that the predicted value is linearly dependent on the input data. Let $y$ be the chronological age that we are trying to predict. $x_{1}, x_{2}, \dots x_{n}$ are known input parameters, such as blood test results. Then in the linear regression model, we approximate $y$ as a linear function:

$$
a_1 x_1 + a_2 x_2 + \dots + a_n x_n = y + \epsilon
$$

where $a_1, a_2, \dots a_n$ are coefficients that we need to select, and $\epsilon$ represents normal noise, explaining, for example, that blood tests are measured with error:

$$
\epsilon \sim \mathcal{N}(0,\,\sigma^{2})
$$

We want to select such coefficients $a_1, a_2, \dots a_n$ so that the model predicts chronological age as accurately as possible. In other words, we want to minimize the error:

$$
min_{a_1,\dots a_n} | (a_1 x_1 + a_2 x_2 + \dots + a_n x_n) - y |
$$

In practice, the error is minimized using gradient descent, where at each iteration the coefficients $a_1, a_2, \dots a_n$ are shifted in such a way as to make the error as small as possible.

### Overfitting and Regularization

The more parameters a model has, and the less data in the training dataset, the easier it is for the model to simply memorize the entire training dataset. In this case, the linear function approximating chronological age will poorly describe the real world, and we will see a large error on the test dataset. This is called overfitting and can easily occur if you have a small dataset and a large number of parameters.

To deal with overfitting, regularization can be applied -- that is, imposing some constraints to make the model simpler. For example, if you overfit a linear regression model, you will notice that its coefficients become very large:

$$
1863526.326 x_1 - 7532253.1663 x_2 + \dots + 52.1 x_n = \hat{y}
$$

It is unlikely that chronological age depends on blood test analyses with such coefficients in real life, so you can try penalizing the model for having too large coefficients during training. To do this, during gradient descent we will minimize both the error and the sum of the absolute values of the coefficients.

$$
min_{a_1,\dots a_n} | (a_1 x_1 + a_2 x_2 + \dots + a_n x_n) - y | + \lambda \sum_{i} |a_i|
$$

"where $\lambda$ is a coefficient representing the strength of regularization. This method of regularization is called L1 regularization and can improve the model's performance on the test dataset in practice.

### L1 and L2 regularization

A model can be regularized in different ways, but the two most common methods are L1 and L2 regularization. L2 regularization differs in that the error is not just the absolute value of the coefficients, but also their squares added to the error:"

$$
min_{a_1,\dots a_n} | (a_1 x_1 + a_2 x_2 + \dots + a_n x_n) - y | + \lambda \sum_{i} a_{i}^{2}
$$

Both regularization methods help to find small coefficients, but the difference between them is that L2 regularization more heavily penalizes large coefficients and less heavily penalizes small coefficients. For example, if the model has two coefficients of 0.5 and 2, then with L2 regularization their contribution to the penalty becomes 0.25 and 4.

Both methods help to combat overfitting, but L1 is also useful in that the coefficients of unimportant features can quickly become zero, which gives us a useful signal that this blood parameter does not help the model predict chronological age. In practice, the regularization that helps improve the model's performance on the test dataset is used.

### Elasticnet

You can choose not to choose between the two regularization methods and simply apply both. Sometimes this works better than one regularization alone:

$$
min_{a_1,\dots a_n} | (a_1 x_1 + a_2 x_2 + \dots + a_n x_n) - y | + \lambda_1 \sum_{i} a_{i}^{2} + \lambda_2 \sum_{i} |a_{i}|
$$

Such a model is called ElasticNet and is used in the construction of several clocks.

```{bibliography}
:style: plain
:filter: docname in docnames
```
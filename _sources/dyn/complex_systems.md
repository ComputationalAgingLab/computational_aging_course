# Complex systems approach

*Nothing in aging biology makes sense except in the light of dynamic equilibrium.*

Aging biology today is not an engineering but science at its early step. This expresses in that we frequently cannot observe a direct causal and numerically tractable relationships (as in physics) but we are doomed to see mostly *associations* and *patterns*. However, it may also be a good starting point for dynamical modeling. Large volumes of data and absense of organizing paradigm are major challenges of the modern aging biology. Complex systems approaches provide some computational instruments and necessary vocabulary for simplification, understanding and identification the essential features from data. This chapter partly relies on recent work of {cite}`cohen2022complex` where corresponding philosophical framework as well as important computational examples were proposed.

Throughout this chapter, you may come across many new words: **system**, **complexity**, **networks**, **emergence**, **resilience** and **critical transitions**. They form an important minimal vocabulary neccessary for developing complex systems intuition which (we believe) can be greatly useful for any researcher. We organize them in subsections and uncover one by one.

```{contents}
```

## Complex systems perspective on aging

Before the consideration of complex systems we should understand what we had before. Typical two common approaches in sciences are **Top-Down** and **Bottom-Up**. Let's the object of study is a human organism, then Top-Down approach asks a question which large scale observations is associated with small scale. For example, a patient's state change is associated with changing of a level of some protein. And vice versa, Bottom-Up approach asks whether large scale patient's state changes after perturbation of some protein level? Moving Bottom-Up generates something we call metabolic pathways, gene ontologies, etc. - i.e. combining small scale entities into new higher scale entities. In turn, moving Top-Down we can differentiate new entities such as organs, tissues, cells, organelles, nuclei at smaller scale (Fig. 1). You might have noticed that the science greatly advanced applying only these two approaches. However, encounter with living systems forces us to develop a new methodology. The problem of that two approaches is that they do not take into account interactions between feedback/feedforward loops at too different scales trying to provide mechanistic explanation of processes in level-by-level manner. They provide theories like **A causes B** and **B causes C** whilst in real complex systems we observe behaviors like **A causes B**, **B causes A**,  **B causes C** and **C causes A and B**. Do you agree that this no more presumes a one-dimensional schematic explanation of the mechanism of action? Such an abundance of causal relationships forces us to use the concept of **networks** for building a more correct body of knowledge.

<img src="<picture Box 1 from Cohen paper>" 
     alt="topdown" 
     width="200"/>
<p align = "center">
Fig.1 - Example of Top-Down and Bottom-Up organization of knowledge.
</p>

Cohen and colleagues {cite}`cohen2022complex` provide a great example of such a *switch to complexity* happened in ecological sciences recently (Fig. 2). You can see that a previously popular *food chains* theory was changed by a system approach where interactions between species form a complex network where it is not obvious how the system will respond to removing a particular species. Currently we observe a similar transformation in aging domain. Two great examples (and already classical) of such a transformation are Hallmarks of aging {cite}`lopez2013hallmarks` and Pillars of aging {cite}`kennedy2014geroscience` papers trying to highlight a set of key entities related to aging and connecting them into network of interacting elements. 

<img src="<picture 1 from Cohen paper>" 
     alt="complex" 
     width="300"/>
<p align = "center">
Fig.2 - Shift to complex systems approaches in ecology and aging biology.
</p>

:::{note}
- **Top-Down approach** -- methodology of connecting large scale observations with smaller scale ones by differentiation of large object to smaller entities.
- **Bottom-Up approach** -- methodology of connecting smaller scale observations with larger scale ones by combination of small objects into larger entities.
:::

Examples of complex systems include ecosystems, economies, traffic systems, power systems, etc. It is kind of magic that all of them, nevertheless, have common properties or hallmarks. Core hallmarks of complex systems include: 
1. networks of interacting elements (for example, interactions among molecules in key aging pathways such as AMP-activated protein kinase (AMPK), mechanistic target of rapamycin (mTOR), sirtuins, insulin-like growth factor); 
2. feedback/feedforward loops (for example, adaptive loops such as blood pressure regulation); 
3. multiscale or modular hierarchical structure (for example, organelles, nested in cells nested within tissues nested within organs); 
4. emergent properties, which are properties of a system that cannot be directly or additively inferred by examining its component parts (for example, cognitive decline cannot be understood simply as the sum of multiple aging cells;).

:::{note}
Cohen et al. {cite}`cohen2022complex` also mention *nonlinear dynamics* as a hallmark of complex systems. But we do not see enough arguments to include this point as a hallmark. In our view, complex systems can also have linear dynamics describing with set of linear ordinary differential equations for instance.
:::

Before we proceed, let's introduce one important rule which helps you to differentiate "bad" complex systems propositions from "good" ones. Any abstract philosophical concepts you will discover about complex systems (such as complexity or resilience) in future **must** be reinforced with concrete embodiment expressing in mathematical or biological terms.


## Aging as loss of Complexity

What can be one of the most common characteristics of aging? Can we express the plephora of our observations of aging organism by one cumulative term? It turns out, we can consider topological characteristics of complex living systems comparing them at different time moments (at young and old ages). The **complexity** was proposed as such characteristic in {cite}`lipsitz1992loss` where authors suggested that aging is associated with "loss of complexity". It is tough to define "complexity" explicitly and the authors do not give such a definition. Instead they measure complexity with some mathematical instruments relying on an intuitve understanding of this concept. One example is depicted at figure 3, where you can see a comparison between young (left) and old (right) neurons. If we would measure a [fractal dimensions](https://en.wikipedia.org/wiki/Fractal_dimension) of left and right structures we would detect deacreasing in this measure. Intuitively it's correct: the left structure looks more complex than the right counterpart, at least, because of the left arbor has more branches.

<img src="<picture 3 from Lipsitz paper>" 
     alt="dendridic" 
     width="200"/>
<p align = "center">
Fig.3 - Age-related loss of fractal structure in the dendritic arbor of the giant pyramidal Betz cell of the motor cortex.
</p>

But may be another example from the same paper will be more intelligible. Look at the figure 4, where you can see heart rate dynamics of young (top) and old (bottom) individuals. We see that top and bottom signal are statistically different. From spectral theory point of view we could say that top signal has more higher frequencies in its spectrum. This means that heart rate signal tends to lose high frequency components as we age. Another way to express this behavior of signal is to measure its entropy. Since the entropy by definition is a *measure of the amount of information needed to predict the future state of the system*, the higher entropy signal has, the higher its complexity. The fact is that top signal has higher entropy than lower one, so, within the aforementioned terms, we again observe a loss of complexity with aging. The observation of complexity decreasing can inspire us to make a next step for studying the phenomenon. For example, in {cite}`lipsitz1992loss` mentioned that the age-related decline in heart rate variability is likely due to dropout of sinus node cells, altered $\beta$-adrenoceptor responsiveness, and reduction in parasympathetic tone.

<img src="<picture 1 from Lipsitz paper>" 
     alt="dendridic" 
     width="200"/>
<p align = "center">
Fig.4 - Heart rate time series for a 22-year-old female subject (top panel) and a 73-year-old male subject (bottom panel).
</p>

It turns out, that the idea to use entropy as a measure of complexity creates a contradiction.  One of the hallmark of aging, genomic instability, was shown to increase entropy with aging. Somatic mutations and spontaneous double strand breaks (DSB) contributes to general "loss of genomic information" (and, therefore, entropy increase) what is associated with aging. Moreover, in the experiment with mice genectically modified for induction DSB show patterns of accelerated aging {cite}`hayano2019dna`, {cite}`yang2019erosion`. Does it mean that aging is not coupled with a loss of complexity? Yes and No, it is rather coupled with poor mathematical counterpart of complexity concept, namely entropy. 

:::{note}
But we can also imagine an another explanation. The loss of information - increase in complexity - on the level of genome leads to degradation in information transition to higher levels of system organization which manifests as loss of complexity. We could even speculate that aging is a loss of the ability to information transition - but we are not ready to provide enough arguments for this view. 
:::

In total, complexity looks like a useful term to make things simpler. Its intuitive accessibility hints us mathematical frameworks for its measurement and highlights biological phenomena for its interpretation. Thinking about system complexity helps us to extract the most general properties of the object of study.

:::{note}
Some additional definitions of [complexity](https://en.wikipedia.org/wiki/Complexity):
- In general, number of systems and links between them describing a model.
- In dynamical systems, statistical complexity measures the size of the minimum program able to statistically reproduce the patterns (configurations) contained in the data set (sequence) {cite}`crutchfield1989inferring`.
- In information processing, complexity is a measure of the total number of properties transmitted by an object and detected by an observer.
:::

## Networks and Biological degeneracy

- Auto-encoder metaphor

* networks have evolved specific structures that allow the system to synthesize large numbers of inputs, make an informed decision and then subsequently regulate large numbers of outputs, while still maintaining evolvability42,45. One such information structure is a ‘bowtie’95,96, with fewer comp

* Having few intermediate pathways is known as ‘degeneracy,’ in the sense that each pathway serves multiple functions.

* The same pathways that are implicated in inflammation are also implicated in regulating oxidative stress, cancer, reproduction and metabolism. This is a natural consequence of the network’s degeneracy and its integration of information to optimize dynamic equilibrium.

* In this context, traditional notions of causality break down103: when causality is sufficiently circular or contingent, it no longer makes sense to claim that A causes B. For example, depending on their cellular context, calpains may either activate caspase 3, leading to apoptosis, or degrade caspase 3, preventing apoptosis104.

* a traditional perspective suggests that single-molecule interventions will be found that substantially slow aging, and indeed many researchers are pursuing such approaches.

* On the cellular scale, the mathematized MARS (mitochondria, aberrant proteins, radicals and scavengers) model describes the breakdown of cellular homeostasis in a networked approach 12
12. Kowald, A. & Kirkwood, T. B. L. A network theory of ageing: the interactions of defective mitochondria, aberrant proteins, free radicals and scavengers in the ageing process

Nijhout, H. F., Sadre-Marandi, F., Best, J. & Reed, M. C. Systems biology of phenotypic robustness and plasticity. Integr. Comp. Biol. 57, 171–184 (2017).

* Top-down computational models with discrete health states interacting with simple explicit networks116–118 have demonstrated how population-level measures such as survival curves can be generated from conceptually simple models of damage propagation within a complex system.

Recent advances in machine learning have allowed general dynamics of continuous longitudinal data to be modeled by deep neural networks for more than 29 covariants121.
121. Farrell, S., Mitnitski, A., Rockwood, K. & Rutenberg, A. D. Interpretable machine learning for high-dimensional trajectories of aging health. PLoS Comput Biol. 18, e1009746 (2022).

## Emergence and Canalization

- complexity связано с emergence

* Biological age as an emerging feature
* frailty, falls and delirium - emergent states
(gene expression example) https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.94.128701

* One common way that emergence arises is through canalization (Box 1), the tendency of the system to converge toward one of a limited number of discrete states

* Canalization and emergence often arise because biological networks can achieve robustness through redundancy, and so become buffered against perturbations—they are able to maintain a dynamic functional stability even when environmental or internal conditions change. This buffering often means that the same functional result can be achieved by multiple alternative pathways, strategies or system states. for example, during skeletal muscle aging, impaired chaperonemediated autophagy appears to be compensated by upregulation of macro-autophagy.

* For example, cellular senescence is a relatively discrete state, an alternative to being a healthy cell or to apoptosis. Senescence is thus an attractor state, with many intermediate states within its ‘attractor basin.’

* Furthermore, mechanisms can emerge at higher scales (for example, tooth wear64) or can have effects from higher scales to lower scales (for example, impacts of psychological stress on telomere length65)



## Resilience and Critical transitions

- https://www.nature.com/articles/nature08227 - temporal autocorrelations, variance and other signs of loss of resilience
- Ives, A. R. Measuring resilience in stochastic systems. Ecol. Monogr. 65, 217–233 (1995).
- Klein, B. et al. A computational exploration of resilience and evolvability of protein–protein interaction networks. Commun. Biol. 4, 1–11 (2021).

*The variance and temporal autocorrelation of time series are expected to increase as resilience decreases.

* If physiological systems are networks of interacting elements, then we can apply stochastic resilience theory to interpret dynamics of a whole suite of biological markers with aging. A key feature providing resilience to interacting networks is self-regulation within modules, while interactions among them might decrease resilience (but see ref. 79).

* One could therefore ask how these two fundamental quantities change during aging. In particular, the variance of individual markers and the temporal covariances among them are expected to increase with age.


**resilience in aging** 
80. Ukraintseva, S. et al. Decline in biological resilience as key manifestation of aging: potential mechanisms and role in health and longevity. Mech. Ageing Dev. 194, 111418 (2021). 
81. Schosserer, M. et al. Modelling physical resilience in ageing mice. Mech. Ageing Dev. 177, 91–102 (2019). 
82. Hadley, E. C., Kuchel, G. A. & Newman, A. B. Workshop Speakers and Participants. Report: NIA workshop on measures of physiologic resiliencies in human aging. J. Gerontol. A Biol. Sci. Med. Sci. 72, 980–990 (2017). 
83. Gijzel, S. M. W. et al. Dynamical resilience indicators in time series of self-rated health correspond to frailty levels in older adults. J. Gerontol. A Biol. Sci. Med. Sci. 72, 991–996 (2017). 
84. Liu, M. et al. Prediction of mortality in hemodialysis patients using moving multivariate distance. Front. Physiol. 12, 612494 (2021).
85. Varadhan, R., Seplaki, C. L., Xue, Q. L., Bandeen-Roche, K. & Fried, L. P. Stimulus-response paradigm for characterizing the loss of resilience in homeostatic regulation associated with frailty. Mech. Ageing Dev. 129,
86. Kalyani, R. R., Varadhan, R., Weiss, C. O., Fried, L. P. & Cappola, A. R. Frailty status and altered glucose-insulin dynamics. J. Gerontol. A Biol. Sci. Med. Sci. 67, 1300–1306 (2012).


## Extra (my thoughts)

Should we define those components of the system which are sources (all links are outgoing) - it might be that such nodes contribute more to aging

Aging is a loss of information transition ability



*Text written by Dmitrii Kriukov*
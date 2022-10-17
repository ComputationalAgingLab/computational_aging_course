# Complex systems approach

*Nothing in aging biology makes sense except in the light of dynamic equilibrium.*

Aging biology today is not an engineering but science at its early step. This expresses in that we frequently cannot observe a direct causal and numerically tractable relationships (as in physics) but we are doomed to see mostly *associations* and *patterns*. However, it may also be a good starting point for dynamical modeling. Large volumes of data and absense of organizing paradigm are major challenges of the modern aging biology. Complex systems approaches provide some computational instruments and necessary vocabulary for simplification, understanding and identification the essential features from data. This chapter partly relies on recent work of {cite}`cohen2022complex` where corresponding philosophical framework as well as important computational examples were proposed.

Throughout this chapter, you may come across many new words: system, complexity, networks, emergence, resilience and critical transitions. They form an important minimal vocabulary neccessary for developing complex systems intuition which (we believe) can be greatly useful for any researcher. We organize them in subsections and uncover one by one.

## Complex systems perspective on aging

Before the consideration of complex systems we should understand what we had before. 

- Top-Down and Bottom-Up approaches: example with observation that patient state change is associated with changing in some protein and experiment where you change this protein amount and observe the change in patient state

<img src="<picture Box 1 from Cohen paper>" 
     alt="parallel" 
     width="180"/>

- switch to complexity

<img src="<picture 1 from Cohen paper>" 
     alt="parallel" 
     width="180"/>

-One, already became Classical, alternative to Top-Down/Bottom-Up paradigm are hallmarks or pillars of aging

* Complex systems can be as diverse as ecosystems, economies, traffic systems and even the internet32–34, but are often surprisingly similar in their characteristics and behavior. Core hallmarks of complex systems include: 
1. networks of interacting elements (for example, interactions among molecules in key aging pathways such as hypoxia-inducible factor (HIF)-1, AMP-activated protein kinase (AMPK), mechanistic target of rapamycin (mTOR), sirtuins, insulin-like growth factor (IGF)-1R and forkhead box O (FOXO)35 (Fig. 2c,e,h); 
2. feedback/feedforward loops (for example, adaptive loops such as blood pressure regulation36 and maladaptive or runaway loops such as cellular senescence increasing the senescence associated secretory phenotype (SASP), which increases cellular senescence through paracrine signaling37,38; Fig. 2d); 
3. a multiscale or modular hierarchical structure (for example, organelles, nested in cells nested within tissues nested within organs, together with how damage propagates up, down or across such structures during aging39,40);  
4. emergent properties, which are properties of a system that cannot be directly or additively inferred by examining its component parts (for example, cognitive decline or loss of mobility cannot be understood simply as the sum of multiple aging cells; Fig. 2a,b,d,f).

- говоря об абстрактных свойствах систем, мы должны обязательно иметь ввиду конкретные воплощения этих свойств, иначе плохо


## Aging as loss of Complexity

- Lipsitz paper examples

- measurement and mechanisms (one mechanism from Lipsitz paper): top-down & bottom-up approaches examples. 

- Counter example, increasing complexity in DNA, epigenetics with aging (Sinclair’s view) (see also picture in the phone about information loss propagation)

- example with ECG signal - increase in recovery rate, autocorrelation and variance

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
# Complex systems approach

*Nothing in aging biology makes sense except in the light of dynamic equilibrium.*

Aging biology today is not engineering but science at its early step. This expresses that we frequently cannot observe direct causal and numerically tractable relationships (as in physics) but we are doomed to see mostly *associations* and *patterns*. However, it may also be a good starting point for dynamic modeling. Large volumes of data and the absence of an organizing paradigm are major challenges of modern aging biology. Complex systems approaches provide some computational instruments and necessary vocabulary for simplification, understanding, and identification of the essential features of data. Throughout this chapter, you will come across many new words: **system**, **complexity**, **networks**, **emergence**, **resilience**, and **critical transitions**. They form an important minimal vocabulary necessary for developing complex systems intuition which (we believe) can be greatly useful for any researcher. We organize them into subsections and uncover them one by one. This chapter partly relies on the recent work of {cite}`cohen2022complex` where corresponding philosophical framework, as well as important computational examples, were proposed.

```{contents}
```

## Complex systems perspective on aging

Before the consideration of complex systems, we should understand what we had before. Typical two common approaches in sciences are **Top-Down** and **Bottom-Up**. Let the object of study is a human organism, then the Top-Down approach asks the question of which large-scale observations are associated with small scale. For example, a patient's state change is associated with changing a level of some protein. And vice versa, the Bottom-Up approach asks whether a large-scale patient's state changes after perturbation of some protein level. Moving Bottom-Up generates something we call metabolic pathways, gene ontologies, etc. - i.e. combining small-scale entities into new higher-scale entities. In turn, moving Top-Down we can differentiate new entities such as organs, tissues, cells, organelles, and nuclei at a smaller scale ({numref}`topdown`). You might have noticed that science greatly advanced by applying only these two approaches. However, an encounter with living systems forces us to develop a new methodology. The problem with that two approaches is that they do not take into account interactions between feedback/feedforward loops at too different scales trying to provide a mechanistic explanation of processes in a level-by-level manner. They provide theories like **A causes B** and **B causes C** whilst in real complex systems we observe behaviors like **A causes B**, **B causes A**,  **B causes C** and **C causes A and B**. Do you agree that this no more presumes a one-dimensional schematic explanation of the mechanism of action? Such an abundance of causal relationships forces us to use the concept of **networks** for building a more correct body of knowledge.

:::{note}
For example, depending on their cellular context, [calpains](https://en.wikipedia.org/wiki/Calpain) may either activate [caspase](https://en.wikipedia.org/wiki/Caspase) 3, leading to apoptosis, or degrade caspase 3, preventing apoptosis {cite}`lopatniuk2011conventional`.
:::

```{figure} figs/topdown.png
:name: topdown
:width: 800
Example of Top-Down and Bottom-Up organization of knowledge.
```

Cohen and colleagues {cite}`cohen2022complex` provide a great example of such a *switch to complexity* that happened in ecological sciences recently ({numref}`complex`). You can see that a previously popular *food chains* theory was changed by a system approach where interactions between species form a complex network where it is not obvious how the system will respond to removing a particular species. Currently, we observe a similar transformation in aging domain. Two great examples (and already classical) of such a transformation are Hallmarks of aging {cite}`lopez2013hallmarks` and Pillars of aging {cite}`kennedy2014geroscience` papers trying to highlight a set of key entities related to aging and connecting them into a network of interacting elements. Thinking in a complex systems paradigm challenges a traditional perspective that single-molecule interventions will be found that substantially slow aging (indeed many researchers are pursuing such approaches). Instead, we should focus on a combinatorial approach requiring, however, a robust model of the system under treatment.

```{figure} figs/complex.png
:name: complex
:width: 800
Shift to complex systems approaches in ecology and aging biology.
```

:::{note}
- **Top-Down approach** -- methodology of connecting large-scale observations with smaller-scale ones by differentiation of large object to smaller entities.
- **Bottom-Up approach** -- methodology of connecting smaller scale observations with larger scale ones by a combination of small objects into larger entities.
:::

Examples of complex systems include ecosystems, economies, traffic systems, power systems, etc. It is a kind of magic that all of them, nevertheless, have common properties or hallmarks. Core hallmarks of complex systems include: 
1. networks of interacting elements (for example, interactions among molecules in key aging pathways such as AMP-activated protein kinase (AMPK), mechanistic target of rapamycin (mTOR), sirtuins, insulin-like growth factor); 
2. feedback/feedforward loops (for example, adaptive loops such as blood pressure regulation); 
3. multiscale or modular hierarchical structure (for example, organelles, nested in cells nested within tissues nested within organs); 
4. emergent properties, which are properties of a system that cannot be directly or additively inferred by examining its component parts (for example, cognitive decline cannot be understood simply as the sum of multiple aging cells;).

:::{note}
Cohen et al. {cite}`cohen2022complex` also mention *nonlinear dynamics* as a hallmark of complex systems. But we do not see enough arguments to include this point as a hallmark. In our view, complex systems can also have linear dynamics describing a set of linear ordinary differential equations for instance.
:::

Before we proceed, let's introduce one important rule which helps you to differentiate "bad" complex systems propositions from "good" ones. Any abstract philosophical concepts you will discover about complex systems (such as complexity or resilience) in the future **must** be reinforced with a concrete embodiment in mathematical or biological terms.


## Aging as loss of Complexity

What can be one of the most common characteristics of aging? Can we express the plethora of our observations of an aging organism by one cumulative term? It turns out, we can consider the topological characteristics of complex living systems comparing them at different time moments (at young and old ages). The **complexity** was proposed as such characteristic in {cite}`lipsitz1992loss` where authors suggested that aging is associated with "loss of complexity". It is tough to define "complexity" explicitly and the authors do not give such a definition. Instead, they measure complexity with some mathematical instruments relying on an intuitive understanding of this concept. One example is depicted at {numref}`dendridic`, where you can see a comparison between young (left) and old (right) neurons. If we would measure a [fractal dimensions](https://en.wikipedia.org/wiki/Fractal_dimension) of left and right structures we would detect decreasing in this measure. Intuitively it's correct: the left structure looks more complex than the right counterpart, at least, because the left arbor has more branches.

```{figure} figs/dendridic.png
:name: dendridic
:width: 600
Age-related loss of fractal structure in the dendritic arbor of the giant pyramidal Betz cell of the motor cortex.
```

But maybe another example from the same paper will be more intelligible. Look at the {numref}`ecg`, where you can see the heart rate dynamics of young (top) and old (bottom) individuals. We see that the top and bottom signals are statistically different. From the spectral theory point of view, we could say that the top signal has more high frequencies in its spectrum. This means that the heart rate signal tends to lose high-frequency components as we age. Another way to express this behavior of signal is to measure its Shannon's entropy {cite}`shannon1948mathematical`. Since entropy by definition is a *measure of the amount of information needed to predict the future state of the system*, the higher entropy signal has, the higher its complexity is. The fact is that top signal has higher entropy than lower one, so, within the aforementioned terms, we again observe a loss of complexity with aging. The observation of complexity decreasing can inspire us to make the next step in studying the phenomenon. For example, in {cite}`lipsitz1992loss` mentioned that the age-related decline in heart rate variability is likely due to dropout of sinus node cells, altered $\beta$-adrenoceptor responsiveness, and reduction in parasympathetic tone.

```{figure} figs/ecg.png
:name: ecg
:width: 600
Heart rate time series for a 22-year-old female subject (top panel) and a 73-year-old male subject (bottom panel).
```

<!-- entropy as a measure of aging??? --> 
It turns out, that the idea to use entropy as a measure of complexity creates a contradiction.  One of the hallmarks of aging, genomic instability, was shown to increase entropy with aging. Somatic mutations and spontaneous double-strand breaks (DSB) contribute to the general "loss of genomic information" (and, therefore, entropy increase) that is associated with aging. Moreover, in the experiment with mice genetically modified for induction DSB show patterns of accelerated aging {cite}`hayano2019dna`, {cite}`yang2019erosion`. Does it mean that aging is not coupled with a loss of complexity? Yes, and No, it is rather coupled with the poor mathematical counterpart of complexity concept, namely entropy. 

:::{note}
But we can also imagine another explanation. The loss of information - increase in complexity - on the level of genome leads to degradation in information transition to higher levels of system organization which manifests as loss of complexity. We could even speculate that aging is a loss of the ability to information transition - but we are not ready to provide enough arguments for this view. 
:::

In total, complexity looks like a useful term to make things simpler. Its intuitive accessibility hints us mathematical frameworks for its measurement and highlights biological phenomena for its interpretation. Thinking about system complexity helps us to extract the most general properties of the object of study.

:::{note}
Some additional definitions of [complexity](https://en.wikipedia.org/wiki/Complexity):
- In general, the number of systems and links between them describing a model.
- In dynamical systems, statistical complexity measures the size of the minimum program able to statistically reproduce the patterns (configurations) contained in the data set (sequence) {cite}`crutchfield1989inferring`.
- In information processing, complexity is a measure of the total number of properties transmitted by an object and detected by an observer.
:::

```{admonition} Exercise 1
:class: dropdown
Look up the table in {cite}`lipsitz1992loss`; [link](https://www.researchgate.net/profile/Lewis-Lipsitz/publication/236319288_Loss_of_'Complexity'_and_AgingPotential_Applications_of_Fractals_and_Chaos_Theory_to_Senescence/links/00b4952c58b5b6bbf5000000/Loss-of-Complexity-and-AgingPotential-Applications-of-Fractals-and-Chaos-Theory-to-Senescence.pdf). Choose one "loss of complexity" fact and corresponding measure from the table. Check out the original study where the loss of complexity was shown. Do you trust the approach suggested in this article? Explain your answer. Try to find more recent research on this topic. If you succeed, add a reference to the report.
```

## Networks and Biological degeneracy

Biological systems can be viewed as complex networks of interacting components. This simple idea may seem quite naive until we start to consider structural properties of these networks. **Bow-tie** or hourglass structure is a common structural feature found in many biological systems. A bow-tie means that a large number of inputs are converted to a small number of intermediates, which then fan out to generate a large number of outputs ({numref}`bowtie`) {cite}`cohen2022complex` (looks like autoencoder isn't it?). The important principle lying behind bow-tie formation is called **degeneracy** {cite}`edelman2001degeneracy`. In a biological sense, this means the ability of structurally different biological elements (e.g. proteins or metabolites) to perform the same function. Two examples of bow-tie include metabolic networks, where the large range of nutrients consumed by the organism is decomposed into 12 universal precursors (including pyruvate, G6P, AKG, ACCOA) from which the organism builds all of its biomass including carbohydrates, nucleic acids and proteins; the human visual system having $\sim 10^8$ input photoreceptors in the retina which fans in to only about $\sim 10^6$ ganglion cells whose axons form the optic nerve going to visual cortex that detects a pattern, color, depth and movement {cite}`friedlander2015evolution`. In the context of aging biology bow-tie structure expresses in the ability of the same pathways to be simultaneously implicated in inflammation, regulating oxidative stress, cancer, reproduction and metabolism ({numref}`bowtie`). This is a natural consequence of the network’s degeneracy by integrating information from multiple inputs and inflating it to multiple outputs. There is a lot of evidence that degeneracy is an important property of evolving systems and may be even a *prerequisite* for evolution {cite}`edelman2001degeneracy`.

:::{note}
**Bow-tie** - network structure assuming that a large number of inputs are converted to a small number of intermediates, which then fan out to generate a large number of outputs.
**Degeneracy** - the ability of structurally different elements to perform the same function. Degeneracy should not be confused with redundancy, which occurs when the same function is performed by identical elements, degeneracy, which involves structurally different elements, may yield the same or different functions depending on the context in which it is expressed {cite}`edelman2001degeneracy`.
:::

```{figure} figs/bowtie.png
:name: bowtie
:width: 800
Bowtie structure of aging pathways.
```

What technical outcomes we can obtain from bow-tie networks? So, the presense of low-dimensional intermediate layer hints us that application of dimensionality reduction techniques to biological data is a good decision. It is the fact that many biological entries (e.g. expression level of different genes) are highly correlated with each other {cite}`podolskiy2015critical` and a huge dimensionality of inputs can be satisfactorily described by a small number of latent parameters. Latent parameter is a mathematical term describing low-dimensional linear (or nonlinear) combination of inputs. This is not a big deal to compute a latent parameter according to some model. The more important thing is to give a correct biological interpretation for this parameter. Sometimes latent parameters do not have a clear interpretation but in other cases, a particular latent parameter may catch a clear biological process such as expression of one of the metabolic precursors mentioned above.

## Emergence and Canalization

The natural property of human counciousness (and, need to say, its bias) is a tendency to simplify things by extracting their common pattern. We call a propery of a system is **emergent** if we do not see this property of any system component. By discovering emergent properties of the system we cope with its **complexity**. Classical examples of emergent properties in physical systems are temperature of a gas and fluidity of a fluid - in both cases we do not see such properties in system components (molecules). Revealed emergent properties are especially useful when we can to measure them. Biological systems are abundant by emergences. Moreover, the concept of Life is a typical example of emergence. One common way that emergence arises in biological systems is through **canalization**, the tendency of the system to converge toward one of a limited number of discrete states {cite}`cohen2022complex`. Once again, if the system can take distinguishable states and these states seem not to be emanating from properties of its components then these states are emergent. An immediate example is acquiring somatic cell state (or cell fate) through differentiantion ({numref}`landscape`) from pluripotent one {cite}`takahashi2016decade`. It is quite remarkable, in spite of the huge complexity of a human cell as a system it has a rather small number of discrete (distinguishable) somatic states that was shown experimentally {cite}`huang2005cell`.

:::{note}
**Emergence** - a high-level property of a system, which is not a property of any component of that system. This intractability can be variously interpreted. In weak emergence interpretations, the inexplicability is merely a practical one due to the sheer complexity of the computation required to reach an explanation. In strong emergence interpretations, the emergent property possesses causal autonomy independently of its constituents {cite}`o2022critical`.
**Canalization** - the tendency of the system to converge toward one of a limited number of discrete states.
:::

```{figure} figs/landscape.png
:name: landscape
:width: 600
Waddington landscape - a metaphor of cell fate transition during differentiantion as a ball rolling down from the top of Waddington’s "mountain" (pluripotency) to the bottom of a "valley" (somatic state, e.g. skin, muscle). The opposite process is called reprogramming.
```

Canalization and emergence often arise because biological networks can achieve robustness through **degeneracy**, and so become stable against perturbations - they are able to maintain a dynamic functional stability even when environmental or internal conditions change. This degeneracy, as we said above, means that the same functional result can be achieved by multiple alternative pathways, strategies or system states. For example, during skeletal muscle aging, impaired chaperonemediated autophagy appears to be compensated by upregulation of macro-autophagy {cite}`cohen2022complex`. Other aging-related examples of canalization include cellular senescence which is a relatively discrete state, an alternative to being a healthy cell or to apoptosis. Senescence is thus an attractor state, with many intermediate states within its "attractor basin". On the level of organism we can discover another emergences like frailty - clinically recognizable state of increased vulnerability resulting from aging-associated decline in reserve and function across multiple physiologic systems such that the ability to cope with everyday or acute stressors is comprised {cite}`xue2011frailty`. Finally, aging is another example of emergent organism property and as it was mentioned above, we highly favor attempts to measure this property.


## Resilience and Critical transitions

It is time to discuss **dynamic equilibrium** mentioned in the epigraph of this chapter. Dynamic equilibrium has two synonyms: **resilience** and **stability** - the first is more biological and the latter is more physical. But in majority of contexts they means the ability of a system to return in the equilibrium state preceding a perturbation. The common metaphor for understanding resilience is a ball in the hole model ({numref}`early`a,d). You can see that small perturbation barely can knock out ball from a basin with sharp and high walls (so called potential barrier) what is associated with high resilience of the system. On the other hand, low walls do not save ball from even a small perturbation. The event when a ball leave its current local minimum state and cross the boundary of its basin is called **critical transition** which we discuss below. Resilience can be measured and different measures of a resilience (including mathematically tractable) were proposed {cite}`varadhan2008stimulus`, {cite}`gavrilov2005reliability`, {cite}`gijzel2017dynamical`, {cite}`pyrkov2021longitudinal`, {cite}`schosserer2019modelling`. It is especially important to measure resilience in older adults to aware of the risks which they bear. Moreover, it was proposed that aging itself is a progressing loss of resilience {cite}`promislow2022resilience`. 

The resilience concept is tightly bounded with **critical transition** concept which has synonyms of (more physical) **phase transition** and (more mathematical) **bifurcation**. It is usually defined as a qualitative change in macroscopic properties of the system {cite}`o2022critical`. One important class of critical transitions is a **fold catastrophic transition** (which is also tempted to associate with the death of the organism) {cite}`scheffer2009early`. This transition is characterized by "sharp" falling the system parameter into a new state (we will cover mathematical details of this bifurcation in the next chapter). We are specially interest in this type of bifurcation because of the presence of early warning signals preceding the system critical transition which we can directly observe in the data. Suppose that our aging-related dataset contains a system variable characterizing its macroscopic state (examples include mentioned heart rate ({numref}`ecg`) or self-rated health evaluations {cite}`gijzel2017dynamical`) and this variable is presented in a form of one-dimensional time series for patients of different ages. Then, we can calculate variances and autocorrelations for all participants in the dataset. The bifurcation theory predicts that approaching to a critical transition boundary (aka tipping point) is accompained with the system **critical slowing down** and an increase in variance and temporal autocorrelations of the system state variable ({numref}`early`b,c,e,f) {cite}`scheffer2009early` and this is something that we expect to observe in real aging data. 

```{figure} figs/early.png
:name: early
:width: 800
a-c, Far from the bifurcation point (a), resilience is large in two respects: the basin of attraction is large and the rate of recovery from perturbations is relatively high. If such a system is stochastically forced, the resulting dynamics are characterized by low correlation between the states at subsequent time intervals (b, c). d–f, When the system is closer to the transition point (d), resilience decreases in two senses: the basin of attraction shrinks and the rate of recovery from small perturbations is lower. As a consequence of this slowing down, the system has a longer memory for perturbations, and its dynamics in a stochastic environment are characterized by a larger variance and a stronger correlation between subsequent states (e, f).
```

One interesting example of the critical slowing down can be found in frail patients ({numref}`glucose`) {cite}`kalyani2012frailty`. The figure represents a resulting dynamics of glucose in oral glucose tolerance test (OGTT) demonstrating slower recovery in glucose level after perturbation in frail patients by comparing with non-frail and pre-frail. Indeed, slowdown in metabolism, proliferation and information processing is a major feature of aging {cite}`ukraintseva2021decline`. Consequently, frail and non-frail individuals may differ in how they respond dynamically to stressors or drug perturbations. 

```{figure} figs/glucose.png
:name: glucose
:width: 400
Glucose dynamics during oral glucose tolerance test by frailty status. Mean ± SE (error bars) for glucose values respectively after a 75 g glucose load.
```

:::{note}
**Resilience** - the ability of a system to return in the equilibrium state preceding a perturbation.
**Critical transition** - a qualitative change in macroscopic properties of the system.
:::

## Summary: combining the learned concepts

Is the living organism the **complex** dynamical **network** of interacting elements acquiring discrete **emergent** states through the **canalization**, forming modules experiencing loss of **resilience** through the loss of **complexity** during aging and approaching its **critical transition** point ultimately falling in the death state? - the question is open for You!

Aging biology is, in particular, so challenging because of the absense of longitudinal high dense data: chemical signals are not so easy for measurements like electrical signals in neurons, moreover, data quality is rather poor frequently. 

Complex systems framework do not answer directly what molecule or intervention will repair the system by getting it back to the equilibrium state, but rather provide a useful methodology to evaluate this state and more precisely measure, control and study effects of any new molecules used for treatment. It also may point to what essential components of the system undergoes changes that manifest themselves as aging. Might it be a extracellular matrix degradation, genomic instability or mitochondrial disfunction? What system state parameter may unequivocally indicate loss of resilience and explain the reason of the loss. How can we define those elements of the system which contribute more to aging? - these are open questions. What we can do now is to make your dynamical systems intuition deeper in the next section.


## Credits
This text prepared by [Dmitrii Kriukov](https://scholar.google.com/citations?user=Wo9H1f4AAAAJ&hl=en).

## References

```{bibliography}
:style: plain
:filter: docname in docnames
```




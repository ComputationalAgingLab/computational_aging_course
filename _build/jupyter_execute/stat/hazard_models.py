#!/usr/bin/env python
# coding: utf-8

# # Hazard models
# 
# **Aging** - increased chance of death with age.
# 
# You have seen this picture on the previous lesson {cite}`lifetables`.  
# 
# ![Risk of mortality](https://upload.wikimedia.org/wikipedia/en/4/4d/USGompertzCurve.svg)
# 
# At this lesson we learn how to understand such mortality risk curves and much more. We will learn Gompertz model - the central conception in aging research.

# ## Survival curve
# 
# Let $T$ is a non-negative random variable with a corresponding distribution function:
# 
# $$F(t) = P(T\leq t)$$ 
# 
# We call $T$ - *survival time* or time before death of some object (e.g. human). For example, $T$ can have normal distribution:

# In[1]:


from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.size'] = '16' # increase font size

rv = norm(loc=4, scale=1.5)
t = np.linspace(0, norm.ppf(0.99, loc=4, scale=1.5), 100)
fig, ax = plt.subplots(1, 1)
ax.set_xlabel('Time')
ax.set_ylabel('Probability to die')
ax.plot(t, rv.cdf(t));


# If $F(t)$ is a probability to die before time moment $T$ we can introduce a probability to survive before this moment $S$ as just a complement to $F$:
# 
# $$S(t) = P(T > t) = 1 - F(t)$$ 
# 
# Let's draw it:

# In[2]:


rv = norm(loc=4, scale=1.5)
t = np.linspace(0, norm.ppf(0.99, loc=4, scale=1.5), 100)
fig, ax = plt.subplots(1, 1)
ax.set_xlabel('Time')
ax.set_ylabel('Probability to survive')
ax.plot(t, 1 - rv.cdf(t));


# This plot is what we actually call *survival curve*. The intuition behind this is rather straightforward - it shows how many of experimental objects survived before a partucular moment of time. You can see a lot of empirical versions of such curves in articles. Rigorous analysis of this curves helps to avoid a misinterpretation of typical drug-testing experiment or other. And it's what we are going to do in further.

# ## Mortality risk

# You could have heard that mortality risk increases exponentially with aging. But what does this actually mean?
# 
# ```{note}
# :class: dropdown
# Mortality risk is **not** a probability of death!
# ```
# 
# Let's consider instantaneous probability of death that the object will die within a time interval $dt$ by condition that it already survived to moment $T$:
# 
# $$\lim_{dt \to 0}\frac{P(t < T ≤ t + dt | T > t)}{dt}$$
# 
# This conditional probability can be decomposed by definition as follows: 
# 
# $$P(A ∩ B) = P(A|B)P(B)$$
# 
# This yields:
# 
# $$P(t < T ≤ t + dt ∩ T > t) = P(t < T ≤ t + dt | T > t)P(T > t)$$
# 
# $$P(t < T ≤ t + dt | T > t) = \frac{P(t < T ≤ t + dt ∩ T > t)}{P(T > t)}$$
# 
# Recall that $P(T > t) = 1 - F(t) = S(t)$ and $P(t < T ≤ t + dt) = F(t+dt) - F(t)$.
# 
# ```{note}
# :class: dropdown
# To understand the last property it is enough to remember that probability function is just a square under probability density function!
# ```
# 
# Now let's rewrite our result:
# 
# $$P(t < T ≤ t + dt | T > t) = \frac{F(t+dt) - F(t)}{S(t)}$$
# 
# It's time to put our derivation to the first formula with a limit. So, we have:
# 
# $$\lim_{dt \to 0}\frac{P(t < T ≤ t + dt | T > t)}{dt} = \lim_{dt \to 0}\frac{F(t+dt) - F(t)}{dt}\frac{1}{S(t)} = \frac{f(t)}{S(t)}$$
# 
# Yes, we obtained a ratio of probability density function of death and probability of survival. And this is what we call **mortality risk function** or hazard function.
# 
# $$m(t) = \frac{f(t)}{S(t)} = -\frac{S'(t)}{S(t)}$$
# 
# ```{admonition} Exercise
# :class: dropdown
# Show that $f(t) = -S'(t)$.
# ```
# 
# This is actually the thing that increases exponentially as we age and have a name of Gompertz law (quite more complex than just a probability, isn't it?). Now let's consider different kinds of such functions.

# ## Gompertz law and other kinds of mortality functions

# ### Constant risk model
# 
# We start with the simplest case of a constant mortality function. 
# 
# $$
#     m(t) = m_0
# $$
# $$
#     S(t) = \exp(-m_0t)
# $$
# $$
#     f(t) = m_0\cdot \exp(-m_0t)
# $$
# 
# ```{admonition} Exercise
# :class: dropdown
# Derive an expression for $S(t)$ at constant risk. **Hint:** use the result from the previous exercise.
# ```
# 
# Let's draw plots for $m$ and $S$:

# In[3]:


t = np.linspace(0, 20, 200)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

m0 = 0.1

ax[0].plot(t, np.ones(len(t)) * m0)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Mortality risk')

ax[1].plot(t, np.exp(-m0*t))
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Probability of survival');


# The corresponding survival curve resembles a [distribution](https://en.wikipedia.org/wiki/Exponential_distribution) of time until radioactive particle decay or so called *"law of rare events"* where events independently occur with a rate $m_0$. Intuitively, we can treat this survival curve describing survivability of an extremely fragile organism, which dies from a single failure - technically speaking, such organism is unaging! Then, $m_0$ actually describes average number of failures per unit of time and, correspondingly, $1/m_0$ - is a **mean survival time**.
# 
# ```{admonition} Exercise
# :class: dropdown
# Prove that $1/m_0$ - is a mean survival time using a definition of expectation.
# ```

# We obtained an object, or system, with survivability depending on one critical subsystem what is not reliable. Can we do better? Sure, we can add an additional critical sustystem reserving the original. As a naive example, just imagine an organism's life depends only of two kidney functioning. If one fails the other can work for two. This (of course) oversimplified system can be represented with the following diagram of parallel connection,
# 
# <img src="../stat/figs/parallel.png" alt="parallel" width="180"/>
# 
# where $m_1$ and $m_2$ are failure risks, which we assume constant and not equal in general. How to derive a survival curve for such a system? First, let's assume that both critical subsystems, let's call them $X$ and $Y$, are independent what means that the failure of one does not affect the failure rate of the other. Then, we may consider joint probability distribution that the whole system fails:
# 
# $$ F_{X,Y}(t) = F_X(t)\cdot F_Y(t) $$
# 
# Recall that $F(t) = 1-S(t)$,
# 
# $$ F_{X,Y}(t) = (1-S_X(t))\cdot (1-S_Y(t)) = (1 - e^{-m_1t})(1 - e^{-m_2t}) = 1 - e^{-m_1t} -  e^{-m_2t} +  e^{-(m_1+m_2)t}$$
# 
# And now we return to survival curve:
# 
# $$ S_{X,Y}(t) = e^{-m_1t} +  e^{-m_2t} -  e^{-(m_1+m_2)t}$$
# 
# $$ m_{X,Y}(t) = \frac{-S_{X,Y}'(t)}{S_{X,Y}(t)} = \frac{m_1e^{-m_1t} +  m_2e^{-m_2t} -  (m_1 + m_2)e^{-(m_1+m_2)t}}{e^{-m_1t} +  e^{-m_2t} -  e^{-(m_1+m_2)t}}$$
# 
# Let's draw it!

# In[4]:


t = np.linspace(0, 40, 200)
m1 = 0.1
m2 = 0.2

dt = t[1] - t[0]
SX = np.exp(-m1*t)
SY = np.exp(-m2*t)
SXY = np.exp(-m1*t) + np.exp(-m2*t) - np.exp(-(m1 + m2)*t) 
mXY = (m1 * np.exp(-m1*t) + m2 * np.exp(-m2*t) - (m1 + m2) * np.exp(-(m1 + m2)*t)) /      (np.exp(-m1*t) + np.exp(-m2*t) - np.exp(-(m1 + m2)*t))

fig, ax = plt.subplots(1, 2, figsize=(13, 5), constrained_layout=True)

ax[0].plot(t, [m1] * len(t), label=f'X only, m1={m1}')
ax[0].plot(t, [m2] * len(t), label=f'Y only, m2={m2}')
ax[0].plot(t, mXY, label='X or Y')
ax[0].legend()
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Mortality risk');

ax[1].plot(t, SX, label=f'X only, m1={m1}')
ax[1].plot(t, SY, label=f'Y only, m2={m2}')
ax[1].plot(t, SXY, label='X or Y')
ax[1].legend()
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Probability of survival');


# We see the lower value of mortality risk the higher survival curve lies if we consider our kidneys (critical subsystems) separately. Combining them into one system leads to the highest survival curve (green curve on the plot). Thus we see a quite obvious corollary: the higher number of reserved subsystems object have the more survival it becomes... But wait a second! What's wrong with the mortality curve for two kindeys system? It is not constant now. We started with two kidneys each having its own constant failure risk and ended with a system where mortality risk is now a function of time - **aging system** actually! It is quite reasonable if we treat aging as a process of critical subsystem failures culminating with system "death". 
# 
# In fact, you may consider human organism as a just a combination of parallel and sequential connections of such critical subsystems (organs) - not bad model for a start (see, for example {cite}`gavrilov2005reliability`). To calculate a survival curve of a particular complex model, you may just use the following formulas considering your system as a set of sequential and parallel block connections.
#  
# <img src="https://nanohub.org/app/site/resources/2013/01/16583/slides/016.03.jpg" alt="connections" width="600"/>
# 
# ```{admonition} Exercise
# :class: dropdown
# Compute an expression for mortality risk of sequential subsystems connection.
# ```

# ### Weibull risk model

# In[5]:


# note that exponential distr is a particular case of Weibull at k=1


# ### Gompertz risk model

# ### Other cases
# 
# * Log-Norm: $log(T) \sim \mathcal{N}$ - if 
# * Raeley: $m_0 + m_1(t)$
# * Decreasing: after surgery

# ## Comparison of survival curves

# In[6]:


from lifelines.datasets import load_waltons


# In[7]:


load_waltons()


# ## Cox proportional hazard model

# In[8]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);


# ## Learn more
# * [Reliability theory textbook](https://crr.umd.edu/sites/crr.umd.edu/files/Free%20Ebook%20Probability%20Distributions%20Used%20in%20Reliability%20Engineering.pdf)
# * [Russian video lecture](https://www.youtube.com/watch?v=rLNzoYmnkgQ&ab_channel=ComputerScienceCenter).
# * [Gompertz model colab notebook by Alexander Fedintsev](https://colab.research.google.com/drive/1Po-OMzIJ_4hVVj5O7btc8OmjJlu0N3cQ?usp=sharing#scrollTo=-_cpx007cIMn)
# * [Python library for hazard modeling](https://lifelines.readthedocs.io/en/latest/index.html)

# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)

# ## Credits
# 
# This notebook was prepared by [Dmitrii Kriukov](https://scholar.google.com/citations?user=Wo9H1f4AAAAJ&hl=ru).
# 
# ## Acknowledgements
# 
# We thank [Alexander Fedintsev](https://scholar.google.com/citations?hl=ru&user=J2F6xmcAAAAJ&view_op=list_works&sortby=pubdate), who made a significant contribution to the theoretical part of this notebook.

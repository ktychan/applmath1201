# Introduction to Probability

Some people say, nothing in life is certain. Even if that's not true, life can be so complicated that, like a game of roulette, it is adequately modelled as the result of chance events. No course in biological modelling, then, is complete without a treatment of probabilistic approaches to model construction. Before we do that, though, we need to establish some  terminology commonly used in probability theory, and we need to lay out the basic mathematical ideas alongside their applications to the study of biology. Those are the principal goals of this chapter. 

## Outcomes, Events, and Probability

In probability theory, we are interested in experiments whose outcomes are uncertain. When studying a given experiment, we pay particular attention to the set of all possible outcomes, otherwise known as *the sample space* of the experiment, {math}`\Omega`. An example of an experiment that gets a lot of attention in math classes is rolling a six-sided die, and in this case {math}`\Omega` is the set of integers from {math}`1` to {math}`6`, that is {math}`\Omega = \{ 1, 2, 3, 4, 5, 6\}`. 

We use the term *event* to refer to a subset\footnote{The empty set, denoted {math}`\emptyset`, contains no elements and is always a subset of any given set.} of {math}`\Omega`. For example, the event that we have rolled an even number corresponds to the subset {math}`E=\{ 2,4,6\}` contained in {math}`\Omega`. Given any event {math}`E` we can construct a new event called *the complement of* {math}`E`, and denoted {math}`E^c`. The set {math}`E^c` contains all elements of {math}`\Omega` not found in {math}`E`. If {math}`E` is the event that we have rolled an even number, then {math}`E^c = \{ 1,3,5\}` and is understood as the event we have rolled an odd number. 

Given any two events, say {math}`E` and {math}`F`, we can construct two new events denoted {math}`E\cup F` and {math}`E\cap F`, respectively. The former event is called the *union of* {math}`E` and {math}`F`, and it includes any outcome in {math}`\Omega` found either in {math}`E` *or* {math}`F` (or both). The latter event is called the *intersection* of {math}`E` and {math}`F`, and includes only those outcomes in {math}`\Omega` that are found in both {math}`E` *and* {math}`F`. As an example, if {math}`E=\{1,2\}` and {math}`F=\{2,3\}`, then {math}`E\cup F = \{1,2,3\}` and {math}`E\cap F =\{ 2\}`. 

In order to quantify the likelihood of a particular event, we introduce the function {math}`\mathbb{P}(E)`, which gives us the *probability of* {math}`E`. The function {math}`\mathbb{P}(E)` maps subsets of {math}`\Omega` to the unit interval {math}`[0,1]`. In particular, it maps the empty set to {math}`0` and the entire set of outcomes to {math}`1`; that is to say, {math}`\mathbb{P} (\emptyset) = 0` and {math}`\mathbb{P}(\Omega) = 1`. In the special case where {math}`\Omega` consists of a finite integer number of equally likely outcomes we can say
```{math}
  \mathbb{P}(E) = \frac{\text{number of outcomes in}\ E}{\text{total number of outcomes in}\ \Omega}.
``` 
If we roll a fair die, then every element of {math}`\Omega` is equally likely and we can say that the probability of rolling an even number is {math}`\frac{3}{6} = \frac{1}{2}`.

In addition to the properties above, we can show, using diagrams like that presented in Figure [](#fig:venn), that 
```{math}
  \mathbb{P} ( E\cup F) 
  =
  \mathbb{P}(E) + \mathbb{P}(F) - \mathbb{P}( E\cap F).
```
As an example here, if {math}`E=\{ 2, 4, 6\}` is the event that a fair die shows an even number when rolled, and {math}`F=\{ 1,2\}` is the event that a fair die shows a number less than {math}`3` when rolled, then  
```{math}
  \mathbb{P}( E \cup F ) 
  =
  \frac{3}{6} + \frac{2}{6} - \frac{1}{6} = \frac{2}{3}
```
is the probability that either {math}`E` or {math}`F` occurs.

:::{figure} ../standalones/build/diagram-venn-2sets.pdf
:label: fig:venn

The Inclusion-Exclusion Principle
:::

One consequence of the formula above is that for *mutually exclusive events* {math}`E` and {math}`F` (meaning {math}`E\cap F=\emptyset`) we have {math}`\mathbb{P}(E\cup F) = \mathbb{P} (E) + \mathbb{P}(F)`.	In turn, this result implies that for any *mutually exclusive and exhaustive* set of events {math}`E_1, \ldots E_n` (meaning {math}`E_i \cap E_j = \emptyset` when {math}`i\neq j`, and {math}`E_1 \cup \cdots \cup E_n = \Omega`) we have {math}`\mathbb{P}(   E_1 \cup \cdots \cup E_n ) = 1`. So, if {math}`E` is the event we have rolled an even number, and {math}`F` is the event we have rolled an odd number, then {math}`\mathbb{P}( E\cup F) = \mathbb{P}(E) + \mathbb{P}(F) = 1`, since {math}`E` and {math}`F`, together, represent a mutually exclusive and exhaustive set of events. 

## Conditional Probability and Independence

It is sometimes important to consider the likelihood of an event in light of the realization than another has occurred. We define the probability of {math}`F` given that {math}`E` has occurred -- or simply, *the probability of* {math}`F` *given* {math}`E` -- as
```{math}
  \mathbb{P}( F \mid  E) = \frac{\mathbb{P}(E \cap F)}{\mathbb{P}(E)}
```
which can be rearranged to give {math}`\mathbb{P}( F \mid  E) \mathbb{P}(E) =  \mathbb{P}(E \cap F)`. For instance, let {math}`F` be the event that a rolled die shows 2, and let {math}`E` be the event that the same rolled die shows an even number. Then,
```{math}
  \mathbb{P}( F \mid  E) 
  =
  \frac{\mathbb{P}( \{ 2\} )}{ \mathbb{P}( \{ 2, 4, 6\}) } = \frac{1/6}{3/6} = \frac{1}{3}.
```
By dividing by the probability of {math}`\{ 2, 4, 6\}` what we have done is effectively re-normalize the likelihood of rolling a {math}`2` to respect the fact that the size of the sample space has shrunk---in this case, from six possibilities to three.

In biology, we use conditional probability to distinguish between different kinds of errors that crop up in experiments, including clinical tests for disease. We commit a {\it type-I 
error} when a test for the presence of some condition leads us to falsely conclude that condition is present when it truly is not. A type-I error is colloquially known as a *false positive*. A *type-II error*, or *false negative*, occurs when the test leads us to falsely conclude that the condition is not present when it truly is. %A test tends to avoid type-I errors is said to be *sensitive*, and one that tends to avoid type-II errors is said to be *specific*.

:::{prf:example}
:label: eg:covid
Let {math}`E` be the event that an individual is infected with COVID-19, and let {math}`F` be the event that the same individual tests positive for COVID-19 when subjected to a nasal swab. The *specificity* of nasal-swab test refers to the rate at which it correctly detects those who are not infected by COVID-19, or equivalently the likelihood with which it correctly identifies someone not infected by COVID. Express the specificity in terms of the probability of committing a type-I error.   
::: 

:::{solution .dropdown} eg:covid
We can symbolize the event associated with correctly identifying an individual not infected by COVID, as {math}`F^c  \mid  E^c`.
A type-I error will have occurred when an individual who does not have COVID-19 tests positive for the disease, and we can symbolize this event as {math}`F  \mid  E^c`. Together, the events {math}`F^c \mid  E^c` and {math}`F  \mid  E^c` are mutually exclusive and exhaustive, with respect to the space of outcomes where the individual tested does not have COVID-19. It follows that
```{math}
  \mathbb{P}(F^c  \mid  E^c) + \mathbb{P}(F  \mid  E^c) = 1
```  
and so the specificity of the test can be expressed as
```{math}
  \mathbb{P}(F^c  \mid  E^c) = 1 - \mathbb{P}(F  \mid  E^c)
```
which is {math}`1` minus the probability of committing a type-I error. Colloquially, this is {math}`1` minus the false positive rate.
:::

If someone wanted to estimate the specificity of a nasal-swab test, we could imagine suggesting that they subject a large number of known healthy people to the test. The suggestion is based on the suspicion that the specificity would be captured by the fraction of the subjects that correctly tested negative. That is to say, we would estimate {math}`\mathbb{P}(F^c  \mid  E^c)` using
```{math}
  \frac{\text{\# negative tests}}{\text{\# healthy subjects tested}}.
```
Our suspicion here is supported by the *weak law of large numbers*. That law tells us that, under a reasonably broad range of conditions, the probability of any event {math}`E` is very likely to be correctly estimated by repeating an experiment many times, counting the number of times that {math}`E` occurs, and asserting that
```{math}
  \mathbb{P}(E) \approx \frac{\text{\# of occurrences of} \ E}{\text{\# repetitions}}.
``` 
We explore the application of the weak law of large numbers in the next example.

:::{prf:example}
:label: eg:triple
A maternal serum triple screen measures the content of alpha-fetoprotein, human chorionic gonadotropin, and estriol the blood of a pregnant woman. The triple screen assesses the risk of birth anomalies and is an alternative to amniocentesis. 

Six thousand pregnant women submitted to a triple screen. Based on the screen, {math}`1 124` of the pregnancies were identified as being at high risk for congenital anomalies. Following delivery, anomalies were found in only {math}`379` of those high-risk pregnancies identified by the screen, whereas the screen missed anomalies in {math}`82` pregnancies. Based on this information, estimate the specificity of the triple screen.     
::: 

:::{solution .dropdown} eg:triple
Let {math}`A` be the event that a birth anomaly occurred, and let {math}`S` be the event that the maternal serum screen finds evidence consistent with an anomaly. A type-I error, then, can be described as the event {math}`\{ S \mid  A^c\}`. 

Based on the information given, we know that there were {math}`379+82 = 461` anomalous births. The remainder of the births in the study, {math}`6 000 - 431 = 5 539`, were not anomalous. We also know that of the {math}`1 124` pregnancies flagged by the screen, {math}`1 124 - 379 = 745` were incorrectly classified.  		
Using the weak law of large numbers the type-I error rate is estimated as
```{math}
  \mathbb{P} ( S \mid  A^c ) = \frac{745}{5 539}
```
and so the specificity is
```{math}
  1 - \frac{745}{5 539} = 0.8655.
```

We could have also calculated the specificity by observing that the of the {math}`5 539` non-anomalous pregnancies, {math}`5 539 - 745` were correctly left unflagged by the screen. Then
```{math}
  \mathbb{P}(S^c  \mid  A^c )
  =
  \frac{4 794}{5 539} 
  =
  0.8655
```
is again the result.
:::

Conditional probability also offers us a particularly handy way of expressing the probability of an event {math}`F` based on a mutually exclusive and exhaustive set of events {math}`E_1, \ldots, E_n`. Since the mutually exclusive and exhaustive set fills the entire space of possible outcomes {math}`\Omega` without overlap, the event {math}`F` can be decomposed as
```{math}
  F 
  =
  (F \cap E_1) \cup (F \cap E_2) \cup \cdots \cup (F \cap E_n)
```
as shown in Figure [](#fig:total_prob). It follows that
```{math}
  \begin{array}{lcl}
    \mathbb{P} (F) 
        &=&
        \mathbb{P} \bigg( 
        (F \cap E_1) \cup (F \cap E_2) \cup \cdots \cup (F \cap E_n)\bigg) \\[2ex]
        &=&
        \mathbb{P}(F \cap E_1) 
        +
        \mathbb{P}(F \cap E_2)
        + \cdots +
        \mathbb{P}(F \cap E_n)  
        \\[2ex]
        &=&
        \mathbb{P}(F \mid  E_1) \mathbb{P}(E_1)  
        +
        \cdots +
        \mathbb{P}(F \mid  E_n) \mathbb{P}(E_n)
  \end{array}
```
The preceding equations can be re-stated more succinctly as one formula
```{math}
  \mathbb{P} ( F ) = \sum_{i=1}^n \mathbb{P} (F \mid  E_i) \mathbb{P} ( E_i ),
```
which is called the *law of total probability*. It cannot be forgotten that the set of events {math}`E_1, \ldots, E_n` featured in this law is mutually exclusive and exhaustive.

:::{figure} ../standalones/image-total-probability.png
:label: fig:total_prob

The law of total probability
:::

We have already applied the law of total probability in a previous chapter, though we did not know it at the time. The next example provides some of the probability detail that we glossed over in earlier discussions.

:::{prf:example}
:label: eg:hapdip
In certain species of insects, sex is determined by an individual's ploidy. Females develop from the fertilized eggs produced by their mother, and so are diploid. By contrast, males develop from unfertilized eggs, and so are haploid. Let {math}`M_t` be the event that an allele currently found in a population of haplodiploids originated from one found in a male exactly {math}`t` generations ago. Express the probability of the event {math}`M_t` in terms of {math}`M_{t-1}` and {math}`F_{t-1} = M^c_{t-1}`.
::: 

:::{solution .dropdown} eg:hapdip
Clearly {math}`M_{t-1}` and {math}`M^c_{t-1}` are mutually exclusive and exhaustive. The allele in question must have originated from either a male or a female {math}`t-1` generations ago; those are the only two options. Using the law of total probability, then, we can assert that
```{math}
  \mathbb{P} (M_t)
  =
  \mathbb{P}( M_t  \mid  M_{t-1} ) \mathbb{P} (M_{t-1})
  +
  \mathbb{P}( M_t  \mid  M_{t-1}^c ) \mathbb{P} (M_{t-1}^c).
```
Since an allele cannot pass from a male to another male in one generation, we have {math}`M_t \cap M_{t-1} = \emptyset`. It follows that {math}`\mathbb{P}( M_t  \mid  M_{t-1} ) = 0` which leaves us with
```{math}
  \mathbb{P} (M_t)
  =
  \mathbb{P}( M_t  \mid  M_{t-1}^c ) \mathbb{P} (M_{t-1}^c)
```
Though it is not required for this example, it is interesting to note that a female {math}`t-1` generations ago would have inherited one allele from its mother and one from its father. Assuming meiosis is fair, the female {math}`t-1` generations ago would be equally likely to transmit each allele, and so {math}`\mathbb{P}( M_t  \mid  M_{t-1}^c ) = \frac{1}{2}`. Using the fact that {math}`\mathbb{P} (M_{t-1}^c) = 1-\mathbb{P} (M_{t-1})` we can say
```{math}
  \mathbb{P} (M_t)
  =
  \frac{1}{2} \big(1-\mathbb{P} (M_{t-1})\big).
```
which is exactly the recursion we uncovered in Chapter 1.
:::

The dedicated reader will note that Example [](#eg:hapdip) differs slightly from its counterpart in Chapter 1. In particular, Example [](#eg:hapdip) dropped the requirement that the present-day allele be found in a male. Even with this difference, though, we still arrived at the same recursive probability statement found in Chapter 1. In some sense, knowing the sex of the individual who currently carries the allele gives us no additional information about the likelihood of the different patterns of inheritance. We can formalize idea like this using the notion of independence.

Two events, {math}`E` and {math}`F`, are *independent* if {math}`\mathbb{P} (E \cap F) = \mathbb{P}(E)  \mathbb{P}(F)`. It follows that if {math}`E` and {math}`F` are independent events, then
```{math}
  \mathbb{P}(F \mid E) = \frac{\mathbb{P}(E)  \mathbb{P}(F)}{\mathbb{P}(E)} = \mathbb{P}(F).
```
Clearly, knowing that event {math}`E` has occurred changes nothing about the likelihood with which {math}`F` occurs. Going back to the previous example, it turns out that we cannot say {math}`M_t` and {math}`M_0` are independent events.\footnote{Recall that, in Chapter 1, we had an initial condition that affects the solution to the recursion.} However, the match between recursions in Example [](#eg:hapdip) and the one in Chapter 1 does allow us to say that {math}`M_\infty` and {math}`M_0` are independent.  

It is perhaps more instructive to note that, by definition, any event that is either impossible or guaranteed must be independent of every other event. To see how this works, let {math}`E` be the event that I embarrass my children at some time within the next year, and let {math}`H` be the event that the result of a coin tossed today is ``heads.'' Obviously, {math}`\mathbb{P}( H \cap E ) = \mathbb{P} (H)`,
since {math}`E` is guaranteed to occur. It follows that,
```{math}
  \mathbb{P}( H \cap E ) = \mathbb{P} (H) \times 1 = \mathbb{P}(H)  \mathbb{P}(E)
```
and so we can conclude that {math}`H` and {math}`E` are independent. Working in a similar way we get
```{math}
  \mathbb{P}( H \cap E^c ) = \mathbb{P} ( \emptyset ) = 0 = \mathbb{P}(H) \times 0 = \mathbb{P}(H)  \mathbb{P}(E^c)
```
and again we can conclude the events are independent. 

Working with independent events is particularly convenient from a mathematical perspective. The next example illustrates this point with another problem from genetics.

:::{prf:example}
:label: eg:offsprings

Two heterozygous parents, {math}`Aa`, produce an offspring. What is the probability that their offspring is also heterzygous? 
::: 

:::{solution .dropdown} eg:offsprings
There are different ways to approach this problem, and here, we will opt for an indirect solution in which we first calculate the probability that the offspring produced is homozygous (i.e. not heterozygous).

There are two mutually exclusive ways an offspring in this problem could be homozygous. It could inherit an {math}`A` allele from both its mother and its father, or it could inherit an {math}`a` allele from both its mother and its father. Because the allele contributed by one parent is independent of that contributed by the other, the probability of the former event is
```{math}
\begin{aligned}
\mathbb{P} ( AA \text{ offspring } ) 
&= \mathbb{P}( \{ A \text{ from mom}\} \cap \{ A \text{ from dad}\} ) \\
&= \mathbb{P}( A\text{ from mom } )  \mathbb{P}( A\ \text{from dad} ) \\
&= \left( \frac{1}{2} \right)^2 = \frac{1}{4}.
\end{aligned}
```
where we have also used the fact that a parent is equally likely to contribute either of its two alleles to its offspring.  

The probability of the latter event is calculated in the same way:
```{math}
  \mathbb{P} ( aa \text{ offspring} ) = \mathbb{P}( \{ a \text{ from mom}\} \cap \{ a \text{ from dad}\} ) = \frac{1}{4}.
```

Using the fact that the event corresponding to the production a heterozygous offspring is the complement of that corresponding to producing a homozygous offspring we get
```{math}
\begin{aligned}
  \mathbb{P} ( \text{heterozygous offspring} )
  &= 1 - \mathbb{P} ( \text{heterozygous offspring} ) \\
  &= 1 - \mathbb{P} ( \{ AA\ \text{offspring} \} \cup \{ aa\ \text{offspring} \} ) \\
  &= 1 - \left( \frac{1}{4} + \frac{1}{4} \right) \\
  &= \frac{1}{2}.
\end{aligned}
```
An alternative means of arriving at the same answer involves the use of a *Punnett square* and is often presented in introductory genetics courses.
:::

Now that we have the basics of probability established we can move on. In the next chapter we will turn our focus to issues that arise when dealing with data collected in the field or in the lab. 

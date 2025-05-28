# Random Variables and Their Applications

Biologists typically work with numbers, not chance events. They have some idea about how a particular living system works in theory, and they gather quantitative data about that system in order to either support or refute the hypotheses they have established. While on duty, biologists rarely flip coins and roll dice.

That said, the numbers that make up a biologist's data set can still be influenced by chance, and the story the numbers will ultimately tell is not at all certain. One cannot say, therefore, that the ideas from probability theory have no relevance to the biologist's day-to-day activities. In order to make probability theory relevant to lab- or field-based studies we need to establish a bridge from the world of "outcomes" and "events" to one in which numbers take centre stage. As we will see, random variables allow us to create this bridge.

In this chapter we learn about what a random variable actually is, we find out how random variables can be modelled with a computer, and we find out how to use random variables to arrive at data-driven conclusions in the face of uncertainty.

## What is a Random Variable?

In many cases we are not as interested in the outcomes of a particular experiment as we are in functions of those outcomes. A function {math}`X` that maps the sample space {math}`\Omega` to the real numbers is called *a random variable*. For the experiment in which we flip a fair coin, we have {math}`\Omega = \{ \text{heads}, \text{tails}\}` and we can define a random variable {math}`X` on this set as follows:
```{math}
	X(\omega)
	=
	\begin{cases}
		0 & \text{if}\ \omega = \text{``heads,''}\\
		1 & \text{if}\ \omega = \text{``tails.}
	\end{cases}
``` 
 
In order for {math}`X` to officially qualify as a random variable it must be true that, for any interval of the real line, the set of outcomes that end up in this interval after being run through {math}`X` corresponds to an event. This point might seem unduly technical, but it allows us to apply ideas presented earlier in the chapter to our discussions about random variables going forward. Staying with the coin-flipping example, consider the set {math}`\{ \omega \in \Omega : X(\omega) \in (-\frac{1}{2}, \pi) \}`. In words, this is the set of outcomes in the sample space that end up somewhere in the open interval {math}`(-\frac{1}{2}, \pi)` after being run through the function {math}`X`. This set can also be understood as the event we have flipped either ``heads'' or ``tails.'' Consequently, we can assign a probability to the set in question, and in this case the result of doing so is
```{math}
	\mathbb{P} \left( \{ \omega \in \Omega : X(\omega) \in (-\frac{1}{2}, \pi) \} \right) = 1.
```
In practice, we will abbreviate the set {math}`\{ \omega \in \Omega : X(\omega) \in (a, b) \}` as {math}`\{ X(\omega) \in (a, b) \}` or sometimes even as {math}`a < X < b`.

The fact that intervals of the real line can be translated into events puts us on solid ground when it comes to defining the *cumulative distribution function* of a random variable. The cumulative distribution function of {math}`X` is defined as 
```{math}
	F(x) = \mathbb{P} \{ -\infty < X \leq x \}.
```
It can be shown that {math}`F` is non-decreasing and right-continuous, with {math}`\displaystyle\lim_{x\to\infty} F(x) = 1` and {math}`\displaystyle\lim_{x\to-\infty} F(x) = 0`.

:::{prf:example}
:label: eg:cdf1

Determine the cumulative distribution function of the random variable {math}`X` we defined above and plot it.
::: 

:::{solution .dropdown} eg:cdf1
For every value of {math}`x` that is strictly less than {math}`0`, the event {math}`\{ X \in (-\infty, x]\}` has probability zero: no outcome maps to the interval {math}`(-\infty, x]` so the event {math}`\{ X \in (-\infty, x]\}` is the empty set. We conclude that {math}`F(x)  = 0` for all values of {math}`x < 0`.
	
One of the two equally-likely outcomes of the experiment maps to {math}`(-\infty, x]` under {math}`X` when {math}`x` is greater than or equal to {math}`0` and strictly less than one.  We conclude that {math}`F(x) = \frac{1}{2}` when {math}`0 \leq x < 1`.
	
All outcomes map to {math}`(-\infty, x]` under {math}`X` when {math}`x` is greater than or equal to {math}`1`. Thus, {math}`F(x) = 1` when {math}`x \geq 1`.
	
Combining our observations gives us
```{math}
    F(x) 
    = 
    \begin{cases}
    0 & x<0 \\
    \frac{1}{2} & 0 \leq x < 1 \\
    1 & x \geq 1
    \end{cases} 
```
as the cumulative distribution function for the random variable {math}`X`. The plot of {math}`X` below highlights the features of {math}`F` we have already identified.

![](../standalones/build/plot-cdf.pdf)
:::

## Discrete and Continuous Random Variables

A *discrete random variable* is one whose the range consists only of a discrete set of numbers. The random variable {math}`X` that we introduced for the coin-flipping experiment above is discrete because its range is the discrete set {math}`\{ 0, 1\}`.  In general, a discrete random variables may have a range that is infinite---perhaps something like, {math}`\{ 2, 4, 6, 8, \ldots \}`. In this course, though, we will (try our best to) restrict attention to those discrete random variables whose ranges are finite.

For a discrete random variable {math}`X` with range {math}`\{ x_1, x_2, x_3, \ldots \}`, we can define the event {math}`E_j` as {math}`\{ \omega\in \Omega : X(\omega) = x_j\}`, or simply {math}`X=x_j` for short. From here we can define the *probability mass function* for {math}`X` as 
```{math}
  p(x)
  =
  \begin{cases}
    \mathbb{P}( X = x_j ) & \text{if}\ x = x_j \\
    0 & \text{otherwise.}
  \end{cases}
```
The graph of the probability mass function associated with the discrete {math}`X` introduced in our coin toss example is presented in Figure [](#fig:pmf).
Note that the cumulative distribution function for discrete random variable {math}`X` can be expressed as {math}`F(x) = \displaystyle\sum_{j=1}^n p(x_j)` when {math}`x_n \leq x < x_{n+1}`, where we have assumed that the elements of {math}`\{ x_1, x_2, x_3, \ldots\}` have been arranged in increasing order.

```{figure} ../standalones/build/plot-pmf.pdf
The probability mass function associated with the discrete random variable {math}`X` defined for the coin-tossing example presented earlier in the section.
```

A *continuous random variable* is one for which there exists a non-negative function {math}`f(x)`, called the *probability density function* of {math}`X`, such that
```{math}
\mathbb{P} (  X \in I ) = \int_I f(x) dx
```
where {math}`I` is any interval, and 
```{math}
\int_{-\infty}^{\infty} f(x) dx = 1.
```

The infinite limits of integration in the previous line are likely unfamiliar to you. If so, there is no need for worry. The key point is that the total area under the graph of {math}`f (x)` is equal to {math}`1`. Perhaps surprisingly, that can happen even when the tails of the graph of a function extend to infinity, provided those tails tend to zero quickly enough. An example of a probability density function is presented in Figure [](#fig:pdf).

:::{figure} ../standalones/build/plot-pdf.pdf
:label: fig:pdf
:::

An example of a probability density function for a continuous random variable {math}`X`. The function is non-negative, and the area under the curve is exactly {math}`1`. Importantly the height of function does not give the probability that {math}`X=x`. This is particularly evident for {math}`x=0` where the height of the graph is {math}`2`. 


Importantly, the probability that a continuous random variable {math}`X` takes on a specific value, say {math}`X=a`, is itself zero. This follows from the fact that {math}`\mathbb{P}( X=a )=\int_a^a f(x) dx = 0`, and it underscores the point that we should not be tempted to interpret {math}`f(x)` as the probability of the event, {math}`X=x`.

We can also see that the cumulative distribution function for a continuous random variable can be expressed as {math}`F(a) = \int_{-\infty}^a f(x) dx`. Assuming that {math}`f(x)` is continuous on {math}`(-\infty, b]`, where {math}`b>a`, and applying the Fundamental Theorem of Calculus tells us that {math}`F'(a) = f(a)`. In other words, for a continuous random variable with continuous density function, said probability density function is the derivative of the cumulative distribution function. We can, therefore, interpret {math}`f(x)` as the rate at which probability accumulates at {math}`x`.  

## Pseudorandom Variables and Simulation

We can generate a sequence of independent\footnote{A pair of random variables {math}`X` and {math}`Y` is independent if {math}`\mathbb{P} ( \{ X \leq x\} \cap\{  Y \leq y\} )` is equal to {math}`\mathbb{P}(X \leq x) \mathbb{P}(Y\leq y)` for all possible {math}`x` and {math}`y`} random variables using recursions similar to those encountered in Chapter 1. We start by selecting positive integer {math}`a` and non-negative integers {math}`b` and {math}`c`. We then use these numbers to construct the recursive model
```{math}
	u_t = a u_{t-1} + b, \quad u_0 = c.
```
Before we can start generating, though, we must ``wrap'' the sequence that results from iterating the recursion using modular arithmetic. In modular arithmetic we identify a particular integer {math}`m>1` as the *modulus* and we make equivalent any two positive integers whose remainders are the same when divided by {math}`m`. For example, we would say {math}`4` and {math}`7` are *equivalent mod {math}`3`*, because {math}`3` goes into {math}`4` once with remainder 1, and {math}`3` goes into {math}`7` twice also with remainder {math}`1`. To remind ourselves of the fact that modular arithmetic is at work we write
```{math}
	u_t = ( a u_{t-1} + b) \mod m, \quad u_0 = c.
```
We call expressions like those in the previous line *random number generators* because they tend to scatter the various values of {math}`u_t` over the interval {math}`[0,m]` in a seemingly random way. Since there is a deterministic rule that underlies what we are doing here, we cannot say that the output from the generator is truly random; consequently, we refer to the output as *pseudorandom* instead.

As a simple example of how this generator works, pick {math}`a=3`, {math}`b=1`, {math}`c=1`, and set the modulus {math}`m=8`. Using a spreadsheet, we see that the sequence of numbers generated by our choice is {math}`1, 4, 5, 0, 1, 4, 5, 0, \ldots` (Figure [](#fig:excel)). This fails to live up to hype I tried to create above, as the sequence is clearly patterned. The lesson, here, is that we can make poor choices for {math}`a, b, c` and {math}`m`. Better choices include large values of {math}`m` that are either powers of {math}`2` or are prime numbers. If we re-run the generator using {math}`m=2^6 = 128` rather than {math}`8`, for instance, we see why one might mistake the output as random. The famous\footnote{Only famous in certain circles.} *Numerical Recipes* series of books recommends
```{math}
	a = 1 664 525, \quad b = 1 013 904 223 \quad m = 2^{32}.
```
Even though this choice is not perfect, for our purposes it will be sufficient. 

:::{danger} TODO
Geoff had some excel spreadsheets here.
:::


Once we have a way to generate a sequence of independent pseudorandom numbers, we can transform them into numbers on the unit interval by dividing by {math}`m`. We then have reasonable model of a sequence of independent observations from a continuous *uniform distribution* on {math}`(0,1)` (Figure [](#fig:histogram)). In other words, {math}`U_t = u_t/m` behaves like a random variable with cumulative density function 
```{math}
	F(x) = 
	\begin{cases}
	0 & x< 0\\
	x & 0\leq x\leq 1\\
	1 & x > 1
	\end{cases}
```
and probability density function   
```{math}
	f(x)
	= 
	\begin{cases}
	1 & 0 \leq x \leq 1\\
	0 &\text{otherwise.}
	\end{cases}
```
From here we can do something really interesting from a calculus perspective, as the next example is meant to show.

:::{figure} ./standalones/histogram_rng.pdf
:label: fig:histogram

A histogram summary of {math}`10 000` numbers output by the random number generator with {math}`a=1 664 525`, {math}`b=1 013 904 223`, {math}`m=2^{32}` and {math}`c=0`. Random number were normalized by dividing by {math}`m`. Vertical axis shows normalized counts for each subinterval of {math}`(0,1)` considered (solid line), and so reflects the density of observations therein. For comparison, the probability density function of a uniform random variable on {math}`(0,1)` is superimposed on the histogram (dashed purple line). The pseudorandom numbers, divided by {math}`m`, fill the unit interval in the same way uniform random variables would. 
:::


:::{prf:example} 
:label: eg:monte-carlo
Approximate {math}`\int_{-1}^{1} e^{-x^2} dx`.
:::  

:::{solution .dropdown} eg:monte-carlo
The given integral does not have a formula in terms of elementary functions. However, we can use a probabilistic method to approximate the given definite integral.

We generate pseudorandom to solve the problem. The basic strategy is best explained using the figure below:

```{figure} ../standalones/build/plot-monte-carlo.pdf
:label: fig:monte-carlo
```


We generate a long sequence of random numbers, uniformly distributed on the unit interval as described above. We then pair successive numbers in the sequence, say {math}`U_t` and {math}`U_{t+1}` to create random coordinates {math}`X = 2U_t - 1` and {math}`Y=U_{t+1}`. The pair {math}`(X,Y)` falls somewhere inside the dotted rectangle shown in the figure. We can mark the pair if it also falls below the graph of {math}`e^{-x^2}`. If we take the fraction of marked pairs and multiply it by the area of the rectangle we will get an estimate of the area under the curve, since pairs will be spread evenly over the rectangle itself.
		
We can carry out our calculation using a spreadsheet. 	

The additions to the spreadsheet below show that we next take every other {math}`U` value and map it to {math}`[-1,1]` to create {math}`X`. The values of {math}`X` alternate with values of {math}`Y` that are simply set equal to their corresponding {math}`U` value. We then pair up {math}`X` and {math}`Y` values as suggested by the shading.

A given pair of {math}`X` and {math}`Y` values lies below the graph of {math}`e^{-x^2}` if and only if {math}`e^{-X^2}>Y`. When {math}`e^{-X^2}>Y` we record a success in a separate column as a {math}`1`; otherwise we record a value of {math}`0`. 

Summing the column containing only {math}`1`s and {math}`0`s tells us the total number of successes. By dividing the total number of success by the total number of pairs we determine the fraction of pairs that fell below the curve. Multiplying this fraction by the total area of the rectangle (which happens to be {math}`2`) gives us an estimate of the definite integral. 

Careful copy-and-pasting allows us to generate 50 pairs by continuing the pattern to line 102 of the spreadsheet. Summing the final column and dividing by 50 gives {math}`0.7` and so the estimate of the definite integral is {math}`1.4` which is close to its true value of about {math}`1.493648266`. Increasing the number of random pairs generated results in an even better match.
:::

## Expectation and Variance

When faced with the uncertainty associated with a particular random variable, it is natural to try to anticipate what its value will be, say, on average. We can scratch that itch, mathematically, using the notion of expectation. 

For a discrete random variable, we define the *expectation of {math}`X`* as
```{math}
	E(X) = \sum_j x_j  p(x_j) 
```
provided the sum exists\footnote{If the range of {math}`X` is infinite then the sum is a series which may diverge.}. You might recognize the expectation of {math}`X` as a kind of weighted average; and if so, good eye! The expectation is indeed a weighted average, with the weights coming from the appropriate corresponding probability.

For a continuous random variable, the expectation of {math}`X` is defined as
```{math}
	E(X) =
	\int\limits_{-\infty}^\infty x f(x) dx
``` 
again provided the integral exists. In this course, you will only compute expectations using density functions defined over bounded regions of the real line, like the interval {math}`[a,b]`. In those cases, {math}`E(X) = \int_a^b x f(x) dx`.

We can also determine the expectation of any function {math}`g` of a discrete or continuous the random variable. In the discrete case we have
```{math}
	E(g(X)) = \sum_j g(x_j) p(x_j)
```
provided the sum exists, whereas in the continuous case we have
```{math}
	E(g(X)) = \int\limits_{-\infty}^\infty g(x) f(x) dx
```
again, provided the integral exists. 

One function that receives a lot of attention in probability theory is {math}`g(X) = (X - E(X))^2`. The attention is not misplaced, because
```{math}
	E(g(X)) = E( (X-E(X))^2  )
```
tells us how variable {math}`X` is, on average. In fact, we call {math}`E( (X-E(X))^2  )` the *variance of {math}`X`*, and we write it as {math}`\text{Var}(X)` for short.  

:::{prf:example}
:label: eg:uniform
If {math}`X` is a continuous random variable with a uniform distribution on the  interval {math}`[0,1]`, find {math}`E(X)` and {math}`\text{Var}(X)`.
:::

:::{solution .dropdown} eg:uniform
We have see that the probability density function for this kind of random variable is
```{math}
    f(x)
    =
    \begin{cases}
        1 &, \text{if } 0 \le  x \le 1\\
        0 &, \text{otherwise}.
    \end{cases}
``` 
Applying the definition of expectation we arrive at
```{math}
E(X) = \int_{-\infty}^\infty x f(x) dx = \int_0^1 x dx = \frac{1}{2}.
```

It should be emphasized that, when the domain of {math}`f(x)` is bounded, the expectation is not always found at its midpoint. 

Applying the definition of variance we get
```{math}
\begin{aligned}
  \text{Var}(X)
  &= E( (X-E(X))^2 ) \\
  &= \int_{-\infty}^{\infty} \left( x - \frac{1}{2} \right)^2 f(x) dx \\
  &= \int_{0}^{1} \left( x - \frac{1}{2} \right)^2 dx = \frac{1}{12}.
\end{aligned}
```
:::

## Working with Data

Biologists collect data to cope with the uncertainty they have about the variable quantities they encounter in the field or in the laboratory. We could imagine, for instance, an ecologist or physiologist collecting data {math}`\mathcal{X}_1, \ldots, \mathcal{X}_n` to gain some insights into a quantity that is, itself, modelled as a random variable, {math}`X`. 

Once collected, data can be summarized in a variety of ways. One common summary statistic is the *sample mean*
```{math}
\bar{\mathcal{X}} = \frac{1}{n} \sum_{j=1}^{n} \mathcal{X}_{j}
```    
which is used as an estimate of the expectation of {math}`X`. Another, common summary statistic is the *sample variance*
```{math}
s^2 = \frac{1}{n-1} \sum_{j=1}^n \left( \mathcal{X}_j - \bar{\mathcal{X}} \right)^2
``` 
which estimates the variance of {math}`X`. The next example takes us through the calculation of the sample mean and sample variance.

:::{prf:example}
:label: eg:sample-stats
Concerns have been raised that an experimental drug will result in either weight loss or weight gain. To test the idea, the drug was administered to twelve rats. The weight gain experienced by each rat, {math}`\mathcal{X}_j`, was recorded in the table below. 

Use the data to calculate the sample mean and the sample variance (from \cite{zar}).

| {math}`j` | {math}`\mathcal{X}_{j}` |
|-----------|-------------------------|
| 1         | {math}` 1.7`                |
| 2         | {math}` 0.7`                |
| 3         | {math}`-0.4`                |
| 4         | {math}`-1.8`                |
| 5         | {math}` 0.2`                |
| 6         | {math}` 0.9`                |
| 7         | {math}`-1.2`                |
| 8         | {math}`-0.9`                |
| 9         | {math}`-1.8`                |
| 10        | {math}`-1.4`                |
| 11        | {math}`-1.8`                |
| 12        | {math}`-2.0`                |

**No one** in 2025 handles data by a table. Data is typically store in a database and retrieved by code. The following python code store the above table of data in a variable called `x`.

```{code} python
x = [ 1.7, 0.7, -0.4, -1.8, 0.2, 0.9, -1.2, -0.9, -1.8, -1.4, -1.8, -2.0 ]
```

:::

:::{solution .dropdown} eg:sample-stats
Summing the data gives us {math}`\displaystyle\sum_{j=1}^{12} \mathcal{X}_j = -7.8`. Dividing the sum by {math}`n=12` gives us {math}`\bar{\mathcal{X}}=\dfrac{-0.78}{12} =-0.65` grams.
	
The sample statistics are calculated using their formulas.

```{code} python
x_mean = sum(x) / len(x)
x_variance = sum( (x_i - x_mean)**2 for x_i in x ) / (len(x) - 1)
```

If we were to perform the calculations by hand, we would get
```{math}
\bar{X} = 17.25\text{ grams} \quad\text{and}\quad s^{2} = \frac{17.25}{11} \text{ grams}^{2}.
```
Notice that the unit for variance has a square.
:::

It is difficult to justify conclusions about quantities like {math}`X` based on summary statistics alone. We might, for instance, be tempted to conclude that the sample mean calculated in the previous example implies that concerns about the experimental drug are founded. Specifically, we might conclude that weight loss is a side effect of the drug since {math}`\bar{\mathcal{X}} =-0.65` is negative. Such a conclusion, however, ignores the possibility that the sample mean of {math}`-0.65` arose by chance and that the drug actually has no effect on weight. To put it another way, jumping to such a conclusion based on summary statistics alone disregards the possibility that we have made a type-I error. In the next example we use simulation to model the probability that, by concluding a drug-induced change in weight occurs, we would have committed a type-I error.

:::{prf:example} 
:label: eg:ttest
If we use the data in the previous example to conclude that an experimental drug changes a rat's weight, then what is the probability that we have made a type-I error?
:::

:::{solution .dropdown} eg:ttest
We treat the data set resulting from the experiment as one element of an infinite sample space {math}`\Omega`. The other elements of {math}`\Omega` represent the alternative data sets we might have observed had we repeated the experiment itself. Assuming that all data sets in {math}`\Omega` are equally likely to have been observed, we can estimate the probability of a type-I error by simulating a large number of replicate experiments, then counting the number of false positives that occur. While the suggestion seems simple enough, some care is required when creating the simulation model. 
	 	
We will simulate one replicate of the experiment by generating {math}`n=12` pseudorandom variables. In keeping with the idea that we are counting false positives, we must work under the assumption that the drug has no effect. This means that the pseudorandom variables we generate must model random ones that follow a distribution with expectation {math}`0` (zero change in weight). We know how to generate uniformly-distributed variables on the unit interval. By doubling each these uniform variables, subtracting {math}`1`, then multiplying by {math}`a>0` we end up spreading them evenly across the interval {math}`[-a,a]` and consequently we shift their expectation to {math}`0`. 
	 	
The next difficulty arises when it comes to choosing a value of {math}`a` for the simulation. The choice of {math}`a` will, of course, affect the variability that we observe in the simulated data sets. Therefore, {math}`a` must be chosen in a way that ensures  variation in each of the simulated data sets mirrors that found in the data collected. 
	 	
To choose {math}`a` correctly, we note that our pseudorandom numbers model random variables with probability density function
```{math}
    f(x)
    =
    \begin{cases}
        \dfrac{1}{2a} & -a \leq x \leq a\```{math}1ex]
        0 & \text{otherwise.}
    \end{cases}
```
so the variance that is relevant to our problem is calculated as
```{math}
    \int\limits_{-a}^a ( x - 0 )^2  \frac{1}{2a}  dx
    =
    \frac{1}{a} \int\limits_0^a x^2 dx = \frac{a^2}{3}. 
```
Since the sample standard deviation is meant to estimate the variance, we assert that
```{math}
    s^2 = \frac{a^2}{3}
    \leftrightarrow
    \sqrt{3 s^2} = a.
```
Using the results from the previous example we get {math}`a=2.169`. We can now create a replicate experiment by generating {math}`n=12` pseudorandom variables uniformly distributed on the interval {math}`[-2.169, 2.169]`.

The final difficulty lies in deciding what constitutes a ``false positive'' in the simulation. We have decided that a sample mean of {math}`-0.65` grams is sufficient to declare a weight change has occurred. However, this threshold was determined based on a data set with some degree of variability that will likely not be matched exactly in another replicate. To keep a level playing field, then, we standardize the mean weight change as
```{math}
    \frac{\bar{\mathcal{X}}}{\sqrt{s^2}} = \frac{-0.65}{\sqrt{1.5682}} = -0.519.
```
Importantly, the standardized measure, or *test statistic*, we have introduced has no units. Equally important is the fact that the benchmark value of {math}`-0.519` establishes the test we apply to each replicate when determining whether said replicate supports the conclusion that a weight change occurred. When the corresponding test statistic for a given replicate is calculated (by dividing the sample mean of a given replicate by the square root of its sample variance) and is determined to be further from zero than {math}`-0.519`, we declare a positive test result has occurred. Since this positive result is clearly false (the mean of the underlying distribution is, after all, zero) we include the replicate in our false-positive count. We eventually report the probability of having committed a type-I error as
```{math}
    \frac{\text{number of false positives}}{\text{number of simulated replicates}}.
```  

While carrying out the simulation using a spreadsheet is not impossible, it is tedious. It is much easier to create the simulation using a standard computer programming language. For those inclined to create such a simulation, the steps involved are as follows:

1. Generate {math}`n=12` pseudorandom variables on the interval {math}`(0,1)`; call them {math}`U_1, \dots, U_{12}`. 
2. Create a new data set {math}`V_1, \ldots, V_{12}`, where {math}`V_j = (2 U_j - 1) (2.169)`.
3. Calculate the test statistic using the formula
```{math}
    T = \frac{ \bar V } {\displaystyle \sqrt{ \sum_{j=1}^{12} \frac{(V_j - \bar V)^2}{12-1}}
    }
```
where {math}`\bar V = \dfrac{1}{12}\displaystyle\sum_{j=1}^{12} V_j`.
1. If {math}`|T| > |-0.519|` then count the replicate as a false positive; otherwise do nothing.
1. Repeat steps 1 to 4 a large number of times. Report the probability of committing a type-I error as the number of false positives divided by the number of times the steps 1 to 4 were carried out.
	 
When I simulated {math}`100 000` replicates on a computer, I found that the false positive rate, i.e. the probability of having committed a type-I error, was {math}`0.09977` or about {math}`10\%`. In practice, this rate is considered to be too high to allow us to reasonably conclude that a mean of {math}`-0.65` grams  represents anything other than a chance deviation from zero weight change, when viewed in the light of a sample variance of {math}`1.5682` grams squared.
:::

In the preceding example I suggested simulating data sets by generating pseudorandom variables uniformly distributed on {math}`[-a,a]` but I provided no justification. Why not use some other distribution? Why not the one corresponding to the density function shown in Figure [](#fig:pdf) for instance? The tl;dr answer is, it doesn't matter. It has long been known that the distribution of the test statistic we created does not depend on the underlying distribution of the data. This fact was discovered by an employee of the Guinness brewery, William Sealy Gosset. Guinness considered Gosset's work to be a trade secret, and so Gosset published his findings under the pseudonym, Student. In fact, the statistic we used in our example is similar to one known as *Student's t statistic* 
```{math}
	t = \frac{\bar{\mathcal{X}} - E[X]}{\sqrt{s^2/n}}.
```
Much is known about the distribution of the {math}`t`, including its cumulative distribution function. Using published tables we can determine that the probability of observing a {math}`T = t/\sqrt{12}` statistic that is farther from {math}`0` than {math}`-0.519` is 
```{math}
\begin{aligned}
\mathbb{P} ( \{ -\infty < T \leq -0.519 \} \cup \{ 0.519 < T < \infty \} )
\\
=
\mathbb{P} (  T \leq -0.519 )
+
\bigg( 1 - \mathbb{P} (  T \leq 0.519  )\bigg)
=
0.09964.
\end{aligned}
```
See [](#fig:two-tailed). This agrees with the simulation results reported in [](#eg:ttest).

:::{figure} ./standalones/plot-two-tailed.pdf
:label: fig:two-tailed

The density of Student's {math}`t` which can be related to the {math}`T` value introduced in Example [](#eg:ttest) by {math}`t = \sqrt{n} T` where {math}`n=12`. The area shaded in purple  is approximately {math}`0.09964` which gives the probability of committing a type-I error in [](#eg:ttest).
:::

Before closing, one final comment on dealing with data is needed. In [](#eg:ttest) we were concerned with weight changes, but we did not have a prior belief that the changes would be positive. Had we been concerned with drug-induced weight loss only, for instance, then we would have only been concerned with values of {math}`T` that were less that {math}`-0.519`. In terms of [](#fig:two-tailed), we would have been concerned only about the area of shaded tail on the left; we would not have cared about the right tail. Details like these, and more, will be emphasized more vigorously in your later courses in statistics.


# Introduction to models

## Models
````{prf:definition} mathematical models and dimensional homogeneity
:label: def:model

A **mathematical model** is an equation 
```{math}
  f( u_1, \ldots , u_n ) = 0
```
in which every symbol represent some real-world quantity. The SI units are the defaults unless explicitly specified.

Moreover, a valid model must satisfy **dimensional homogeneity**, that is, all top-level summands in the equation must have the same unit. 
````

It is convenient to think of {math}`u_{1}, \dots, u_{n}` as measurements of real-world quantities.  Note that the requirement of dimensional homogeneity is NOT placed on individual variables, but on top-level summands of the equation.

Making sure a model satisfies dimensional homogeneity is a basic sanity check because models like
```{math}
x \text{ apples} = y \text{ oranges}
```
is silly[^silly]. Furthermore, ensuring dimensional homogeneity provides hints (more on this in [Chapter 2](./ch2)) for creating models.

[^silly]: Technically speaking, the model is invalid.

Here are some examples of mathematical models.

:::{prf:example}
:label: eg:model-volume-cube

The equation {math}`y - x^{3} = 0` is just an equation but not a mathematical model.

However, if we let {math}`y` represent volume and {math}`x` the side length of a cube, then {math}`y - x^{3} = 0` turns into a mathematical model
```{math}
:label: eq:model-cube

(\text{volume in } \text{m}^{3}) = (\text{side length in m})^{3}.
```
Moreover, the equation works not just for one special cube but for all cubes.

Notice the units on both sides of the equation are the same.
::: 

Here is an example from physics.

:::{prf:example}
:label: eg:model-mass-density

If the density of an object is uniform throughout, then its mass and volume are related by

```{math}
(\text{mass in grams}) = (\text{density constant in } \text{g}/\text{m}^{3}) \times (\text{volume in }\text{m}^{3})
```

Notice, after cancellation, the units on both sides of the equation are the same.  If we decide to measure lengths in centimetres, then we must modify relevant terms of the equation.

If we all agree to use SI units, then we can shorten the equation to 
```{math}
(\text{mass}) = (\text{density constant}) \times (\text{volume}).
```
:::

:::{exercise} Concept Check

Which of the followings is (or are) a valid model?
1. {math}`(\text{mass in grams}) = (\text{density constant in } \text{g}/\text{cm}^{3}) \times (\text{volume in }\text{cm}^{3})`

2. {math}`(\text{mass in grams}) = (\text{density constant in } \text{g}/\text{m}^{3}) \times (\text{volume in }\text{cm}^{3})`

3. {math}`(\text{mass in mg}) = (\text{density constant in } \text{g}/\text{m}^{3}) \times (\text{volume in }\text{cm}^{3})`
::: 

Here is an example from chemistry.

:::{prf:example}
:label: eg:model-ideal-gas
You might remember the ideal gas model law from chemistry[^ideal-gas-model] or physics.  

Under certain conditions, the pressure, volume, substance and temperature of an ideal gas is related by
```{math}
(\text{pressure}) \times (\text{volume}) = (\text{substance}) \times (\text{gas constant}) \times (\text{temperature}).
```

The idea gas law is commonly presented in a succinct form by assigning each quantity a single-letter variable. If we assign the letter {math}`P` for pressure, {math}`V` for volume, {math}`n` for substance, {math}`T` for temperature and {math}`R` for the gas constant, then the equation in the ideal gas law becomes
```{math}
PV = nRT.
```
[^ideal-gas-model]:  The ideal gas law is typically taught in Chemistry 1302B at Western University.
::: 


The models from the examples above all carry assumptions which restrict their applicability. [](#eg:model-volume-cube) works for cubes but not spheres. [](#eg:model-mass-density) works for water (at a fixed temperature) but *not directly* for a mixture of oil and vinegar. [](#eg:model-ideal-gas) provides inaccurate prediction for a real gas under high pressure. While assumptions are important, we leave to physical science courses to discuss assumptions of specific models.

:::{attention} 
:label: attn:modelling-overview

In this course, we focus on the following aspects of (mathematical) modelling.

- Build and analyze models using power models {math}`y = c \cdot x^{\alpha}`.
- Build and analyze discrete-time models using recurrence equations.
- Build and analyze continuous-time models using (ordinary) differential equations.
- Build and analyze linear systems of discrete- and continuous-time models.

Moreover, we introduce scientific computing using Python to help you deal with real-world data.
:::

## Scientific computing with Python, Part 1

Scientific computing is an integral part of today's science.  [](#table:birds) contains measurements of birds of a from an observation.  However, real-world data is almost never presented in a table but stored in a database.  After data is retrieved in from a database, they are stored in code.  Scientists work with data using code. 

We are going to learn scientific computing the real-world way.  Look at some examples, play with them, and modify bits and pieces of an existing code to do what we need. If things break, undo and try again. 

### Variables and `print(...)`

If we write `x = 5` in Python, then `x` becomes a variable whose value is `5`. 
- If we want to change the value of `x` to `-3`, then we just write `x = -3`.  
- If we want to examine the value of `x`, then we write `print(x)`.

Variables in Python can be a lot of things, not just numbers.  For example, it can be some plain text, called a string in Python.  The code `s = "hello"` makes a variable whose value is the text "hello". 

If we want to print the value of `x` but want a more descriptive output, then we can use `print(f"...")`[^fstring]
 The code `print(f"x = {x}")` print `x = 5` (instead of just `5`) thanks to the f-string `f"x = {x}"`.  The code `print(f"There are {x} days in a work week.")` prints `There are 5 days in a work week.`

[^fstring]: The `f"..."` is called an [f-string](https://stackoverflow.com/questions/57150426/what-is-printf) (not an official resource, but helpful) for those interested in digging deeper in Python. 

:::{exercise} Concept Check
:label: ex:
What do you think `print(f"{s} world!")` outputs?
::: 

Variable names can be descriptive (as long as there are no spaces and certain special characters).  The following are totally valid names for variables.  

:::{code-cell} python
today = "Friday"
the_day_after_tomorrow = "Sunday"
iAmOutOfIdeasForNames = 42
:::


### Lists

Python indicates lists using square brackets.  Items in a list are separated by commas.  The code
```python
xs = [ 1, 2, 4, 8, 16, 32, 64 ]
```
contains a list of numbers.  The left-hand side of the equation is the name of the list, called `xs` in this example.  The right-hand side of the equation is the content of the list, powers of {math}`2` in this example.  The code `xs[0]` represent the value of the first item in the list called `xs`. 

Try it out.
```python
print(xs[0])

i = 5
print(xs[i])
```

The number `i` in `xs[i]` is called the index.  If you want the last item in the list, you can use an negative index `xs[-1]`.  
```python
print(xs[-1])
print(xs[-2])
print(xs[-4])
```

### Visualization


```python
lengths = [
  132, 61, 76, 58, 41, 58, 28, 25, 48, 30, 30, 40, 53, 8, 30.5, 17, 15.5, 11.5, 18, 22, 18, 12.5
]

mass = [
  2500, 1100, 1400, 1500, 350, 900, 115, 95, 450, 300, 100, 425, 1000, 3, 150, 42, 17, 12, 32, 9, 34, 64, 45, 13
]
```


## Power models

When an artist first learns their craft, they are taught to  break their subject down into its basic shapes. So, a sketch of a tree might initially look like a cylinder topped by a cone, and a sculpture of person might start out looking more like a collection of spheres and less like the [Venus de Milo](https://en.wikipedia.org/wiki/Venus_de_Milo).

```{figure} ./standalones/image-rubberduck.pdf
:label: fig:duck

It is mathematically convenient to treat all birds as if they are perfect cubes of constant density {math}`k` (grams per cubic cm). This implies that a bird's mass {math}`m` can be modelled as 
:::{math}
    (\text{density constant}) \times (\text{body length as a cube})^{3}.
:::
```

Thinking about shapes is also a good first step in **building mathematical modelling skills** --- especially those skills related to modelling the growth and form of organisms.

Consider, for example, the challenge of modelling the relationship between body length and weight in, say, birds. We can construct an abstract model for this relationship by picturing a bird as a perfect cube. Granted, few artists would likely be satisfied with this abstraction, but a modeller is worried about a different kind of aesthetic. To a modeller, the simplicity of a cube-based model makes it beautiful. Assuming the density across all birds are the same, then we can *partly capture* the complexity between mass and body length using a relation
```{math}
:label: eq:model-mass-length

(\text{mass in grams}) = (\text{density constant}) \times (\text{body length in cm})^{3}.
```

## Visually fitting the data to a model

[](#table:birds) presents average length and weight measurements associated with twenty-four species of birds common to Eastern North America. If our model is useful, we would expect a plot of weight versus length to look like the graph of {math}`k\, \ell^3`. A plot of the data in [](tab:birds) suggests we are on the right track, in that the data in [](tab:birds) tend to follow the graph of {math}`k\ell^3` when {math}`k` is approximately {math}`0.006` (Figure [](fig:bird_cubic)). However, based on Figure [](fig:bird_cubic) alone, one could also argue that the data support a model in which {math}`w` is proportional to {math}`\ell^2`. So the utility of our model (or, at least, its utility compared to that of a model we just pulled out of thin air) is still questionable at this point. Fortunately, we can sort out our confusion by looking at the data in a different way. 

```{csv-table} Length and weight for twenty-four common bird species. Data were obtained from Stiles and Skutch, *A Guide to the Birds of Costa Rica* (Cornell University Press, 1989).
:label: table:birds
:delim: &
:header:  Species & Length (cm) & Weight (g)


Great Blue Heron (Ardea herodias) & 132 & 2500 
Mallard (Anas platyrhynchos) & 61 & 1100 
Turkey Vulture (Cathartes aura) & 76 & 1400 
Osprey (Pandion haliaetus) & 58 & 1500 
Cooper's Hawk (Accipiter cooperii) & 41 & 350 
Red-tailed Hawk (Buteo jamaicensis) & 58 & 900 
American Kestrel (Falco sparverius) & 28 & 115 
Killdeer (Charadrius vociferus) & 25 & 95 
Ring-billed Gull (Larus delawarensis) & 48 & 450 
Rock Dove (Columba livia) & 30 & 300 
Mourning Dove (Zenaida macroura) & 30 & 100 
Common Barn-owl (Tyto alba) & 40 & 425 
Great Horned Owl (Bubo virginianus) & 53 & 1000 
Ruby-throated Hummingbird (Archilochus colubris) & 8 & 3 
Belted Kingfisher (Ceryle alcyon) & 30.5 & 150 
Hairy Woodpecker (Picoides villosus) & 17 & 42 
Barn Swallow (Hirundo rustica) & 15.5 & 17 
House Wren (Troglodytes aedon) & 10 & 12 
Cedar Waxwing (Bombycilla cedrorum) & 16.5 & 32 
Yellow Warbler (Dendroica petechia) & 11.5 & 9 
Northern Oriole (Icterus galbula) & 18 & 34 
Red-winged Blackbird (Agelaius phoeniceus) & 22 & 64 
Rose-breasted Grosbeak (Pheucticus ludovicianus) & 18 & 45 
Chipping Sparrow (Spizella passerina) & 12.5 & 13 
```

```{figure} ./standalones/plot-Ch0_fig0.pdf
:label: fig:bird_cubic

A plot of the data presented in [](table:birds). Solid line show graph of {math}`k \ell^{2}` with {math}`k = 0.006`. The scatter of points appears to follow the graph of {math}`k \ell^{3}`, however a graph of {math}`m = k \ell^{2}` (dotted line) also appears to produce a reasonable match to the data.
```

You will likely notice that some of the data points in Figure [](fig:bird_cubic) form a tight cluster, whereas others are more scattered. What's more, the tight clustering occurs among points closer to the origin, while the more diffuse scattering tends to occur among points farther from the origin. This pattern makes it difficult to discern how well the model {math}`m = k \ell^{3}` fits the data. It also suggests to us that a log-log transformation of the data can help tidy things up and make our evaluation of model performance more straightforward [](fig:log).

```{figure} ./standalones/plot-loglog.pdf
:label: fig:log

The function {math}`y = \ln(x)` has a spreading effect on small {math}`x` values and a clumping effect on large {math}`x` values. Small values in the domain that are close to one another map to values in the range that are farther apart (solid purple arrows). Large values in the domain that are are far apart map to values in the range that are closer together (dotted purple arrows).
```

As expected a plot of the data in log-log space resolves the clustering-and-scattering problem. After log-log transforming both {math}`\ell^{3}` and {math}`m` the points appear more evenly spaced in the plot (Figure [](fig:logdata)). In addition, the log transformed data suggest there exists a linear relationship between the (transformed) quantities\footnote{Technically, an *affine linear relationship* between transformed quantities.}. 

The linear relationship revealed by Figure [](fig:logdata) is predicted by the model we have proposed. Taking the natural log of both sides of {math}`w=k\, \ell^3` we obtain
```{math}
  \ln w = \ln k + \ln (\ell^{\, 3}).
```
Not only does this argue for a linear relationship between log-transformed variables; it also suggests that the line involved in the linear relationship ought to have a slope equal to 1. Importantly, Figure [](fig:logdata) matches this prediction: a line of slope 1 appears to follow the scatter closely. Just as important: a line of slope {math}`2/3`, which is predicted by an alternative, out-of-thin-air model {math}`w=k\,\ell^2`, does not appear to match the data nearly as well (Figure [](fig:logdata)). 

By extrapolating the solid line in Figure [](fig:logdata), we can determine its vertical intercept to be approximately equal to {math}`-5.1`. Thus, the data suggest that
```{math}
  \ln k = -5.1 \ \leftrightarrow\ k \approx 0.0061
```  
which is not far off the estimate we used in Figure [](fig:bird_cubic). 

Overall, it seems that we have good reason to be confident in our model, even though it is based on a very simplistic view of bird shape. The less credulous reader may still take issue with, what appears to be, an outlier in Figure [](fig:logdata). The largest bird in the data set (the Great Blue Heron) is unusually far away from the straight line and will be of concern to anyone looking for a clear-cut picture of nature. Dealing with this remaining concern will be the focus of the next section.  

:::{figure} ./standalones/plot-Ch0_fig1.pdf
:label: fig:logdata

A plot of {math}`\ln w` against {math}`\ln (\ell^3)`. The solid line has a slope of {math}`1` which is consistent with the model {math}`w = k\, \ell^3`. The dotted line has slope {math}`2/3` and while it matches the predictions that would be made by a model that treats {math}`w` as being proportional to {math}`\ell^2`, it clearly does not match the data well.
:::

## Scaling, Isometry and Allometry

The model we built in the previous section is an example of a *scaling relationship*. We developed the model under the assumption that all birds were simply scaled-up or scaled-down versions of the same cube. This, in turn, allowed us to use what we know about cubes to arrive at a straightforward mathematical formulation. Reasoning similar to that applied in the previous section would have led us to predict that a bird's wingspan ought to be proportional to its length, and that its surface area ought to be proportional to its length squared. These predictions make sense based on our experience with measurement and dimension: both body length and wingspan could be measured in centimetres, whereas surface area would be measured in terms of square-centimetres. 

Even though predictions make sense, intuitively, the outlying data point corresponding to the Great Blue Heron suggests they might break down in certain cases. Here, the breakdown may be due to the fact that  the Great Blue Heron is not simply a scaled-up version of the smaller birds that were included in the data set. As Figure [](fig:bird_pics) shows, the proportions of the heron are quite different from those of other birds. So, it might be unreasonable to expect the heron to follow the pattern established by its not-so-gangly counterparts. It seems wise, therefore, to limit the application of {math}`w=k\ell^3` to similarly shaped birds so as not to undermine our key model assumptions.

:::{figure} ./standalones/image-birds.pdf
:label: fig:bird_pics

The shape of the Great Blue Heron (top left) is quite different from that of other species found in [](tab:birds), including the Mallard (top right), the Yellow Warbler (bottom right), and the Northern Oriole (bottom left). Images reproduced under the terms of the Enhanced Licensing agreement, Adobe Inc.
:::


In general, outliers like the Great Blue Heron are to be expected because birds -- and many other species of vertebrates for that matter -- cannot grow without changing shape. To understand why, you first need to know that the ability of a bone to withstand direct compression is proportional to its cross-sectional area\footnote{The principle, here, is the same one that makes a snowshoe work: force comes to be distributed over a greater area.}. Thus, the weight supported by the skeleton of an animal of length {math}`\ell` is expected to scale as {math}`\ell^2` (i.e., as an area). As we have seen, though, the body weight of the same animal is predicted to scale as {math}`\ell^3`. Consequently, if no change in shape accompanied growth, an animal's body weight would increase much more quickly than its skeleton's ability to support that weight.\footnote{In concrete terms, doubling the body length would increase four-fold the skeleton's ability to withstand compression, but would increase weight by a factor of eight.} Evolution or development helps species or individuals avoid collapsing under their own weight, then, by changing their features at disproportionate rates as size increases.

This brings us to some important terminology. When an organism's features change disproportionately as it grows, we say those features exhibit *allometry*. By contrast, features that remain in constant proportion as growth occurs are said to exhibit *isometry*.  Here are the precise statements.

:::{prf:definition}
:label: def:isometry-allometry

We consider models of the form {math}`y = c u^{\alpha}` where {math}`c` is a *non-zero* constant and {math}`\alpha` is a constants.  

- If {math}`\alpha = 1`, then we say the model **exhibit isometry**.
- If {math}`\alpha \ne 1`, then we say the model **exhibit allometry**.

Note that the value of the constant {math}`c` is NOT used to determine isometry and allometry.
:::


In mathematical terms, quantities {math}`u_1` and {math}`u_2` exhibit allometry when {math}`u_1 = k u_2^m` with {math}`k>0` and {math}`m\neq 1`, but exhibit isometry when {math}`k>0` and {math}`m=1`. Adopting this terminology, we would say that bird weight ({math}`w`) and body length ({math}`\ell`) exhibit allometry, but bird weight and volume ({math}`\ell^3`) exhibit isometry. 

The study of allometric and isometric relationships goes well beyond body shape. Biologists have uncovered scaling relationships involving (but not limited to) metabolic rate, heart rate, nucleotide-substitution rate, and running speed. Given that the scale at which life on earth operates varies over about 10 orders of magnitude, it is likely that there is much more to learn about even the most well-studied scaling relationships. Unfortunately, such explorations are beyond the scope of our course.

## Discrete-time models

Modelling can be made easier by thinking about how one version of a problem depends on simpler versions of the same problem. This kind of self-referential approach to modelling is called *recursion* and its use is widespread.

A well-known example of recursion in mathematics arises with the definition of the factorial. For non-negative integer {math}`n`, the factorial of {math}`n` is defined as {math}`1` if {math}`n=0` and is defined as {math}`n` times the factorial of {math}`(n-1)` otherwise. The recursive definition, along with knowledge about the simplest possible case, allows us to determine the factorial of any non-negative integer in which we might be interested.

In biology, recursive thinking often arises in models of population growth. Suppose we wish to devise a model for the relationship between the size of a deer population, call it {math}`u`, and time in years {math}`t`. A recursive approach to this problem begins by considering how the population size this year depends on the size last year. If {math}`\lambda` denotes the net per-capita reproductive rated, then one could argue that
the size at time {math}`t` is equal to the size at time {math}`t-1` multiplied by {math}`\lambda`. Restating this using some technical notation we get
```{math}
  u_{t} = \lambda \, u_{t-1}.
```
Knowing that {math}`u_0` was equal to some value, say {math}`u_0 =a`, helps us solve the *recursive equation*. Specifically, we find
```{math}
  u_{t} = \underbrace{\lambda \times \cdots \times \lambda}_{t\ {\rm times}} \times u_0
```
and so
```{math}
  u_{t} = \lambda^{t} a, \text{ for all integers } t \ge 0.
```
When {math}`\lambda >1` this model predicts a population explosion. Given that the earth is not overrun with deer, it stands to reason that some refinement of the model is in order. Of course, recursion can help there too.

Recursion will feature in the coming chapters as we investigate modelling applications of differential equations, matrices and vectors, and probability. In biological terms, we can use recursion to explore topics beyond population growth. Recursion is an important part of modelling physiological and developmental processes, disease progression, and (as the next example shows) genetics. 

:::{prf:example}
:label: eg:recursion-alles

Bees, wasps, and ants are insects that belong to the order Hymenoptera. In many hymenopterans, sex is determined by the number of chromosomes an individual possesses. Females carry two sets of chromosomes, one from the method and one from the father.  Males, by contrast, only carry one set of chromosomes from the mother.

Using the given information, what is the probability that an allele (a variant of a gene inside a chromosome) currently carried by a male hymenopteran descended from a male exactly {math}`t` generations ago?
:::

:::{solution .dropdown} eg:recursion-alles

The unknown is the probability that an allele currently carried by a male descended from one carried by a male exactly {math}`t` generations ago.  

We outline the solution before diving into each step.

1. We need to ask ourselves "Is the unknown a single number or a function?" The unknown is a probability that depends on time {math}`t`. Therefore, the unknown is a function function.  We introduce a symbol {math}`p_{t}` to represent this unknown function. 

2. The given information translates into an equation
```{math}
  p_{t} = p_{t-1} \times 0 + (1-p_{t-1}) \times \frac{1}{2} \quad\text{with}\quad p_{0} = 1.
```

3. Using a change of variable {math}`u_{t} = p_{t} - \frac{1}{3}`, we can solve the recurrence using the technique introduced above. The final solution is
```{math}
  p_{t} = \frac{2}{3}\, \left( - \frac{1}{2}\right)^t + \frac{1}{3}
```

Now we analyze the question in depth. Realizing that the unknown is a function suggests modelling the given information using {math}`p_{t}`.  We consider the reproductive process given in the question.

You can replace "*{math}`t` generations ago*" with "*{math}`t`-th predecessor*" whenever you find the language in the question hard to parse.

The symbol {math}`p_{0}` is the probability that an allele descended from a male exactly {math}`0` generation ago.  If you find the sentence hard to parse, give the male a name, say Darth Vader. The sentence becomes "*the symbol {math}`p_{0}` is the probability that an allele descended from Darth Vader exactly {math}`0` generation ago*." Darth Vader's {math}`0`-generation predecessor is just Darth Vader itself. Therefore, {math}`p_{0}` is the probability that an allele carried by Darth Vader comes from Darth Vader, which implies {math}`p_{0} = 1`.

Darth Vader is a male. From the information "*males, by contrast, only carry one set of chromosomes from the mother*," we know that the allele must come from one of the two chromosomes from its mother because the allele cannot come from its father.  The previous sentence translates directly in the equation in step 2.

To solve the recurrence, we simplify the equation in step 2 as
```{math}
p_{t} = -\frac{1}{2} p_{t-1} + \frac{1}{2} \text{ with } p_{0} = 1.
```

Recall the form of the substitution is {math}`p_{t} = u_{t} + (\text{equilibrium}) = u_{t} + \frac{1}{3}`.  Perform substitution to get {math}`u_{t} = -\frac{1}{2} u_{t-1}` with {math}`u_{0} = \frac{2}{3}`.  The recursion in {math}`u` has solution {math}`u_{t} = \frac{2}{3} \left( - \frac{1}{2} \right)^{t}`. Undoing the substitution we get, 
```{math}
p_{t} = \frac{2}{3} \left( - \frac{1}{2} \right)^{t} + \frac{1}{3}, \text{ for all integers } t \ge 0.
```

:::

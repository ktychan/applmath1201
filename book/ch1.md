# Some Modelling Basics

````{prf:definition} mathematical model
:label: def:model

A *mathematical model* is an equation **in which** every symbols is attached to some real-world quantities. 
```{math}
  f( u_1, \ldots , u_n ) = 0.
```

The left-hand side is an expression that relates a bunch of relevant quantities {math}`u_{1}, \ldots, u_{n}` using mathematical operations.
````

You are likely already familiar with a wide range of mathematical models. For example, you know that the model 
```{math}
(\text{area}) - (\text{width}) \times (\text{legnth}) = 0
```
establishes a *connection* between three related quantities of a rectangle.

You might know the ideal gas model model from a chemistry course[^ideal-gas-model]. Under certain conditions, the pressure {math}`P`, volume {math}`V`, and temperature {math}`T` of a gas satisfy 
```{math}
PV - nRT = 0 \quad\text{ where {math}`n` and {math}`R` are constants.}
```
[^ideal-gas-model]:  The idea gas model is usually taught in CHEM 1302.

It's important to recognize that mathematical models need not be perfect. In fact, models often present an abstract view of the reality because they rely on simplifying assumptions. For example, the ideal gas model  
```{math}
PV - nRT = 0 \quad\text{ where {math}`n` and {math}`R` are constants.}
```
assumes that interactions between individual gas molecules can be neglected. As such, the ideal gas model provides accurate predictions for larger volumes of gas at lower pressures. In general, we do not expect mathematical models to explain the world, rather we hope they make useful predictions about what happens therein.  

The remainder of this chapter is devoted to illustrating the points made above. Though we focus on models based on geometry, and on something called recursion, the themes we explore will continue throughout the course. 

## Models from Simple Shapes

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
label: eq:model-mass-length:
    (\text{mass in grams}) = (\text{density constant}) \times (\text{body length in cm})^{3}.
```

## Models must compare apples to apples -- dimensional homogeneity

The equation 
```{math}
  1 = 1
``` 
makes perfect sense in mathematics, but 
```{math}
  1 \text{ apple} = 1 \text{ orange}
```
does not make much sense.  The difference between these two equations is in the interpretation of numbers.  In the first equation, numbers have no units. In the second equation, the two one's have different units and represent different quantities.

Does the model in Equation~\eqref{eq:model-mass-length} makes sense? Do so by comparing the units of each quantity and using physics. 

The quantities in a mathematical model naturally come with units. 

it is *dimensionally homogeneous*, meaning that the units associated with each of its terms match. The quantity {math}`m` is measured in grams, and this agrees with the units we have attached to the product {math}`k \ell^{3}`. The fact that we're not equating apples and oranges gives us some confidence that our model is a reasonable one. Beyond this observation, though, how sure can we be that our model is useful? To answer this question, we can turn to data.

## Visually fitting the data to a model

Table [](#table:birds) presents average length and weight measurements associated with twenty-four species of birds common to Eastern North America. If our model is useful, we would expect a plot of weight versus length to look like the graph of {math}`k\, \ell^3`. A plot of the data in Table [](tab:birds) suggests we are on the right track, in that the data in Table [](tab:birds) tend to follow the graph of {math}`k\ell^3` when {math}`k` is approximately {math}`0.006` (Figure [](fig:bird_cubic)). However, based on Figure [](fig:bird_cubic) alone, one could also argue that the data support a model in which {math}`w` is proportional to {math}`\ell^2`. So the utility of our model (or, at least, its utility compared to that of a model we just pulled out of thin air) is still questionable at this point. Fortunately, we can sort out our confusion by looking at the data in a different way. 

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

The shape of the Great Blue Heron (top left) is quite different from that of other species found in Table [](tab:birds), including the Mallard (top right), the Yellow Warbler (bottom right), and the Northern Oriole (bottom left). Images reproduced under the terms of the Enhanced Licensing agreement, Adobe Inc.
:::

In general, outliers like the Great Blue Heron are to be expected because birds -- and many other species of vertebrates for that matter -- cannot grow without changing shape. To understand why, you first need to know that the ability of a bone to withstand direct compression is proportional to its cross-sectional area\footnote{The principle, here, is the same one that makes a snowshoe work: force comes to be distributed over a greater area.}. Thus, the weight supported by the skeleton of an animal of length {math}`\ell` is expected to scale as {math}`\ell^2` (i.e., as an area). As we have seen, though, the body weight of the same animal is predicted to scale as {math}`\ell^3`. Consequently, if no change in shape accompanied growth, an animal's body weight would increase much more quickly than its skeleton's ability to support that weight.\footnote{In concrete terms, doubling the body length would increase four-fold the skeleton's ability to withstand compression, but would increase weight by a factor of eight.} Evolution or development helps species or individuals avoid collapsing under their own weight, then, by changing their features at disproportionate rates as size increases.

This brings us to some important terminology. When an organism's features change disproportionately as it grows, we say those features exhibit *allometry*. By contrast, features that remain in constant proportion as growth occurs are said to exhibit *isometry*. In mathematical terms, quantities {math}`u_1` and {math}`u_2` exhibit allometry when {math}`u_1 = k u_2^m` with {math}`k>0` and {math}`m\neq 1`, but exhibit isometry when {math}`k>0` and {math}`m=1`. Adopting this terminology, we would say that bird weight ({math}`w`) and body length ({math}`\ell`) exhibit allometry, but bird weight and volume ({math}`\ell^3`) exhibit isometry. 

The study of allometric and isometric relationships goes well beyond body shape. Biologists have uncovered scaling relationships involving (but not limited to) metabolic rate, heart rate, nucleotide-substitution rate, and running speed. Given that the scale at which life on earth operates varies over about 10 orders of magnitude, it is likely that there is much more to learn about even the most well-studied scaling relationships. Unfortunately, such explorations are beyond the scope of our course.

## Models Based on Recursion

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

Bees, wasps, and ants are insects that belong to the order Hymenoptera. In many hymenopterans, sex is determined by the number of chromosomes an individual possesses. Females are diploid because they develop from fertilized oocytes. Males, by contrast, develop from unfertilized oocytes and are haploid. What is the probability that an allele currently carried by a male hymenopteran descended from a male exactly {math}`t` generations ago?
:::

:::{solution .dropdown} eg:recursion-alles

Let {math}`p_t` denote the probability that an allele currently carried by a male descended from one carried by a male exactly {math}`t` generations ago. The quantity {math}`p_t` is what we are looking to model. 

Thinking recursively, we suppose we have solved the modelling problem for {math}`p_{t-1}`. In that case, we could solve modelling problem for {math}`p_t` as follows:
```{math}
  p_t = p_{t-1}\times 0 + (1-p_{t-1}) \times \frac{1}{2} .
```
In words, the previous equation says that if an allele has descended from a male {math}`t-1` generations ago, then there is no chance it also descended from a male {math}`t` generations ago; alternatively, if the allele descended from a female {math}`t-1` generations ago, then it is equally likely to have come from a male or female {math}`t` generations ago. 

Because we are considering an allele that is currently carried by a male, we have {math}`p_0=1`. So, putting all the information together, we have
```{math}
  p_t = -\frac{1}{2} \, p_{t-1} + \frac{1}{2},
  \quad
  \text{and}
  \quad
  p_0 = 1 .
```
We can turn this recursive problem into one we have already solved by defining {math}`u_t = p_t - \frac{1}{3}` and by noting that {math}`\frac{1}{2} = \frac{1}{6} + \frac{1}{3}`. Keeping this in mind, we have
```{math}
  p_t - \frac{1}{3} = - \frac{1}{2}\left( p_{t-1} - \frac{1}{3}\right)
  \ \leftrightarrow\
  u_t = - \frac{1}{2} \, u_{t-1}
```
with {math}`u_0 = p_0-\frac{1}{3} = \frac{2}{3}`.  We now see that
```{math}
  u_t = \frac{2}{3}\, \left( - \frac{1}{2}\right)^t 
```
and so
```{math}
  p = \frac{2}{3}\, \left( - \frac{1}{2}\right)^t + \frac{1}{3}
```
is the model we are looking for. Interestingly, if we go back far enough in time, the probability that an allele currently carried by a male descended from a male settles down to one third. 
:::

# Vectors and Functions of Vectors

Biological systems are often multidimensional. Ecological communities are made of up of numerous interconnected biotic and abiotic components; organs work together to carry out important bodily functions; infectious diseases spread from the sick to the healthy; popular individuals spread their influence across social networks of varying topology. To model any one of these multidimensional scenarios, we must turn to vectors and functions thereof. In this chapter, we review vectors and the mathematical operations we can perform on them. We also introduce the concept of a vector field that is particularly useful for modelling dynamics of biological systems in several dimensions.

## What is a Vector?

A *vector* can be thought of as a finite list of numbers arranged in a specific order. In this course we will often discuss *column vectors* whose constituents are listed vertically. For example,
```{math}
  \vec{u} 
  =
  \begin{bmatrix}
    1 \\
    2 
  \end{bmatrix}
  \quad 
  \text{and}
  \quad
  \vec{v} 
  =
  \begin{bmatrix}
    2 \\ 1
  \end{bmatrix}
```
are column vectors. Note that the vectors {math}`\vec{u}` and {math}`\vec{v}` are different: even though the same numbers are found in both, they are different because the ordering of the numbers in a vector matters. In general, a vector consists of {math}`n` numbers, or *elements*, each identified by a unique subscript. For example,
```{math}
  \vec{x}
  =
  \begin{bmatrix}
    x_1 \\
    x_2 \\
    \vdots \\
    x_n
  \end{bmatrix}	 
```
or sometimes simply {math}`\vec{x} = [ x_{i} ]_{i=1}^n`.

Though we will often work with column vectors in this course, we will also occasionally need to discuss row vectors. A *row vector* is one whose elements are arranged horizontally. We will superscript ``{math}`T`'' to distinguish a row vector from a column vector, so
```{math}
  \vec{u}^{ T} 
  =
  \begin{bmatrix}
    1 & 2
  \end{bmatrix}.
```
The default assumption in the course will be that a vector exists in column form. So {math}`\vec{x} = [x_i]_{i=1}^n` would be a column vector and {math}`\vec{x}^{ T} = [x_j]_{j=1}^n` would be a row vector.

There are other ways to represent vectors, besides thinking of them as ordered lists of numbers. We can, for instance, think of a vector as a point in {math}`n`-dimensional space. If we were to conceive of {math}`\vec{x}` in this way, the element {math}`x_i` would give the position of the point with respect to the {math}`i`th axis used to orient the space itself (Figure [](#fig:vector_rep)a). We can also represent a vector as an arrow whose tail is at the origin and whose tip extends to the aforementioned point in {math}`n`-dimensional space (Figure [](#fig:vector_rep)b). 

:::{figure} ../standalones/build/plot-vector_rep.pdf
:label: fig:vector_rep
We can represent a vector as either (a) a point in {math}`n=2` dimensional space, or as (b) an arrow whose tail is placed at the origin and whose tip extends to the point shown in (a). When representing vectors as points or arrows, we will not make a distinction between those that exist as columns and those that exists as rows.
:::


When we represent a vector as an arrow it seems natural to ask how long the arrow is. Similarly, we we represent a vector as a point we might wonder how far that point is from the origin. In both cases, resolution can be achieved by referencing the magnitude of the vector in question. We define the *magnitude* of the vector {math}`\vec{x}` as 
```{math}
  \| \vec{x}\| = \sqrt{ x_1^2 + x_2^2 + \cdots + x_n^2 }
```
and note that the same definition would apply to the row vector {math}`\vec{x}^{T}`. 

## Operations On and With Vectors

### Multiplication by a constant

We can perform many operations on vectors. One of the simpler operations involves multiplying a vector by a constant number {math}`c` to create a new vector, {math}`c \vec{x}`. In order to multiply a vector by a constant we multiply the given constant by each element of the given vector. Thus,
```{math}
  c  \vec{x}
  =
  \begin{bmatrix}
    c x_1 \\ c x_2\\ \vdots \\ c x_n
  \end{bmatrix}.
```  
The same procedure applies to {math}`c \vec{x}^{ T}`.

It is worth observing that 
```{math}
  \| c \vec{x}\|
  =
  \sqrt{c^2  x_1^2 + c^2 x_2^2 + \cdots + c^2  x_n^2}
  =
  |c| \| \vec{x}\|.
```
In words, when we multiply a vector by a constant {math}`c` we are effectively altering its distance from the origin  (if thought of as a point), or changing its length (if thought of as an arrow) by a factor {math}`|c|`. In addition, when the constant happens to be negative, {math}`c  \vec{x}` reflects the given vector about the origin. This effectively moves the given vector to the opposite orthant (if thought of as a point) or takes the given vector and reverses its direction (if thought of as an arrow).

### Vector addition

We can also take two column vectors (or two row vectors) and add them together to create a new column vector (or a new row vector). Two vectors are added by adding corresponding elements, so
```{math}
  \vec{x} + \vec{y}
  =
  \begin{bmatrix}
    x_1 \\ x_2 \\ \vdots \\ x_n
  \end{bmatrix}
  +
  \begin{bmatrix}
    y_1 \\ y_2 \\ \vdots \\ y_n
  \end{bmatrix}
  =
  \begin{bmatrix}
    x_1 + y_1 \\
    x_2 + y_2 \\
    \vdots \\
    x_n + y_n
  \end{bmatrix}.
```
The same procedure applies when adding two row vectors. 

If we represent vectors {math}`\vec{x}` and {math}`\vec{y}` as points in space, then we can envision adding them by beginning at the point {math}`\vec{x}` and moving from there along each of {math}`i=1, \ldots, n` axes by {math}`y_i = y_1, \ldots, y_n` units, respectively (Figure [](#fig:summation)a). If we represent the vectors as arrows, then we can envision adding them by translating one arrow to the point where its tail touches the tip of the other (Figure [](#fig:summation)b).

:::{figure} ../standalones/build/plot-vector-addition.pdf
:label: fig:summation
We can envision adding {math}`\vec{x} = \begin{bmatrix}1 \\ 2\end{bmatrix}` and {math}`\vec{y} = \begin{bmatrix}2 \\ 1\end{bmatrix}` when vectors are represented as (a) points in {math}`n=2` dimensional space, or as (b) arrows. 
:::


### Linear combinations of vectors

We have yet to address vector subtraction, but it is easy to see how this operation would work by combining what we know about vector addition with what we know about multiplication of a vector by a constant. To subtract {math}`\vec{y}` from {math}`\vec{x}` we can multiply the former vector by the constant {math}`(-1)` and add the result to the latter vector. That is to say,
```{math}
  \vec{x} - \vec{y}
  =
  \vec{x} + (-1) \vec{y}.
```
The previous equation provides an example of what we call, a linear combination of vectors. Formally, if {math}`\vec{x}_1, \ldots, \vec{x}_n` is a collection of {math}`n` vectors, and {math}`c_1, \ldots, c_n` is a collection of {math}`n` constants, then {math}`c_1 \vec{x}_1 + \cdots + c_n  \vec{x}_n` is a *linear combination* of the vectors.

:::{prf:example} 
:label: eg:vector-decomposition
Show that any vector that can be represented as a point in two dimensions can also be expressed as a linear combination of {math}`\vec{e}_1 = \begin{bmatrix}1\\ 0\end{bmatrix}` and {math}`\vec{e}_2 =\begin{bmatrix}0\\ 1\end{bmatrix}`. In other words, show that {math}`\vec{e}_1` and {math}`\vec{e}_2` form a *basis* for two-dimensional space.
:::
:::{solution .dropdown} eg:vector-decomposition
Any vector that can be represented as a point in two-dimensional can also be written as {math}`\vec{u} = \begin{bmatrix} u_1 \\ u_2\end{bmatrix}`. We now observe that
```{math}
  \vec{u} = 
  \begin{bmatrix}
    u_1 \\ u_2 
  \end{bmatrix}
  = 
  u_1 
  \begin{bmatrix}
    1 \\ 0
  \end{bmatrix}
  +
  u_2
  \begin{bmatrix}
    0 \\ 1
  \end{bmatrix}
  =
  u_1  \vec{e}_1
  +
  u_2  \vec{e}_2
```
as required.
:::

### Dot product of vectors

The *dot product* of two vectors {math}`\vec{x}` and {math}`\vec{y}` is defined as
```{math}
  \vec{x} \bullet \vec{y} = x_1 y_1 + \cdots + x_n y_n.
``` 
Alternatively, the dot product can be expressed as
```{math}
  \vec{x} \bullet \vec{y} = \| \vec{x}\|  \| \vec{y}\|  \cos \theta
```
where {math}`\theta` is the angle made between the line segments made by joining the origin to the points corresponding to {math}`\vec{x}` and {math}`\vec{y}`, respectively. 

:::{figure} ../standalones/build/plot-cosine-law.pdf
:label: fig:dotprod
If {math}`\vec{x}` casts a shadow onto {math}`\vec{y}` as shown above, then the dot product {math}`\vec{x}\bullet \vec{y}` gives the length of the shadow expressed as a multiple of the magnitude of {math}`\| y\|`.
:::

The alternative expression for the dot product allows us to interpret the result of this operation as the length of the projection of {math}`\vec{x}` onto {math}`\vec{y}`, or vice versa. Loosely speaking, if we were to shine a light directly above {math}`\vec{x}`, as shown in Figure [](#fig:dotprod), then {math}`\vec{x} \bullet \vec{y}` would give the length of the shadow cast by {math}`\vec{x}` in terms of the magnitude of {math}`\vec{y}`. 

:::{prf:example} 
:label: eg:dotprod
Verify {math}`\vec{x}\bullet\vec{y} = \| \vec{x}\|  \| \vec{y}\|  \cos \theta` for the case in which vectors can be represented as points in two-dimensions.
:::
:::{solution .dropdown} eg:dotprod
Consider the triangle {math}`AOB` spanned by the vectors {math}`\vec{x}` and {math}`\vec{y}`. From the picture below it is evident that {math}`|AB|` is equal to {math}`\| \vec{x}-\vec{y}\|`.

```{figure} ../standalones/build/plot-dotprod-triangle.pdf
```

The Law of Cosines gives us 
```{math}
  \| \vec{x}-\vec{y}\|^2
  =
  \| \vec{x}\|^2
  +
  \| \vec{y}\|^2
  - 
  2 \| \vec{x}\| \|\vec{y}\| \cos\theta
```
where {math}`\theta` is {math}`\angle AOB`. Rearranging the previous expression yields
```{math}
\begin{array}{lcl}
  \| \vec{x}\| \|\vec{y}\| \cos\theta 
  &=& \dfrac{1}{2} \left( \| \vec{x}\|^2 + \| \vec{y}\|^2 \| \vec{x}-\vec{y}\|^2 \right) \\
  &=& \dfrac{1}{2} \left( x_1^2 + x_2^2 y_1^2 + y_2^2 (x_1-y_1)^2 (x_2-y_2)^2 \right) \\
  &=& x_1 y_1 + x_2 y_2 = \vec{x} \bullet \vec{y}.
\end{array}
```
This concludes the exercise.
:::

For vectors that exist as points or arrows in three dimensions, we can also define the cross-product. The *cross-product* of vectors {math}`\vec{x}` and {math}`\vec{y}` as follows
```{math}
  \vec{x}\times \vec{y}
  =
  \begin{bmatrix}
    x_2  y_3 - x_3 y_2 \\
    x_3 y_1 - x_1 y_3 \\
    x_1  y_2 - x_2 y_1 
  \end{bmatrix}.
```
Note that, unlike the dot product, the cross product of two vectors results is, itself, a vector. In particular, the vector {math}`\vec{x}\times \vec{y}`, thought of as an arrow, is perpendicular to the plane spanned by {math}`\vec{x}` and {math}`\vec{y}` (Figure [](#fig:xprod)). It is also easy to verify that {math}`\vec{y}\times \vec{x} = - (\vec{x}\times \vec{y})`. Thus, while the vector {math}`\vec{y}\times \vec{x}` is also perpendicular to the plane spanned by {math}`\vec{x}` and {math}`\vec{y}` it points the opposite direction to {math}`\vec{x} \times \vec{y}` (Figure [](#fig:dotprod)). 

:::{figure} 
:label: fig:xprod

The cross product of two vectors {math}`\vec{x}\times \vec{y}` is, itself, a vector that is perpendicular to the plane spanned by {math}`\vec{x}` and {math}`\vec{y}`. The cross product {math}`\vec{y}\times\vec{x}` is perpendicular to the same plane, but points in the opposite direction. A ``right-hand rule'' can be used to determine the direction of the cross product of a given pair of vectors: when one's right index finger points in the direction of the first vector of the given pair, and one's right middle finger points in the direction of the second vector, then the direction of the cross product is given by one's right thumb.
:::

The cross product can also be expressed as
```{math}
  \vec{x} \times \vec{y} = \left( \| \vec{x}\| \| \vec{y}\|  \sin \theta  \right) \vec{n}
```
where {math}`\theta` is the angle between {math}`\vec{x}` and {math}`\vec{y}`, and {math}`\vec{n}` is the vector with unit magnitude that points in the same direction as {math}`\vec{x}\times\vec{y}`. We will omit the proof of this identity, as we introduce it primarily to help solve the following example.

:::{prf:example} 
:label: eg:area
Show that the area of the parallelogram spanned by the vectors {math}`\begin{bmatrix}a\\ c\end{bmatrix}` and {math}`\begin{bmatrix}b\\ d\end{bmatrix}` is given by {math}`\| \vec{x} \times \vec{y}\|` where 
```{math}
  \vec{x}
  =
  \begin{bmatrix}
    a \\ c \\ 0
  \end{bmatrix}
  \quad \text{and}\quad
  \vec{y}
  =
  \begin{bmatrix}
    b \\ d \\ 0
  \end{bmatrix}.
``` 
:::
:::{solution .dropdown} eg:area
We use {math}`OABC` to denote the parallelogram spanned by the vectors {math}`\vec{x}` and {math}`\vec{y}` as shown below. 

```{figure} ../standalones/build/plot-cross-product-exercise.pdf
```

The area of the parallelogram is determined as
```{math}
\begin{array}{lcl}
  \text{base} \cdot \text{height}
  &=& |OC| \cdot |OA| \sin ( \angle AOC )\\
  &=& |OC| \cdot |OA| \sin ( \angle DOA ) \\
  &=& \| \vec{x}\| \| \vec{y}\|  \sin \theta \\
  &=& \| \vec{x}\| \| \vec{y}\|  \sin (\pi - \theta).
\end{array}
```	

Since {math}`0<\theta< \pi`, we have used the fact that {math}`\sin \theta =\sin(\pi - \theta)`. In addition {math}`0<\theta< \pi` implies that {math}`\sin \theta = |\sin\theta|`, and so
```{math}
  \text{Area of}\ OABC 
  = \| \vec{x}\| \| \vec{y}\|  |\sin \theta | 
  = \| \vec{x} \times \vec{y}\|.
```

For later use, note that {math}`\|  \vec{x} \times \vec{y}\| = |ad-bc|`.
:::

## Functions of Vectors

### Real-valued functions

Functions can take vectors as their input. When the output of such a function is a real number, the function is described as being *real-valued*. An example of a real-valued function is the following
```{math}
  f(\vec{x}) = f(x_1,x_2) = x_1 e^{- x_1^2 - x_2^2}
```  
the graph of which can be visualized as a surface in three-dimensions (Figure [](#fig:surface)).

:::{figure} ./standalones/plot-surface1
:label: fig:surface

The graph of the real-valued function {math}`f(\vec{x}) = x_1 e^{-x_1^2-x_2^2}` presented as a surface in three dimensions.
:::

A real-valued function is said to be *linear* if it preserves linear combinations of its arguments. Mathematically, this means 
```{math}
  f( c_1  \vec{x} + c_2 \vec{y} ) = c_1  f(\vec{x} ) + c_2  f (\vec{y})
```
where {math}`c_1` and {math}`c_2` are constants. The previous line says that a function {math}`f` is linear if and only if the application of {math}`f` to a linear combination of vectors is equivalent to taking the same linear combination of {math}`f` applied to each vector individually. In other words, a linear function preserves linear combinations.

:::{prf:example}
:label: eg:linearity
Show that {math}`f(x_1, x_2) = a x_1+bx_2` preserves linear combinations of vectors.
:::
:::{solution .dropdown} eg:linearity
Let {math}`\vec{x}` and {math}`\vec{y}` be vectors that exist as points in two-dimensional space, and let {math}`c_1` and {math}`c_2` be constants. Then
```{math}
\begin{array}{lcl}
  f(c_1 \vec{x} + c_2 \vec{y})
  &=& a (c_1  x_1 + c_2 y_1) b (c_1  x_2 + c_2 y_2) \\
  &=& c_1 ( a x_1 + b x_2 ) c_2 ( a y_1 + b y_2 ) \\
  &=& c_1  f(x_1, x_2) + c_2 f(y_1, y_2).
\end{array}
``` 
This concludes the solution.
:::

The previous example shows that if {math}`f` takes the given form, then it is linear. The converse of that statement is also true: if {math}`f` is linear it must take the form given in the example. To see why, note that {math}`\vec x` can always be written as {math}`x_1 \begin{bmatrix} 1\\ 0 \end{bmatrix}  + x_2 \begin{bmatrix} 0\\1 \end{bmatrix}`. Because {math}`f` is linear, we can then write
```{math}
  f ( \vec x)
  =
  f\left(x_1 \begin{bmatrix}
      1\\ 0
      \end{bmatrix}  + x_2 \begin{bmatrix}
      0\\1
  \end{bmatrix} \right)
  = 
  x_1 
  f\left( \begin{bmatrix}
      1\\ 0
      \end{bmatrix} \right) + x_2 f\left( \begin{bmatrix}
      0\\1
  \end{bmatrix} \right).
``` 
Here, {math}`f\left( \begin{bmatrix} 1\\ 0 \end{bmatrix} \right)` plays the role of the constant {math}`a` in Example 4, while {math}`f\left( \begin{bmatrix} 0\\ 1 \end{bmatrix} \right)` plays the role of the constant {math}`b`.

The take-home message, here, is that linear real-valued functions can always always be written as
```{math}
  f(x_1, x_2, \ldots, x_n) = \sum_{j=1}^{n} a_{j}  x_{j}
```
for some set of constants {math}`a_1, a_2, \ldots a_n`. Notice that this is equivalent to saying that any linear function {math}`f` can be represented as the dot product between a vector of constants {math}`\vec{a}` and the vector argument of the function itself, {math}`\vec{x}`. That is, {math}`f(\vec{x}) = \vec{a}\bullet\vec{x}`. 

### Vector-valued functions

When the output of a function is a vector, rather than a real number, the function is described as being *vector-valued*. In general, these functions take a vector with {math}`n` elements and map it to a vector with {math}`m` elements. In other words, the domain of a vector-valued function is {math}`n`-dimensional space, and the range is {math}`m`-dimensional space. 

We write the general vector-valued function as follows:
```{math}
  \vec{F}(\vec{x})
  =
  \vec{F} ( x_1, x_2, \ldots, x_n)
  =
  \begin{bmatrix}
    f_1 (x_1, x_2, \ldots, x_n) \\
    f_2 (x_2, x_2, \ldots, x_n) \\
    \vdots\\
    f_m (x_1, x_2, \ldots, x_n)
  \end{bmatrix}
``` 
where each {math}`f_i` is a real-valued function of the {math}`n`-dimensional vector, {math}`\vec{x}`. We will pay particular attention to linear vector-valued functions in this course; in other words, those vector-valued functions whose components are all linear. If {math}`\vec{a}_i^{ T} = [a_{i1}, a_{i2}, \ldots, a_{in}]` is the vector of {math}`n` constants associated with the {math}`i`th component of {math}`\vec{F}`, then we can represent {math}`\vec{F}` as
```{math}
  \vec{F}(\vec{x})
  =
  \begin{bmatrix}
    \vec{a}_1 \bullet \vec{x} \\
    \vec{a}_2 \bullet \vec{x} \\
    \vdots \\
    \vec{a}_m \bullet \vec{x}
  \end{bmatrix}.
``` 
It is usual to store all constants associated with a given vector-valued function in a rectangular arrangement of numbers known as a *matrix*. Using our general notation, the matrix associated with a vector-valued function {math}`\vec{F}` is written as
```{math}
  A
  =
  \begin{bmatrix}
    \vec{a}_1^{ T} \\
    \vec{a}_2^{ T} \\
    \vdots \\
    \vec{a}_m^{ T}
  \end{bmatrix}
  =
  \begin{bmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    a_{21} & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots &\ddots & \vdots \\
    a_{m1} & a_{m2} & \cdots & a_{mn} 
  \end{bmatrix}.
```
As the previous line suggests, a matrix stores numbers that are themselves arranged into {math}`m` rows and {math}`n` columns. When discussing the vector-valued function {math}`\vec{F}` it is understood that the {math}`i`th row of the corresponding matrix contains the constants associated with {math}`f_i`.

It is also usual to see linear vector-valued functions written simply as {math}`\vec{F}(\vec{x}) = A \vec{x}` (but not as {math}`\vec{x} A` for reasons that are not important to us at the moment). In this case, it is understood that the matrix-vector product {math}`A \vec{x}` is, itself, a new vector of {math}`m` elements. Moreover, the {math}`i`th element of this new vector is determined by taking the dot product of {math}`\vec{x}` and the {math}`i`th row of {math}`A`. With that convention in mind, one can easily show that {math}`\vec{F}` preserves linear combinations of its arguments. That is 
```{math}
  A (c_1 \vec{x}_1 + \cdots + c_1  \vec{x}_n)
  =
  c_1 A \vec{x}_1 + \cdots + c_2  A  \vec{x}_n 
```
where it is understood that a {math}`c_i  A` represents multiplication of each row of {math}`A` by the constant {math}`c_i`.

:::{prf:example}
:label: eg:linearity2
Consider the linear vector-valued function suggested by 
```{math}
  A
  =
  \begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6
  \end{bmatrix}.
```
Show that this linear vector-valued function does indeed preserve linear combinations of two vectors.
:::

:::{solution .dropdown} eg:linearity2
The matrix {math}`A` has {math}`m=2` rows and {math}`n=3` columns. Consequently, it transforms a vector with {math}`3` elements into a new vector with {math}`2` elements. In other words, the domain of the function is three-dimensional space and its range is two-dimensional space.

Let {math}`\vec{x}` and {math}`\vec{y}` be two vectors that exist in three-dimensional space, and let {math}`c` and {math}`d` be two constants. Now consider
```{math}
  A ( c \vec{x} + d  \vec{y} )
  = 
  \begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6
  \end{bmatrix}
  \begin{bmatrix}
    c  x_1 + d y_1 \\
    c  x_2 + d y_2 \\
    c  x_3 + d y_3
  \end{bmatrix}.
```
Taking the dot product between the vector on the far right and each row of the matrix, we get
```{math}
  \begin{bmatrix}
    c x_1 + d y_1 
    +
    2(c x_2 + d y_2 )
    + 
    3(c x_3 + d y_3 ) \\
    4(c x_1 + d y_1) 
    +
    5(c x_2 + d y_2 )
    + 
    6(c x_3 + d y_3 )
  \end{bmatrix}
```
which is a two-dimensional column vector, as expected. Next, using what we know about vectors we can re-write the previous line as
```{math}
  c
  \begin{bmatrix}
    x_1 + 2 x_2 + 3  x_3 \\
    4 x_1 + 5 x_2 + 6 x_3
  \end{bmatrix}
  +
  d
  \begin{bmatrix}
    y_1 + 2 y_2 + 3  y_3 \\
    4 y_1 + 5 y_2 + 6 y_3
  \end{bmatrix}
```
which is equivalent to {math}`c A \vec{x} + d A \vec{y}` as required.
:::

### Vector fields

Our main preoccupation for the rest of the course will be with a specific class of vector-valued functions known as vector fields. A *vector field* is a vector-valued function that maps {math}`n`-dimensional vectors to {math}`n`-dimensional vectors (Figure [](#fig:mapping)). A linear vector field can be summarized with a square matrix, i.e. one that consists of {math}`n` rows and {math}`n` columns. 

```{figure} ../standalones/build/plot-linear-transformation.pdf
:label: fig:mapping
A linear vector field {math}`\vec{F}(\vec{x})=A \vec{x}` transforms a given {math}`n`-dimensional vector, {math}`\vec{x}`, in the function's domain into a new {math}`n`-dimensional vector, {math}`A \vec{x}`, in the function's range. 
```

We can depict a vector field {math}`\vec{F}(\vec{x}) = A \vec{x}`  graphically by drawing the new {math}`n`-dimensional vector {math}`A \vec{x}` as an arrow applied at the point {math}`\vec{x}`. In other words, the tail of {math}`A \vec{x}` is placed at the point corresponding to {math}`\vec{x}` and the tip is placed at the point corresponding to {math}`\vec{x} + A \vec{x}`. An example is provided in Figure [](#fig:vf). As this example demonstrates, a vector field suggests movement through {math}`n`-dimensional space: each element of {math}`\vec{F}(\vec{x})` can be interpreted as the component of the instantaneous velocity of a hypothetical particle at location {math}`\vec{x}`. It should not come as a surprise, then, that vector fields can be used to model the dynamics of higher-dimensional biological systems.

:::{figure} ../standalones/build/plot-vector-field-geoff.pdf
:label: fig:vf
The linear vector field {math}`\vec{F}(\vec{x}) = A \vec{x}`  can be depicted by applying the vector {math}`A \vec{x}` to the point {math}`\vec{x}` in the domain of {math}`\vec{F}`. In this example {math}`A = \begin{bmatrix} 0 & -0.1 \\ 0.1 & 0\end{bmatrix}`. As the plot demonstrates, vector fields suggest motion in space. Importantly, linear vector fields, like the one shown here, do not always suggest motion in straight lines. 
:::


:::{prf:example} 
:label: eg:age
Consider an age-structured population composed of juveniles and adults. A fraction {math}`s_1` of the juveniles present at the beginning of a given year survive and mature to become an adults at the beginning of the next year, while the rest die. In addition, a fraction {math}`s_2` of the adults present at the beginning of a given year survive to the next year, while the rest die. Finally, each adult at the beginning of a given year produces {math}`b` offspring who become juveniles at the beginning of the next year. 

Given this information devise a vector field that describes the dynamics of the population. Use the model to predict the number of adults and juveniles found after two years, if there are {math}`2` juveniles and {math}`4` adults in the current year.   
:::
:::{solution .dropdown} eg:age
Let {math}`x_1(t)` be the number of juveniles in the population at the beginning of year {math}`t`, and let {math}`x_2(t)` be the number of adults in the population at the beginning of time {math}`t`. 

Using recursive reasoning we can assert
```{math}
  x_1(t+1) = b x_2(t).
```
This says that the juveniles in the next year are the result of the total reproduction that occurred in the current year. Recursive reasoning also gives us
```{math}
  x_2(t+1) = s_1  x_1(t) + s_2  x_2(t)
```
which means that the adults next year either come from the juveniles in current year who survived and matured, or come from the adults in the current year who survived. 
Overall, the dynamics can be captured by the linear vector field {math}`\vec{F}(\vec{x}(t)) = A \vec{x}(t)` where
```{math}
  A =
  \begin{bmatrix}
    0 & b \\ s_1 & s_2
  \end{bmatrix}.
```

We are told that {math}`\vec{x}(0) = \begin{bmatrix} 2 \\ 4 \end{bmatrix}`, and so
```{math}
  \begin{bmatrix}
    x_1 (1) \\ x_2(1)
  \end{bmatrix}
  =
  \begin{bmatrix}
    0 & b \\
    s_1 & s_2 
  \end{bmatrix}
  \begin{bmatrix}
    2 \\ 4
  \end{bmatrix}
  =
  \begin{bmatrix}
    4 b \\ 2 s_1 + 4 s_2
  \end{bmatrix}
```
and
```{math}
  \begin{bmatrix}
    x_1 (1) \\ x_2(1)
  \end{bmatrix}
  =
  \begin{bmatrix}
    0 & b \\
    s_1 & s_2 
  \end{bmatrix}
  \begin{bmatrix}
    4 b \\ 2 s_1 + 4 s_2
  \end{bmatrix}
  =
  \begin{bmatrix}
    2 s_1  b + 4 s_2 b \\
    4 b s_1 + 2 s_1 s_2 + 4 s_2^2.
  \end{bmatrix}
```
So, there are {math}`2 s_1  b + 4 s_2 b` juveniles and {math}`4 b s_1 + 2 s_1 s_2 + 4 s_2^2` adults after two years.
:::

A few of remarks about the previous example are warranted. First, the motion described by the vector field in the example can be envisioned as a displacement from the tip of {math}`\vec{x}(t)` to the tip of {math}`\vec{F}(\vec{x}(t))`.  A sense of motion, then, is arguably captured better by applying the vector {math}`\Delta\vec{x}(t)=\vec{F}(\vec{x}(t)) - \vec{x}(t)` to the point {math}`\vec{x}(t)` (Figure [](#fig:dt_motion)). 

:::{figure} ../standalones/build/plot-dt_motion.pdf
:label: fig:dt_motion
A sense of motion in Example [](#eg:age) is best captured by considering the vector field {math}`\Delta\vec{x}(t)=\vec{F}(\vec{x}(t)) - \vec{x}(t)` as the population moves from location {math}`\vec{x}(t)` at time {math}`t` to location {math}`\vec{x}(t+1) = \vec{F}(\vec{x}(t))` at time {math}`t+1`.
:::

Second, the distribution of individuals across the various age categories after {math}`t` is
```{math}
  \vec{x}(t) = \underbrace{A  A  \cdots A}_{n\ \text{times}}  \vec{x}(0)
```
which is reminiscent of a result we encountered in our discussion of linear population growth in Chapter 1. 

Third, and for use in a later chapter, it is possible to represent the vector-valued function in the example as a network of nodes and arrows. As shown in Figure [](#fig:transition-diagram), the nodes of the network represent the numbers of juveniles and adults, respectively, in the population at the beginning of a given year. The arrows, by contrast, represent demographic processes like survival and reproduction. Multiplying the labels on the arrow with the variable labelling the node connected to arrow's tail give next-year's value of the variable labelling the node connected to the arrows tip.

:::{figure} ../standalones/build/plot-adult-juveniles-transition-diagram.pdf
:label: fig:transition-diagram
A network representation of the vector field in Example [](#eg.age). Nodes represent age classes and arrows represent demographic processes. To find the number of individuals in a given age class next year we consider all arrows pointing into the corresponding node. We then take  follow each of these arrows back to their source, taking the product of the constant labelling the arrow and the variable found at its tail; the next-year's value is the sum of the products for each of the arrows pointing into a given age class.
:::

### Invertible vector fields

Returning to our broader discussion of linear vector fields, we note that it will sometimes be necessary to consider the inverse of {math}`\vec{F}(\vec{x}) = A \vec{x}`, called {math}`\vec{F}^{-1}(\vec{x})` (Figure [](#fig:mapping_inv)). Unlike linear real-valued functions of one variable, however, the inverse of a linear vector field may or may not exist. We would, therefore, like to have a decisive method for determining whether or not a linear vector field is invertible or not. We close out this chapter by developing such a method.

:::{figure} ../standalones/build/plot-invertible-vf.pdf
:label: fig:mapping_inv
If a linear vector field {math}`\vec{F}(\vec{x})=A \vec{x}` can be inverted, its inverse {math}`\vec{F}^{-1}(\vec{x})` is a also a linear vector field.  We use {math}`A^{-1}` to denote the matrix associated with {math}`F^{-1}(\vec{x})`.
:::

To make progress, let's consider the vector field {math}`\vec{F}` defined by the matrix
```{math}
  A
  =
  \begin{bmatrix}
    a & b \\
    c & d
  \end{bmatrix}.
```
Rather than depicting this function as we did in Figure [](#fig:vf), we will depict it as we have done in Figures [](#fig:mapping) and [](#fig:mapping_inv). In particular, we will consider where the unit square in the domain of {math}`\vec{F}` maps to in the range.

The unit square in two dimensions can be described as the set of all linear combinations of {math}`\begin{bmatrix}1\\ 0\end{bmatrix}` and {math}`\begin{bmatrix}0\\ 1\end{bmatrix}` constructed as follows:
```{math}
  c_1  
  \begin{bmatrix}
    1 \\ 0
  \end{bmatrix}
  + 
  c_2
  \begin{bmatrix}
    0 \\ 1
  \end{bmatrix},
  \quad
  0 \leq c_1,c_2 \leq 1.
```
Using what we know about linear vector-valued functions, we can see that the unit square maps to the set
```{math}
  c_1 	
  \begin{bmatrix}
    a & b \\
    c & d
  \end{bmatrix} 
  \begin{bmatrix}
    1 \\ 0	
  \end{bmatrix}
  +
  c_2 
  \begin{bmatrix}
    a & b \\
    c & d
  \end{bmatrix}
  \begin{bmatrix}
    0 \\ 1
  \end{bmatrix}
  =
  c_1 
  \begin{bmatrix}
    a \\ c	
  \end{bmatrix}
  +
  c_2 
  \begin{bmatrix}
    b \\ d
  \end{bmatrix},
  \quad
  0 \leq c_1,c_2 \leq 1
```
which can be viewed as a parallelogram in the range. In fact, the parallelogram in question is spanned by {math}`\begin{bmatrix} a \\ c\end{bmatrix}` and {math}`\begin{bmatrix} b \\ d\end{bmatrix}`, and as we have seen in Example [](#eg:area) its area is given by 
```{math}
  |ad - bc|.
```
With this in mind, what happens when {math}`ad=bc`? The answer is that, when {math}`ad=bc`, the unit square in domain of {math}`\vec{F}` collapses to a line or a point. In this case, then, it is impossible to tell definitively from where a point in the range originated. That is to say, {math}`\vec{F}` associated with {math}`A = \begin{bmatrix}a & b \\ c & d\end{bmatrix}` cannot be inverted. This suggests that {math}`ad-bc` can be used to determine whether or not a two-dimensional vector field can be inverted: when {math}`ad-bc \neq 0` the two dimensional vector field can be inverted, and when {math}`ad-bc = 0` it cannot. In recognition of this fact we define the *determinant* of a matrix {math}`A = \begin{bmatrix}a & b \\ c & d\end{bmatrix}`
```{math}
  \det \begin{bmatrix}
    a & b \\ c & d
  \end{bmatrix} = ad - bc.
```

In general, a square matrix {math}`A` is invertible if and only if its determinant is non zero. Calculating {math}`\det A` for a large matrix is particularly tedious. For example,
```{math}
\begin{aligned}
  & \det 
  \begin{bmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23} \\
    a_{31} & a_{32} & a_{33}  
  \end{bmatrix} \\[5ex]
  =&
  a_{11}  
  \det
  \begin{bmatrix}
    a_{22} & a_{23} \\
    a_{32} & a_{33} 
  \end{bmatrix}
  -
  a_{12}  
  \det
  \begin{bmatrix}
    a_{21} & a_{23} \\
    a_{31} & a_{33} 
  \end{bmatrix}
  +
  a_{13}  
  \det
  \begin{bmatrix}
    a_{21} & a_{22} \\
    a_{31} & a_{32} 
  \end{bmatrix}
\end{aligned}
```
and similar recursive definitions apply to matrices that are larger still.

The final example of this chapter is meant to illustrate an interesting feature of non-invertible vector fields (and their corresponding matrices). 
:::{prf:example} 
:label: eg:non-invertible-matrix
Suppose {math}`\vec{F}(\vec{x}) = A \vec{x}` with {math}`A=\begin{bmatrix}a & b \\ c & d\end{bmatrix}` and {math}`\det A = 0`. Find a vector, other than {math}`\begin{bmatrix} 0 \\ 0\end{bmatrix}`, such that {math}`A \vec{x} = \begin{bmatrix} 0 \\ 0\end{bmatrix}`. 
:::
:::{solution .dropdown} eg:non-invertible-matrix
We can express {math}`A \vec{x} = \begin{bmatrix} 0 \\ 0\end{bmatrix}` as
```{math}
  \begin{array}{lcl}
    a x_1 + b x_2 &=& 0 \\
    c x_1 + d x_2 &=& 0
  \end{array}
```
From the first of these equations we get {math}`x_2 = -\frac{a}{b}x_1`. Substituting this into the second equation we find
```{math}
  c  x_1 + d (-\frac{a}{b} x_1) = 0
  \ \leftrightarrow\ 
  (ad - bc)  x_1 = 0.
```
Since {math}`\det A = 0` we know that the previous equation is satisfied for any value of {math}`x_1\neq 0` we might care to choose. It follows that any vector of the form
```{math}
  \begin{bmatrix}
    x_1 \\ - \frac{a}{b} x_1
  \end{bmatrix}
```
satisfies {math}`A \vec{x} = \begin{bmatrix} 0 \\ 0\end{bmatrix}`. To put it slightly differently, any point in the domain that lies on the line of slope {math}`-a/b` that passes through the origin will collapse onto the origin in the range. 
:::

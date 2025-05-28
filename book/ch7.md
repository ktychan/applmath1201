# Eigenvalues and Eigenvectors

In this chapter, we focus on the following question. Given a square matrix {math}`A`, can we find a number {math}`\lambda` and a non-zero vector {math}`\vec{v}` such that {math}`A\vec{v} = \lambda \vec{v}`? 
In other words, can we find examples where matrix-vector multiplication can be replaced by multiplication by a constant? This is called *an eigenvalue problem*.

At first glance, it might seem that the eigenvalue problem is unlikely to be connected to biology. However, its solution is relevant to anyone looking to model the dynamics of biological systems. Its solution is is also relevant to many modern data-driven modelling techniques. 

In the sections that follow, we develop the solution to the eigenvalue problem, then demonstrate how it can be applied to analyse the dynamics of age-structured populations. In a later chapter, we will see how we can use the solution to the eigenvalue problem to study systems of coupled differential equations.

## Solving the eigenvalue problem

Given a square matrix {math}`A` can we find a number {math}`\lambda` and a non-zero vector {math}`\vec{v}` such that {math}`A \vec{v}= \lambda \vec{v}`? The short answer is yes. In general, we can find several such number-vector pairs. The numbers {math}`\lambda` are called *eigenvalues* and the corresponding vectors {math}`\vec{v}` are called *eigenvectors*. 

To find an eigenvalue-eigenvector pair we start with the central equation:
```{math}
  A \vec{v} = \lambda \vec{v}.
```
Subtracting {math}`\lambda \vec{v}` from both sides of the previous line gives us
```{math}
  A \vec{v} - \lambda \vec{v} = \vec{0}
```
where {math}`\vec{0}` is an {math}`n`-dimensional vector containing only zeros. Our next move involves factoring {math}`\vec{v}` out of the left side of our equation, and we will do this in a couple of steps. First we recognize that {math}`\vec{v}` can be expressed as the product of the matrix
```{math}
  I =
  \begin{bmatrix}
    1 & 0 & \cdots & & &0 \\
    0 & 1 & \cdots & && 0 \\
    \vdots & & \ddots & & & \vdots \\
           & & & & &0 \\
    0 & \cdots &  &0 && 1
  \end{bmatrix}
```
and {math}`\vec{v}` itself; that is, {math}`\vec{v} = I  \vec{v}`. Thus, our equation becomes
```{math}
  A \vec{v} - \lambda I \vec{v} = 0.
```
Next, we right-factor {math}`\vec{v}` from the left-hand side of the equation to get,
```{math}
  (A - \lambda I) \vec{v} = \vec{0}.
```
To understand the what is happening in the previous line, we must first recognize that 
```{math}
  \lambda  I =
  \begin{bmatrix}
    \lambda & 0 & \cdots & & &0 \\
    0 & \lambda & \cdots & && 0 \\
    \vdots & & \ddots & & & \vdots \\
           & & & & &0 \\
    0 & \cdots &  &0 && \lambda
  \end{bmatrix},
``` 
because multiplication of a matrix by a constant is carried out by multiplying each number in the matrix by the constant in the regular way. Second, we must recognize that {math}`A - \lambda I` can be understood as a single matrix: addition and subtraction is defined for matrices of identical dimensions, and is carried out by adding/subtracting corresponding elements in the usual way. Finally, we must recognize that we have factored {math}`\vec{v}` to the right of the terms in brackets because {math}`\vec{v} ( A - \lambda I)` does not mean anything to us.

At this point we have {math}`(A - \lambda I)  \vec{v} = \vec{0}`. This tells us that the matrix {math}`(A - \lambda I)` maps the non-zero vector {math}`\vec{v}` to the origin in the range. Of course any matrix, including {math}`(A - \lambda I)`, maps the origin in the domain to the origin in the range. It follows that {math}`(A - \lambda I)` is not invertible and so it must be true that
```{math}
  \det (A - \lambda I) = 0.
```
in keeping with the test we encountered in the previous chapter. As we will see in the next example, the test  gives us an equation that we can solve to find the eigenvalues {math}`\lambda`. 

:::{prf:example}
:label: eg:eigen1
Find the eigenvalues of the matrix {math}`A = \begin{bmatrix} 2 & 1 \\ 1 & -1\end{bmatrix}`. 
:::

:::{solution .dropdown} eg:eigen1
We start by constructing {math}`A - \lambda  I`, and we find that
```{math}
  A - \lambda I
  =
  \begin{bmatrix}
    2 & 1 \\
    1 &-1
  \end{bmatrix}
  -
  \begin{bmatrix}
    \lambda & 0 \\ 0 & \lambda
  \end{bmatrix}
  =
  \begin{bmatrix}
    2 - \lambda & 1 - 0 \\
    1 - 0 & -1 - \lambda
  \end{bmatrix}
  =
  \begin{bmatrix}
    2 - \lambda & 1 \\
    1 & -(1 + \lambda)
  \end{bmatrix}.
```

% Some of the matrix arithmetic applied in the previous is likely new to you. Notice, however, that the manipulations we have performed mirror the ones we learned for vectors. That is to say, we can multiply a matrix by constant by multiplying said constant by each entry found in the matrix, and we add/subtract one matrix to/from another of the same size by adding/subtracting corresponding entries.

% With those basics out of the way, 

We now look to solve {math}`\det (A-\lambda I) = 0` for the unknown {math}`\lambda`. This is equivalent to solving
```{math}
  -(2-\lambda)(1+\lambda) - 1 = 0
  \quad\leftrightarrow\quad
  \lambda^2 - \lambda - 3 = 0 .
```
Applying the quadratic formula we find that
```{math}
  \lambda_1
  =
  \frac{1 + \sqrt{13}}{2}
  \quad
  \text{and}
  \quad
  \lambda_2
  =
  \frac{1 - \sqrt{13}}{2}
```
are the eigenvalues of {math}`A`.
:::

Once the eigenvalues have been identified, we find their corresponding eigenvectors by substituting a known value of {math}`\lambda` into {math}`(A - \lambda I) \vec{v} = \vec{0}` and then solving the resulting system of equations for the elements of {math}`\vec{v}`. In general, the solution to the system of equations yields an infinite number of solutions. Thus, an eigenvalue is associated with a *family* of eigenvectors whose members all point in the same direction. 

:::{prf:example} 
:label: eg:eigen2
Find the eigenvectors of the matrix {math}`A = \begin{bmatrix}2 & 1 \\ 1 & -1\end{bmatrix}`. 
:::

:::{solution .dropdown} eg:eigen2
After substituting the known eigenvalue {math}`\lambda_1 = \frac{1+\sqrt{13}}{2}` into the equation {math}`(A- \lambda I) \vec{v} = \vec{0}` we get
```{math}
  \begin{bmatrix}
    2 - \frac{1+\sqrt{13}}{2} & 1 \\
    1 & -1 - \frac{1+\sqrt{13}}{2}
  \end{bmatrix}
  \begin{bmatrix}
    v_1 \\ v_2
  \end{bmatrix}
  =
  \begin{bmatrix}
    0 \\ 0
  \end{bmatrix}
```
or equivalently
```{math}
  \begin{array}{lcl}
    (2 - \frac{1+\sqrt{13}}{2})  v_1 + v_2 &=& 0\\
    v_1 - (1+\frac{1+\sqrt{13}}{2}) v_2 &=& 0
  \end{array}
```
From the first of these equations we can conclude that
\begin{equation} \label{eq:key}
  v_2 = - \left(2 - \frac{1+\sqrt{13}}{2}\right) v_1
\end{equation}
and putting this into the second of the equations gets us
```{math}
\begin{aligned}
  v_1 + \left(1+\frac{1+\sqrt{13}}{2}\right)
  \left(2 - \frac{1+\sqrt{13}}{2}\right) v_1 = 0
  \\
  \leftrightarrow
  -v_1  \left(
    \underbrace{
      -\left(2 - \frac{1+\sqrt{13}}{2}\right)
    \left(1+\frac{1+\sqrt{13}}{2}\right) - 1}_{=\det (A - \lambda_1  I)}
  \right) = 0.
\end{aligned}
```

As we saw in the previous example {math}`\det(A-\lambda_1 I)=0` and so the second of our pair of equations boils down to the trivial statement {math}`0=0`. Because {math}`0=0` for any value {math}`v_1`, we are free to choose whatever value of {math}`v_1` we find most convenient. Setting {math}`v_1 = s` and using \eqref{eq:key}, we find
```{math}
  \vec{v}
  =
  s 
  \begin{bmatrix}
    1 \\
    - ( 2 - \frac{1+ \sqrt{13}}{2} )
  \end{bmatrix}
  =
  s 
  \begin{bmatrix}
    1 \\
    -  \frac{3 - \sqrt{13}}{2}
  \end{bmatrix}
```
describes a family of eigenvectors associated with the eigenvalue {math}`\lambda_1 = \frac{1+\sqrt{13}}{2}`.

The same procedure can be applied to show that 
```{math}
  \vec{v}=
  c 
  \begin{bmatrix}
    1
    \\
    -  \frac{3 + \sqrt{13}}{2}
  \end{bmatrix}
```
for any constant {math}`c`, is the family of eigenvectors associated with {math}`\lambda_2 = \frac{1 - \sqrt{13}}{2}`.
:::


## Complex eigenvalues and eigenvectors

Eigenvalues and eigenvectors can take complex values. A complex number {math}`z` is written as {math}`a + i b`, where {math}`a` and {math}`b` are real numbers, and {math}`i` satisfies {math}`i^2 = -1`. We often call {math}`a` the *real part of* {math}`z`, and {math}`b` the *imaginary part of* {math}`z`. We also sometimes make reference to the *conjugate of* {math}`z`. When {math}`z= a+i b` its conjugate is {math}`\bar z = a - i b`. The absolute value of a complex number is {math}`|z| = \sqrt{a^2+b^2}` and so {math}`|z| = |\bar z|`.

We add and subtract two complex numbers by adding and subtracting their real and imaginary parts, respectively. So,
```{math}
\begin{array}{lcl}
  ( a + i b) + ( c + i d) &=& (a+c) + i (b+d) \\
  ( a + i b) - ( c + i d) &=& (a-c) + i (b-d)
\end{array}
```
We multiply two complex numbers by using familiar distributive properties:
```{math}
  (a+i b)(c+i d) 
  = a c + i a d + i b c + i^2 b d 
  = (a c - b d) + i (a d + b c)
```
where we have used {math}`i^2=-1`. We can also divide one complex number by another. To do this, we define
```{math}
  z^{-1} = \frac{1}{z} = \frac{\bar z}{|z|^2},
```
since {math}`z z^{-1} = 1`. With this in mind, {math}`w/z` can be understood as {math}`w  z^{-1}` and carried out using the rules of multiplication.

Let's now turn our attention to an example involving a matrix whose eigenvalues and eigenvectors take complex values.

:::{prf:example} 
:label: eg:complex
Find the eigenvalues and eigenvectors of {math}`A= \begin{bmatrix}1 & -1 \\ 2 & 3\end{bmatrix}`.
:::
:::{solution .dropdown} eg:complex
As always we start by solving {math}`\det (A - \lambda I)=0` for {math}`\lambda`. This equation simplifies to
```{math}
  \lambda^2 - 4  \lambda + 5 = 0.
```
From the quadratic formula we then get
```{math}
  \lambda = \frac{4 \pm \sqrt{-4}}{2} = 2 \pm i.
```
So {math}`\lambda = 2 + i` and {math}`\bar \lambda = 2 -i` are the eigenvalues of {math}`A`. 

To find the eigenvector corresponding to {math}`\lambda = 2+i` we solve
```{math}
  \begin{array}{lcl}
    ( 1-(2+i) )  v_1 - v_2  &=& 0 \\
    2 v_1 + (3 - (2+i)) v_2 &=& 0
  \end{array}
```
keeping in mind that {math}`v_1` and {math}`v_2` can also take complex values. From the first equation, we know that
```{math}
  v_2 
  = (1-(2+i))  v_1 
  = ( (1+i 0) - (2 + i) ) v_1
  =(-1-i) v_1.
``` 
Substituting this identity into the second of the pair of equations we get
```{math}
  2 v_1 + (1-i)(-1-i)  v_1 = 0
```
which simplifies to {math}`0=0` as expected. It follows that eigenvectors associated with {math}`\lambda=2+i` belong to the family
```{math}
  s 
  \begin{bmatrix}
    1 \\
    -1-i
  \end{bmatrix}
```
where {math}`s` is a constant. 

The same procedure shows that {math}`\begin{bmatrix}1 \\ -1 + i\end{bmatrix}` defines the family of eigenvectors associated with {math}`\bar \lambda = 2-i`.
:::

The previous example illustrates a helpful piece of trivia. When the entries of {math}`A` are real, any complex eigenvalues occur as conjugate pairs, {math}`\lambda` and {math}`\bar \lambda`. Furthermore, if {math}`\vec{x}+i \vec{y}` is an eigenvector associated with the eigenvalue {math}`\lambda`, then {math}`\vec{x} - i \vec{y}` is an eigenvector associated with the eigenvalue {math}`\bar\lambda`.  In this case, both {math}`\vec{x}` and {math}`\vec{y}` are vectors with real entries only.

When the eigenvalues of {math}`A` are complex, the motion suggested by the linear vector field is rotational in nature. When the real part of the conjugate pair of eigenvalues is positive, as it was in Example [](#fig:vf_rot), the vector field carries us away from the origin (Figure [](#fig:vf_rot)). When the real part of the conjugate pair of eigenvalues is negative, movement is toward the origin. 

:::{figure} ./standalones/plot-rotationVF.pdf
:label: fig:vf_rot
A depiction of the vector field {math}`\vec{F}(\vec{x}) = A \vec{x}` where {math}`A` is the matrix in Example [](#eg:complex). The vector field suggests an anticlockwise movement away from the origin. Arrows have been rescaled. 
:::

We can illustrate the points above further by considering the *antisymmetric matrix*,
```{math} 
  \begin{bmatrix}
    a & -b\\
    b & a
  \end{bmatrix}.
```
The eigenvalues of this matrix are {math}`\lambda = a\pm i b`. Assuming {math}`a` and {math}`b` are not both zero, we can re-write the matrix as
```{math}
  |\lambda |
  \begin{bmatrix}
    a/|\lambda| & -b/|\lambda|\\
    b/|\lambda| & a/|\lambda|
  \end{bmatrix}
  =
  |\lambda |
  \begin{bmatrix}
    a/\sqrt{a^2+b^2} & -b/\sqrt{a^2+b^2}\\
    b/\sqrt{a^2+b^2} & a/\sqrt{a^2+b^2}
  \end{bmatrix}.
```
If we now think of {math}`a` as the base of a right triangle, and {math}`b` as its height, then the matrix can be re-written yet again as
```{math}
  \begin{bmatrix}
    |\lambda | & 0 \\
    0 & |\lambda|
  \end{bmatrix}
  \begin{bmatrix}
    \cos \theta & -\sin \theta\\
    \sin \theta & \cos \theta
  \end{bmatrix}.
```
where {math}`\theta` is the angle adjacent to the side of the triangle of length {math}`a` and opposite to the side of length {math}`b` (Figure [](#fig:triangle)). When expressed in this new way, it becomes clear that the antisymmetric matrix is the composition of two transformations: first, rotation through {math}`\theta` radians, and second, multiplicative scaling by {math}`|\lambda|` (Figure [](#fig:comp_two)).

:::{figure} ../standalones/build/plot-triangle.pdf
:label: fig:triangle
We can identify the entries of an antisymmetric matrix with the sides of a right triangle.
:::


:::{figure} ../standalones/build/plot-antisymmetric-matrix.pdf
:label: fig:comp_two
(a) An antisymmetric matrix {math}`A` can be understood as a composition of two linear transformations: a rotation through {math}`\theta` radians, then a scaling by some factor. (b) The same interpretation can be used when visualizing the effect of {math}`A` by applying {math}`A \vec{x}` to {math}`\vec{x}` as was done in Figure [](#fig:vf_rot).
:::

## Application to models of age-structured populations

Let's now return to the model for the growth of an age-structured population presented in the previous chapter. Recall that model tracked the number of juveniles {math}`x_1(t)`, and the number of adults {math}`x_2(t)` over time, measured in years. Recall also that
```{math}
  \begin{bmatrix}
    x_1 (t+1) \\ x_2(t+1)
  \end{bmatrix}
  =
  \begin{bmatrix}
    0 & b \\ s_1 & s_2
  \end{bmatrix}
  \begin{bmatrix}
    x_1 (t) \\ x_2(t)
  \end{bmatrix}.
```
To make our discussion more concrete, we will suppose that the annual birth rate is {math}`b=6` offspring per adult, and that the survival rates of juveniles and adults are {math}`s_1=1/4` and {math}`s_2=1/2`, respectively. We will also suppose that, at time {math}`t=0`, we have {math}`x_1(0) = 2` juveniles and {math}`x_2(0) = 4` adults. So our model becomes
```{math}
  \begin{bmatrix}
    x_1 (t+1) \\ x_2(t+1)
  \end{bmatrix}
  =
  \begin{bmatrix}
    0 & 6 \\ \frac{1}{4} & \frac{1}{2}
  \end{bmatrix}
  \begin{bmatrix}
    x_1 (t) \\ x_2(t)
  \end{bmatrix},
  \quad \text{with}\quad
  \begin{bmatrix}
    x_1(0) \\ x_2(0)
  \end{bmatrix}
  =
  \begin{bmatrix}
    2 \\ 4
  \end{bmatrix}
```
and our goal, now, is to turn the recursive statement into one that expresses {math}`x_1(t)` and {math}`x_2(t)` explicitly in terms of {math}`t`. As you might guess, the explicit model will require us to find the eigenvalues and eigenvectors of the matrix above.

We now know that the eigenvalues of the matrix in our recursive model are those values of {math}`\lambda` that satisfy 
```{math}
  \det
  \begin{bmatrix}
    -\lambda & 6 \\ \frac{1}{4} & \frac{1}{2} - \lambda
  \end{bmatrix}
  =0
```
or equivalently
```{math}
  -\lambda \left( \frac{1}{2} - \lambda \right) - \frac{6}{4} = 0.
```
The left-hand side of the previous equation simplifies to
```{math}
  \lambda^2 - \frac{1}{2} \lambda - \frac{3}{2} = 
  \left(\lambda - \frac{3}{2}\right)\bigg(\lambda + 1\bigg) 
```
and so the eigenvalues of the matrix are {math}`\lambda_1 = \frac{3}{2}` and {math}`\lambda_2 = -1`. 

We can use an abbreviated method for finding the eigenvectors corresponding to each eigenvalue. Dotting the eigenvector with the first row of the matrix gives us 
```{math}
  6 v_2 = \lambda_i  v_1.
```
So, if we choose {math}`v_1 = 6`, then {math}`v_2` must be equal to {math}`\lambda_i`. This tells us that {math}`\lambda_1 = 3/2` and {math}`\lambda_2 = -1` are associated with eigenvectors
```{math}
  \vec{v}_1 = 
  \begin{bmatrix}
    6 \\ \frac{3}{2}
  \end{bmatrix}
  \quad
  \text{and}
  \quad
  \vec{v}_2 =
  \begin{bmatrix}
    6 \\ -1
  \end{bmatrix}
```
respectively.

As we saw in the last chapter, the solution we seek can be written as
```{math}
  \begin{bmatrix}
    x_1 (t) \\ x_2(t)
  \end{bmatrix}
  =
  \underbrace{
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
    \cdots
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
  }_{t\ \text{times}}
  \begin{bmatrix}
    2\\4
  \end{bmatrix}.
```
Though this technically gives us an explicit model, it is of limited utility, since we would need to carry out a lot of computations to make predictions far into the future (imagine trying to figure out the age distribution after even just 10 years). What we can do to make the solution more practicable is leverage the fact that, for eigenvectors, the complications of matrix-vector multiplication boil down to multiplication by a constant. 

To pull this off, we need to figure out how to express the initial distribution {math}`\begin{bmatrix} 2 \\ 4\end{bmatrix}` as a linear combination of the eigenvectors. So, our next move, then, is to solve
```{math}
  c_1 
  \begin{bmatrix}
    6 \\ \frac{3}{2}
  \end{bmatrix}
  +
  c_2
  \begin{bmatrix}
    6 \\ - 1
  \end{bmatrix}
  =
  \begin{bmatrix}
    2 \\ 4
  \end{bmatrix},
```
or equivalently,
```{math}
  \begin{array}{lcl}
    6 c_1 + 6 c_2 &=& 2, \\
    \frac{3}{2} c_1 -\  c_2 &=& 4.
  \end{array}
```
The second of the preceding pair of equations gives us {math}`c_2 = \frac{3}{2} c_1 - 4`. Substituting this into the first of the pair of equations gives {math}`c_1 = \frac{26}{15}`,
and so
```{math}
  \frac{26}{15}  
  \begin{bmatrix}
    6 \\ \frac{3}{2}
  \end{bmatrix}
  -
  \frac{7}{5} 
  \begin{bmatrix}
    6 \\ - 1
  \end{bmatrix}
  =
  \begin{bmatrix}
    2 \\ 4
  \end{bmatrix}.
```
Returning to the less-than-useful solution, we use our new way of writing the initial conditions to obtain
```{math}
  \begin{bmatrix}
    x_1 (t) \\ x_2(t)
  \end{bmatrix}
  =
  \underbrace{
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
    \cdots
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
  }_{t\ \text{times}}
  \left(
    \frac{26}{15}  
    \begin{bmatrix}
      6 \\ \frac{3}{2}
    \end{bmatrix}
    -
    \frac{7}{5} 
    \begin{bmatrix}
      6 \\ - 1
    \end{bmatrix}
  \right).
```
Using the fact that matrix-vector multiplication preserves linear combinations, we get
```{math}
  \begin{bmatrix}
    x_1 (t) \\ x_2(t)
  \end{bmatrix}
  =
  \underbrace{
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
    \cdots
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
  }_{t-1\ \text{times}}
  \left(
    \frac{26}{15}  
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
    \begin{bmatrix}
      6 \\ \frac{3}{2}
    \end{bmatrix}
    -
    \frac{7}{5} 
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
    \begin{bmatrix}
      6 \\ - 1
    \end{bmatrix}
  \right)
```
which becomes
```{math}
  \begin{bmatrix}
    x_1 (t) \\ x_2(t)
  \end{bmatrix}
  =
  \underbrace{
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
    \cdots
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
  }_{t-1\ \text{times}}
  \left(
    \frac{26}{15}  
    \left(\frac{3}{2}\right)  
    \begin{bmatrix}
      6 \\ \frac{3}{2}
    \end{bmatrix}
    -
    \frac{7}{5} 
    (-1) 
    \begin{bmatrix}
      6 \\ - 1
    \end{bmatrix}
  \right)
```
because {math}`\begin{bmatrix} 6 \\ 3/2\end{bmatrix}` and {math}`\begin{bmatrix} 6 \\ -1\end{bmatrix}` are eigenvectors associated with eigenvalues {math}`3/2` and {math}`-1`, respectively. Going through the same steps once again, we to obtain
```{math}
  \begin{bmatrix}
    x_1 (t) \\ x_2(t)
  \end{bmatrix}
  =
  \underbrace{
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
    \cdots
    \begin{bmatrix}
      0 & 6 \\ \frac{1}{4} & \frac{1}{2}
    \end{bmatrix}
  }_{t-2\ \text{times}}
  \left(
    \frac{26}{15}  
    \left(\frac{3}{2}\right)^2  
    \begin{bmatrix}
      6 \\ \frac{3}{2}
    \end{bmatrix}
    -
    \frac{7}{5} 
    (-1)^2 
    \begin{bmatrix}
      6 \\ - 1
    \end{bmatrix}
  \right).
```
Repeating {math}`t-2` more times leads us to
```{math}
  \begin{bmatrix}
    x_1 (t) \\ x_2(t)
  \end{bmatrix}
  =
  \left(
    \frac{26}{15}  
    \left(\frac{3}{2}\right)^t  
    \begin{bmatrix}
      6 \\ \frac{3}{2}
    \end{bmatrix}
    -
    \frac{7}{5} 
    (-1)^t 
    \begin{bmatrix}
      6 \\ - 1
    \end{bmatrix}
  \right)
```
which is a more practicable version of the explicit age-structured model.

## Perron's theorem

In the limit as {math}`t` becomes large, the predictions of the age-structured model we produced in the previous section come to be dominated by the larger of the two eigenvalues and its corresponding eigenvector. In other words, the ratio of juveniles to adults in the population is approximately {math}`6:\frac{3}{2}` (or {math}`4:1`), and the number of individuals in both age classes increases by a factor of {math}`\lambda_1 = \frac{3}{2}` every year (Table [](#tab:PF)). These findings are not coincidental; rather, they are a consequence of a well-known, and quite useful, result known as the Perron's theorem.

:::{figure} ../standalones/build/plot-perron.pdf
:label: fig:perron
Predictions arising from the age-structured model presented in the previous section. Over time, the ratio of juveniles to adults in the population converges to 4:1, and over time the numbers in each age class increase by a factor of {math}`3/2 = 1.5`. Convergence to these values is a consequence of the Perron-Frobenius theorem.
:::

Perron's theorem tells us about *positive matrices*, i.e. matrices whose entries are all strictly greater than zero. Specifically, if a  {math}`A` is positive, then we are guaranteed of the following: 

- {math}`A` has one eigenvalue that is greater than all others in absolute value, and we call this the *dominant eigenvalue*, {math}`\rho`;
- {math}`\rho` is real, positive, and is associated with one (and only one) family of eigenvectors, represented by the *dominant eigenvector*, {math}`\vec{u}`.
- we can choose {math}`\vec{u}` so that each of its entries is positive.  
- {math}`\vec{u}` and multiples thereof are the only eigenvectors of {math}`A` with elements that are all non-negative;
- as {math}`t` becomes large {math}`\underbrace{A \cdots A}_{t\ \text{times}} \vec{x}` tends to some multiple of {math}`\vec{u}`. 

Perron's theorem can be extended to include certain kinds of non-negative matrices\footnote{The extension to non-negative matrices is known as the Perron-Frobenius theorem,  in recognition of the mathematician who worked on this very important generalization.}.  A matrix is *non-negative* if each of its entries is greater than, or equal to zero. In order to apply Perron's theorem to a non-negative matrix, that matrix must also be a primitive matrix. Saying that a non-negative matrix {math}`A` is *primitive* is equivalent to saying that some composition of the form
```{math}
  \underbrace{A\cdots A}_{k \ \text{times}}
``` 
can, itself, be represented as a positive matrix. Thus, Perron's theorem applies also to non-negative matrices that are primitive.

The matrix we studied in the previous section is an example of a primitive matrix since applying the matrix twice to any vector {math}`\vec{x}`, like this
```{math}
  \begin{bmatrix}
    x_1(t+2) \\ x_2(t+2)
  \end{bmatrix}
  =
  \begin{bmatrix}
    0 & 6 \\
    1/4 & 1/2
  \end{bmatrix}
  \begin{bmatrix}
    0 & 6 \\
    1/4 & 1/2
  \end{bmatrix}
  \begin{bmatrix}
    x_1(t) \\ x_2(t)
  \end{bmatrix}.
```
is equivalent to multiplying the vector by a positive matrix, as follows 
```{math}
  \begin{bmatrix}
    x_1(t+2) \\ x_2(t+2)
  \end{bmatrix}
  =
  \begin{bmatrix}
    3/2 & 3 \\
    1/8 & 7/4
  \end{bmatrix}
  \begin{bmatrix}
    x_1(t) \\ x_2(t)
  \end{bmatrix}
```
An example of a non-negative matrix that is not primitive is {math}`A = \begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix}`. In this case, applying the matrix an even number of times is equivalent to multiplying by {math}`I`, and applying the matrix an odd number of times is equivalent to applying {math}`A` once.  

We can rule out primitivity of a matrix in those cases where the problem it models is reducible. In practice, a reducible model tracks irrelevant information. A reducible age-structured model, for example, would be one that tracked the number of deceased individuals. From a modelling perspective, deceased individuals are irrelevant because they are a demographic dead end. When a matrix models a scenario that cannot be reduced, we say that matrix is *irreducible*. 
More formally, we can say that a matrix is irreducible if the corresponding network diagram allows us to travel from any node to any other node\footnote{In discrete mathematics we would say the network is *strongly connected*.}. What's more, if we can travel from a given node to any other node in the network, then we can be sure that the matrix partner of the network is irreducible. 

We should also note that while we it is true that all primitive matrices are irreducible, it is not true that all irreducible matrices are primitive. This means that irreducibility, alone, is not enough to allow us to conclude anything about the primitivity of a given non-negative matrix. From a practical perspective, then, those who are looking to apply Perron's theorem to non-negative matrix models are well advised to verify primitivity first.  


:::{figure} ../standalones/plot-age-structure-primitive.pdf
:label: fig:net
An example of an age-structured population whose dynamics are captured using a primitive matrix. 
:::

From a biological perspective, a primitive matrix would describe the dynamics of an age-structured population in which every individual, at any given time, is expected to still be able to produce descendants who will, eventually, spread across all age categories. For primitivity an individual's history is irrelevant; we care only about their future. An example of a primitive scenario appears in Figure [](#fig:net). As you can see by following the arrows in that figure, it is likely that an adult this year will have both juvenile descendants (its own offspring) and adult descendants (itself) next year. And, while juveniles this year will not be able to produce juveniles next year, there is a chance that they will be adults next year, and eventually have the breadth of descendants we seek.  

Notice that if we took away the adult-adult loop in Figure [](#fig:net), then generations would no longer mix and we would not be able to achieve the kind of distribution of descendants we need for the primitivity of the matrix to hold. After thinking in this way, we might begin to suspect that there exists a connection between primitivity and the structure of networks like those shown in Figure [](#fig:net). It turns out that those suspicions are well founded. Suppose we are given a network arising from an irreducible model. Suppose further that for each node we (a) identify every path through this network that begins and ends on that node, without traversing the same set of arrows twice (b) list the number of arrows we traverse along each of the paths we identify, and (c) calculate greatest common divisor (gcd) of each number listed. If the gcd we identified is 1 for every node in the network, then the corresponding irreducible matrix is primitive. Furthermore, if an irreducible matrix is primitive, then the gcd is 1 for every node in the corresponding network. This result gives a useful tool for determining whether a matrix is primitive or not, and ultimately whether the conclusions of Perron's theorem can be applied. 


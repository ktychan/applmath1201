# Systems of Differential Equations

We already know that many biological phenomena are multidimensional. In this chapter we expand our ability to create and analyse multi-dimensional models by learning to develop and solve coupled systems of differential equations. In coupled systems of differential equations, the solution to one equation depends on the solution to another and (possibly) vice versa. As you will see, we will have to draw on our previous experience with both calculus and vectors in order to untangle the recursive statements with which we are faced.

Counter-intuitively, we will begin our discussion by exploring a non-linear system of differential equations intended to model the dynamics of a predator species and its prey.  The model, itself, was originally proposed as part of an effort to understand the oscillatory ``boom and bust'' patterns seen in certain fisheries, and it highlighted how cycles seen in natural populations can be driven by endogenous factors.

## Predator-prey dynamics

Consider two populations of species whose dynamics are coupled by the fact that one is preyed upon by the other. Let {math}`n_1(t)` and {math}`n_2(t)` denote the number of individuals in the prey and predator populations, respectively, at time {math}`t`. We will assume that both populations are cut off from migration, and we model the population dynamics using conservation laws that pay attention only to births and deaths.

In an effort to keep our model as simple as possible, we will assume the per-capita birth rate of the prey species is a constant, {math}`\alpha>0`. Thus, the total rate birth rate of the prey population is {math}`\alpha n_i(t)`. We will also assume that mortality among prey is primarily due to predation. To capture this, we model the per-capita death rate of the prey species as {math}`\beta  n_2(t)`, where {math}`\beta >0` is a constant. In this case, if there are no predators, our model predicts no death among prey. It follows that the total death rate of the prey species is {math}`\beta n_2(t) n_1(t)`, and so
\begin{subequations} \label{eq:system}
  \begin{equation} \label{eq:prey}
    \frac{dn_1(t)}{dt} = \alpha  n_1(t) - \beta  n_1(t) n_2(t)
  \end{equation}
  is the net rate of production in the prey population.

  Our model for the dynamics of the predator population will also be simple. We assume that the prey species is the main food source for the predator, and use {math}`\gamma n_1(t)`, with {math}`\gamma >0` constant, to describe the per-capita birth rate of the predator. Here, if there are no prey species present, then the birth rate of the predator is zero. We model the per-capita death rate of the predator as a constant, {math}`\delta >0`. It follows that
  \begin{equation} \label{eq:predator}
    \frac{dn_2(t)}{dt} = \gamma  n_1(t) n_2(t) - \delta  n_2(t)
  \end{equation}
\end{subequations}
is the net rate of production in the predator population.

The equations \eqref{eq:prey} and \eqref{eq:predator} form a coupled system because the solution to one depends on the solution to the other. We can express this coupled system simply as {math}`\vec{n}^{ \prime}(t) = \vec{F}(\vec{n}(t))`, where 
```{math}
  \vec{F}(\vec{n}(t))
  =
  \begin{bmatrix}
    \left( \alpha  - \beta  n_2(t)\right) n_1(t) \\
    \left( \gamma  n_1(t) - \delta\right) n_2(t)
  \end{bmatrix}
```
is a non-linear vector field. Recognizing that we can think of the system of differential equations as a vector field is helpful because it can give us hints about the solutions. 

Let's think about sketching the vector field to get a better sense of what solutions to the system \eqref{eq:system} might look like. We will sketch the vector field by applying {math}`\vec{F}(\vec{n})` to the point corresponding to {math}`\vec{n}` in the positive quadrant of {math}`n_1,n_2`-space. To help us out, we will make reference to two lines: the horizontal line {math}`n_2 = \frac{\alpha}{\beta}`, the vertical line {math}`n_1 = \frac{\delta}{\gamma}`. 

When {math}`\vec{F}` is applied to points above the aforementioned horizontal line, its first element, namely {math}`\frac{dn_1}{dt}`, is negative. This is due to the fact that {math}`n_2 > \frac{\beta}{\alpha}`. On the other hand, when {math}`\vec{F}` is applied to points below the aforementioned horizontal line, its first element is positive owing to the fact that {math}`n_2 < \frac{\beta}{\alpha}`. Of course, if {math}`\vec{F}` is applied to a point directly on the horizontal line, {math}`n_2 = \frac{\beta}{\alpha}` and so its first element is zero.

Let's now turn our attention to the aforementioned vertical line. When {math}`\vec{F}` is applied to the right (respectively, the left) of said line, its second element, namely {math}`\frac{dn_2}{dt}`, is positive (respectively, negative) because {math}`n_1 > \frac{\delta}{\gamma}` (respectively, {math}`n_1 < \frac{\delta}{\gamma}`). If {math}`\vec{F}` is applied a point directly on the vertical line, the fact that {math}`n_1 = \frac{\delta}{\gamma}` means that its second component is zero.

We can put all the information presented above together to get a composite sketch of {math}`\vec{F}` in {math}`n_1,n_2`-space. As we see in Figure [](#fig:predprey1) the vector field suggests anticlockwise rotation in this two-dimensional space. Because {math}`\vec{n}^{ \prime}(t) = \vec{F}(\vec{n}(t))`, the vector field is tangent to the solutions to \eqref{eq:system}, at least when those solutions are projected into {math}`n_1,n_2`-space. Therefore, we expect the solutions to rotate in {math}`n_1,n_2`-space as well. This rotation means that, when expressed as functions of time, solutions will oscillate with numbers rising and falling repeatedly as time goes on.

:::{figure} ../standalones/build/plot-predprey1.pdf
:label: fig:predprey1
A very rough sketch of the vector field {math}`\vec{F}(\vec{n})`. Direction of arrows suggests anticlockwise rotation, but further analysis is required. The arrows lead us to predict that the solution to \eqref{eq:system}, projected into {math}`n_1,n_2`-space, will also rotate in an anticlockwise manner, possibly as shown by the purple curve.
:::

As Figure [](#fig:predprey1) shows, when we project the solutions to system \eqref{eq:system} into {math}`n_1` and {math}`n_2` it is tempting to view one variable as a function of the other. If we take that perspective, then we might conjecture that curves, like the purple one in Figure [](#fig:predprey1), satisfy 
```{math}
  \frac{dn_2}{dn_1}
  =
  \frac{(\gamma n_1(t) - \delta )n_2(t)}{(\alpha - \beta n_2(t) ) n_1(t)}.
``` 
Note that this new differential equation has been constructed by dividing the predator equation in \eqref{eq:predator} by prey equation in \eqref{eq:prey}.

With a little algebra, the preceding equation becomes
```{math}
  \frac{\alpha - \beta n_2(t) }{n_2(t)}  \frac{dn_2}{dn_1}
  =
  \frac{\gamma n_1(t) - \delta }{n_1(t)}.
```
Next, integrating with respect to {math}`n_1` gives us
```{math}
  \int
  \frac{\alpha - \beta n_2}{n_2}  \frac{dn_2}{dn_1} dn_1
  =
  \int
  \frac{\gamma n_1 - \delta }{n_1} dn_1
```
which, after an elementary change of variable on the left, becomes
```{math}
  \int
  \frac{\alpha - \beta n_2}{n_2} dn_2
  =
  \int
  \frac{\gamma n_1 - \delta }{n_1} dn_1.
```
Completing the integration shown, and keeping in mind that {math}`n_1` and {math}`n_2` are both strictly postive, we arrive at
\begin{equation}\label{eq:relation}
  \alpha \ln n_2 - \beta n_2 = \gamma  n_1 - \delta  \ln n_1 +C
\end{equation}
where {math}`C` is a constant. We cannot solve this equation to express one variable as a function of the other. However, we can look at the equation as a relation between {math}`n_1` and {math}`n_2`. Moreover, we can represent that relation as a curve, with different values of {math}`C` defining different curves.\footnote{Like the way in which we represent {math}`x^2 + y^2 = C`, for positive {math}`C`, as a circle of radius {math}`\sqrt{C}`.} When we plot our relation between {math}`n_1` and {math}`n_2`, we see that it takes a rather odd shape, but does yield a closed curve in the plane (Figure [](#eq:fieldplot)). 

\begin{figure}
  \begin{center}
    \includegraphics[scale=0.5,trim={1in, 4.5in, 2in, 0.75in}, clip]{./standalones/plot-predPrey}
    \parbox{4.5in}{
      \caption{The dynamics of the prey population ({math}`n_1`) and the predator population ({math}`n_2`) are revealed when we plot the relation in equation \eqref{eq:relation}. Curves  were constructed assuming {math}`\alpha = 3`, {math}`\beta = \gamma = \frac{3}{2}`, and {math}`\delta = 1`. Curves correspond to different values of the constant {math}`C`, and are overlaid on the vector field associated with the system of differential equations in \eqref{eq:system}. If we think of the current state of the populations as a particle (``{math}`\bullet`''), then that particle will travel along the curve, periodically returning to its original position. The significance of points A-D is made clear in the text.  \label{eq:fieldplot} }
    }
  \end{center}
\end{figure}

Using Figure [](#eq:fieldplot) we can deduce key qualitative predictions of our predator-prey model. First, the fact that curves are closed means that the dynamics are predicted to be periodic. This means that at some time in the future the populations will simultaneously return to their current state. 

Second, the shape of each closed curve means that the oscillations we expect to see in species' population sizes will be out of phase. As an example of this, suppose the population began with a relatively moderate number of prey and a relatively small number of predators (at point A in Figure [](#eq:fieldplot)). From there, numbers of prey and predator will increase until the system reaches point B in Figure [](#eq:fieldplot). Beyond point B, numbers of prey will begin to fall, but numbers of predators will continue to increase. The size of the predator population would be greatest as the system passes through point C in Figure [](#eq:fieldplot). Between points C and D in Figure [](#eq:fieldplot) both populations decline in size, then prey begin to recover as the system passes through point D. 

\begin{figure}
  \begin{center}
    \includegraphics[scale=0.55]{./standalones/plot-time_series}
    \parbox{4.5in}
    {
      \caption{ Solution to system \eqref{eq:system} presented as functions of time. Predator and prey numbers oscillated, in agreement with Figure [](#eq:fieldplot). \label{fig:time_series}}
    }
  \end{center}
\end{figure}

If we modify numerical methods we encountered in an earlier chapter, we can generate a solution to \eqref{eq:system}, as shown in Figure [](#fig:time_series). That solution confirms the oscillatory behaviour we have just described. The solution also raises two concerns. One is that the predator population is often larger than the prey population, which runs counter to what we see in many ecosystems. Admittedly, this prediction is likely the result of poor choices for parameters {math}`\alpha`, {math}`\beta`, {math}`\gamma` and {math}`\delta` and not a limitation of the model itself. The second concern, however, is a bit more substantive and relates to the fact that, given certain initial conditions, the model predicts that population sizes drop well below {math}`1` for a reasonable period of time. This concern has been dubbed the *attofox problem*, since the model will predict that even populations with {math}`10^{-18}` individuals eventually recover. The attofox problem suggests that the predictions of our deterministic model break down and should be replaced by ones generated by model that incorporates uncertainty.   

## Linear Systems of Differential Equations
Before one can analyse models of biological phenomena based around non-linear systems of differential equations, one must first come to terms with linear ones. In this chapter, we will define a *linear system of differential equations* as a collection of equations of the form
```{math}
  \begin{array}{ccc}
    \dfrac{du_1}{dt} 
                &=&
                a_{11} u_1(t) + \cdots + a_{1n} u_n(t) 
                + 
                b_1(t) 
                \\
                &\vdots & 
                \\
                \dfrac{du_n}{dt}
                &=&
                a_{n1} u_1(t) + \cdots + a_{nn} u_n(t) 
                + b_n(t) 	
  \end{array}
```
where {math}`a_{11}, \ldots, a_{1n}, \ldots, a_{n1}, \ldots a_{nn}` are real constants, and {math}`b_1(t), \ldots, b_n(t)` are given functions of the variable {math}`t`. In matrix-vector notation, we can re-write the previous system as 
```{math}
  \frac{d\vec{u}}{dt} = A \vec{x} + \vec{b}(t)
```
where {math}`A` is the matrix whose {math}`ij`th entry is the constant {math}`a_{ij}` and {math}`\vec{b}(t)` is the vector whose {math}`i`th entry is {math}`b_i(t)`.

In this chapter, we will restrict our discussion to systems of two equations with {math}`\vec{b}(t)` independent of {math}`t`. Consequently, {math}`A` will be a {math}`2\times 2` matrix and {math}`\vec{b}` will be a vector containing two constants. Though the Exercises provided below do present you with the occasional three-dimensional system, sensible modifications of the presentation surrounding two-dimensional problems can be applied to find solutions.

Our discussion will begin by focusing on systems for which {math}`\vec{b} = \vec{0}`. In keeping with terminology introduced in Chapter 2, such systems are called *homogeneous* and stand apart from *inhomogeneous* systems where {math}`\vec{b}\neq \vec{0}`.

Consider the following homogeneous equation
```{math}
  \frac{d}{dt}
  \begin{bmatrix}
    x_1(t) \\ \vdots \\ x_n(t)
  \end{bmatrix}	 
  = 
  \begin{bmatrix}
    \lambda_1 &\cdots& 0 \\
    \vdots & \ddots & \vdots \\
    0&\cdots& \lambda_n
  \end{bmatrix}
  \begin{bmatrix}
    x_1(t) \\ \vdots \\ x_n(t)
  \end{bmatrix}	 
```
where the only non-zero entries of the matrix are found on the diagonal. This system is easy to solve because the equations are not coupled

### Homogeneous systems: distinct real eigenvalues

Consider the initial-value problem suggested by
```{math}
  \frac{d\vec{u}(t)}{dt} = A \vec{u}(t), \quad 
  \text{with}\quad \vec{u}(0) = \vec{u}_0 
```
where {math}`A` is a {math}`2\times 2` matrix of constants. For the moment, we assume that {math}`A` has two distinct real eigenvectors, {math}`\lambda_1` and {math}`\lambda_2`, associated with eigenvectors {math}`\vec{v}_1` and {math}`\vec{v}_n`, respectively. Because {math}`\lambda_1 \neq \lambda_2`, we can express the solution we are looking for as a linear combination of their eigenvectors as follows:
\begin{equation}\label{eq:lc1}
  \vec{u}(t)
  =
  c_1(t) \vec{v}_1 
  +
  c_2(t) \vec{v}_2.
\end{equation}
Substituting this linear combination into the differential equation gives us
```{math}
  \begin{array}{lcl}
    \dfrac{d c_1(t)}{dt}  \vec{v}_1
    +
    \dfrac{d c_2(t)}{dt}  \vec{v}_2
        &=& 
        c_1(t) A \vec{v}_1 
        +
        c_2(t) A \vec{v}_2
        \```{math}1ex]
        &=&
        c_1(t) \lambda_1 \vec{v}_1 
        +
        c_2(t) \lambda_2 \vec{v}_2
  \end{array}
```
where we have used the fact that {math}`A \vec{v}_i = \lambda_i  \vec{v}_i` to simplify. If we now equate the coefficients of {math}`\vec{v}_i` on either side of the equation, we obtain
```{math}
  \frac{dc_i(t)}{dt} = c_i(t) \lambda_i  
  \quad
  \text{for } i = 1, 2
```
which is easily solved to give
```{math}
  c_i(t) = c_i(0) e^{\lambda_i  t}
  \quad
  \text{for } i = 1,2.
```
After putting this expression for {math}`c_i(t)` into \eqref{eq:lc1}, we arrive at a solution to the given initial-value problem:
\begin{equation} \label{eq:lc2}
  \vec{u}(t) = c_1(0) e^{\lambda_1  t}  \vec{v}_1
  +
  c_2(0) e^{\lambda_2  t} \vec{v}_2.
\end{equation}
It can be shown ours is the only solution to the initial-value problem given, in the case where {math}`A` has distinct real eigenvalues. However, proving that is beyond the scope of this book. 

In words, equation \eqref{eq:lc2} tells us that the solution to the initial value problem is a linear combination of the *fundamental solutions*  {math}`e^{\lambda_i  t} \vec{v}_i`. Once we identify the fundamental solutions, the coefficients used to combine them -- namely {math}`c_1(0)` and {math}`c_2(0)` -- are found by using information given by the initial condition. The next example illustrates this point.

  :::{prf:example} \label{eg:DE-linear1}
    Solve the following initial-value problem:
    ```{math}
      \begin{array}{lcl}
        u_1'(t) &=& u_2(t) - 2 u_1(t) \\
        u_2'(t) &=&  u_1(t) + 2 u_2(t) 
      \end{array}
      \quad
      \text{with}
      \quad
      \begin{array}{lcl}
        u_1(0) &=& 2\sqrt{5}, \\
        u_2(0) &=& -2\sqrt{5}.
      \end{array}
    ``` 
  :::
  :::{solution .dropdown} eg:
    We can re-write the given problem as {math}`\vec{u}^{ \prime}(t) = A \vec{u}(t)`, where
    ```{math}
      A =
      \begin{bmatrix}
        -2 & 1 \\ 1 & 2
      \end{bmatrix}.
    ```
    The eigenvalues of the matrix are {math}`\lambda_1 = \sqrt{5}` and {math}`\lambda_2=-\sqrt{5}`. These are real and distinct, and so the formula we developed can be used to solve the problem.

    The eigenvector {math}`\vec{v}_1 = {1 \brack \sqrt{5}+2}` is a member of the family associated with {math}`\lambda_1=\sqrt{5}`, and the eigenvector {math}`\vec{v}_2 = {1 \brack -\sqrt{5}+2}` is a member of the family associated with {math}`\lambda_2 = -\sqrt{5}`. It follows that the fundamental solutions are
    ```{math}
      e^{\lambda_1  t}  \vec{v}_1
      =
      e^{t\sqrt{5}} 
      \begin{bmatrix}
        1 \\ \sqrt{5}+2
      \end{bmatrix}
      \quad \text{and} \quad
      e^{\lambda_2  t}  \vec{v}_2
      =
      e^{-t\sqrt{5}} 
      \begin{bmatrix}
        1 \\ -\sqrt{5}+2
      \end{bmatrix}.
    ```

    We now turn our attention to the initial conditions and solve
    ```{math}
      \begin{array}{rccrccr}
                                & c_1(0) & + & & c_2(0) &=& 2\sqrt{5} \```{math}1ex]
        (\sqrt{5}+2) &c_1(0) & + & (-\sqrt{5}+2) & c_2(0) &=&
        -2\sqrt{5}
      \end{array}
    ```
    to find
    ```{math}
      c_1(0) = \sqrt{5}-3,\quad\text{and}\quad
      c_2(0) = \sqrt{5}+3.
    ```
    Using our formula, then, we assert that
    ```{math}
      \vec{u} (t)
      =
      (\sqrt{5}-3) 
      e^{t\sqrt{5}}  
      \begin{bmatrix}
        1 \\ \sqrt{5}+2
      \end{bmatrix}
      +
      (\sqrt{5}+3) 
      e^{-t\sqrt{5}}  
      \begin{bmatrix}
        1 \\ -\sqrt{5}+2
      \end{bmatrix}
    ```
    or equivalently
    ```{math}
      \begin{array}{lcl}
        u_1(t)
                                &=&
                                (\sqrt{5}-3)  e^{t\sqrt{5}} + 
                                (\sqrt{5}+3)  e^{-t\sqrt{5}}
                                \```{math}1ex]
                                u_2(t)
                                &=&
                                (\sqrt{5}-3)(\sqrt{5}+2)  e^{t\sqrt{5}} + 
                                (\sqrt{5}+3)(-\sqrt{5}+2)  e^{-t\sqrt{5}}
      \end{array}
    ```
    is the solution to the problem.
  :::

We can plot the solutions to the previous problem as functions of {math}`t` (Figure [](#fig:timeseries1)). We can also project the solutions into {math}`u_1,u_2`-space, which better illustrates the steps we took to arrive at a solution (Figure [](#fig:eg_illustrate)). 

Recall that we began developing our answer by finding the fundamental solutions {math}`e^{\lambda_i  t} \vec{v}_i`. As Figure [](#fig:eg_illustrate) shows, these fundamental solutions trace our straight lines in the plane that are collinear with the eigenvector upon which they are based. As their name suggests, fundamental solutions satisfy the given differential equation, but do not necessarily satisfy the given initial condition. When the real eigenvalue that makes up part of a  the fundamental solution is positive, the fundamental solution, itself, flows away from the origin. By contrast, the fundamental solution flows toward the origin when the corresponding real eigenvalue is negative.


:::{figure} ../standalones/build/plot-timeseries1.pdf
:label: fig:timeseries1
The solution to the initial-value problem in Example [](#eg:DE-linear1), plotted as functions of {math}`t`.
:::


Once we found the fundamental solutions, we used them in linear combination to express the solution to the initial-value problem. In a sense, the fundamental solutions act like a skeleton on which we hang the solution we are actually focused on finding (Figure [](#fig:eg_illustrate)). 

```{code}
\begin{figure}
  \begin{center}
    \begin{tikzpicture}[scale=0.4]
      \draw[variable=\r,domain=0:2,blue]
      plot( {\r*cos(deg(-0.2318238040))}, {\r*sin(deg(-0.2318238040))} );
      \draw[variable=\r,domain=0:2,blue]
      plot( {\r*cos(deg(-0.2318238040)+180)}, {\r*sin(deg(-0.2318238040)+180)} );
        %
      \draw[<-,variable=\r,domain=2:4,blue]
      plot( {\r*cos(deg(-0.2318238040))}, {\r*sin(deg(-0.2318238040))} );
      \draw[<-,variable=\r,domain=2:4,blue]
      plot( {\r*cos(deg(-0.2318238040)+180)}, {\r*sin(deg(-0.2318238040)+180)} );
        %
      \draw[<-,variable=\r,domain=4:6,blue]
      plot( {\r*cos(deg(-0.2318238040))}, {\r*sin(deg(-0.2318238040))} );
      \draw[<-,variable=\r,domain=4:6,blue]
      plot( {\r*cos(deg(-0.2318238040)+180)}, {\r*sin(deg(-0.2318238040)+180)} );
        %
      \draw[<-,variable=\r,domain=6:8,blue]
      plot( {\r*cos(deg(-0.2318238040))}, {\r*sin(deg(-0.2318238040))} );
      \draw[<-,variable=\r,domain=6:8,blue]
      plot( {\r*cos(deg(-0.2318238040)+180)}, {\r*sin(deg(-0.2318238040)+180)} );
        %
      \draw[<-,variable=\r,domain=8:10,blue]
      plot( {\r*cos(deg(-0.2318238040))}, {\r*sin(deg(-0.2318238040))} );
      \draw[<-,variable=\r,domain=8:10,blue]
      plot( {\r*cos(deg(-0.2318238040)+180)}, {\r*sin(deg(-0.2318238040)+180)} ) node[above right] {{math}`e^{-t\sqrt{5}}\vec{v}_2`};
        %
        %
      \draw[->,variable=\r,domain=0:2,blue]
      plot( {\r*cos(deg(1.338972522))}, {\r*sin(deg(1.338972522))} );
      \draw[->,variable=\r,domain=0:2,blue]
      plot( {\r*cos(deg(1.338972522)+180)}, {\r*sin(deg(1.338972522)+180)} );
        %
        %
      \draw[->,variable=\r,domain=2:4,blue]
      plot( {\r*cos(deg(1.338972522))}, {\r*sin(deg(1.338972522))} );
      \draw[->,variable=\r,domain=2:4,blue]
      plot( {\r*cos(deg(1.338972522)+180)}, {\r*sin(deg(1.338972522)+180)} );
        %
      \draw[->,variable=\r,domain=4:6,blue]
      plot( {\r*cos(deg(1.338972522))}, {\r*sin(deg(1.338972522))} );
      \draw[->,variable=\r,domain=4:6,blue]
      plot( {\r*cos(deg(1.338972522)+180)}, {\r*sin(deg(1.338972522)+180)} );
        %
      \draw[->,variable=\r,domain=6:8,blue]
      plot( {\r*cos(deg(1.338972522))}, {\r*sin(deg(1.338972522))} );
      \draw[->,variable=\r,domain=6:8,blue]
      plot( {\r*cos(deg(1.338972522)+180)}, {\r*sin(deg(1.338972522)+180)} );
        %
      \draw[variable=\r,domain=8:10,blue]
      plot( {\r*cos(deg(1.338972522))}, {\r*sin(deg(1.338972522))} ) node[right] {{math}`e^{t\sqrt{5}}\vec{v}_1`};
      \draw[variable=\r,domain=8:10,blue]
      plot( {\r*cos(deg(1.338972522)+180)}, {\r*sin(deg(1.338972522)+180)} );
        %
        %
        %
      \draw[->,variable=\t,domain=-0.25:-0.2,samples=10]
      plot({(sqrt(5)-3)*exp(\t*sqrt(5))+(sqrt(5)+3)*exp(-\t*sqrt(5))},
      {(sqrt(5)-3)*(sqrt(5)+2)*exp(\t*sqrt(5))+(sqrt(5)+3)*(-sqrt(5)+2)*exp(-\t*sqrt(5))} );
        %
      \draw[->,variable=\t,domain=-0.2:-0.1,samples=50]
      plot({(sqrt(5)-3)*exp(\t*sqrt(5))+(sqrt(5)+3)*exp(-\t*sqrt(5))},
      {(sqrt(5)-3)*(sqrt(5)+2)*exp(\t*sqrt(5))+(sqrt(5)+3)*(-sqrt(5)+2)*exp(-\t*sqrt(5))} );
        %
      \draw[->,variable=\t,domain=-0.15:0.1,samples=50]
      plot({(sqrt(5)-3)*exp(\t*sqrt(5))+(sqrt(5)+3)*exp(-\t*sqrt(5))},
      {(sqrt(5)-3)*(sqrt(5)+2)*exp(\t*sqrt(5))+(sqrt(5)+3)*(-sqrt(5)+2)*exp(-\t*sqrt(5))} );
        %
      \draw[->,variable=\t,domain=0.1:0.2,samples=50]
      plot({(sqrt(5)-3)*exp(\t*sqrt(5))+(sqrt(5)+3)*exp(-\t*sqrt(5))},
      {(sqrt(5)-3)*(sqrt(5)+2)*exp(\t*sqrt(5))+(sqrt(5)+3)*(-sqrt(5)+2)*exp(-\t*sqrt(5))} );
        %
      \draw[->,variable=\t,domain=0.2:0.3,samples=50]
      plot({(sqrt(5)-3)*exp(\t*sqrt(5))+(sqrt(5)+3)*exp(-\t*sqrt(5))},
      {(sqrt(5)-3)*(sqrt(5)+2)*exp(\t*sqrt(5))+(sqrt(5)+3)*(-sqrt(5)+2)*exp(-\t*sqrt(5))} );
        %
      \draw[->,variable=\t,domain=0.3:0.4,samples=50]
      plot({(sqrt(5)-3)*exp(\t*sqrt(5))+(sqrt(5)+3)*exp(-\t*sqrt(5))},
      {(sqrt(5)-3)*(sqrt(5)+2)*exp(\t*sqrt(5))+(sqrt(5)+3)*(-sqrt(5)+2)*exp(-\t*sqrt(5))} );
        %
      \draw[variable=\t,domain=0.4:0.475,samples=50]
      plot({(sqrt(5)-3)*exp(\t*sqrt(5))+(sqrt(5)+3)*exp(-\t*sqrt(5))},
      {(sqrt(5)-3)*(sqrt(5)+2)*exp(\t*sqrt(5))+(sqrt(5)+3)*(-sqrt(5)+2)*exp(-\t*sqrt(5))} ) node[below] {{math}`\vec{u}(t)`};
        %
      \filldraw (4.472135954,-4.472135954) circle (0.175cm);
      \node[below right] at (4.472135954,-4.472135954) 
      {{math}`{2\sqrt{5}\brack -2\sqrt{5}}`};
        %
      \draw[-latex, gray] (-10,0)--(10,0);
      \draw[-latex, gray] (0,-10)--(0,10);
        %\draw[gray] (-12,-12)--(12,-12)--(12,12)--(-12,12)--(-12,-12);
      \draw[dotted] (-1,-4.472135954)--(4.472135954,-4.472135954)
      --(4.472135954,-1);
    \end{tikzpicture}
    \parbox{3.75in}{
      \caption{The solution to Example [](#eg:linear1) projected into the {math}`u_1,u_2`-plane. The solution {math}`\vec{u}(t)` is a linear combination of the fundamental solutions\label{fig:eg_illustrate} }
    }
  \end{center}
\end{figure}
```

### Homogeneous linear systems: complex eigenvalues

The eigenvalues of a matrix are not always real, and so it is not obvious that the formula derived in the previous section can also always be used to solve problems like {math}`\vec{u}^{ \prime}(t) = A \vec{u}(t)` with {math}`\vec{u}(0) = \vec{u}_0` when {math}`A` has complex eigenvalues. It turns out that equation \eqref{eq:lc2} still applies in this case, but some modifications are required before you might be able to use it effectively. 

When {math}`A` has only real entries, any complex eigenvalues it has occur as conjugate pairs {math}`\lambda = a+i b` and {math}`\bar \lambda = a-i b`. In this case, we can simplify equation \eqref{eq:lc2}  by applying *Euler's formula*. This formula says that
```{math}
  e^{i \theta} = \cos \theta + i  \sin \theta.
``` 
Euler's formula is crucial to understanding the steps that are described below.

Let {math}`\lambda = a+i b` be a complex eigenvalue of {math}`A`, associated with the eigenvector {math}`\vec{v} = \vec{x} + i \vec{y}`. Then, the corresponding fundamental solution is
\begin{multline*}
  e^{\lambda t}
   \vec{v}
  =
  e^{(a+i b)t}  (\vec{x}+i \vec{y})
  =
  e^{a t} (\cos (bt) + i \sin (bt) )(\vec{x}+i \vec{y})
  \```{math}1ex]
  =
  \underbrace{
    e^{a t} ( \cos (bt) \vec{x} - \sin (bt) \vec{y} )
  }_{\text{real part}}
  +
  i 
  \underbrace{
    e^{a t} ( \sin (bt) \vec{x} + \cos (bt) \vec{y} ).
  }_{\text{imaginary part}}
\end{multline*}
As we might expect, the other fundamental solution would involve {math}`\bar \lambda = a - i b` and its eigenvector {math}`\vec{w} = \vec{x} - i \vec{y}`. With that in mind, the second fundamental solution could be expressed as
\begin{multline*}
  e^{\bar \lambda t}
   \vec{w}
  =
  e^{(a-i b)t}  (\vec{x}-i \vec{y})
  =
  e^{a t} (\cos (-bt) + i \sin (-bt) )(\vec{x}-i \vec{y})
  \```{math}1ex]
  =
  e^{a t} (\cos (bt) - i \sin (bt) )(\vec{x}-i \vec{y})
  \```{math}1ex]
  =
  \underbrace{
    e^{a t} ( \cos (bt) \vec{x} - \sin (bt) \vec{y} )
  }_{\text{real part}}
  -
  i 
  \underbrace{
    e^{a t} ( \sin (bt) \vec{x} + \cos (bt) \vec{y} ).
  }_{\text{imaginary part}}
\end{multline*}
where we have used the fact that cosine is an even function and sine is an odd function to simplify. Following equation \eqref{eq:lc2}, we then express the solution to the initial-value problem as
\begin{multline} \label{eq:final_eq}
  \vec{u}(t)
  =
  e^{a t}
  (c_1(0) + c_2(0))
  \left(
    \cos(bt) \vec{x} - \sin(bt) \vec{y}
  \right)
  \\+
  i e^{at} (c_1(0) - c_2(0)) 
  \left(
    \sin(bt) \vec{x} + \cos(bt) \vec{y}
  \right).
\end{multline}
In this case, we allow {math}`c_1(0)` and {math}`c_2(0)` to be complex numbers. Given that {math}`\vec{u}(t)` is a vector of real numbers, it must be the case that {math}`c_1(0)` and {math}`c_2(0)` in equation \eqref{eq:final_eq} are complex conjugates. With this in mind {math}`c_1(0) + c_2(0) = k_1(0)` and {math}`i ( c_1(0) - c_2(0)) = k_2(0)` where {math}`k_1(0)` and {math}`k_2(0)` are real numbers. It follows that the solution to the initial-value problem can be expressed as 
```{math}
  \vec{u}(t)
  =
  e^{a t} 
  k_1(0)
  \left(
    \cos(bt) \vec{x} - \sin(bt) \vec{y}
  \right)
  +
  e^{at} k_2(0) 
  \left(
    \sin(bt) \vec{x} + \cos(bt) \vec{y}
  \right).
```
where {math}`k_1(0)` and {math}`k_2(0)` are found using information provided by the initial condition {math}`\vec{u}(0) = \vec{u}_0`. The next example shows our modified version of \eqref{eq:lc2} at work.

  :::{prf:example} \label{eg:complex1}
    Solve the following initial-value problem:
    ```{math}
      \begin{bmatrix}
        u_1'(t) \\ u_2'(t)
      \end{bmatrix}
      =
      \begin{bmatrix}
        1 & -3 \\
        2 & 3
      \end{bmatrix}
      \begin{bmatrix}
        u_1(t) \\ u_2(t)
      \end{bmatrix}
      \quad \text{with}\quad
      \begin{bmatrix}
        u_1(0) \\ u_2(0)
      \end{bmatrix}
      =
      \begin{bmatrix}
        3 \\ 0
      \end{bmatrix}.
    ```
  :::
  :::{solution .dropdown} eg:
    The eigenvalue-eigenvectors pairs for the matrix include
    ```{math}
      \lambda = 2 + i \sqrt{5}, \quad
      \vec{v} 
      =
      \begin{bmatrix}
        3 \\ -1
      \end{bmatrix}
      +
      i 
      \begin{bmatrix}
        0\\
        -\sqrt{5}
      \end{bmatrix}
    ```
    and
    ```{math}
      \bar
      \lambda = 2 - i \sqrt{5}, \quad
      \vec{w}
      =
      \begin{bmatrix}
        3 \\ -1
      \end{bmatrix}
      - i
      \begin{bmatrix}
        0 \\ -\sqrt{5}
      \end{bmatrix}
    ```
    Applying the formula we derived, we obtain
    \begin{multline*}
      \begin{bmatrix}
        u_1(t) 
        \\
        u_2(t)
      \end{bmatrix}		=
      e^{2 t} 
      k_1(0)
      \left( 
        \cos (\sqrt{5} t) 
        \begin{bmatrix}
          3 \\ -1
        \end{bmatrix}
        -
        \sin (\sqrt{5} t) 
        \begin{bmatrix}
          0 \\ -\sqrt{5}
        \end{bmatrix}
      \right)
      \```{math}1ex]
      +
      e^{2 t} 
      k_2(0)
      \left( 
        \sin (\sqrt{5} t) 
        \begin{bmatrix}
          3 \\ -1
        \end{bmatrix}
        +
        \cos (\sqrt{5} t) 
        \begin{bmatrix}
          0 \\ -\sqrt{5}
        \end{bmatrix}
      \right)
    \end{multline*}
    which simplifies to
    \begin{multline*}
      \begin{bmatrix}
        u_1(t) \\ u_2(t)
      \end{bmatrix}
      =
      k_1(0) 
      e^{2t}  
      \begin{bmatrix}
        3  \cos (\sqrt{5}t)
        \\
        - \cos(\sqrt{5}t) + \sqrt{5}\sin(\sqrt{5}t)
      \end{bmatrix}
      \```{math}1ex]+
      k_2(0) 
      e^{2t} 
      \begin{bmatrix}
        3  \sin(\sqrt{5}t) \\
        -\sin(\sqrt{5}t) - \sqrt{5}  \cos(\sqrt{5}t)
      \end{bmatrix}.
    \end{multline*}
    Using the given initial condition, we see that the constants {math}`k_1(0)` and {math}`k_2(0)` must satisfy
    ```{math}
      \begin{array}{rcl}
        3  k_1(0) &=& 3 \\
        -k_1(0) - \sqrt{5} k_2(0) &=& 0
      \end{array}
    ```  
    and so {math}`k_1(0) = 1` and {math}`k_2(0) = -\frac{1}{\sqrt{5}}`. The solution to the given problem, therefore, is
    ```{math}
      \begin{array}{lcl}
        u_1(t)
                                &=&
                                e^{2 t} \left(3 \cos(\sqrt{5} t) - \frac{3}{\sqrt{5}} \sin (\sqrt{5} t)\right) \\
        u_2(t) &=&
        e^{2 t} 
        \frac{6}{\sqrt{5}}\sin(\sqrt{5}t)
      \end{array}
    ```
    after some simplification.
  :::

The solution to the previous example, plotted as a curve in the {math}`u_1,u_2`-plane, shows the rotation we have come to associate with complex eigenvalues (Figure [](#fig:complex1)). Because the real part of the eigenvalues in the example is positive, the rotational movement carries us away from the origin. Movement carries us toward the origin in those cases where the real part of the eigenvalues is negative.

```{code}
:label: 
\begin{figure}
  \begin{center}
    \begin{tikzpicture}[scale=0.35]
      \draw[-latex, gray] (-15,0)--(15,0);
      \draw[-latex, gray] (0,-2.5)--(0,15);
      \node[below] at (-13,13) {{math}`\vec{u}(t)`};
      \filldraw (3,0) circle (0.2cm);
      \node[below right] at (3,0) {{math}`{3\brack 0}`};
      \draw[variable=\t,domain=-1.5:0.2,samples=100,->]
      plot( {exp(2*\t)*( 3*cos(deg(sqrt(5)*\t)) - 3*sin(deg(sqrt(5)*\t))/sqrt(5) )},
      {exp(2*\t)*6*sin(deg(sqrt(5)*\t))/sqrt(5)} );
      \draw[variable=\t,domain=0.2:0.5,samples=100,->]
      plot( {exp(2*\t)*( 3*cos(deg(sqrt(5)*\t)) - 3*sin(deg(sqrt(5)*\t))/sqrt(5) )},
      {exp(2*\t)*6*sin(deg(sqrt(5)*\t))/sqrt(5)} );
      \draw[variable=\t,domain=0.5:0.71,samples=100,->]
      plot( {exp(2*\t)*( 3*cos(deg(sqrt(5)*\t)) - 3*sin(deg(sqrt(5)*\t))/sqrt(5) )},
      {exp(2*\t)*6*sin(deg(sqrt(5)*\t))/sqrt(5)} );
      \draw[variable=\t,domain=0.71:0.875,samples=100,->]
      plot( {exp(2*\t)*( 3*cos(deg(sqrt(5)*\t)) - 3*sin(deg(sqrt(5)*\t))/sqrt(5) )},
      {exp(2*\t)*6*sin(deg(sqrt(5)*\t))/sqrt(5)} );
    \end{tikzpicture}
    \parbox{4.5in}{
      \caption{The solution to the initial-value problem in Example [](#eg:complex1) projected into the {math}`u_1,u_2`-plane. The complex eigenvalues associated with the matrix in that example give rise to the rotation that we see in this plot (notice that the solution passes through all four quadrants of the plane). The fact that the real part of the complex eigenvalues is positive, means that the solution flows away from the origin as indicated by the arrows.\label{fig:complex1}}
    }
  \end{center}
\end{figure}
```


### Homogenous linear systems: repeated real eigenvalue

The formula given in equation \eqref{eq:lc2} was built on the assumption that {math}`A` had distinct eigenvalues. In some cases, though, the expression {math}`\det(A-\lambda I)` has a double root and the assumption is violated. This raises the important question, what do we do in this case?

If {math}`A = \begin{bmatrix}a & 0 \\ 0 & a\end{bmatrix}` happens to be a diagonal matrix, its only eigenvalue is {math}`\lambda =a`. In this case, though, the system of differential equations could simply be expressed as
```{math}
  \begin{array}{lcl}
    u_1'(t) &=& a u_1(t) \\
    u_2'(t) &=& a u_2(t)
  \end{array}
```
This system of differential equations is *uncoupled*, meaning that its constituents can be solved independently. We saw how to do that in Chapter 2, and so this particular instance of the problem can be set aside. Focus can instead be placed on the case of real concern: that in which {math}`A` is *not* a diagonal matrix. 

The difficulty posed by a matrix that has a repeated eigenvalue but is not diagonal has to do with the eigenvalue being associated with only one family of eigenvectors. Ultimately, this means we cannot guarantee that our solution can be expressed as a linear combination of eigenvectors. Recall that expressing {math}`\vec{u}(t)` as a linear combination of the eigenvectors of {math}`A` was the first, key step in developing the formula in \eqref{eq:lc2}.

Though our original strategy does not work in this case, a related one might. We could, for example, express the solution to the system of differential equations as a linear combination of the one eigenvector of {math}`A` (call it {math}`\vec{v}`), and a second vector that is decidedly *not* an eigenvector of {math}`A` (call it {math}`\vec{w}`). 

In order for this new strategy to work the vector {math}`\vec{w}`  must point in a direction that is altogether different from the direction given by any multiple of the eigenvector {math}`\vec{v}`. A clever way to find such a vector {math}`\vec{w}` is to require that it satisfy 
\begin{equation} \label{eq:obs}
  A \vec{w} = \lambda  \vec{w} + \vec{v}.
\end{equation} 
Notice that {math}`\vec{w} = k \vec{v}` can never be a solution to equation \eqref{eq:obs} since the eigenvector {math}`\vec{v}` is never equal to the zero vector.

We proceed, then, by writing the solution to the initial-value problem as a linear combination of {math}`\vec{v}` and {math}`\vec{w}` as follows:
```{math}
  \vec{u}(t) = c_1(t)  \vec{v} + c_2(t) \vec{w}.
```
Substituting this into the differential equation {math}`u'(t) = A u(t)` gives us
```{math}
  \begin{array}{lcl}
    \dfrac{dc_1}{dt} \vec{v}
    +
    \dfrac{dc_2}{dt} \vec{w}
        &=&
        c_1(t)  A \vec{v} + c_2(t) A \vec{w}
        \```{math}1ex]
        &=&
        c_1(t)  \lambda \vec{v}
        +
        c_2(t)  (\lambda \vec{w} + \vec{v})
        \```{math}1ex]
        &=&
        (\lambda c_1(t) + c_2(t) ) \vec{v}
        +
        \lambda c_2(t)  \vec{w} 
  \end{array}
```
Matching the coefficients of {math}`\vec{v}` and {math}`\vec{w}` respectively gives us
```{math}
  \begin{array}{lcl}
    \dfrac{dc_1}{dt}
                &=&
                \lambda c_1(t) + c_2(t) \```{math}2ex]
                \dfrac{dc_2}{dt}
                &=&
                \lambda c_2(t)
  \end{array}
```
We can solve the second of these equations to get {math}`c_2(t) = c_2(0)  e^{\lambda t}`. This leaves us with 
```{math}
  \dfrac{dc_1}{dt} = \lambda c_1(t) + c_2(0) e^{\lambda t}
```
which is a linear differential equation we can solve to obtain
```{math}
  c_1(t)  = c_1(0) e^{\lambda t} + c_2(0)  t e^{\lambda t}.
```
It follows that 
\begin{equation}\label{eq:repeat}
  \vec{u}(t)
  =
  \left(
    c_1(0) e^{\lambda t} + c_2(0)  t e^{\lambda t}
  \right) \vec{v}
  +
  c_2(0)  e^{\lambda t}  \vec{w}
\end{equation}
where {math}`c_1(0)` and {math}`c_2(0)` can be determined using the information provided by the initial condition.

  :::{prf:example} \label{eg:repeat}
    Solve the initial-value problem,
    ```{math}
      \begin{bmatrix}
        u_1'(t) \\ u_2'(t)
      \end{bmatrix}
      =
      \begin{bmatrix}
        -5 & 9 \\
        -1 & 1
      \end{bmatrix}
      \begin{bmatrix}
        u_1(t) \\ u_2(t)
      \end{bmatrix}
      \quad \text{with}
      \quad
      \begin{bmatrix}
        u_1(0) \\ u_2(0)
      \end{bmatrix}
      =
      \begin{bmatrix}
        5 \\ -5
      \end{bmatrix}
    ```
    \vspace{0.1cm}
  :::
  :::{solution .dropdown} eg:
    Given the matrix {math}`A = \begin{bmatrix} -5 & 9 \\ -1 & 1\end{bmatrix}` we find that
    ```{math}
      \det (A - \lambda I) = (\lambda + 2)^2
    ```
    which has a double root at {math}`\lambda = -2`. This eigenvalue is associated with one eigenvector {math}`\vec{v} = {3\brack 1}`.

    We find {math}`\vec{w}` as the solution to {math}`A \vec{w} = \lambda  \vec{w} + \vec{v}` or 
    ```{math}
      \begin{array}{rcrcl}
        - 5  w_1 &+& 9  w_2 &=& -2  w_1 + 3 \\
        - w_1 &+& w_2 &=& -2 w_2 + 1
      \end{array}
    ``` 
    which can be re-arranged to obtain
    ```{math}
      \begin{array}{rcrcl}
        -3 w_1 &+& 9 w_2 &=& 3 \\
        - w_1 &+& 3 w_2 &=& 1
      \end{array}
    ```
    Notice that the first of the previous pair of equations is simply three times the second. Just like with eigenvectors, then, we can exercise some choice when solving for {math}`\vec{w}`. If we choose to set {math}`w_2=1`, the {math}`w_1=2` and so we get {math}`\vec{w}={2\brack 1}`. 

    Using equation \eqref{eq:repeat} we get
    ```{math}
      \begin{array}{lcl}
        u_1(t) 
        &=& 
        3 (c_1(0)  e^{-2 t} + c_2(0) t e^{-2 t}) 
        +
        2 c_2(0) e^{-2 t}
        \\
        u_2(t)
        &=&
        c_1(0)  e^{-2 t} + c_2(0) t e^{-2 t} 
        +
        c_2(0) e^{-2 t}
      \end{array}
    ```
    where {math}`c_1(0)` and {math}`c_2(0)` satisfy
    ```{math}
      \begin{array}{rcrcl}
        3 c_1(0) &+& 2 c_2(0) &=& 5 \\
        c_1(0) &+& c_2(0) &=& -5
      \end{array}
    ```
    in order to capture the initial condition provided. It follows that {math}`c_1(0) = 15` and {math}`c_2(0) = -20` and so
    ```{math}
      \begin{array}{lcl}
        u_1(t) 
        &=& 
        5  e^{-2 t} - 60 t e^{-2 t}
        \\
        u_2(t)
        &=&
        -5 e^{-2 t} -20 t e^{-2 t} 
      \end{array}
    ```
    is the solution to the initial-value problem.
  :::
The solution to the initial-value problem in the previous example is presented in Figure [](#fig:eg_repeat). As you can see, in this example, the solution tends to run parallel to the eigenvector {math}`\vec{v} = {3\brack 1}` in the limit as {math}`t\to \pm \infty`.

```{code}
\begin{figure}
  \begin{center}
    \begin{tikzpicture}[scale=0.4]
      \draw[-latex, gray] (-10,0)--(10,0);
      \draw[-latex, gray] (0,-10)--(0,10);
                        % eigenvector
      \node[above, blue] at (9,3) {{math}`e^{-2 t} \vec{v}`};
      \draw[->, blue] (9,3) -- (7.5,2.5);
      \draw[->, blue] (7.5,2.5) -- (6,2);
      \draw[->, blue] (6,2) -- (4.5,1.5);
      \draw[->, blue] (4.5,1.5) -- (3,1);
      \draw[->, blue] (3,1) -- (1.5,0.5);
      \draw[, blue] (1.5,0.5) -- (-1.5,-0.5);
      \draw[->, blue] (-9,-3) -- (-7.5,-2.5);
      \draw[->, blue] (-7.5,-2.5) -- (-6,-2);
      \draw[->, blue] (-6,-2) -- (-4.5,-1.5);
      \draw[->, blue] (-4.5,-1.5) -- (-3,-1);
      \draw[->, blue] (-3,-1) -- (-1.5,-0.5);
                        %
      \node[above right] at (8,-4.5) {{math}`\vec{u}(t)`};
      \filldraw[black] (5,-5) circle (4pt) node[above] {{math}`{5\brack -5}`};
                        % ivp solution
      \draw[samples=25, domain=-0.05:0.05, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=0.05:0.15, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=0.15:0.25, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=0.25:0.35, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=0.35:0.55, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=0.55:0.75, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=0.75:0.95, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=0.95:1.15, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=1.15:1.35, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
      \draw[samples=25, domain=1.35:3, variable=\t,->]
      plot( {5*exp(-2*\t)-60*\t*exp(-2*\t)},
      {-5*exp(-2*\t)-20*\t*exp(-2*\t)});
    \end{tikzpicture}
    \parbox{3.75in}{
    \caption{The solution to Example [](#eg:repeat) projected into the {math}`u_1,u_2`-plane. As the solution {math}`\vec{u}(t)` approaches the origin it becomes tangent to the eigenvector of the matrix in that example. In the limit as {math}`t\to -\infty` the solution {math}`\vec{u}(t)` is approximately parallel to the eigenvector of the matrix as suggested by the plot. \label{fig:eg_repeat} }}
  \end{center}
\end{figure}
```

### Inhomogeneous systems

We can use what we already know about differential equations to solve linear inhomogeneous systems of the form
\begin{equation}\label{eq:inhomog}
  \vec{u}^{ \prime}(t) = A \vec{u}(t) + \vec{b}.
\end{equation}
Suppose, first, that we can find an equilibrium solution to the previous equation, {math}`\vec{u}^{ *}`. That is to say, assume we can find a {math}`\vec{u}^{ *}` such that {math}`A \vec{u}^{ *} + \vec{b}=\vec{0}`. In this case, solving the previous system is quite straitforward. We define {math}`\vec{x}(t) = \vec{u}(t) - \vec{u}^{ *}` and find
```{math}
  \vec{x}^{ \prime} 
  = \vec{u}^{ \prime}(t) 
  = A \vec{u}(t) + \vec{b} 
  = A \vec{u}(t) - \vec{0} + \vec{b} 
  = A \vec{u}(t) - (A \vec{u}^{ *} + \vec{b}) + \vec{b} 
  = A \vec{x}(t).
```
We can solve the resulting homogeneous system to find {math}`\vec{x}(t)` which then gives {math}`\vec{u}(t) = \vec{x}(t) + \vec{u}^{ *}` as the solution to the original problem.

  :::{prf:example}
    A drug is administered intravenously at a constant rate of {math}`a = 0.6` mg min{math}`^{-1}`. The drug moves from the bloodstream to the target tissue at rate {math}`k_{1} = 0.007`, from the target tissue into the bloodstream at rate {math}`k_{-1} = 0.003`, and leaves the bloodstream at rate {math}`k_e = 0.002`, where all rates are measured as min{math}`^{-1}`. Devise a model for the relationship between the amount of drug (in mg) in the bloodstream and time, and another for the amount of drug (in mg) in the target tissue and time. Assume that the drug is not broken down in either the bloodstream or the target tissue, and assume that no drug was initially present in the system as a whole.
  :::
  :::{solution .dropdown} eg:
    Let {math}`u_1(t)` be the amount of drug in the bloodstream at time {math}`t`, and let {math}`u_2(t)` be the amount of drug in the target tissue at time {math}`t`. A picture helps us generalize the application of conservation laws to this multi-system scenario.
    ```{code}
    \begin{center}
      \begin{tikzpicture}
        \filldraw[blue!35] (0,0)--(3,0)--(3,2)--(0,2)--cycle;
        \filldraw[blue!35] (5,0)--(8,0)--(8,2)--(5,2)--cycle;
        \draw[ultra thick] (0,0)--(3,0)--(3,2)--(0,2)--cycle;
        \draw[ultra thick] (5,0)--(8,0)--(8,2)--(5,2)--cycle;
        \draw[->, ultra thick] (-1,1) -- (0,1);
        \node[above] at (-0.5,1) {{math}`a`};
        \draw[white] (8.1,1)--(9,1);
        \draw[->, ultra thick] (3,1.5)--(5,1.5);
        \node[above] at (4,1.5) {{math}`k_1 u_1(t)`};
        \draw[->, ultra thick] (5,0.5)--(3,0.5);
        \node[below] at (4,0.5) {{math}`k_{-1} u_2(t)`};
        \draw[->, ultra thick] (1.5,0) -- (1.5,-1);
        \node[right] at (1.5,-0.5) {{math}`k_e  u_1(t)`};
        \node[white] at (1.5, 1.25) {bloodstream};
        \node[white] at (1.5, 0.75) {{math}`u_1(t)`};
        \node[white] at (6.5, 1.25) {target tissue};
        \node[white] at (6.5, 0.75) {{math}`u_2(t)`};
      \end{tikzpicture}
    \end{center} 
    ```

    From the picture {math}`u_1(t)` and {math}`u_2(t)` satisfy
    ```{math}
      \begin{array}{lcrcc}
        u_1'(t) &=& - 0.009  u_1(t) + 0.003 u_2(t) &+& 0.6\\
        u_2'(t) &=& 0.007  u_1(t) - 0.003 u_2(t) 
      \end{array}
    ```
    We identify an equilibrium by first setting {math}`u_1'(t) = u_2'(t) = 0`, {math}`u_1(t) = u_1^*`, and {math}`u_2(t) =u_2^*` to obtain
    ```{math}
      \begin{array}{lcrcc}
        0 &=& - 0.009  u_1^* + 0.003 u_2^* &+& 0.6\\
        0 &=& 0.007  u_1^* - 0.003 u_2^* 
      \end{array}
    ```
    Solving the system we find the equilibrium to be {math}`\vec{u}^{ *} = {300\brack 700}`. 

    We now define {math}`\vec{x}(t)` as {math}`{u_1(t)\brack u_2(t)} -{300\brack 700}`. Then we look to solve
    ```{math}
      \vec{x}'(t) =
      \begin{bmatrix}
        -0.009 & 0.003 \\
        0.007 & -0.003
      \end{bmatrix}
      \vec{x}(t)
      \quad
      \text{with}
      \quad
      \vec{x}(0) =
      \begin{bmatrix}
        -300 \\ -700
      \end{bmatrix}.
    ```
    The matrix in the preceding homogeneous equation has two distinct real eigenvalues. In fact, the eigenvalue-eigenvector pairs are
    ```{math} 
      \lambda_1 =
      \frac{-6 + \sqrt{30}}{1000}, \quad \vec{v}_1 = { 3 \brack 3 +\sqrt{30}}
    ```
    and
    ```{math} 
      \lambda_2 =
      \frac{-6 - \sqrt{30}}{1000}, \quad \vec{v}_2 = { 3 \brack 3 -\sqrt{30}}
    ```
    Using the initial condition we find that
    ```{math}
      \vec{x}(t)
      =
      -\left(\frac{20\sqrt{30}}{3} + 50\right)  e^{\lambda_1 t} { 3 \brack 3 +\sqrt{30}}
      +
      \left(\frac{20\sqrt{30}}{3} - 50\right) e^{\lambda_2 t} { 3 \brack 3 -\sqrt{30}}
    ```
    and so
    \begin{multline*}
      {u_1(t) \brack u_2(t)} = 
      {300\brack 700} 
      -\left(\frac{20\sqrt{30}}{3} + 50\right)  e^{\lambda_1 t} { 3 \brack 3 +\sqrt{30}}
      \```{math}1ex]+
      \left(\frac{20\sqrt{30}}{3} - 50\right) e^{\lambda_2 t} { 3 \brack 3 -\sqrt{30}}.
    \end{multline*}
    Because {math}`\lambda_1, \lambda_2 < 0` we can also see that the equilibrium solution we identified is asymptotically stable.
  :::

As we said, the strategy for solving \eqref{eq:inhomog} by re-defining variables relative to an equilibrium is quite straightforward. However, we can only be sure that an equilbrium {math}`\vec{u}^{ *}` exists when zero is *not* an eigenvalue of {math}`A`. 

When zero is an eigenvalue of {math}`A`, an equilibrium will only exist when {math}`\vec{b}` is an eigenvector associated with the other (non-zero) eigenvalue {math}`\lambda`. In this case, {math}`\vec{u}^{ *} = -\vec{b}/\lambda` would be the equilibrium and we can use the strategy for finding a solution outlined above.

When zero is an eigenvalue of {math}`A` and {math}`\vec{b}` is not an eigenvector associated with the other eigenvalue, then a different strategy for finding a solution is required because no equilibrium exists. The path forward in this case is a bit complicated, but is not beyond our grasp. To understand the procedure, we first define the *transpose of {math}`A`*, denoted {math}`A^T`, as the matrix whose {math}`i`th row is the {math}`i`th column of {math}`A`. As an example, if {math}`A = \begin{bmatrix} a & b \\ c & d\end{bmatrix}` then {math}`A^T = \begin{bmatrix}a & c \\ b & d \end{bmatrix}`. 

It can be shown that {math}`A` and {math}`A^T` have the same eigenvalues,\footnote{One can easily verify this directly for the case in which {math}`A` is {math}`2\times 2` matrix.} though their eigenvectors may differ. That said, we approach the next step in the process by focusing on an eigenvector of {math}`A^T` that is associated with the zero eigenvalue of the matrix. Let {math}`\vec{v}` denote this eigenvector, and define a new variable {math}`y(t) = \vec{v}\bullet \vec{u}(t)` where {math}`\vec{u}(t)` is the solution to the given inhomogeneous differential equation. It follows that
```{math}
  y'(t) = \vec{v} \bullet \vec{u}^{ \prime}(t) 
  = \vec{v} \bullet ( A \vec{u}(t) + \vec{b} )
  = \vec{v} \bullet A \vec{u}(t) + \vec{v} \bullet \vec{b}
  = \vec{u}(t) \bullet A^T \vec{v} + \vec{v} \bullet \vec{b}
  = \vec{v} \bullet \vec{b}
```
where we have applied a well-known identity to convert {math}`\vec{v} \bullet A \vec{u}(t)` to {math}`\vec{u}(t) \bullet A^T \vec{v} = 0`. Solving the equation we arrive at
```{math}
  y(t) = \vec{v}\bullet\vec{b} t + \vec{v}\bullet\vec{u}(0)
  \quad\leftrightarrow\quad
  v_2 u_2(t) + v_1  u_1(t) =
  \vec{v}\bullet\vec{b} t + \vec{v}\bullet\vec{u}(0)
```
which can be used to turn the given system of equations into a single linear equation that we can solve using the approaches set out in Chapter 2. The next example shows how our alternative strategy works, in practice.

:::{prf:example}
:label: eg:ivp1
Solve the initial-value problem
```{math}
  \frac{d}{dt} \vec{u}(t)
  =
  \begin{bmatrix} 2 & 1 \\ 4 & 2 \end{bmatrix} \vec{u}(t) + \begin{bmatrix} 3 & 1 \end{bmatrix}
  \quad
  \text{with}
  \quad
  \vec{u}(0) = \begin{bmatrix} 1 & 1 \end{bmatrix}
```
:::

:::{solution .dropdown} eg:ivp1
The matrix featured in the differential equation has a zero eigenvalue, associated with an eigenvector {math}`{1\brack -2}`. Since {math}`{3\brack 1}` is not a multiple of this eigenvalue, we cannot find an equilibrium solution to the differential equation. We therefore try our alternate approach.

The transpose of the matrix from the differential equation is {math}`{2 \quad 4 \brack 1\quad 2}`. It also has a zero eigenvalue, but this eigenvalue is associated with an eigenvector {math}`\vec{v} = {-2\brack 1}`. 

Define {math}`y(t) = \vec{v} \bullet \vec{u}(t)` and observe that
```{math}
\begin{aligned}
  y'(t) 
  &= -2  u_1'(t) + u_2'(t) \\
  &= -2(2 u_1(t) + u_2(t) +3) +(4u_1(t) + 2 u_2(t) + 1) \\
  &= - 5 .
\end{aligned}
```
Using the fact that {math}`y(0) = \vec{v} \bullet\vec{u}(0) = -1` we get
```{math}
  y(t) = - 5 t - 1
  \quad\longrightarrow\quad
  u_2(t) = 2 u_1(t) - 5 t - 1.
```
Substituting the previous expression into the differential equation we have been given for {math}`u_1(t)` we obtain
```{math}
  u_1'(t) = 2 u_1(t) + (2 u_1(t) - 5 t - 1) + 3
  \quad\longleftrightarrow\quad
  u_1'(t) - 4 u_1(t) = 2 - 5 t
```
with {math}`u_1(0)=1`. We find
```{math}
  u_1(t) = e^{4 t} + e^{4 t}  \int_{0}^{t} e^{-4 s} (2-5 s) ds
```
and so
```{math}
  u_2(t) = 2 e^{4 t} + 2 e^{4 t} \int_0^t e^{-4 s} (2-5 s) ds 5t -1.
```
:::

There is so much more to say about systems of differential equations. In fact, most universities offer several courses on differential equations at the undergraduate level alone. Later courses outline the various ways in which models can simultaneously incorporate changes that occur over both time and space. More advanced treatments provide modellers with strategies for coping with the non-linear feedbacks we saw in the predator-prey model we tackled at the outset of this chapter.  Some courses focus on computational strategies while others emphasize analytic ``pencil and paper'' methods. Though these topics are beyond the scope of this text, they are surely not beyond the scope of its readers' ability.

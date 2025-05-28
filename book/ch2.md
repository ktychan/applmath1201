# Introduction to Differential Equations

Mathematical models are often expressed as differential equations. To be successful, modellers typically use information about a given biological problem to formulate a differential equation. Once they are formulated, differential equations can be solved by mathematical or computational means to present the model in a different, and possibly more useful, way.

## What is a differential equation?
A differential equation is the special name given to an equation involving an unknown function {math}`u(t)` and its derivatives {math}`u'(t), u''(t), \ldots`. 
For example,
:::{math}
  u'(t) = u(t)
  \quad \text{and} \quad
  u''(t) - u(t)\, u'(t) = 0
:::
are differential equations because each one expresses a mathematical relationship between an unknown function, namely {math}`u(t)`, and its derivatives. 

## What is a solution to a differential equation?
We can plug functions into a differential equation.  A solution for a differential equation is a function that makes both sides of the differential equation equal to each other. 

:::{prf:example}

We demonstrate the meaning of solutions for differential equations. 

Consider the differential equation {math}`u'(t) = u(t)`.  

1. We can plug {math}`u(t) = e^{t}` into the differential equation. To do so, we replace every {math}`u(t)` by {math}`e^{t}`. The left-hand side of the differential equation becomes {math}`(e^{t})'` which is just {math}`e^{t}`. The right-hand side of the differential equation is just {math}`e^{t}`.  Because the two sides are equal when {math}`u(t) = e^{t}` is plugged into the differential equation, we say that {math}`e^{t}` is a solution.

1. We can plug {math}`u(t) = t^{2}` into the differential equation. The left-hand side of the differential equation becomes {math}`(t^{2})'` which is {math}`2t`.  The right-hand side of the differential equation is {math}`t^{2}`. Because the two sides are \emph{not equal} when {math}`u(t) = t^{2}` is plugged into the differential equation, we say that {math}`t^{2}` is not a solution.

1. Try it for yourself. Which of the following is a solution to the given differential equation?
    1. {math}`u(t) = t^{3}`.
    1. {math}`u(t) = 2e^{t}`. 
    1. {math}`u(t) = e^{5t}`. 
:::

The process of turning the unknown function {math}`u(t)` in a differential equation into an explicit function, one that you can plug in numbers for {math}`t` to get useful outputs, is call \hlmain{solving an differential equation}. In other words, to solve a differential equation is to find the unknown function or functions that make the given statement true. 

In general, a differential equation can be expressed as the zero of a multivariable function of {math}`t`, {math}`u`, and the various derivatives of {math}`u`. That is to say, we can always write a differential equation as
```{math}
  f( t, u(t), u'(t), u''(t), \ldots , u^{(n)}(t) ) = 0.
```	

We can see that, when expressed in this way, a differential equation serves as a recursive model that relates {math}`u` and {math}`t`. By solving the differential equation, we can turn the recursive model into one that involves {math}`u` and {math}`t` only.	

At a basic level, differential equations are classified according to the highest-order derivative they contain. The example {math}`u'(t) = u(t)` above is known as a *first-order* differential equation because {math}`u'(t)` is the derivative of highest order involved in its statement. The example {math}`u''(t) - u(t)u'(t) =0` is a second-order differential equation, because {math}`u''(t)` is the derivative of highest order we find in it.

Differential equations can also be linear or nonlinear. A *linear* differential equation can be rearranged to obtain the form
```{math}
  P_{0}(t) u(t) + P_{1}(t) u'(t) \cdots P_n(t) u^{(n)}(t) = Q(t),
```
where {math}`P_{1}(t), \ldots, P_{n}(t)`, and {math}`Q(t)` are continuous functions of {math}`t` but could, themselves, be nonlinear.
If the differential equation is not linear, then (of course) we call it *nonlinear*.

Linear differential equations can be further subdivided. If {math}`Q(t) = 0` we say the linear differential equation is *homogeneous*. We say that the linear differential equation is *inhomogeneous* (sometimes *non-homogeneous*) if it is not homogeneous. 

Further classifications of differential equations are possible and are made to help us identify those  mathematical techniques that would be most appropriate for finding a solution. Much of this chapter is devoted to exploring first-order linear differential equations as this class of equations crops up in a broad range of biologically important situations.

## A First Look at Solving Differential Equations

Let's turn our attention to {math}`u'(t) = u(t)` and see what it takes to solve this first-order, linear differential equation. Recall that we are attempting to find the unknown function {math}`u(t)`, so it makes sense to try to gather all the terms involving this function on one side of the equation. Provided {math}`u(t)` is not zero\footnote{If {math}`u(t)` is zero then the differential equation becomes {math}`u'(t) = 0` which implies that {math}`u(t)` is constant. Since {math}`u(t)` is zero, the constant in question must also be zero. Consequently, {math}`u(t) = 0` is the solution for all {math}`t`, we can obtain 
```{math}
  \frac{u'(t)}{u(t)} = 1.
```

Taking the indefinite integral with respect to {math}`t` of both sides the differential equation yields
```{math}
  \int \frac{u'(t)}{u(t)} dt = \int dt.
```
Applying the FTC to the left-hand side we get
```{math}
  \int \frac{du}{u} = \int dt
  \quad \longleftrightarrow \quad
  \ln |u(t)| = t + C
  \quad \longleftrightarrow \quad
  |u(t)| = e^t e^C.
```
Removing the absolute value bars from the expression on the far right of the previous line may or may not change the sign of {math}`e^t e^C`. In recognition of this fact we define {math}`a = \pm e^C` and express our result as
```{math}
  u(t) = a e^{t}.
``` 

The solution to the differential equation, here, is actually a family of functions, with each member of the family being specified by a different {math}`a` value [](fig:ch1_fig1).

```{figure} ./standalones/plot-exp.pdf
:label: fig:ch1_fig1

The solution to {math}`u'(t) = u(t)` is the family of functions {math}`u(t) = a e^t`. Each member of the family is defined by its own {math}`a` value.
```

We sometimes pair a differential equation with information about the particular member of the family of solutions we are looking for. We might, for example, try to solve
```{math}
  u'(t) = u(t) \quad \text{with} \quad u(0) = 1.
``` 
In this case, we are looking for the member of the family of solutions that passes through the point {math}`(0,1)`. To solve this *initial value problem* we can simply use the work we have already done above. Doing so, we discover that  
```{math}
  1 = u(0) = a\, e^0 \quad \leftrightarrow\quad a = 1.
```
It follows that the particular solution we seek is {math}`u(t) = e^t`. 


## Linear, First-order Differential Equations

In this section, we discuss a method, called the integrating factor method, to solve a linear, first-order differential equation
```{math}
  u'(t) + p(t) u(t) = q(t).
```
Recall that {math}`u(t)` is the unknown function, and {math}`p(t), q(t)` are parameters. 

:::{prf:definition} integrating factor

Given a linear, first-order differential equation {math}`u'(t) + p(t) u(t) = q(t)`, its integrating factor, often denoted as {math}`v(t)`, is any antiderivative of {math}`p(t)`.  It is often convenient to choose
```{math}
v(t) = \int p(t) \;dt \quad\text{and choose } C = 0.
```
:::

In the next example, we demonstrate how to find an integrating factor for linear, first-order differential equations.

:::{prf:example} 
:label: eg:find-integrating-factor
Find an integrating factor for the differential equation {math}`u'(t) - 2 u(t) = 3t`. 
:::

:::{solution .dropdown} eg:find-integrating-factor
We can directly apply the definition for integrating factors which, in plain English, says that an integrating factor for the given differential equation is any antiderivative for the coefficient of {math}`u(t)`.  

The coefficient of {math}`u(t)` in the given differential equation is {math}`-2`. Therefore an integrating factor for the given differential equation is {math}`v(t) = -2t`. Symbolically, we can express this computation as
```{math}
v(t) = \int -2 \;dt = -2t \text{ (because we can choose {math}`C = 0`)}.
```

Therefore, an integrating factor for the differential equation {math}`u'(t) - 2 u(t) = 3t` is {math}`v(t) = -2t`.
:::

When solving {math}`u'(t) = u(t)` above we chose to collect terms involving {math}`u(t)` by dividing both sides of the differential equation by {math}`u(t)`. This decision led us to an indefinite integral that was familiar to us, and so we found the solution easily. Of course, we could have collected terms in the unknown function by subtracting it from both sides of the equation to get
```{math}
  u'(t) - u(t) = 0 
```	
and eventually
```{math}
  \int (u'(t) - u(t)) dt = 0.
```
This indefinite integral is unfamiliar, and so we might be inclined to conclude that we have collected our unknown terms incorrectly. Fortunately, we are not doomed if we choose this path. 

If we multiply the the differential equation by {math}`e^{-t}` we find
```{math}
  e^{-t} u'(t) - e^{-t} u(t) = 0.
```
The lefthand side of the equation now looks like the result of applying the Product Rule for derivatives. Recognizing this allows us to re-write the equation yet again to obtain
```{math}
  \frac{d}{dt} \bigg[ e^{-t} u(t) \bigg] = 0
```
which tells us {math}`e^{-t} \, u(t)` must be a constant. In other words, {math}`e^{-t} \, u(t) = a` or simply {math}`u(t) = a\, e^{t}`.

Now let's take a step back and consider the general linear first-order equation,
```{math}
  u'(t) + p(t) u(t) = q(t)
```
where {math}`p(t)` and {math}`q(t)` are functions of {math}`t` that we take to be continuous. We will try to solve this general equation by modifying the trick that worked above. Specifically, we multiply through by some convenient function that allows us to exploit what we know about the Product Rule. It turns out that the convenient function in question is {math}`v(t) = e^{\int p(t)\, dt}` where {math}`\int p(t) dt` is any antiderivative of {math}`p(t)` (we do not need to state the antiderivative in its most general form). Multiplying both sides of the differential equation by {math}`v(t)` gives us
```{math}
  v(t)\, u'(t) + v(t)\, p(t)\, u(t)  =  v(t) \, q(t) .
```  
Since the Chain Rule tells us {math}`v'(t) = \frac{d}{dt} \left[e^{\int p(t)dt}\right] = v(t) p(t)`, the previous line can be written simply as
```{math}
  v(t)\, u'(t) + v'(t)\, u(t) = v(t)\, q(t)
  \quad \longleftrightarrow\quad
  \frac{d}{dt}[\, v(t)\, u(t) \, ] = v(t)\, q(t) .
```

Integrating with respect to {math}`t` we arrive at
```{math}
  v(t) u(t) = \int v(t) q(t) dt + C 
```
where we have added the constant of integration {math}`C` to emphasize the fact that we are looking a family of functions. Indeed, that family of functions is given by
```{math}
  u(t) = \frac{1}{v(t)} \left( \int v(t)\, q(t) dt + C \right).
```
We can re-state this more using a definite integral as
```{math}
  u(t) = \frac{1}{v(t)} \left( u(a) v(a) +  \int_{a}^{t} v(s) q(s) ds \right), \text{ where \(a\) is a constant.}
```


:::{prf:example} 
:label: eg:linear1
Solve {math}`u'(t) = \frac{1}{t} u(t) + 1`, that is find all functions that satisfy the differential equation.
:::

:::{solution .dropdown} eg:linear1
If we rearrange the given equation as {math}`u'(t) - \frac{1}{t} u(t) = 1` we see that it is linear with {math}`p(t) = -\frac{1}{t}` and {math}`q(t) = 1`. Note, however, that {math}`p(t)` is not continuous at {math}`t = 0`. This means we may wish to treat the domain of {math}`u(t)` in two parts, {math}`(-\infty, 0)` and {math}`(0, \infty)`. 

We will start with {math}`t` on the interval {math}`(-\infty, 0)`. Following the recipe above we set {math}`v(t) = e^{-\ln |t|} = \frac{1}{|t|}`. Whenever {math}`t` is negative, we know {math}`|t|=-t` and so {math}`v(t) = -\frac{1}{t}`. So
```{math}
  u(t) = \frac{1}{(-1/t)}
  \left(
    \int \left(-\frac{1}{t}\right) dt + C_1
  \right)
  =
  t ( \ln (-t) + C_1 ) 
```
where {math}`C_1` is a constant. When {math}`t` is on the interval {math}`(0,\infty)` we have {math}`v(t) = \frac{1}{t}` and so
```{math}
  u(t) = \frac{1}{1/t}
  \left(
    \int \frac{1}{t} dt + C_2
  \right)
  =
  t ( \ln t + C_2 )
```	
where {math}`C_2` is another constant. We can combine the piecewise solutions and state the solution more generally as
```{math}
  u(t) = t (\ln |t| + C), \quad t\neq 0
``` 
This family of solutions is plotted in [](fig:ch1_fig2). Looking more closely at this figure we can see that the limit of {math}`t (\ln |t| + C)` is zero, so we can state the full solution (for all {math}`t`) as
```{math}
  u(t) 
  =
  \begin{cases}
    t (\ln |t| + C) & t \neq 0,\\
    0 & t =0.
  \end{cases}
```
The catch, here, is that {math}`u(t)` is not differentiable at {math}`t=0`.

```{figure} ./standalones/plot-ch1_fig2.pdf
:label: fig:ch1_fig2

The solution to {math}`u'(t) = \frac{1}{t}u(t)+1` is the family of functions {math}`u(t) = t(\ln|t|+C)` as shown in [](eg:linear1).  Notice that all members of the family converge as {math}`t` tends to {math}`0` which is connected to the presence of the discontinuity in {math}`p(t)` at this point.
```
:::


## Applications of Differential Equations

Differential equations are especially useful for modelling quantities that change over time and space. In biology, we use them to study population growth, the dynamics of food webs, the progress of epidemics, the kinetics of chemical reactions, neuronal spikes, and much more. 

Differential equations offer us a way to move effectively between the biological world and the mathematical one. Suppose we are interested in devising a mathematical expression that describes how much of some drug in a patient's bloodstream changes over time. We could devise such an expression by simply choosing a particular form for the function---one that seems to make sense. However, it is far from clear that our choice would respect all the relevant pharmacokinetic details of the situation. To ensure some degree of plausibility, then, we opt instead for an indirect approach. Specifically, we take what we know about the way drugs behave in the body and use this knowledge to state a differential equation that our unknown function must satisfy. We would then find the mathematical expression we need by solving said equation. 

:::{prf:example} 
:label: eg:drug1
A particular drug is metabolized at a rate of {math}`P\times 100\%` per hour. Assuming the drug is administered at one point in time only, how long will it take for the amount in a patient's body to fall below {math}`1\%` of the original dose? 
:::

:::{solution .dropdown} eg:drug1
We assume that drug metabolism is a *first-order kinetic process*. That is to say the time rate of change in the concentration of the drug is proportional to the concentration itself. If the volume of the patient's bloodstream remains constant first-order kinetics give us
```{math}
  u'(t) = - k\, u(t), \quad \text{with} \quad u(0) = u_0
```
where {math}`u(t)` is the amount of the drug present at time {math}`t` (say, in mg), and {math}`u_0` is the initial dose (again, in mg). We assume the rate constant {math}`k` is positive, and so the negative sign reminds us that there is a decay in the amount of drug in the patient's system.

There are different ways to solve the initial value problem above. Here, we will solve by re-writing the differential equation in standard linear form to get {math}`u'(t) + k\, u(t) = 0`. Using the formula we developed,
```{math}
  u(t) = \frac{1}{e^{kt}} \left( u(0) e^0 +  \int\limits_0^t e^{ks}\, 0 \, dt \right) = u_0 \, e^{-kt} 
```
where we have used {math}`v(0)=1`. We are told that a fraction {math}`P` of the initial dose has been metabolized one hour after the drug is administered, so at this time, a fraction {math}`1-P` remains. If {math}`t` is measured in hours, we get {math}`(1-P)\, u_0 = u(1) = u_0 \, e^{-k(1)}` which tells us that {math}`k = \ln \frac{1}{1-P}`.

We now know the amount of drug at time {math}`t` is given by {math}`u(t) = u_0 \, e^{- t \, \ln (1/(1-P))}` {math}`= u_0 \, (1-P)^t`. To answer the question posed, then, we simply solve
```{math}
  0.01\, u_0 = u_0 \, (1-P)^t
``` 
for {math}`t`. Doing so gives us {math}`t = \frac{ \ln 0.01 }{\ln (1-P)}` hours, and so the amount of drug is below {math}`1\%` of the original dose beyond this time. 
:::

The fate of drugs in a patient's system may be more complicated that the previous example suggests. To tackle more complicated scenarios using differential equations we build a model using a *conservation law* as a guide. This law says that the time-rate of change of a quantity contained within a system is equal to its net rate of production inside the system, minus the net rate of loss from the system:
```{math}
  \frac{d}{dt} \text{quantity} = (\text{net rate of production}) - (\text{net rate of loss}).
```	

In the next example, we apply a conservation law to investigate the dynamics of a drug that is administered in a continuous fashion. 

:::{prf:example} 
:label: eg:drug2
A solution containing a {math}`100` mg per L of drug is administered intravenously at a continuous rate of {math}`80` mL per hour. If the drug is metabolized at a rate of {math}`75 \%` per hour, then what amount of drug is found in a patient's body after {math}`t` hours?
:::

:::{solution .dropdown} eg:drug2
In order to address this problem we need to make five assumptions. First, we will treat the patient as if they are simply a well-mixed container of blood. Second, we will assume drug metabolism is a first-order kinetic process. Third, we will assume that the volume of blood in the container remains a constant 5 L. Fourth, we will assume that any increase in volume caused by the intravenous administration of drug is exactly compensated by excretion (this fourth assumption is really a consequence of the third). Finally, we assume that the patient had no drug in their system prior to receiving the intravenous drip.

Our next step involves stating a differential equation. We recall that the net rate of change in the amount of drug is the difference between the net rate at which it is produced inside the patient's system, and the net rate at which it is lost from the patient's system. 

In this scenario, the net rate of production in the system is actually negative, because the drug is only broken down inside the patient's body. In addition, the net rate of loss from the system is the rate at which the drug is eliminated minus the rate at which drug is added intraveneously. If {math}`u(t)` is the amount of drug (in mg) present at time {math}`t`, then 
```{math}
  \dfrac{d}{dt} u(t) = -(\text{rate metabolized}) 
  - (\text{rate eliminated} - \text{rate added}).
```
It is important to recognize the units involved in our differential equation, as they must be consistent throughout. That is to say, our model must be dimensionally homogeneous. The units associated with {math}`u(t)` are mg and those associated with {math}`t` are hours, consequently {math}`du(t)/dt` is measured in mg per hour. These same units must be used to express other terms in the model.

To establish the correct rate of metabolism we use our work in Example [](eg:drug1) to find {math}`k=\ln \frac{1}{1-0.75} / 1 = 2\ln 2/1` which has units of per hour (i.e. {math}`k` is a frequency). It follows that
```{math}
  \text{rate metabolized} = 2\ln 2\, u(t) \ \text{mg per hour.} 
```
It may seem silly to divide {math}`k` by {math}`1` as was done above. However, the {math}`1` represents the number of hours it takes to lose {math}`75\%` of the drug. By including {math}`1` clearly in our calculation, we remind ourselves that we have a dimensionally homogeneous statement.  	

To determine the correct form of the rate at which drug is added, we take the concentration of the drug solution (mg per L) and multiply it by the administration rate expressed in terms L per hour. Thus,
```{math}
  \text{rate added} = 100\ \frac{\text{mg}}{\text{L}} \times 0.08\ \frac{\text{L}}{\text{hour}} = 8\ \text{mg per hour.} 
```
Lastly, to determine the rate at which the drug is eliminated we take the concentration of drug in the patient's system and multiply it by the administration rate (remember: blood volume is constant!) to get
```{math}
  \text{rate eliminated} = \frac{u(t)}{5} \,\frac{\text{mg}}{\text{L}} \times 0.08 \, \frac{\text{L}}{\text{hour}} =  \frac{2}{125} \, \text{mg per hour.}
``` 

Putting our work together, we have the following recursive model
```{math}
  u'(t) = 8  - 2 \left( \ln 2\, + \frac{1}{125} \right) u(t). 
```
Since there is no drug in the patient's system initially, {math}`u(0)=0`. To turn the recursive model into one that explicitly relates {math}`u` and {math}`t`, then, we need to solve an initial value problem. 

After putting the differential equation in standard form and applying the now-familiar formula we get
```{math}
\begin{aligned}
u(t) 
&= 0 + \frac{1}{e^{t\,2(\ln 2 + 1/125)}} \int_{0}^{t} 8 e^{s 2(\ln 2 + 1/125)} ds \\[3ex]
&= \frac{8\left( 1 - e^{-t\, 2(\ln 2 + 1/125)} \right)}{2(\ln 2 + 1/125)} \\[3ex]
&=\frac{8}{2(\ln 2 + 1/125)} \left( 1 - \left(1- \frac{3}{4} \right)^{t} e^{-\frac{2}{125}t} \right).
\end{aligned}
```
:::

In the previous example, the amount of drug in a patient's system tends to {math}`\frac{8}{2(\ln 2 + 1/125)}` mg as time goes on. This value is significant in the sense that it is the amount at which the rate in is exactly balanced by the rate out. In other words, this is the *equilibrium* amount of drug in the patient's system. Though the function {math}`u(t) = \frac{8}{2(\ln 2 + 1/125)}` is not a solution to the initial value problem, it is a solution to the differential equation that involved in that problem. It is also the function that all solutions to the differential equation begin to resemble over time, and for that reason we refer to the equilibrium {math}`u(t) = \frac{8}{2(\ln 2 + 1/125)}` as *stable* ([](fig:ch1_fig3)).

:::{figure} ./standalones/plot-ch1_fig3.pdf
:label: fig:ch1_fig3

The solution to the initial value problem in Example [](eg:drug2) (solid curve) tends toward an equilibrium of {math}`\frac{8}{2(\ln 2+1/125)}` (dashed line) as {math}`t` grows. In fact, all solutions to the differential equation found in Example [](eg:drug2) (dotted lines) tend toward the same equilibrium over time and for that reason we say that the equilibrium is stable.
:::

In the next example we turn our attention away from pharmacokinetics and toward a problem in ecology. Specifically, we develop the famous *logistic model* of population growth.

:::{prf:example} 
:label: eg:logistic

Consider a population in which individuals reproduce at per-capita rate {math}`r`. If reproduction is exactly balanced by mortality when the population reaches carrying capacity {math}`K`, then state a differential equation for the time-rate of change in population size {math}`N(t)`. Verify that {math}`N(t)=K` is a stable equilibrium solution to the differential equation. Are there any other equilibria?
:::

:::{solution .dropdown} eg:logistic
We will again use a conservation law to develop the differential equation. Assuming the population is closed to migration our differential equation will only need to consider the net rate at which individuals are produced in the population. In other words, we only need to consider the total birth rate minus the total death rate. 

Given that each individual produces {math}`r` offspring per unit time ({math}`r` is a frequency), then {math}`r\, N(t)` gives the total rate of births. 

To get the total death rate we must think carefully about mortality. We are told that, at carrying capacity {math}`N(t) = K`, the per-capita death rate should equal {math}`r`. Though we don't have to, we will assume that the death rate is negligible when population size is very small; in other words, the per-capita mortality will tend to zero as {math}`N(t)` tends to zero. The simplest way to capture these ideas is to connect {math}`(0,0)` with {math}`(K,r)` and model per-capita death as a line of slope {math}`r/K` (see below). 	

```{figure} ./standalones/plot-logistic.pdf
:label: fig:logistic

The relation between {math}`r` and {math}`k` due to mortality.
```

We can state the differential equation now as
```{math}
  \dfrac{dN(t)}{dt} = r\, N(t) - \frac{r}{K}N(t)^2 = r\, N(t)\, \left( 1 - \frac{N(t)}{K}\right) 
```
and we can verify that the units in the equation are consistent. To find equilibrium solutions, we set {math}`N'(t) = 0` and solve for {math}`N(t)`. Solving this equation we find two equilibria, namely {math}`N(t) = K` and {math}`N(t) = 0`. The first equilibrium is stable. This follows from the fact that when {math}`N(t)` belongs to the interval {math}`(0,K)` the derivative {math}`N'(t) > 0` ({math}`N(t)` is increasing toward {math}`K`). When {math}`N(t)` is strictly greater than {math}`K`, then {math}`N'(t) < 0` and so {math}`N(t)` is decreasing toward {math}`K`. A similar argument shows {math}`N(t)=0` to be an unstable equilibrium.
:::

## Bernoulli substitution
The differential equation in the previous example might look difficult to solve, but we can do it with ingenious use of tools we have already developed (see also Exercise 13). Assume {math}`N(t)` is not equal to zero, and let {math}`u(t)` be its reciprocal, that is set {math}`u(t) = \frac{1}{N(t)}`. Now, observe that
```{math}
  u'(t) = - \frac{1}{N(t)^2} N'(t) = - \frac{1}{N(t)^2}\, r\, N(t)\, \left( 1 - \frac{N(t)}{K}\right) = \frac{r}{K} - r\, u(t).
```
It follows that
```{math}
  u(t) = \frac{1}{e^{rt}} \left( u(0)\cdot 1 + \frac{r}{K}\int\limits_0^t e^{rs}\, ds \right) =  \frac{K/N(0) + e^{rt} - 1}{K e^{rt}}. 
```
and so
```{math}
  N(t) = \frac{K e^{rt}}{K/N(0) + e^{rt} - 1} = \frac{N(0)\, K}{N(0) + (\, K  - N(0)\, )\,  e^{-rt}}.
```
Our ingenious trick has worked! A plot of the solution for {math}`0 < N(0) < K` results in a curve with the characteristic S-shape often referred to in ecology textbooks [](fig:ch1_fig4).

:::{figure} ./standalones/plot-logistic.pdf
:label: fig:ch1_fig4

The S-shaped solution to the logistic model in [](eg:logistic) (solid curve). As expected {math}`N(t)` tends toward the equilibrium at {math}`K` (dashed line) and away from the unstable equilibrium at {math}`0` as {math}`t` goes on.
:::

There are many other tricks we can use to solve differential equations exactly, but an exhaustive exploration of these is beyond the scope of this course.  Even if you know all the tricks there are still differential equations whose exact solution would be beyond your grasp. To solve the most challenging differential equations, modellers turn to computational (i.e. numerical) methods implemented on a computer. Those methods will be our focus in the next chapter.  

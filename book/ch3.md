# Inexact Approaches to Differential Equations

Not all differential equations have solutions that can be found easily or written in terms of elementary functions. Even when a solution to a differential equation can be found we may not want to take the time required to find it. When we are unable or unwilling to find the exact solution to a differential equation, we can turn to {\it graphical methods} or {\it numerical methods} for help. The first of these approaches gives us a qualitative understanding of the behaviour of solutions to a differential equation. The second set of approaches allow us to generate an approximate solutions to the differential equation through computational means. Both approaches serve  also to underscore the fact that mathematics does not always have be exact and elegant.       

In this chapter, we will focus on straightforward methods for solving differential equations graphically and numerically. We will study how the methods work when applied to first-order differential equations, and in some cases, how we can make them work better. 

## Phase-Line Plots

Phase-line plots allow us to uncover important qualitative features of solutions to differential equations without having to solve the equations themselves explicitly. These plots can be applied to study {\it autonomous} first-order equations only; in other words only those differential equations that can be expressed as \(f(u'(t) , u(t) ) =0\) or equivalently as \(u'(t) = g(u(t))\) for continuous \(g\).

A phase-line plot is constructed by simply graphing \(g(u)\) versus \(u\). The horizontal axis of this plot represents the various states of the system whose dynamics are governed by \(u' = g(u)\). The vertical axis tells us about the rate of change in the state of the system itself. When the graph of \(g(u)\) lies above the horizontal axis we know that \(u' = g(u)\) is positive. In this case the state of the system (whatever that may be) is increasing. By contrast, when when the graph of \(g(u)\) falls below the horizontal axis, \(u' = g(u)\) is negative and the state is decreasing. Where the graph of \(g\) passes through the horizontal axis we know that \(u' =0\) and so the value of \(u\) where the root occurs is an equilibrium.

\begin{mdframed}
  \begin{example}
    Use a phase-line plot to uncover qualitative features of solutions to the logistic growth equation \(N'(t) = r(1 - N(t)/K)N(t)\) with \(N(0) >0\).
  \end{example}	

  \begin{solution}
    The differential equation is autonomous, so phase-line analysis is possible. We plot \(r(1-N/K)N\) versus \(N\) as shown below.
    \begin{center}
      \begin{tikzpicture}[blue,yscale=2]
        \draw (0,0)--(3,0) node[right] {\(N\)};
        \draw (0,-0.75)--(0,0.75) node[above] {\(N'\)};
        \draw[domain=0:2.5,samples=100,variable=\N]
        plot({\N}, {\N*(1-\N/2)});
        \node at (0,0) {\(\bullet\)};
        \node[below left] at (0,0) {\(0\)};
        \node at (2,0) {\(\bullet\)};
        \node[above right] at (2,0) {\(K\)};
      \end{tikzpicture}
    \end{center}
    We can immediately identify two equilibria, namely \(\bar u=0\) and \(\bar u=K\). These equilibria are the roots of \(N'\). 

    For values of \(N\) between \(0\) and \(K\) we see that the graph of \(N'\) lies above the horizontal axis. This means that population size \(N\) is increasing when \(0< N < K\). We can represent that by placing arrows on the horizontal axis pointing to the right between values \(0\) and \(K\). 

    For values of \(N\) greater than \(K\) we see that the graph of \(N'\) lies below the horizontal axis. This means that population size \(N\) is decreasing when \(N > K\). We can represent that by placing arrows on the horizontal axis pointing to the left beyond \(K\).
    \begin{center}
      \begin{tikzpicture}[blue,yscale=2]
        \draw (0,0)--(3,0) node[right] {\(N\)};
        \draw (0,-0.75)--(0,0.75) node[above] {\(N'\)};
        \draw[domain=0:2.5,samples=100,variable=\N]
        plot({\N}, {\N*(1-\N/2)});
        \node at (0,0) {\(\bullet\)};
        \node[below left] at (0,0) {\(0\)};
        \node at (2,0) {\(\bullet\)};
        \node[above right] at (2,0) {\(K\)};
        \foreach \p in {0.25, 0.5, 0.75, 1, 1.25, 1.5,1.75}
        {
          \draw[-latex] (\p,0)--({\p+0.125},0);
        }
        \foreach \p in {2.125, 2.375, 2.625}
        {
          \draw[-latex] ({\p+0.125},0)--(\p,0);
        }
      \end{tikzpicture}
    \end{center}

    As the arrows suggest, populations with non-zero numbers of individuals grow or shrink in size until the equilibrium \(\bar u=K\) is reached. Strictly speaking, the equilibrium at \(K\) is only achieved asymptotically, as \(t\to \infty\). With this in mind we classify \(\bar u=K\) as {\it asymptotically stable}. This classification agrees with the discussion presented in Chapter 2.

    The arrows also suggest that if the equilibrium at \(0\) is perturbed even slightly (e.g. by placing a small number of individuals into an empty habitat), population size will tends away from \(0\) over time. With this in mind, we classify \(\bar u=0\) as {\it unstable}. This classification also agrees with the discussion presented in Chapter 2.
  \end{solution}
\end{mdframed}

It is useful to compare the conclusions we obtained in Example 1 with those we would have obtained by solving the differential equation exactly. Recall that, in Chapter 2, we found that the  solution to the differential equation in Example 1 was
\[
  N(t)=
  \frac{N(0)\, K}{N(0) + (\, K  - N(0)\, )\,  e^{-rt}}.
\] 
This equation captures our equilibrium solutions when \(N(0)=0\) and when \(N(0)=K\). What's more, it shows us that (i) when \(0 < N(0) < K\) population size \(N\) is an increasing function of \(t\) that tends away from \(0\) and toward \(K\) as \(t\to \infty\), and (ii) when \(N(0)>K\) population size \(N\) is a decreasing function of \(t\) that also tends to \(K\) as \(t\to \infty\) (see Figure [](#fig:ch2_logistic)).

\begin{figure}
  \centering
  \begin{tikzpicture}[thick, scale=3.25]
    \draw[] (0,0) -- (2.25,0) node [right] {\(t\)};
    \draw[] (0,0) -- (0,1.75) node [above] {\(N(t)\)};
    \draw[] (0,1) -- (2,1);
    \node[left] at (0,1) {\(K\)};
    \node[left] at (0,0) {\(0\)};
    \node at (0,1) {\(\bullet\)};
    \node at (0,0) {\(\bullet\)};
    \draw[domain=0:2, variable=\t, samples=100]
    plot( {\t}, {0.05/(0.05 + 0.95*exp(-4.5*\t))});
    \draw[domain=0:2, variable=\t, samples=100]
    plot( {\t}, {0.5/(0.5 + 0.5*exp(-4.5*\t))});
    \draw[domain=0:2, variable=\t, samples=100]
    plot( {\t}, {0.175/(0.175 + 0.825*exp(-4.5*\t))});
    \draw[domain=0:2, variable=\t, samples=100]
    plot( {\t}, {1.7/(1.7 + (1-1.7)*exp(-4.5*\t))});
    \draw[domain=0:2, variable=\t, samples=100]
    plot( {\t}, {1.25/(1.25 + (1-1.25)*exp(-4.5*\t))});
    \draw[domain=0.125:2, variable=\t, samples=100]
    plot( {\t}, {4/(4 + (1-4)*exp(-4.5*\t))});
    \foreach \N in {0,0.25,0.5,0.75}
    {
      \draw[-latex] (0,\N)--(0,{\N + 0.125});
    }
    \foreach \N in {1.25,1.5}
    {
      \draw[-latex] (0,{\N + 0.125})--(0,\N);
    }
  \end{tikzpicture}

  \caption{A plot of exact solutions to the logistic model in Example 1. As expected \(N(t)\) tends toward the equilibrium at \(K\) and away from the unstable equilibrium at \(0\) as \(t\) tends to \(\infty\). We see \(N(t)\) is increasing when \(0< N(0) < K\) and is decrasing when \(N(0)>K\).}
  \label{fig:ch2_logistic}
\end{figure}

Notice that the equilibria identified as points in Example 1 are represented as horizontal lines in Figure [](#fig:ch2_logistic). As in Example 1, we see that time-dependent solutions with \(N(0) >0\) tend toward the asymptotically stable equilibrium and are repelled by the unstable one.


\begin{figure}
  \centering
  \begin{tikzpicture}[yscale=0.25]
    \draw (-1,0)--(3,0) node[right] {\(u\)};
    \draw[domain=-0.5:2.5, samples=100] 
    plot( {\x}, {(\x+1)*(\x-1)*(\x-3)} ) node[right] {\(g(u)\)};
    \draw[domain=-0.5:2.5, dashed]
    plot( {\x}, {-4*(\x-1)} );
    \node at (1,0) {\(\bullet\)};
    \node[above] at (1,0.2) {\(\bar u\)};
    \foreach \p in {-0.75,-0.25, 0.25,  0.75}
    {
      \draw[-latex] (\p,0)--({\p+0.125},0);
    }
    \foreach \p in {1.125,1.625,2.125,2.625}
    {
      \draw[-latex] ({\p+0.125},0)--(\p,0);
    }
    \node at (-1,5) {(a)};
  \end{tikzpicture}
    \hspace{0.35in}
    \begin{tikzpicture}[yscale=0.25]
      \draw (-1,0)--(3,0) node[right] {\(u\)};
      \draw[domain=-0.5:2.5, samples=100] 
      plot( {\x}, {-(\x+1)*(\x-1)*(\x-3)} ) node[right] {\(g(u)\)};
      \draw[domain=-0.5:2.5, dashed]
      plot( {\x}, {4*(\x-1)} );
      \node at (1,0) {\(\bullet\)};
      \node[above] at (1,0.2) {\(\bar u\)};
      \foreach \p in {-0.75,-0.25, 0.25}
      {
        \draw[-latex] ({\p+0.125},0)--(\p,0);
      }
      \foreach \p in {1.625,2.125,2.625}
      {
        \draw[-latex] (\p,0)--({\p+0.125},0);
      }
      \node at (-1,5) {(b)};
    \end{tikzpicture}

  \caption{(a) If \(\bar u\) is an equilibrium solution to \(u' = g(u)\) with \(g'(\bar u) < 0\), then \(\bar u\) attracts all solutions to the differential equation whose initial conditions are sufficiently close to \(\bar u\). In this case, we describe \(\bar u\) as {\it locally asymptotically stable}. (b) If \(g'(\bar u) >0\), then \(\bar u\) repells nearby solutions to \(u'=g(u)\) and we would conclude that \(\bar u\) is unstable.} 
  \label{fig:phase} 
\end{figure}

Phase-line plots suggest that we can test the stability of equilibrium solutions to autonomous differential equations using tools from calculus. If \(\bar u\) is an asymptotically stable equilibrium solution to \(u' = g(u)\), then to the left of the point \(\bar u\) the graph of \(g\) is above the horizontal axis, and to the right of \(\bar u\) it is below the horizontal axis. Assuming that \(g\) is differentiable at \(\bar u\), then we would expect asymptotic stability to imply \(g'(\bar u) \leq 0\). In fact, \(g'(\bar u) < 0\) is sufficient to allow us to conclude that the equilibrium \(\bar u\) is {\it locally asymptotically stable} (Figure [](#fig:phase)a). Along the same lines, if \(\bar u\) is unstable then \(g'(\bar u) \geq 0\) and \(g'(\bar u) > 0\) would allow us to conclude that \(\bar u\) is unstable (Figure [](#fig:phase)). 

To apply the ideas about \(g'\) to the differential equation in Example 1, we would do the following. First, we would calculate derivatives: 
\[
  \begin{array}{ccccrcl}
    g'(K) 
        &=& 
        \frac{d}{dN}
        \left[ rN \left(1-\frac{N}{K}\right) \right]_{N=K}
        &=&
        -r
        &<&0, 
        \\[1ex]
        g'(0) 
        &=& 
        \frac{d}{dN}
        \left[ rN \left(1-\frac{N}{K}\right)\right]_{N=0}
        &=&
        r
        &>&0.
  \end{array}
\] 
Second, based on these calculations, we would be able to conclude that the equilibrium at \(K\) is locally asymptotically stable, while that at \(0\) is unstable.

It must be emphasized that we cannot make any conclusions about the stability of \(\bar u\) using \(g'\) when \(g'(\bar u) = 0\). If \(g'(\bar u) = 0\) the equilibrium \(\bar u\) could be stable, but it does not have to be. As shown in Figure [](#fig:phase2), \(g'(\bar u) =0\) can occur when \(\bar u\) is asymptotically stable and when \(\bar u\) is unstable. When \(g'(\bar u)=0\) we opt to use the phase-line plot to assess an equilibrium's stability.

\begin{figure}
  \centering
  \begin{tikzpicture}
    \node at (-1.25,1) {(a)};
    \draw (-1,0) -- (1,0);
    \draw[domain=-0.875:0, samples=50]
    plot({\x},{(\x)^4});
    \draw[domain=0:0.875, samples=50]
    plot({\x},{-(\x)^4});
    \foreach \p in {-1,-0.8,-0.6}
    {
      \draw[-latex] (\p,0)--({\p + 0.1},0);
    }
    \foreach \p in {0.6,0.8,1}
    {
      \draw[-latex] (\p,0)--({\p - 0.1},0);
    }
    \node at (0,0) {\(\bullet\)};
    \node[above] at (0,0.2) {\(\bar u\)};
  \end{tikzpicture}
  \hspace{0.25in}
  \begin{tikzpicture}
    \node at (-1.25,1) {(b)};
    \draw (-1,0) -- (1,0);
    \draw[domain=-0.875:0, samples=50]
    plot({\x},{-(\x)^4});
    \draw[domain=0:0.875, samples=50]
    plot({\x},{(\x)^4});
    \foreach \p in {0.6,0.8,1}
    {
      \draw[-latex] (\p,0)--({\p + 0.1},0);
    }
    \foreach \p in {-1,-0.8,-0.6}
    {
      \draw[-latex] (\p,0)--({\p - 0.1},0);
    }
    \node at (0,0) {\(\bullet\)};
  \end{tikzpicture}
  \hspace{0.25in}
  \begin{tikzpicture}
    \node at (-1.25,1) {(c)};
    \draw (-1,0) -- (1,0);
    \draw[domain=-0.75:0, samples=50]
    plot({\x},{(\x)^4});
    \draw[domain=0:0.75, samples=50]
    plot({\x},{(\x)^4});
    \foreach \p in {0.6,0.8,1}
    {
      \draw[-latex] (\p,0)--({\p + 0.1},0);
    }
    \foreach \p in {-1,-0.8,-0.6}
    {
      \draw[-latex] ({\p - 0.1},0)--(\p,0);
    }
    \node at (0,0) {\(\bullet\)};
    \node at (0.75,-0.45) {};
  \end{tikzpicture}
  \caption{When \(g'(\bar u) =0\) an equilibrium can be locally asymptotically stable (as in a), or unstable (as in b and c).}
  \label{fig:phase2}
\end{figure}

\begin{mdframed}
  \begin{example}
    Find the equilibrium solutions to the autonomous differential equation \(u' = u^2 - 3u - 4\) and classify them according to their local stability properties.
  \end{example}
  \begin{solution}
    The given equation can be written as \(u' = g(u) = (u+1)(u-4)\).
    We immediately identify that \(\bar u = -1\) and \(\bar u= 4\) are the only equilibrium solutions to the equation. 

    We have \(g'(-1) = 2(-1)-3 = -7 < 0\) and \(g(4) = 2(4) - 3 = 5 >0\). Consequently, we can classify \(\bar u=-1\) as locally asymptotically stable and \(\bar u=4\) as unstable.   
  \end{solution}
\end{mdframed}

\end{document}

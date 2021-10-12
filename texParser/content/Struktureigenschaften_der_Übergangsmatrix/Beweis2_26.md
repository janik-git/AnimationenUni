---
 title: "Beweis2_26"
 mathjax : true
---
Zunächst einmal gilt für jedes $x \in E$
$$\sum_{y \in E}G(x,y) = \sum_{n=0}^{\infty} \sum_{y \in E} p_{n}(x,y) = \sum_{n=0}^{\infty} 1 = \infty$$
Da E endlich ist, gibt es folglich ein $y \in E$ mit $G(x,y) = \infty$.
Da E aufgrund der Irreduzibilität nur aus einer kommunizierenden Klasse
besteht, ist insbesondere $y \rightarrow x$. Folglich existiert ein
$m \in \mathbb{N}$ mit $p_{m}(x,y)>0$. Aus der
Chapman-Kolmogorov-Gleichung folgt zudem
$p_{m+n}(x,x) \geq p_{n}(x,y) \cdot p_{m}(y,x)$. Also,
$$G(x,x) \geq \sum_{n=0}^{\infty} p_{n}(x,y)p_{m}(y,x) = \underbrace{p_{m}(y,x)}_{>0} \cdot G(x,y) = \infty$$
Somit ist x nach Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ rekurrent.
Aus Satz $\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$
folgt dann aber, dass jeder Zustand in E rekurrent ist. Angenommen
$x \in E$ wäre nullrekurrent. Dann folgt aus Satz
$\ref{x und y selbe Periode, x transient y auch x nullrekurrent y auch}$,
dass jeder Zustand nullrekurrent ist. Aber dann folgt aus Korollar
$\ref{nullrekurrent und limes}$
$$1 = \lim_{n \to \infty} \sum_{y \in E} p_{n}(x,y) \stackrel{\vert E \vert < \infty}{=} 0 \: \: \lightning$$
$\Rightarrow$ alle Zustände in E sind positiv rekurrent.

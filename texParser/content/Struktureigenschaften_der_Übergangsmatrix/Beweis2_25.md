---
 title: "Beweis2_25"
 mathjax : true
---
a\) : $x \leftrightarrow y \quad \Rightarrow \quad d(x) = d(y)$\
\
Bezeichne mit
$D(x) := \lbrace n \in \mathbb{N}_{0} \: : \: p_{n}(x,x)>0 \rbrace$,
$x \in E$. Seien nun $x,y \in E$ mit x $\leftrightarrow$ y. Wähle
$m,n \in \mathbb{N}_{0}$ so, dass $p_{m}(x,y)>0$ und $p_{n}(y,x)>0$.
Dann gilt für jedes $k \in D(y)$ aufgrund der
Chapman-Kolmogorov-Gleichung
$$p_{m+k+n}(x,x) \geq p_{m}(x,y) \cdot p_{k}(y,y) \cdot p_{n}(y,x) > 0$$
Folglich ist $m+k+n \in D(x)$. Ist nun d ein Teiler von D(x), so gilt
$$d \: | \: \lbrace m+k+n \: : \: k \in D(y) \rbrace$$ Da aber
$m+n \in D(x)$ und somit $d \: | \: (m+n)$, folgt $d \: | \: D(y)$.
Also, $$d(x) = ggT(D(x)) \leq ggT(D(y)) = d(y)$$ Durch Vertauschen der
Rollen von x und y folgt analog $d(y) \leq d(x)$. Also $d(x) = d(y)$.\
\
b) $"\Rightarrow"$ Sei x transient. Da x $\leftrightarrow$ y, existieren
$k,l \in \mathbb{N}$ so, dass $p_{k}(x,y)>0$ und $p_{l}(y,x)>0$. Dann
folgt aus der Chapman-Kolmogorov-Gleichung
$$p_{k+l+n}(x,x) \geq p_{k}(x,y) \cdot p_{n}(y,y) \cdot p_{l}(y,x) > 0 \quad \forall n \in \mathbb{N}.$$
Daraus folgt aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$
$$\infty > \sum_{n=1}^{\infty} p_{k+l+n}(x,x) \geq \underbrace{p_{k}(x,y)}_{>0} \cdot \underbrace{p_{l}(y,x)}_{>0} \sum_{n=1}^{\infty} p_{n}(y,y) \quad \Rightarrow \quad \sum_{n=1}^{\infty} p_{n}(y,y) < \infty$$
Also ist y transient.\
$"\Leftarrow"$ Analog.\
\
c) $"\Rightarrow"$ Sei x nullrekurrent. Da $x \leftrightarrow y$
existieren somit $k,l \in \mathbb{N}$ mit $p_{k}(x,y) > 0$ und
$p_{l}(y,x) > 0$. Wiederum folgt aus der Chapman-Kolmogorov-Gleichung
$$p_{k+l+n}(x,x) \geq p_{k}(x,y) \cdot p_{n}(y,y) \cdot p_{l}(y,x) \quad \forall n \in \mathbb{N}$$
Dann folgt aus Satz $\ref{nullrekurrent und limes}$
$$0 = \lim_{n \to \infty}p_{k+l+n}(x,x) \geq \limsup_{n \to \infty} \underbrace{p_{k}(x,y)}_{>0} \cdot \underbrace{p_{l}(y,x)}_{>0} \cdot p_{n}(y,y) \quad \Rightarrow \quad \lim_{n \to \infty} p_{n}(y,y) = 0$$
Folglich ist y nach Satz $\ref{nullrekurrent und limes}$ nullrekurrent.\
$"\Leftarrow"$ Analog.

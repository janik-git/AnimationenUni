---
 title: "Beweis2_19"
 mathjax : true
---
Sei $y \in E$ nullrekurrent. Dann folgt aus Satz
$\ref{nullrekurrent und limes}$, dass
$\lim \limits_{ n \to \infty} p_{n}(y,y) = 0$. Zudem ist
$$p_{n}(x,y) = \sum_{k=1}^{n} \mathbb{P}_{x}[S_{\lbrace y \rbrace} = k] p_{n-k}(y,y) = \sum_{k=1}^{\infty} \mathbb{P}_{x}[S_{\lbrace y \rbrace} = k] \mathbbm{1}_{k \geq n} p_{n-k}(y,y).$$
Setze
$f_{n}(k) := \mathbbm{1}_{k \geq n} p_{n-k}(y,y), \: k \in \mathbb{N}$.
Dann gilt $f_{n}(k)$ $\stackrel{n \to \infty}{\to}$ 0,
$\forall \: k \in \mathbb{N}$ und
$\vert \vert f_{n} \vert \vert_{\infty} \leq 1$,
$\forall n \in \mathbb{N}$.

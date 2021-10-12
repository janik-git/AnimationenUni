---
 title: "Beweis2_18"
 mathjax : true
---
Sei $y \in E$ ein transienter Zustand. Dann folgt aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$
$$\sum_{n=1}^{\infty} p_{n}(y,y) < \infty \: \Rightarrow \: \lim_{n \to \infty} p_{n}(y,y) = 0$$
Sei also nun $x \in E$, $x \neq y$. Dann gilt
$$p_{n}(x,y) = \mathbb{P}_{x}[X_{n} = y] = \sum_{k=1}^{n} \mathbb{P}_{x}[X_{n} = y, S_{\lbrace y \rbrace} = k]$$
$$= \sum_{k=1}^{n} \mathbb{P}_{x}[S_{\lbrace y \rbrace} = k] \cdot \mathbb{P}_{x}[X_{n} = y \: | \: X_{k} = y, S_{\lbrace y \rbrace} = k]$$
Somit folgt aus Satz $\ref{vorangegangene und zukünftige Ereignisse}$
$$p_{n}(x,y) = \sum_{k=1}^{n} \mathbb{P}_{x}[S_{\lbrace y \rbrace} = k] \cdot \mathbb{P}_{y}[X_{n-k} = y] = \sum_{k=1}^{n} \mathbb{P}_{x}[S_{\lbrace y \rbrace} = k] \cdot p_{n-k}(y,y)$$
Also,
$$\sum_{n=1}^{\infty} p_{n}(x,y) = \sum_{k=1}^{\infty} \mathbb{P}_{x}[S_{\lbrace y \rbrace} = k] \sum_{n=k}^{\infty} p_{n-k}(y,y) = \mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty](1 + \underbrace{\sum_{n=1}^{\infty} p_{n}(y,y)}_{< \infty}) < \infty$$
Damit erhält man $\lim \limits_{n \to \infty} p_{n}(x,y) = 0$ für alle
$x \neq y$.

---
 title: "Beweis2_23"
 mathjax : true
---
: $y \rightarrow x$\
\
Angenommen $y \not\rightarrow x$, d.h. $p_{n}(y,x) = 0$ für alle
$n \in \mathbb{N}$. Wähle $n_{0} \in \mathbb{N}_{0}$ so, dass
$$p_{n_{0}}(x,y) > 0.$$ Da x rekurrent ist, gilt
$$0 \stackrel{\mathrm{Satz} \: \ref{alternative Chrakterisierung von rekurrent/transient}}{=} \mathbb{P}_{x}[X_{n} = x \: für \: endlich \: viele \: n \in \mathbb{N}_{0}]$$
$$\geq \mathbb{P}_{x}[X_{n_{0}} = y, X_{n_{0} + 1} \neq x, X_{n_{0} + 2} \neq x,...]$$
$$= \mathbb{P}_{x}[X_{n_{0}}=y] \cdot \mathbb{P}_{x}[X_{n_{0}} = y,  X_{n_{0} + 1} \neq x, X_{n_{0} + 2} \neq x,... \: | \: X_{n_{0}} = y]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} p_{n_{0}}(x,y) \cdot \mathbb{P}_{y}[X_{1} \neq x, X_{2} \neq x,...]$$
Setze $A_{n} = \lbrace X_{1} \neq x,...,X_{n} \neq x \rbrace.$ Dann gilt
$$A_{n} \downarrow \bigcap_{k=1}^{\infty} A_{k} = \lbrace X_{1} \neq x, X_{2} \neq x,...\rbrace$$
und
$$\mathbb{P}_{y}[X_{1} \neq x,..., X_{n} = x] = 1 - \mathbb{P}_{y}[{\lbrace X_{1} \neq x,..., X_{n} = x \rbrace}^{C}] \geq 1 - \sum_{k =1}^{n} \underbrace{\mathbb{P}_{y}[X_{k} = x]}_{p_{n}(y,x) = 0} = 1$$
Damit erhält man aus der Stetigkeit des Wahrscheinlichkeitsmaßes
$\mathbb{P}_{y}$
$$\mathbb{P}_{y}[X_{1} \neq x, X_{2} \neq x,...] = \lim_{n \to \infty} \mathbb{P}_{y}[X_{1} \neq x,...,X_{n} \neq x] = 1.$$
Also
$$0 \geq p_{n_{0}}(x,y) \cdot \mathbb{P}_{y}[X_{1} \neq x, X_{2} \neq x,...] = p_{n_{0}}(x,y) > 0 \: \: \lightning$$
Folglich gilt $y \rightarrow x$.

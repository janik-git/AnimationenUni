---
 title: "Beweis1_14"
 mathjax : true
---
: $h_{A}$ ist eine Lösung des obigen Dirichletproblems.\
\
Da $\lbrace X_{0} \in A \rbrace = \lbrace T_{A} = 0 \rbrace$, ist
folglich $h_{A}(x) = 1$ für alle $x \in A$.\
Sei also nun $x \in A^{C}$. Dann folgt mit Satz
[\[vorangegangene und zukünftige Ereignisse\]](#vorangegangene und zukünftige Ereignisse){reference-type="ref"
reference="vorangegangene und zukünftige Ereignisse"}
$$\mathbb{P}_{x}[T_{A} < \infty] = \mathbb{P}_{x}[T_{A} \in \mathbb{N}] = \sum_{y \in E} \mathbb{P}_{x}[T_{A} \in \mathbb{N}, X_{1} = y]$$
$$= \sum_{y \in E} \mathbb{P}[X_{1} = y \: | \: X_{0} = x] \cdot \mathbb{P}_{\nu}[T_{A} \in \mathbb{N} \: | \: X_{0} = x, X_{1} = y]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[T_{A} \in \mathbb{N}_{0}]$$
Also,
$$h_{A}(x) = \mathbb{P}_{x}[T_{A} < \infty] = \sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[T_{A} \in \mathbb{N}_{0}] = \sum_{y \in E} p(x,y) \cdot h_{A}(y) \Leftrightarrow (Lh_{A})(x) = 0$$
: $h_{A}$ ist die kleinste, nichtnegative Lösung des folgenden
Dirichletproblems $$(Lh)(x) = 0, \: x \notin A$$
$$h(x) = 1, \: x \in A$$ : Für alle $N \in \mathbb{N}_{0}$ gilt
$\mathbb{P}_{x}[T_{A} \leq N] \leq h(x)$, $x \in E$\
\
Für jedes $N \in \mathbb{N}_{0}$ und $x \in A$ folgt
$P_{x}[T_{A} \leq N] = 1 = h(x)$. Für jedes $x \in A^{C}$ ergibt sich
mittels vollständiger Induktion über N\
\
**IA** $N=0$:
$\mathbb{P}_{x}[T_{A} = 0] \stackrel{x \notin A}{=}0 \leq h(x)$\
\
**IS** $N \to N+1$: Sei also $x \notin A$. Dann gilt mittels Satz
[\[vorangegangene und zukünftige Ereignisse\]](#vorangegangene und zukünftige Ereignisse){reference-type="ref"
reference="vorangegangene und zukünftige Ereignisse"}
$$P_{x}[T_{A} \leq N+1] = P_{x}[1 \leq T_{A} \leq N+1]$$
$$= \sum_{y \in E} \mathbb{P}[X_{1} = y \: | \: X_{0} = x] \cdot \mathbb{P}_{\nu}[1 \leq T_{A} \leq N+1 \: | \: X_{0} = x, X_{1} = y]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[T_{A} \leq N]$$
$$\stackrel{\mathrm{IV}}{\leq}\sum_{y \in E} p(x,y) \cdot h(y)$$
$$\stackrel{(Lh)(x) = 0}{=}h(x)$$ Da
$\lbrace T_{A} \leq N \rbrace \uparrow \bigcup_{k \in \mathbb{N}} \lbrace T_{A} \leq k \rbrace = \lbrace T_{A} < \infty \rbrace$
für $N \to \infty$, so folgt aus der Stetigkeit des
Wahrscheinlichkeitsmaßes $\mathbb{P}_{x}$
$$h_{A}(x) = \mathbb{P}_{x}[T_{A} < \infty] = \lim_{N \to \infty} \mathbb{P}_{x}[T_{A} \leq N] \leq h(x), \: x \in E$$

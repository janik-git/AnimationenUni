---
 title: "Beweis2_20"
 mathjax : true
---
a\) Sei D̂ die kleinste Teilmenge von $\mathbb{Z}$ mit der Eigenschaft,
dass
$$D \subseteq \hat{D} \quad \mathrm{und} \quad \forall d_{1},d_{2} \in \hat{D} \quad \Rightarrow \quad d_{1} \pm d_{2} \in \hat{D}$$
Betrachte nun die Menge
$$\mathcal{D} := \lbrace \hat{d} \in \hat{D} \: : \: \exists k \in \mathbb{N}, \: a_{1},...,a_{k} \in \mathbb{Z}, \: d_{1},...,d_{k} \in D \: \: s.d. \: \: \hat{d} = \sum_{i=1}^{k} a_{i}d_{i} \rbrace$$
: $\hat{D} = \mathcal{D}$\
\
Zunächst einmal gilt $D \subseteq \mathcal{D}$. Betrachte nun
$x,y \in \mathcal{D}$. Dann gilt $x \pm y \in \mathcal{D}$. Da aber
$\hat{D}$ die kleinste Teilmenge ist, die D enthält und abgeschlossen
bzgl. Addition/Subtraktion ist, folgt $\hat{D} \subseteq \mathcal{D}$.
Also $\hat{D} = \mathcal{D}$\
\
: $ggT(D) = ggT(\hat{D})$\
\
Da $ggT(D) \: | \: \sum_{i=1}^{k} a_{i}d_{i}$ für alle
$k \in \mathbb{N}$, $a_{1},...,a_{k} \in \mathbb{Z}$,
$d_{1},...,d_{k} \in D$ folgt $ggT(D) \: | \: \hat{D}$. Also
$$ggT(D) \leq ggT(\hat{D})$$ Adererseits ist $D \subseteq \hat{D}$,
weshalb $ggT(\hat{D}) \: | \: D$. Also, $$ggT(\hat{D}) \leq ggT(D)$$ und
somit gilt $ggT(D) = ggT(\hat{D})$.\
\
: $ggT(\hat{D}) \in \hat{D}$\
\
Setze
$m := \min \lbrace x \in \mathbb{N} \: : \: x \in \hat{D} \rbrace$.
Aufgrund von Bemerkung $\ref{Bemerkung zu Teilern}$ gilt
$ggT(\hat{D}) \leq m$. Durch die Anwendung des euklidischen Algorithmus
ergibt sich für jedes $\hat{d} \in \hat{D}$, dass
$$\hat{d} = a \cdot m + r \qquad \mathrm{für} \: a \in \mathbb{Z} \: \mathrm{und} \: r \in \lbrace 0,...,m-1 \rbrace$$
Also,
$$r = \underbrace{\hat{d}}_{\in \hat{D}} - \underbrace{a \cdot m}_{\in \hat{D}} \in \hat{D}$$
Angenommen $r \neq 0$, so ist $r<m$ $\lightning$. Also ist
$m \: | \: \hat{D}$ und folglich $m \leq ggT(\hat{D})$. Somit gilt
$m=ggT(\hat{D})$ und $ggT(\hat{D}) \in \hat{D}$\
\
b) Sei zusätzlich angenommen, dass $D \subseteq \mathbb{N}_{0}$ und
$d_{1}, d_{2} \in D$ $\Rightarrow$ $d_{1} + d_{2} \in D$.\
\
\
: $\exists \: N \in \mathbb{N}:$ $\lbrace
 n \cdot ggT(D) \: : \: n \geq N \rbrace$ $\subseteq$ D\
\
Da D abgeschlossen unter Addition ist, folgt
$\hat{D} = \lbrace d_{2} - d_{1} \: : \: d_{1},d_{2} \in D \cup \lbrace 0 \rbrace \rbrace$.
Da
$$ggT(D) = ggT(\hat{D}) = \min \lbrace x \in \mathbb{N} \: : \: x \in \hat{D} \rbrace \quad (\mathrm{nach \: Beweisteil \: a}))$$
gibt es somit $d_{1} \in D \cup \lbrace 0 \rbrace$ und $d_{2} \in D$,
$d_{2} > d_{1}$ so, dass $$ggT(D) = d_{2} - d_{1}$$ Falls $d_{1} = 0$,
so gilt
$$n \cdot ggT(D) = n \cdot d_{2} \in D \quad \forall n \in \mathbb{N} \quad \Rightarrow \quad N=1$$
Falls $d_{1} \neq 0$, so wähle ein $a \in \mathbb{N}$ mit
$d_{1} = a \cdot ggT(D)$. Dann gilt für alle $m,r \in \mathbb{N}_{0}$
mit $0 \leq r < m$
$$(a^{2} + m \cdot a +r)\cdot ggT(D) = (a+m)\cdot a \cdot ggT(D) + r \cdot ggT(D) = (a+m) \cdot d_{1} + r \cdot d_{2} \in D$$
Wähle somit $N = a^{2}$. Dann gilt
$\lbrace n \cdot ggT(D) \: : \: n \geq N \rbrace \subseteq D.$

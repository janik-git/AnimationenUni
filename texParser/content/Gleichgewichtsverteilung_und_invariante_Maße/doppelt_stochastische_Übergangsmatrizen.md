---
 title: "doppelt_stochastische_Übergangsmatrizen"
 mathjax : true
---
[\[doppelt stochastische Übergangsmatrizen\]]{#doppelt stochastische Übergangsmatrizen
label="doppelt stochastische Übergangsmatrizen"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E, wobei die Übergangsmatrix $P$ folgende Eigenschaft
besitzt $$\sum_{y \in E} p(y,x) = 1 \qquad \forall \: x \in E,$$ d.h. P
ist doppelt stochastisch. Ein Spezialfall von doppelt stochastischen
Matrizen ist $$p(x,y) = \mu(y-x) \qquad, \quad x,y \in E$$ für ein
Wahrscheinlichkeitsmaß $\mu$ auf E. Dann ist $\pi(x) = 1$ für alle
$x \in E$ ein invariantes Maß, denn
$$\sum_{y \in E} \pi(y) p(y,x) \sum_{y \in E} p(y,x) = 1 = \pi(x) \qquad , \quad x \in E.$$
---
 title: "doppelt_stochastische_Übergangsmatrizen"
 mathjax : true
---
[\[doppelt stochastische Übergangsmatrizen\]]{#doppelt stochastische Übergangsmatrizen
label="doppelt stochastische Übergangsmatrizen"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E, wobei die Übergangsmatrix $P$ folgende Eigenschaft
besitzt $$\sum_{y \in E} p(y,x) = 1 \qquad \forall \: x \in E,$$ d.h. P
ist doppelt stochastisch. Ein Spezialfall von doppelt stochastischen
Matrizen ist $$p(x,y) = \mu(y-x) \qquad, \quad x,y \in E$$ für ein
Wahrscheinlichkeitsmaß $\mu$ auf E. Dann ist $\pi(x) = 1$ für alle
$x \in E$ ein invariantes Maß, denn
$$\sum_{y \in E} \pi(y) p(y,x) \sum_{y \in E} p(y,x) = 1 = \pi(x) \qquad , \quad x \in E.$$[\[doppelt stochastische Übergangsmatrizen\]]{#doppelt stochastische Übergangsmatrizen
label="doppelt stochastische Übergangsmatrizen"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E, wobei die Übergangsmatrix $P$ folgende Eigenschaft
besitzt $$\sum_{y \in E} p(y,x) = 1 \qquad \forall \: x \in E,$$ d.h. P
ist doppelt stochastisch. Ein Spezialfall von doppelt stochastischen
Matrizen ist $$p(x,y) = \mu(y-x) \qquad, \quad x,y \in E$$ für ein
Wahrscheinlichkeitsmaß $\mu$ auf E. Dann ist $\pi(x) = 1$ für alle
$x \in E$ ein invariantes Maß, denn
$$\sum_{y \in E} \pi(y) p(y,x) \sum_{y \in E} p(y,x) = 1 = \pi(x) \qquad , \quad x \in E.$$

**Beispiel 3.15**\[Einfache, asymmetrische Irrfahrt auf $\mathbb{Z}$\]
[\[Einfache, asymmetrische Irrfahrt auf Z\]]{#Einfache, asymmetrische Irrfahrt auf Z
label="Einfache, asymmetrische Irrfahrt auf Z"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf $E=\mathbb{Z}$ mit
$p(x,x+1) = p$ und $p(x,x-1)=1-p$ für alle $x \in E$ und $p \in (0,1)$.
Nach Beispiel $\ref{doppelt stochastische Übergangsmatrizen}$ ist
$\pi(x) = 1$ für alle $x \in E$ ein invariantes Maß. Für
$p \neq \dfrac{1}{2}$ ist zudem
$\pi(x) = {\left( \dfrac{p}{1-p} \right)}^{x}$, $x \in E$ ein
invariantes Maß, denn
$$\sum_{y \in E} \pi(y) p(y,x) = \pi(x-1)p(x-1,x) + \pi(x+1)p(x+1,x)= {\left( \dfrac{p}{1-p} \right)}^{x}(1-p+p) = \pi(x)$$

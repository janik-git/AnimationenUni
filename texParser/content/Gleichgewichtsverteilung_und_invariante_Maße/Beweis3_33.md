---
 title: "Beweis3_33"
 mathjax : true
---
-   Definiere $\bar{P} = (\bar{p}(x,y))_{x,y \in E}$ durch
    $\bar{p}(x,y) := \sum_{n=1}^{\infty} 2^{-n} p_{n}(x,y) \:, \quad x,y \in E$.
    Dann ist $\bar{P}$ eine stochastische Matrix, denn für alle
    $x \in E$ gilt
    $$\sum_{y \in E} \bar{p} (x,y) \stackrel{\mathrm{Fubini}}{=} \sum_{n=1}^{\infty} 2^{-n} \sum_{y \in E} p_{n}(x,y) = \sum_{n=1}^{\infty} 2^{-n} = 1$$
    Da P nach Voraussetzungen irreduzibel ist, folgt $\bar{p}(x,y)>0$
    für alle $x,y \in E$. Angenommen es gäbe zwei
    Gleichgewichtsverteilungen $\pi_{1},\pi_{2} \in Inv(P)$ mit
    $\pi_{1} \neq \pi_{2}$. Da
    $$(\pi_{i} \bar{P})(x) = \sum_{y \in E} \pi_{i}(y) \bar{p}(y,x) \stackrel{\mathrm{Fubini}}{=} \sum_{n=1}^{\infty} 2^{-n} \sum_{y \in E} \pi_{i} p(y,x) = \pi_{i}(x) \sum_{n=1}^{\infty} 2^{-n} = \pi_{i}(x)$$
    für alle $x \in E$ und $i \in \lbrace 1,2 \rbrace$, ist
    $\pi_{1}, \pi_{2} \in Inv(\bar{P})$. Betrachte nun das signierte Maß
    $$\bar{\pi} := \pi_{1} - \pi_{2}.$$ Dann gilt
    $\bar{\pi} \bar{P} = \pi_{1} \bar{P} - \pi_{2} \bar{P} = \pi_{1} - \pi_{2} = \bar{\pi}$.
    Da $\bar{\pi} \neq 0$ und $\bar{\pi}[E]=0$ existieren $x,y \in E$
    mit $\bar{\pi}(x) > 0$ und $\bar{\pi}(y) < 0$. Weiterhin gilt
    $$\sum_{z \in E} \vert \bar{\pi}(z) \vert = \sum_{z \in E} \vert (\bar{\pi}\bar{P})(z) \vert$$
    $$= \sum_{z \in E}\vert \underbrace{\bar{\pi}(x)\bar{p}(x,z)}_{>0} + \underbrace{\bar{\pi}(y)\bar{p}(y,z)}_{<0} +  \sum_{\substack{ z' \in E \\ z' \neq x,y } }\bar{\pi}(z')\bar{p}(z',z) \vert$$
    $$< \sum_{z \in E} \sum_{z' \in E} \vert \bar{\pi}(z') \vert \bar{p}(z',z)$$
    $$= \sum_{z' \in E} \vert \bar{\pi}(z') \vert \quad \lightning$$
    Folglich ist $\bar{\pi}=0$, d.h. $\pi_{1} = \pi_{2}$.

-   Angenommen $Inv(P) \neq \emptyset$, d.h. es gibt eine
    Gleichgewichtsverteilung $\pi$. Nach Voraussetzung ist jeder Zustand
    $y \in E$ transient. Also folgt aus dem Korollar
    $\ref{transienter Zustand dann lim n -> unendl. pn(x,y) = 0}$ und
    dem Satz von Lebesgue
    $$0 = \sum_{x \in E} \pi (x) \lim_{n \to \infty}p_{n}(x,y) = \lim_{n \to \infty} \sum_{x \in E} \pi(x) p_{n}(x,y) = \pi(y) \qquad \forall \: y \in E$$\
    Also, $$\sum_{y \in E} \pi (y) = 0 \neq 1 \quad \lightning$$
    Folglich gibt es keine Gleichgewichtsverteilung.

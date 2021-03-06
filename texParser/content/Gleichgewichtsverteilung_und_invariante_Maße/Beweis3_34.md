---
 title: "Beweis3_34"
 mathjax : true
---
Da $P$ irreduzibel ist, ist nach Bemerkung
$\ref{Auflistende Bemerkung zu invarianten Maßen}$ c) $\pi(x) > 0$ für
alle $x \in E$. Somit sind die Matrixeinträge von $P^{*}$ wohldefiniert.
Zudem gilt
$$\sum_{y \in E} p^{*}(x,y) = \dfrac{1}{\pi (x)} \sum_{y \in E} \pi (y) p(y,x) = 1 \qquad \forall \: x \in E$$
d.h. $P^{*}$ ist eine stochastische Matrix. Aufgrund von Satz
$\ref{Besitzen Markovketten die Markoveigenschaft}$ (i) genügt es nun\
\
: $\: \forall \: n \in \lbrace 0,1,...,N \rbrace$ und
$y_{0},...,y_{n} \in E$ gilt
$$\mathbb{P}_{\pi} [Y_{0} = y_{0},...,Y_{n}=y_{n}] = \pi(y_{0})p^{*}(y_{0},y_{1}) \cdot ... \cdot p^{*}(y_{n-1},y_{n})$$
Für $n \in \lbrace 0,1,...,N \rbrace$ und $y_{0},...,y_{n} \in E$
betrachte nun
$$\mathbb{P}_{\pi} [Y_{0} = y_{0},...,Y_{n}=y_{n}] = \mathbb{P}_{\pi} [X_{N} = y_{0},...,X_{N-n}=y_{n}]$$
$$= \mathbb{P}_{\pi}[X_{N-n} = y_{n}] \mathbb{P}_{\pi} [X_{N} = y_{0},...,X_{N-n+1}=y_{n-1} \: | \: X_{N-n}=y_{n}]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \mathbb{P}_{\pi}[X_{N-n} = y_{n}] \mathbb{P}_{Y_{n}} [X_{n} = y_{0},...,X_{1}=y_{n-1}]$$
$$\stackrel{\mathrm{Satz} \: \ref{"Satz 1.8"}}{=} \underbrace{(\pi P^{N-n})}_{\pi}(y_{n}) \mathbb{P}_{Y_{n}} [X_{1} = y_{n-1},...,X_{n}=y_{0}]$$
$$\stackrel{\mathrm{Satz} \: \ref{Besitzen Markovketten die Markoveigenschaft}}{=} \pi(y_{n}) p(y_{n},y_{n-1}) \cdot ... \cdot p(y_{1},y_{0})$$
$$= \pi(y_{0})p^{*}(y_{0},y_{1}) \cdot ... \cdot p^{*}(y_{n-1},y_{n})$$
Somit ist nach Satz $\ref{Besitzen Markovketten die Markoveigenschaft}$
(i) $(Y_{n})_{0 \leq n \leq N}$ eine $(\pi,P^{*})$-Markovkette.

---
 title: "einfache_Irrfahrt_auf_dem_Graphen"
 mathjax : true
---
Sei G = (V,E(V)) ein Graph mit Knotenmenge V und Kantenmenge E(V).\
\
[Schreibweise]{.ul}: $x \sim y$ $:\Leftrightarrow$ $x,y \: \in V \:$
sind durch eine Kante aus E(V) verbunden. Betrachte $$p(x,y)=
\begin{cases}
\dfrac{1}{deg(x)} &  ,x \sim y\\
0 & ,\mathrm{sonst}
\end{cases}$$ wobei deg(x) die Anzahl der von x ausgehenden Kanten ist.
Dann ist $P =(p(x,y))_{x,y \in V}$ eine stochastische Matrix, und die
($\nu$,P)-Markovkette $(X_{n})_{n \in \mathbb{N}_{0}}$ bezeichnet man
als Irrfahrt auf dem Graphen G mit Startverteilung $\nu$.

. ![Irrfahrt auf einem Graphen](beispiel111 "fig:")

Dabei ist $V = \lbrace 1,2,3,4 \rbrace$ die Knotenmenge und
$E(V) = \lbrace \lbrace 1,2 \rbrace, \lbrace 1,3 \rbrace, \lbrace 2,3 \rbrace, \lbrace 3,4 \rbrace \rbrace$
die Kantenmenge.

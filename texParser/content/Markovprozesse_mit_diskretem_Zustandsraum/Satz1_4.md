---
 title: "Satz1_4"
 mathjax : true
---
Sei $P = (p(x,y))_{x,y \in E}$ eine stochastische Matrix, $\nu$ eine
beliebige Verteilung auf E und $(U_{n})_{n \in \mathbb{N}_{0}}$ eine
Folge u.i.v. Zufallsvariablen mit $U_{0} \sim \mathcal{U}([0,1])$.\
Dann existieren Funktionen $f:[0,1] \to E$ und $F:E \times [0,1] \to E$
so, dass $(X_{n})_{n \in \mathbb{N}_{0}}$ mit\
\
$X_{n}=
\begin{cases}
f(U_{0})  &  , n=0  \\
F(X_{n-1},U_{n})  & , n \in \mathbb{N}
\end{cases}$\
\
\
eine $(\nu,P)$-Markovkette ist.

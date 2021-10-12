---
 title: "unabhängiges_Verschmelzen"
 mathjax : true
---
Sei $P = (p(x,y))_{x,y \in E}$ eine stochastische Matrix und $\mu,\nu$
zwei Wahrscheinlichkeitsmaße auf E. Definiere die Übergangsmatrix
$\bar{P}$ durch $$\bar{p}((x,y),(x',y'))=
\begin{cases}
p(x,x')p(y,y') & , x \neq y\\
p(x,x') & , x = y \: \mathrm{und} \: x' = y'\\
0 & , x=y \: \mathrm{und} \: x' \neq y'
\end{cases}$$ für alle $(x,y),(x',y') \in E \times E$. Dann ist die
$(\mu \otimes \nu,\bar{P})$-Markovkette
$((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$ mit Zustandsraum $E \times E$
eine Kopplung einer $(\mu,P)$-Markovkette und einer
$(\nu,P)$-Markovkette auf E.

. ![unabhängiges Verschmelzen zweier
Markovketten](unabhängiges Verschmelzen "fig:")

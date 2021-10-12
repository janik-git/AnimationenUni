---
 title: "Satz1_1"
 mathjax : true
---
[\[Besitzen Markovketten die Markoveigenschaft\]]{#Besitzen Markovketten die Markoveigenschaft
label="Besitzen Markovketten die Markoveigenschaft"} Sei
${(X_{n})}_{n \in \mathbb{N}_{0}}$ eine Folge von E-wertigen
Zufallsvariablen auf $(\Omega, \mathfrak{F}, \mathbb{P})$, $\nu$ eine
Verteilung auf E und $P = (p(x,y))_{x,y \in E}$ eine stochastische
Matrix.\
\
(i) ${(X_{n})}_{n \in \mathbb{N}_{0}}$ ist genau dann eine
$(\nu,P)$-Markovkette, wenn für alle $n \in \mathbb{N}_{0}$ und
$x_{0},...,x_{n} \in E$ gilt
$$\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}] = \nu(x_{0}) p(x_{0},x_{1}) \cdot ...\cdot p(x_{n-1},x_{n}).$$\
\
(ii) Ist ${(X_{n})}_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette,
so gilt $$\mathbb{P}[X_{n+1} = y \: | \: X_{n} = x] = p(x,y)$$ für alle
$n \in \mathbb{N}_{0}$ und $x,y \in E$ mit $P[X_{n} = x]>0$.

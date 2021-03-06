---
 title: "zeithomogene_Markovkette"
 mathjax : true
---
[\[zeithomogene Markovkette\]]{#zeithomogene Markovkette
label="zeithomogene Markovkette"} Sei $P =(p(x,y))_{x,y \in E}$ eine
stochastische Matrix und $\nu: E \to [0,1]$ ein
Wahrscheinlichkeitsvektor. Ein stochastischer Prozess
$(X_{n})_{n \in \mathbb{N}_{0}}$ auf
$(\Omega, \mathfrak{F}, \mathbb{P})$ mit Zustandsraum E heißt
(zeithomogene) Markovkette mit Übergangsmatrix $P$ und Startverteilung
$\nu$ (kurz: $(\nu,P)$-Markovketten), falls\
\
(i) Für alle $n \in \mathbb{N}_{0}$ und $x_{0},...,x_{n+1} \in E$ mit
$\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}]>0$ gilt
$$\mathbb{P}[X_{n+1} = x_{n+1} \: | \: X_{0} = x_{0},...,X_{n} = x_{n}] = p(x_{n},x_{n+1})$$
(ii) Für alle $x_{0} \in E$ gilt
$$\mathbb{P}[X_{0} = x_{0}]  = \nu(x_{0})$$

---
 title: "Markoveigenschaft"
 mathjax : true
---
Ein stochastischer Prozess $(X_{n})_{n \in \mathbb{N}_{0}}$ auf
$(\Omega, \mathfrak{F}, \mathbb{P})$ mit Werten in E besitzt die
(elementare) Markoveigenschaft, wenn für jedes $n \in \mathbb{N}_{0}$
und alle $x_{0},...,x_{n+1} \in E$ mit
$\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}]>0$ gilt
$$\mathbb{P}[X_{n+1} = x_{n} \: | \: X_{0} = x_{0},...,X_{n} = x_{n}] = \mathbb{P}[X_{n+1} = x_{n} \: | \: X_{n} = x_{n}]$$
Falls zudem für alle $n \in \mathbb{N}_{0}$ und $x,y \in E$ gilt, dass
$$\mathbb{P}[X_{n+1} = y \: | \: X_{n} = x] = \mathbb{P}[X_{1} = y \: | \: X_{0} = x]$$
so besitzt $(X_{n})_{n \in \mathbb{N}_{0}}$ die zeithomogene
Markoveigenschaft.

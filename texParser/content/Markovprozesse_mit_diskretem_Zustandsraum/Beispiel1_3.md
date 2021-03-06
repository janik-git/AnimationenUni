---
 title: "Beispiel1_3"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Folge von unabhängigen
Zufallsvariablen mit Werten in E. Dann gilt für jedes
$n \in \mathbb{N}_{0}$ und $x_{0},...,x_{n+1} \in E$ mit
$\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}]>0$
$$\mathbb{P}[X_{n+1} = x_{n} \: | \: X_{0} = x_{0},...,X_{n} = x_{n}] = \mathbb{P}[X_{n+1} = x_{n+1}] = \mathbb{P}[X_{n+1} = x_{n} \: | \: X_{n} = x_{n}]$$
Folglich besitzt die Folge $(X_{n})_{n \in \mathbb{N}_{0}}$ die
Markoveigenschaft. Falls die Zufallsvariablen zudem identisch verteilt
sind, d.h. $\mathbb{P}[X_{n+1} = x] = \mathbb{P}[X_{1} = x]$ für alle
$n \in \mathbb{N}_{0}$, so hat $(X_{n})_{n \in \mathbb{N}_{0}}$ die
zeithomogene Markoveigenschaft.

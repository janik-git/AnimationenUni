---
 title: "Geburts-_und_Todesprozess"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf
$E = \mathbb{N}_{0}$, dessen Übergangsmatrix $P$ durch folgenden
Übergangsgraphen beschrieben wird

. ![Übergangsgraph eines Geburts- und
Todesprozess](Geburts- und Todesprozess "fig:")

wobei angenommen sei, dass $q_{x} > 0$ für alle $x \in \mathbb{N}$.
Setze
$$\pi(0) := 1 \quad und \quad \pi(x) = \prod_{y=1}^{x} \dfrac{p_{y-1}}{q_{y}}, \quad x \in \mathbb{N}$$
Dann gilt
$$\pi(x-1)p(x-1,x) = \pi(x-1)p_{x-1} = \pi(x-1) \dfrac{p_{x-1}}{q_{x}}p(x,x-1) = \pi(x)p(x,x-1)$$
Folglich ist $\pi$ reversible bzgl. $P$ und insbesondere ein invariantes
Maß. Falls zudem gilt, dass
$$\sum_{x \in E} \pi(x) = \sum_{x \in E} \prod_{y=1}^{x} \dfrac{p_{y-1}}{q_{y}} < \infty$$
so lässt sich $\pi$ zu einer Gleichverteilung normieren.

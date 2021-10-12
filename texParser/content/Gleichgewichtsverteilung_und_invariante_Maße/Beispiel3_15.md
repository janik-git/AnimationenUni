---
 title: "Beispiel3_15"
 mathjax : true
---
Betrachte eine Markovkette $(X_{n})_{n \in \mathbb{N}_{0}}$ mit
Zustandsraum $E = \lbrace 0,1,2,3 \rbrace$, dessen Übergangsmatrix $P$
durch den folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph auf $\lbrace 0,1,2,3 \rbrace$](Beispiel 33 "fig:")

Dann bilden die Zustände $\lbrace 0 \rbrace$ und $\lbrace 2,3 \rbrace$
jeweils eine kommunizierende, positiv rekurrente Klasse, während der
Zustand $\lbrace 1 \rbrace$ transient ist. Folglich sind
$$\pi_{1} = \mathbbm{1}_{\lbrace 0 \rbrace} \quad und \quad \pi_{2} = \dfrac{2}{3}\mathbbm{1}_{\lbrace 2 \rbrace} + \dfrac{1}{3}\mathbbm{1}_{\lbrace 3 \rbrace}$$
die beiden Gleichgewichtsverteilungen in $Inv(p)$. Zudem ist
$\mathbb{E}_{2}[S_{\lbrace 2 \rbrace}] = \dfrac{3}{2}$.

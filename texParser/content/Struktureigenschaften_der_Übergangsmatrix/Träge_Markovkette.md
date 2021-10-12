---
 title: "Träge_Markovkette"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E. Angenommen der Zustand $x \in E$ ist periodisch
$(d(x) \geq 2)$. Betrachte man die Markovkette
$(X'_{n})_{n \in \mathbb{N}_{0}}$ mit Startverteilung $\nu$ und
Übergangsmatrix $P' = \epsilon I + (1-\epsilon)P, \epsilon \in (0,1)$,
wobei I die Einheitsmatrix auf E ist. Dann gilt $d(x)=1$ für alle
$x \in E$, da
$$\lbrace 1 \rbrace \in \lbrace n \in \mathbb{N}_{0} \: : \: p'_{n}(x,x)>0 \rbrace$$
Die Markovkette $(X'_{n})_{n \in \mathbb{N}_{0}}$ nennt man auch träge
Markovkette.

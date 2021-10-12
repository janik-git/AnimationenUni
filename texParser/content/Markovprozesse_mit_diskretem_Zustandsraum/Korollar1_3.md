---
 title: "Korollar1_3"
 mathjax : true
---
[\[Anzahl Besuche\]]{#Anzahl Besuche label="Anzahl Besuche"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E und
$$V_{x} := \sum_{n=0}^{\infty} \mathbbm{1}_{X_{n} = x} \: , \quad x \in E$$
Dann gilt für alle $k \in \mathbb{N}$
$$\mathbb{P}_{x}[V_{x} > k] = (1-\mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty] )^{k}.$$
Falls $\mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty] > 0$, so gilt
$$\mathbb{E}[V_{x}] = \dfrac{1}{\mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty]}$$

---
 title: "unabhängige_Kopplung"
 mathjax : true
---
[\[BSP unabhängige Kopplung\]]{#BSP unabhängige Kopplung
label="BSP unabhängige Kopplung"} Sei $P = (p(x,y))_{x,y \in E}$ eine
stochastische Matrix und $\mu, \nu$ zwei Wahrscheinlichkeitsmaße auf E.
Dann ist die Markovkette $((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$ mit
Werten im Zustandsraum $E \times E$, Startverteilung $\mu \otimes \nu$
und Übergangsmatrix $\bar{P}$ mit
$$\bar{p} \left( (x,y),(x',y') \right) := p(x,x')p(y,y')$$ eine Kopplung
einer $(\mu,P)$-Markovkette $(X_{n})_{n \in \mathbb{N}_{0}}$ und einer
$(\nu,P)$-Markovkette $(Y_{n})_{n \in \mathbb{N}_{0}}$ mit Zustandsraum
E, denn
$$\mathbb{P}_{\mu \otimes \nu}[X_{0} =x] = \mathbb{P}_{\mu \otimes \nu}[(X_{0},Y_{0}) \in \lbrace x \rbrace \times E] = \sum_{y \in E} \mu(x) \nu(y) = \mu(x)$$
und
$$\mathbb{P}_{\mu \otimes \nu}[X_{n+1}=x' \: | \: (X_{n},Y_{n}) = (x,y)]$$
$$= \mathbb{P}_{\mu \otimes \nu}[(X_{n+1},Y_{n+1}) \in \lbrace x' \rbrace \times E \: | \: (X_{n},Y_{n}) = (x,y)]$$
$$= \sum_{y' \in E} \bar{p} \left( (x,y).(x',y') \right) = \sum_{y' \in E} p(x,x')p(y,y') = p(x,x')$$
(Analog prüft man die Bedingung für $(Y_{n})_{n \in \mathbb{N}_{0}}$
nach.)

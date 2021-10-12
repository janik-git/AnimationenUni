---
 title: "Kopplung_von_Markovketten"
 mathjax : true
---
Eine bivariate Markovkette $((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$ mit
Werten im Zustandsraum $E \times E$ heißt eine (markov) Kopplung der
$(\mu,P)$-Markovkette $(X_{n})_{n \in \mathbb{N}_{0}}$ und der
$(\nu,P)$-Markovkette $(Y_{n})_{n \in \mathbb{N}_{0}}$ auf E, falls für
alle $n \in \mathbb{N}_{0}$ und alle $(x,y),(x',y') \in E \times E$ gilt
$$\mathbb{P}[X_{n+1}= x' \: | \: (X_{n},Y_{n}) = (x,y)] = p(x,x')$$
$$\mathbb{P}[Y_{n+1}= y' \: | \: (X_{n},Y_{n}) = (x,y)] = p(y,y')$$

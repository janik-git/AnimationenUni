---
 title: "Beweis1_11"
 mathjax : true
---
Sei $\mathbb{P}[(X_{0},X_{1},...,X_{n-1}) \in  B, X_{n} = x] > 0$. Dann
folgt aus Satz $\ref{vorangegangene und zukünftige Ereignisse}$
$$\mathbb{P}[(X_{0},X_{1},...,X_{n-1}) \in  B, (X_{n+1}, X_{n+2},...) \in A \: | \: X_{n} = x]$$
$$= \mathbb{P}[(X_{0},X_{1},...,X_{n-1}) \in  B \: | \: X_{n} = x] \cdot \mathbb{P}_{\nu}[(X_{n+1}, X_{n+2},...) \in A \: | \: (X_{0},...,X_{n-1}) \in B, X_{n} = x]$$
$$= \mathbb{P}[(X_{0},X_{1},...,X_{n-1}) \in  B \: | \: X_{n} = x] \cdot \mathbb{P}_{x}[(X_{1}, X_{2},...) \in A]$$
$$= \mathbb{P}[(X_{0},X_{1},...,X_{n-1}) \in  B \: | \: X_{n} = x] \cdot \mathbb{P}[(X_{n+1}, X_{n+2},...) \in A \: | \: X_{n} = x]$$

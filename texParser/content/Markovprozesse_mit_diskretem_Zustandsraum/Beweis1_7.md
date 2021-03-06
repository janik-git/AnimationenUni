---
 title: "Beweis1_7"
 mathjax : true
---
\(i\) $\dq \Leftarrow \dq$ Sei $n \in \mathbb{N}_{0}$ und
$x_{0},...,x_{n+1} \in E$ mit
$\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}]>0$. Dann gilt

-   $\mathbb{P}[X_{n+1} = x_{n+1} \: | \: X_{0} = x_{0},...,X_{n} = x_{n}]$
    $$=\dfrac{\mathbb{P}[X_{0} = x_{0},...,X_{n+1} = x_{n+1}]}{\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}]} = \dfrac{\nu(x_{0}) p(x_{0},x_{1}) \cdot ...\cdot p(x_{n-1},x_{n})p(x_{n},x_{n+1})}{\nu(x_{0}) p(x_{0},x_{1}) \cdot ...\cdot p(x_{n-1},x_{n})} = p(x_{n},x_{n+1})$$

-   $\mathbb{P}[X_{0} = x_{0}] = \nu(x_{0})$

Folglich ist ${(X_{n})}_{n \in \mathbb{N}_{0}}$ eine
$(\nu,P)$-Markovkette.\
\
$\dq \Rightarrow n\dq$ Beweis durch vollständige Induktion über n\
\
**IA**\
n=0 :
$\mathbb{P}[X_{0} = x_{0}] \stackrel{\mathrm{Def.} \ref{zeithomogene Markovkette} \:        \mathrm{(ii)}}{=} \nu(x_{0})$\
n=1 :
$\mathbb{P}[X_{0} = x_{0},X_{1} = x_{1}] = \mathbb{P}[X_{0} = x_{0}]\mathbb{P}[X_{1} = x_{1} \: | \: X_{0} = x_{0}]  \stackrel{\mathrm{Def.} \ref{zeithomogene Markovkette} \: \mathrm{(i),(ii)}}{=} \nu(x_{0})p(x_{0},x_{1})$\
\
**IS** n $\to$ n+1\
Sei $\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}]>0$ (andernfalls sind
beide Seiten identisch gleich 0).
$$\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}, X_{n+1} = x_{n+1}]$$
$$= \mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}]\mathbb{P}[X_{n+1} = x_{n+1          }\: | \: X_{0} = x_{0},...,X_{n} = x_{n}]$$
$$\stackrel{\mathrm{IV}}{=} \nu(x_{0}) p(x_{0},x_{1}) \cdot ...\cdot p(x_{n-1},x_{n})\mathbb{P}[X_{n+1} = x_{n+1}\: | \: X_{0} = x_{0},...,X_{n} = x_{n}]$$
$$\stackrel{\mathrm{Def.}\ref{zeithomogene Markovkette} \: \mathrm{(i)}}{=} \nu(x_{0}) p(x_{0},x_{1}) \cdot ...\cdot p(x_{n-1},x_{n})p(x_{n},x_{n+1})$$
(ii) Für $n \in \mathbb{N}_{0}$ und $x,y \in E$ mit
$\mathbb{P}[X_{n} = x]>0$
$$\mathbb{P}[X_{n+1} = y \: | \: X_{n} = x] = \dfrac{\mathbb{P}[X_{0} \in E,.., X_{n-1} \in E, X_{n} = x, X_{n+1} = y]}{\mathbb{P}[X_{0} \in E,.., X_{n-1} \in E, X_{n} = x]}$$
$$= \dfrac{\sum_{x_{0},..,x_{n-1}} \nu(x_{0}) p(x_{0},x_{1}) \cdot ...\cdot p(x_{n-1},x)p(x,y)}{\sum_{x_{0},..,x_{n-1}} \nu(x_{0}) p(x_{0},x_{1}) \cdot ...\cdot p(x_{n-1},x)} = p(x,y)$$

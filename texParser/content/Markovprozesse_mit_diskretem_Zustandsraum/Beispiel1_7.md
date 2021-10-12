---
 title: "Beispiel1_7"
 mathjax : true
---
Sei $E = \lbrace 1,2 \rbrace$ und
$P = \begin{bmatrix} 1 - \alpha & \alpha \\ \beta & 1 - \beta  \end{bmatrix}$
mit $\alpha, \beta \in [0,1].$\
\
Im folgenden soll
$\mathbb{P}[X_{n} = 1 \: | \: X_{0} = 1] = (P^{n})(1,1)$ berechnet
werden. Es gilt
$$p_{n}(1,1) = (P^{n-1} \cdot P)(1,1) = p_{n-1}(1,1)(1 - \alpha) + p_{n-1}(1,2)\beta$$
$$= p_{n-1}(1,1)(1-\alpha) + (1 - p_{n-1}(1,1))\beta$$
$$= (1-\alpha - \beta)p_{n-1}(1,1) + \beta$$ Mit $P^{0}(1,1) = 1$
besitzt die obige Rekursionsgleichung folgende eindeutige Lösung\
\
$p_{n}(1,1)=
\begin{cases}
\dfrac{\beta}{\alpha + \beta} + \dfrac{\alpha}{\alpha + \beta}(1 - \alpha - \beta)^{n}  &  falls \: \: \alpha + \beta > 0\\
1 & falls \: \: \alpha + \beta = 0
\end{cases}$

---
 title: "Beispiel3_14"
 mathjax : true
---
Sei $E= (\mathbb{Z} / (2N)\mathbb{N})$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Irrfahrt auf E mit $$p(x,y)=
\begin{cases}
p & , y = (x+2) \: mod \: 2N  \\
1-p & , y = (x-2) \: mod \: 2N 
\end{cases} 
\qquad p \in (0,1)$$ Bezeichne mit
$$G := \lbrace 2k \: : \: k \in \mathbb{N}_{0} \rbrace \cap E \quad und \quad U := \lbrace 2k +1 \: : \: k \in \mathbb{N}_{0} \rbrace \cap E$$
und setze für $\lambda \in [0,1]$
$$\pi_{\lambda}(x) := \dfrac{\lambda}{N}\mathbbm{1}_{G}(x) + \dfrac{1-\lambda}{N}\mathbbm{1}_{U}(x) \qquad, x \in E$$
Dann gilt
$$\sum_{y \in E} \pi_{\lambda}(y)p(y,x) = \dfrac{\lambda}{N} \sum_{y \in G} p(y,x) + \dfrac{1-\lambda}{N} \sum_{y \in U} p(y,x)$$
$$= \dfrac{\lambda}{N}\mathbbm{1}_{G}(x)(1-p+p) + \dfrac{1-\lambda}{N}\mathbbm{1}_{U}(x)(1-p+p) = \pi_{\lambda}(x)$$
für alle $x \in E$. Folglich ist $\pi_{\lambda} \in Inv(P)$ für alle
$\lambda \in [0,1]$, d.h. $\vert Inv(P) \vert = \infty$. Beachte, dass
die stochastische Matrix $P$ nicht irreduzibel ist und zwei
kommunizierenden Klassen besitzt, nämlich die Menge G und U.

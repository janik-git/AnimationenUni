---
 title: "Beweis2_22"
 mathjax : true
---
Offensichtlich ist die Relation $\leftrightarrow$ symmetrisch und
reflexiv. Seien nun $x,y,z \in E$ mit $x \leftrightarrow y$ und
$y \leftrightarrow z$. Dann gibt es $n_{1},n_{2} \in \mathbb{N}$ mit
$p_{n_{1}}(x,y)>0$ und $p_{n_{2}}(y,z)>0$.\
Aus der Chapman-Kolmogorov-Gleichung folgt
$$p_{n_{1} + n_{2}}(x,z) \geq p_{n_{1}}(x,y) \cdot p_{n_{2}}(y,z) > 0 \Rightarrow x \rightarrow z$$
Analog ergibt sich $z \rightarrow x$. Somit ist $\leftrightarrow$ auch
transitiv. Die zweite Aussage folgt direkt aus der Definition der
kommunizierenden Klasse.

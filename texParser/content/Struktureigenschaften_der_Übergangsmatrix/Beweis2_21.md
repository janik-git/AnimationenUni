---
 title: "Beweis2_21"
 mathjax : true
---
Für $x \in E$ sei
$D(x) := \lbrace n \in \mathbb{N}_{0} \: : \: p_{n}(x,x)>0 \rbrace$.
Falls $D(x) \neq \lbrace 0 \rbrace$, so ergibt sich für alle
$n_{1},n_{2} \in D(x)$ aus der Chapman-Kolmogorov-Gleichung (Satz
$\ref{Chapman-Kolmogorov Gleichung}$)
$$p_{n_{1} + n_{2}}(x,x) = \sum_{z \in E} p_{n_{1}}(x,z)p_{n_{2}}(z,x) \geq p_{n_{1}}(x,x)p_{n_{2}}(x,x) > 0$$
Also, $n_{1} + n_{2} \in D(x)$. Folglich ist $D(x)$ abgeschlossen unter
der Addition.

-   $d(x) < \infty$ $\Rightarrow$ $D(x) \neq \lbrace 0 \rbrace$
    $\stackrel{\mathrm{Satz} \: \ref{Teiler als Linearkombi} \: b)}{\Rightarrow}$
    $\: \exists \: N(x) \in \mathbb{N} \: : \: p_{n \cdot d(x)}(x,x) > 0, \: \forall n \geq N(x)$

-   $"\Rightarrow"$ Folgt direkt aus a)\
    $"\Leftarrow"$ Sei also nun $p_{n}(x,x)>0$ für alle
    $n \geq N(x) \in \mathbb{N}$. Dann enthält $D(x)$ unendlich viele
    Primzahlen. Folglich ist $d(x)=ggT(D(x))=1$

---
 title: "Satz4_21"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine irreduzible, aperiodische,
rekurrente Markovkette mit Zustandsraum E und Übergangsgraph
$P = (p(x,y))_{x,y \in E}$. Dann gilt für alle $x,y \in E$
$$\lim_{n \to \infty} p_{n}(x,y) =
\begin{cases}
\dfrac{1}{\mathbb{E}_{y}[S_{\lbrace y \rbrace}]} & , \mathbb{E}_{y}[S_{\lbrace y \rbrace}] < \infty\\
0 & , \mathbb{E}_{y}[S_{\lbrace y \rbrace}] = \infty 
\end{cases}$$

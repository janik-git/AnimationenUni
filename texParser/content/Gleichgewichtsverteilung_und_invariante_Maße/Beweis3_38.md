---
 title: "Beweis3_38"
 mathjax : true
---
$"\Rightarrow"$ Sei $\pi \in Inv(p)$ mit $\sum_{x \in K} \pi(x) = 1$.
Dann gibt es ein $x \in K$ mit $\pi(x) > 0$. Für jedes $y \in K$ gilt
$x \leftrightarrow y$. Also folgt aus Bemerkung
$\ref{Auflistende Bemerkung zu invarianten Maßen}$ c, dass
$\lambda = \mu_{x}$. Insbesondere ist
$$\mathbb{E}_{x}[S_{\lbrace x \rbrace}] = \sum_{y \in K} \mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace}-1} \mathbbm{1}_{X_{n}=y}] = \sum_{y \in K} \mu_{x}(y) = \dfrac{1}{\pi(x)} \sum_{y \in K} \pi(y) = \dfrac{1}{\pi(x)} < \infty.$$
Folglich ist x positiv rekurrent und es gilt nach Bemerkung
$\ref{Bemerkung 16}$, dass jedes $y \in K$ positiv rekurrent ist. Zudem
gilt
$$\pi(x) = \dfrac{1}{\mathbb{E}_{x}[S_{\lbrace x \rbrace}]} \qquad \forall  \: x \in K$$
d.h. $\pi$ ist eindeutig bestimmt.\
$"\Leftarrow"$ Sei K eine positiv rekurrente Klasse. Dann gilt für ein
$x \in K$
$$\sum_{y \in K} \mu_{x}(y) = \mathbb{E}_{x}[S_{\lbrace x \rbrace}]  < \infty$$
Folglich ist nach Satz
$\ref{aufzählungen existenz von invarianten Maßen}$
$\pi(y) := \mu_{x}(y) / \mathbb{E}_{x}[S_{\lbrace x \rbrace}]$ eine
Gleichgewichtsverteilung mit $\pi(y) = 0$ für alle $y \in K^{C}$. Also
$\sum_{y \in K} \pi(y) = 1$.\
b) Folgt aus Satz $\ref{höchstens eine Gleichverteilung}$ b).

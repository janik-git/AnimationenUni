---
 title: "Beweis2_28"
 mathjax : true
---
Zunächst einmal gilt für jede beschränkte Funktion $f: E \to \mathbb{R}$
und jedes $n \in \mathbb{N}$
$$(P^{n}f)(x) - f(x) = \sum_{k=0}^{n-1} (P^{k+1}f)(x) - (P^{k}f)(x) = \sum_{k=0}^{n-1} (P^{k} Lf)(x) \quad \forall x \in E.$$
Setze $g:= -Lh \geq 0$. Dann gilt nach Voraussetzungen, dass $g(y) > 0$.
Daraus folgt
$$h(y) \geq h(y) - (P^{n}h)(y) = \sum_{k=0}^{n-1} (P^{k}g)(y) = \sum_{k=0}^{n-1} \sum_{z \in E} p_{k}(y,z)g(z) \geq g(y) \sum_{k=0}^{n-1} p_{k}(y,y)$$
für jedes $n \in \mathbb{N}$. Also,
$$\sum_{k=1}^{\infty} p_{k}(y,y) \leq \lim_{n \to \infty} \sum_{k=0}^{n-1} p_{k}(y,y) \leq \dfrac{h(y)}{g(y)} < \infty$$
Folglich ist der Zustand y nach Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ transient.
---
 title: "Beweis2_28"
 mathjax : true
---
Zunächst einmal gilt für jede beschränkte Funktion $f: E \to \mathbb{R}$
und jedes $n \in \mathbb{N}$
$$(P^{n}f)(x) - f(x) = \sum_{k=0}^{n-1} (P^{k+1}f)(x) - (P^{k}f)(x) = \sum_{k=0}^{n-1} (P^{k} Lf)(x) \quad \forall x \in E.$$
Setze $g:= -Lh \geq 0$. Dann gilt nach Voraussetzungen, dass $g(y) > 0$.
Daraus folgt
$$h(y) \geq h(y) - (P^{n}h)(y) = \sum_{k=0}^{n-1} (P^{k}g)(y) = \sum_{k=0}^{n-1} \sum_{z \in E} p_{k}(y,z)g(z) \geq g(y) \sum_{k=0}^{n-1} p_{k}(y,y)$$
für jedes $n \in \mathbb{N}$. Also,
$$\sum_{k=1}^{\infty} p_{k}(y,y) \leq \lim_{n \to \infty} \sum_{k=0}^{n-1} p_{k}(y,y) \leq \dfrac{h(y)}{g(y)} < \infty$$
Folglich ist der Zustand y nach Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$
transient.Zunächst einmal gilt für jede beschränkte Funktion
$f: E \to \mathbb{R}$ und jedes $n \in \mathbb{N}$
$$(P^{n}f)(x) - f(x) = \sum_{k=0}^{n-1} (P^{k+1}f)(x) - (P^{k}f)(x) = \sum_{k=0}^{n-1} (P^{k} Lf)(x) \quad \forall x \in E.$$
Setze $g:= -Lh \geq 0$. Dann gilt nach Voraussetzungen, dass $g(y) > 0$.
Daraus folgt
$$h(y) \geq h(y) - (P^{n}h)(y) = \sum_{k=0}^{n-1} (P^{k}g)(y) = \sum_{k=0}^{n-1} \sum_{z \in E} p_{k}(y,z)g(z) \geq g(y) \sum_{k=0}^{n-1} p_{k}(y,y)$$
für jedes $n \in \mathbb{N}$. Also,
$$\sum_{k=1}^{\infty} p_{k}(y,y) \leq \lim_{n \to \infty} \sum_{k=0}^{n-1} p_{k}(y,y) \leq \dfrac{h(y)}{g(y)} < \infty$$
Folglich ist der Zustand y nach Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ transient.

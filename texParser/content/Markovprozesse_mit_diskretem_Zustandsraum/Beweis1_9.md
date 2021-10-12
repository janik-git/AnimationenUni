---
 title: "Beweis1_9"
 mathjax : true
---
Aus Satz 1.4 folgt
$$\mathbb{E}[f(X_{m+n}) \: | \: X_{m} = x] = \sum_{y \in E} f(y)\mathbb{P}[X_{m+n} = y \: | \: X_{m} = x] = (P^{n}f)(x)$$
$$\mathbb{E}[f(X_{n})] = \sum_{x \in E} f(x) \mathbb{P}[X_{n} = x] = \sum_{x \in E} (\nu P^{n})(x) f(x) = \nu P^{n}f$$
Wobei die absolute Konvergenz der beiden Reihen durch die Voraussetzung
$f \in \mathcal{L}^{\infty}(E)$ garantiert ist, da
$\mathbb{E}[|f(X_{n})|] \leq \sup\limits_{x \in E} |f(x)| < \infty$

---
 title: "Bemerkung2_17"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Irrfahrt auf $\mathbb{Z}^{d}$
mit Start in $x \in \mathbb{Z}^{d}$ und $p(x,y) = \mu(y-x)$, d.h.
$$X_{n} = x + \sum_{k=1}^{n} Z_{k} \quad mit \: (Z_{n})_{k \in \mathbb{N}} \: u.i.v\quad mit \quad \mathbb{P}[Z_{1} = y] = \mu(y).$$

-   $\varphi(0) = 1$ und
    $\vert \varphi(t) \vert \leq \mathbb{E}[\vert e^{i \langle t, Z_{1} \rangle} \vert] = 1$

-   Es gilt
    $$\sum_{x \in \mathbb{Z}^{d}} e^{i \langle t, x \rangle} p_{n}(0,x) = \mathbb{E}_{0}[e^{i \langle t, X_{n} \rangle} ] = \mathbb{E}[\prod_{k=1}^{n} e^{i \langle t, Z_{k} \rangle}] = \mathbb{E}[e^{i \langle t, Z_{1} \rangle}]^{n} = {\varphi (t)}^{n}$$
    Insbesondere folgt aus dem Satz von Lebesgue
    $$(2 \pi)^{-d} \int_{[-\pi, \pi)^{d}} e^{i \langle t, x \rangle} {\varphi (t)}^{n} \diff t = \lim_{r \to \infty} \sum_{\substack{{z \in \mathbb{Z}^{d}} \\ {\vert \vert z \vert \vert < r}}} \underbrace{ p_{n}(0,z) (2 \pi)^{-d} \int_{[-\pi, \pi)^{d}} e^{i \langle t, z- x \rangle} \diff t }_{= (2\pi)^{d} \mathbbm{1}_{x=
    z}} = p_{n}(0,x)$$

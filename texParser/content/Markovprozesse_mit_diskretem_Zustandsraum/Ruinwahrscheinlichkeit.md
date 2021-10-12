---
 title: "Ruinwahrscheinlichkeit"
 mathjax : true
---
Betrachte eine einfache asymmetrische Irrfahrt auf $E = \mathbb{N}_{0}$
mit Absorbtion im Zustand 0.

. ![asymmetrische Irrfahrt auf $\mathbb{N}_{0}$](beispiel23 "fig:")

wiederum soll die Eintrittswahrscheinlichkeit in $\lbrace 0 \rbrace$ (=
Absorbtionswahrscheinlichkeit) bestimmt werden. Aus Satz
[\[Dirichletsatz\]](#Dirichletsatz){reference-type="ref"
reference="Dirichletsatz"} folgt, dass
$h_{\lbrace 0 \rbrace}(x) := \mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty], \: x \in E$
die minimale, nichtnegative Lösung des folgenden Dirichletproblems ist:
$$(Lh_{\lbrace 0 \rbrace})(x) = p(h_{\lbrace 0 \rbrace}(x+1) - h_{\lbrace 0 \rbrace}(x)) + q(h_{\lbrace 0 \rbrace}(x-1) - h_{\lbrace 0 \rbrace}(x)) = 0, \: x \neq 0$$
$$h_{\lbrace 0 \rbrace}(0) = 1$$ [Beh.]{.ul}: Für $p \neq q$ ist die
Lösung von $(Lh)(x) = 0$ für alle $x \in E$ gegeben durch
$$h(x) = a + b \cdot (\dfrac{q}{p})^{x}$$ Es gilt nämlich für
$x \in \mathbb{N}$
$$(Lh)(x) = pb (\dfrac{q}{p})^{x}(\dfrac{q}{p} - 1) + qb (\dfrac{q}{p})^{x} (\dfrac{p}{q} - 1) = b (\dfrac{q}{p})^{x}(q-p + p-q) = 0$$
: p\<q\
\
Da $h_{\lbrace 0 \rbrace}(x) \in [0,1]$ für alle $x \in \mathbb{N}_{0}$,
folgt $b=0$ und, wegen $h_{\lbrace 0 \rbrace}(0) = 1, \: a=1$. Also
$$h_{\lbrace 0 \rbrace}(x) = \mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty] = 1 \qquad \forall x \in \mathbb{N}_{0}$$
: q\<p\
\
Aus $h_{\lbrace 0 \rbrace}(0) = 1$ folgt zunächst einmal, dass
$b = 1-a$. Also
$$\ni h_{\lbrace 0 \rbrace}(x) = (\dfrac{q}{p})^{x} + a(1- (\dfrac{q}{p})^{x}) \qquad \forall x \in \mathbb{N}_{0} \: \Rightarrow a \geq 0$$
Somit impliziert erst die Minimalitätsbedingung, dass $a=0$ ist, d.h.
$$h_{\lbrace 0 \rbrace}(x) = \mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty] = (\dfrac{q}{p})^{x}$$
[Beh.]{.ul}: Für $p=q$ ist die Lösung von $(Lh)(x) = 0$ für alle
$x \in E$ gegeben durch $$h(x) = a + bx$$ Denn für alle
$x \in \mathbb{N}$ gilt
$(Lh)(x) = \dfrac{1}{2}b(x + 1 -x) + \dfrac{1}{2}b(x -1 -x) = 0$\
Da $h_{\lbrace 0 \rbrace}(x) \in [0,1]$ für alle $x \in \mathbb{N}_{0}$,
so folgt $b=0$. Wegen $h_{\lbrace 0 \rbrace}(0) = 1$ ist zudem $a = 1$:
$$h_{\lbrace 0 \rbrace}(x) = \mathbb{P}_{x}[T_{\lbrace 0 \rbrace} \leq \infty] = 1$$

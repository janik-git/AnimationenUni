---
 title: "Beweis1_12"
 mathjax : true
---
Das Ziel ist es den Satz von Daniell-Kolmogorov anzuwenden.\
\
[Schritt 1]{.ul} Definiere die Mengenfunktion
$\mathbb{Q}_{\lbrace 0,1,...,n \rbrace}: \varepsilon^{ \otimes (n+1)} \to [0, \infty]$
durch
$$\mathbb{Q}_{\lbrace 0,1,...,n \rbrace}[\lbrace x_{0},x_{1},..,x_{n} \rbrace] := \nu(x_{0})p(x_{0},x_{1}) \cdot...\cdot p(x_{n-1},x_{n}), \: x_{0},...,x_{n} \in E$$
: $\mathbb{Q}_{\lbrace 0,1,...,n \rbrace}$ ist ein
Wahrscheinlichkeitsmaß\
\
Offensichtlich ist
$\mathbb{Q}_{\lbrace 0,1,...,n \rbrace}[\emptyset] = 0$ und für alle
$A_{1},A_{2},... \in \varepsilon^{ \otimes (n+1)}$ disjunkt gilt
$$\mathbb{Q}_{\lbrace 0,1,...,n \rbrace}[\cup_{i=1}^{\infty}A_{i}] = \sum _{x_{0},...,x_{n} \in E} \mathbbm{1}_{\bigcup_{i=1}^{\infty}A_{i}}(x_{0},...,x_{n}) \cdot \nu(x_{0})p(x_{0},x_{1}) \cdot ... \cdot p(x_{n-1},x_{n})$$
$$\stackrel{A_{i} \mathrm{\: disjunkt}}{=} \sum_{i=1}^{\infty} \sum _{x_{0},...,x_{n} \in E} \mathbbm{1}_{A_{i}}(x_{0},...,x_{n}) \cdot \nu(x_{0})p(x_{0},x_{1}) \cdot ... \cdot p(x_{n-1},x_{n})$$
$$= \sum_{i=1}^{\infty} \mathbb{Q}_{\lbrace 0,1,...,n \rbrace}[A_{i}]$$
Zudem gilt, da P eine stochastische Matrix und $\nu$ ein
Wahrscheinlichkeitsvektor ist
$$\sum_{x_{0},...,x_{n} \in E} \mathbb{Q}_{\lbrace 0,1,...,n \rbrace}[\lbrace x_{0},...,x_{n} \rbrace] = \sum_{x_{0} \in E} \nu(x_{0}) \sum_{x_{1} \in E} p(x_{0},x_{1}) \: ... \sum_{x_{n} \in E}p(x_{n-1},x_{n}) = 1$$
:
$\mathbb{Q}_{\lbrace 0,1,...,n \rbrace} = \mathbb{Q}_{\lbrace 0,1,...,n+1 \rbrace} \circ ({\pi_{\lbrace 0,...,n \rbrace}}^{\lbrace 0,...,n+1 \rbrace})^{-1} \qquad \forall n \in \mathbb{N}_{0}$\
\
Für $A \in \varepsilon^{ \otimes (n+1)}$ gilt

$$\mathbb{Q}_{\lbrace 0,1,...,n+1 \rbrace}[({\pi_{\lbrace 0,...,n \rbrace}}^{\lbrace 0,...,n+1 \rbrace})^{-1}(A)]$$
$$= \sum_{x_{0},...,x_{n} \in A} \nu(x_{0})p(x_{0},x_{1}) \cdot ... \cdot p(x_{n-1},x_{n}) \sum_{x_{n+1} \in E} p(x_{n},x_{n+1}) = \mathbb{Q}_{\lbrace 0,1,...,n \rbrace}[A]$$
Folglich ist die Familie
$\lbrace \mathbb{Q}_{\lbrace 0,1,...,n \rbrace} \: : \: n\in \mathbb{N}_{0}\rbrace$
konsistent. Aus Satz $\ref{Existenzsatz von Daniel und Kolmogorov}$
folgt somit die Existenz genau eines Wahrscheinlichkeitsmaßes
$\mathbb{Q}$ auf
$(E^{\mathbb{N}_{0}},\varepsilon^{ \otimes \mathbb{N}{0}})$ mit
$$\mathbb{Q}_{\lbrace 0,1,...,n \rbrace} = \mathbb{Q} \circ {\pi_{\lbrace 0,1,...,n \rbrace}}^{-1}$$
[Schritt 2]{.ul} Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ ein stochastischer
Prozess auf $(\Omega, \mathfrak{F}, \mathbb{P})$ mit Zustandsraum E.
Definiere $\mathbb{P}_{X} = \mathbb{P} \circ X^{-1} := \mathbb{Q}$\
\
: $(X_{n})_{n \in \mathbb{N}_{0}}$ ist eine $(\nu,P)$-Markovkette\
\
Aus Lemma $\ref{Teilmengen Lemma}$ (i) folgt zunächst einmal, dass
$$\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}] = \mathbb{P}_{X_{\lbrace 0,...,n \rbrace}}[\lbrace x_{0},...,x_{n}  \rbrace] = (\mathbb{P}_{X} \circ {\pi_{\lbrace 0,1,...,n \rbrace}}^{-1})[\lbrace x_{0},...,x_{n}  \rbrace]$$
$$= (\mathbb{Q} \circ {\pi_{\lbrace 0,1,...,n \rbrace}}^{-1})[\lbrace x_{0},...,x_{n}  \rbrace]$$
$$= \mathbb{Q}_{\lbrace 0,1,...,n \rbrace}$$
$$= \nu(x_{0})p(x_{0},x_{1}) \cdot ... \cdot p(x_{n-1},x_{n})$$ Damit
folgt die Behauptung aus dem Satz
$\ref{Besitzen Markovketten die Markoveigenschaft}$ (i).

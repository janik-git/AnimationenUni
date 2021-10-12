---
 title: "Beweis1_10"
 mathjax : true
---
[Schritt 1]{.ul} Für ein beliebiges $k \in \mathbb{N}_{0}$ und
$x_{0},...,x_{k} \in E$ betrachte zunächst
$$\mathbb{P}_{\nu}[(X_{0},...,X_{n-1}) \in B ,  X_{n} = x, X_{n+i} = x_{i} \: , \forall \: i \in \lbrace 0,1,...,k \rbrace]$$
$$\stackrel{\mathrm{Satz \: 1.3 \: (i)}}{=} \sum_{(y_{0},...,y_{n-1}) \in B} \nu(y_{0})p(y_{0},y_{1}) \cdot ... \cdot p(y_{n-1},x) \cdot \mathbbm{1}_{ x = x_{0}} \cdot p(x_{0},x_{1})  \cdot ... \cdot p(x_{k-1},x_{k})$$
$$= \mathbb{P}_{\nu}[(X_{0},...,X_{n-1}) \in B, X_{n} = x] \cdot  \mathbb{P}_{x}[X_{i} = x_{i} \: , \forall \: i \in \lbrace 0,1,...,k \rbrace]$$
Da E diskret ist, folgt somit die Behauptung für alle
endlich-dimensionalen Rechteckmengen.\
\
[Schritt 2]{.ul} Betrachte das Mengensystem
$$\mathcal{D} = \lbrace A \in \varepsilon^{ \otimes \mathbb{N}_{0}} \: | \: \mathbb{P}_{\nu}[(X_{n},X_{n+1},...) \in A \: | \: (X_{0},...,X_{n-1})  \in B, \: X_{n} = x] = \mathbb{P}_{x}[(X_{0},X_{1},...) \in A] \rbrace$$
Wir wollen zeigen, dass $\mathcal{D}$ ein Dynkinssystem ist.\
\
1. Wir müssen zeigen dass $\mathcal{D}$ Omega(hier $E^{\mathbb{N}_{0}}$)
enthält.\
\
Da
$\mathbb{P}_{\nu}[(X_{n},X_{n+1},...) \in E^{\mathbb{N}_{0}}  \: | \: (X_{0},...,X_{n-1})  \in B, X_{n} = x] = 1 = \mathbb{P}_{x}[(X_{0},X_{1},...) \in E^{\mathbb{N}_{0}}]$
ist somit $E^{\mathbb{N}_{0}} \in \mathcal{D}$\
\
2. Wir müssen Stabiltät unter Komplementbildung zeigen.\
\
Sei $D \in \mathcal{D}$. Dann ist auch $D^{C} \in \mathcal{D}$, denn
$$\mathbb{P}_{\nu}[(X_{n},X_{n+1},...) \in D^{C} \: | \: (X_{0},...,X_{n-1})  \in B, X_{n} = x]$$
$$= 1 - \mathbb{P}_{\nu}[(X_{n},X_{n+1},...) \in D \: | \: (X_{0},...,X_{n-1})  \in B, X_{n} = x]$$
$$\stackrel{D \in \mathcal{D}}{=} 1 - \mathbb{P}_{x}[(X_{0},X_{1},...) \in D]$$
$$= \mathbb{P}_{x}[(X_{0},X_{1},...) \in D^{C}]$$\
\
3. Wir müssen Abgeschlossenheit unter disjunkter Vereinigung zeigen.\
\
Seien nun $D_{1},D_{2}... \in \mathcal{D}$ disjunkt und
$D = \bigcup_{i=1}^{\infty}$ $D_{i}$ Dann gilt
$$\mathbb{P}_{\nu}[(X_{n},X_{n+1},...) \in D \: | \: (X_{0},...,X_{n-1})  \in B, X_{n} = x]$$
$$\stackrel{\sigma \mathrm{-Additivität}}{=}  \sum_{i=1}^{\infty} \mathbb{P}_{\nu}[(X_{n},X_{n+1},...) \in D_{i} \: | \: (X_{0},...,X_{n-1})  \in B, X_{n} = x]$$
$$\stackrel{D_{i} \in \mathcal{D}}{=} \sum_{i=1}^{\infty} \mathbb{P}_{x}[(X_{0},X_{1},...) \in D_{i}]$$
$$\stackrel{\sigma \mathrm{-Additivität}}{=} \mathbb{P}_{x}[(X_{0},X_{1},...) \in D]$$
Also ist auch $D \in \mathcal{D}$.\
\
Da $\mathcal{D}$ nach Schritt 1 auch das $\cap$-stabile Mengensystem
$\mathcal{Z}$ der endlich-dimensionalen Rechtecke enthält, folgt aus dem
Hauptsatz über Dynkinsysteme
$$\mathcal{Z} \subseteq \mathcal{D} \qquad \Rightarrow \qquad \varepsilon^{ \otimes \mathbb{N}_{0}} = \sigma(\mathcal{Z}) = d(\mathcal{Z}) \subseteq \mathcal{D} \subseteq \varepsilon^{ \otimes \mathbb{N}_{0}}$$

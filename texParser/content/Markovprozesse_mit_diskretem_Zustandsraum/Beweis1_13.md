---
 title: "Beweis1_13"
 mathjax : true
---
[Schritt 1]{.ul} Sei $E = \mathbb{N}$. Setze\
$$\label{eq: zwei}
\alpha(0) := 0, \alpha(i) := \sum_{k=1}^{i} \nu[\lbrace k \rbrace] \qquad und \qquad \beta(i,0) := 0, \beta(i,j) := \sum_{k=1}^{j} p(i,k) , i \in \mathbb{N}$$
Weiterhin definiere die Funktionen $f:[0,1] \to \mathbb{N}$ und
$F:\mathbb{N} \times [0,1] \to \mathbb{N}$ durch
$$f(u) := \sum_{i=1}^{\infty} i \cdot \mathbbm{1}_{\alpha(i-1)\leq u \leq \alpha(i) }$$
$$F(i,u) := \sum_{j=1}^{\infty} j \cdot \mathbbm{1}_{\beta(i,j-1)\leq u \leq \beta(i,j) }$$
Dann gilt für die durch ($\ref{eq: zwei}$) definierte Folge und alle
$i_{0},...,i_{n} \in \mathbb{N}$
$$\mathbb{P}[X_{0} = i_{0},...,X_{n} = i_{n}]$$
$$= \mathbb{P}[U_{0} \in [\alpha(i_{0} - 1),\alpha(i_{0})], U_{k} \in [\beta(i_{k-1},i_{k} -1),\beta(i_{k-1},i_{k})] \: \: \forall k  \in \lbrace 1,...,n \rbrace ]$$
$$\stackrel{}{=} \mathbb{P}[U_{0} \in [\alpha(i_{0} - 1),\alpha(i_{0})] \cdot \prod_{k=1}^{n} \mathbb{P}[ U_{k} \in [\beta(i_{k-1},i_{k} -1),\beta(i_{k-1},i_{k})]]$$
$$= \nu(i_{0})p(i_{0},i_{1}) \cdot .... \cdot p(i_{n-1},i_{n})$$ Also
ist $(X_{n})_{n \in \mathbb{N}_{0}}$ nach Satz
$\ref{Besitzen Markovketten die Markoveigenschaft}$ (i) eine
$(\nu,P)$-Markovkette.\
\
[Schritt 2]{.ul} Da E abzählbar ist, gibt es eine bijektive Funktion
$\varphi: \mathbb{N} \to E$. Die Aussage des Satzes folgt somit aus
Schritt 1.

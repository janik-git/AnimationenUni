---
 title: "Satz3_18"
 mathjax : true
---
[\[aufzählungen existenz von invarianten Maßen\]]{#aufzählungen existenz von invarianten Maßen
label="aufzählungen existenz von invarianten Maßen"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E und $\emptyset \neq K \subseteq E$ eine rekurrente,
kommunizierende Klasse. Für $x \in K$ definiere
$$\mu_{x}(y) := \mu_{x}[\lbrace y \rbrace] := \mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace} - 1} \mathbbm{1}_{X_{n} = y}] \quad , \quad y \in E$$
wobei
$S_{\lbrace x \rbrace} := \inf \lbrace n \in \mathbb{N} \: : \: X_{n} = x  \rbrace$
die erste Treffzeit des Zustandes $x \in E$ sei.

-   Dann gilt für alle $x,y \in K$ mit $x \neq y$
    $$\mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace}] > 0 \quad und \quad \mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace} - 1} \mathbbm{1}_{X_{n} = y}] = \dfrac{\mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace}]}{\mathbb{P}_{y}[S_{\lbrace x \rbrace} < S_{\lbrace y \rbrace}]}$$
    Insbesondere ist $\mu_{x}(x)=1, \: \mu_{x}(y) =0$ für alle
    $y \in K^{C}$ und $\mu_{x}(y) \in (0,\infty)$ für alle $y \in K$.

-   Für jedes $x \in K$ ist $\mu_{x}$ ein invariantes Maß bzgl. $P$.

-   Ist $\lambda$ ein invariantes Maß bzgl. $P$ mit $\lambda(x) =1$ für
    ein $x \in K$ und $\lambda(y) = 0$ für alle $y \in K^{C}$, so gilt
    $\lambda = \mu_{x}$

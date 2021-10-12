---
 title: "Beweis2_30"
 mathjax : true
---
Da nach Vorraussetzungen $(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel
ist, gibt es nach Definition nur eine kommunizierende Klasse.

-   Für $x \in A$ gilt
    $S_{\lbrace x \rbrace}(\omega) \geq S_{A}(\omega)$ für alle
    $\omega \in \Omega$. Daraus folgt
    $$0<\mathbb{P}_{x}[S_{A}=\infty] = \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq S_{A}, S_{A} = \infty] \leq \mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty] \: \Leftrightarrow \: \mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] < 1$$
    Also ist jeder Zustand x transient. Der Satz
    $\ref{x und y selbe Periode, x transient y auch x nullrekurrent y auch}$
    impliziert nun, dass jeder Zustand $y \in E$ transient ist.

-   Bezeichne wieder mit $S_{A}^{k}$ die k-te Treffzeit der Menge A,
    d.h.
    $$S_{A}^{0} := 0 \quad und \quad S_{A}^{k} := \inf \lbrace n> S_{A}^{k-1} \: : \: X_{n} \in A \rbrace, \quad k \in \mathbb{N}$$
    Da $\mathbb{P}_{x}[S_{A} < \infty] = 1$ für alle $x \in A$, so folgt
    für jedes $n \in \mathbb{N}$ $$\mathbb{P}_{x} [S_{A}^{n} < \infty]$$
    $$= \sum_{y \in A} \mathbb{P}_{x}[S_{A}^{n} < \infty \: | \: S_{A}^{n-1} < \infty, X_{S_{A}^{n}}=y]\mathbb{P}_{x} [S_{A}^{n-1} < \infty, X_{S_{A}^{n-1}} = y]$$
    $$\stackrel{\mathrm{Satz} \: \ref{starke Markoveigenschaft}}{=} \sum_{y \in A} \underbrace{\mathbb{P}_{y}[S_{A} < \infty]}_{= 1} \mathbb{P}_{x} [S_{A}^{n-1} < \infty, X_{S_{A}^{n-1}} = y]$$
    $$= \mathbb{P}_{x}[S_{A}^{n-1} < \infty]$$ Induktiv ergibt sich
    daraus, dass $\mathbb{P}_{x}[S_{A}^{k} < \infty] = 1$ für alle
    $n \in \mathbb{N}$ und $x \in A$.\
    Da $(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, gilt für alle
    $x \in A$ und $y \in E \setminus A$, dass $x \leftrightarrow y$,
    d.h. $$\mathbb{P}_{x}[S_{\lbrace y \rbrace} = \infty] < 1$$ Folglich
    existiert zu jedem $x \in A$ ein $N_{x} \in \mathbb{N}$ und
    $\epsilon_{x} > 0$ mit
    $$\mathbb{P}_{x}[n < S_{\lbrace y \rbrace}] \leq 1 - \epsilon_{x} \qquad \forall \: n \geq N_{x}$$
    Setze $N := \max \lbrace N_{x} \: : \: x \in A \rbrace$ und
    $\epsilon := \min \lbrace \epsilon_{x} \: : \: x \in A \rbrace$. Da
    A endlich ist, gilt $N < \infty, \: \epsilon > 0$ und
    $$\mathbb{P}_{x}[n < S_{\lbrace y \rbrace}] \leq 1 - \epsilon \qquad \forall n \geq N, \: x \in A$$
    Da $S_{A}^{n} \geq n$, folgt somit
    $$\mathbb{P}_{x}[S_{A}^{n} < S_{\lbrace y \rbrace}] \leq 1 - \epsilon \qquad \forall n \geq N, \: x \in A$$
    Zudem gilt für alle $k \in \mathbb{N}$
    $$\mathbb{P}_{x}[S_{A}^{kN} < S_{\lbrace y \rbrace}] =$$
    $$\sum_{z \in A} \mathbb{P}_{x}[S_{A}^{kN} < S_{\lbrace y \rbrace} \: | \: S_{A}^{(k-1)N} < S_{\lbrace y \rbrace}, X_{S_{A}^{(k-1)N}} = z] \mathbb{P}_{x}[ S_{A}^{(k-1)N} < S_{\lbrace y \rbrace}, X_{S_{A}^{(k-1)N}} = z]$$
    $$\stackrel{\mathrm{Satz} \: \ref{starke Markoveigenschaft}}{=} \sum_{z \in A} \underbrace{\mathbb{P}_{z}[S_{A}^{N} < S_{\lbrace y \rbrace}]}_{\leq 1-\epsilon} \mathbb{P}_{x}[ S_{A}^{(k-1)N} < S_{\lbrace y \rbrace}, X_{S_{A}^{(k-1)N}} = z]$$
    $$\leq (1- \epsilon)\mathbb{P}_{x}[ S_{A}^{(k-1)N} < S_{\lbrace y \rbrace}].$$
    Daraus ergibt sich induktiv, dass
    $$\mathbb{P}_{x}[S_{A}^{kN} < S_{\lbrace y \rbrace}] \leq (1- \epsilon)^{k} \qquad \forall \: k \in \mathbb{N}, \: x \in A$$
    Somit erhält man
    $$\mathbb{P}_{x}[S_{\lbrace y \rbrace} = \infty] = \limsup_{k \to \infty} \mathbb{P}_{x}[S_{A}^{kN} < \infty, S_{\lbrace y \rbrace} = \infty]$$
    $$\leq \limsup_{k \to \infty} \mathbb{P}_{x}[S_{A}^{kN} < S_{\lbrace y \rbrace}] = \limsup_{k \to \infty} (1 - \epsilon)^{k} = 0$$
    Also, $$\mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] = 1$$
    Angenommen y wäre transient. Dann folgt aus Satz
    $\ref{irreduzibel, y rekurrent -> Px=1 , y transient -> Px<1 }$,
    dass
    $$\mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] < 1 \quad \lightning$$
    Folglich ist y rekurrent. Aus Satz
    $\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$ folgt
    dann aber, dass jeder Zustand $y \in E$ rekurrent ist.

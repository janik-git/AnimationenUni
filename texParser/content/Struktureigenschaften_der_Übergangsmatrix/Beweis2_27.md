---
 title: "Beweis2_27"
 mathjax : true
---
Da $(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, folgt
$x \leftrightarrow y$ für alle $x,y \in E$. Insbesondere sind nach Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$ und
$\ref{x und y selbe Periode, x transient y auch x nullrekurrent y auch}$
alle Zustände entweder rekurrent oder transient, d.h.

-   $\mathbb{P}_{y}[S_{\lbrace y \rbrace} < \infty] = 1 \: \forall y \in E$

-   $\mathbb{P}_{y}[S_{\lbrace y \rbrace} < \infty] < 1 \: \forall y \in E$

Sei nun $x,y \in E$ mit $x \neq y$. Dann existieren wegen
$x \leftrightarrow y$ ein $n \in \mathbb{N}$ so, dass
$$n = \min \lbrace k \in \mathbb{N} \: : \: p_{k}(y,x)>0 \rbrace.$$ Dann
gilt für jedes N>n
$$\mathbb{P}_{y}[S_{\lbrace y \rbrace} \leq N, X_{n} = x]$$
$$= \sum_{k=1}^{N} \mathbb{P}_{y}[S_{\lbrace y \rbrace} = k, X_{n} = x]$$
$$= \sum_{k=1}^{n-1} \mathbb{P}_{y}[S_{\lbrace y \rbrace} = k]\mathbb{P}_{y}[X_{n} = x \: | \: X_{S_{\lbrace y \rbrace}} = y, S_{\lbrace y \rbrace} = k] + \sum_{k=n+1}^{N} \mathbb{P}_{y}[X_{n} =x]\mathbb{P}_{y}[S_{\lbrace y \rbrace} = k \: | \: X_{n} = x]$$
$$= \sum_{k=1}^{n-1} \mathbb{P}_{y}[S_{\lbrace y \rbrace} = k]\mathbb{P}_{y}[X_{n-k} = x] + \sum_{k=n+1}^{N} \mathbb{P}_{y}[X_{n} =x]\mathbb{P}_{y}[S_{\lbrace y \rbrace} = k-n]$$
wobei im letzten Schritt sowohl die Markoveigenschaft als auch die
starke Markoveigenschaft benutzt wurde. Zudem gilt nach Wahl von n, dass
$$\mathbb{P}_{y}[X_{n-k} = x] = 0 \quad \forall \; k \in \lbrace 1,2,...,n-1 \rbrace$$
Daraus folgt
$$\mathbb{P}_{y}[S_{\lbrace y \rbrace} < \infty, X_{n} = x]$$
$$= \lim_{N \to \infty} \mathbb{P}_{y}[S_{\lbrace y \rbrace} \leq N, X_{n} = x]$$
$$= p_{n}(y,x) \sum_{k=n+1}^{\infty}\mathbb{P}_{x}[S_{\lbrace y \rbrace} = k-n]$$
$$= p_{n}(y,x) \cdot \mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty]$$

-   Ist nun $\mathbb{P}_{y}[S_{\lbrace y \rbrace} < \infty] = 1$, so
    folgt
    $$p_{n}(y,x) = \mathbb{P}_{y}[S_{\lbrace y \rbrace} < \infty, X_{n} = x] = p_{n}(y,x) \cdot \mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] \: \Leftrightarrow \: \mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] = 1$$

-   Ist nun $\mathbb{P}_{y}[S_{\lbrace y \rbrace} < \infty] < 1$, so
    gilt
    $$p_{n}(y,x) > \mathbb{P}_{y}[S_{\lbrace y \rbrace} < \infty, X_{n} = x] = p_{n}(y,x) \cdot \mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] \: \Leftrightarrow \: \mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] < 1$$

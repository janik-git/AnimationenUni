---
 title: "Beweis2_17"
 mathjax : true
---
Für $x \in E$ sei $V_{x} := \sum_{n=0}^{\infty} \mathbbm{1}_{X_{n} = x}$
die Gesamtzahl der Besuche von $(X_{n})_{n \in \mathbb{N}_{0}}$ in x.
Insbesondere ist
$\mathbb{E}_{x}[V_{x}] = 1 + \sum_{n=1}^{\infty} p_{n}(x,x)$.

-   $\dashuline{zu \: zeigen}:$ x rekurrent $\Rightarrow$
    $\mathbb{P}_{x}[X_{n} = x \: \: u.o.] = 1$\
    \
    Sei also x rekurrent, d.h.
    $\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] = 1$. Dann folgt aus
    Korollar $\ref{Anzahl Besuche}$:
    $$\mathbb{P}_{x}[X_{n} = x \: \: u.o.] = \mathbb{P}_{x}[V_{x} = \infty] = \lim_{k \to \infty} \mathbb{P}_{x}[V_{x} > k] = \lim_{k \to \infty} {\underbrace{\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty]}_{=1}}^{k} = 1$$
    $\mathrm{\dashuline{zu \: zeigen}:}$
    $\mathbb{P}_{x}[X_{n} = x \: \: u.o.] = 1$ $\Rightarrow$
    $\sum_{n=1}^{\infty} p_{n}(x,x) = \infty$\
    \
    Es gilt nun aber
    $$\mathbb{P}_{x}[V_{x} = \infty] = \mathbb{P}_{x}[X_{n} = x \: \: u.o.] = 1 \Rightarrow \mathbb{E}_{x}[V_{x}] = \infty$$
    $$\Rightarrow \sum_{n=1}^{\infty} p_{n}(x,x) = \mathbb{E}_{x}[V_{x}] - 1 = \infty$$
    $\dashuline{zu \: zeigen}:$
    $\sum_{n=1}^{\infty} p_{n}(x,x) = \infty$ $\Rightarrow$
    $\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] = 1$\
    \
    Angenommen $\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] < 1$.
    Dann folgt aus Korollar $\ref{Anzahl Besuche}$
    $$\sum_{n=1}^{\infty} p_{n}(x,x) = \mathbb{E}_{x}[V_{x}] - 1 \leq \mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty]^{-1} < \infty \: \: \lightning$$
    Also ist $\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] = 1$.

-   $\dashuline{zu \: zeigen}:$ x transient $\Rightarrow$
    $\sum_{n=1}^{\infty} p_{n}(x,x) < \infty$ $\Rightarrow$
    $\mathbb{P}_{x}[X_{n} = x \: \: u.o.] = 0$\
    \
    Sei also x transient, d.h.
    $\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] < 1$. Dann folgt aus
    Korollar $\ref{Anzahl Besuche}$
    $$\sum_{n=1}^{\infty} p_{n}(x,x) = \mathbb{E}_{x}[V_{x}] - 1 \leq \mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty]^{-1} < \infty$$
    Insbesondere impliziert $\mathbb{E}_{x}[V_{x}] < \infty$, dass
    $\mathbb{P}_{x}[X_{n} = x \: \: u.o.] = 0$\
    \
    $\dashuline{zu \: zeigen}:$
    $\mathbb{P}_{x}[X_{n} = x \: \: u.o.] = 0$ $\Rightarrow$
    $\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] < 1$\
    \
    Angenommen $\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] = 1$.
    Dann folgt aus Korollar $\ref{Anzahl Besuche}$
    $$\mathbb{P}_{x}[X_{n} = x \: \: u.o.] = \mathbb{P}_{x}[V_{x} = \infty] = \lim_{k \to \infty} \mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty]^{k} = 1 \: \: \lightning$$
    Also gilt $\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty] < 1$.

---
 title: "Beweis1_15"
 mathjax : true
---
Sei also $A \in \varepsilon^{ \otimes \mathbb{N}_{0}}$,
$F \in \mathfrak{F}_{T}^{X}$ und $x \in E$ mit
$\mathbb{P}_{\nu}[F, X_{T} = x, T < \infty] > 0$. Dann gibt es zu jedem
$n \in \mathbb{N}_{0}$ ein $B \subseteq E^{n}$ mit
$$F \cap \lbrace T = n \rbrace \cap \lbrace X_{T} = x \rbrace = \lbrace (X_{0},...,X_{n-1}) \in B, X_{n} = x \rbrace$$
Falls zudem $\mathbb{P}_{\nu}[(X_{0},...,X_{n-1}) \in B, X_{n} = x] > 0$
ist, so folgt aus Satz $\ref{vorangegangene und zukünftige Ereignisse}$
$$\mathbb{P}_{\nu}[(X_{T},X_{T+1},...) \in A \: | \: F, X_{T} = x, T = n]$$
$$= \mathbb{P}_{\nu}[(X_{T},X_{T+1},...) \in A \: | \: (X_{0},...,X_{n-1}) \in B, X_{n} = x]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \mathbb{P}_{x}[(X_{0},X_{1},...) \in A]$$
Also,
$$\mathbb{P}_{\nu}[(X_{T},X_{T+1},...) \in A \: | \: F, X_{T} = x, T < \infty]$$
$$= \sum_{n=0}^{\infty} \dfrac{\mathbb{P}_{\nu}[(X_{T},X_{T+1},...) \in A \: | \: F, X_{T} = x, T = n] \cdot \mathbb{P}_{\nu}[F, X_{T} = x, T = n]}{ \mathbb{P}_{\nu}[F, X_{T} = x, T < \infty]}$$
$$= \sum_{n=0}^{\infty} \dfrac{\mathbb{P}_{x}[(X_{0},X_{1},...) \in A] \cdot \mathbb{P}_{\nu}[F, X_{T} = x, T = n]}{ \mathbb{P}_{\nu}[F, X_{T} = x, T < \infty]}$$
$$= \mathbb{P}_{x}[(X_{0},X_{1},...) \in A]$$

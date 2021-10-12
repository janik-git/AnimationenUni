---
 title: "Beispiel1_9"
 mathjax : true
---
Sei $X=(X_{n})_{n \in \mathbb{N}_{0}}$ ein stochastischer Prozess mit
Zustandsraum E und $A \subseteq E$.

-   Die Erste Rückkehr-bzw. Treffzeit $S_{A}$ und die Eintrittszeit
    $T_{A}$ ist gegeben durch
    $$S_{A}(\omega) := \inf \lbrace n \in \mathbb{N} : X_{n}(\omega) \in A \rbrace$$
    $$T_{A}(\omega) := \inf \lbrace n \in \mathbb{N}_{0} : X_{n}(\omega) \in A \rbrace$$
    sind Stoppzeiten, denn
    $$\lbrace S_{A} = n \rbrace = \lbrace X_{1} \notin A,...,X_{n-1} \notin A, X_{n} \in A  \rbrace \in \mathfrak{F}_{n}^{X}$$
    $$\lbrace T_{A} = n \rbrace = \lbrace X_{0} \notin A,...,X_{n-1} \notin A, X_{n} \in A  \rbrace \in \mathfrak{F}_{n}^{X}$$
    Insbesondere gilt $\mathbb{P}[S_{A} = T_{A} \: | \: X_{0} = x] = 1$
    für alle $x \notin A$

-   Die k-te Treffzeit ist gegeben durch
    $$S_{A}^{0}(\omega) := 0 \: , \: S_{A}^{k}(\omega) := \inf \lbrace n> S_{A}^{k-1}(\omega) \: : \: X_{n} \in A \rbrace \: , \: k \in \mathbb{N}$$

-   Jede deterministische Zeit $T(\omega) = t$, $t \in \mathbb{N}_{0}$
    ist eine Stoppzeit, da
    $$\lbrace T = n \rbrace \in \lbrace \emptyset, \Omega \rbrace  \in \mathfrak{F}_{n}^{X} \:,\: n \in \mathbb{N}_{0}$$

-   Die letzte Austrittszeit auf der Menge A
    $$L_{A}(\omega) := \sup \lbrace n \in \mathbb{N}_{0} \: : \: X_{n} \in A \rbrace$$
    ist i.A. keine Stoppzeit, da $\lbrace L_{A} = n \rbrace$ davon
    abhängt, ob $(X_{n+m})_{m \in \mathbb{N}_{0}}$ die Menge A trifft
    oder nicht.

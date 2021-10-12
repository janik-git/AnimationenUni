---
 title: "Beweis2_31"
 mathjax : true
---
-   Offensichtlich gilt für die Stoppzeit $S_{A} \wedge n$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n] \leq n$ für alle $x \in E$ und
    $n \in \mathbb{N}$. Aus der Dynkin-Formel(Satz
    $\ref{Dynkin-Formel}$) angewendet auf $T = S_{A} \wedge n$ und
    $f = h \wedge n$ folgt zusammen mit dem Lemma von Fatou
    $$h(y) = \liminf_{m \to \infty} h(y) \wedge m \geq \liminf_{m \to \infty}
    \liminf_{n \to \infty} \mathbb{E}_{y}[h(X_{S_{A} \wedge n}) \wedge m]$$
    $$\geq \mathbb{E}_{y}[h(X_{S_{A}})\mathbbm{1}_{S_{A} < \infty}] \geq \inf_{z \in A} h(z) \mathbb{P}_{y}[S_{A} < \infty]$$
    Also,
    $$\mathbb{P}_{y}[S_{A}< \infty] \leq \dfrac{h(y)}{\inf_{z \in A} h(z)} < 1$$
    Zusammen mit Lemma $\ref{Px[SA < unendlich] < 1, so y transient}$ a)
    folgt somit, dass jeder Zustand in E transient ist.

-   : Für jedes $c \geq 0$ gilt
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in \lbrace h \leq c \rbrace$\
    \
    Aus der Irreduziblität folgt zunächst einmal, dass für jedes
    $c \geq 0$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] < 1 \qquad \forall x \in \lbrace h \leq c \rbrace$$
    Folglich existiert zu jedem $x \in \lbrace h \leq c \rbrace$ ein
    $N_{x} \in \mathbb{N}$ und $\epsilon_{x} > 0$ so, dass
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon_{x} \qquad n \geq N_{x}$$
    Setze
    $N := \max {\lbrace N_{x} \: : \: x \in {\lbrace h \leq c \rbrace}  \rbrace}$
    und
    $\epsilon := \min \lbrace \epsilon_{x} \: : \: x \in \lbrace h \leq c \rbrace \rbrace$.
    Da nach Voraussetzungen die Menge $\lbrace h \leq c \rbrace$ endlich
    ist für jedes $c \geq 0$, folgt $N < \infty$, $\epsilon > 0$ und
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon \quad \forall n \geq N \quad \mathrm{und} \quad x \in {\lbrace h \leq x \rbrace}$$
    Weiterhin gilt für jedes $k \in \mathbb{N}$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN]$$
    $$= \sum_{y \in {\lbrace h \leq c \rbrace}} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN \: | \: S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y] \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in {\lbrace h \leq c \rbrace}} \underbrace{\mathbb{P}_{y}[S_{\lbrace h > c \rbrace}> N]}_{\leq 1 - \epsilon} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\leq (1-\epsilon) \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N]$$
    Folglich ergibt sich induktiv, dass
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N] \leq (1-\epsilon)^{k}$
    für alle $k \in \mathbb{N}$ und $x \in \lbrace h \leq c \rbrace$.\
    Somit erhält man
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] = \limsup_{k \to \infty} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = kN] \leq \limsup_{k \to \infty} (1-\epsilon)^{k} = 0 \quad \forall x \in {\lbrace h > c \rbrace}$$
    :
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in A$\
    \
    Für jedes $c \geq 0$ gilt für die Stoppzeit
    $S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}] \leq n < \infty$
    für alle $n \in \mathbb{N}$ und $x \in E$. Mit der Dynkin-Formel
    (Satz $\ref{Dynkin-Formel}$) angewendet auf
    $T=S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$ und
    $f = h \wedge m$ folgt zusammen mit dem Lemma von Fatou
    $$h(x) = \liminf_{m \to \infty} h(x) \wedge m$$
    $$\geq \liminf_{m \to \infty} \liminf_{n \to \infty} \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} ) \wedge m] \geq \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} )]$$
    Daraus folgt
    $$h(x) \geq \mathbb{E}_{x}[h(X_{S_{{\lbrace h > c \rbrace}}}) \mathbbm{1}_{S_{{\lbrace h > c \rbrace} < \infty}}\mathbbm{1}_{S_{{\lbrace A \rbrace} = \infty}}] \geq c \cdot \mathbb{P}_{x}[S_{{\lbrace h > c \rbrace}} < \infty, S_{{\lbrace h > c \rbrace}} = \infty]$$
    $$= c \cdot \mathbb{P}_{x}[S_{A} = \infty]$$ Da dies für jedes
    $c \geq 0$ gilt, folgt schließlich
    $$\mathbb{P}_{x}[S_{A} = \infty] \leq \limsup_{c \to \infty} \dfrac{h(x)}{c} = 0 \quad \Leftrightarrow \quad \mathbb{P}_{x}[S_{A} < \infty] = 1 \qquad \forall x \in E$$
    Folglich ist nach Lemma
    $\ref{Px[SA < unendlich] < 1, so y transient}$ b) jeder Zustand
    $y \in E$ rekurrent.
---
 title: "Beweis2_31"
 mathjax : true
---
-   Offensichtlich gilt für die Stoppzeit $S_{A} \wedge n$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n] \leq n$ für alle $x \in E$ und
    $n \in \mathbb{N}$. Aus der Dynkin-Formel(Satz
    $\ref{Dynkin-Formel}$) angewendet auf $T = S_{A} \wedge n$ und
    $f = h \wedge n$ folgt zusammen mit dem Lemma von Fatou
    $$h(y) = \liminf_{m \to \infty} h(y) \wedge m \geq \liminf_{m \to \infty}
    \liminf_{n \to \infty} \mathbb{E}_{y}[h(X_{S_{A} \wedge n}) \wedge m]$$
    $$\geq \mathbb{E}_{y}[h(X_{S_{A}})\mathbbm{1}_{S_{A} < \infty}] \geq \inf_{z \in A} h(z) \mathbb{P}_{y}[S_{A} < \infty]$$
    Also,
    $$\mathbb{P}_{y}[S_{A}< \infty] \leq \dfrac{h(y)}{\inf_{z \in A} h(z)} < 1$$
    Zusammen mit Lemma $\ref{Px[SA < unendlich] < 1, so y transient}$ a)
    folgt somit, dass jeder Zustand in E transient ist.

-   : Für jedes $c \geq 0$ gilt
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in \lbrace h \leq c \rbrace$\
    \
    Aus der Irreduziblität folgt zunächst einmal, dass für jedes
    $c \geq 0$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] < 1 \qquad \forall x \in \lbrace h \leq c \rbrace$$
    Folglich existiert zu jedem $x \in \lbrace h \leq c \rbrace$ ein
    $N_{x} \in \mathbb{N}$ und $\epsilon_{x} > 0$ so, dass
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon_{x} \qquad n \geq N_{x}$$
    Setze
    $N := \max {\lbrace N_{x} \: : \: x \in {\lbrace h \leq c \rbrace}  \rbrace}$
    und
    $\epsilon := \min \lbrace \epsilon_{x} \: : \: x \in \lbrace h \leq c \rbrace \rbrace$.
    Da nach Voraussetzungen die Menge $\lbrace h \leq c \rbrace$ endlich
    ist für jedes $c \geq 0$, folgt $N < \infty$, $\epsilon > 0$ und
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon \quad \forall n \geq N \quad \mathrm{und} \quad x \in {\lbrace h \leq x \rbrace}$$
    Weiterhin gilt für jedes $k \in \mathbb{N}$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN]$$
    $$= \sum_{y \in {\lbrace h \leq c \rbrace}} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN \: | \: S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y] \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in {\lbrace h \leq c \rbrace}} \underbrace{\mathbb{P}_{y}[S_{\lbrace h > c \rbrace}> N]}_{\leq 1 - \epsilon} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\leq (1-\epsilon) \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N]$$
    Folglich ergibt sich induktiv, dass
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N] \leq (1-\epsilon)^{k}$
    für alle $k \in \mathbb{N}$ und $x \in \lbrace h \leq c \rbrace$.\
    Somit erhält man
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] = \limsup_{k \to \infty} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = kN] \leq \limsup_{k \to \infty} (1-\epsilon)^{k} = 0 \quad \forall x \in {\lbrace h > c \rbrace}$$
    :
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in A$\
    \
    Für jedes $c \geq 0$ gilt für die Stoppzeit
    $S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}] \leq n < \infty$
    für alle $n \in \mathbb{N}$ und $x \in E$. Mit der Dynkin-Formel
    (Satz $\ref{Dynkin-Formel}$) angewendet auf
    $T=S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$ und
    $f = h \wedge m$ folgt zusammen mit dem Lemma von Fatou
    $$h(x) = \liminf_{m \to \infty} h(x) \wedge m$$
    $$\geq \liminf_{m \to \infty} \liminf_{n \to \infty} \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} ) \wedge m] \geq \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} )]$$
    Daraus folgt
    $$h(x) \geq \mathbb{E}_{x}[h(X_{S_{{\lbrace h > c \rbrace}}}) \mathbbm{1}_{S_{{\lbrace h > c \rbrace} < \infty}}\mathbbm{1}_{S_{{\lbrace A \rbrace} = \infty}}] \geq c \cdot \mathbb{P}_{x}[S_{{\lbrace h > c \rbrace}} < \infty, S_{{\lbrace h > c \rbrace}} = \infty]$$
    $$= c \cdot \mathbb{P}_{x}[S_{A} = \infty]$$ Da dies für jedes
    $c \geq 0$ gilt, folgt schließlich
    $$\mathbb{P}_{x}[S_{A} = \infty] \leq \limsup_{c \to \infty} \dfrac{h(x)}{c} = 0 \quad \Leftrightarrow \quad \mathbb{P}_{x}[S_{A} < \infty] = 1 \qquad \forall x \in E$$
    Folglich ist nach Lemma
    $\ref{Px[SA < unendlich] < 1, so y transient}$ b) jeder Zustand
    $y \in E$ rekurrent.

```{=html}
<!-- -->
```
-   Offensichtlich gilt für die Stoppzeit $S_{A} \wedge n$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n] \leq n$ für alle $x \in E$ und
    $n \in \mathbb{N}$. Aus der Dynkin-Formel(Satz
    $\ref{Dynkin-Formel}$) angewendet auf $T = S_{A} \wedge n$ und
    $f = h \wedge n$ folgt zusammen mit dem Lemma von Fatou
    $$h(y) = \liminf_{m \to \infty} h(y) \wedge m \geq \liminf_{m \to \infty}
    \liminf_{n \to \infty} \mathbb{E}_{y}[h(X_{S_{A} \wedge n}) \wedge m]$$
    $$\geq \mathbb{E}_{y}[h(X_{S_{A}})\mathbbm{1}_{S_{A} < \infty}] \geq \inf_{z \in A} h(z) \mathbb{P}_{y}[S_{A} < \infty]$$
    Also,
    $$\mathbb{P}_{y}[S_{A}< \infty] \leq \dfrac{h(y)}{\inf_{z \in A} h(z)} < 1$$
    Zusammen mit Lemma $\ref{Px[SA < unendlich] < 1, so y transient}$ a)
    folgt somit, dass jeder Zustand in E transient ist.

-   : Für jedes $c \geq 0$ gilt
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in \lbrace h \leq c \rbrace$\
    \
    Aus der Irreduziblität folgt zunächst einmal, dass für jedes
    $c \geq 0$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] < 1 \qquad \forall x \in \lbrace h \leq c \rbrace$$
    Folglich existiert zu jedem $x \in \lbrace h \leq c \rbrace$ ein
    $N_{x} \in \mathbb{N}$ und $\epsilon_{x} > 0$ so, dass
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon_{x} \qquad n \geq N_{x}$$
    Setze
    $N := \max {\lbrace N_{x} \: : \: x \in {\lbrace h \leq c \rbrace}  \rbrace}$
    und
    $\epsilon := \min \lbrace \epsilon_{x} \: : \: x \in \lbrace h \leq c \rbrace \rbrace$.
    Da nach Voraussetzungen die Menge $\lbrace h \leq c \rbrace$ endlich
    ist für jedes $c \geq 0$, folgt $N < \infty$, $\epsilon > 0$ und
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon \quad \forall n \geq N \quad \mathrm{und} \quad x \in {\lbrace h \leq x \rbrace}$$
    Weiterhin gilt für jedes $k \in \mathbb{N}$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN]$$
    $$= \sum_{y \in {\lbrace h \leq c \rbrace}} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN \: | \: S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y] \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in {\lbrace h \leq c \rbrace}} \underbrace{\mathbb{P}_{y}[S_{\lbrace h > c \rbrace}> N]}_{\leq 1 - \epsilon} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\leq (1-\epsilon) \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N]$$
    Folglich ergibt sich induktiv, dass
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N] \leq (1-\epsilon)^{k}$
    für alle $k \in \mathbb{N}$ und $x \in \lbrace h \leq c \rbrace$.\
    Somit erhält man
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] = \limsup_{k \to \infty} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = kN] \leq \limsup_{k \to \infty} (1-\epsilon)^{k} = 0 \quad \forall x \in {\lbrace h > c \rbrace}$$
    :
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in A$\
    \
    Für jedes $c \geq 0$ gilt für die Stoppzeit
    $S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}] \leq n < \infty$
    für alle $n \in \mathbb{N}$ und $x \in E$. Mit der Dynkin-Formel
    (Satz $\ref{Dynkin-Formel}$) angewendet auf
    $T=S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$ und
    $f = h \wedge m$ folgt zusammen mit dem Lemma von Fatou
    $$h(x) = \liminf_{m \to \infty} h(x) \wedge m$$
    $$\geq \liminf_{m \to \infty} \liminf_{n \to \infty} \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} ) \wedge m] \geq \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} )]$$
    Daraus folgt
    $$h(x) \geq \mathbb{E}_{x}[h(X_{S_{{\lbrace h > c \rbrace}}}) \mathbbm{1}_{S_{{\lbrace h > c \rbrace} < \infty}}\mathbbm{1}_{S_{{\lbrace A \rbrace} = \infty}}] \geq c \cdot \mathbb{P}_{x}[S_{{\lbrace h > c \rbrace}} < \infty, S_{{\lbrace h > c \rbrace}} = \infty]$$
    $$= c \cdot \mathbb{P}_{x}[S_{A} = \infty]$$ Da dies für jedes
    $c \geq 0$ gilt, folgt schließlich
    $$\mathbb{P}_{x}[S_{A} = \infty] \leq \limsup_{c \to \infty} \dfrac{h(x)}{c} = 0 \quad \Leftrightarrow \quad \mathbb{P}_{x}[S_{A} < \infty] = 1 \qquad \forall x \in E$$
    Folglich ist nach Lemma
    $\ref{Px[SA < unendlich] < 1, so y transient}$ b) jeder Zustand
    $y \in E$ rekurrent.

**Beispiel 2.13**\[Einfache Irrfahrt auf $\mathbb{Z}$\] Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf $E = \mathbb{Z}$
mit folgendem Übergangsgraphen

. ![Einfache Irrfahrt auf $\mathbb{Z}$](einfache Irrfahrt auf Z "fig:")

Betrachte zunächst den Fall $p \neq \dfrac{1}{2}$. Dann gilt für
$h(x) = {\left(\dfrac{1-p}{p} \right)}^{x}$, $x \in E$
$$(Lh)(x) = p(h((x+1)-h(x)) + (1-p)(h(x-1)-h(x)) = h(x)(1-2p+(2p-1)) = 0$$
für alle $x \in E$. Wähle nun $A = \lbrace 0 \rbrace$ und $$y =
\begin{cases}
\: \: \:1 & , p > \dfrac{1}{2}\\
& \\
-1 & , p < \dfrac{1}{2}
\end{cases}$$ Dann gilt
$$(Lh)(x) = 0 \quad \forall \: x \in A^{C} \quad und \quad h(y) < h(0) = 1$$
Somit ist die Bedingung (LT) erfüllt. Da zudem
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, folgt aus Satz
$\ref{Folgerung Dynkin Formel, (LR), (LT)}$ a), dass jeder Zustand
transient ist.\
Im Falle $p = \dfrac{1}{2}$ betrachte die Funktion
$h(x) = \vert x \vert$. Dann gilt
$$(Lh)(x) = \dfrac{1}{2} (\vert x +1 \vert - \vert x \vert) + \dfrac{1}{2}(\vert x -1 \vert - \vert x \vert) =
\begin{cases}
0 & , x \neq 0\\

1 & , x = 0
\end{cases}$$ Wähle nun $A = \lbrace 0 \rbrace$. Dann gilt
$$(Lh)(x) = 0 \quad \forall \: x \in A^{C} \quad und \quad \vert \lbrace h \leq c\rbrace \vert < \infty \quad \forall \: c \geq 0.$$
Somit ist die Bedingung (LR) erfüllt. Da
$(X_{n})_{n \in \mathbb{N}_{0}}$ zudem irreduzibel ist, ist folglich
nach Satz $\ref{Folgerung Dynkin Formel, (LR), (LT)}$ b) jeder Zustand
rekurrent.
---
 title: "Beweis2_31"
 mathjax : true
---
-   Offensichtlich gilt für die Stoppzeit $S_{A} \wedge n$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n] \leq n$ für alle $x \in E$ und
    $n \in \mathbb{N}$. Aus der Dynkin-Formel(Satz
    $\ref{Dynkin-Formel}$) angewendet auf $T = S_{A} \wedge n$ und
    $f = h \wedge n$ folgt zusammen mit dem Lemma von Fatou
    $$h(y) = \liminf_{m \to \infty} h(y) \wedge m \geq \liminf_{m \to \infty}
    \liminf_{n \to \infty} \mathbb{E}_{y}[h(X_{S_{A} \wedge n}) \wedge m]$$
    $$\geq \mathbb{E}_{y}[h(X_{S_{A}})\mathbbm{1}_{S_{A} < \infty}] \geq \inf_{z \in A} h(z) \mathbb{P}_{y}[S_{A} < \infty]$$
    Also,
    $$\mathbb{P}_{y}[S_{A}< \infty] \leq \dfrac{h(y)}{\inf_{z \in A} h(z)} < 1$$
    Zusammen mit Lemma $\ref{Px[SA < unendlich] < 1, so y transient}$ a)
    folgt somit, dass jeder Zustand in E transient ist.

-   : Für jedes $c \geq 0$ gilt
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in \lbrace h \leq c \rbrace$\
    \
    Aus der Irreduziblität folgt zunächst einmal, dass für jedes
    $c \geq 0$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] < 1 \qquad \forall x \in \lbrace h \leq c \rbrace$$
    Folglich existiert zu jedem $x \in \lbrace h \leq c \rbrace$ ein
    $N_{x} \in \mathbb{N}$ und $\epsilon_{x} > 0$ so, dass
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon_{x} \qquad n \geq N_{x}$$
    Setze
    $N := \max {\lbrace N_{x} \: : \: x \in {\lbrace h \leq c \rbrace}  \rbrace}$
    und
    $\epsilon := \min \lbrace \epsilon_{x} \: : \: x \in \lbrace h \leq c \rbrace \rbrace$.
    Da nach Voraussetzungen die Menge $\lbrace h \leq c \rbrace$ endlich
    ist für jedes $c \geq 0$, folgt $N < \infty$, $\epsilon > 0$ und
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon \quad \forall n \geq N \quad \mathrm{und} \quad x \in {\lbrace h \leq x \rbrace}$$
    Weiterhin gilt für jedes $k \in \mathbb{N}$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN]$$
    $$= \sum_{y \in {\lbrace h \leq c \rbrace}} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN \: | \: S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y] \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in {\lbrace h \leq c \rbrace}} \underbrace{\mathbb{P}_{y}[S_{\lbrace h > c \rbrace}> N]}_{\leq 1 - \epsilon} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\leq (1-\epsilon) \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N]$$
    Folglich ergibt sich induktiv, dass
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N] \leq (1-\epsilon)^{k}$
    für alle $k \in \mathbb{N}$ und $x \in \lbrace h \leq c \rbrace$.\
    Somit erhält man
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] = \limsup_{k \to \infty} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = kN] \leq \limsup_{k \to \infty} (1-\epsilon)^{k} = 0 \quad \forall x \in {\lbrace h > c \rbrace}$$
    :
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in A$\
    \
    Für jedes $c \geq 0$ gilt für die Stoppzeit
    $S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}] \leq n < \infty$
    für alle $n \in \mathbb{N}$ und $x \in E$. Mit der Dynkin-Formel
    (Satz $\ref{Dynkin-Formel}$) angewendet auf
    $T=S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$ und
    $f = h \wedge m$ folgt zusammen mit dem Lemma von Fatou
    $$h(x) = \liminf_{m \to \infty} h(x) \wedge m$$
    $$\geq \liminf_{m \to \infty} \liminf_{n \to \infty} \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} ) \wedge m] \geq \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} )]$$
    Daraus folgt
    $$h(x) \geq \mathbb{E}_{x}[h(X_{S_{{\lbrace h > c \rbrace}}}) \mathbbm{1}_{S_{{\lbrace h > c \rbrace} < \infty}}\mathbbm{1}_{S_{{\lbrace A \rbrace} = \infty}}] \geq c \cdot \mathbb{P}_{x}[S_{{\lbrace h > c \rbrace}} < \infty, S_{{\lbrace h > c \rbrace}} = \infty]$$
    $$= c \cdot \mathbb{P}_{x}[S_{A} = \infty]$$ Da dies für jedes
    $c \geq 0$ gilt, folgt schließlich
    $$\mathbb{P}_{x}[S_{A} = \infty] \leq \limsup_{c \to \infty} \dfrac{h(x)}{c} = 0 \quad \Leftrightarrow \quad \mathbb{P}_{x}[S_{A} < \infty] = 1 \qquad \forall x \in E$$
    Folglich ist nach Lemma
    $\ref{Px[SA < unendlich] < 1, so y transient}$ b) jeder Zustand
    $y \in E$ rekurrent.

```{=html}
<!-- -->
```
-   Offensichtlich gilt für die Stoppzeit $S_{A} \wedge n$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n] \leq n$ für alle $x \in E$ und
    $n \in \mathbb{N}$. Aus der Dynkin-Formel(Satz
    $\ref{Dynkin-Formel}$) angewendet auf $T = S_{A} \wedge n$ und
    $f = h \wedge n$ folgt zusammen mit dem Lemma von Fatou
    $$h(y) = \liminf_{m \to \infty} h(y) \wedge m \geq \liminf_{m \to \infty}
    \liminf_{n \to \infty} \mathbb{E}_{y}[h(X_{S_{A} \wedge n}) \wedge m]$$
    $$\geq \mathbb{E}_{y}[h(X_{S_{A}})\mathbbm{1}_{S_{A} < \infty}] \geq \inf_{z \in A} h(z) \mathbb{P}_{y}[S_{A} < \infty]$$
    Also,
    $$\mathbb{P}_{y}[S_{A}< \infty] \leq \dfrac{h(y)}{\inf_{z \in A} h(z)} < 1$$
    Zusammen mit Lemma $\ref{Px[SA < unendlich] < 1, so y transient}$ a)
    folgt somit, dass jeder Zustand in E transient ist.

-   : Für jedes $c \geq 0$ gilt
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in \lbrace h \leq c \rbrace$\
    \
    Aus der Irreduziblität folgt zunächst einmal, dass für jedes
    $c \geq 0$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] < 1 \qquad \forall x \in \lbrace h \leq c \rbrace$$
    Folglich existiert zu jedem $x \in \lbrace h \leq c \rbrace$ ein
    $N_{x} \in \mathbb{N}$ und $\epsilon_{x} > 0$ so, dass
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon_{x} \qquad n \geq N_{x}$$
    Setze
    $N := \max {\lbrace N_{x} \: : \: x \in {\lbrace h \leq c \rbrace}  \rbrace}$
    und
    $\epsilon := \min \lbrace \epsilon_{x} \: : \: x \in \lbrace h \leq c \rbrace \rbrace$.
    Da nach Voraussetzungen die Menge $\lbrace h \leq c \rbrace$ endlich
    ist für jedes $c \geq 0$, folgt $N < \infty$, $\epsilon > 0$ und
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon \quad \forall n \geq N \quad \mathrm{und} \quad x \in {\lbrace h \leq x \rbrace}$$
    Weiterhin gilt für jedes $k \in \mathbb{N}$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN]$$
    $$= \sum_{y \in {\lbrace h \leq c \rbrace}} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN \: | \: S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y] \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in {\lbrace h \leq c \rbrace}} \underbrace{\mathbb{P}_{y}[S_{\lbrace h > c \rbrace}> N]}_{\leq 1 - \epsilon} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\leq (1-\epsilon) \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N]$$
    Folglich ergibt sich induktiv, dass
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N] \leq (1-\epsilon)^{k}$
    für alle $k \in \mathbb{N}$ und $x \in \lbrace h \leq c \rbrace$.\
    Somit erhält man
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] = \limsup_{k \to \infty} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = kN] \leq \limsup_{k \to \infty} (1-\epsilon)^{k} = 0 \quad \forall x \in {\lbrace h > c \rbrace}$$
    :
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in A$\
    \
    Für jedes $c \geq 0$ gilt für die Stoppzeit
    $S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}] \leq n < \infty$
    für alle $n \in \mathbb{N}$ und $x \in E$. Mit der Dynkin-Formel
    (Satz $\ref{Dynkin-Formel}$) angewendet auf
    $T=S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$ und
    $f = h \wedge m$ folgt zusammen mit dem Lemma von Fatou
    $$h(x) = \liminf_{m \to \infty} h(x) \wedge m$$
    $$\geq \liminf_{m \to \infty} \liminf_{n \to \infty} \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} ) \wedge m] \geq \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} )]$$
    Daraus folgt
    $$h(x) \geq \mathbb{E}_{x}[h(X_{S_{{\lbrace h > c \rbrace}}}) \mathbbm{1}_{S_{{\lbrace h > c \rbrace} < \infty}}\mathbbm{1}_{S_{{\lbrace A \rbrace} = \infty}}] \geq c \cdot \mathbb{P}_{x}[S_{{\lbrace h > c \rbrace}} < \infty, S_{{\lbrace h > c \rbrace}} = \infty]$$
    $$= c \cdot \mathbb{P}_{x}[S_{A} = \infty]$$ Da dies für jedes
    $c \geq 0$ gilt, folgt schließlich
    $$\mathbb{P}_{x}[S_{A} = \infty] \leq \limsup_{c \to \infty} \dfrac{h(x)}{c} = 0 \quad \Leftrightarrow \quad \mathbb{P}_{x}[S_{A} < \infty] = 1 \qquad \forall x \in E$$
    Folglich ist nach Lemma
    $\ref{Px[SA < unendlich] < 1, so y transient}$ b) jeder Zustand
    $y \in E$ rekurrent.

**Beispiel 2.13**\[Einfache Irrfahrt auf $\mathbb{Z}$\] Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf $E = \mathbb{Z}$
mit folgendem Übergangsgraphen

. ![Einfache Irrfahrt auf $\mathbb{Z}$](einfache Irrfahrt auf Z "fig:")

Betrachte zunächst den Fall $p \neq \dfrac{1}{2}$. Dann gilt für
$h(x) = {\left(\dfrac{1-p}{p} \right)}^{x}$, $x \in E$
$$(Lh)(x) = p(h((x+1)-h(x)) + (1-p)(h(x-1)-h(x)) = h(x)(1-2p+(2p-1)) = 0$$
für alle $x \in E$. Wähle nun $A = \lbrace 0 \rbrace$ und $$y =
\begin{cases}
\: \: \:1 & , p > \dfrac{1}{2}\\
& \\
-1 & , p < \dfrac{1}{2}
\end{cases}$$ Dann gilt
$$(Lh)(x) = 0 \quad \forall \: x \in A^{C} \quad und \quad h(y) < h(0) = 1$$
Somit ist die Bedingung (LT) erfüllt. Da zudem
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, folgt aus Satz
$\ref{Folgerung Dynkin Formel, (LR), (LT)}$ a), dass jeder Zustand
transient ist.\
Im Falle $p = \dfrac{1}{2}$ betrachte die Funktion
$h(x) = \vert x \vert$. Dann gilt
$$(Lh)(x) = \dfrac{1}{2} (\vert x +1 \vert - \vert x \vert) + \dfrac{1}{2}(\vert x -1 \vert - \vert x \vert) =
\begin{cases}
0 & , x \neq 0\\

1 & , x = 0
\end{cases}$$ Wähle nun $A = \lbrace 0 \rbrace$. Dann gilt
$$(Lh)(x) = 0 \quad \forall \: x \in A^{C} \quad und \quad \vert \lbrace h \leq c\rbrace \vert < \infty \quad \forall \: c \geq 0.$$
Somit ist die Bedingung (LR) erfüllt. Da
$(X_{n})_{n \in \mathbb{N}_{0}}$ zudem irreduzibel ist, ist folglich
nach Satz $\ref{Folgerung Dynkin Formel, (LR), (LT)}$ b) jeder Zustand
rekurrent.

-   Offensichtlich gilt für die Stoppzeit $S_{A} \wedge n$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n] \leq n$ für alle $x \in E$ und
    $n \in \mathbb{N}$. Aus der Dynkin-Formel(Satz
    $\ref{Dynkin-Formel}$) angewendet auf $T = S_{A} \wedge n$ und
    $f = h \wedge n$ folgt zusammen mit dem Lemma von Fatou
    $$h(y) = \liminf_{m \to \infty} h(y) \wedge m \geq \liminf_{m \to \infty}
    \liminf_{n \to \infty} \mathbb{E}_{y}[h(X_{S_{A} \wedge n}) \wedge m]$$
    $$\geq \mathbb{E}_{y}[h(X_{S_{A}})\mathbbm{1}_{S_{A} < \infty}] \geq \inf_{z \in A} h(z) \mathbb{P}_{y}[S_{A} < \infty]$$
    Also,
    $$\mathbb{P}_{y}[S_{A}< \infty] \leq \dfrac{h(y)}{\inf_{z \in A} h(z)} < 1$$
    Zusammen mit Lemma $\ref{Px[SA < unendlich] < 1, so y transient}$ a)
    folgt somit, dass jeder Zustand in E transient ist.

-   : Für jedes $c \geq 0$ gilt
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in \lbrace h \leq c \rbrace$\
    \
    Aus der Irreduziblität folgt zunächst einmal, dass für jedes
    $c \geq 0$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] < 1 \qquad \forall x \in \lbrace h \leq c \rbrace$$
    Folglich existiert zu jedem $x \in \lbrace h \leq c \rbrace$ ein
    $N_{x} \in \mathbb{N}$ und $\epsilon_{x} > 0$ so, dass
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon_{x} \qquad n \geq N_{x}$$
    Setze
    $N := \max {\lbrace N_{x} \: : \: x \in {\lbrace h \leq c \rbrace}  \rbrace}$
    und
    $\epsilon := \min \lbrace \epsilon_{x} \: : \: x \in \lbrace h \leq c \rbrace \rbrace$.
    Da nach Voraussetzungen die Menge $\lbrace h \leq c \rbrace$ endlich
    ist für jedes $c \geq 0$, folgt $N < \infty$, $\epsilon > 0$ und
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > n] \leq 1 - \epsilon \quad \forall n \geq N \quad \mathrm{und} \quad x \in {\lbrace h \leq x \rbrace}$$
    Weiterhin gilt für jedes $k \in \mathbb{N}$
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN]$$
    $$= \sum_{y \in {\lbrace h \leq c \rbrace}} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace}> kN \: | \: S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y] \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in {\lbrace h \leq c \rbrace}} \underbrace{\mathbb{P}_{y}[S_{\lbrace h > c \rbrace}> N]}_{\leq 1 - \epsilon} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N, X_{(k-1)N}=y]$$
    $$\leq (1-\epsilon) \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N]$$
    Folglich ergibt sich induktiv, dass
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} > (k-1)N] \leq (1-\epsilon)^{k}$
    für alle $k \in \mathbb{N}$ und $x \in \lbrace h \leq c \rbrace$.\
    Somit erhält man
    $$\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = \infty] = \limsup_{k \to \infty} \mathbb{P}_{x}[S_{\lbrace h > c \rbrace} = kN] \leq \limsup_{k \to \infty} (1-\epsilon)^{k} = 0 \quad \forall x \in {\lbrace h > c \rbrace}$$
    :
    $\mathbb{P}_{x}[S_{\lbrace h > c \rbrace} < \infty] = 1 \quad \forall x \in A$\
    \
    Für jedes $c \geq 0$ gilt für die Stoppzeit
    $S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$, dass
    $\mathbb{E}_{x}[S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}] \leq n < \infty$
    für alle $n \in \mathbb{N}$ und $x \in E$. Mit der Dynkin-Formel
    (Satz $\ref{Dynkin-Formel}$) angewendet auf
    $T=S_{A} \wedge n \wedge S_{{\lbrace h > c \rbrace}}$ und
    $f = h \wedge m$ folgt zusammen mit dem Lemma von Fatou
    $$h(x) = \liminf_{m \to \infty} h(x) \wedge m$$
    $$\geq \liminf_{m \to \infty} \liminf_{n \to \infty} \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} ) \wedge m] \geq \mathbb{E}_{x}[h(X_{S_{A} \wedge n \wedge S_{\lbrace h > c \rbrace}} )]$$
    Daraus folgt
    $$h(x) \geq \mathbb{E}_{x}[h(X_{S_{{\lbrace h > c \rbrace}}}) \mathbbm{1}_{S_{{\lbrace h > c \rbrace} < \infty}}\mathbbm{1}_{S_{{\lbrace A \rbrace} = \infty}}] \geq c \cdot \mathbb{P}_{x}[S_{{\lbrace h > c \rbrace}} < \infty, S_{{\lbrace h > c \rbrace}} = \infty]$$
    $$= c \cdot \mathbb{P}_{x}[S_{A} = \infty]$$ Da dies für jedes
    $c \geq 0$ gilt, folgt schließlich
    $$\mathbb{P}_{x}[S_{A} = \infty] \leq \limsup_{c \to \infty} \dfrac{h(x)}{c} = 0 \quad \Leftrightarrow \quad \mathbb{P}_{x}[S_{A} < \infty] = 1 \qquad \forall x \in E$$
    Folglich ist nach Lemma
    $\ref{Px[SA < unendlich] < 1, so y transient}$ b) jeder Zustand
    $y \in E$ rekurrent.

**Beispiel 2.13**\[Einfache Irrfahrt auf $\mathbb{Z}$\] Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf $E = \mathbb{Z}$
mit folgendem Übergangsgraphen

. ![Einfache Irrfahrt auf $\mathbb{Z}$](einfache Irrfahrt auf Z "fig:")

Betrachte zunächst den Fall $p \neq \dfrac{1}{2}$. Dann gilt für
$h(x) = {\left(\dfrac{1-p}{p} \right)}^{x}$, $x \in E$
$$(Lh)(x) = p(h((x+1)-h(x)) + (1-p)(h(x-1)-h(x)) = h(x)(1-2p+(2p-1)) = 0$$
für alle $x \in E$. Wähle nun $A = \lbrace 0 \rbrace$ und $$y =
\begin{cases}
\: \: \:1 & , p > \dfrac{1}{2}\\
& \\
-1 & , p < \dfrac{1}{2}
\end{cases}$$ Dann gilt
$$(Lh)(x) = 0 \quad \forall \: x \in A^{C} \quad und \quad h(y) < h(0) = 1$$
Somit ist die Bedingung (LT) erfüllt. Da zudem
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, folgt aus Satz
$\ref{Folgerung Dynkin Formel, (LR), (LT)}$ a), dass jeder Zustand
transient ist.\
Im Falle $p = \dfrac{1}{2}$ betrachte die Funktion
$h(x) = \vert x \vert$. Dann gilt
$$(Lh)(x) = \dfrac{1}{2} (\vert x +1 \vert - \vert x \vert) + \dfrac{1}{2}(\vert x -1 \vert - \vert x \vert) =
\begin{cases}
0 & , x \neq 0\\

1 & , x = 0
\end{cases}$$ Wähle nun $A = \lbrace 0 \rbrace$. Dann gilt
$$(Lh)(x) = 0 \quad \forall \: x \in A^{C} \quad und \quad \vert \lbrace h \leq c\rbrace \vert < \infty \quad \forall \: c \geq 0.$$
Somit ist die Bedingung (LR) erfüllt. Da
$(X_{n})_{n \in \mathbb{N}_{0}}$ zudem irreduzibel ist, ist folglich
nach Satz $\ref{Folgerung Dynkin Formel, (LR), (LT)}$ b) jeder Zustand
rekurrent.

**Beispiel 2.13**\[Einfache, symmetrische Irrfahrt auf $\mathbb{Z}^{d}$,
$d \geq 3$\] Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf
$E = \mathbb{Z}^{d}$, $d \geq 3$ mit folgender
Übergangswahrscheinlichkeiten $$p(x,y)=
\begin{cases}
\dfrac{1}{2d} & ,  \vert \vert x - y \vert \vert = 1\\
0 & , sonst
\end{cases}$$ Betrachte nun die Funktion $h(0)=1$ und
$h(x)= {\vert \vert x \vert \vert}_{2}^{-\alpha}, \: x \neq 0$. Dann
gilt für jedes $x \in \mathbb{Z}^{d}$ mit
${\vert \vert x \vert \vert}_{2} > 1$ und $e \in \mathbb{Z}^{d}$ mit
${\vert \vert e \vert \vert}_{2} = 1$
$$h(x+e) - h(x) = h(x)\left(\left(\dfrac{{\vert \vert x + e \vert \vert}_{2}^{2}}{{\vert \vert x \vert \vert}_{2}^{2}}\right)^{-\alpha} - 1 \right) = h(x)\left(\left( 1 + \dfrac{{2\langle x,e \rangle + 1}}{{\vert \vert x \vert \vert}_{2}^{2}}\right)^{-\alpha} - 1 \right)$$
$$= h(x)\left(1 - \alpha \dfrac{{2\langle x,e \rangle + 1}}{{\vert \vert x \vert \vert}_{2}^{2} } + 2\alpha(\alpha + 1)\dfrac{{{\langle x,e \rangle}^{2}}}{{\vert \vert x \vert \vert}_{2}^{4} } + \mathcal{O}({\vert \vert x \vert \vert}_{2}^{-3}) - 1 \right)$$
wobei die Taylorentwicklung der Funktion
$f(z)=(1+z)^{-\alpha}= 1 - \alpha z + \dfrac{1}{2} \alpha(\alpha +1)z^{2} + \mathcal{O}({\vert z \vert}^{3})$
benutzt wurde. Da zudem gilt
$$\sum_{{\vert \vert e \vert \vert}_{2} = 1} 1 = 2d, \quad \sum_{{\vert \vert e \vert \vert}_{2} = 1} \langle x,e \rangle = 0 \quad und \quad \sum_{{\vert \vert e \vert \vert}_{2} = 1} {\langle x,e \rangle}^{2} = 2 {\vert \vert x \vert \vert}_{2}^{2}$$
folgt
$$\sum_{{\vert \vert e \vert \vert}_{2} = 1} \dfrac{1}{2d} \left(h(x+e) - h(x)\right) = \dfrac{1}{2d}h(x)(-2 \alpha d {\vert \vert x \vert \vert}_{2}^{-2} + 4 \alpha (\alpha + 1){\vert \vert x \vert \vert}_{2}^{-2} + \mathcal{O}({\vert \vert x \vert \vert}_{2}^{-3}) )$$
$$= \dfrac{\alpha}{d} {\vert \vert x \vert \vert}_{2}^{-2 \alpha - 2} (2(\alpha + 1) - d + \mathcal{O}({\vert \vert x \vert \vert}_{2}^{-1}))$$
Daraus folgt für $d \geq 3$ $\alpha \in \left(0,\dfrac{d-2}{2}\right)$
und
$A := \lbrace x \: : \: {\vert \vert x \vert \vert}_{2} \leq r \rbrace$
für ein hinreichend großes $r>0$, dass
$$(Lh)(x) \leq 0 \quad \forall \: x \in A^{C} \quad und \quad h(y) < \inf_{z \in A} h(z) \quad für \: ein \: y \: mit \: {\vert \vert y \vert \vert}_{2} > 2r.$$
Da $(X_{n})_{n \in \mathbb{N}_{0}}$ zudem irreduzibel ist, folgt aus
Satz $\ref{Folgerung Dynkin Formel, (LR), (LT)}$ a), dass die einfache,
symmetrische Irrfahrt auf $E = \mathbb{Z}^{d}$ für jedes $d \geq 3$
transient ist.

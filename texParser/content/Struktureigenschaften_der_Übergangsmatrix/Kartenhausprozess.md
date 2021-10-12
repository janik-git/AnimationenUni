---
 title: "Kartenhausprozess"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette mit Zustandsraum
$E = \mathbb{N}_{0}$, dessen Übergangsmatrix $P = (p(x,y))_{x,y \in E}$
durch folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph des
Kartenhausprozesses](Beispiel_Kartenhausprozess "fig:")

[Frage?]{style="color: red"} Unter welchen Bedingungen an
$(p_{i})_{i \in \mathbb{N}_{0}}$ ist der Zustand $x=0$ rekurrent?\
\
Da es für jedes $n \in \mathbb{N}$ genau einen Pfad gibt, der bei Start
in $x=0$ nach genau n-Schritten wieder in 0 trifft (nämlich
$(X_{0},X_{1},...,X_{n}) = (0,1,2,...,n-1,0)$) folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = (1-p_{0}) \cdot ... \cdot (1-p_{n-2}) \cdot p_{n-1} \: , \quad n \in \mathbb{N}$$
Setze nun $u_{0} := 1$ und
$u_{n} = (1-p_{0}) \cdot ... \cdot (1-p_{n-1})$, $\:$
$n \in \mathbb{N}$. Dann gilt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = u_{n-1} - u_{n}$$ Daraus
folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} < \infty] = \lim_{N \to \infty} \sum_{n=1}^{N} \mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = \lim_{N \to \infty}(1-u_{N}) = 1 - \lim_{N \to \infty } \prod_{n=0}^{N-1}  (1 - p_{n})$$
[Beh.]{.ul}: Falls $p_{i} \in (0,1)$ für alle $i \in \mathbb{N}_{0}$ so
gilt
$$\lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = 0 \quad \Leftrightarrow \quad \sum_{n=0}^{\infty} p_{n} = \infty$$
$"\Leftarrow"$ Da $e^{-x} \geq 1-x$ für alle $x \geq 0$, folgt
$$0 \leq \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) \leq \lim_{N \to \infty} exp(-\sum_{n=0}^{N}p_{n}) \stackrel{\sum_{n=0}^{\infty}p_{n} = \infty}{=} 0$$
$"\Rightarrow"$ $\dashuline{zu \: zeigen}:$ Für jedes
$m \in \mathbb{N}_{0}$ gilt
$\prod_{n=m}^{m+N}(1-p_{n}) \geq 1 - \sum_{n=m}^{m+N}p_{n}$,
$\forall N \in \mathbb{N}_{0}$\
\
**IA** $N=0$: $\checkmark$\
\
**IS** $N \to N+1$: Es gilt nun aber
$$\prod_{n=m}^{m+N+1} (1-p_{n}) \stackrel{\mathrm{IV}}{\geq} (1 - \sum_{n=m}^{m+N}p_{n})(1-p_{m+N+1}) = 1 - p_{m+N+1} - (\underbrace{1-p_{m+N+1}}_{\leq 1}) \cdot \sum_{n=m}^{m+N}p_{n} \geq 1 - \sum_{n=m}^{m+N+1} p_{n}$$
Angenommen $\sum_{n=0}^{\infty}p_{n} < \infty$. Dann existiert ein
$m \in \mathbb{N}$ so, dass $0 < \sum_{n=m}^{\infty} p_{n} < 1$.\
Daraus folgt
$$0 = \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = \prod_{n=0}^{m-1} (1-p_{n})  \lim_{N \to \infty} \prod_{n=m}^{N} (1-p_{n}) \geq \prod_{n=0}^{m-1} (1-p_{n}) \cdot (1 - \underbrace{\sum_{n=m}^{\infty} p_{n}}_{<1}) > 0 \: \: \lightning$$
Folglich ist $\sum_{n=0}^{\infty} p_{n} = \infty$.
---
 title: "Kartenhausprozess"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette mit Zustandsraum
$E = \mathbb{N}_{0}$, dessen Übergangsmatrix $P = (p(x,y))_{x,y \in E}$
durch folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph des
Kartenhausprozesses](Beispiel_Kartenhausprozess "fig:")

[Frage?]{style="color: red"} Unter welchen Bedingungen an
$(p_{i})_{i \in \mathbb{N}_{0}}$ ist der Zustand $x=0$ rekurrent?\
\
Da es für jedes $n \in \mathbb{N}$ genau einen Pfad gibt, der bei Start
in $x=0$ nach genau n-Schritten wieder in 0 trifft (nämlich
$(X_{0},X_{1},...,X_{n}) = (0,1,2,...,n-1,0)$) folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = (1-p_{0}) \cdot ... \cdot (1-p_{n-2}) \cdot p_{n-1} \: , \quad n \in \mathbb{N}$$
Setze nun $u_{0} := 1$ und
$u_{n} = (1-p_{0}) \cdot ... \cdot (1-p_{n-1})$, $\:$
$n \in \mathbb{N}$. Dann gilt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = u_{n-1} - u_{n}$$ Daraus
folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} < \infty] = \lim_{N \to \infty} \sum_{n=1}^{N} \mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = \lim_{N \to \infty}(1-u_{N}) = 1 - \lim_{N \to \infty } \prod_{n=0}^{N-1}  (1 - p_{n})$$
[Beh.]{.ul}: Falls $p_{i} \in (0,1)$ für alle $i \in \mathbb{N}_{0}$ so
gilt
$$\lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = 0 \quad \Leftrightarrow \quad \sum_{n=0}^{\infty} p_{n} = \infty$$
$"\Leftarrow"$ Da $e^{-x} \geq 1-x$ für alle $x \geq 0$, folgt
$$0 \leq \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) \leq \lim_{N \to \infty} exp(-\sum_{n=0}^{N}p_{n}) \stackrel{\sum_{n=0}^{\infty}p_{n} = \infty}{=} 0$$
$"\Rightarrow"$ $\dashuline{zu \: zeigen}:$ Für jedes
$m \in \mathbb{N}_{0}$ gilt
$\prod_{n=m}^{m+N}(1-p_{n}) \geq 1 - \sum_{n=m}^{m+N}p_{n}$,
$\forall N \in \mathbb{N}_{0}$\
\
**IA** $N=0$: $\checkmark$\
\
**IS** $N \to N+1$: Es gilt nun aber
$$\prod_{n=m}^{m+N+1} (1-p_{n}) \stackrel{\mathrm{IV}}{\geq} (1 - \sum_{n=m}^{m+N}p_{n})(1-p_{m+N+1}) = 1 - p_{m+N+1} - (\underbrace{1-p_{m+N+1}}_{\leq 1}) \cdot \sum_{n=m}^{m+N}p_{n} \geq 1 - \sum_{n=m}^{m+N+1} p_{n}$$
Angenommen $\sum_{n=0}^{\infty}p_{n} < \infty$. Dann existiert ein
$m \in \mathbb{N}$ so, dass $0 < \sum_{n=m}^{\infty} p_{n} < 1$.\
Daraus folgt
$$0 = \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = \prod_{n=0}^{m-1} (1-p_{n})  \lim_{N \to \infty} \prod_{n=m}^{N} (1-p_{n}) \geq \prod_{n=0}^{m-1} (1-p_{n}) \cdot (1 - \underbrace{\sum_{n=m}^{\infty} p_{n}}_{<1}) > 0 \: \: \lightning$$
Folglich ist $\sum_{n=0}^{\infty} p_{n} = \infty$.Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette mit Zustandsraum
$E = \mathbb{N}_{0}$, dessen Übergangsmatrix $P = (p(x,y))_{x,y \in E}$
durch folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph des
Kartenhausprozesses](Beispiel_Kartenhausprozess "fig:")

[Frage?]{style="color: red"} Unter welchen Bedingungen an
$(p_{i})_{i \in \mathbb{N}_{0}}$ ist der Zustand $x=0$ rekurrent?\
\
Da es für jedes $n \in \mathbb{N}$ genau einen Pfad gibt, der bei Start
in $x=0$ nach genau n-Schritten wieder in 0 trifft (nämlich
$(X_{0},X_{1},...,X_{n}) = (0,1,2,...,n-1,0)$) folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = (1-p_{0}) \cdot ... \cdot (1-p_{n-2}) \cdot p_{n-1} \: , \quad n \in \mathbb{N}$$
Setze nun $u_{0} := 1$ und
$u_{n} = (1-p_{0}) \cdot ... \cdot (1-p_{n-1})$, $\:$
$n \in \mathbb{N}$. Dann gilt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = u_{n-1} - u_{n}$$ Daraus
folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} < \infty] = \lim_{N \to \infty} \sum_{n=1}^{N} \mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = \lim_{N \to \infty}(1-u_{N}) = 1 - \lim_{N \to \infty } \prod_{n=0}^{N-1}  (1 - p_{n})$$
[Beh.]{.ul}: Falls $p_{i} \in (0,1)$ für alle $i \in \mathbb{N}_{0}$ so
gilt
$$\lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = 0 \quad \Leftrightarrow \quad \sum_{n=0}^{\infty} p_{n} = \infty$$
$"\Leftarrow"$ Da $e^{-x} \geq 1-x$ für alle $x \geq 0$, folgt
$$0 \leq \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) \leq \lim_{N \to \infty} exp(-\sum_{n=0}^{N}p_{n}) \stackrel{\sum_{n=0}^{\infty}p_{n} = \infty}{=} 0$$
$"\Rightarrow"$ $\dashuline{zu \: zeigen}:$ Für jedes
$m \in \mathbb{N}_{0}$ gilt
$\prod_{n=m}^{m+N}(1-p_{n}) \geq 1 - \sum_{n=m}^{m+N}p_{n}$,
$\forall N \in \mathbb{N}_{0}$\
\
**IA** $N=0$: $\checkmark$\
\
**IS** $N \to N+1$: Es gilt nun aber
$$\prod_{n=m}^{m+N+1} (1-p_{n}) \stackrel{\mathrm{IV}}{\geq} (1 - \sum_{n=m}^{m+N}p_{n})(1-p_{m+N+1}) = 1 - p_{m+N+1} - (\underbrace{1-p_{m+N+1}}_{\leq 1}) \cdot \sum_{n=m}^{m+N}p_{n} \geq 1 - \sum_{n=m}^{m+N+1} p_{n}$$
Angenommen $\sum_{n=0}^{\infty}p_{n} < \infty$. Dann existiert ein
$m \in \mathbb{N}$ so, dass $0 < \sum_{n=m}^{\infty} p_{n} < 1$.\
Daraus folgt
$$0 = \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = \prod_{n=0}^{m-1} (1-p_{n})  \lim_{N \to \infty} \prod_{n=m}^{N} (1-p_{n}) \geq \prod_{n=0}^{m-1} (1-p_{n}) \cdot (1 - \underbrace{\sum_{n=m}^{\infty} p_{n}}_{<1}) > 0 \: \: \lightning$$
Folglich ist $\sum_{n=0}^{\infty} p_{n} = \infty$.

**Beispiel 2.11**\[Einfache Irrfahrt auf $\mathbb{Z}$\] Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf $E=\mathbb{Z}$ mit
folgendem Übergangsgraphen:

. ![Einfache Irrfahrt auf
$\mathbb{Z}$](Beispiel_Einfache_Irrfahrt_auf_Z "fig:")

Dann gilt $p_{2n+1}(0,0) = 0$ für jedes $n \in \mathbb{N}_{0}$ und
$p_{2n}(0,0) = \binom{2n}{n} p^{n} (1-p)^{n}$ für jedes
$n \in \mathbb{N}$. Aus der Stirlingformel
$$n! \sim \sqrt{2 \pi n} \cdot n^{n} e^{-n} \qquad (a_{n} \sim b_{n} :\Leftrightarrow \lim_{n \to \infty} \dfrac{a_{n}}{b_{n}} = 1)$$
folgt dann
$$p_{2n}(0,0) = \dfrac{(2n)!}{(n!)^{2}} \cdot p^{n}(1-p)^{n} \sim \dfrac{\sqrt{4 \pi n}}{2 \pi n} \dfrac{(2n)^{2n}}{n^{2n}} \cdot p^{n} (1-p)^{n} = \dfrac{1}{\sqrt{\pi n}} (4p(1-p))^{n}$$
[1.Fall]{.ul}: $p=\dfrac{1}{2}$ $\:$ $\Rightarrow$ $\:$ $p_{2n}(0,0)$
$\sim$ $\dfrac{1}{\sqrt{\pi n}}$ $\:$ $\Rightarrow$ $\:$ $\exists$
$n_{0} \in \mathbb{N} \: : \: p_{2n}(0,0) \geq \dfrac{1}{2\sqrt{n}}$
$\:$ $\forall n \geq n_{0}$\
Also
$$\sum_{n=1}^{\infty} p_{n}(0,0) \geq \sum_{n=n_{0}}^{\infty}p_{2n}(0,0) \geq \dfrac{1}{2} \sum_{n=n_{0}}^{\infty}\dfrac{1}{\sqrt{n}} = \infty$$
Aus Satz $\ref{alternative Chrakterisierung von rekurrent/transient}$
folgt somit, dass $x=0$ rekurrent ist.\
\
[2.Fall]{.ul}: $p \neq \dfrac{1}{2}$ $\:$ $\Rightarrow$ $\:$
$4p(1-p) =: r < 1$ $\:$ $\Rightarrow$ $\:$ $\exists$
$n_{0} \in \mathbb{N} \: : \: p_{2n}(0,0) \leq r^{n}$ $\:$
$\forall n \geq n_{0}$\
Also,
$$\sum_{n=1}^{\infty} p_{n}(0,0) = \sum_{n=1}^{\infty} p_{2n}(0,0) \leq n_{0} + \sum_{n=n_{0}}^{\infty} r^{n} < \infty$$
Aus Satz $\ref{alternative Chrakterisierung von rekurrent/transient}$
folgt somit, dass $x=0$ transient ist.
---
 title: "Kartenhausprozess"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette mit Zustandsraum
$E = \mathbb{N}_{0}$, dessen Übergangsmatrix $P = (p(x,y))_{x,y \in E}$
durch folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph des
Kartenhausprozesses](Beispiel_Kartenhausprozess "fig:")

[Frage?]{style="color: red"} Unter welchen Bedingungen an
$(p_{i})_{i \in \mathbb{N}_{0}}$ ist der Zustand $x=0$ rekurrent?\
\
Da es für jedes $n \in \mathbb{N}$ genau einen Pfad gibt, der bei Start
in $x=0$ nach genau n-Schritten wieder in 0 trifft (nämlich
$(X_{0},X_{1},...,X_{n}) = (0,1,2,...,n-1,0)$) folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = (1-p_{0}) \cdot ... \cdot (1-p_{n-2}) \cdot p_{n-1} \: , \quad n \in \mathbb{N}$$
Setze nun $u_{0} := 1$ und
$u_{n} = (1-p_{0}) \cdot ... \cdot (1-p_{n-1})$, $\:$
$n \in \mathbb{N}$. Dann gilt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = u_{n-1} - u_{n}$$ Daraus
folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} < \infty] = \lim_{N \to \infty} \sum_{n=1}^{N} \mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = \lim_{N \to \infty}(1-u_{N}) = 1 - \lim_{N \to \infty } \prod_{n=0}^{N-1}  (1 - p_{n})$$
[Beh.]{.ul}: Falls $p_{i} \in (0,1)$ für alle $i \in \mathbb{N}_{0}$ so
gilt
$$\lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = 0 \quad \Leftrightarrow \quad \sum_{n=0}^{\infty} p_{n} = \infty$$
$"\Leftarrow"$ Da $e^{-x} \geq 1-x$ für alle $x \geq 0$, folgt
$$0 \leq \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) \leq \lim_{N \to \infty} exp(-\sum_{n=0}^{N}p_{n}) \stackrel{\sum_{n=0}^{\infty}p_{n} = \infty}{=} 0$$
$"\Rightarrow"$ $\dashuline{zu \: zeigen}:$ Für jedes
$m \in \mathbb{N}_{0}$ gilt
$\prod_{n=m}^{m+N}(1-p_{n}) \geq 1 - \sum_{n=m}^{m+N}p_{n}$,
$\forall N \in \mathbb{N}_{0}$\
\
**IA** $N=0$: $\checkmark$\
\
**IS** $N \to N+1$: Es gilt nun aber
$$\prod_{n=m}^{m+N+1} (1-p_{n}) \stackrel{\mathrm{IV}}{\geq} (1 - \sum_{n=m}^{m+N}p_{n})(1-p_{m+N+1}) = 1 - p_{m+N+1} - (\underbrace{1-p_{m+N+1}}_{\leq 1}) \cdot \sum_{n=m}^{m+N}p_{n} \geq 1 - \sum_{n=m}^{m+N+1} p_{n}$$
Angenommen $\sum_{n=0}^{\infty}p_{n} < \infty$. Dann existiert ein
$m \in \mathbb{N}$ so, dass $0 < \sum_{n=m}^{\infty} p_{n} < 1$.\
Daraus folgt
$$0 = \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = \prod_{n=0}^{m-1} (1-p_{n})  \lim_{N \to \infty} \prod_{n=m}^{N} (1-p_{n}) \geq \prod_{n=0}^{m-1} (1-p_{n}) \cdot (1 - \underbrace{\sum_{n=m}^{\infty} p_{n}}_{<1}) > 0 \: \: \lightning$$
Folglich ist $\sum_{n=0}^{\infty} p_{n} = \infty$.Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette mit Zustandsraum
$E = \mathbb{N}_{0}$, dessen Übergangsmatrix $P = (p(x,y))_{x,y \in E}$
durch folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph des
Kartenhausprozesses](Beispiel_Kartenhausprozess "fig:")

[Frage?]{style="color: red"} Unter welchen Bedingungen an
$(p_{i})_{i \in \mathbb{N}_{0}}$ ist der Zustand $x=0$ rekurrent?\
\
Da es für jedes $n \in \mathbb{N}$ genau einen Pfad gibt, der bei Start
in $x=0$ nach genau n-Schritten wieder in 0 trifft (nämlich
$(X_{0},X_{1},...,X_{n}) = (0,1,2,...,n-1,0)$) folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = (1-p_{0}) \cdot ... \cdot (1-p_{n-2}) \cdot p_{n-1} \: , \quad n \in \mathbb{N}$$
Setze nun $u_{0} := 1$ und
$u_{n} = (1-p_{0}) \cdot ... \cdot (1-p_{n-1})$, $\:$
$n \in \mathbb{N}$. Dann gilt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = u_{n-1} - u_{n}$$ Daraus
folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} < \infty] = \lim_{N \to \infty} \sum_{n=1}^{N} \mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = \lim_{N \to \infty}(1-u_{N}) = 1 - \lim_{N \to \infty } \prod_{n=0}^{N-1}  (1 - p_{n})$$
[Beh.]{.ul}: Falls $p_{i} \in (0,1)$ für alle $i \in \mathbb{N}_{0}$ so
gilt
$$\lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = 0 \quad \Leftrightarrow \quad \sum_{n=0}^{\infty} p_{n} = \infty$$
$"\Leftarrow"$ Da $e^{-x} \geq 1-x$ für alle $x \geq 0$, folgt
$$0 \leq \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) \leq \lim_{N \to \infty} exp(-\sum_{n=0}^{N}p_{n}) \stackrel{\sum_{n=0}^{\infty}p_{n} = \infty}{=} 0$$
$"\Rightarrow"$ $\dashuline{zu \: zeigen}:$ Für jedes
$m \in \mathbb{N}_{0}$ gilt
$\prod_{n=m}^{m+N}(1-p_{n}) \geq 1 - \sum_{n=m}^{m+N}p_{n}$,
$\forall N \in \mathbb{N}_{0}$\
\
**IA** $N=0$: $\checkmark$\
\
**IS** $N \to N+1$: Es gilt nun aber
$$\prod_{n=m}^{m+N+1} (1-p_{n}) \stackrel{\mathrm{IV}}{\geq} (1 - \sum_{n=m}^{m+N}p_{n})(1-p_{m+N+1}) = 1 - p_{m+N+1} - (\underbrace{1-p_{m+N+1}}_{\leq 1}) \cdot \sum_{n=m}^{m+N}p_{n} \geq 1 - \sum_{n=m}^{m+N+1} p_{n}$$
Angenommen $\sum_{n=0}^{\infty}p_{n} < \infty$. Dann existiert ein
$m \in \mathbb{N}$ so, dass $0 < \sum_{n=m}^{\infty} p_{n} < 1$.\
Daraus folgt
$$0 = \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = \prod_{n=0}^{m-1} (1-p_{n})  \lim_{N \to \infty} \prod_{n=m}^{N} (1-p_{n}) \geq \prod_{n=0}^{m-1} (1-p_{n}) \cdot (1 - \underbrace{\sum_{n=m}^{\infty} p_{n}}_{<1}) > 0 \: \: \lightning$$
Folglich ist $\sum_{n=0}^{\infty} p_{n} = \infty$.

**Beispiel 2.11**\[Einfache Irrfahrt auf $\mathbb{Z}$\] Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf $E=\mathbb{Z}$ mit
folgendem Übergangsgraphen:

. ![Einfache Irrfahrt auf
$\mathbb{Z}$](Beispiel_Einfache_Irrfahrt_auf_Z "fig:")

Dann gilt $p_{2n+1}(0,0) = 0$ für jedes $n \in \mathbb{N}_{0}$ und
$p_{2n}(0,0) = \binom{2n}{n} p^{n} (1-p)^{n}$ für jedes
$n \in \mathbb{N}$. Aus der Stirlingformel
$$n! \sim \sqrt{2 \pi n} \cdot n^{n} e^{-n} \qquad (a_{n} \sim b_{n} :\Leftrightarrow \lim_{n \to \infty} \dfrac{a_{n}}{b_{n}} = 1)$$
folgt dann
$$p_{2n}(0,0) = \dfrac{(2n)!}{(n!)^{2}} \cdot p^{n}(1-p)^{n} \sim \dfrac{\sqrt{4 \pi n}}{2 \pi n} \dfrac{(2n)^{2n}}{n^{2n}} \cdot p^{n} (1-p)^{n} = \dfrac{1}{\sqrt{\pi n}} (4p(1-p))^{n}$$
[1.Fall]{.ul}: $p=\dfrac{1}{2}$ $\:$ $\Rightarrow$ $\:$ $p_{2n}(0,0)$
$\sim$ $\dfrac{1}{\sqrt{\pi n}}$ $\:$ $\Rightarrow$ $\:$ $\exists$
$n_{0} \in \mathbb{N} \: : \: p_{2n}(0,0) \geq \dfrac{1}{2\sqrt{n}}$
$\:$ $\forall n \geq n_{0}$\
Also
$$\sum_{n=1}^{\infty} p_{n}(0,0) \geq \sum_{n=n_{0}}^{\infty}p_{2n}(0,0) \geq \dfrac{1}{2} \sum_{n=n_{0}}^{\infty}\dfrac{1}{\sqrt{n}} = \infty$$
Aus Satz $\ref{alternative Chrakterisierung von rekurrent/transient}$
folgt somit, dass $x=0$ rekurrent ist.\
\
[2.Fall]{.ul}: $p \neq \dfrac{1}{2}$ $\:$ $\Rightarrow$ $\:$
$4p(1-p) =: r < 1$ $\:$ $\Rightarrow$ $\:$ $\exists$
$n_{0} \in \mathbb{N} \: : \: p_{2n}(0,0) \leq r^{n}$ $\:$
$\forall n \geq n_{0}$\
Also,
$$\sum_{n=1}^{\infty} p_{n}(0,0) = \sum_{n=1}^{\infty} p_{2n}(0,0) \leq n_{0} + \sum_{n=n_{0}}^{\infty} r^{n} < \infty$$
Aus Satz $\ref{alternative Chrakterisierung von rekurrent/transient}$
folgt somit, dass $x=0$ transient ist.Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette mit Zustandsraum
$E = \mathbb{N}_{0}$, dessen Übergangsmatrix $P = (p(x,y))_{x,y \in E}$
durch folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph des
Kartenhausprozesses](Beispiel_Kartenhausprozess "fig:")

[Frage?]{style="color: red"} Unter welchen Bedingungen an
$(p_{i})_{i \in \mathbb{N}_{0}}$ ist der Zustand $x=0$ rekurrent?\
\
Da es für jedes $n \in \mathbb{N}$ genau einen Pfad gibt, der bei Start
in $x=0$ nach genau n-Schritten wieder in 0 trifft (nämlich
$(X_{0},X_{1},...,X_{n}) = (0,1,2,...,n-1,0)$) folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = (1-p_{0}) \cdot ... \cdot (1-p_{n-2}) \cdot p_{n-1} \: , \quad n \in \mathbb{N}$$
Setze nun $u_{0} := 1$ und
$u_{n} = (1-p_{0}) \cdot ... \cdot (1-p_{n-1})$, $\:$
$n \in \mathbb{N}$. Dann gilt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = u_{n-1} - u_{n}$$ Daraus
folgt
$$\mathbb{P}_{0} [S_{\lbrace 0 \rbrace} < \infty] = \lim_{N \to \infty} \sum_{n=1}^{N} \mathbb{P}_{0} [S_{\lbrace 0 \rbrace} = n] = \lim_{N \to \infty}(1-u_{N}) = 1 - \lim_{N \to \infty } \prod_{n=0}^{N-1}  (1 - p_{n})$$
[Beh.]{.ul}: Falls $p_{i} \in (0,1)$ für alle $i \in \mathbb{N}_{0}$ so
gilt
$$\lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = 0 \quad \Leftrightarrow \quad \sum_{n=0}^{\infty} p_{n} = \infty$$
$"\Leftarrow"$ Da $e^{-x} \geq 1-x$ für alle $x \geq 0$, folgt
$$0 \leq \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) \leq \lim_{N \to \infty} exp(-\sum_{n=0}^{N}p_{n}) \stackrel{\sum_{n=0}^{\infty}p_{n} = \infty}{=} 0$$
$"\Rightarrow"$ $\dashuline{zu \: zeigen}:$ Für jedes
$m \in \mathbb{N}_{0}$ gilt
$\prod_{n=m}^{m+N}(1-p_{n}) \geq 1 - \sum_{n=m}^{m+N}p_{n}$,
$\forall N \in \mathbb{N}_{0}$\
\
**IA** $N=0$: $\checkmark$\
\
**IS** $N \to N+1$: Es gilt nun aber
$$\prod_{n=m}^{m+N+1} (1-p_{n}) \stackrel{\mathrm{IV}}{\geq} (1 - \sum_{n=m}^{m+N}p_{n})(1-p_{m+N+1}) = 1 - p_{m+N+1} - (\underbrace{1-p_{m+N+1}}_{\leq 1}) \cdot \sum_{n=m}^{m+N}p_{n} \geq 1 - \sum_{n=m}^{m+N+1} p_{n}$$
Angenommen $\sum_{n=0}^{\infty}p_{n} < \infty$. Dann existiert ein
$m \in \mathbb{N}$ so, dass $0 < \sum_{n=m}^{\infty} p_{n} < 1$.\
Daraus folgt
$$0 = \lim_{N \to \infty} \prod_{n=0}^{N} (1-p_{n}) = \prod_{n=0}^{m-1} (1-p_{n})  \lim_{N \to \infty} \prod_{n=m}^{N} (1-p_{n}) \geq \prod_{n=0}^{m-1} (1-p_{n}) \cdot (1 - \underbrace{\sum_{n=m}^{\infty} p_{n}}_{<1}) > 0 \: \: \lightning$$
Folglich ist $\sum_{n=0}^{\infty} p_{n} = \infty$.

**Beispiel 2.11**\[Einfache Irrfahrt auf $\mathbb{Z}$\] Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf $E=\mathbb{Z}$ mit
folgendem Übergangsgraphen:

. ![Einfache Irrfahrt auf
$\mathbb{Z}$](Beispiel_Einfache_Irrfahrt_auf_Z "fig:")

Dann gilt $p_{2n+1}(0,0) = 0$ für jedes $n \in \mathbb{N}_{0}$ und
$p_{2n}(0,0) = \binom{2n}{n} p^{n} (1-p)^{n}$ für jedes
$n \in \mathbb{N}$. Aus der Stirlingformel
$$n! \sim \sqrt{2 \pi n} \cdot n^{n} e^{-n} \qquad (a_{n} \sim b_{n} :\Leftrightarrow \lim_{n \to \infty} \dfrac{a_{n}}{b_{n}} = 1)$$
folgt dann
$$p_{2n}(0,0) = \dfrac{(2n)!}{(n!)^{2}} \cdot p^{n}(1-p)^{n} \sim \dfrac{\sqrt{4 \pi n}}{2 \pi n} \dfrac{(2n)^{2n}}{n^{2n}} \cdot p^{n} (1-p)^{n} = \dfrac{1}{\sqrt{\pi n}} (4p(1-p))^{n}$$
[1.Fall]{.ul}: $p=\dfrac{1}{2}$ $\:$ $\Rightarrow$ $\:$ $p_{2n}(0,0)$
$\sim$ $\dfrac{1}{\sqrt{\pi n}}$ $\:$ $\Rightarrow$ $\:$ $\exists$
$n_{0} \in \mathbb{N} \: : \: p_{2n}(0,0) \geq \dfrac{1}{2\sqrt{n}}$
$\:$ $\forall n \geq n_{0}$\
Also
$$\sum_{n=1}^{\infty} p_{n}(0,0) \geq \sum_{n=n_{0}}^{\infty}p_{2n}(0,0) \geq \dfrac{1}{2} \sum_{n=n_{0}}^{\infty}\dfrac{1}{\sqrt{n}} = \infty$$
Aus Satz $\ref{alternative Chrakterisierung von rekurrent/transient}$
folgt somit, dass $x=0$ rekurrent ist.\
\
[2.Fall]{.ul}: $p \neq \dfrac{1}{2}$ $\:$ $\Rightarrow$ $\:$
$4p(1-p) =: r < 1$ $\:$ $\Rightarrow$ $\:$ $\exists$
$n_{0} \in \mathbb{N} \: : \: p_{2n}(0,0) \leq r^{n}$ $\:$
$\forall n \geq n_{0}$\
Also,
$$\sum_{n=1}^{\infty} p_{n}(0,0) = \sum_{n=1}^{\infty} p_{2n}(0,0) \leq n_{0} + \sum_{n=n_{0}}^{\infty} r^{n} < \infty$$
Aus Satz $\ref{alternative Chrakterisierung von rekurrent/transient}$
folgt somit, dass $x=0$ transient ist.

**Beispiel 2.11**\[einefache, symmterische Irrfahrt auf
$\mathbb{Z}^{2}$\] Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette
auf $E=\mathbb{Z}^2$ mit
$p(x,y)=\dfrac{1}{4} \mathbbm{1}_{\vert \vert x-y \vert \vert = 1}$.
Zunächst einmal ist $p_{2n+1}(0,0)=0$ für alle $n \mathbb{N}_{0}$. Um in
2n Schritten nach $x=0$ zurückzukehren muss
$(X_{n})_{n \in \mathbb{N}_{0}}$ gleich oft (k-Mal) nach rechts bzw.
links und gleich oft ((n-k)-Mal) nach oben bzw. unten gelaufen sein.
Daraus folgt
$$p_{2n}(0,0) = 4^{-2n} \sum_{k=0}^{n} \dfrac{(2n)!}{(k!)^{2}((n-k)!)^{2}} = 4^{-2n} \binom{2n}{n} \underbrace{\sum_{k=0}^{n} \binom{n}{k} \binom{n}{n-k}}_{= \binom{2n}{n}} = ({\underbrace{\binom{2n}{n} 2^{-n}}_{\sim \dfrac{1}{\sqrt{\pi n}}}})^{2} \sim \dfrac{1}{\pi n}$$
Also existiert wiederum ein $n_{0} \in \mathbb{N}$ mit
$p_{2n}(0,0) \geq \dfrac{1}{4n}$ für alle $n \geq n_{0}$. Daraus folgt
$$\sum_{n=1}^{\infty} p_{n}(0,0) \geq \sum_{n = n_{0}}^{\infty} p_{2n}(0,0) \geq \dfrac{1}{4} \sum_{n = n_{0}}^{\infty} \dfrac{1}{n} = \infty$$
$\Rightarrow$ x=0 ist rekurrent.

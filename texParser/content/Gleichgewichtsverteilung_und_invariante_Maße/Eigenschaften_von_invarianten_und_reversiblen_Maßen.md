---
 title: "Eigenschaften_von_invarianten_und_reversiblen_Maßen"
 mathjax : true
---
**Definition 3.1**\[invariantes Maß, Gleichgewichtsverteilung\] Sei
$P = (p(x,y))_{x,y \in E}$ eine stochastische Matrix. Ein Maß $\pi$ auf
E heißt invariantes Maß bezüglich P, falls
$$\pi (x) = (\pi P)(x) = \sum_{y \in E} \pi (y) p(y,x)$$ Falls $\pi$
invariant und eine Verteilung ist, d.h. $\pi[E] = 1$, so nennt man $\pi$
eine Gleichgewichtsverteilung (oder invariante Verteilung). Bezeichne
mit
$$Inv(P) := \lbrace \pi \: : \: E \to [0,1] \: : \: \pi P = \pi \: und \: \pi[E] = 1 \rbrace$$
die Menge der Gleichgewichtsverteilungen.

**Bemerkung 3.20**

[\[Auflistende Bemerkung zu invarianten Maßen\]]{#Auflistende Bemerkung zu invarianten Maßen
label="Auflistende Bemerkung zu invarianten Maßen"}

-   Ein invariantes Maß $\pi : \: E \to [0,1]$ ist als Zeilenvektor
    $(\pi \in [0,\infty]^{E})$ aufgefasst ein (nichtnegativer)
    Linkseigenvektor von $P$ zum Eigenwert 1.

-   Ist $\vert E \vert < \infty$, so kann jedes invariantes Maß zu einer
    Gleichgewichtsverteilung normiert werden.

-   Ist $\pi$ ein invariantes Maß bzgl. $P$, so gilt $\pi = \pi P^{n}$
    für jedes $n \in \mathbb{N}_{0}$. Falls $P$ zudem irreduzibel und
    $\pi \neq 0$ ist, so folgt $$\pi(x) > 0 \qquad \forall \: x \in E.$$
    Da nämlich $\pi \neq 0$, gibt es ein $z \in E$ mit $\pi (z) > 0$.
    Aus der Irreduzibilität von $P$ folgt weiterhin, dass zu jedem
    $x \in E \setminus \lbrace z \rbrace$ ein $n \in \mathbb{N}$
    existiert mit $p_{n}(z,x)>0$. Also,
    $$\pi (x) = (\pi P^{n})(x) = \sum_{y \in E} \pi (y) p_{n} (y,x) \geq
    \underbrace{\pi (z)}_{>0} \underbrace{ p_{n} (z,x)}_{>0} > 0.$$

-   Ist $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette mit
    Zustandsraum E und Übergangsmatrix $P$. Wenn $\pi$ eine
    Gleichgewichtsverteilung ist, so gilt für jedes
    $n \in \mathbb{N}_{0}$
    $$\mathbb{P}_{\pi}[X_{n} = x] = \sum_{y \in E} \pi (y) \mathbb{P}_{y}[X_{n} = x] = \sum_{y \in E} \pi (y) p_{n}(y,x) = \pi (x).$$
    Insbesondere ist
    $$\mathbb{P}_{\pi} [X_{k+1} = x_{1},...,X_{k+n} = x_{n}] = \sum_{y \in E} \mathbb{P}_{\pi} [X_{k} = y] \mathbb{P}_{\pi} [X_{k+1} = x_{1},...,X_{k+n} = x_{n} \: | \: X_{k} = y]$$
    $$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in E} \pi (y)  \mathbb{P}_{y} [X_{1} = x_{1},...,X_{n} = x_{n}]$$
    $$\mathbb{P}_{\pi} [X_{1} = x_{1},...,X_{n} = x_{n}]$$

-   Für $\pi_{1}, \pi_{2} \in Inv(P)$ und $\lambda \in [0,1]$ gilt
    $(\lambda \pi_{1} + (1- \lambda) \pi_{2})[E] = \lambda + (1-\lambda)=1$
    und
    $$(\lambda \pi_{1} + (1- \lambda) \pi_{2})P = \lambda \pi_{1}P + (1- \lambda) \pi_{2}P = \lambda \pi_{1} + (1- \lambda) \pi_{2}.$$
    Folglich ist die Menge $Inv(P)$ der Gleichgewichtsverteilungen
    konvex.

**Beispiel 3.15** Sei $E = \lbrace 1,2 \rbrace$ und $$P=
\begin{bmatrix}
 1- \alpha & \alpha \\
 \beta & 1-\beta \\
\end{bmatrix}
\qquad mit \quad \alpha , \beta \in [0,1].$$ Dann ist für
$\alpha + \beta \neq 0$ die Gleichgewichtsverteilung $\pi$ gegeben durch
$$\pi(1) = \dfrac{\beta}{\alpha + \beta } \quad und \quad \pi(2) = \dfrac{\alpha}{\alpha + \beta }$$
Für $\alpha = \beta = 0$ gilt
$$Inv(P) = \lbrace \lambda \cdot \mathbbm{1}_{\lbrace 1 \rbrace} + (1-\lambda) \cdot \mathbbm{1}_{\lbrace 2 \rbrace} \: : \: \lambda \in [0,1] \rbrace.$$

**Beispiel 3.15**\[Irrfahrt auf dem Torus\] Sei
$E = (\mathbb{Z}/N \mathbb{Z})^{d}$ für $N \geq 2$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf E mit
Übergangswahrscheinlichkeit $p(x,y) = \mu (y-x)$ für ein
Wahrscheinlichkeitsmaß $\mu$ auf E. Dann ist
$\pi(x) = N^{-d}, \: x \in E$ eine Gleichgewichtsverteilung, denn
$$\sum_{y \in E} \pi(y)p(x,y) = N^{-d} \sum_{y \in E} \mu (y-x) = N^{-d} \sum_{y \in E} \mu (y) =  N^{-d} = \pi (x) \qquad \forall \: x \in E.$$

**Beispiel 3.15** Sei $E= (\mathbb{Z} / (2N)\mathbb{N})$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Irrfahrt auf E mit $$p(x,y)=
\begin{cases}
p & , y = (x+2) \: mod \: 2N  \\
1-p & , y = (x-2) \: mod \: 2N 
\end{cases} 
\qquad p \in (0,1)$$ Bezeichne mit
$$G := \lbrace 2k \: : \: k \in \mathbb{N}_{0} \rbrace \cap E \quad und \quad U := \lbrace 2k +1 \: : \: k \in \mathbb{N}_{0} \rbrace \cap E$$
und setze für $\lambda \in [0,1]$
$$\pi_{\lambda}(x) := \dfrac{\lambda}{N}\mathbbm{1}_{G}(x) + \dfrac{1-\lambda}{N}\mathbbm{1}_{U}(x) \qquad, x \in E$$
Dann gilt
$$\sum_{y \in E} \pi_{\lambda}(y)p(y,x) = \dfrac{\lambda}{N} \sum_{y \in G} p(y,x) + \dfrac{1-\lambda}{N} \sum_{y \in U} p(y,x)$$
$$= \dfrac{\lambda}{N}\mathbbm{1}_{G}(x)(1-p+p) + \dfrac{1-\lambda}{N}\mathbbm{1}_{U}(x)(1-p+p) = \pi_{\lambda}(x)$$
für alle $x \in E$. Folglich ist $\pi_{\lambda} \in Inv(P)$ für alle
$\lambda \in [0,1]$, d.h. $\vert Inv(P) \vert = \infty$. Beachte, dass
die stochastische Matrix $P$ nicht irreduzibel ist und zwei
kommunizierenden Klassen besitzt, nämlich die Menge G und U.

**Satz 3.18**
[\[höchstens eine Gleichverteilung\]]{#höchstens eine Gleichverteilung
label="höchstens eine Gleichverteilung"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E.

-   Falls $(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, so gilt
    $\vert Inv(P) \vert \in \lbrace 0,1 \rbrace$. D.h. es gibt höchstens
    eine Gleichgewichtsverteilung.

-   Falls $(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel und transient
    ist, so gilt $Inv(P) = \emptyset$. D.h. es gibt keine
    Gleichgewichtsverteilung.

**Beweis 3.36**

-   Definiere $\bar{P} = (\bar{p}(x,y))_{x,y \in E}$ durch
    $\bar{p}(x,y) := \sum_{n=1}^{\infty} 2^{-n} p_{n}(x,y) \:, \quad x,y \in E$.
    Dann ist $\bar{P}$ eine stochastische Matrix, denn für alle
    $x \in E$ gilt
    $$\sum_{y \in E} \bar{p} (x,y) \stackrel{\mathrm{Fubini}}{=} \sum_{n=1}^{\infty} 2^{-n} \sum_{y \in E} p_{n}(x,y) = \sum_{n=1}^{\infty} 2^{-n} = 1$$
    Da P nach Voraussetzungen irreduzibel ist, folgt $\bar{p}(x,y)>0$
    für alle $x,y \in E$. Angenommen es gäbe zwei
    Gleichgewichtsverteilungen $\pi_{1},\pi_{2} \in Inv(P)$ mit
    $\pi_{1} \neq \pi_{2}$. Da
    $$(\pi_{i} \bar{P})(x) = \sum_{y \in E} \pi_{i}(y) \bar{p}(y,x) \stackrel{\mathrm{Fubini}}{=} \sum_{n=1}^{\infty} 2^{-n} \sum_{y \in E} \pi_{i} p(y,x) = \pi_{i}(x) \sum_{n=1}^{\infty} 2^{-n} = \pi_{i}(x)$$
    für alle $x \in E$ und $i \in \lbrace 1,2 \rbrace$, ist
    $\pi_{1}, \pi_{2} \in Inv(\bar{P})$. Betrachte nun das signierte Maß
    $$\bar{\pi} := \pi_{1} - \pi_{2}.$$ Dann gilt
    $\bar{\pi} \bar{P} = \pi_{1} \bar{P} - \pi_{2} \bar{P} = \pi_{1} - \pi_{2} = \bar{\pi}$.
    Da $\bar{\pi} \neq 0$ und $\bar{\pi}[E]=0$ existieren $x,y \in E$
    mit $\bar{\pi}(x) > 0$ und $\bar{\pi}(y) < 0$. Weiterhin gilt
    $$\sum_{z \in E} \vert \bar{\pi}(z) \vert = \sum_{z \in E} \vert (\bar{\pi}\bar{P})(z) \vert$$
    $$= \sum_{z \in E}\vert \underbrace{\bar{\pi}(x)\bar{p}(x,z)}_{>0} + \underbrace{\bar{\pi}(y)\bar{p}(y,z)}_{<0} +  \sum_{\substack{ z' \in E \\ z' \neq x,y } }\bar{\pi}(z')\bar{p}(z',z) \vert$$
    $$< \sum_{z \in E} \sum_{z' \in E} \vert \bar{\pi}(z') \vert \bar{p}(z',z)$$
    $$= \sum_{z' \in E} \vert \bar{\pi}(z') \vert \quad \lightning$$
    Folglich ist $\bar{\pi}=0$, d.h. $\pi_{1} = \pi_{2}$.

-   Angenommen $Inv(P) \neq \emptyset$, d.h. es gibt eine
    Gleichgewichtsverteilung $\pi$. Nach Voraussetzung ist jeder Zustand
    $y \in E$ transient. Also folgt aus dem Korollar
    $\ref{transienter Zustand dann lim n -> unendl. pn(x,y) = 0}$ und
    dem Satz von Lebesgue
    $$0 = \sum_{x \in E} \pi (x) \lim_{n \to \infty}p_{n}(x,y) = \lim_{n \to \infty} \sum_{x \in E} \pi(x) p_{n}(x,y) = \pi(y) \qquad \forall \: y \in E$$\
    Also, $$\sum_{y \in E} \pi (y) = 0 \neq 1 \quad \lightning$$
    Folglich gibt es keine Gleichgewichtsverteilung.

**Beispiel 3.15**\[doppelt stochastische Übergangsmatrizen\]
[\[doppelt stochastische Übergangsmatrizen\]]{#doppelt stochastische Übergangsmatrizen
label="doppelt stochastische Übergangsmatrizen"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E, wobei die Übergangsmatrix $P$ folgende Eigenschaft
besitzt $$\sum_{y \in E} p(y,x) = 1 \qquad \forall \: x \in E,$$ d.h. P
ist doppelt stochastisch. Ein Spezialfall von doppelt stochastischen
Matrizen ist $$p(x,y) = \mu(y-x) \qquad, \quad x,y \in E$$ für ein
Wahrscheinlichkeitsmaß $\mu$ auf E. Dann ist $\pi(x) = 1$ für alle
$x \in E$ ein invariantes Maß, denn
$$\sum_{y \in E} \pi(y) p(y,x) \sum_{y \in E} p(y,x) = 1 = \pi(x) \qquad , \quad x \in E.$$

**Beispiel 3.15**\[Einfache, asymmetrische Irrfahrt auf $\mathbb{Z}$\]
[\[Einfache, asymmetrische Irrfahrt auf Z\]]{#Einfache, asymmetrische Irrfahrt auf Z
label="Einfache, asymmetrische Irrfahrt auf Z"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf $E=\mathbb{Z}$ mit
$p(x,x+1) = p$ und $p(x,x-1)=1-p$ für alle $x \in E$ und $p \in (0,1)$.
Nach Beispiel $\ref{doppelt stochastische Übergangsmatrizen}$ ist
$\pi(x) = 1$ für alle $x \in E$ ein invariantes Maß. Für
$p \neq \dfrac{1}{2}$ ist zudem
$\pi(x) = {\left( \dfrac{p}{1-p} \right)}^{x}$, $x \in E$ ein
invariantes Maß, denn
$$\sum_{y \in E} \pi(y) p(y,x) = \pi(x-1)p(x-1,x) + \pi(x+1)p(x+1,x)= {\left( \dfrac{p}{1-p} \right)}^{x}(1-p+p) = \pi(x)$$

**Satz 3.18** Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine irreduzible
$(\pi,P)$-Markovkette mit Zustandsraum E, wobei angenommen sei, dass die
Startverteilung $\pi$ invariant ist. Dann ist für jedes
$N \in \mathbb{N}_{0}$ der stochastische Prozess
$(Y_{n})_{0 \leq n \leq N}$ mit $Y_{n} := X_{N-n}$ eine
$(\pi,P^{*})$-Markovkette mit
$$p^{*}(x,y) := \dfrac{\pi (y) p(y,x)}{\pi(x)} \qquad \forall \: x,y \in E.$$
Die stochastische Matrix $P^{*}$ heißt auch duale Übergangsmatrix.

**Beweis 3.36** Da $P$ irreduzibel ist, ist nach Bemerkung
$\ref{Auflistende Bemerkung zu invarianten Maßen}$ c) $\pi(x) > 0$ für
alle $x \in E$. Somit sind die Matrixeinträge von $P^{*}$ wohldefiniert.
Zudem gilt
$$\sum_{y \in E} p^{*}(x,y) = \dfrac{1}{\pi (x)} \sum_{y \in E} \pi (y) p(y,x) = 1 \qquad \forall \: x \in E$$
d.h. $P^{*}$ ist eine stochastische Matrix. Aufgrund von Satz
$\ref{Besitzen Markovketten die Markoveigenschaft}$ (i) genügt es nun\
\
: $\: \forall \: n \in \lbrace 0,1,...,N \rbrace$ und
$y_{0},...,y_{n} \in E$ gilt
$$\mathbb{P}_{\pi} [Y_{0} = y_{0},...,Y_{n}=y_{n}] = \pi(y_{0})p^{*}(y_{0},y_{1}) \cdot ... \cdot p^{*}(y_{n-1},y_{n})$$
Für $n \in \lbrace 0,1,...,N \rbrace$ und $y_{0},...,y_{n} \in E$
betrachte nun
$$\mathbb{P}_{\pi} [Y_{0} = y_{0},...,Y_{n}=y_{n}] = \mathbb{P}_{\pi} [X_{N} = y_{0},...,X_{N-n}=y_{n}]$$
$$= \mathbb{P}_{\pi}[X_{N-n} = y_{n}] \mathbb{P}_{\pi} [X_{N} = y_{0},...,X_{N-n+1}=y_{n-1} \: | \: X_{N-n}=y_{n}]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \mathbb{P}_{\pi}[X_{N-n} = y_{n}] \mathbb{P}_{Y_{n}} [X_{n} = y_{0},...,X_{1}=y_{n-1}]$$
$$\stackrel{\mathrm{Satz} \: \ref{"Satz 1.8"}}{=} \underbrace{(\pi P^{N-n})}_{\pi}(y_{n}) \mathbb{P}_{Y_{n}} [X_{1} = y_{n-1},...,X_{n}=y_{0}]$$
$$\stackrel{\mathrm{Satz} \: \ref{Besitzen Markovketten die Markoveigenschaft}}{=} \pi(y_{n}) p(y_{n},y_{n-1}) \cdot ... \cdot p(y_{1},y_{0})$$
$$= \pi(y_{0})p^{*}(y_{0},y_{1}) \cdot ... \cdot p^{*}(y_{n-1},y_{n})$$
Somit ist nach Satz $\ref{Besitzen Markovketten die Markoveigenschaft}$
(i) $(Y_{n})_{0 \leq n \leq N}$ eine $(\pi,P^{*})$-Markovkette.

**Definition 3.1**\[reversibel\] Ein Maß $\pi$ auf E heißt reversibel
bezüglich einer stochastisch Matrix $P = (p(x,y))_{x,y \in E}$ falls die
sog. \"detailed balance\" Bedingung erfüllt ist:
$$\pi(x)p(x,y) = \pi(y)p(y,x) \qquad \forall \: x,y \in E$$ Eine
stochastische Matrix nennt man reversibel, falls ein bzg. P reversibles
Maß existiert.

**Erklärung 3.3** Anschaulich ist ein Prozess im detaillierten
Gleichgewicht, wenn nicht erkennbar ist, ob er sich zeitlich vorwärts
oder rückwärts bewegt.

**Bemerkung 3.20**

-   $\pi$ reversibel bzgl. P $\Rightarrow$ $\pi$ invariant bzgl. P

-   Falls P reversibel und irreduzibel ist, so ist $P = P*$

**Beispiel 3.15**\[Ehrenfest's Urnenmodell\] In zwei Urnen liegen N
Kugeln. Zu jedem Zeitpunkt $n \in \mathbb{N}$ wird eine Kugel zufällig
mit gleicher Wahrscheinlichkeit ausgewählt, die die Urne dann wechselt.
Die Anzahl der Kugeln in der ersten Urne wird durch die Markovkette
$(X_{n})_{n \in \mathbb{N}_{0}}$ mit Zustandsraum
$E = \lbrace 0,...,N \rbrace$ und Übergangswahrscheinlichkeiten
beschrieben: $$p(x,y)=
\begin{cases}
\dfrac{x}{N} & , y = x - 1 \: \wedge \: x \geq 1\\
 &  \\
1 - \dfrac{x}{N} & , y = x + 1 \: \wedge \: x \leq N - 1
\end{cases}$$ beschrieben.

. ![Die Ehrenfest'sche Urne mit n = 10 Kugeln. Im nächsten Schritt wird
mit Wahrscheinlichkeit $4/10$ eine Kugel von der linken Kammer in die
rechte und mit Wahrscheinlichkeit $6/10$ von der rechten in die linke
Kammer gelegt.](Ehrenfests Urnenmodell "fig:")

Sei $\pi(x) := 2^{-N} \binom{N}{x}$. Dann gilt für alle
$x \in \lbrace 0,...,N-1 \rbrace$
$$\pi(x)p(x,x+1) =  2^{-N} \binom{N}{x} \left( 1 - \dfrac{x}{N} \right) = 2^{-N} \dfrac{N!}{x!(N-x)!} \cdot \dfrac{N-x}{N}$$
$$= 2^{-N} \dfrac{(N-1)!}{x!(N-x-1)!} = 2^{-N} \dfrac{N!}{(x+1)!(N-(x+1))! } \cdot \dfrac{x+1}{N} = \pi(x+1)p(x+1,x)$$
Folglich ist $\pi$ ein bzgl. $P$ reversibles Wahrscheinlichkeitsmaß.

**Satz 3.18**\[Kolmogorov's Zykelbedingung\]
[\[Kolmogorov\'s Zykelbedingung\]]{#Kolmogorov's Zykelbedingung
label="Kolmogorov's Zykelbedingung"} Sei $P = (p(x,y))_{x,y \in E}$ eine
irreduzible, stochastische Matrix. Ein Maß $\pi$ auf E ist genau dann
reversibel bzgl. $P$, wenn

-   $p(x,y)>0 \quad \Rightarrow \quad p(y,x)>0 \qquad \forall \: x,y \in E$

-   für jeden Zykel $x_{0},x_{1},...,x_{n}$ mit $x_{n} = x_{0}$ und
    $\prod_{i=1}^{n} p(x_{i},x_{i-1})>0$ gilt
    $$\prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = 1$$

**Beweis 3.36** $"\Rightarrow"$ Da $\pi$ reversibel bzgl. $P$ ist, ist
folglich $\pi$ ein invariantes Maß. Da $P$ zudem irreduzibel ist, so
folgt aus Bemerkung $\ref{Auflistende Bemerkung zu invarianten Maßen}$
c), dass $\pi(x) > 0$ für alle $x \in E$\
\
: $p(x,y)>0 \quad \Rightarrow \quad p(y,x)>0$\
\
Sei also $p(x,y)>0$. Dann ergibt sich aus der \"detailed balance\"
$\:$Bedingung
$$p(y,x) = \dfrac{\pi(y)}{\pi(y)} p(y,x) = \underbrace{\dfrac{\pi(x)}{\pi(y)}}_{>0} \underbrace{p(x,y)}_{>0} > 0.$$
Betrachte nun $x_{0},...,x_{n} \in E$ mit $x_{n} = x_{0}$ und
$\prod_{i=1}^{n} p(x_{i},x_{i-1})>0$ .\
\
: $\prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = 1$\
\
Wiederum ergibt sich aus der \"detailed balance\" Bedingung
$$\prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = \prod_{i=1}^{n} \dfrac{\pi(x_{i-1})}{\pi(x_{i-1})} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = \prod_{i=1}^{n} \dfrac{\pi(x_{i})}{\pi(x_{i-1})} = \dfrac{\pi(x_{n})}{\pi(x_{0})} \stackrel{x_{0} = x_{n}}{=} 1$$
$"\Leftarrow"$ Für ein festes $z \in E$ setze $\pi(z) = 1$. Aus der
Irreduzibilität von $P$ folgt, dass zu jedem $x \in E$ ein
$n \in \mathbb{N}$ existiert mit $p_{n}(z,x) > 0$. Fo0lglich existieren
$x_{0},...,x_{n} \in E$ mit
$$x_{0} = z \quad, \: x_{n} = x \quad und  \quad \prod_{i=1}^{n} p(x_{i},x_{i-1})>0.$$
Definiere
$$\pi(x) = \prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})}$$\
\
: $\pi(x)$ ist unabhängig vom gewählten Pfad\
\
Sei $(x_{0}',...,x_{m}')$ ein weiterer Pfad in E mit
$x_{0}' = z, \: x_{m}' = x$ und $\prod_{j=1}^{m} p(x_{j}',x_{j-1}')>0$.
Dann folgt aus (i), dass auch $\prod_{j=1}^{m} p(x_{j-1}',x_{j}')>0$.
Setze $$(y_{0},...,y_{n+m}) = (x_{0},...,x_{n},x_{m-1}',...,x_{0}')$$
Dann gilt
$$y_{0} = y_{n+m} = z \quad und \quad \prod_{i=1}^{n+m} p(y_{i},y_{i-1}) \stackrel{x_{n}'=x_{n}}{=} \prod_{i=1}^{n} p(x_{i},x_{i-1})  \prod_{j=1}^{m} p(x_{j-1}',x_{j}')>0$$
Also folgt aus (ii)
$$\pi(x) = \prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = \prod_{j=1}^{m} \dfrac{p(x_{j-1}',x_{j}')}{p(x_{j}',x_{j-1}')} \cdot \underbrace{\prod_{i=1}^{n+m} \dfrac{p(y_{i-1},y_{i})}{p(y_{i},y_{i-1})}} _{=1} = \prod_{j=1}^{m} \dfrac{p(x_{j-1}',x_{j}')}{p(x_{j}',x_{j-1}')}$$
Folglich ist $\pi(x)$ unabhängig vom gewählten Pfad.\
\
: $\pi(x)p(x,y) = \pi(y) p(y,x)$\
\
Falls $p(x,y)=0$, so ist aufgrund von (i) auch $p(y,x)=0$ und die
Aussage ist trivial. sei nun also $p(x,y)>0$. Dann ist wegen (i) auch
$p(y,x)>0$. Zudem gilt
$$\pi(x)p(x,y) = \prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})}  \cdot p(x,y)$$
$$= \prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})}  \cdot \dfrac{p(x,y)}{p(y,x)} \cdot p(y,x) = \pi(y)p(y,x),$$
da mit $x_{n+1}:= y$ der Pfad $(x_{0},...,x_{n},x_{n+1})$ die
Eigenschaft hat, dass $x_{0} = z, \: x_{n+1} = y$ und
$\prod_{i=1}^{n+1} p(x_{i},x_{i-1})>0$.

**Beispiel 3.15**\[Geburts- und Todesprozess\] Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette auf
$E = \mathbb{N}_{0}$, dessen Übergangsmatrix $P$ durch folgenden
Übergangsgraphen beschrieben wird

. ![Übergangsgraph eines Geburts- und
Todesprozess](Geburts- und Todesprozess "fig:")

wobei angenommen sei, dass $q_{x} > 0$ für alle $x \in \mathbb{N}$.
Setze
$$\pi(0) := 1 \quad und \quad \pi(x) = \prod_{y=1}^{x} \dfrac{p_{y-1}}{q_{y}}, \quad x \in \mathbb{N}$$
Dann gilt
$$\pi(x-1)p(x-1,x) = \pi(x-1)p_{x-1} = \pi(x-1) \dfrac{p_{x-1}}{q_{x}}p(x,x-1) = \pi(x)p(x,x-1)$$
Folglich ist $\pi$ reversible bzgl. $P$ und insbesondere ein invariantes
Maß. Falls zudem gilt, dass
$$\sum_{x \in E} \pi(x) = \sum_{x \in E} \prod_{y=1}^{x} \dfrac{p_{y-1}}{q_{y}} < \infty$$
so lässt sich $\pi$ zu einer Gleichverteilung normieren.
[invariantes_Maß,_Gleichgewichtsverteilung](Gleichgewichtsverteilung_und_invariante_Maße/invariantes_Maß,_Gleichgewichtsverteilung.md)  
[Bemerkung3_18](Gleichgewichtsverteilung_und_invariante_Maße/Bemerkung3_18.md)  
[Beispiel3_13](Gleichgewichtsverteilung_und_invariante_Maße/Beispiel3_13.md)  
[Irrfahrt_auf_dem_Torus](Gleichgewichtsverteilung_und_invariante_Maße/Irrfahrt_auf_dem_Torus.md)  
[Beispiel3_14](Gleichgewichtsverteilung_und_invariante_Maße/Beispiel3_14.md)  
[Satz3_16](Gleichgewichtsverteilung_und_invariante_Maße/Satz3_16.md)  
[Beweis3_33](Gleichgewichtsverteilung_und_invariante_Maße/Beweis3_33.md)  
[doppelt_stochastische_Übergangsmatrizen](Gleichgewichtsverteilung_und_invariante_Maße/doppelt_stochastische_Übergangsmatrizen.md)  
[doppelt_stochastische_Übergangsmatrizen](Gleichgewichtsverteilung_und_invariante_Maße/doppelt_stochastische_Übergangsmatrizen.md)  
[Satz3_17](Gleichgewichtsverteilung_und_invariante_Maße/Satz3_17.md)  
[Beweis3_34](Gleichgewichtsverteilung_und_invariante_Maße/Beweis3_34.md)  
[reversibel](Gleichgewichtsverteilung_und_invariante_Maße/reversibel.md)  
[Erklärung3_2](Gleichgewichtsverteilung_und_invariante_Maße/Erklärung3_2.md)  
[Bemerkung3_19](Gleichgewichtsverteilung_und_invariante_Maße/Bemerkung3_19.md)  
[Ehrenfest_s_Urnenmodell](Gleichgewichtsverteilung_und_invariante_Maße/Ehrenfest_s_Urnenmodell.md)  
[Kolmogorov_s_Zykelbedingung](Gleichgewichtsverteilung_und_invariante_Maße/Kolmogorov_s_Zykelbedingung.md)  
[Beweis3_35](Gleichgewichtsverteilung_und_invariante_Maße/Beweis3_35.md)  
[Geburts-_und_Todesprozess](Gleichgewichtsverteilung_und_invariante_Maße/Geburts-_und_Todesprozess.md)  
[Satz3_18](Gleichgewichtsverteilung_und_invariante_Maße/Satz3_18.md)  
[Beweis3_36](Gleichgewichtsverteilung_und_invariante_Maße/Beweis3_36.md)  
[Bemerkung3_20](Gleichgewichtsverteilung_und_invariante_Maße/Bemerkung3_20.md)  
[Satz3_19](Gleichgewichtsverteilung_und_invariante_Maße/Satz3_19.md)  
[Beweis3_37](Gleichgewichtsverteilung_und_invariante_Maße/Beweis3_37.md)  
[Bemerkung3_21](Gleichgewichtsverteilung_und_invariante_Maße/Bemerkung3_21.md)  
[Satz3_20](Gleichgewichtsverteilung_und_invariante_Maße/Satz3_20.md)  
[Beweis3_38](Gleichgewichtsverteilung_und_invariante_Maße/Beweis3_38.md)  
[Korollar3_8](Gleichgewichtsverteilung_und_invariante_Maße/Korollar3_8.md)  
[Beweis3_39](Gleichgewichtsverteilung_und_invariante_Maße/Beweis3_39.md)  
[Beispiel3_15](Gleichgewichtsverteilung_und_invariante_Maße/Beispiel3_15.md)  

---
 title: "Stoppzeiten_und_starke_Markoveigenschaften"
 mathjax : true
---
[Frage?]{style="color: red"} Wie lassen sich zufällige Zeitpunkte
beschreiben? **Definition 2.1**\[erzeugte $\sigma$-Algebra\] Sei
$X=(X_{n})_{n \in \mathbb{N}_{0}}$ ein stochastischer Prozess auf
$(\Omega,\mathfrak{F},\mathbb{P})$ mit Werten in $(E,\epsilon)$. Setze
$$\mathfrak{F}_{n}^{X} := \sigma(X_{k} \: : \: k \in \lbrace 0,...,n \rbrace) := \lbrace (X_{0},...,X_{n})^{-1}(B) \: : \: B \in  \varepsilon^{ \otimes (n+1)} \rbrace, \qquad n \in \mathbb{N}_{0}$$
Dann heißt $(\mathfrak{F}_{n}^{X})_{n \in \mathbb{N}_{0}}$ die von X
erzeugte $\sigma$-Algebra.

***Erinnerung:** Sei $\Omega \neq \emptyset$, $(\Omega', \mathfrak{F}')$
und $X: \Omega \to \Omega'$ ein messbarer Raum. Dann ist
$$X^{-1}(\mathfrak{F}') := \lbrace X^{-1}(B) \: : B \in \mathfrak{F}' \rbrace$$
eine $\sigma$-Algebra. Zudem gilt für jedes System
$\mathcal{A}' \subseteq \mathfrak{F}'$
$$\sigma(X^{-1}(\mathcal{A}')) = X^{-1}(\sigma(\mathcal{A}'))$$*
**Bemerkung 2.11**

-   Es gilt
    $\mathfrak{F}_{m}^{X} \subseteq \mathfrak{F}_{n}^{X} \subseteq \mathfrak{F}$
    für alle $m,n \in \mathbb{N}_{0}$ mit $m<n$.

-   $\mathfrak{F}_{n}^{X}$ umfasst alle Informationen, die ein
    Beobachter von $X=(X_{n})_{n \in \mathbb{N}_{0}}$ bis zum Zeitpunkt
    n hat.

**Definition 2.1**\[Stoppzeit\] Sei $X= (X_{n})_{n \in \mathbb{N}_{0}}$
ein stochastischer Prozess auf $(\Omega,\mathfrak{F},\mathbb{P})$ mit
Werten in E. Eine Abbildung
$T: \Omega \to \mathbb{N}_{0} \cup \lbrace \infty \rbrace$ heißt
Stoppzeit bzgl. X, wenn gilt
$$\lbrace T = n \rbrace \in \sigma(X_{0},...,X_{n}) = \mathfrak{F}_{n}^{X}, \qquad n \in \mathbb{N}_{0}$$

**Bemerkung 2.11** Das Ereignis $\lbrace T = \infty \rbrace$ kann
interpretiert werden, dass die Stoppzeit nie eintritt.

**Beispiel 2.11** Sei $X=(X_{n})_{n \in \mathbb{N}_{0}}$ ein
stochastischer Prozess mit Zustandsraum E und $A \subseteq E$.

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

[Frage?]{style="color: red"} Wie kann man die
Eintrittswahrscheinlichkeit einer Markovkette in eine Menge A berechnen?
**Definition 2.1**\[Generator\] Sei P eine stochastische Matrix. Dann
nennt man $L := P-I$ den zugehörigen (diskreten) Generator, wobei mit I
die Einheitsmatrix gemeint ist.

**Definition 2.1**\[Dirichletproblem\] Sei
$\emptyset \neq A \subsetneq E$ und $g: A \to \mathbb{R}$. Dann heißt
das lineare Gleichungssystem $$(Lf)(x) = 0, \: x \in A^{C}$$

$$f(x) = g(x), \: x \in A$$ das zu L gehörige Dirichletproblem auf
$A^{C}$ mit Randwerten g auf A.

**Satz 2.6** [\[Dirichletsatz\]]{#Dirichletsatz label="Dirichletsatz"}
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E. Für $A \subsetneq E$ setze
$h_{A}(x) := \mathbb{P}_{x}[T_{A} < \infty]$. Dann ist $h_{A}$ die
kleinste Lösung des Dirichletproblems
$$(Lh_{A})(x) = 0, \: x \in A^{C}$$ $$h_{A}(x) = 1, \: x \in A$$

**Beweis 2.17** : $h_{A}$ ist eine Lösung des obigen Dirichletproblems.\
\
Da $\lbrace X_{0} \in A \rbrace = \lbrace T_{A} = 0 \rbrace$, ist
folglich $h_{A}(x) = 1$ für alle $x \in A$.\
Sei also nun $x \in A^{C}$. Dann folgt mit Satz
[\[vorangegangene und zukünftige Ereignisse\]](#vorangegangene und zukünftige Ereignisse){reference-type="ref"
reference="vorangegangene und zukünftige Ereignisse"}
$$\mathbb{P}_{x}[T_{A} < \infty] = \mathbb{P}_{x}[T_{A} \in \mathbb{N}] = \sum_{y \in E} \mathbb{P}_{x}[T_{A} \in \mathbb{N}, X_{1} = y]$$
$$= \sum_{y \in E} \mathbb{P}[X_{1} = y \: | \: X_{0} = x] \cdot \mathbb{P}_{\nu}[T_{A} \in \mathbb{N} \: | \: X_{0} = x, X_{1} = y]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[T_{A} \in \mathbb{N}_{0}]$$
Also,
$$h_{A}(x) = \mathbb{P}_{x}[T_{A} < \infty] = \sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[T_{A} \in \mathbb{N}_{0}] = \sum_{y \in E} p(x,y) \cdot h_{A}(y) \Leftrightarrow (Lh_{A})(x) = 0$$
: $h_{A}$ ist die kleinste, nichtnegative Lösung des folgenden
Dirichletproblems $$(Lh)(x) = 0, \: x \notin A$$
$$h(x) = 1, \: x \in A$$ : Für alle $N \in \mathbb{N}_{0}$ gilt
$\mathbb{P}_{x}[T_{A} \leq N] \leq h(x)$, $x \in E$\
\
Für jedes $N \in \mathbb{N}_{0}$ und $x \in A$ folgt
$P_{x}[T_{A} \leq N] = 1 = h(x)$. Für jedes $x \in A^{C}$ ergibt sich
mittels vollständiger Induktion über N\
\
**IA** $N=0$:
$\mathbb{P}_{x}[T_{A} = 0] \stackrel{x \notin A}{=}0 \leq h(x)$\
\
**IS** $N \to N+1$: Sei also $x \notin A$. Dann gilt mittels Satz
[\[vorangegangene und zukünftige Ereignisse\]](#vorangegangene und zukünftige Ereignisse){reference-type="ref"
reference="vorangegangene und zukünftige Ereignisse"}
$$P_{x}[T_{A} \leq N+1] = P_{x}[1 \leq T_{A} \leq N+1]$$
$$= \sum_{y \in E} \mathbb{P}[X_{1} = y \: | \: X_{0} = x] \cdot \mathbb{P}_{\nu}[1 \leq T_{A} \leq N+1 \: | \: X_{0} = x, X_{1} = y]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} \sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[T_{A} \leq N]$$
$$\stackrel{\mathrm{IV}}{\leq}\sum_{y \in E} p(x,y) \cdot h(y)$$
$$\stackrel{(Lh)(x) = 0}{=}h(x)$$ Da
$\lbrace T_{A} \leq N \rbrace \uparrow \bigcup_{k \in \mathbb{N}} \lbrace T_{A} \leq k \rbrace = \lbrace T_{A} < \infty \rbrace$
für $N \to \infty$, so folgt aus der Stetigkeit des
Wahrscheinlichkeitsmaßes $\mathbb{P}_{x}$
$$h_{A}(x) = \mathbb{P}_{x}[T_{A} < \infty] = \lim_{N \to \infty} \mathbb{P}_{x}[T_{A} \leq N] \leq h(x), \: x \in E$$

**Beispiel 2.11** Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine
$(\nu,P)$-Markovkette auf $E = \lbrace 1,2,3,4 \rbrace$, deren
stochastische Matrix durch folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph des stochastischen Prozesses](beispiel22 "fig:")

Im folgenden soll die Eintrittswahrscheinlichkeit in den Zustand
$\lbrace 4 \rbrace$, d.h.
$$h_{\lbrace    4 \rbrace}(x) := \mathbb{P}_{x}[T_{\lbrace 4 \rbrace} < \infty], \: x \in E$$
bestimmt werden. Nach Satz
[\[Dirichletsatz\]](#Dirichletsatz){reference-type="ref"
reference="Dirichletsatz"} genügt es dazu, die minimale Lösung des
Dirichletproblems mit $A=\lbrace 4 \rbrace$ zu berechnen. Betrachte
somit folgendes Gleichungssystem. $$\begin{aligned}
     I. \quad h_{\lbrace 4 \rbrace}(1) &= c          & II. \quad h_{\lbrace 4 \rbrace}(2) &= \dfrac{1}{2}(h_{\lbrace 4 \rbrace}(1) + h_{\lbrace 4 \rbrace}(3))  \,  \\ 
  III. \quad h_{\lbrace 4 \rbrace}(3) &= \dfrac{1}{2}(h_{\lbrace 4 \rbrace}(2) + h_{\lbrace 4 \rbrace}(4))   & IV. \quad h_{\lbrace    4 \rbrace}(1) &= 1.\end{aligned}$$

::: center
$\Leftrightarrow$
$h_{\lbrace 4 \rbrace} = (c, \dfrac{2}{3}c + \dfrac{2}{3}, \dfrac{1}{3}c + \dfrac{5}{6},1)^{T}$
:::

Folglich besitzt obiges Gleichungssystem erst durch die
Minimalitätsbedingung eine eindeutige Lösung. Wähle hierzu $c=0$. Dann
folgt

::: center
$h_{\lbrace 4 \rbrace}(2) = \mathbb{P}_{2}[T_{\lbrace 4 \rbrace} < \infty] = \dfrac{2}{3}$
und
$h_{\lbrace 4 \rbrace}(3) = \mathbb{P}_{3}[T_{\lbrace 4 \rbrace} < \infty] = \dfrac{5}{6}$
:::

**Beispiel 2.11**\[Ruinwahrscheinlichkeit\] Betrachte eine einfache
asymmetrische Irrfahrt auf $E = \mathbb{N}_{0}$ mit Absorbtion im
Zustand 0.

. ![asymmetrische Irrfahrt auf $\mathbb{N}_{0}$](beispiel23 "fig:")

wiederum soll die Eintrittswahrscheinlichkeit in $\lbrace 0 \rbrace$ (=
Absorbtionswahrscheinlichkeit) bestimmt werden. Aus Satz
[\[Dirichletsatz\]](#Dirichletsatz){reference-type="ref"
reference="Dirichletsatz"} folgt, dass
$h_{\lbrace 0 \rbrace}(x) := \mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty], \: x \in E$
die minimale, nichtnegative Lösung des folgenden Dirichletproblems ist:
$$(Lh_{\lbrace 0 \rbrace})(x) = p(h_{\lbrace 0 \rbrace}(x+1) - h_{\lbrace 0 \rbrace}(x)) + q(h_{\lbrace 0 \rbrace}(x-1) - h_{\lbrace 0 \rbrace}(x)) = 0, \: x \neq 0$$
$$h_{\lbrace 0 \rbrace}(0) = 1$$ [Beh.]{.ul}: Für $p \neq q$ ist die
Lösung von $(Lh)(x) = 0$ für alle $x \in E$ gegeben durch
$$h(x) = a + b \cdot (\dfrac{q}{p})^{x}$$ Es gilt nämlich für
$x \in \mathbb{N}$
$$(Lh)(x) = pb (\dfrac{q}{p})^{x}(\dfrac{q}{p} - 1) + qb (\dfrac{q}{p})^{x} (\dfrac{p}{q} - 1) = b (\dfrac{q}{p})^{x}(q-p + p-q) = 0$$
: p\<q\
\
Da $h_{\lbrace 0 \rbrace}(x) \in [0,1]$ für alle $x \in \mathbb{N}_{0}$,
folgt $b=0$ und, wegen $h_{\lbrace 0 \rbrace}(0) = 1, \: a=1$. Also
$$h_{\lbrace 0 \rbrace}(x) = \mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty] = 1 \qquad \forall x \in \mathbb{N}_{0}$$
: q\<p\
\
Aus $h_{\lbrace 0 \rbrace}(0) = 1$ folgt zunächst einmal, dass
$b = 1-a$. Also
$$\ni h_{\lbrace 0 \rbrace}(x) = (\dfrac{q}{p})^{x} + a(1- (\dfrac{q}{p})^{x}) \qquad \forall x \in \mathbb{N}_{0} \: \Rightarrow a \geq 0$$
Somit impliziert erst die Minimalitätsbedingung, dass $a=0$ ist, d.h.
$$h_{\lbrace 0 \rbrace}(x) = \mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty] = (\dfrac{q}{p})^{x}$$
[Beh.]{.ul}: Für $p=q$ ist die Lösung von $(Lh)(x) = 0$ für alle
$x \in E$ gegeben durch $$h(x) = a + bx$$ Denn für alle
$x \in \mathbb{N}$ gilt
$(Lh)(x) = \dfrac{1}{2}b(x + 1 -x) + \dfrac{1}{2}b(x -1 -x) = 0$\
Da $h_{\lbrace 0 \rbrace}(x) \in [0,1]$ für alle $x \in \mathbb{N}_{0}$,
so folgt $b=0$. Wegen $h_{\lbrace 0 \rbrace}(0) = 1$ ist zudem $a = 1$:
$$h_{\lbrace 0 \rbrace}(x) = \mathbb{P}_{x}[T_{\lbrace 0 \rbrace} \leq \infty] = 1$$

**Beispiel 2.11**\[Aussterbewahrscheinlichkeit von
Verzweigungsprozessen\] Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ ein
Verzweigungsprozess, d.h. $(X_{n})_{n \in \mathbb{N}_{0}}$ ist eine
Markovkette mit Zustandsraum $E = \mathbb{N}_{0}$ und Übergangsmatrix
$P = (p(x,y))_{x,y \in E}$
$$p(x,y) = \mu^{*x}(y) \qquad \mathrm{mit} \: \mu^{*0}(y) := \mathbbm{1}_{\lbrace 0 \rbrace}(y)$$
wobei $\mu$ eine gegebene Wahrscheinlichkeitsverteilung auf E ist.\
\
[Ziel]{.ul}: Berechne
$\mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty ], \: x \in E$ (=
Aussterbewahrscheinlichkeit)\
[Beh.]{.ul}: Für alle $n \in \mathbb{N}_{0}$ gilt
$\mathbb{P}_{x}[X_{n} = 0] = \mathbb{P}_{1}[X_{n} = 0]^{x}$, $x \in E$\
\
Beweis durch vollständige Induktion über n.\
\
**IA** $n=0$ :
$\mathbb{P}_{x}[X_{0} = 0] = \mathbbm{1}_{\lbrace x \rbrace}(0) = \mathbb{P}_{1}[X_{0} = 0]^{x}$,
$(0^{0} = 1)$\
**IS** $n \to n+1$ : Es gilt nun aber
$$\mathbb{P}_{x}[X_{n+1} = 0] = \sum_{y \in E} \mathbb{P}[X_{n+1} = 0, X_{1} = y \: | \: X_{0} = x]$$
$$=\sum_{y \in E} \mathbb{P}[X_{1} = y \: | \: X_{0} = x] \cdot \mathbb{P}[X_{n+1} = 0 \: | \: X_{0} = x, X_{1} = y ]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=}   \sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[X_{n} = 0]$$
Nach Induktionsvoraussetzung gilt weiterhin
$$\sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[X_{n} = 0] \stackrel{\mathrm{IV}}{=}  \sum_{y \in E} \mu^{*x}(y) \cdot \mathbb{P}_{1}[X_{n} = 0]^{y}$$
$$\sum_{y \in E} \sum_{y_{1} +....+ y_{x} = y} \mu(y_{1}) \cdot ... \cdot \mu(y_{x}) \mathbb{P}_{1}[X_{n} = 0]^{y_{1}+...+y_{x}}$$
$$= \sum_{y_{1},...,y_{x} \geq 0 } \mu(y_{1}) \mathbb{P}_{1}[X_{n} = 0]^{y_{1}} \cdot...\cdot \mu(y_{x}) \mathbb{P}_{1}[X_{n} = 0]^{y_{x}}$$
$$= (\sum_{z \geq 0} \mu(z) \mathbb{P}_{1}[X_{n} = 0]^{z})^{x}$$
$$\stackrel{\mathrm{IV}}{=} (\sum_{z \in E} p(1,z) \mathbb{P}_{z}[X_{n} = 0])^{x}$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=}   \mathbb{P}_{1}[X_{n+1} = 0]^{x}$$
Da $\lbrace T_{\lbrace 0 \rbrace} \leq n \rbrace$ =
$\lbrace X_{n} = 0 \rbrace$ für alle $n \in \mathbb{N}_{0}$ und
$\lbrace T_{\lbrace 0 \rbrace}  \leq n \rbrace$ $\uparrow$
$\bigcup_{k=0}^{\infty}$ $\lbrace T_{\lbrace 0 \rbrace} \leq k \rbrace$
$=$ $\lbrace T_{\lbrace 0 \rbrace} < \infty \rbrace$ für $n \to \infty$
folgt aus der Stetigkeit von $\mathbb{P}_{x}$
$$\mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty] = \lim_{n \to \infty} \mathbb{P}_{x}[X_{n} = 0] = \lim_{n \to \infty} \mathbb{P}_{1}[X_{n} = 0]^{x} = \mathbb{P}_{1}[T_{\lbrace 0 \rbrace} < \infty]^{x}$$
Folglich gilt
$h_{\lbrace 0 \rbrace}(x) = h_{\lbrace 0 \rbrace}(1)^{x} =: q^{x}$ für
alle $x \in E$. Im folgenden soll $q \in [0,1]$ bestimmt werden. Da nach
Satz $\ref{Dirichletsatz}$ $h_{\lbrace 0 \rbrace}$ die kleinste,
nichtnegative Lösung des Dirichletproblems ist, gilt
$$(Lh_{\lbrace 0 \rbrace})(1) = 0 \: \Leftrightarrow \: q = h_{\lbrace 0 \rbrace}(1) = \sum_{y \in E} \mu(y) \cdot  h_{\lbrace 0 \rbrace}(1)^{y} = G_{\mu}(q),$$
wobei $$G_{\mu}(s) := \sum_{y \in E} \mu(y) s^{y}, \: s \in [0,1]$$ Die
erzeugende Funktion von $\mu$ ist. Also ist q ein Fixpunkt der Gleichung
$$s = G_{\mu}(s)$$ Ist nun $\overline{q}$ ein weiterer Fixpunkt, so
genügt die Funktion $h(x) := \overline{q}^{x}$ ebenfalls dem
Dirichletproblem. Dann folgt aus Satz
[\[Dirichletsatz\]](#Dirichletsatz){reference-type="ref"
reference="Dirichletsatz"}
$$\overline{q} = h(1) \geq  h_{\lbrace 0 \rbrace}(1) = q,$$ d.h. q ist
der kleinste, nichtnegative Fixpunkt der Gleichung $s = G_{\mu}(s)$.\
\
Nachfolgend soll der kleinste nichtnegative Fixpunkt der Gleichung
$s = G_{\mu}(s)$ genauer analysiert werden. Da $\mu$ ein
Wahrscheinlichkeitsmaß auf E ist, gilt
$$G_{\mu}(1) = \sum_{y \in E} \mu(y) = 1$$ Falls $\mu$ entweder linear
$(\mu(0) + \mu(1) = 1)$ oder strikt konvex mit
$$G'_{\mu}(1) = \lim_{s \uparrow 1} G'_{\mu}(s) = \lim_{s \uparrow 1} \sum_{ k \geq 1} k \cdot \mu(k) \cdot s^{k-1} = \sum_{ k \geq 0} k \cdot \mu(k) < \infty$$
so gilt

. ![Fixpunktanalyse](beispiel24 "fig:")

**Definition 2.1**\[harmonische Funktion\] Sei $A \subsetneq E$. Eine
Funktion $f: \: E \to R$ heißt harmonisch auf $A^{C}$, wenn für alle
$x \in A^{C}$
$$(Lf)(x) \: \: \mathrm{existiert} \qquad \mathrm{und} \qquad (Lf)(x) = 0.$$

[Frage?]{style="color: red"} Gilt die Markoveigenschaft auch an
Stoppzeiten? **Definition 2.1**\[T-Vergangenheit\]
[\[T-Vergangenheit\]]{#T-Vergangenheit label="T-Vergangenheit"} Ist
$T: \Omega \to \mathbb{N}_{0} \cup \lbrace \infty \rbrace$ eine
Stoppzeit bzgl. eines stochastischen Prozesses
$X = (X_{n})_{n \in \mathbb{N}_{0}}$ auf
$(\Omega, \mathfrak{F}, \mathbb{P})$, so bezeichnet
$$\mathfrak{F}_{T}^{X} := \lbrace A \in \mathfrak{F} \: : \: A \cap \lbrace T = n \rbrace \in \mathfrak{F}_{n}^{X} \: \forall \: n \in \mathbb{N}_{0} \rbrace$$
die Menge der Ereignisse der T-Vergangenheit

**Bemerkung 2.11** $\mathfrak{F}_{T}^{X}$ ist eine $\sigma$-Algebra. Da
T eine Stopppzeit bzgl. X ist, ist $\Omega \in \mathfrak{F}_{T}^{X}$.
Weiterhin gilt für jedes $n \in \mathbb{N}_{0}$ und
$A \in \mathfrak{F}_{T}^{X}$
$$A^{C} \cap \lbrace T = n \rbrace = \underbrace{(A \cap \lbrace T = n \rbrace)^{C}}_{ \in \mathfrak{F}_{T}^{X}} \cap \underbrace{\lbrace T = n \rbrace}_{ \in \mathfrak{F}_{T}^{X}} \in \mathfrak{F}_{T}^{X}$$
Somit ist auch $A^{C} \in \mathfrak{F}_{T}^{X}$. Seien nun
$A_{1},A_{2},... \in \mathfrak{F}_{T}^{X}$. Dann gilt für alle
$n \in \mathbb{N}_{0}$
$$(\bigcup_{i=1}^{\infty} A_{i}) \cap \lbrace T = n \rbrace = (\bigcup_{i=1}^{\infty} \underbrace { A_{i} \cap \lbrace T = n \rbrace}_{ \in \mathfrak{F}_{T}^{X}}) \in \mathfrak{F}_{T}^{X}$$
Also ist auch $\bigcup_{i=1}^{\infty} A_{i} \in \mathfrak{F}_{T}^{X}$.

**Satz 2.6**\[starke Markoveigenschaft\]
[\[starke Markoveigenschaft\]]{#starke Markoveigenschaft
label="starke Markoveigenschaft"} Ist $(X_{n})_{n \in \mathbb{N}_{0}}$
eine $(\nu,P)$-Markovkette mit Zustandsraum E und T eine Stoppzeit, so
gilt für alle $A \in \varepsilon^{ \otimes \mathbb{N}_{0}}$,
$F \in \mathfrak{F}_{T}^{X}$ und $x \in E$ mit
$\mathbb{P}_{\nu}[F,X_{T} = x, T < \infty] > 0$
$$\mathbb{P}_{\nu}[(X_{T},X_{T+1},...) \in A \: | \: F, X_{T} = x, T < \infty] = \mathbb{P}_{x}[(X_{0},X_{1},...) \in A],$$
wobei $X_{T}$ auf $\lbrace T < \infty \rbrace$ definiert ist durch
$X_{T}(\omega) := X_{T(\omega)}(\omega)$

**Beweis 2.17** Sei also $A \in \varepsilon^{ \otimes \mathbb{N}_{0}}$,
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

**Korollar 2.4** [\[Anzahl Besuche\]]{#Anzahl Besuche
label="Anzahl Besuche"} Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine
$(\nu,P)$-Markovkette mit Zustandsraum E und
$$V_{x} := \sum_{n=0}^{\infty} \mathbbm{1}_{X_{n} = x} \: , \quad x \in E$$
Dann gilt für alle $k \in \mathbb{N}$
$$\mathbb{P}_{x}[V_{x} > k] = (1-\mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty] )^{k}.$$
Falls $\mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty] > 0$, so gilt
$$\mathbb{E}[V_{x}] = \dfrac{1}{\mathbb{P}_{x}[S_{\lbrace x \rbrace} = \infty]}$$

**Beweis 2.17** Für $x \in E$ definiere
$$S_{\lbrace x \rbrace}^{0} := 0 \quad und \quad S_{\lbrace x \rbrace}^{k} := \inf \lbrace n > S_{\lbrace x \rbrace}^{k-1} \: : \: X_{n} = x \rbrace \: , \quad k \in \mathbb{N}$$
Dann gilt für alle $k \in \mathbb{N}$
$$\lbrace V_{ \lbrace x \rbrace} > k \rbrace \cap \lbrace X_{0} = x \rbrace = \lbrace S_{\lbrace x \rbrace}^{k} < \infty \rbrace \cap \lbrace X_{0} = x \rbrace .$$
Aus der starken Markoveigenschaft folgt somit
$$\mathbb{P}_{x}[V_{ \lbrace x \rbrace} > k+1 \: | \: V_{ \lbrace x \rbrace} > k] = \mathbb{P}_{\lbrace x \rbrace}[S_{\lbrace x \rbrace}^{k+1} < \infty \: | \: S_{\lbrace x \rbrace}^{k} < \infty]$$
$$= \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{k+1} < \infty \: | \: X_{S_{\lbrace x \rbrace}^{k}} = x, S_{\lbrace x \rbrace}^{k} < \infty]$$
$$= \mathbb{P}_{\nu}[\inf \lbrace n>0 \: : \: X_{S_{\lbrace x \rbrace}^{k} + n} = x \rbrace + S_{\lbrace x \rbrace}^{k} < \infty  \: | \: X_{0} = x,X_{S_{\lbrace x \rbrace}^{k}} = x, S_{\lbrace x \rbrace}^{k} < \infty]$$
$$\stackrel{\mathrm{Satz} \: \ref{starke Markoveigenschaft}}{=} \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty]$$
Daraus folgt dann
$$\mathbb{P}_{x}[V_{x} > k] = \prod_{l=1}^{k-1} \mathbb{P}_{x}[V_{x} > l + 1 \: | \: V_{x} > l] \cdot \mathbb{P}_{x}[V_{x} > 1] \stackrel{\mathrm{Satz} \: \ref{starke Markoveigenschaft}}{=} \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty]^{k}.$$
Weiterhin gilt im Falle
$\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty] < 1$
$$\mathbb{E}_{x}[V_{x}] = \sum_{k=0}^{\infty}\mathbb{P}_{x}[V_{x} > k] = 1 + \sum_{k=1}^{\infty}\mathbb{P}_{x}[V_{x} > k] = 1 + \sum_{k=1}^{\infty}\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty]^{k}$$
$$= \dfrac{1}{1-\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty]} = \dfrac{1}{\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} = \infty]}$$

# Struktureigenschaften der Übergangsmatrix

Im folgenden sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine
$(\nu,P)$-Markovkette auf $(\Omega, \mathfrak{F},\mathbb{P})$ mit
höchstens abzählbaren Zustandsraum E. Bezeichne wieder mit
$P^{n} = (p_{n}(x,y))_{x,y \in E}$ das n-fache Matrixprodukt ($P^{0}$ =
Einheitsmatrix auf E), $n \in \mathbb{N}_{0}$
[absorbierender,_rekurrenter,_transienter_Zustand](Struktureigenschaften_der_Übergangsmatrix/absorbierender,_rekurrenter,_transienter_Zustand.md)  
[Bemerkung2_11](Struktureigenschaften_der_Übergangsmatrix/Bemerkung2_11.md)  
[Satz2_6](Struktureigenschaften_der_Übergangsmatrix/Satz2_6.md)  
[Beweis2_17](Struktureigenschaften_der_Übergangsmatrix/Beweis2_17.md)  
[Greenfunktion_von_X](Struktureigenschaften_der_Übergangsmatrix/Greenfunktion_von_X.md)  
[Korollar2_4](Struktureigenschaften_der_Übergangsmatrix/Korollar2_4.md)  
[Beweis2_18](Struktureigenschaften_der_Übergangsmatrix/Beweis2_18.md)  
[Kartenhausprozess](Struktureigenschaften_der_Übergangsmatrix/Kartenhausprozess.md)  
[Kartenhausprozess](Struktureigenschaften_der_Übergangsmatrix/Kartenhausprozess.md)  
[Kartenhausprozess](Struktureigenschaften_der_Übergangsmatrix/Kartenhausprozess.md)  
[positiv_und_nullrekurrent](Struktureigenschaften_der_Übergangsmatrix/positiv_und_nullrekurrent.md)  
[Unterschied_positiv_und_nullrekurrent](Struktureigenschaften_der_Übergangsmatrix/Unterschied_positiv_und_nullrekurrent.md)  
[Satz2_7](Struktureigenschaften_der_Übergangsmatrix/Satz2_7.md)  
[Korollar2_5](Struktureigenschaften_der_Übergangsmatrix/Korollar2_5.md)  
[Beweis2_19](Struktureigenschaften_der_Übergangsmatrix/Beweis2_19.md)  
[Periode](Struktureigenschaften_der_Übergangsmatrix/Periode.md)  
[Bemerkung2_12](Struktureigenschaften_der_Übergangsmatrix/Bemerkung2_12.md)  
[Beispiel2_11](Struktureigenschaften_der_Übergangsmatrix/Beispiel2_11.md)  
[Satz2_8](Struktureigenschaften_der_Übergangsmatrix/Satz2_8.md)  
[Beweis2_20](Struktureigenschaften_der_Übergangsmatrix/Beweis2_20.md)  
[Korollar2_6](Struktureigenschaften_der_Übergangsmatrix/Korollar2_6.md)  
[Beweis2_21](Struktureigenschaften_der_Übergangsmatrix/Beweis2_21.md)  
[Träge_Markovkette](Struktureigenschaften_der_Übergangsmatrix/Träge_Markovkette.md)  

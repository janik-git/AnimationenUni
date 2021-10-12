---
 title: "Klassifikation_von_Markovketten"
 mathjax : true
---
**Definition 2.1**\[erreichbar, kommunizieren, wesentlich\]

-   Ein Zustand $y \in E$ heißt erreichbar von $x \in E$
    $(x \rightarrow y)$, falls ein $n \in \mathbb{N}_{0}$ existiert mit
    $p_{n}(x,y)>0$

-   Die Zustände $x,y \in E$ kommunizieren $(x\leftrightarrow y)$, falls
    $x \rightarrow y$ und $y \rightarrow x$.

-   Eine nichtleere Teilmenge $\emptyset \neq K \subseteq E$ heißt
    kommunizierende Klasse, falls

    -   $x \leftrightarrow y$ für alle $x,y \in K$

    -   aus $x \in K$ und $y \in E$ mit $x \leftarrow y$ folgt $y \in K$
        $\quad (Abgeschlossenheit)$

-   Ist $x \in E$ Element einer kommunizierenden Klasse, so heißt x
    wesentlich(sonst unwesentlich).

**Bemerkung 2.16** Jedes $x \in E$ liegt höchstens in einer
kommunizierenden Klasse.

**Beispiel 2.13**

-   kommunizierende Klassen: $\lbrace 1,2,3 \rbrace$,
    $\lbrace 5 \rbrace$

-   unwesentliche Zustände: $\lbrace 4,6,7 \rbrace$

. ![Markovkette mit zwei kommunizierenden
Klassen](Beispiel_Kommunizierende_Klasse "fig:")

**Satz 2.14** Die Relation $\leftrightarrow$ ist eine
Äquivalenzrelation. Auf der Menge der wesentlichen Zustände sind die
zugehörigen Äquivalenzklassen die kommunizierenden Klassen.

**Beweis 2.28** Offensichtlich ist die Relation $\leftrightarrow$
symmetrisch und reflexiv. Seien nun $x,y,z \in E$ mit
$x \leftrightarrow y$ und $y \leftrightarrow z$. Dann gibt es
$n_{1},n_{2} \in \mathbb{N}$ mit $p_{n_{1}}(x,y)>0$ und
$p_{n_{2}}(y,z)>0$.\
Aus der Chapman-Kolmogorov-Gleichung folgt
$$p_{n_{1} + n_{2}}(x,z) \geq p_{n_{1}}(x,y) \cdot p_{n_{2}}(y,z) > 0 \Rightarrow x \rightarrow z$$
Analog ergibt sich $z \rightarrow x$. Somit ist $\leftrightarrow$ auch
transitiv. Die zweite Aussage folgt direkt aus der Definition der
kommunizierenden Klasse.

**Satz 2.14**
[\[rekkurent und x -\> y so gilt y -\> x und y rekurrent\]]{#rekkurent und x -> y so gilt y -> x und y rekurrent
label="rekkurent und x -> y so gilt y -> x und y rekurrent"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E. Wenn $x \in E$ rekurrent ist und $x \rightarrow y$, so
gilt $y \rightarrow x$ und y ist rekurrent.

**Beweis 2.28** : $y \rightarrow x$\
\
Angenommen $y \not\rightarrow x$, d.h. $p_{n}(y,x) = 0$ für alle
$n \in \mathbb{N}$. Wähle $n_{0} \in \mathbb{N}_{0}$ so, dass
$$p_{n_{0}}(x,y) > 0.$$ Da x rekurrent ist, gilt
$$0 \stackrel{\mathrm{Satz} \: \ref{alternative Chrakterisierung von rekurrent/transient}}{=} \mathbb{P}_{x}[X_{n} = x \: für \: endlich \: viele \: n \in \mathbb{N}_{0}]$$
$$\geq \mathbb{P}_{x}[X_{n_{0}} = y, X_{n_{0} + 1} \neq x, X_{n_{0} + 2} \neq x,...]$$
$$= \mathbb{P}_{x}[X_{n_{0}}=y] \cdot \mathbb{P}_{x}[X_{n_{0}} = y,  X_{n_{0} + 1} \neq x, X_{n_{0} + 2} \neq x,... \: | \: X_{n_{0}} = y]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=} p_{n_{0}}(x,y) \cdot \mathbb{P}_{y}[X_{1} \neq x, X_{2} \neq x,...]$$
Setze $A_{n} = \lbrace X_{1} \neq x,...,X_{n} \neq x \rbrace.$ Dann gilt
$$A_{n} \downarrow \bigcap_{k=1}^{\infty} A_{k} = \lbrace X_{1} \neq x, X_{2} \neq x,...\rbrace$$
und
$$\mathbb{P}_{y}[X_{1} \neq x,..., X_{n} = x] = 1 - \mathbb{P}_{y}[{\lbrace X_{1} \neq x,..., X_{n} = x \rbrace}^{C}] \geq 1 - \sum_{k =1}^{n} \underbrace{\mathbb{P}_{y}[X_{k} = x]}_{p_{n}(y,x) = 0} = 1$$
Damit erhält man aus der Stetigkeit des Wahrscheinlichkeitsmaßes
$\mathbb{P}_{y}$
$$\mathbb{P}_{y}[X_{1} \neq x, X_{2} \neq x,...] = \lim_{n \to \infty} \mathbb{P}_{y}[X_{1} \neq x,...,X_{n} \neq x] = 1.$$
Also
$$0 \geq p_{n_{0}}(x,y) \cdot \mathbb{P}_{y}[X_{1} \neq x, X_{2} \neq x,...] = p_{n_{0}}(x,y) > 0 \: \: \lightning$$
Folglich gilt $y \rightarrow x$.

: y ist rekurrent\
\
Seien nun $k,l \in \mathbb{N}$ so gewählt, dass $p_{k}(x,y) > 0$ und
$p_{l}(y,x) > 0$. Dann ergibt sich aus der Chapman-Kolmogorov-Gleichung
$$p_{k+l+n}(y,y) \geq p_{l}(y,x) \cdot p_{n}(x,x) \cdot p_{k}(x,y) \qquad \forall n \in \mathbb{N}$$
Also
$$\sum_{n=1}^{\infty} p_{k+l+n}(y,y) \geq \underbrace{p_{l}(y,x)}_{>0} \cdot \underbrace{p_{k}(x,y)}_{>0} \cdot \sum_{n=1}^{\infty} p_{n}(x,x) \stackrel{\mathrm{Satz} \: \ref{alternative Chrakterisierung von rekurrent/transient}}{=} \infty.$$
da x rekurrent ist. **Korollar 2.8** Rekurrente Zustände sind
wesentlich.

**Beweis 2.28** Sei $x \in E$ rekurrent, und setze
$K(x) := \lbrace y \in E \: : \: x \rightarrow y \rbrace$. Nach Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$ gilt aber
$y \rightarrow x$ für alle $y \in K(x)$. Folglich ist $K(x)$ eine
kommunizierende Klasse, d.h. x ist wesentlich.

**Bemerkung 2.16** Unwesentliche Zustände sind transient.

**Satz 2.14**
[\[x und y selbe Periode, x transient y auch x nullrekurrent y auch\]]{#x und y selbe Periode, x transient y auch x nullrekurrent y auch
label="x und y selbe Periode, x transient y auch x nullrekurrent y auch"}
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette mit
Zustandsraum E und $x,y \in E$. Wenn $x \leftrightarrow y$, so gilt

-   x und y haben die selbe Periode, d.h. $d(x) = d(y)$

-   x ist transient $\Leftrightarrow$ y ist transient

-   x ist nullrekurrent $\Leftrightarrow$ y ist nullrekurrent

**Bemerkung 2.16** [\[Bemerkung 16\]]{#Bemerkung 16
label="Bemerkung 16"} Ist $x \in E$ positiv rekurrent und gilt
$x \rightarrow y$, so ist auch y positiv rekurrent.

**Beweis 2.28** a) :
$x \leftrightarrow y \quad \Rightarrow \quad d(x) = d(y)$\
\
Bezeichne mit
$D(x) := \lbrace n \in \mathbb{N}_{0} \: : \: p_{n}(x,x)>0 \rbrace$,
$x \in E$. Seien nun $x,y \in E$ mit x $\leftrightarrow$ y. Wähle
$m,n \in \mathbb{N}_{0}$ so, dass $p_{m}(x,y)>0$ und $p_{n}(y,x)>0$.
Dann gilt für jedes $k \in D(y)$ aufgrund der
Chapman-Kolmogorov-Gleichung
$$p_{m+k+n}(x,x) \geq p_{m}(x,y) \cdot p_{k}(y,y) \cdot p_{n}(y,x) > 0$$
Folglich ist $m+k+n \in D(x)$. Ist nun d ein Teiler von D(x), so gilt
$$d \: | \: \lbrace m+k+n \: : \: k \in D(y) \rbrace$$ Da aber
$m+n \in D(x)$ und somit $d \: | \: (m+n)$, folgt $d \: | \: D(y)$.
Also, $$d(x) = ggT(D(x)) \leq ggT(D(y)) = d(y)$$ Durch Vertauschen der
Rollen von x und y folgt analog $d(y) \leq d(x)$. Also $d(x) = d(y)$.\
\
b) $"\Rightarrow"$ Sei x transient. Da x $\leftrightarrow$ y, existieren
$k,l \in \mathbb{N}$ so, dass $p_{k}(x,y)>0$ und $p_{l}(y,x)>0$. Dann
folgt aus der Chapman-Kolmogorov-Gleichung
$$p_{k+l+n}(x,x) \geq p_{k}(x,y) \cdot p_{n}(y,y) \cdot p_{l}(y,x) > 0 \quad \forall n \in \mathbb{N}.$$
Daraus folgt aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$
$$\infty > \sum_{n=1}^{\infty} p_{k+l+n}(x,x) \geq \underbrace{p_{k}(x,y)}_{>0} \cdot \underbrace{p_{l}(y,x)}_{>0} \sum_{n=1}^{\infty} p_{n}(y,y) \quad \Rightarrow \quad \sum_{n=1}^{\infty} p_{n}(y,y) < \infty$$
Also ist y transient.\
$"\Leftarrow"$ Analog.\
\
c) $"\Rightarrow"$ Sei x nullrekurrent. Da $x \leftrightarrow y$
existieren somit $k,l \in \mathbb{N}$ mit $p_{k}(x,y) > 0$ und
$p_{l}(y,x) > 0$. Wiederum folgt aus der Chapman-Kolmogorov-Gleichung
$$p_{k+l+n}(x,x) \geq p_{k}(x,y) \cdot p_{n}(y,y) \cdot p_{l}(y,x) \quad \forall n \in \mathbb{N}$$
Dann folgt aus Satz $\ref{nullrekurrent und limes}$
$$0 = \lim_{n \to \infty}p_{k+l+n}(x,x) \geq \limsup_{n \to \infty} \underbrace{p_{k}(x,y)}_{>0} \cdot \underbrace{p_{l}(y,x)}_{>0} \cdot p_{n}(y,y) \quad \Rightarrow \quad \lim_{n \to \infty} p_{n}(y,y) = 0$$
Folglich ist y nach Satz $\ref{nullrekurrent und limes}$ nullrekurrent.\
$"\Leftarrow"$ Analog.

**Definition 2.1**\[irreduzibel\] Eine stochastische Matrix P auf E
heißt irreduzibel, falls E nur aus einer kommunizierenden Klasse
besteht. Eine $(\nu,P)$-Markovkette $(X_{n})_{n \in \mathbb{N}_{0}}$
heißt irreduzibel, falls P irreduzibel ist.

**Satz 2.14**
[\[irr. Markovkette x positiv rekurrent\]]{#irr. Markovkette x positiv rekurrent
label="irr. Markovkette x positiv rekurrent"} Ist
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine irreduzible $(\nu,P)$-Markovkette
auf einem endlichen Zustandsraum E, so ist $x \in E$ positiv rekurrent.

**Beweis 2.28** Zunächst einmal gilt für jedes $x \in E$
$$\sum_{y \in E}G(x,y) = \sum_{n=0}^{\infty} \sum_{y \in E} p_{n}(x,y) = \sum_{n=0}^{\infty} 1 = \infty$$
Da E endlich ist, gibt es folglich ein $y \in E$ mit $G(x,y) = \infty$.
Da E aufgrund der Irreduzibilität nur aus einer kommunizierenden Klasse
besteht, ist insbesondere $y \rightarrow x$. Folglich existiert ein
$m \in \mathbb{N}$ mit $p_{m}(x,y)>0$. Aus der
Chapman-Kolmogorov-Gleichung folgt zudem
$p_{m+n}(x,x) \geq p_{n}(x,y) \cdot p_{m}(y,x)$. Also,
$$G(x,x) \geq \sum_{n=0}^{\infty} p_{n}(x,y)p_{m}(y,x) = \underbrace{p_{m}(y,x)}_{>0} \cdot G(x,y) = \infty$$
Somit ist x nach Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ rekurrent.
Aus Satz $\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$
folgt dann aber, dass jeder Zustand in E rekurrent ist. Angenommen
$x \in E$ wäre nullrekurrent. Dann folgt aus Satz
$\ref{x und y selbe Periode, x transient y auch x nullrekurrent y auch}$,
dass jeder Zustand nullrekurrent ist. Aber dann folgt aus Korollar
$\ref{nullrekurrent und limes}$
$$1 = \lim_{n \to \infty} \sum_{y \in E} p_{n}(x,y) \stackrel{\vert E \vert < \infty}{=} 0 \: \: \lightning$$
$\Rightarrow$ alle Zustände in E sind positiv rekurrent.

\
**Satz 2.14**
[\[irreduzibel, y rekurrent -\> Px=1 , y transient -\> Px\<1 \]]{#irreduzibel, y rekurrent -> Px=1 , y transient -> Px<1 
label="irreduzibel, y rekurrent -> Px=1 , y transient -> Px<1 "} Ist
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine irreduzible $(\nu,P)$-Markovkette
mit Zustandsraum E. Dann gilt

-   $y \in E$ ist rekurrent $\quad$ $\Rightarrow$ $\quad$
    $\mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] = 1$ $\quad$
    $\forall x,y \in E$

-   $y \in E$ ist transient $\quad$ $\Rightarrow$ $\quad$
    $\mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] < 1$ $\quad$
    $\forall x,y \in E$

**Beweis 2.28** Da $(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist,
folgt $x \leftrightarrow y$ für alle $x,y \in E$. Insbesondere sind nach
Satz $\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$ und
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

**Definition 2.1**\[Rekurrenz/Transienz einer Markovkette\] Eine
irreduzible $(\nu,P)$-Markovkette heißt rekurrent/transient, wenn ein
Zustand rekurrent/transient ist.
[erreichbar,_kommunizieren,_wesentlich](Struktureigenschaften_der_Übergangsmatrix/erreichbar,_kommunizieren,_wesentlich.md)  
[Bemerkung2_13](Struktureigenschaften_der_Übergangsmatrix/Bemerkung2_13.md)  
[Beispiel2_12](Struktureigenschaften_der_Übergangsmatrix/Beispiel2_12.md)  
[Satz2_9](Struktureigenschaften_der_Übergangsmatrix/Satz2_9.md)  
[Beweis2_22](Struktureigenschaften_der_Übergangsmatrix/Beweis2_22.md)  
[Satz2_10](Struktureigenschaften_der_Übergangsmatrix/Satz2_10.md)  
[Beweis2_23](Struktureigenschaften_der_Übergangsmatrix/Beweis2_23.md)  
[Korollar2_7](Struktureigenschaften_der_Übergangsmatrix/Korollar2_7.md)  
[Beweis2_24](Struktureigenschaften_der_Übergangsmatrix/Beweis2_24.md)  
[Bemerkung2_14](Struktureigenschaften_der_Übergangsmatrix/Bemerkung2_14.md)  
[Satz2_11](Struktureigenschaften_der_Übergangsmatrix/Satz2_11.md)  
[Bemerkung2_15](Struktureigenschaften_der_Übergangsmatrix/Bemerkung2_15.md)  
[Beweis2_25](Struktureigenschaften_der_Übergangsmatrix/Beweis2_25.md)  
[irreduzibel](Struktureigenschaften_der_Übergangsmatrix/irreduzibel.md)  
[Satz2_12](Struktureigenschaften_der_Übergangsmatrix/Satz2_12.md)  
[Beweis2_26](Struktureigenschaften_der_Übergangsmatrix/Beweis2_26.md)  
[Satz2_13](Struktureigenschaften_der_Übergangsmatrix/Satz2_13.md)  
[Beweis2_27](Struktureigenschaften_der_Übergangsmatrix/Beweis2_27.md)  
[Rekurrenz_Transienz_einer_Markovkette](Struktureigenschaften_der_Übergangsmatrix/Rekurrenz_Transienz_einer_Markovkette.md)  
[Beweis2_28](Struktureigenschaften_der_Übergangsmatrix/Beweis2_28.md)  
[Beweis2_28](Struktureigenschaften_der_Übergangsmatrix/Beweis2_28.md)  
[Bemerkung2_16](Struktureigenschaften_der_Übergangsmatrix/Bemerkung2_16.md)  
[Dynkin-Formel](Struktureigenschaften_der_Übergangsmatrix/Dynkin-Formel.md)  
[Beweis2_29](Struktureigenschaften_der_Übergangsmatrix/Beweis2_29.md)  
[Lemma2_4](Struktureigenschaften_der_Übergangsmatrix/Lemma2_4.md)  
[Beweis2_30](Struktureigenschaften_der_Übergangsmatrix/Beweis2_30.md)  
[Satz2_15](Struktureigenschaften_der_Übergangsmatrix/Satz2_15.md)  
[Beweis2_31](Struktureigenschaften_der_Übergangsmatrix/Beweis2_31.md)  
[Beweis2_31](Struktureigenschaften_der_Übergangsmatrix/Beweis2_31.md)  
[Beweis2_31](Struktureigenschaften_der_Übergangsmatrix/Beweis2_31.md)  
[Chung-Fuchs](Struktureigenschaften_der_Übergangsmatrix/Chung-Fuchs.md)  
[Bemerkung2_17](Struktureigenschaften_der_Übergangsmatrix/Bemerkung2_17.md)  
[Beweis2_32](Struktureigenschaften_der_Übergangsmatrix/Beweis2_32.md)  
[Beweis2_32](Struktureigenschaften_der_Übergangsmatrix/Beweis2_32.md)  
[Beweis2_32](Struktureigenschaften_der_Übergangsmatrix/Beweis2_32.md)  

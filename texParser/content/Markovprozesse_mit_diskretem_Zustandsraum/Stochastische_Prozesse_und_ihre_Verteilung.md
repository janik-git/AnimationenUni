---
 title: "Stochastische_Prozesse_und_ihre_Verteilung"
 mathjax : true
---
Sei $(\Omega, \mathfrak{F}, \mathbb{P})$ ein Wahrscheinlichkeitsraum,
$(E, \varepsilon)$ ein meßbarer Raum und I eine nichtleere Indexmenge
z.B

-   E ist endlich oder abzählbar unendlich

-   E = $\mathbb{R},\: \mathbb{R}^{d}$

-   E ist ein Funktionsraum

-   I = endlich, $\: \mathbb{N}_{0},\: \mathbb{Z}$ (diskret)

-   I = $\: [0,\infty), \:\mathbb{R}, \:\mathbb{R}^{d}$ (kontinuierlich)

Interpretation: E ist der Zustandsraum(Ort) und I ist die Zeit.

**Definition 1.1**\[Stochastischer Prozess\] Ein stochastischer Prozess
auf $(\Omega, \mathfrak{F}, \mathbb{P})$ mit Werten im Zustandsraum
$(E, \varepsilon)$ ist eine Familie $(X_{t})_{t\in I}$ von E-wertigen
Zufallsvariablen. Für festes $\omega \in \Omega$ heißt die Abbildung\
$$I \ni t \mapsto X_{t}(\omega)$$\
eine Trajektorie(Pfad, Realisierung) von $(X_{t})_{t\in I}$. Falls I =
$\mathbb{N}_{0}$ oder I = $[0,\infty)$, so heißt die Verteilung von
$X_{0}$ die Startverteilung des stochastischen Prozesses.

**Bemerkung 1.6** Falls E diskret ist, so bezeichnet man eine Verteilung
auch als Wahrscheinlichkeitsvektor.

Unser Ziel ist es die Verteilung des stochastischen Prozesses
$(X_{t})_{t\in I}$ zu charakterisieren. Zunächst einmal lässt sich der
Produktraum $E^{I}$ auch als Menge $\lbrace x: I \to E\rbrace$ aller
Abbildungen von I nach E interpretieren.\
\
[Frage?]{style="color: red"} Wie lässt sich die zugehörige
Produkt-$\sigma$-Algebra $\varepsilon^{ \otimes I}$ charakterisieren?
**Definition 1.1**\[Produkt-$\sigma$-Algebra\] Die
Produkt-$\sigma$-Algebra $\varepsilon^{ \otimes I}$ ist die kleinste
$\sigma$-Algebra über $E^{I}$, die die Menge $\mathcal{Z}$ aller
endlich-dimensionalen Rechtecke(Zylindermenge) der Form
$$\lbrace x \in E^{I} : x_{t_{1}} \in B_{1}, x_{t_{2}} \in B_{2},..., x_{t_{n}} \in B_{n}   \rbrace$$
mit n $\in \mathbb{N}$,
$t_{1},..., t_{n} \in I \: und \:B_{1},...,B_{n} \in \varepsilon$
enthält.

**Lemma 1.4** Sei $(X_{t})_{t\in I}$ ein stochastischer Prozess mit
Zustandsraum $(E,\varepsilon)$, und definiere die Abbildung
$X:(\Omega,\mathfrak{F}) \to (E^{I},\varepsilon^{ \otimes I})$ durch
$X(\omega) := (X_{t}(\omega))_{t\in I}$. Dann ist X meßbar.

**Beweis 1.6** Übungsaufgabe.

**Definition 1.1**\[Verteilung eines stochastischen Prozesses\] Die
Verteilung eines stochastischen Prozesses $(X_{t})_{t\in I}$ auf
$(\Omega, \mathfrak{F}, \mathbb{P})$ mit Zustandsraum $(E, \varepsilon)$
ist das Bildmaß $\mathbb{P}$ unter der in Lemma 1.1 definierten
Abbildung X, d.h.
$${{\mathbb{P}}_{X}}[B] := (\mathbb{P} \circ X^{-1})[B] = \mathbb{P}[ \lbrace \omega \in \Omega : X(\omega) \in B\rbrace] , \: B \in \varepsilon^{ \otimes I}$$

[Frage?]{style="color: red"} Welcher Zusammenhang besteht zwischen der
Verteilung eines stochastischen Prozesses und der Verteilung des
Prozesses an endlich vielen Zeitpunkten?\
\
Betrachte zwei nicht-leere, endliche Teilmengen $J,k \subseteq I$ mit
$k \subseteq J$. Definiere
$$\pi_{J}: E^{I} \to E^{J}, \qquad  {(X_{t})}_{t\in I} \mapsto \pi_{J}{(X_{t})}_{t\in I}:= {(X_{t})}_{t\in J}$$
$${\pi_{k}}^{J}: E^{J} \to E^{k}, \qquad  {(X_{t})}_{t\in J} \mapsto {\pi_{k}}^{J}{(X_{t})}_{t\in J}:= {(X_{t})}_{t\in k}$$
die endlich-dimensionale Projektionen.\
\
Da $\varepsilon^{ \otimes I}$ von den Mengen
${({\pi_{\lbrace t \rbrace}}^{J})}^{-1}(A)$,
$t \in J, \: A \in \varepsilon$ erzeugt wird und
$${\pi_{J}}^{-1}({({\pi_{\lbrace t \rbrace}}^{J})}^{-1}(A)) = {({\pi_{\lbrace t \rbrace}}^{J} \circ \pi_{J})}^{-1}(A) = {\pi_{\lbrace t \rbrace}}^{-1}(A) \in \varepsilon^{ \otimes I}$$
ist folglich
$\pi_{J} \: \:  (\varepsilon^{ \otimes I}, \varepsilon^{ \otimes J})$-meßbar.
**Definition 1.1**\[endlich-dimensionale Verteilung eines stochastischen
Prozesses\] Sei $X = {(X_{t})}_{t\in I}$ ein stochastischer Prozess mit
Verteilung ${\mathbb{P}}_X$ auf $(E^{I},\varepsilon^{ \otimes I})$ und
$J \subseteq I$ eine nichtleere, endliche Teilmenge von I. Setze
$X_{J} := {(X_{t})}_{t\in J} = \pi_{J}(X)$. Die
Wahrscheinlichkeitsverteilung ${{\mathbb{P}}_X}_{J}$ heißt
endlich-dimensionale Verteilung von X.

**Notation 1.2** Für $B \in \varepsilon^{ \otimes J}$ ist
${{\mathbb{P}}_{X_{J}}}[B] = {\mathbb{P} \circ {{(X_{t})}}_{t\in J}^{-1}[B] = \mathbb{P}[(X_{t})}_{t\in J} \in B]$.

**Lemma 1.4** [\[Teilmengen Lemma\]]{#Teilmengen Lemma
label="Teilmengen Lemma"} Sei $X = {(X_{t})}_{t\in I}$ ein
stochastischer Prozess mit Zustandsraum $(E,\varepsilon)$.

-   Für jede endliche Teilmenge $J \neq \emptyset$ von I gilt
    $${{\mathbb{P}}_{X_{J}}} = {\mathbb{P}}_{X} \circ {\pi_{J}}^{-1}$$

-   Für je zwei nicht-leere, endliche Teilmengen
    $J_{1},J_{2} \subseteq I$ mit $J_{1} \subseteq J_{2}$ gilt
    $${{\mathbb{P}}_{X_{J_{1}}}} = {\mathbb{P}}_{X_{J_{2}}} \circ {({\pi_{J_{1}}}^{J_{2}})}^{-1}$$

**Beweis 1.6**

-   Wegen $X_{J} = \pi_{J}({(X_{t})}_{t\in I}) = \pi_{J} \circ X$ gilt
    $${\mathbb{P}}_{X_{J}} = \mathbb{P} \circ {X_{J}}^{-1} = \mathbb{P} \circ {(\pi_{J} \circ X)}^{-1} = (\mathbb{P} \circ X^{-1}) \circ {\pi_{J}}^{-1} = \mathbb{P}_{X} \circ {\pi_{J}}^{-1}$$

-   Wegen $X_{J_{1}} = {\pi_{J_{1}}}^{J_{2}} \circ X_{J_{2}}$ folgt die
    Behauptung aus (i).

[Frage?]{style="color: red"} Ist es auch möglich die
unendlich-dimensionale Verteilung eindeutig durch die
endlich-dimensionale Verteilung festzulegen? **Lemma 1.4** Für jedes
$J \subseteq I$ sei ein Wahrscheinlichkeitsmaß $\mathbb{Q}_{J}$ auf
$(E^{J},\varepsilon^{ \otimes J})$ gegeben. Dann existiert höchstens ein
Wahrscheinlichkeitsmaß $\mathbb{Q}$ auf
$(E^{I},\varepsilon^{ \otimes I})$ mit
$${\mathbb{Q}}_{J} = \mathbb{Q} \circ {\pi_{J}}^{-1}$$ für alle
endlichen $\emptyset \neq J \subseteq J$.

**Beweis 1.6** Da nach Aufgabe 2 die Menge $\mathcal{Z}$ der
endlich-dimensionalen Rechtecke einen $\cap$-stabilen Erzeuger von
$\varepsilon^{ \otimes I}$ bilden und
$$\mathbb{Q}[\lbrace x \in E^{I} : x_{j} \in A_{j}, \: \forall j \in J\rbrace] = \mathbb{Q}[{\pi_{J}}^{-1}(\times_{j \in J} \: A_{j})] = (\mathbb{Q} \circ {\pi_{J}}^{-1})[\times_{j \in J} \: A_{j}] = \mathbb{Q}_{J}[\times_{j \in J} \: A_{j}]$$
für alle $\emptyset \neq J \subseteq I$ endlich und
$A_{j} \in \varepsilon$ für alle $j \in J$, folgt die Aussage aus dem
Eindeutigkeitssatz für Maße.

[Warnung!]{style="color: red"} Die eindimensionalen Verteilungen legen
$\mathbb{Q}$ im Allgemeinen nicht fest. **Beispiel 1.3** Betrachte eine
Folge ${(X_{n})}_{n \in N_{0}}$ von unabhängig, identisch verteilten
Zufallsvariablen und ${(Y_{n})}_{n \in N_{0}}$ sei definiert durch
$Y_{n} = X_{0}$ für alle $n \in \mathbb{N}$.

**Definition 1.1**\[konsistente Familie von Wahrscheinlichkeitsmaßen\]
Für jedes $\emptyset \neq J \subseteq I$ endlich sei $\mathbb{Q}_{J}$
ein Wahrscheinlichkeitsmaß auf $(E^{J},\varepsilon^{ \otimes J})$. Die
Familie
$\lbrace \mathbb{Q}_{J} : J \subseteq I \: \mathrm{endlich}\rbrace$
heißt konsistent, wenn
$$\mathbb{Q}_{J_{1}} = {\mathbb{Q}}_{J_{2}} \circ {({\pi_{J_{1}}}^{J_{2}})}^{-1} \qquad \forall \: J_{1} \subseteq J_{2} \subseteq I, \emptyset \neq J_{1},J_{2} \: \mathrm{endlich}$$

**Bemerkung 1.6**

-   Die endlich-dimensionalen Verteilungen eines stochastischen
    Prozesses bilden eine konsistente Familie

-   Falls $I = \mathbb{N}_{0}$ ist, so genügt es $J \subseteq I$ endlich
    der Form $J = \lbrace 0,1,..,n \rbrace$, $n \in \mathbb{N}_{0}$ zu
    wählen.

**Beispiel 1.3** Sei $I = \mathbb{N}_{0}$, $E = \mathbb{Z}^{2}$ und
$\mathbb{Q}_{\lbrace 0,..,n \rbrace}$ die Gleichverteilung auf der Menge
$$A_{n} = \lbrace (x_{0},...,x_{1}) \in E^{n+1} : x_{0} = 0, \; ||{x_{i} - x_{i-1}}|| = 1  \; \forall i = 1,..,n,\; x_{i} \neq x_{j} \; \forall i,j \in \lbrace 0,...,n \rbrace \rbrace$$
für $n \in \mathbb{N}_{0}$. Dann ist die zugehörige Familie
$\lbrace \mathbb{Q}_{\lbrace 0,..,n \rbrace} : n \in \mathbb{N}_{0} \rbrace$
$\underline{\mathrm{NICHT}}$ konsistent.

![Systemzustände n=1,\...,4](beispiel12)

Denn es gilt
$$\mathbb{Q}_{\lbrace 0,..,3 \rbrace}[\lbrace x_{0},x_{1},x_{2},x_{3} \rbrace] = \dfrac{1}{36} \neq \dfrac{2}{100} = \mathbb{Q}_{\lbrace 0,..,4 \rbrace}[{({\pi_{\lbrace 0,..3 \rbrace}}^{ \lbrace 0,...4 \rbrace})}^{-1}(\lbrace x_{0},x_{1},x_{2},x_{3} \rbrace)]$$

**Definition 1.1**\[Polnischer Raum\] Ein topologischer Raum $(E,\tau)$
heißt polnischer Raum, falls er vollständig metrisierbar und seperabel
ist

**Bemerkung 1.6**

-   $(E,\tau)$ heißt vollständig metrisierbar, falls eine vollständige
    Metrik d auf E existiert, die $\tau$ erzeugt.

-   $(E,\tau)$ heißt separabel, falls es eine abzählbare dichte
    Teilmenge $A \subseteq E$ gibt, d.h $\bar{A} = E$

**Bemerkung 1.6** Praktisch alle Räume, die in der
Wahrscheinlichkeitstheorie bedeutsam sind, sind polnisch, z.B

-   abzählbar, diskrete Räume, euklidische Räume $\mathbb{R}^{d}$

-   $C([0,1]) = \lbrace f:[0,1] \to \mathbb{R} \: \: stetig \rbrace$
    bzgl. Supremumsnorm

**Satz 1.1**\[Existenzsatz von Daniel und Kolmogorov\]
[\[Existenzsatz von Daniel und Kolmogorov\]]{#Existenzsatz von Daniel und Kolmogorov
label="Existenzsatz von Daniel und Kolmogorov"} Sei $(E, \varepsilon)$
ein polnischer Raum und
$\lbrace \mathbb{Q}_{J} : J \subseteq I \: \mathrm{endlich}\rbrace$ eine
konsistente Familie von Wahrscheinlichkeitsmaßen. Dann existiert genau
ein Wahrscheinlichkeitsmaß $\mathbb{Q}$ auf
$(E^{I},\varepsilon^{ \otimes I})$ mit der Eigenschaft
$${\mathbb{Q}}_{J} = \mathbb{Q} \circ {\pi_{J}}^{-1} \qquad \forall J \subseteq I \: \: \mathrm{endlich}
\label{eins}$$

**Beweis 1.6** siehe Klenke, Satz 14.36

**Bemerkung 1.6** Die Konstruktion von $\mathbb{Q}$ beruht auf dem Satz
von Carathéodory

-   $\mathcal{Z}$ ist eine Algebra und damit insbesondere ein Semiring.

-   Der Nachweis, dass die Mengenfunktion $\mathbb{Q}$ definiert
    durch (1) additiv ist, ist nicht allzu schwierig.

-   Zum Nachweis der $\sigma$-Subadditivität von $\mathbb{Q}$ verwendet
    man ein Kompaktheitsargument, wobei hierzu benutzt wird, dass E
    polnisch ist.

**Korollar 1.2** Sei $(E,\varepsilon)$ ein polnischer Raum. Weiterhin
sei $(X_{t})_{t\in I}$ ein stochastischer Prozess auf
$(\Omega, \mathfrak{F}, \mathbb{P})$ mit Zustandsraum $(E,\varepsilon)$.
Dann existiert genau ein Wahrscheinlichkeitsmaß
${\mathbb{P}}_{X} = \mathbb{P} \circ {X}^{-1}$, dessen
endlich-dimensionale Verteilung mit der gegebenen Familie
$$\lbrace \mathbb{P}_{X_{J}} : J \subseteq I \: \mathrm{endlich} \rbrace$$
übereinstimmen.

**Beweis 1.6** Nach Bemerkung 1.3 bilden die endlich-dimensionalen
Verteilungen des stochastischen Prozesses $(X_{t})_{t\in I}$ eine
konsistente Familie von Wahrscheinlichkeitsmaßen. Folglich ergibt sich
die Aussage direkt aus Satz 1.1.
[Stochastischer_Prozess](Markovprozesse_mit_diskretem_Zustandsraum/Stochastischer_Prozess.md)  
[Bemerkung1_1](Markovprozesse_mit_diskretem_Zustandsraum/Bemerkung1_1.md)  
[Produkt-__sigma_-Algebra](Markovprozesse_mit_diskretem_Zustandsraum/Produkt-__sigma_-Algebra.md)  
[Lemma1_1](Markovprozesse_mit_diskretem_Zustandsraum/Lemma1_1.md)  
[Beweis1_1](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_1.md)  
[Verteilung_eines_stochastischen_Prozesses](Markovprozesse_mit_diskretem_Zustandsraum/Verteilung_eines_stochastischen_Prozesses.md)  
[endlich-dimensionale_Verteilung_eines_stochastischen_Prozesses](Markovprozesse_mit_diskretem_Zustandsraum/endlich-dimensionale_Verteilung_eines_stochastischen_Prozesses.md)  
[Notation1_1](Markovprozesse_mit_diskretem_Zustandsraum/Notation1_1.md)  
[Lemma1_2](Markovprozesse_mit_diskretem_Zustandsraum/Lemma1_2.md)  
[Beweis1_2](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_2.md)  
[Lemma1_3](Markovprozesse_mit_diskretem_Zustandsraum/Lemma1_3.md)  
[Beweis1_3](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_3.md)  
[Beispiel1_1](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_1.md)  
[konsistente_Familie_von_Wahrscheinlichkeitsmaßen](Markovprozesse_mit_diskretem_Zustandsraum/konsistente_Familie_von_Wahrscheinlichkeitsmaßen.md)  
[Bemerkung1_2](Markovprozesse_mit_diskretem_Zustandsraum/Bemerkung1_2.md)  
[Beispiel1_2](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_2.md)  
[Polnischer_Raum](Markovprozesse_mit_diskretem_Zustandsraum/Polnischer_Raum.md)  
[Bemerkung1_3](Markovprozesse_mit_diskretem_Zustandsraum/Bemerkung1_3.md)  
[Bemerkung1_4](Markovprozesse_mit_diskretem_Zustandsraum/Bemerkung1_4.md)  
[Existenzsatz_von_Daniel_und_Kolmogorov](Markovprozesse_mit_diskretem_Zustandsraum/Existenzsatz_von_Daniel_und_Kolmogorov.md)  
[Beweis1_4](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_4.md)  
[Korollar1_1](Markovprozesse_mit_diskretem_Zustandsraum/Korollar1_1.md)  
[Beweis1_5](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_5.md)  
[Beweis1_5](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_5.md)  
[Markoveigenschaft](Markovprozesse_mit_diskretem_Zustandsraum/Markoveigenschaft.md)  
[Erklärung1_1](Markovprozesse_mit_diskretem_Zustandsraum/Erklärung1_1.md)  
[Beispiel1_3](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_3.md)  
[Beispiel1_4](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_4.md)  
[stochastiche_Matrix](Markovprozesse_mit_diskretem_Zustandsraum/stochastiche_Matrix.md)  
[Chapman-Kolmogorov_Gleichung](Markovprozesse_mit_diskretem_Zustandsraum/Chapman-Kolmogorov_Gleichung.md)  
[Beweis1_6](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_6.md)  
[Chapman-Kolmogorov_Gleichung](Markovprozesse_mit_diskretem_Zustandsraum/Chapman-Kolmogorov_Gleichung.md)  
[Beispiel1_5](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_5.md)  
[zeithomogene_Markovkette](Markovprozesse_mit_diskretem_Zustandsraum/zeithomogene_Markovkette.md)  
[Notation1_2](Markovprozesse_mit_diskretem_Zustandsraum/Notation1_2.md)  
[Bemerkung1_6](Markovprozesse_mit_diskretem_Zustandsraum/Bemerkung1_6.md)  
[Beispiel1_6](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_6.md)  
[Beispiel1_6](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_6.md)  
[Beispiel1_6](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_6.md)  
[Irrfahrt_auf___lbrace_0,___,N__rbrace_](Markovprozesse_mit_diskretem_Zustandsraum/Irrfahrt_auf___lbrace_0,___,N__rbrace_.md)  
[Irrfahrt_auf___lbrace_0,___,N__rbrace_](Markovprozesse_mit_diskretem_Zustandsraum/Irrfahrt_auf___lbrace_0,___,N__rbrace_.md)  
[einfache_Irrfahrt_auf_dem_Graphen](Markovprozesse_mit_diskretem_Zustandsraum/einfache_Irrfahrt_auf_dem_Graphen.md)  
[Verzweigungsprozesse](Markovprozesse_mit_diskretem_Zustandsraum/Verzweigungsprozesse.md)  
[Satz1_1](Markovprozesse_mit_diskretem_Zustandsraum/Satz1_1.md)  
[Beweis1_7](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_7.md)  
[Satz1_2](Markovprozesse_mit_diskretem_Zustandsraum/Satz1_2.md)  
[Beweis1_8](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_8.md)  
[Beispiel1_7](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_7.md)  
[Korollar1_2](Markovprozesse_mit_diskretem_Zustandsraum/Korollar1_2.md)  
[Beweis1_9](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_9.md)  
[Satz1_3](Markovprozesse_mit_diskretem_Zustandsraum/Satz1_3.md)  
[Beweis1_10](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_10.md)  
[Unabhängigkeit_von_Zukunft_und_Vergangenheit_bei_geg__Gegenwart](Markovprozesse_mit_diskretem_Zustandsraum/Unabhängigkeit_von_Zukunft_und_Vergangenheit_bei_geg__Gegenwart.md)  
[Beweis1_11](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_11.md)  
[Existenzsatz_von_Markovketten](Markovprozesse_mit_diskretem_Zustandsraum/Existenzsatz_von_Markovketten.md)  
[Beweis1_12](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_12.md)  
[Satz1_4](Markovprozesse_mit_diskretem_Zustandsraum/Satz1_4.md)  
[Beweis1_13](Markovprozesse_mit_diskretem_Zustandsraum/Beweis1_13.md)  
[Bemerkung1_7](Markovprozesse_mit_diskretem_Zustandsraum/Bemerkung1_7.md)  
[Beispiel1_8](Markovprozesse_mit_diskretem_Zustandsraum/Beispiel1_8.md)  

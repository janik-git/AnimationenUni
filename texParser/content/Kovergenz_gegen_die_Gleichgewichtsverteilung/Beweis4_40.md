---
 title: "Beweis4_40"
 mathjax : true
---
[Schritt 1]{.ul}: Sei $((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$ die
Markovkette der unabhängigen Kopplung (vgl. Beispiel
$\ref{BSP unabhängige Kopplung}$). Da $P$ irreduzibel und aperiodisch
ist, gibt es nach Satz
$\ref{x und y selbe Periode, x transient y auch x nullrekurrent y auch}$
udn Korollar $\ref{Korollar 2.6}$ für alle $x,x',y,y' \in E$ ein
$\mathbb{N}_{0} \equiv \mathbb{N}_{0}(x,x',y,y') \in \mathbb{N}$ so,
dass
$$\bar{p} \left( (x,y),(x',y') \right) = p_{n}(x,x')p_{n}(y,y') > 0 \qquad n \geq N_{0}.$$
Folglich ist die Markovkette $((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$
irreduzibel. Für ein beliebig gewähltes $x_{0} \in E$ definiere
$$S \equiv S_{\lbrace (x_{0},x_{0}) \rbrace} := \inf \lbrace n \in \mathbb{N} \: | \:  \left( X_{n},Y_{n} \right)  =(x_{0},x_{0}) \rbrace.$$
:
$\vert p_{n}(x,y) - p_{n}(z,y) \vert \leq \mathbb{P}_{\lbrace (x,z) \rbrace}[S>n] \qquad \forall \: n \in \mathbb{N}$\
Es gilt nun aber
$$\mathbb{P}_{(x,z)}[X_{n} = y, S \leq n] = \sum_{m=1}^{n} \mathbb{P}_{(x,z)}[X_{n}=y, S = m]$$
$$= \sum_{m=1}^{n} \mathbb{P}_{(x,z)}[S = m]\mathbb{P}_{(x,z)}[X_{n}=y  \: | \: (X_{S},Y_{S})=(x_{0},x_{0}), S = m]$$
$$\stackrel{\mathrm{Satz \:}\ref{vorangegangene und zukünftige Ereignisse}}{=}
\sum_{m=1}^{n} \mathbb{P}_{(x,z)}[S = m]\mathbb{P}_{(x_{0},x_{0})}[X_{n-m}=y]$$
Weiterhin gilt
$$\mathbb{P}_{(x_{0},x_{0})}[X_{n-m}=y] = \sum_{y' \in E} \underbrace{\bar{p}_{n-m}\left( (x_{0},x_{0}),(y,y') \right)}_{= \: p_{n-m}(x_{0},y)p_{n-m}(x_{0},y')}$$
$$\qquad \qquad  \qquad \qquad \:   = \sum_{y' \in E} \overbrace{\bar{p}_{n-m}\left( (x_{0},x_{0}),(y',y) \right)}$$
$$\qquad \qquad  \quad = \mathbb{P}_{(x_{0},x_{0})}[Y_{n-m}=y]$$ Daraus
folgt
$$\mathbb{P}_{(x,z)}[X_{n}=y, S \leq n] = \sum_{m=1}^{n} \mathbb{P}_{(x,z)}[S=m]\mathbb{P}_{(x_{0},x_{0})}[X_{n-m}=y]$$
$$= \sum_{m=1}^{n} \mathbb{P}_{(x,z)}[S=m]\mathbb{P}_{(x_{0},x_{0})}[Y_{n-m}=y] = \mathbb{P}_{(x,z)}[Y_{n}=y, S \leq n]$$
Somit ergibt sich
$$\vert p_{n}(x,y) - p_{n}(z,y) \vert = \vert \mathbb{P}_{(x,z)}[X_{n}=y] - \mathbb{P}_{(x,z)}[Y_{n} =y] \vert$$
$$= \vert \mathbb{P}_{(x,z)}[X_{n}=y, S>n] - \mathbb{P}_{(x,z)}[Y_{n} =y, S>n] \vert$$
$$= \vert \mathbb{P}_{(x,z)}[X_{n}=y \: | \: S>n] - \mathbb{P}_{(x,z)}[Y_{n} =y \: | \: S>n] \vert \mathbb{P}_{(x,z)}[S>n]$$
$$\leq \mathbb{P}_{(x,z)}[S>n]$$ [Schritt 2]{.ul}: Betrachte zunächst
den Fall, dass $(X_{n})_{n \in \mathbb{N}_{0}}$ positiv rekurrent ist.
Dann existiert nach Satz $\ref{Satz 3.6}$ a) eine eindeutig bestimmte
Gleichgewichtsverteilung $\pi$. Da aber
$$\sum_{(x,y) \in E \times E} (\pi \otimes \pi)(x,y)\bar{p}\left( (x,y),(x',y') \right) = (\pi P)(x')(\pi P)(y') \stackrel{\pi = \pi P}{=} \pi(x') \pi(y') = (\pi \otimes \pi)(x',y')$$
ist folglich $\pi \otimes \pi$ eine Gleichverteilung von
$((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$. Insbesondere ist nach Satz
$\ref{Satz 3.6}$ a) die Markovkette
$((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$ positiv rekurrent und damit
auch rekurrent.\
Aus Satz $\ref{irreduzibel, y rekurrent -> Px=1 , y transient -> Px<1 }$
folgt daher
$$\mathbb{P}_{(x,z)}[S_{\lbrace (x_{0},x_{0}) \rbrace} < \infty] =1$$
Daraus folgt
$$\limsup_{n \to \infty} \vert p_{n}(x,y) - p_{n}(z,y) \vert \leq \mathbb{P}_{(x,z)}[S_{\lbrace (x_{0},x_{0}) \rbrace} = \infty] = 0$$
Also, $$\lim_{n \to \infty} \vert p_{n}(x,y) - p_{n}(z,y) \vert = 0$$
Weiterhin gilt
$$\vert p_{n}(x,y) - \pi(y) \vert = \vert \sum_{z \in E} \pi(z) \left( p_{n}(x,y) - p_{n}(z,y) \right) \vert \leq \sum_{z \in E} \pi(z) \vert  p_{n}(x,y) - p_{n}(z,y)  \vert$$
Also folgt aus dem Satz von Lebesgue
$$\limsup_{n \to \infty} \vert p_{n}(x,y) - \pi(y) \vert \leq 0$$ Da
$\pi(y) = \dfrac{1}{\mathbb{E}_{y}[S_{\lbrace y \rbrace}]}$ nach Satz
$\ref{Satz 3.6}$ a) ist, folgt die Behauptung.\
\
[Schritt 3]{.ul}: Sei nun $(X_{n})_{n \in \mathbb{N}_{0}}$
nullrekurrent. Dann gibt es zwei Fälle zu untersuchen\
\
[1. Fall]{.ul}: $((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$ ist transient\
Nach Korollar
$\ref{transienter Zustand dann lim n -> unendl. pn(x,y) = 0}$ gilt dann
aber
$$\lim_{n \to \infty} p_{n}(x,y)^{2} = \lim_{n \to \infty} \bar{p}_{n}((x,x),(y,y)) = 0.$$
woraus die Behauptung folgt.\
\
[2. Fall]{.ul}: $((X_{n},Y_{n}))_{n \in \mathbb{N}_{0}}$ ist rekurrent\
Dann ist nach Satz
$\ref{irreduzibel, y rekurrent -> Px=1 , y transient -> Px<1 }$
$\mathbb{P}_{(x,z)}[S_{\lbrace (x_{0},x_{0}) \rbrace} < \infty] = 1$ und
aus Schritt 1 folgt
$$\limsup_{n \to \infty} \vert p_{n}(x,y) - p_{n}(z,y) \vert \leq \mathbb{P}_{(x,z)}[S_{\lbrace (x_{0},x_{0}) \rbrace} = \infty] = 0$$
Also, $$\lim_{n \to \infty} \vert p_{n}(x,y) - p_{n}(z,y) \vert = 0$$
Angenommen es existiert ein $(x,y) \in E \times E$ mit
$$\limsup_{n \to \infty} p_{n}(x,y) =: \alpha > 0$$ Dann existiert eine
Teilfolge $(n_{k})_{k \in \mathbb{N}}$ derart, dass
$$\lim_{k \to \infty} p_{n_{k}}(x,y) = \alpha$$ Da
$(X_{n})_{n \in \mathbb{N}_{0}}$ nullrekurrent ist, folgt aus Satz
$\ref{aufzählungen existenz von invarianten Maßen}$, dass
$$\mu(z)_{x} := \mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace}-1} \mathbbm{1}_{X_{n}=z}] \qquad , z \in E$$
ein invariantes Maß ist mit $\mu_{x}(z) \in (0,\infty)$ für alle
$z \in E$ und
$$\sum_{z \in E} \mu_{x}(z) = \mathbb{E}_{x}[S_{\lbrace x \rbrace}] = \infty$$
Also existiert eine endliche Teilmenge $M \subseteq E$ mit
$$\sum_{z \in M} \mu_{x}(z) > \dfrac{2}{\alpha} \mu_{x}(y).$$ Weiterhin
existiert ein $k_{0} \in \mathbb{N}$ so, dass für alle $k \geq k_{0}$
$$\vert p_{n_{k}}(x,y) - \alpha \vert < \dfrac{\alpha}{4} \qquad \mathrm{und} \qquad \max_{z \in M} \vert p_{n_{k}}(x,y) - p_{n_{k}}(z,y)  \vert < \dfrac{\alpha}{4}.$$
Daraus folgt dann aber für alle $z \in M$ und $k \geq k_{0}$
$$p_{n_{k}}(z,y) = \alpha + p_{n_{k}}(z,y) - \alpha \geq \alpha - \underbrace{\vert p_{n_{k}}(z,y) - p_{n_{k}}(x,y) \vert}_{< \dfrac{\alpha}{4}} - \underbrace{\vert p_{n_{k}}(x,y) - \alpha \vert}_{<\dfrac{\alpha}{4}} > \alpha$$
Also
$$\mu_{x}(y) \stackrel{\mu_{x} = \mu_{x}P}{=} \sum_{z \in E} \mu_{x}(z) p_{n_{k}}(z,y) \geq \sum_{z \in M} \mu_{x}(z) p_{n_{k}}(z,y) > \dfrac{\alpha}{2} \sum_{z \in M} \mu_{x}(z) > \mu_{x}(y) \qquad \lightning$$
Folglich war die Annahme falsch und es gilt
$$\lim_{n \to \infty} p_{n}(x,y) = 0.$$

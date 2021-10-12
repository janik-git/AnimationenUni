---
 title: "Bemerkung3_18"
 mathjax : true
---
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

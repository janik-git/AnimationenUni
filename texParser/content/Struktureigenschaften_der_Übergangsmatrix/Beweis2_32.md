---
 title: "Beweis2_32"
 mathjax : true
---
Für $\lambda \in (0,1)$ folgt aus dem Satz von Lebesgue
$$R(\lambda) = \sum_{n=0}^{\infty} \lambda^{n} p_{n}(0,0) = \sum_{n = 0}^{\infty} \lambda^{n} (2 \pi)^{-d}  \int_{[-\pi, \pi)^{d}} {\varphi (t)}^{n} \diff t$$
$$= (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \sum_{n=0}^{\infty} {\lambda \varphi (t)}^{n} \diff t = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \dfrac{1}{1 - \lambda \varphi(t)} \diff t$$
Da die linke Seite rein reel ist, folgt somit
$$R(\lambda) = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \mathfrak{R}({\dfrac{1}{1 - \lambda \varphi(t)}}) \diff t$$
Da nun aber $G(0,0) = \lim \limits_{\lambda \uparrow 1} R(\lambda)$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, so folgt die
Behauptung aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ und Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$.
---
 title: "Beweis2_32"
 mathjax : true
---
Für $\lambda \in (0,1)$ folgt aus dem Satz von Lebesgue
$$R(\lambda) = \sum_{n=0}^{\infty} \lambda^{n} p_{n}(0,0) = \sum_{n = 0}^{\infty} \lambda^{n} (2 \pi)^{-d}  \int_{[-\pi, \pi)^{d}} {\varphi (t)}^{n} \diff t$$
$$= (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \sum_{n=0}^{\infty} {\lambda \varphi (t)}^{n} \diff t = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \dfrac{1}{1 - \lambda \varphi(t)} \diff t$$
Da die linke Seite rein reel ist, folgt somit
$$R(\lambda) = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \mathfrak{R}({\dfrac{1}{1 - \lambda \varphi(t)}}) \diff t$$
Da nun aber $G(0,0) = \lim \limits_{\lambda \uparrow 1} R(\lambda)$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, so folgt die
Behauptung aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ und Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$.Für
$\lambda \in (0,1)$ folgt aus dem Satz von Lebesgue
$$R(\lambda) = \sum_{n=0}^{\infty} \lambda^{n} p_{n}(0,0) = \sum_{n = 0}^{\infty} \lambda^{n} (2 \pi)^{-d}  \int_{[-\pi, \pi)^{d}} {\varphi (t)}^{n} \diff t$$
$$= (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \sum_{n=0}^{\infty} {\lambda \varphi (t)}^{n} \diff t = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \dfrac{1}{1 - \lambda \varphi(t)} \diff t$$
Da die linke Seite rein reel ist, folgt somit
$$R(\lambda) = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \mathfrak{R}({\dfrac{1}{1 - \lambda \varphi(t)}}) \diff t$$
Da nun aber $G(0,0) = \lim \limits_{\lambda \uparrow 1} R(\lambda)$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, so folgt die
Behauptung aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ und Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$.

**Beispiel 2.13**\[Einfache, symmtetrische Irrfahrt auf
$\mathbb{Z}^{d}$\] Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette
mit Zustandsraum $E= \mathbb{Z}^{d}$ und Übergangsmatrix
$P = (p(x,y))_{x,y \in E}$ mit $$p(x,y)=
\begin{cases}
\dfrac{1}{2d} & , \vert \vert x - y \vert \vert = 1\\
& \\
0 & , \mathrm{sonst}
\end{cases}$$ Dann gilt
$$\varphi (t) = \sum_{x \in E} e^{i \langle t,x \rangle} p(0,x) = \dfrac{1}{d} \sum_{i=1}^{d} \cos(t_{i})$$
Da aber
$$\dfrac{s^{2}}{6} \leq 1 - \cos(s) \leq \dfrac{s^{2}}{2} \qquad \forall \: s \in [- \pi, \pi)$$
so ist nach $\ref{Chung-Fuchs}$ der Zustand $x=0$ und wegen der
Irreduzibilität damit nach Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$ jeder
Zustand genau dann rekurrent, wenn für jedes $\epsilon > 0$
$$\int_{{\vert \vert t \vert \vert}_{2} < \epsilon} \dfrac{1}{{\vert \vert t \vert \vert}_{2}} \diff t = c_{d} \int_{0}^{\epsilon} r^{d-1} r^{-2} \diff r = \infty \quad \Leftrightarrow \quad d \leq 2$$
D.h. die einfache, symmetrische Irrfahrt auf $\mathbb{Z}^{d}$ ist für
$d \leq 2$ rekurrent und für $d>2$ transient.
---
 title: "Beweis2_32"
 mathjax : true
---
Für $\lambda \in (0,1)$ folgt aus dem Satz von Lebesgue
$$R(\lambda) = \sum_{n=0}^{\infty} \lambda^{n} p_{n}(0,0) = \sum_{n = 0}^{\infty} \lambda^{n} (2 \pi)^{-d}  \int_{[-\pi, \pi)^{d}} {\varphi (t)}^{n} \diff t$$
$$= (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \sum_{n=0}^{\infty} {\lambda \varphi (t)}^{n} \diff t = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \dfrac{1}{1 - \lambda \varphi(t)} \diff t$$
Da die linke Seite rein reel ist, folgt somit
$$R(\lambda) = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \mathfrak{R}({\dfrac{1}{1 - \lambda \varphi(t)}}) \diff t$$
Da nun aber $G(0,0) = \lim \limits_{\lambda \uparrow 1} R(\lambda)$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, so folgt die
Behauptung aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ und Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$.Für
$\lambda \in (0,1)$ folgt aus dem Satz von Lebesgue
$$R(\lambda) = \sum_{n=0}^{\infty} \lambda^{n} p_{n}(0,0) = \sum_{n = 0}^{\infty} \lambda^{n} (2 \pi)^{-d}  \int_{[-\pi, \pi)^{d}} {\varphi (t)}^{n} \diff t$$
$$= (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \sum_{n=0}^{\infty} {\lambda \varphi (t)}^{n} \diff t = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \dfrac{1}{1 - \lambda \varphi(t)} \diff t$$
Da die linke Seite rein reel ist, folgt somit
$$R(\lambda) = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \mathfrak{R}({\dfrac{1}{1 - \lambda \varphi(t)}}) \diff t$$
Da nun aber $G(0,0) = \lim \limits_{\lambda \uparrow 1} R(\lambda)$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, so folgt die
Behauptung aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ und Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$.

**Beispiel 2.13**\[Einfache, symmtetrische Irrfahrt auf
$\mathbb{Z}^{d}$\] Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette
mit Zustandsraum $E= \mathbb{Z}^{d}$ und Übergangsmatrix
$P = (p(x,y))_{x,y \in E}$ mit $$p(x,y)=
\begin{cases}
\dfrac{1}{2d} & , \vert \vert x - y \vert \vert = 1\\
& \\
0 & , \mathrm{sonst}
\end{cases}$$ Dann gilt
$$\varphi (t) = \sum_{x \in E} e^{i \langle t,x \rangle} p(0,x) = \dfrac{1}{d} \sum_{i=1}^{d} \cos(t_{i})$$
Da aber
$$\dfrac{s^{2}}{6} \leq 1 - \cos(s) \leq \dfrac{s^{2}}{2} \qquad \forall \: s \in [- \pi, \pi)$$
so ist nach $\ref{Chung-Fuchs}$ der Zustand $x=0$ und wegen der
Irreduzibilität damit nach Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$ jeder
Zustand genau dann rekurrent, wenn für jedes $\epsilon > 0$
$$\int_{{\vert \vert t \vert \vert}_{2} < \epsilon} \dfrac{1}{{\vert \vert t \vert \vert}_{2}} \diff t = c_{d} \int_{0}^{\epsilon} r^{d-1} r^{-2} \diff r = \infty \quad \Leftrightarrow \quad d \leq 2$$
D.h. die einfache, symmetrische Irrfahrt auf $\mathbb{Z}^{d}$ ist für
$d \leq 2$ rekurrent und für $d>2$ transient.Für $\lambda \in (0,1)$
folgt aus dem Satz von Lebesgue
$$R(\lambda) = \sum_{n=0}^{\infty} \lambda^{n} p_{n}(0,0) = \sum_{n = 0}^{\infty} \lambda^{n} (2 \pi)^{-d}  \int_{[-\pi, \pi)^{d}} {\varphi (t)}^{n} \diff t$$
$$= (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \sum_{n=0}^{\infty} {\lambda \varphi (t)}^{n} \diff t = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \dfrac{1}{1 - \lambda \varphi(t)} \diff t$$
Da die linke Seite rein reel ist, folgt somit
$$R(\lambda) = (2\pi)^{-d}  \int_{[-\pi, \pi)^{d}} \mathfrak{R}({\dfrac{1}{1 - \lambda \varphi(t)}}) \diff t$$
Da nun aber $G(0,0) = \lim \limits_{\lambda \uparrow 1} R(\lambda)$ und
$(X_{n})_{n \in \mathbb{N}_{0}}$ irreduzibel ist, so folgt die
Behauptung aus Satz
$\ref{alternative Chrakterisierung von rekurrent/transient}$ und Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$.

**Beispiel 2.13**\[Einfache, symmtetrische Irrfahrt auf
$\mathbb{Z}^{d}$\] Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine Markovkette
mit Zustandsraum $E= \mathbb{Z}^{d}$ und Übergangsmatrix
$P = (p(x,y))_{x,y \in E}$ mit $$p(x,y)=
\begin{cases}
\dfrac{1}{2d} & , \vert \vert x - y \vert \vert = 1\\
& \\
0 & , \mathrm{sonst}
\end{cases}$$ Dann gilt
$$\varphi (t) = \sum_{x \in E} e^{i \langle t,x \rangle} p(0,x) = \dfrac{1}{d} \sum_{i=1}^{d} \cos(t_{i})$$
Da aber
$$\dfrac{s^{2}}{6} \leq 1 - \cos(s) \leq \dfrac{s^{2}}{2} \qquad \forall \: s \in [- \pi, \pi)$$
so ist nach $\ref{Chung-Fuchs}$ der Zustand $x=0$ und wegen der
Irreduzibilität damit nach Satz
$\ref{rekkurent und x -> y so gilt y -> x und y rekurrent}$ jeder
Zustand genau dann rekurrent, wenn für jedes $\epsilon > 0$
$$\int_{{\vert \vert t \vert \vert}_{2} < \epsilon} \dfrac{1}{{\vert \vert t \vert \vert}_{2}} \diff t = c_{d} \int_{0}^{\epsilon} r^{d-1} r^{-2} \diff r = \infty \quad \Leftrightarrow \quad d \leq 2$$
D.h. die einfache, symmetrische Irrfahrt auf $\mathbb{Z}^{d}$ ist für
$d \leq 2$ rekurrent und für $d>2$ transient.

**Beispiel 2.13**\[Symmetrische Irrfahrt auf $\mathbb{Z}$ mit 2.
Moment\] Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine irreduzible
Markovkette auf $E=\mathbb{Z}$ mit Übergangswahrscheinlichkeit
$p(x,y) = \mu (y-x)$, wobei das Wahrscheinlichkeitsmaß $\mu$ folgende
Eigenschaft besitzt
$$\mu (x) = \mu (-x) \qquad und \qquad \sum_{x \in \mathbb{Z}} x^{2} \mu(x) =: c_{1} < \infty$$
Dann gilt
$$\varphi(t) = \sum_{x \in \mathbb{Z}} e^{itx} \mu(x) = \dfrac{1}{2} \sum_{x \in \mathbb{Z}} \left( e^{itx} \mu(x) + e^{-itx} \mu(-x)  \right) \stackrel{\mu (x) = \mu (-x)}{=} \sum_{x \in \mathbb{Z}} \cos(tx)\mu(x)$$
Aus der Taylorentwicklung der Kosinusfunktion folgt
$\cos(s) \geq 1 - \dfrac{1}{2} s^{2}$. Also
$$\varphi(t) \geq  \sum_{x \in \mathbb{Z}} \left( 1 - \dfrac{t^{2}}{2} x^{2}\right) \mu(x) = 1 - \dfrac{c_{1}}{2} t^{2}$$
Damit erhält man
$$\lim_{\lambda \uparrow 1} \int_{-\pi}^{\pi} \mathfrak{R}(1 - \lambda \varphi(t))^{-1} \diff t \stackrel{\mathrm{Fatou}}{\geq} \int_{-\pi}^{\pi} (1 -  \varphi(t))^{-1} \diff t \geq 2 \int_{0}^{\pi} \dfrac{2}{c_{1} t^{2}} \diff t = \infty$$
Somit folgt aus dem Satz von Chung-Fuchs (Satz $\ref{Chung-Fuchs}$),
dass die Irrfahrt $(X_{n})_{n \in \mathbb{N}_{0}}$ rekurrent ist.

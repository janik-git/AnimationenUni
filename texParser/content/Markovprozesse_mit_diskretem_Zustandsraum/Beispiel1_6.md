---
 title: "Beispiel1_6"
 mathjax : true
---
Sei $(Y_{n})_{n \in \mathbb{N}_{0}}$ eine Folge u.i.v. Zufallsvariablen
mit\
$\mathbb{P}[Y_{1} = 1] = \mathbb{P}[Y_{1} = -1] =\dfrac{1}{2}$. Setze
$X_{0} = 1$ und $X_{n} = Y_{n}, n \in \mathbb{N}$. Dann besitzt
$(X_{n})_{n \in \mathbb{N}_{0}}$ wegen Beispiel 1.3 die zeithomogene
Markoveigenschaft und ist somit wegen Bemerkung 1.6 eine Markovkette auf
dem Zustandsraum $E = \lbrace -1,+1  \rbrace$ mit Startverteilung
$\nu = \mathbbm{1}_{\lbrace 1 \rbrace}$ und Übergangsmatrix
$$P =(p(x,y))_{x,y \in E} \: \: \:  und \: \: \: p(x,y) = \dfrac{1}{2}$$
---
 title: "Beispiel1_6"
 mathjax : true
---
Sei $(Y_{n})_{n \in \mathbb{N}_{0}}$ eine Folge u.i.v. Zufallsvariablen
mit\
$\mathbb{P}[Y_{1} = 1] = \mathbb{P}[Y_{1} = -1] =\dfrac{1}{2}$. Setze
$X_{0} = 1$ und $X_{n} = Y_{n}, n \in \mathbb{N}$. Dann besitzt
$(X_{n})_{n \in \mathbb{N}_{0}}$ wegen Beispiel 1.3 die zeithomogene
Markoveigenschaft und ist somit wegen Bemerkung 1.6 eine Markovkette auf
dem Zustandsraum $E = \lbrace -1,+1  \rbrace$ mit Startverteilung
$\nu = \mathbbm{1}_{\lbrace 1 \rbrace}$ und Übergangsmatrix
$$P =(p(x,y))_{x,y \in E} \: \: \:  und \: \: \: p(x,y) = \dfrac{1}{2}$$Sei
$(Y_{n})_{n \in \mathbb{N}_{0}}$ eine Folge u.i.v. Zufallsvariablen mit\
$\mathbb{P}[Y_{1} = 1] = \mathbb{P}[Y_{1} = -1] =\dfrac{1}{2}$. Setze
$X_{0} = 1$ und $X_{n} = Y_{n}, n \in \mathbb{N}$. Dann besitzt
$(X_{n})_{n \in \mathbb{N}_{0}}$ wegen Beispiel 1.3 die zeithomogene
Markoveigenschaft und ist somit wegen Bemerkung 1.6 eine Markovkette auf
dem Zustandsraum $E = \lbrace -1,+1  \rbrace$ mit Startverteilung
$\nu = \mathbbm{1}_{\lbrace 1 \rbrace}$ und Übergangsmatrix
$$P =(p(x,y))_{x,y \in E} \: \: \:  und \: \: \: p(x,y) = \dfrac{1}{2}$$

**Beispiel 1.7**\[Irrfahrt auf $\mathbb{Z}$\] Sei $E = \mathbb{Z}$ mit\
\
$p(x,y)=
\begin{cases}
\dfrac{1}{2} &  |x - y| = 1\\
0 & sonst
\end{cases}$\
\
Diese Markovkette beschreibt ein Teilchen, das pro Zeiteinheit auf
$\mathbb{Z}$ um eins nach rechts oder links springt, und zwar immer mit
Wahrscheinlichkeit $\dfrac{1}{2}$. Die Übergangsmatrix
$P = (p(x,y))_{x,y \in \mathbb{Z}}$ ist dann eine unendlich große
Triagonalmatrix, die auf der Hauptdiagonalen ausschließlich Nullen hat
und auf den beiden Nebendiagonalen immer den Wert $\dfrac{1}{2}$. Das
Anfangsstück eines Pfades der symmetrischen Irrfahrt (mit Start in Null)
kann zum Beispiel so aussehen (linear interpoliert):

. ![Realisierung einer symmetrischen Irrfahrt](beispiel18 "fig:")
---
 title: "Beispiel1_6"
 mathjax : true
---
Sei $(Y_{n})_{n \in \mathbb{N}_{0}}$ eine Folge u.i.v. Zufallsvariablen
mit\
$\mathbb{P}[Y_{1} = 1] = \mathbb{P}[Y_{1} = -1] =\dfrac{1}{2}$. Setze
$X_{0} = 1$ und $X_{n} = Y_{n}, n \in \mathbb{N}$. Dann besitzt
$(X_{n})_{n \in \mathbb{N}_{0}}$ wegen Beispiel 1.3 die zeithomogene
Markoveigenschaft und ist somit wegen Bemerkung 1.6 eine Markovkette auf
dem Zustandsraum $E = \lbrace -1,+1  \rbrace$ mit Startverteilung
$\nu = \mathbbm{1}_{\lbrace 1 \rbrace}$ und Übergangsmatrix
$$P =(p(x,y))_{x,y \in E} \: \: \:  und \: \: \: p(x,y) = \dfrac{1}{2}$$Sei
$(Y_{n})_{n \in \mathbb{N}_{0}}$ eine Folge u.i.v. Zufallsvariablen mit\
$\mathbb{P}[Y_{1} = 1] = \mathbb{P}[Y_{1} = -1] =\dfrac{1}{2}$. Setze
$X_{0} = 1$ und $X_{n} = Y_{n}, n \in \mathbb{N}$. Dann besitzt
$(X_{n})_{n \in \mathbb{N}_{0}}$ wegen Beispiel 1.3 die zeithomogene
Markoveigenschaft und ist somit wegen Bemerkung 1.6 eine Markovkette auf
dem Zustandsraum $E = \lbrace -1,+1  \rbrace$ mit Startverteilung
$\nu = \mathbbm{1}_{\lbrace 1 \rbrace}$ und Übergangsmatrix
$$P =(p(x,y))_{x,y \in E} \: \: \:  und \: \: \: p(x,y) = \dfrac{1}{2}$$

**Beispiel 1.7**\[Irrfahrt auf $\mathbb{Z}$\] Sei $E = \mathbb{Z}$ mit\
\
$p(x,y)=
\begin{cases}
\dfrac{1}{2} &  |x - y| = 1\\
0 & sonst
\end{cases}$\
\
Diese Markovkette beschreibt ein Teilchen, das pro Zeiteinheit auf
$\mathbb{Z}$ um eins nach rechts oder links springt, und zwar immer mit
Wahrscheinlichkeit $\dfrac{1}{2}$. Die Übergangsmatrix
$P = (p(x,y))_{x,y \in \mathbb{Z}}$ ist dann eine unendlich große
Triagonalmatrix, die auf der Hauptdiagonalen ausschließlich Nullen hat
und auf den beiden Nebendiagonalen immer den Wert $\dfrac{1}{2}$. Das
Anfangsstück eines Pfades der symmetrischen Irrfahrt (mit Start in Null)
kann zum Beispiel so aussehen (linear interpoliert):

. ![Realisierung einer symmetrischen Irrfahrt](beispiel18 "fig:")

Sei $(Y_{n})_{n \in \mathbb{N}_{0}}$ eine Folge u.i.v. Zufallsvariablen
mit\
$\mathbb{P}[Y_{1} = 1] = \mathbb{P}[Y_{1} = -1] =\dfrac{1}{2}$. Setze
$X_{0} = 1$ und $X_{n} = Y_{n}, n \in \mathbb{N}$. Dann besitzt
$(X_{n})_{n \in \mathbb{N}_{0}}$ wegen Beispiel 1.3 die zeithomogene
Markoveigenschaft und ist somit wegen Bemerkung 1.6 eine Markovkette auf
dem Zustandsraum $E = \lbrace -1,+1  \rbrace$ mit Startverteilung
$\nu = \mathbbm{1}_{\lbrace 1 \rbrace}$ und Übergangsmatrix
$$P =(p(x,y))_{x,y \in E} \: \: \:  und \: \: \: p(x,y) = \dfrac{1}{2}$$

**Beispiel 1.7**\[Irrfahrt auf $\mathbb{Z}$\] Sei $E = \mathbb{Z}$ mit\
\
$p(x,y)=
\begin{cases}
\dfrac{1}{2} &  |x - y| = 1\\
0 & sonst
\end{cases}$\
\
Diese Markovkette beschreibt ein Teilchen, das pro Zeiteinheit auf
$\mathbb{Z}$ um eins nach rechts oder links springt, und zwar immer mit
Wahrscheinlichkeit $\dfrac{1}{2}$. Die Übergangsmatrix
$P = (p(x,y))_{x,y \in \mathbb{Z}}$ ist dann eine unendlich große
Triagonalmatrix, die auf der Hauptdiagonalen ausschließlich Nullen hat
und auf den beiden Nebendiagonalen immer den Wert $\dfrac{1}{2}$. Das
Anfangsstück eines Pfades der symmetrischen Irrfahrt (mit Start in Null)
kann zum Beispiel so aussehen (linear interpoliert):

. ![Realisierung einer symmetrischen Irrfahrt](beispiel18 "fig:")

**Beispiel 1.7**\[Irrfahrt auf $\mathbb{Z}^{d}$\] Sei $\mu$ eine
Wahrscheinlichkeitsverteilung auf $\mathbb{Z}^{d}$ . Setze
$$p(x,y) = \mu(x-y) \qquad \forall \: x,y \in \mathbb{Z}^{d}$$
Offensichtlich ist $P =(p(x,y))_{x,y \in \mathbb{Z}^d}$ eine
stochastische Matrix. Dann nennt man
$(\mathbbm{1}_{x},\mathbb{P})$-Markovkette
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine Irrfahrt(random walk) auf
$\mathbb{Z}^{d}$ mit Start in $x \in \mathbb{Z}^{d}$. Im Spezialfall,
dass $$\mu(x)=
\begin{cases}
\dfrac{1}{2d} &  ,|x|=1\\
0 & ,\mathrm{sonst}
\end{cases}$$ nennt man $(X_{n})_{n \in \mathbb{N}_{0}}$ eine einfache,
symmetrische Irrfahrt.

. ![Symmetrische Irrfahrt auf $\mathbb{Z}^2$](beispiel17(2) "fig:")

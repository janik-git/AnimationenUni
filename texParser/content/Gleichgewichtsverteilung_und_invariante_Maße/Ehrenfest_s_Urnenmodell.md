---
 title: "Ehrenfest_s_Urnenmodell"
 mathjax : true
---
In zwei Urnen liegen N Kugeln. Zu jedem Zeitpunkt $n \in \mathbb{N}$
wird eine Kugel zufällig mit gleicher Wahrscheinlichkeit ausgewählt, die
die Urne dann wechselt. Die Anzahl der Kugeln in der ersten Urne wird
durch die Markovkette $(X_{n})_{n \in \mathbb{N}_{0}}$ mit Zustandsraum
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

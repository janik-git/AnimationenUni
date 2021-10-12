---
 title: "Chapman-Kolmogorov_Gleichung"
 mathjax : true
---
[\[Chapman-Kolmogorov Gleichung\]]{#Chapman-Kolmogorov Gleichung
label="Chapman-Kolmogorov Gleichung"} Für jede stochastische Matrix
$P =(p(x,y))_{x,y \in E}$ sei $P^{n} =(p_{n}(x,y))_{x,y \in E}$,
$n \in \mathbb{N}_{0}$. Dann gilt für alle $m,n \in \mathbb{N}_{0}$
$$p_{m+n} (x,y) = \sum_{z \in E} \: p_{m}(x,z) p_{n}(z,y) \qquad \forall \: x,y \in E$$
---
 title: "Chapman-Kolmogorov_Gleichung"
 mathjax : true
---
[\[Chapman-Kolmogorov Gleichung\]]{#Chapman-Kolmogorov Gleichung
label="Chapman-Kolmogorov Gleichung"} Für jede stochastische Matrix
$P =(p(x,y))_{x,y \in E}$ sei $P^{n} =(p_{n}(x,y))_{x,y \in E}$,
$n \in \mathbb{N}_{0}$. Dann gilt für alle $m,n \in \mathbb{N}_{0}$
$$p_{m+n} (x,y) = \sum_{z \in E} \: p_{m}(x,z) p_{n}(z,y) \qquad \forall \: x,y \in E$$
$$\bbordermatrix{
  & A   & B   & C  \cr
A & 0 & 0.5 & 0.5 \cr
B & 1 & 0 & 0 \cr
C & 0.5 & 0.5 & 0  \cr
}$$ Man kann leicht nachprüfen, dass $P$ den Anforderungen in Definition
1.8 genügt. Im weiteren seien wir an $p_{2}(A,A)$ interessiert. Also der
Wahrscheinlichkeit, nach zwei Durchläufen wieder im Startpunkt A zu
sein. Chapman-Kolmogorov liefert uns:
$$p_{2} (A,A) = \sum_{z \in E} \: p_{1}(A,z) p_{1}(z,A)$$
$$= p(A,A) \: \cdot \: p(A,A) \: + \: p(A,B) \: \cdot \: p(B,A) \: + \: p(A,C) \: \cdot \: p(C,A) = 0.75$$
Wobei hier alle Möglichkeiten von A nach A in zwei Durchläufen zu
gelangen betrachtet wurden. Ist man ferner an der Matrix $P^{2}$
interessiert, so ist es demnach hinreichend $P = P \cdot P$ zu berechnen

                                                                                $\begin{bmatrix} 0 & 0.5 & 0.5 \\ 1 & 0 & 0 \\ 0.5 & 0.5 & 0 \end{bmatrix}$
  ----------------------------------------------------------------------------- ------------------------------------------------------------------------------------------
                                                                                
   $\begin{bmatrix} 0 & 0.5 & 0.5 \\ 1 & 0 & 0 \\ 0.5 & 0.5 & 0 \end{bmatrix}$  $\begin{bmatrix} \textcolor{red} {0 \cdot 0 + 0.5 \cdot 1 + 0.5 \cdot 0.5 }& 0.25 & 0\\ 
                                                                                                 0 & 0.5 & 0.5 \\ 
                                                                                                  0.5 & 0.25 & 0.25    \end{bmatrix}$

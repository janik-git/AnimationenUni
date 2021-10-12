import re 
x= r"""\begin{defi}[Stochastischer Prozess]
Ein stochastischer Prozess auf $(\Omega, \mathfrak{F}, \mathbb{P})$ mit Werten im Zustandsraum $(E, \varepsilon)$ ist eine Familie $(X_{t})_{t\in I}$ von E-wertigen Zufallsvariablen. Für festes $\omega \in \Omega$ heißt die Abbildung
\\
\begin{equation*}
I \ni t \mapsto X_{t}(\omega)
\end{equation*}
\\
eine Trajektorie(Pfad, Realisierung) von $(X_{t})_{t\in I}$. Falls I = $\mathbb{N}_{0}$ oder I = $[0,\infty)$, so heißt die Verteilung von $X_{0}$ die Startverteilung des stochastischen Prozesses.
\end{defi}
\begin{bem}
Falls E diskret ist, so bezeichnet man eine Verteilung auch als Wahrscheinlichkeitsvektor.
\end{bem} 
"""

def clean(string,theorems,sectionIndex):
    newString = string[:]
    for pat,rep in theorems.items():
        regex = rf".*\{{{pat}}}"
        results = re.findall(regex,string)
        for res in results:
            if "begin" in res :
                newString = newString.replace(res,fr"\textbf{{{rep[0]} {sectionIndex}.{rep[1]}}}")
            else:
                newString = newString.replace(res,"")
    return newString
# toReplace= {"defi":["Definition",1]}
# s = clean(x,toReplace)
# print(s)

import itertools
from math import sqrt
from manim import *
from numpy.ma.core import left_shift 
import pydtmc.markov_chain as mark
import itertools
from fractions import Fraction
class Ani(Scene):
    def construct(self):
        sc1 = MarkovMatrix()
        sc2 = MarkovGraph()
        sc1.construct()
        sc2.construct()
class MarkovMatrix(Scene):
    def construct(self):
        transition_matrix=np.array(
            [
                ["1/2","1/2","0"],
                ["1/3","1/3","1/3"],
                ["1","0","0"]
            ]
        )

        matrix = self.transitionMatrix(transition_matrix).scale(1)
        title = Tex("Übergangsmatrix").shift(UP*3)
        P = Tex("P = ")
        P.next_to(matrix,LEFT)
        self.add(matrix,P,title)
        self.wait(2)
        self.clear()
    def transitionMatrix(self,transition_matrix):
        return Matrix(transition_matrix)
class MarkovGraph(GraphScene):
    CONFIG = {
        "y_axis_label": r"State",
        "x_axis_labe": "Time"
    }
    def construct1(self):
        transition_matrix=np.array(
            [
                ["1/2","1/2","0"],
                ["1/3","1/3","1/3"],
                ["1","0","0"]
            ]
        )

        matrix = self.transitionMatrix(transition_matrix).scale(1)
        title = Tex("Übergangsmatrix").shift(UP*3)
        P = Tex("P = ")
        P.next_to(matrix,LEFT)
        self.add(matrix,P,title)
        self.wait(3)
        self.clear()
    def markovChain(self,p,states):
        return mark.MarkovChain(p,states)
    def createNode(self,state):
        node = Circle(radius=0.5,color=YELLOW).set_fill(YELLOW,opacity=0.5)
        nodeText = Tex(state).move_to(node.get_center()) 
        return VGroup(node,nodeText)
        
    def drawCurvedArrows(self,start,end,p,leftOrRight=1):
        arrow = CurvedArrow(start_point=start,end_point=end).scale(1.1)
        prob  = MathTex(rf"{p}").scale(0.7)
        prob.move_to(arrow.get_center()+[leftOrRight*-0.5,0.1,0])
        return VGroup(arrow,prob)
    def drawArrows(self,start,end,p,leftOrRight):
        arrow = Arrow(start,end).scale(0.9)
        prob  = MathTex(rf"{p}").scale(0.7)
        cS = start.get_center()
        cE = end.get_center()
        if np.isclose(cS[1],cE[1],atol=0.0001):
            arrow.shift([0,leftOrRight*0.2,0])
            prob.move_to(arrow.get_center()+[0,leftOrRight*0.3,0])
        else:
            arrow.shift([leftOrRight*0.2,0,0])
            prob.move_to(arrow.get_center()+[leftOrRight * 0.5,0,0])
        return VGroup(arrow,prob)
    def createDiagramm(self,states,transition_matrix):
        diagramm = Triangle().scale(3)
        nodes = [(s,self.createNode(s)) for s in states ]
        # print(nodes[0][0].get_all_points())
        vertices = diagramm.get_vertices()
        for i, n in enumerate(nodes) : 
            n[1].move_to(vertices[i])
        arrows = []
        for comb in itertools.product(range(len(nodes)),range(len(nodes))):
            leftOrRight = 1
            if comb[0]>comb[1]:
               leftOrRight =-1 
            if comb[0]==comb[1]:
                if nodes[comb[0]][1][0].get_center()[0]-2.5>0:
                    arrow = self.drawCurvedArrows(start=nodes[comb[0]][1][0].get_all_points()[-4],end=nodes[comb[1]][1][0].get_all_points()[-27],p=transition_matrix[comb],leftOrRight=-1)
                    arrow.shift([0.4,0,0])
                else:
                    arrow = self.drawCurvedArrows(start=nodes[comb[0]][1][0].get_all_points()[4],end=nodes[comb[1]][1][0].get_all_points()[27],p=transition_matrix[comb])
                    arrow.shift([-1,0,0])
            else:
                arrow = self.drawArrows(start=nodes[comb[0]][1][0],end=nodes[comb[1]][1][0],p=transition_matrix[comb],leftOrRight=leftOrRight)                 
            arrows.append((comb,arrow))
            # print(comb)
        return VGroup(VDict(nodes),VDict(arrows,show_keys=False))
    def transitionMatrix(self,transition_matrix):
        return Matrix(transition_matrix)
    def graph(self,steps):
        grid = Axes(
            x_range = [0,steps,1],
            y_range = [1,3,1],
            x_length= sqrt(steps) ,
            y_length= 3,
            tips=False
        )
        grid.add_coordinates([],[1,2,3],None)
        return grid
    def construct(self):
        self.construct1()
        transition_matrix=np.array(
            [
                ["1/2","1/2","0"],
                ["1/3","1/3","1/3"],
                ["1","0","0"]
            ]
        )
        invariantMeasure =  [4/8,3/8,1/8]
        invariantMeasureText = MathTex("\pi = ")
        STEPS = 25
        graph =  self.graph(25).scale(0.6).shift(RIGHT*3)
        self.add(graph)
        transition_matrixFloat = [list(map(lambda x :float(Fraction(x)),t )) for t in transition_matrix]
        diagram = self.createDiagramm(['1','2','3'],transition_matrix).scale(0.5).shift(LEFT*2)
        self.add(diagram)
        mc = self.markovChain(transition_matrixFloat,['1','2','3'])
        dot = Dot(color=RED).scale(2)
        #MARKOVCHAIN 
        mcString = mc.walk(steps=STEPS)
        currentState = mcString[0]
        #GRAPH INITIAL STATE
        self.add(Dot(point=graph.c2p(0,int(currentState),0)))  
        
        matrix = self.transitionMatrix(transition_matrix).scale(0.4)
        self.add(matrix.move_to([-5,3,0]))
        for i,state in enumerate(mcString[1:]):
            self.add(Dot(point=graph.c2p(i+1,int(state),0)))
            path = (int(currentState)-1,int(state)-1)
            diagram[1][path][0].set_color(RED)
            diagram[0][state].set_color(RED)
            self.play(MoveAlongPath(dot,diagram[1][path][0]),rate_func=rate_functions.rush_from)
            # self.play(Flash(diagram[0][state],0.5,color=RED,run_time=0.5))
            diagram[1][path].set_color(WHITE)
            diagram[0][state].set_color(YELLOW)
            currentState = state
            #ADD POINT ON GRAPH
        bar = BarChart(
            [mcString.count(i) for i in ['1','2','3']],
            height=5 , 
            width = 3,
            max_value= 25 , 
            bar_names = ["1","2","3"]

        ).scale(0.7).shift(LEFT)
        self.remove(diagram,dot)
        self.add(bar)
        invMeasureRow = MathTex(invariantMeasure).scale(0.6)
        invariantMeasureText.next_to(invMeasureRow,LEFT)
        invMeasure = VGroup(invMeasureRow,invariantMeasureText)
        invMeasure.shift(LEFT*4)
        self.add(invMeasure)
        self.wait(3)
# self.wait(5)
        

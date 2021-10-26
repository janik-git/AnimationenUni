
from manim import * 
import scipy.stats as st 
import numpy as np 
import collections
class MCI(Scene):
    def f1(self,x):
        return -x**2 + 4 
    def construct(self):
        title = Text("Analytical").move_to([-3,2,0]).scale(0.8)
        ax1 = Axes(
                y_range=[-4.5,4.5,1],
                x_range=[-3.5,3.5,1],
                x_axis_config={"numbers_to_include":[-2,2]},
                tips = False,
            ).scale(0.4).move_to([3,2,0]) 

        c1 = ax1.get_graph(self.f1,x_range=[-2.5,2.5,1],color=BLUE_C)
        f1Text = MathTex(r"-x^{2} + 3").move_to([4,3.3,0]).scale(0.5)
        area1 = ax1.get_area(
             c1,
             x_range=(-2,2),
             color=GREEN_B,
            opacity = 0.6
        ).scale(0.95) 
        self.add(ax1,c1,f1Text,area1,title)
        self.wait(1)
        eq1= MathTex(r"\int_{-2}^{2} -x^{2}+4 =  10.66").move_to([-3,-1,0]).scale(0.8)
        self.play(Transform(area1,eq1))    
        self.wait(2)
        self.clear()
        title = Text("Monte-Carlo").move_to([-3,2,0]).scale(0.8)
        self.add(title,ax1,c1,f1Text)
        #MONTECARLO INTEGRATION
        a=-2
        b= 2 
        n = 1000 
        _error = []
        for N in  [10,100,1000,10_000,100_000,1_000_000]:
            U = np.random.uniform(0,1,(N,n))
            u_func = self.f1(a+(b-a)*U)
            s = ((b-a)/n)*u_func.sum(axis=1)
            _error.append(s-10.66)
            if N==10:
                string =  "["
                for i in U[0][:4]:
                    string += str(round(i,2)) + ","
                string += "\ldots ]"
                uText = MathTex("U=" + string).scale(0.7).shift(LEFT*2)
                lines = []
                for i in (a+(b-a)*U[0][:10]): 
                    l = ax1.get_vertical_line(ax1.i2gp(i,c1),color=YELLOW)
                    lines.append(l) 
                lines = VGroup(*lines)
                self.add(uText)
                self.wait(0.5)
                self.play(Transform(uText,lines))
                self.wait(0.5)
                formula = MathTex(r"\frac{b-a}{1000} \sum_{k=1}^{1000} f(a+(b-a)*U_k ="+f" {round(s[0],2)}")
                self.play(Transform(lines,formula))  
                self.wait(1)
        self.clear()

        for er in  _error:
            bars = [] 
            self.clear()
            count = collections.Counter(er.round(1))
            MY = max(count.values())
            MX =  max(count.keys())
            mx =  min(count.keys()) 

            bar2 = Axes(
                    y_range=[0,MY+(MY/2),MY/10],
                    x_range=[mx-abs(mx-MX)/2,MX+abs(mx-MX)/2,MX],
                    # x_axis_config={"numbers_to_include":samples}
                    tips = False
                ).scale(0.4)
            for mean ,count in count.items():
                # print(count)
                height = (bar2.coords_to_point(mean,count)-bar2.coords_to_point(mean,0))[1]
                meanBar = Rectangle(width=(bar2.coords_to_point(mean-0.03,0)-bar2.coords_to_point(mean+0.03,0))[0],\
                                            height=height)\
                                            .move_to(bar2.coords_to_point(mean,0)+[0,height/2,0]).set_fill(WHITE,opacity=1)
                bars.append(meanBar)
            self.add(bar2,*bars)
            self.wait(1)
        self.wait(2)




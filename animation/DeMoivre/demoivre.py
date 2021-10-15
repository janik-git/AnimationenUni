
from manim import * 
import scipy.stats as st 
import numpy as np 
import collections
NumberLine.get_tick_marks = None
class DeMoivre(Scene):
    CONFIG={'distribution_mean' : 10,
    'distribution_variance' : np.sqrt(10)}
    def construct(self):
        """
            Draw two Charts one displaying the Distribution 
            the other displaying the Sample Mean and Variance 
            then run n iterations visualising the sampling on the left hand side 
            one the right hand side update the sample mean etc. 
        """
        N = 32

        samples = np.random.binomial(N,1/2,10_000)

        counts = collections.Counter(samples) 
        for N in [2,4,8,16,32,64,128,256]:
            samples = np.random.binomial(N,1/2,10_000)
            
            # axes = {i:Axes(
            #     x_range = [0,20,5],
            #     y_range=[0,0.3,0.05],
            #     tips = False 
            #     ).add_coordinates().scale(0.4) for i in range(3)}
             
            counts = collections.Counter(samples) 
            # countsSqrt = {k:v/np.sqrt(N) for k,v in counts.items()}
            nText = Text(f"N:{N}").move_to([0,0,0])
            self.add(nText)
            M = max(counts.values())
            NM = max(counts.keys())
            Nm = min(counts.keys())
            bar1 = Axes(
                y_range=[0,M*(N/10),M*(N/10)],
                x_range=[0,N,(N)/1],
                # x_axis_config={"numbers_to_include":samples}
                tips = False,
            ).scale(0.4).move_to([3,2,0])
            bar2 = Axes(
                y_range=[0,M,M],
                x_range=[0,NM+1,(NM+1)/1],
                tips=False
            ).scale(0.4).move_to([-3,-2,0])

            bar3 = Axes(
                y_range=[0,M,M],
                x_range=[Nm,NM+1,(NM+1)/1],
                tips=False
            ).scale(0.4).move_to([3,-2,0])

            bar4 = Axes(
                y_range=[0,M*(N/10),M*(N/10)],
                x_range=[0,NM+1,(NM+1)/1],
                tips=False
            ).scale(0.4).move_to([-3,2,0])
            self.add(bar1,bar2,bar3,bar4)
            bars = []
            for succ , count in counts.items(): 
                height = (bar1.coords_to_point(succ,count)-bar1.coords_to_point(succ,0))[1]
                freqBar = Rectangle(width=(bar1.coords_to_point(succ-0.05,0)-bar1.coords_to_point(succ+0.01,0))[0],\
                                            height=height)\
                                            .move_to(bar1.coords_to_point(succ,0)+[0,height/2,0]).set_fill(WHITE,opacity=1)
                self.add(freqBar)

                height = (bar2.coords_to_point(succ,count)-bar2.coords_to_point(succ,0))[1]
                freqBar = Rectangle(width=(bar2.coords_to_point(succ-0.05,0)-bar2.coords_to_point(succ+0.01,0))[0],\
                                            height=height)\
                                            .move_to(bar2.coords_to_point(succ,0)+[0,height/2,0]).set_fill(WHITE,opacity=1)
                self.add(freqBar)

                height = (bar3.coords_to_point(succ,count)-bar3.coords_to_point(succ,0))[1]
                freqBar = Rectangle(width=(bar3.coords_to_point(succ-0.05,0)-bar3.coords_to_point(succ+0.01,0))[0],\
                                            height=height)\
                                            .move_to(bar3.coords_to_point(succ,0)+[0,height/2,0]).set_fill(WHITE,opacity=1)
                self.add(freqBar)

                height = (bar4.coords_to_point(succ,count)-bar4.coords_to_point(succ,0))[1]
                freqBar = Rectangle(width=(bar4.coords_to_point(succ-0.05,0)-bar4.coords_to_point(succ+0.01,0))[0],\
                                            height=height)\
                                            .move_to(bar4.coords_to_point(succ,0)+[0,height/2,0]).set_fill(WHITE,opacity=1)
                self.add(freqBar)
            
            self.wait(1)
            self.clear()

        
        

           

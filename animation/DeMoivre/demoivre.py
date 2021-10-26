
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

        n = 10_000
        for i,N in enumerate([8,32,128,256,512]):
            mean=N*0.1
            var = np.sqrt(N*0.1*0.9)
            samples = np.random.binomial(N,0.1,n)
            s1 = samples 
            s3 = ((samples-mean)).round(1)
            s4 = ((samples-mean)/(var)).round(1)
            # 
            counts = []
            for s in [s1,s3,s4]:
                counts.append(collections.Counter(s) )
            # countsAll = {k:[v,v*np.sqrt(N),(v-mean)*np.sqrt(N),((v-mean)/(var))*np.sqrt(N)] for k,v in counts.items()}

            nText = Text(f"N:{N}").move_to([0,0,0])
            self.add(nText)
            count = counts[0]
            MN = 0.6-(i+1)*0.1
            M = [round(max(i.keys()),2) for i in counts] 
            m = [round(min(i.keys()),2) for i in counts] 
            #nothing
            bar1 = Axes(
                y_range=[0,MN,1],
                x_range=[-M[1],M[0],(M[1])/1],
                x_axis_config={"numbers_to_include":[m[1],M[1]]},
                tips = False,
            ).scale(0.4).move_to([-3,2,0])
            bar2 = Axes(
                y_range=[0,MN,1],
                x_range=[-M[1],M[1],(M[1])/1],
                x_axis_config={"numbers_to_include":[m[1],M[1]]},
                tips=False
            ).scale(0.4).move_to([3,2,0])

            bar3 = Axes(
                y_range=[0,MN,1],
                x_range=[-M[1],M[1],(M[1])/1],
                x_axis_config={"numbers_to_include":[m[1],M[1]]},
                tips=False
            ).scale(0.4).move_to([0,-2,0])

                     
            self.add(bar1,bar2,bar3)
            print(len(counts))
            for bar , count in zip([bar1,bar2,bar3],counts):
                for succ,c in count.items():
                    height = (bar.coords_to_point(succ,c/n)-bar.coords_to_point(succ,0))[1]
                    freqBar = Rectangle(width=(bar.coords_to_point(succ-0.05,0)-bar.coords_to_point(succ+0.01,0))[0],\
                                                height=height)\
                                                .move_to(bar.coords_to_point(succ,0)+[0,height/2,0]).set_fill(WHITE,opacity=1)
                    self.add(freqBar)
            
            self.wait(1)
            self.clear()

        
        

           

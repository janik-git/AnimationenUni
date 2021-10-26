from manim import * 
import scipy.stats as st 
import numpy as np 
import collections

class Poisson(Scene):
    CONFIG={'distribution_mean' : 10,
    'distribution_variance' : np.sqrt(10)}
    def poissonPdf(self,x):
        return st.poisson.pmf(x,10)
    def samplePoisson(self,samples,distribution_mean):
        return np.random.poisson(distribution_mean,samples)
    def normal(self,x):
        return st.norm.pdf(x)
    def exponetial(self,x):
        _lambda = 0.3
        return st.expon.pdf(x,scale=1/_lambda)
    def sampleExpo(self,samples,_lambda):
        return np.random.exponential(1/_lambda,samples)
    def construct(self):
        """
            Draw two Charts one displaying the Distribution 
            the other displaying the Sample Mean and Variance 
            then run n iterations visualising the sampling on the left hand side 
            one the right hand side update the sample mean etc. 
        """
        ax1 = Axes(
            x_range = [0,20,5],
            y_range=[0,0.3,0.05],
            tips = False 
            ).add_coordinates().scale(0.4).move_to([-3,2,0])
        c1 = ax1.get_graph(self.exponetial,x_range=[0,20,5],color=BLUE_C)
        ####
        # WE LOOP THROUGH GET N SAMPLES with sampel size 30, 
        # we store the sample Counts to draw the lines 
        # we store the normalized_sample_means with their frequency
        distribution_mean=1/0.3
        distribution_variance=(1/0.3)**2
        sampleMeans = {}
        for N in [10,20,40,80,160,320]:
            nText = Text(f"Amount of Individual Samples {N}").move_to([0,-3,0])
            self.add(ax1,c1,nText)
            for n in range(N): 
                sample = self.sampleExpo(300,1/distribution_mean)
                sample_mean = np.mean(sample)
                normalized_sample_mean = round(np.sqrt(N)*((sample_mean-distribution_mean)/distribution_variance),2)
                print(normalized_sample_mean)
                if normalized_sample_mean in sampleMeans:
                    sampleMeans[normalized_sample_mean].append(collections.Counter(sample))
                    sampleMeans[normalized_sample_mean][0] += 1
                else:
                    sampleMeans[normalized_sample_mean] = [1,[collections.Counter(sample)]]
            # print(sampleMeans)
            #we go through sampleMeans and counts and transform each count into lines which then Transform into the bar
            M = max(sampleMeans.values(),key=lambda x:x[0])[0]/N
            m =  min(sampleMeans.values(),key=lambda x:x[0])[0]/N
            bar2 = Axes(
                y_range=[0,M+(M/2),M/10],
                x_range=[-5,5,1],
                # x_axis_config={"numbers_to_include":samples}
                tips = False
            ).scale(0.4).move_to([3,2,0])

            self.add(bar2)
            norm = bar2.get_graph(lambda x : self.normal(x))
            # self.add(norm)
            bars = []
            for mean ,count in sampleMeans.items():
                # print(count)
                height = (bar2.coords_to_point(mean,count[0]/N)-bar2.coords_to_point(mean,0))[1]
                meanBar = Rectangle(width=(bar2.coords_to_point(mean-0.01,0)-bar2.coords_to_point(mean+0.01,0))[0],\
                                            height=height)\
                                            .move_to(bar2.coords_to_point(mean,0)+[0,height/2,0]).set_fill(WHITE,opacity=1)
                bars.append(meanBar)

            lines = VGroup(*[ax1.get_vertical_line(ax1.i2gp(i,c1),color=YELLOW) for i in list(count[1][0].keys())[:20]])
            self.play(Write(lines))
            self.play(Transform(lines,VGroup(*bars))) 
            self.wait(2) 
            self.clear() 


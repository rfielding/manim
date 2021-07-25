from manim import *
import math

            
class Xput(Scene):
    def construct(self):
        # Throughput
        form5 = MathTex(
            r"\underbrace{X_n}_{n\ \text{Worker Throughput}} = \frac{1}{T_n} = \frac{n\ \gamma}{1 + \alpha (n - 1) + \beta\ n(n - 1)}"
        )
        self.play(Write(form5))
        self.play(Wait(5))
        form5.scale(0.5)
        form5.to_corner(UP + RIGHT)

        self.meetings(5)

        blist = BulletedList(
            "Number of clients in the system is Load",
            "Throughput as a function of load is the most important metric",
            "X[n] is \"Mean Throughput at Load\"",
            "Amdahl's Law represents the simple throughput limitation"
        )
        blist.scale(0.5)
        self.add(blist)
        self.play(Wait(10))
        self.play(FadeOut(blist))    

        # show a graph of how this behaves in general
        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graphLinear = ax.get_graph(lambda n: n, color=PINK, x_range=[0,100])
        graphLimit = ax.get_graph(lambda n: 7, color=RED, x_range=[0,100])
        graphAmdahl = ax.get_graph(lambda n: (n * 1)/(1 + (1.0/7)*(n-1) + 0*n*(n-1)), color=BLUE, x_range=[0, 100])
        self.add(ax, graphLimit, graphLinear, graphAmdahl)
        self.play(Wait(10))
        self.play(FadeOut(graphLimit))
        self.play(FadeOut(graphAmdahl))
        self.play(FadeOut(graphLinear))

        self.usl(ax,7,100,1.0)
        self.usl(ax,7,100,2.0)
        self.usl(ax,14,100,2.0)
        self.usl(ax,14,200,2.0)
        self.usl(ax,14,200,1.0)
        self.usl(ax,14,800,1.0)
        self.usl(ax,28,800,1.0)

        self.play(Wait(15))

    def meetings(self, n):
        participants = []
        edges = []
        for i in range(0,n):
            r = 1
            c = r*math.cos(math.pi * i * 2.0 / n)
            s = r*math.sin(math.pi * i * 2.0 / n)
            for j in range(0,n):
                c2 = r*math.cos(math.pi * j * 2.0 / n)
                s2 = r*math.sin(math.pi * j * 2.0 / n)
                edges.append(Line(np.array([c,s,0]), np.array([c2,s2,0])))
                self.add(edges[j])

        for i in range(0,n):
            r = 1
            c = r*math.cos(math.pi * i * 2.0 / n)
            s = r*math.sin(math.pi * i * 2.0 / n)
            participants.append(Square(color=BLUE, fill_opacity=1))
            participants[i].scale(0.05)
            participants[i].shift(c*RIGHT + s*UP)
            self.add(participants[i])

        explain = MathTex(r"\beta n(n-1)")
        self.add(explain)
        explain.shift(3*LEFT)

        for i in range(0,len(edges)):
          self.play(FadeOut(edges[i]))
        for i in range(0,len(participants)):
          self.play(FadeOut(participants[i]))
        self.play(FadeOut(explain))

    def usl(self, ax,ai,bi,g):
        # Show a beta term
        newParams = MathTex(r"\gamma = %f, \alpha = \frac{1}{%d}, \beta = \frac{1}{%d}" % (g, ai, bi))
        graphAmdahl2 = ax.get_graph(lambda n: (n * g)/(1 + (1.0/ai)*(n-1) + (1.0/bi)*n*(n-1)), color=BLUE, x_range=[0, 100])
        graphLinear = ax.get_graph(lambda n: n*g, color=PINK, x_range=[0,100])
        self.add(graphAmdahl2,newParams,graphLinear)
        self.play(Wait(2))
        self.play(FadeOut(graphAmdahl2))
        self.play(FadeOut(newParams))
        self.play(FadeOut(graphLinear))

class MainScene(Scene):
    def construct(self):
        # Define gamma
        form = MathTex(
            r"\underbrace{0 < \gamma}_{\text{Worker speed}}"
        )
        self.play(Write(form))
        self.wait(5)
        form.scale(0.33)
        form.to_corner(UP + LEFT)

        form0 = MathTex(
            r"\underbrace{T_1 = \frac{1}{\gamma}}_{\text{1 Worker Time}}"
        )
        self.play(Write(form0))
        self.wait(5)
        form0.scale(0.33)
        form0.next_to(form,RIGHT)

        form1 = MathTex(
            r"\underbrace{0 \le \alpha \le 1}_{\text{Serial Fraction}}"
        )
        self.play(Write(form1))
        self.wait(5)
        form1.scale(0.33)
        form1.next_to(form0,RIGHT)

        form1a = MathTex(
            r"\underbrace{(1 - \alpha)}_{\text{Parallel Fraction}}"
        )
        self.play(Write(form1a))
        self.wait(5)
        form1a.scale(0.33)
        form1a.next_to(form1,RIGHT)

        form2 = MathTex(
            r"\underbrace{0 \le \beta}_{\text{Consensus Amount}}"
        )
        self.play(Write(form2))
        self.wait(5)
        form2.scale(0.33)
        form2.next_to(form1a,RIGHT)

        # Define alpha and beta
        form3 = MathTex(
            r"\underbrace{T_n}_{n\ \text{Worker Time}} = \underbrace{(1 - \alpha)\ \frac{T_1}{n}}_{\text{Parallel}}+ \underbrace{\alpha\ T_1}_{\text{Serial}} + \underbrace{\beta\ T_1\ (n-1)}_{\text{Consensus}}"
        )
        self.play(Write(form3))
        self.play(Wait(5))
        form3.scale(0.33)
        form3.next_to(form1,DOWN)

        # Define alpha and beta
        form4 = MathTex(
            r"\underbrace{T_n}_{n\ \text{Worker Time}} = \underbrace{\frac{T_1}{n}}_{\text{Time Per Processor}} * \underbrace{(1 + \alpha\ (n - 1) + \beta\ n(n-1))}_{\text{Time Expansion}}"
        )
        self.play(Write(form4))
        self.play(Wait(5))
        form4.scale(0.33)
        form4.next_to(form3,RIGHT)

        # Throughput
        form5 = MathTex(
            r"\underbrace{X_n}_{n\ \text{Worker Throughput}} = \frac{1}{T_n} = \frac{n\ \gamma}{1 + \alpha (n - 1) + \beta\ n(n - 1)}"
        )
        self.play(Write(form5))
        self.play(Wait(5))
        form5.scale(0.5)
        form5.next_to(form3,DOWN)

        # All the work units
        lastser = None
        for j in range(0,4):
            sqs = []
            lastsq = None
            for i in range(0,7):
                sq = Square(color=BLUE,fill_opacity=1)
                sq.set_fill(BLUE)
                sq.scale(0.1)
                self.play(Write(sq))
                if lastsq == None:
                    if j == 0:
                        sq.to_corner(DOWN + LEFT)
                    else:
                        sq.next_to(lastser,RIGHT)
                else:
                    sq.next_to(lastsq, RIGHT)
                lastsq = sq
                sqs.append(sq)
            i = 1
            while i < len(sqs)-1:
                prev = sqs[i-1]
                sqs[i].set_color(GREEN)
                sqs[i].next_to(prev,UP)
                self.play(Wait(0.1))
                i += 1
            lastser = sqs[len(sqs)-1]
            sqs[0].set_color(GREEN)
            lastser.set_color(GREEN)
            lastser.next_to(sqs[0],RIGHT)

        blist = BulletedList(
            "There are 6 workers to do work at the same time",
            "1/7 of the work is serial",
            "28/6 * (1 + (1/7)(6-1)) = 8",
            "One processor takes 42 units of time"
        )
        blist.scale(0.5)
        self.add(blist)
        self.play(Wait(10))
        self.play(FadeOut(blist))

        # Define alpha and beta
        formExample = MathTex(
            r"T_1 = 42, \underbrace{T_6}_{6\ \text{Worker Time}} = \underbrace{\frac{42}{6}}_{\text{Time Per Processor}} * \underbrace{(1 + \frac{1}{7}\ (6 - 1) + 0 * 6(6-1))}_{\text{Time Expansion}} = 8"
        )
        formExample.scale(0.5)
        self.play(Write(formExample))
        self.play(Wait(15))

        self.play(FadeOut(formExample))

        # Wait for end
        self.play(Wait(10))


class MovingScene(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.get_graph(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))

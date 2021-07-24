from manim import *

class MainScene(Scene):
    def construct(self):
        # Define gamma
        form = MathTex(
            r"\underbrace{0 < \gamma}_{\text{Worker speed}}"
        )
        self.play(Write(form))
        self.wait(15)
        form.scale(0.33)
        form.to_corner(UP + LEFT)

        form0 = MathTex(
            r"\underbrace{T_1 = \frac{1}{\gamma}}_{\text{1 Worker Time}}"
        )
        self.play(Write(form0))
        self.wait(15)
        form0.scale(0.33)
        form0.next_to(form,RIGHT)

        form1 = MathTex(
            r"\underbrace{0 \le \alpha \le 1}_{\text{Serial Fraction}}"
        )
        self.play(Write(form1))
        self.wait(15)
        form1.scale(0.33)
        form1.next_to(form0,RIGHT)

        form1a = MathTex(
            r"\underbrace{(1 - \alpha)}_{\text{Parallel Fraction}}"
        )
        self.play(Write(form1a))
        self.wait(15)
        form1a.scale(0.33)
        form1a.next_to(form1,RIGHT)

        form2 = MathTex(
            r"\underbrace{0 \le \beta}_{\text{Consensus Amount}}"
        )
        self.play(Write(form2))
        self.wait(15)
        form2.scale(0.33)
        form2.next_to(form1a,RIGHT)

        # Define alpha and beta
        form3 = MathTex(
            r"\underbrace{T_n}_{n\ \text{Worker Time}} = \underbrace{(1 - \alpha)\ \frac{T_1}{n}}_{\text{Parallel}}+ \underbrace{\alpha\ T_1}_{\text{Serial}} + \underbrace{\beta\ T_1\ (n-1)}_{\text{Consensus}}"
        )
        self.play(Write(form3))
        self.play(Wait(15))
        form3.scale(0.33)
        form3.next_to(form1,DOWN)

        # Define alpha and beta
        form4 = MathTex(
            r"\underbrace{T_n}_{n\ \text{Worker Time}} = \underbrace{\frac{T_1}{n}}_{\text{Time Per Processor}} * \underbrace{(1 + \alpha\ (n - 1) + \beta\ n(n-1))}_{\text{Time Expansion}}"
        )
        self.play(Write(form4))
        self.play(Wait(15))
        form4.scale(0.33)
        form4.next_to(form3,DOWN)

        # Throughput
        form4 = MathTex(
            r"\underbrace{X_n}_{n\ \text{Worker Throughput}} = \frac{1}{T_n} = \frac{n\ \gamma}{1 + \alpha (n - 1) + \beta\ n(n - 1)}"
        )
        self.play(Write(form4))
        self.play(Wait(15))
#        form4.next_to(form3,DOWN)

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

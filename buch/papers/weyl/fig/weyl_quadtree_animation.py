"""
Weyl's Quadtree Algorithm for Finding Polynomial Roots
=======================================================

A Manim Community animation explaining Hermann Weyl's 1924 algorithm for
locating the complex zeros of a polynomial via repeated subdivision of a
square in the complex plane, using Cauchy's argument principle to count
zeros inside each sub-square.

Render with:
    manim -pqh weyl_quadtree.py WeylQuadtree

Quality flags:
    -pql  low  (480p, fast)
    -pqm  medium (720p)
    -pqh  high (1080p)
    -pqk  4K
"""

from manim import *
import numpy as np


# ------------------------------------------------------------------
#  Example polynomial used throughout the animation
#  f(z) = z^4 - 1  has zeros at  1, i, -1, -i  (the 4th roots of unity)
#  We then visualise a generic polynomial whose 4 roots are scattered
#  so the quadtree refinement is more interesting:
#      roots = 1.2 + 0.6i,  -0.9 + 1.1i,  -1.0 - 0.8i,  0.7 - 1.0i
# ------------------------------------------------------------------
ROOTS = np.array([
    1.2 + 0.6j,
    -0.85 + 1.1j,
    -1.05 - 0.85j,
    0.7 - 1.05j,
])


def count_roots_in_square(center: complex, half_side: float) -> int:
    """Return the number of ROOTS that lie strictly inside the open square."""
    x0, y0 = center.real, center.imag
    n = 0
    for r in ROOTS:
        if (x0 - half_side < r.real < x0 + half_side and
                y0 - half_side < r.imag < y0 + half_side):
            n += 1
    return n


# ==================================================================
#  Main scene
# ==================================================================
class WeylQuadtree(Scene):
    def construct(self):
        self.intro_title()
        self.fundamental_theorem()
        self.argument_principle()
        self.algorithm_idea()
        self.quadtree_demo()
        self.outro()

    # ------------------------------------------------------------------
    #  1.  Title card
    # ------------------------------------------------------------------
    def intro_title(self):
        title = Text("Weyl's Quadtree Algorithm", font_size=56, weight=BOLD)
        subtitle = Text(
            "Locating the zeros of a polynomial in the complex plane",
            font_size=28,
            color=GREY_B,
        )
        attribution = Text("Hermann Weyl, 1924", font_size=24, color=GREY_C, slant=ITALIC)

        title.move_to(UP * 1.0)
        subtitle.next_to(title, DOWN, buff=0.4)
        attribution.next_to(subtitle, DOWN, buff=0.6)

        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(attribution), run_time=0.8)
        self.wait(1.5)
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(attribution),
            run_time=0.8,
        )

    # ------------------------------------------------------------------
    #  2.  Fundamental theorem of algebra reminder
    # ------------------------------------------------------------------
    def fundamental_theorem(self):
        header = Text("The Problem", font_size=42, weight=BOLD).to_edge(UP)

        problem = MathTex(
            r"f(z) \;=\; a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n",
            font_size=40,
        )
        problem.next_to(header, DOWN, buff=0.7)

        statement = Tex(
            r"Find every $z \in \mathbb{C}$ with $f(z) = 0$.",
            font_size=36,
        ).next_to(problem, DOWN, buff=0.6)

        fta = Tex(
            r"Fundamental theorem of algebra:\\"
            r"there are exactly $n$ such zeros (with multiplicity).",
            font_size=32,
            color=YELLOW_B,
        ).next_to(statement, DOWN, buff=0.7)

        self.play(Write(header), run_time=0.8)
        self.play(Write(problem), run_time=1.2)
        self.play(FadeIn(statement, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)
        self.play(Write(fta), run_time=1.2)
        self.wait(2.0)

        self.play(
            FadeOut(header),
            FadeOut(problem),
            FadeOut(statement),
            FadeOut(fta),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    #  3.  Cauchy's argument principle: how to *count* zeros in a region
    # ------------------------------------------------------------------
    def argument_principle(self):
        header = Text("Counting zeros in a region", font_size=40, weight=BOLD).to_edge(UP)
        self.play(Write(header), run_time=0.7)

        # --- the formula --------------------------------------------------
        formula = MathTex(
            r"N(D) \;=\; \frac{1}{2\pi i}\,\oint_{\partial D} \frac{f'(z)}{f(z)}\,dz",
            font_size=44,
        )
        formula.next_to(header, DOWN, buff=0.5)

        explanation = Tex(
            r"The contour integral of $f'/f$ around $\partial D$ \\"
            r"equals the number of zeros of $f$ inside $D$.",
            font_size=30,
            color=GREY_B,
        ).next_to(formula, DOWN, buff=0.5)

        self.play(Write(formula), run_time=1.6)
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=1.0)
        self.wait(1.5)

        # --- a small picture: square in C with some zeros inside ----------
        plane = ComplexPlane(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            background_line_style={"stroke_opacity": 0.3, "stroke_width": 1},
        ).scale(0.55).to_edge(DOWN, buff=0.5)

        # Draw the square boundary D
        square = Square(side_length=2.5, color=YELLOW, stroke_width=4)
        square.move_to(plane.get_center())

        # Mark some "zeros" — three inside, one outside
        zeros_visual = VGroup(
            Dot(plane.n2p(0.4 + 0.3j), color=RED, radius=0.08),
            Dot(plane.n2p(-0.6 + 0.5j), color=RED, radius=0.08),
            Dot(plane.n2p(0.2 - 0.7j), color=RED, radius=0.08),
            Dot(plane.n2p(2.0 + 1.8j), color=RED, radius=0.08),
        )

        n_label = MathTex(r"N(D) = 4", font_size=36, color=YELLOW)
        n_label.next_to(plane, RIGHT, buff=0.4)

        self.play(FadeOut(explanation), run_time=0.4)
        self.play(FadeIn(plane), Create(square), run_time=1.0)
        self.play(LaggedStartMap(FadeIn, zeros_visual, lag_ratio=0.2), run_time=1.0)

        # Animate a moving dot around the boundary to suggest the integral
        tracker = ValueTracker(0)
        moving_dot = always_redraw(
            lambda: Dot(
                square.point_from_proportion(tracker.get_value() % 1.0),
                color=GREEN,
                radius=0.10,
            )
        )
        self.add(moving_dot)
        self.play(tracker.animate.set_value(1), run_time=2.0, rate_func=linear)
        self.remove(moving_dot)

        self.play(Write(n_label), run_time=0.8)
        self.wait(2.0)

        # take-away line
        takeaway = Tex(
            r"Key fact: we can compute $N(D)$ from the coefficients alone.",
            font_size=28,
            color=YELLOW_B,
        ).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(takeaway, shift=UP * 0.2), run_time=1.0)
        self.wait(2.0)

        self.play(
            FadeOut(header),
            FadeOut(formula),
            FadeOut(plane),
            FadeOut(square),
            FadeOut(zeros_visual),
            FadeOut(n_label),
            FadeOut(takeaway),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    #  4.  The algorithmic idea (analogous to bisection in 2D)
    # ------------------------------------------------------------------
    def algorithm_idea(self):
        header = Text("The Idea: 2D bisection", font_size=40, weight=BOLD).to_edge(UP)

        steps = VGroup(
            Tex(r"1. Enclose all zeros in a big square $D_0 = [-r, r]^2$.", font_size=30),
            Tex(r"2. Split $D_0$ into 4 equal sub-squares.", font_size=30),
            Tex(r"3. Use $\;N(D) = \dfrac{1}{2\pi i}\oint_{\partial D} \dfrac{f'}{f}\,dz\;$"
                r"to count zeros in each.", font_size=30),
            Tex(r"4. Discard empty sub-squares.", font_size=30),
            Tex(r"5. Recurse on the rest until sub-squares are tiny.", font_size=30),
        )
        steps.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        steps.next_to(header, DOWN, buff=0.6)

        self.play(Write(header), run_time=0.7)
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.0)

        radius_remark = Tex(
            r"A safe choice: $r = \sum_{k=0}^{n}|a_k|/|a_n|$ "
            r"contains every zero.",
            font_size=26,
            color=GREY_B,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(radius_remark), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(header),
            FadeOut(steps),
            FadeOut(radius_remark),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    #  5.  Live demo: subdivide a square and locate the four roots
    # ------------------------------------------------------------------
    def quadtree_demo(self):
        header = Text("Demo: locating 4 roots", font_size=40, weight=BOLD).to_edge(UP)
        self.play(Write(header), run_time=0.7)

        # ------------------------------------------------------------------
        # Set up the complex plane
        # ------------------------------------------------------------------
        plane = ComplexPlane(
            x_range=[-2.2, 2.2, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=6.5,
            y_length=6.5,
            background_line_style={"stroke_opacity": 0.25, "stroke_width": 1},
        )
        plane.shift(LEFT * 2.2 + DOWN * 0.3)

        plane_label = MathTex(r"\mathbb{C}", font_size=32, color=GREY_B)
        plane_label.next_to(plane, UP, buff=0.1).align_to(plane, RIGHT)

        self.play(FadeIn(plane), FadeIn(plane_label), run_time=0.8)

        # ------------------------------------------------------------------
        # Show the (hidden) true roots as faint marks the algorithm is
        # trying to localise.  We reveal them lightly so the viewer can
        # see why the quadtree zooms in where it does.
        # ------------------------------------------------------------------
        true_root_dots = VGroup(*[
            Dot(plane.n2p(r), color=RED, radius=0.09).set_z_index(5)
            for r in ROOTS
        ])
        roots_label = Tex(r"true zeros of $f$", font_size=24, color=RED)
        roots_label.to_corner(UR, buff=0.6).shift(LEFT * 0.2)

        self.play(LaggedStartMap(FadeIn, true_root_dots, lag_ratio=0.15), run_time=1.0)
        self.play(Write(roots_label), run_time=0.6)
        self.wait(0.6)

        # ------------------------------------------------------------------
        # Side panel that will display the count for each square
        # ------------------------------------------------------------------
        info_title = Text("Zeros found in:", font_size=24, weight=BOLD)
        info_title.to_edge(RIGHT, buff=0.5).shift(UP * 1.5)
        self.play(FadeIn(info_title), run_time=0.5)

        # ------------------------------------------------------------------
        # LEVEL 0 — the bounding square
        # ------------------------------------------------------------------
        L0_half = 2.0  # in complex-plane units
        L0_center = 0 + 0j
        big_square = self._make_square(plane, L0_center, L0_half, color=YELLOW)

        big_label = MathTex(r"D_0:\; N = 4", font_size=28, color=YELLOW)
        big_label.next_to(info_title, DOWN, buff=0.4).align_to(info_title, LEFT)

        self.play(Create(big_square), run_time=1.0)
        self._flash_boundary(big_square)
        self.play(Write(big_label), run_time=0.7)
        self.wait(0.6)

        # ------------------------------------------------------------------
        # LEVEL 1 — split into 4 quadrants
        # ------------------------------------------------------------------
        L1_half = L0_half / 2
        L1_centers = [
            -L1_half - L1_half * 1j,   # SW
             L1_half - L1_half * 1j,   # SE
            -L1_half + L1_half * 1j,   # NW
             L1_half + L1_half * 1j,   # NE
        ]
        L1_squares = [
            self._make_square(plane, c, L1_half, color=BLUE_C, stroke_width=3)
            for c in L1_centers
        ]
        L1_counts = [count_roots_in_square(c, L1_half) for c in L1_centers]

        # Animate the split
        self.play(
            big_square.animate.set_stroke(opacity=0.35),
            *[Create(s) for s in L1_squares],
            run_time=1.2,
        )

        # Place a count label at the centre of each square and color empty
        # ones red, non-empty ones green.
        L1_count_labels = VGroup()
        for sq, c, k in zip(L1_squares, L1_centers, L1_counts):
            label = MathTex(f"N={k}", font_size=22)
            label.move_to(plane.n2p(c))
            label.set_color(GREEN_B if k > 0 else GREY_C)
            L1_count_labels.add(label)
        self.play(LaggedStartMap(FadeIn, L1_count_labels, lag_ratio=0.15), run_time=1.0)
        self.wait(1.0)

        # Discard empty squares — fade them out
        keep_L1 = [
            (sq, c, k) for sq, c, k in zip(L1_squares, L1_centers, L1_counts) if k > 0
        ]
        drop_L1 = [
            sq for sq, c, k in zip(L1_squares, L1_centers, L1_counts) if k == 0
        ]
        if drop_L1:
            self.play(
                *[sq.animate.set_stroke(opacity=0.1) for sq in drop_L1],
                FadeOut(VGroup(*[
                    lab for lab, k in zip(L1_count_labels, L1_counts) if k == 0
                ])),
                run_time=0.7,
            )

        # ------------------------------------------------------------------
        # LEVEL 2 — split each surviving square into 4
        # ------------------------------------------------------------------
        self.play(FadeOut(VGroup(*[
            lab for lab, k in zip(L1_count_labels, L1_counts) if k > 0
        ])), run_time=0.4)

        L2_half = L1_half / 2
        L2_squares_all = []
        L2_centers_all = []
        L2_counts_all = []

        for sq_parent, c_parent, k_parent in keep_L1:
            children_centers = [
                c_parent + (-L2_half - L2_half * 1j),
                c_parent + ( L2_half - L2_half * 1j),
                c_parent + (-L2_half + L2_half * 1j),
                c_parent + ( L2_half + L2_half * 1j),
            ]
            children_squares = [
                self._make_square(plane, c, L2_half, color=TEAL, stroke_width=2.5)
                for c in children_centers
            ]
            children_counts = [count_roots_in_square(c, L2_half) for c in children_centers]
            L2_squares_all.extend(children_squares)
            L2_centers_all.extend(children_centers)
            L2_counts_all.extend(children_counts)

        self.play(
            *[Create(s) for s in L2_squares_all],
            run_time=1.4,
        )

        # Show counts and discard empty
        L2_kept = []
        L2_drop_squares = []
        L2_count_marks = VGroup()
        for sq, c, k in zip(L2_squares_all, L2_centers_all, L2_counts_all):
            if k > 0:
                m = MathTex(f"{k}", font_size=18, color=GREEN_B)
                m.move_to(plane.n2p(c))
                L2_count_marks.add(m)
                L2_kept.append((sq, c, k))
            else:
                L2_drop_squares.append(sq)
        self.play(LaggedStartMap(FadeIn, L2_count_marks, lag_ratio=0.1), run_time=0.8)
        self.wait(0.6)
        if L2_drop_squares:
            self.play(
                *[sq.animate.set_stroke(opacity=0.08) for sq in L2_drop_squares],
                run_time=0.6,
            )

        info_L2 = MathTex(
            rf"\text{{Level 2: }} {len(L2_kept)} \text{{ live cells}}",
            font_size=24, color=TEAL,
        )
        info_L2.next_to(big_label, DOWN, buff=0.3).align_to(info_title, LEFT)
        self.play(Write(info_L2), run_time=0.6)
        self.wait(0.4)

        # ------------------------------------------------------------------
        # LEVEL 3 — final refinement
        # ------------------------------------------------------------------
        self.play(FadeOut(L2_count_marks), run_time=0.3)

        L3_half = L2_half / 2
        L3_squares_all = []
        L3_centers_all = []
        L3_counts_all = []
        for sq_parent, c_parent, k_parent in L2_kept:
            children_centers = [
                c_parent + (-L3_half - L3_half * 1j),
                c_parent + ( L3_half - L3_half * 1j),
                c_parent + (-L3_half + L3_half * 1j),
                c_parent + ( L3_half + L3_half * 1j),
            ]
            children_squares = [
                self._make_square(plane, c, L3_half, color=GREEN, stroke_width=2)
                for c in children_centers
            ]
            children_counts = [count_roots_in_square(c, L3_half) for c in children_centers]
            L3_squares_all.extend(children_squares)
            L3_centers_all.extend(children_centers)
            L3_counts_all.extend(children_counts)

        self.play(
            *[Create(s) for s in L3_squares_all],
            run_time=1.6,
        )

        L3_kept_squares = []
        L3_drop_squares = []
        for sq, c, k in zip(L3_squares_all, L3_centers_all, L3_counts_all):
            if k > 0:
                L3_kept_squares.append(sq)
            else:
                L3_drop_squares.append(sq)
        if L3_drop_squares:
            self.play(
                *[sq.animate.set_stroke(opacity=0.08) for sq in L3_drop_squares],
                run_time=0.6,
            )

        # Highlight the surviving cells — each contains exactly one zero
        self.play(
            *[sq.animate.set_stroke(color=GOLD, width=3.5) for sq in L3_kept_squares],
            run_time=0.8,
        )

        info_L3 = MathTex(
            rf"\text{{Level 3: }} {len(L3_kept_squares)} \text{{ tiny boxes,"
            r" each isolating one zero}}",
            font_size=22, color=GOLD,
        )
        info_L3.next_to(info_L2, DOWN, buff=0.3).align_to(info_title, LEFT)
        self.play(Write(info_L3), run_time=0.8)
        self.wait(2.0)

        # ------------------------------------------------------------------
        # Cleanup before outro
        # ------------------------------------------------------------------
        all_demo_objects = VGroup(
            plane, plane_label, big_square,
            *L1_squares, *L2_squares_all, *L3_squares_all,
            *true_root_dots, roots_label,
            info_title, big_label, info_L2, info_L3,
            header,
        )
        self.play(FadeOut(all_demo_objects), run_time=0.8)

    # ------------------------------------------------------------------
    #  6.  Outro: complexity and outlook
    # ------------------------------------------------------------------
    def outro(self):
        title = Text("Why it matters", font_size=42, weight=BOLD).to_edge(UP)
        self.play(Write(title), run_time=0.7)

        bullets = VGroup(
            Tex(r"$\bullet$ First general algorithm for complex roots (1924).", font_size=30),
            Tex(r"$\bullet$ Works in $\mathcal{O}(n^2 \, h \, \log n)$ steps for $h$ digits.", font_size=30),
            Tex(r"$\bullet$ Locate, then polish with Newton's method nearby.", font_size=30),
            Tex(r"$\bullet$ Direct ancestor of modern fan-out root-finders.", font_size=30),
        )
        bullets.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        bullets.next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.5)

        closing = Text("Hermann Weyl, 1924", font_size=26, color=GREY_B, slant=ITALIC)
        closing.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(closing), run_time=0.8)
        self.wait(2.5)

        self.play(FadeOut(VGroup(title, bullets, closing)), run_time=0.8)

    # ==================================================================
    #  Helpers
    # ==================================================================
    def _make_square(self, plane, center: complex, half_side: float,
                     color=YELLOW, stroke_width=4):
        """Build a Square positioned on the complex plane."""
        # Convert (center ± half_side, center ± half_side) corners into
        # screen coords via plane.n2p so the square has the right size.
        bl = plane.n2p(center - half_side - half_side * 1j)
        br = plane.n2p(center + half_side - half_side * 1j)
        tr = plane.n2p(center + half_side + half_side * 1j)
        tl = plane.n2p(center - half_side + half_side * 1j)
        sq = Polygon(bl, br, tr, tl,
                     color=color, stroke_width=stroke_width, fill_opacity=0)
        return sq

    def _flash_boundary(self, square):
        """Animate a dot travelling around the square's boundary."""
        tracker = ValueTracker(0)
        dot = always_redraw(
            lambda: Dot(
                square.point_from_proportion(tracker.get_value() % 1.0),
                color=GREEN,
                radius=0.08,
            )
        )
        self.add(dot)
        self.play(tracker.animate.set_value(1), run_time=1.6, rate_func=linear)
        self.remove(dot)
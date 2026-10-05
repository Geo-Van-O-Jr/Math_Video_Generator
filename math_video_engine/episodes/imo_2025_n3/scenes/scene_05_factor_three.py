from engine.base_scene import MathScene


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("A missing factor of 3 cannot return", 5)
        self.equation(r"2\mid a_n,\qquad3\nmid a_n", r"p_1=2,\quad p_2\ge4,\quad p_3\ge5",
                      caption="Suppose an even term has no factor 3.", hold=7)
        self.equation(r"\frac{a_{n+1}}{a_n}\le\frac12+\frac14+\frac15=\frac{19}{20}<1",
                      caption="It shrinks. Could it escape by acquiring a factor 3?", hold=7)
        self.equation(r"3\mid a_{n+1}\quad\text{(assume for contradiction)}",
                      r"a_{n+1}=a_n\left(\frac12+\frac1{p_2}+\frac1{p_3}\right)",
                      caption="All denominators and the current term are invertible modulo 3.", hold=8)
        self.equation(r"2^{-1}\equiv2,\quad1^{-1}\equiv1\pmod3",
                      r"2+p_2+p_3\equiv0\pmod3",
                      caption="Each nonzero residue modulo 3 is its own inverse.", hold=9)
        self.equation(r"p_2,p_3\in\{1,2\}\pmod3", r"p_2\equiv p_3\equiv2\pmod3",
                      caption="Both residues must be 2: this is the only sum that vanishes modulo 3.", hold=7)
        self.equation(r"4\mid a_n\ \Rightarrow\ p_2=4\equiv1\pmod3",
                      r"\therefore\quad4\nmid a_n,\qquad v_2(a_n)=1",
                      caption="A factor 4 would contradict the required residue of the second divisor.", hold=9)
        self.equation(r"p_2\text{ is odd}",
                      caption="An even divisor after 2 would have a smaller odd partner.\nThat partner would come first, so the second divisor must be odd.", hold=9)
        self.equation(r"p_3\text{ even}\ \Rightarrow\ p_3=2d,\quad d\text{ odd},\quad1<d<p_3",
                      r"d=p_2\quad\Rightarrow\quad p_3=2p_2",
                      caption="There is room for only one divisor between 2 and the third divisor.", hold=10)
        self.equation(r"p_2\equiv2\pmod3\ \Rightarrow\ 2p_2\equiv1\pmod3",
                      r"p_3\equiv2\pmod3\quad\text{is a contradiction}",
                      caption="The third divisor must therefore be odd as well.", hold=9)
        self.equation(r"\frac{a_n}{2}\text{ odd},\qquad\frac{a_n}{p_2},\frac{a_n}{p_3}\text{ even}",
                      r"a_{n+1}=\text{odd}+\text{even}+\text{even}=\text{odd}",
                      caption="But we already proved that an odd term cannot survive.", hold=9)
        self.equation(r"3\nmid a_n\quad\Rightarrow\quad3\nmid a_{n+1}",
                      r"a_n>a_{n+1}>a_{n+2}>\cdots",
                      caption="In a valid sequence, a missing factor 3 stays missing.\nStrict decrease would continue forever: impossible.", hold=9)
        self.result(r"6\mid a_n\qquad\text{for every }n",
                    caption="Every surviving term is divisible by both 2 and 3.", hold=8)
        self.finish()

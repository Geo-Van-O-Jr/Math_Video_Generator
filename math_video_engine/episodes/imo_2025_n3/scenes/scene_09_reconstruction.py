from engine.base_scene import MathScene


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("Reconstruct the starting value", 9)
        self.equation(r"6\mid A,\qquad4\nmid A,\qquad5\nmid A",
                      r"A=6M,\quad M\text{ odd},\quad5\nmid M",
                      caption="Work backwards from a fixed point: its first three divisors are 2, 3, 6.", hold=9)
        self.equation(r"A=a_1\left(\frac{13}{12}\right)^c", r"a_1=A\left(\frac{12}{13}\right)^c",
                      caption="Let c be the number of growth steps before the sequence freezes.", hold=8)
        self.equation(r"13^c\mid A\quad\Rightarrow\quad13^c\mid M",
                      r"M=13^c m,\qquad A=6\cdot13^c m",
                      caption="Since 12 and 13 are coprime, integrality requires c factors of 13 in A.", hold=9)
        self.equation(r"a_1=6\cdot13^c m\left(\frac{12}{13}\right)^c=6\cdot12^c m",
                      r"m\text{ odd},\quad5\nmid m",
                      caption="Removing powers of 13 changes neither parity nor divisibility by 5.", hold=9)
        self.result(r"a_1=6\cdot12^c m", r"c\in\mathbb Z_{\ge0},\quad m\in\mathbb Z_{>0},\quad\gcd(m,10)=1",
                    caption="These conditions are necessary. Now check that they are sufficient.", hold=8)
        self.equation(r"a_{j+1}=6\cdot12^{c-j}13^j m\qquad(0\le j\le c)",
                      r"j<c\ \Rightarrow\ 12\mid a_{j+1}\ \Rightarrow\ p_3=4",
                      caption="For each of the first c steps, the three smallest divisors are 2, 3, 4.", hold=10)
        self.equation(r"a_{c+1}=6\cdot13^c m", r"4\nmid a_{c+1},\quad5\nmid a_{c+1}\quad\Rightarrow\quad p_3=6",
                      caption="Then the sequence freezes. Every term is a multiple of 6,\nso it has at least the four divisors 1, 2, 3, 6.", hold=10)
        self.result(r"a_1=2^{2c+1}3^{c+1}m", r"c\ge0,\quad m>0,\quad\gcd(m,10)=1",
                    caption="Thus every value in the family works, and no other value can work.", hold=8)
        self.finish()

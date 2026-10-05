"""Numerical invariants supplement the exact proof in the episode sources."""
from decimal import Decimal, getcontext
import math
import random


def main():
    getcontext().prec=60
    a=Decimal(39999).sqrt()
    eps=1/(Decimal(200)+a)
    assert eps>Decimal(1)/400
    assert abs(eps*eps+1-400*eps)<Decimal('1e-55')
    for d in map(Decimal,['2','5','50','99.999999','100']):
        y2=1+(d-eps)**2
        assert y2-d*d>Decimal('.5')
        assert abs(y2-(d*d+eps*(400-2*d)))<Decimal('1e-54')
    aa=float(a)
    previous=(0.,0.)
    for k in range(1,201):
        r=(k*aa/200,k/200)
        assert math.isclose(math.dist(r,previous),1,abs_tol=1e-12)
        assert k/200<=1
        assert math.isclose(math.dist(r,(r[0],0)),k/200)
        previous=r
    rng=random.Random(201703)
    samples=0
    for d in (2,20,50,99.999,100):
        best=1+(d-float(eps))**2
        for _ in range(5000):
            radius=200*math.sqrt(rng.random()); angle=rng.random()*math.tau
            u=-d+radius*math.cos(angle); v=radius*math.sin(angle)
            worst=max((aa-u)**2+(1-v)**2,(aa-u)**2+(-1-v)**2)
            assert worst+1e-10>=best
            samples+=1
    # Exact accounting; strict block increments turn equality into >10000.
    blocks=19992
    assert 4+Decimal(blocks)/2==10000
    assert blocks<20000
    assert 1+200*blocks==3998401<4000000<10**9
    # Legal first-round construction, for arbitrary strategy-determined direction.
    for angle in (0,.1,1,2,5):
        h=(math.cos(angle),math.sin(angle)); r=(-h[0],-h[1])
        assert math.isclose(math.dist(h,r),2)
        assert math.isclose(math.dist(r,(0,0)),1)
    print(f"PASS: exact high-precision identities, 200 unit hops and common pings, {samples} minimax endpoints, equality case and strict round count.")


if __name__=='__main__':
    main()

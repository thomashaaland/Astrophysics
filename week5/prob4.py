from scitools.all import *

class Rel:
    def __init__(self):
        #Variables
        self.me = 9.109383*10**(-31)
        self.mp = 1.672622*10**(-27)
        self.mn = 1.674927*10**(-27)
        self.vrel = 0.99
        self.gamma_rel = 1./sqrt(1-self.vrel**2)

        #solutions:
        self.variables()
        self.momenergy()
        
    def variables(self):
        me = self.me
        mp = self.mp
        mn = self.mn
        self.gamma_e = (mn**2-mp**2+me**2)/(2*mn*me)
        gamma_e = self.gamma_e
        self.gamma_p = (mn-me*gamma_e)/mp
        gamma_p = self.gamma_p
        self.ve = sqrt(1-1/gamma_e**2)
        ve = self.ve
        self.vp = -(me*gamma_e*ve)/(mp*gamma_p)
        vp = self.vp
        print ve, vp

    def momenergy(self):
        me = self.me
        mp = self.mp
        mn = self.mn
        gamma_e = self.gamma_e
        gamma_p = self.gamma_p
        ve = self.ve
        vp = self.vp
        vrel = self.vrel
        gamma_rel = self.gamma_rel
        self.Ee = me*gamma_e*gamma_rel*(1+vrel*ve)
        self.pe = me*gamma_e*gamma_rel*(vrel+ve)
        self.Ep = mp*gamma_p*gamma_rel*(1+vrel*vp)
        self.pp = mp*gamma_p*gamma_rel*(vrel+vp)

        v_abse = sqrt(1-me**2/self.Ee**2)

        v_absp = sqrt(1-mp**2/self.Ep**2)
        
        print self.Ee, self.pe, self.Ep, self.pp
        print v_abse, v_absp

Rel()

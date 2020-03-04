from scitools.all import *

class Galaxy:
    def __init__(self, filename):
        self.filename = filename
        self.c = 3*10**8 #m/s, speed of light
        self.G = 6.67*10**(-11) #Newtons gravitational constant in Nm^2/kg^2
        self.x_arcmin = [] # in arcseconds
        self.y_arcmin = [] #-||-
        self.r_earth = [] # in Mega parsecs
        self.SpinnH = [] # 21-cm line observed

        self.read_file()
        self.veloceties()
        self.positions()
#        self.plot()
        self.virial()

    def read_file(self): # Leser inn fila og formaterer i lister
        infile = open(self.filename, 'r')
        
        for line in infile:
            row = line.split()
            self.x_arcmin.append(float(row[0].strip())) # Arcmin langs x-aksen
            self.y_arcmin.append(float(row[1].strip())) # Arcmin langs y-aksen
            self.r_earth.append(float(row[2].strip())) # avstanden fra jorda til den gitte galaksen i Mpc
            self.SpinnH.append(float(row[3].strip())) # forskyvningnen i 21.2 cm bolgelengde
        
        r_arc = []
        for i in range(0, len(self.x_arcmin)):
            a = array([self.x_arcmin[i], self.y_arcmin[i]])
            r_arc.append(a)
        self.r_arc = array(r_arc) #Arcmin x, y array
        self.r_earth=array(self.r_earth)
        self.SpinnH = array(self.SpinnH)
        
    def veloceties(self):
        self.v_gal=self.c*(self.SpinnH-0.212)/0.212 # in m/s
        self.v_cluster = 1/float(len(self.v_gal))*sum(self.v_gal) #in m/s
        self.v_rel = self.v_gal-self.v_cluster # in m/s
        print 'Hastigheten til galaksehopens massesenter er ', self.v_cluster, ' m/s'

    def positions(self):
        self.r_cm = range(0, (len(self.x_arcmin)))
        self.r_cm_z = self.r_earth-1/float((len(self.r_earth)))*sum(self.r_earth) #Liste m/ avstand til cm galaksehop langs z
        r_x = 0
        r_y = 0
        for i in range(0, len(self.x_arcmin)):
            self.r_cm[i] = self.r_earth[i]*(self.r_arc[i,:]/(60.*360))*2*pi
            r_x = r_x + self.r_cm[i][0]
            r_y = r_y + self.r_cm[i][1]
        for i in range(0,100):
            self.r_cm[i][0] = self.r_cm[i][0] - r_x/100.
            self.r_cm[i][1] = self.r_cm[i][1] - r_y/100.
            self.r_cm[i] = array(list(self.r_cm[i])+[self.r_cm_z[i]])
        self.r_cm = array(self.r_cm) # 3D position in Mpc, i forhold til massesenteret
        
    def plot(self):
        hold('on')
        plot(self.x_arcmin, self.y_arcmin,
                 'ko',
                 title='Galakser i galaksehopen som sett fra jorda',
                 xlabel='arcminutes',
                 ylabel='arcminutes')
        savefig('plot.png')
    def virial(self):
        self.m = 0
        r_tot = 0
        n = len(self.r_cm)
        v_tot_sq = sum(self.v_rel**2)
        for i in range(0,n):
            for j in range(i+1,n):
                r_tot = r_tot + 1/(3.086*10**22*sqrt(dot(self.r_cm[i]-self.r_cm[j], self.r_cm[i]-self.r_cm[j]))) #in meters
        self.m = v_tot_sq/(self.G*r_tot) # Massen til hver enkelt galakse
        self.M = 100*self.m # Massen til galaksehopen
        print 'Massen til en galakse er', self.m, 'kg'
        print 'Massen til galaksehopen er', self.M, 'kg'

Galaxy = Galaxy('galaxies.txt')

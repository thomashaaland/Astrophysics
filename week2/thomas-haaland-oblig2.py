from scitools.all import *

#Star class
class star:
    def __init__(self, filename):
        # Variables/lists
        self.filename = filename
        self.t = []
        self.flux = []
        self.wl = [] 
        self.c = 299792458. # Speed of light in vacuum
        self.wl0 = 656.3 * 10**(-9) # The Spectral line we are looking for: alphaH
        self.planet = 'no'

        #Calculations and functions
        self.read_file()
        self.rad_velocity()
        self.pec_velocity()
        self.light_curve()
        self.vel_curve()
        self.model()
        self.planet_mass()
        self.output()

    #function that imports text
    def read_file(self):
        infile = open(self.filename, 'r')

        for line in infile:
            row = line.split()
            self.t.append(float(row[0].strip()))
            self.wl.append(float(row[1].strip()))
            self.flux.append(float(row[2].strip()))
            
        self.t=array(self.t); self.flux=array(self.flux); self.wl=array(self.wl)
    
    #function for calculating radial velocity
    def rad_velocity(self):
        wl=self.wl*10**(-9)
        c = self.c
        wl0= self.wl0
        self.rad_vel = (wl-wl0)/wl*c #radial velocity

    #function for calculating peculiar velocity
    def pec_velocity(self):
        self.pec_vel = sum(self.rad_vel)/(len(self.rad_vel))

    #Plotting the the light-curve
    def light_curve(self):
        figure(01)
        plot(self.t, self.flux)
        title('light-curve')

    #Plotting the velocity curve
    def vel_curve(self):
        #Relative velocity difference between radial and peculiar velocity
        self.rel_vel = self.rad_vel - self.pec_vel

        figure(02)
        plot(self.t, self.rel_vel)
        title('relative velocity')

    #For smoothing the curves... finding the best constant for making a smooth
    #cosine curve from the raw data
    def model(self):
        self.planet = (raw_input('Is there a planet eclipsing  %s? (yes/no): ' % (self.filename)))

        if self.planet == 'yes':
            #Read in min and max of t0, vr and P from cml, using eval to allow scientific notation and computations on cml.
            t0_min = eval(raw_input('type t0 min value: '))
            t0_max = eval(raw_input('type t0 max value: '))
            vr_min = eval(raw_input('type vr min value: '))
            vr_max = eval(raw_input('type vr max value: '))
            P_min  = eval(raw_input('type Period min value: '))
            P_max  = eval(raw_input('type Period max value: '))
            
            t0 = linspace(t0_min, t0_max, 40)
            vr = linspace(vr_min, vr_max, 40)
            P = linspace(P_min, P_max, 40)
            
            best_t0 = t0[0]
            best_vr = vr[0]
            best_P  = P[0]
            self.best_delta = 10**12 # some random large starting value, making sure it is larger than the smallest delta

            #Going through every element in t0, vr and P to pick the best
            for i in range(len(t0)):
                for j in range(len(vr)):
                    for k in range(len(P)):
                        #rel_vel_model is the model used to aproximate the data-curve
                        rel_vel_model = vr[j]*cos((2*pi/P[k])*(self.t-t0[i]))

                        #Using method of least square to see how the model fits the data 

                        delta = sum((self.rel_vel - rel_vel_model)**2)

                        #checking to see if variables are better:
                        if delta < self.best_delta:
                            self.best_t0 = t0[i]
                            self.best_vr = vr[j]
                            self.best_P  = P[k]
                            self.best_delta = delta

            #Plotting final model
            best_rel_vel_model = self.best_vr*cos((2*pi/self.best_P)*(self.t-self.best_t0))
            figure(n)
            plot(self.t, best_rel_vel_model,legend='model')
            hold('on')
            plot(self.t, self.rel_vel, legend='data')
            title('%s' % (self.filename))
            hold('off')

    #Finding the mass of the orbiting planet
    def planet_mass(self):
        if self.planet == 'yes':
            m_star=eval(raw_input('type the mass of star described in %s in solar masses: ' % (self.filename)))
            self.planet_mass = (((m_star*(1.988435*10**30))**2*self.best_P)/(2*pi*(6.67*10**(-11))))**(1/3.)*self.best_vr

    def output(self):
        #Writes results to file
        if self.planet == 'yes':
            outfile=open('tmp_week2/stars.txt','a')
            outfile.write('%s\n' % (self.filename))
            outfile.write('%s               %s                   %s            %s\n' % ('t0', 'vr', 'P', 'M'))
            outfile.write('%s    %s    %s   %s   %s\n' % (str(self.best_t0), str(self.best_vr), str(self.best_P), str(self.planet_mass)))
            outfile.write('\n')
            outfile.close()
                
                        

#______________________________
#MAIN

# Snippet to clean outfile everytime program runs.
outfile=open('tmp_week2/stars.txt','w')
outfile.write('')
outfile.close()
n = 0
star0 = star('star0.txt'); n = 1
star1 = star('star1.txt'); n = 2
star2 = star('star2.txt'); n = 3
star3 = star('star3.txt'); n = 4
star4 = star('star4.txt'); n = 5
star5 = star('star5.txt'); n = 6
star6 = star('star6.txt'); n = 7
star7 = star('star7.txt'); n = 8
star8 = star('star8.txt'); n = 9
star9 = star('star9.txt')


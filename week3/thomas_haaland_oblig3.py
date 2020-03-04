from scitools.all import *

class Spectrum:
    def __init__(self, filename):
        #variables
        self.filename = filename
        self.t = []
        self.wl = []
        self.flux = []
        self.F_min = []
        self.sigma = []
        self.lambda_center = []
        
        #functions
        self.readfile()
        self.plot()
        self.model()

        #Reads file
    def readfile(self):
        infile = open(self.filename, 'r')

        for line in infile:
            row = line.split()
            self.wl.append(float(row[0].strip()))
            self.flux.append(float(row[1].strip()))
        
        self.wl=array(self.wl)
        self.flux=array(self.flux)
        infile.close()
    
        #For plotting initial raw data
    def plot(self):
        figure(01)
        plot(self.wl, self.flux)
        xlabel('wavelength [nm]')
        ylabel('flux [J/(m^2 s)]')
        title('Wavelength vs. Flux')
        
        #Function for tayloring the model to the data
    def model(self):
        flux_min = eval(raw_input('Type flux_min min value: '))
        flux_max = eval(raw_input('Type flux_min max value: '))
        wl_min = eval(raw_input('Type minimum wavelength center: '))
        wl_max = eval(raw_input('Type maximum wavelength center: '))
        sigma_min = eval(raw_input('Type Full Width At Half Maximum minimum: '))
        sigma_max = eval(raw_input('Type Full Width At Half Maximum maximum: '))

        fmin = linspace(flux_min, flux_max, 20)
        lambdacenter = linspace(wl_min, wl_max, 20)
        sigma = (linspace(sigma_min, sigma_max, 20))/sqrt(8*log(2))
        
        self.best_fmin = fmin[0]
        self.best_lambdacenter = lambdacenter[0]
        self.best_sigma = sigma[0]
        
        best_Delta = Infinity

        for i in range(len(fmin)):
            for j in range(len(lambdacenter)):
                for k in range(len(sigma)):
                    model = 1 + (fmin[i] - 1)*exp(-((self.wl-lambdacenter[j])**2)/(2*sigma[k]**2))
                    
                    Delta = sum((self.flux - model)**2)

                    if Delta < best_Delta:
                        self.best_fmin = fmin[i]
                        self.best_lambdacenter = lambdacenter[j]
                        self.best_sigma = sigma[k]
                        best_Delta = Delta

        delta = array([self.best_fmin, self.best_lambdacenter, self.best_sigma])

        best_model = 1 + (self.best_fmin - 1)*exp(-(((self.wl - self.best_lambdacenter)**2)/(2*self.best_sigma**2)))
        
        figure(n)
        plot(self.wl, best_model, legend='model')
        hold('on')
        plot(self.wl, self.flux, legend='raw data')
        xlabel('wavelength [nm]')
        ylabel('flux [J/(m^2 s)]')
        title('Wavelength vs. flux')
        hold('off')
        hardcopy('result.ps')
        print delta

        
    
#____
#MAIN
time = array([0, 67, 133, 200, 267, 333, 400, 467, 533, 600]); n = 0
time0 = Spectrum('files/spectrum_day0.txt'); n = 1
#time67 = Spectrum('files/spectrum_day67.txt'); n = 2
#time133 = Spectrum('files/spectrum_day133.txt'); n = 3
#time200 = Spectrum('files/spectrum_day200.txt'); n = 4
#time267 = Spectrum('files/spectrum_day267.txt'); n = 5
#time333 = Spectrum('files/spectrum_day333.txt'); n = 6
#time400 = Spectrum('files/spectrum_day400.txt'); n = 7
#time467 = Spectrum('files/spectrum_day467.txt'); n = 8
#time533 = Spectrum('files/spectrum_day533.txt'); n = 9
#time600 = Spectrum('files/spectrum_day600.txt'); n = 10

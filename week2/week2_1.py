def load(filename):
    infile=open(filename, 'r')

    t=[] # measured time, starting at t=0
    wl=[] #measured wavelength subject to redshifts
    """influx = measured flux / maximum flux for the given star"""
    influx=[]

    for line in infile:
        row = line.split() # splits line with regards to whitespaces

        t.append(float(row[0].strip().strip()))
        wl.append(float(row[1].strip().strip()))
        influx.append(float(row[2].strip().strip()))

    infile.close()
    return t, wl, influx

t=load('star0.txt')[0]


print t

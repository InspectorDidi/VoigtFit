# -*- coding: UTF-8 -*-

__author__ = 'Jens-Kristian Krogager'

import numpy as np
from pkg_resources import resource_filename

datafile = resource_filename('VoigtFit', '../static/Asplund2009.dat')

dt = [('element', 'S2'), ('N', 'f4'), ('N_err', 'f4'), ('N_m', 'f4'), ('N_m_err', 'f4')]
data = np.loadtxt(datafile, dtype=dt)

photosphere = dict()
meteorite = dict()

for element, N_phot, N_phot_err, N_met, N_met_err in data:
    photosphere[element] = [N_phot, N_phot_err]
    meteorite[element] = [N_met, N_met_err]

print "\n Loaded Solar abundances from Asplund et al. 2009  (photospheric)"
# print bold+"    The Chemical Composition of the Sun"+reset
# print " Annual Review of Astronomy and Astrophysics"
# print "             Vol. 47: 481-522"
# print ""
# print " Data available:  photosphere,  meteorite"
print ""

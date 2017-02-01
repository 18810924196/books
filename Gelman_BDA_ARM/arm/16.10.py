import rpy2.robjects as R
import rpy2.rinterface as rinterface
from rpy2.robjects.packages import importr
import rpy2.robjects.numpy2ri
from rpy2.robjects.vectors import FloatVector, StrVector
import numpy as np
r2jags = importr('R2jags')

schools = np.loadtxt("schools-tests.dat",  skiprows=1, usecols = (0,1,2,3,4))

n=len(schools)
J = np.unique(np.max(schools[:,0]))[0]
y = schools[:,2]
school = schools[:,0]
x = schools[:,3]
T = schools[:,4]

print n
print J
print y
print school

R.r.assign('n',n)
R.r.assign('J',J)
R.r.assign('y',y)
R.r.assign('school',school)
R.r.assign('x',x)
R.r.assign('T',T)

radon_data = StrVector(("n", "J", "y", "school", "x", "T"))
radon_params = StrVector(("a", "b", "sigma.y", "sigma.a"))

radon_inits = R.r('''function (){
  list (a=rnorm(J), b=rnorm(1), g.0=rnorm(1), g.1=rnorm(1),
        sigma.y=runif(1), sigma.a=runif(1))
  }''')

jags_schools = r2jags.jags(data = radon_data, inits = radon_inits,
                           parameters_to_save = radon_params,
                           n_iter = 500,
                           n_chains = 3,
                           model_file = "16.10.bug")

print jags_schools

'''
            mean   sd    2.5%     25%     50%     75%   97.5% Rhat n.eff
a[1]         3.8  0.8     2.3     3.1     3.7     4.3     5.4    1   750
a[2]         5.1  1.0     3.2     4.4     5.1     5.7     6.9    1   520
a[3]         5.1  1.0     3.1     4.5     5.1     5.8     7.2    1   750
a[4]         0.3  0.8    -1.4    -0.3     0.3     0.9     1.9    1   750
a[5]         2.5  1.2     0.1     1.7     2.4     3.2     4.7    1   750
a[6]         5.5  0.8     4.0     5.0     5.4     6.0     7.0    1   690
a[7]         3.8  0.8     2.3     3.2     3.8     4.3     5.4    1   260
a[8]        -0.3  0.7    -1.8    -0.7    -0.2     0.2     1.1    1   750
a[9]        -1.3  1.2    -3.6    -2.1    -1.3    -0.6     1.0    1   490
a[10]       -3.4  1.0    -5.3    -4.1    -3.4    -2.7    -1.2    1   270
a[11]        1.8  0.9    -0.1     1.2     1.7     2.5     3.6    1   340
a[12]       -0.6  1.0    -2.6    -1.3    -0.6     0.1     1.4    1   340
a[13]       -1.5  0.9    -3.4    -2.2    -1.5    -0.9     0.3    1   470
a[14]       -1.6  0.5    -2.7    -2.0    -1.6    -1.3    -0.6    1   420
a[15]       -1.8  0.8    -3.3    -2.4    -1.9    -1.3    -0.3    1   230
a[16]       -4.1  0.8    -5.5    -4.6    -4.0    -3.5    -2.6    1   750
a[17]       -1.7  0.7    -3.0    -2.1    -1.7    -1.2    -0.4    1   750
a[18]       -0.9  0.6    -2.2    -1.3    -0.9    -0.4     0.3    1   750
a[19]       -0.1  1.0    -1.9    -0.8    -0.1     0.6     1.9    1   270
a[20]        2.2  1.1     0.0     1.5     2.3     3.0     4.3    1   750
a[21]        2.4  0.9     0.6     1.9     2.4     3.0     4.1    1   750
a[22]       -4.3  0.8    -5.8    -4.8    -4.3    -3.8    -2.9    1   750
a[23]       -5.0  1.3    -7.5    -5.8    -5.0    -4.1    -2.4    1   420
a[24]        2.1  1.1    -0.2     1.4     2.1     2.8     4.3    1   750
a[25]       -2.3  0.8    -3.9    -2.9    -2.3    -1.8    -0.8    1   750
a[26]       -0.2  0.8    -1.9    -0.7    -0.2     0.4     1.5    1   500
a[27]        0.3  1.1    -1.8    -0.4     0.2     1.0     2.5    1   750
a[28]       -6.1  1.0    -7.9    -6.8    -6.1    -5.4    -4.3    1   750
a[29]        2.4  0.8     0.8     1.9     2.4     3.0     4.1    1   750
a[30]        1.5  1.1    -0.7     0.8     1.5     2.3     3.5    1   220
a[31]        0.4  1.0    -1.6    -0.3     0.4     1.0     2.4    1   450
a[32]        0.0  1.1    -2.1    -0.8     0.0     0.7     2.1    1   750
a[33]        0.3  0.8    -1.4    -0.3     0.3     0.8     1.9    1   530
a[34]       -1.4  1.3    -3.9    -2.2    -1.4    -0.5     1.2    1   750
a[35]        1.3  1.2    -0.9     0.5     1.3     2.1     3.7    1   260
a[36]       -1.8  0.9    -3.4    -2.4    -1.8    -1.2     0.0    1   750
a[37]       -1.9  1.5    -4.8    -2.9    -1.9    -0.9     1.1    1   750
a[38]       -1.5  1.0    -3.5    -2.2    -1.5    -0.9     0.4    1   750
a[39]        1.4  1.0    -0.7     0.7     1.4     2.0     3.3    1   750
a[40]       -2.3  0.9    -4.0    -2.9    -2.3    -1.8    -0.6    1   750
a[41]        2.1  0.9     0.3     1.5     2.1     2.7     4.0    1   750
a[42]        1.0  0.9    -0.9     0.4     1.0     1.6     2.8    1   700
a[43]       -0.9  0.9    -2.7    -1.5    -0.9    -0.3     0.8    1   750
a[44]       -2.5  1.3    -5.0    -3.4    -2.5    -1.6     0.2    1   750
a[45]       -1.1  1.0    -3.0    -1.7    -1.2    -0.5     0.9    1   750
a[46]       -3.5  0.8    -5.1    -4.1    -3.5    -2.9    -2.0    1   750
a[47]       -0.4  0.8    -1.9    -0.9    -0.4     0.2     1.2    1   750
a[48]       -0.4  2.8    -5.8    -2.2    -0.4     1.5     5.2    1   590
a[49]        0.4  0.7    -1.0     0.0     0.5     0.9     1.8    1   320
a[50]       -3.0  0.8    -4.6    -3.6    -3.0    -2.4    -1.5    1   750
a[51]       -0.5  0.9    -2.4    -1.2    -0.5     0.1     1.2    1   380
a[52]        3.9  0.9     2.0     3.3     3.8     4.5     5.6    1   750
a[53]        7.3  0.9     5.6     6.7     7.3     7.9     9.0    1   750
a[54]       -5.7  2.0    -9.5    -7.1    -5.7    -4.3    -2.0    1   240
a[55]        5.1  1.0     3.2     4.4     5.1     5.8     7.2    1   750
a[56]        0.1  1.1    -2.2    -0.7     0.2     0.9     2.4    1   750
a[57]        0.3  0.9    -1.5    -0.2     0.3     0.9     2.1    1   750
a[58]        1.4  1.2    -0.8     0.6     1.4     2.2     3.8    1   750
a[59]       -6.6  1.1    -8.6    -7.3    -6.6    -5.9    -4.5    1   750
a[60]        2.3  0.8     0.8     1.7     2.3     2.8     3.8    1   750
a[61]       -0.3  0.9    -2.0    -0.9    -0.3     0.3     1.4    1   750
a[62]       -0.5  0.8    -2.1    -1.1    -0.5     0.0     1.2    1   750
a[63]        5.5  1.2     3.3     4.6     5.5     6.3     7.9    1   750
a[64]        0.9  0.9    -0.9     0.3     0.9     1.6     2.7    1   750
a[65]       -1.6  0.8    -3.2    -2.2    -1.7    -1.1     0.0    1   280
b            0.6  0.0     0.5     0.6     0.6     0.6     0.6    1   750
deviance 27901.0 11.4 27880.3 27892.7 27900.3 27908.0 27924.7    1   750
sigma.a      3.2  0.3     2.6     2.9     3.1     3.4     3.9    1    93
sigma.y      7.5  0.1     7.4     7.5     7.5     7.6     7.7    1   450

For each parameter, n.eff is a crude measure of effective sample size,
and Rhat is the potential scale reduction factor (at convergence, Rhat=1).

DIC info (using the rule, pD = var(deviance)/2)
pD = 64.9 and DIC = 27965.9
DIC is an estimate of expected predictive error (lower deviance is better).
'''
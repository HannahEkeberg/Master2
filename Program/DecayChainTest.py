from npat import DecayChain
import csv
import numpy as np

t_irradiation = 1.0     # in hours
name_of_csv_file = './new_csvs/Ni_58Co_128.dat'

### 58m/gCo decay chain, units of hours, assumed 2:1 production rate, for t_irradiation hours
dc = DecayChain('58COm', 'h', R={'58CO':1.0, '58COm':2.0}, time=t_irradiation)
# dc.plot()


### Read in numbers of decays from csv file
def decomment(csvfile):
    for row in csvfile:
        raw = row.split('#')[0].strip()
        if raw: yield raw

results = []
with open(name_of_csv_file) as csvfile:
    reader = csv.reader(decomment(csvfile))
    for row in reader:
        results.append(row)

results = np.asarray(results, dtype=float)


# Reshape csv data structure
list_of_counts = results[:, np.r_[0, 0, 3, 4]]
list_of_counts[:,1] = list_of_counts[:,1] + (results[:,5] / 3600)
print(list_of_counts)

### Calculate decay over timespan of all counts
dc.append(DecayChain('58COm', 'h', time=max(list_of_counts[:,1])))
# dc.plot()

### Measured counts: [start_time (d), stop_time (d), decays, unc_decays]
### Times relative to last appended DecayChain, i.e. EoB time
dc.counts = {'58COg':list_of_counts}



### Find the scaled production rate that gives us these counts
# dc.fit_R( unc=True)
dc.fit_A0( unc=True)
### Only plot the 5 most active isotopes in the decay chain
dc.plot(N_plot=5)
print('              ', dc.isotopes)
print('Activity (Bq):',dc.A0)
print('Uncertainty in Activity (Bq):', dc._unc_A0_fit)
import math as mt

import matplotlib.pyplot as plt
import numpy as np

import gpsinfo_pb2
import macinfo_pb2
import samplesseq_pb2
import sensorcollection_pb2
import vector3_pb2

smp = samplesseq_pb2.Samples()

inf = open("./data/0.pbc", "rb")

smp.ParseFromString(inf.read())
inf.close()

accraw = []
gyrraw = []

for col in smp.data:
    for acc in col.acc:
        accraw.append([acc.x, acc.y, acc.z])
    for gyr in col.gyr:
        gyrraw.append([gyr.x, gyr.y, gyr.z])

duration = smp.data[-1].timestamp - smp.data[0].timestamp
fl = len(accraw) / duration * 1000
print("sample frequency = " + str(fl))

mtracc = np.asarray(accraw)
noracc = []
for al in mtracc:
    noracc.append(mt.sqrt(al[0] ** 2 + al[1] ** 2 + al[2] ** 2) - 9.8)

mtrgyr = np.asarray(gyrraw)
norgyr = []
for gl in mtrgyr:
    norgyr.append(mt.sqrt(gl[0] ** 2 + gl[1] ** 2 + gl[2] ** 2) - 9.8)

plt.figure(1)
plt.plot(noracc)

plt.figure(2)
plt.plot(norgyr)

plt.show()

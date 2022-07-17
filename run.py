import os
import numpy as np
import shutil
import matplotlib.pyplot as plt
def run():
    """
    for i in range(30):
        os.chdir(str(i))
        os.system('fix_ase.py 0.0 0.08')
        #os.remove('POSCAR')
        shutil.copy('POSCAR.new', 'POSCAR')
        os.system('gen_input.py vasp')
        #os.system('qsub pbs-opt')
        os.chdir('..')
    """
       
    for i in range(30):
        os.chdir(str(i))
        shutil.copy('../INCAR', './')
        os.system('qsub pbs-opt')
        os.chdir('..')

def anal():
    energies = []
    ind = []
    for i in range(30):
        A = []
        os.chdir(str(i))
        f = open('OSZICAR', 'r')
        for j in f:
            if ('F=' in j):
                a = j.strip().split()[4]
                A.append(a)
        #print(A[-1])
        energies.append(float(A[-1]))
        ind.append(str(i))
        f.close()
        os.chdir('../')
    energies_1 = energies
    #energies.sort(key=None, reverse=True)
    energies_sort = sorted(energies, reverse=True)
    energies_ave = sum(energies)/30
    print(energies_ave)
    
    num=0
    ind_1 = []
    f = open('result.txt', 'w')
    for i in energies_sort:
        print("No.%d"%num)
        print('structure %s: %f'%(energies_1.index(i), float(i)))
        ind_1.append(str(energies_1.index(i)))
        f.write('structure %s: %f'%(energies_1.index(i), float(i)))
        f.write('\n')
        num+=1
    f.close()
    energies_1 = []
    for i in energies:
        value = i - energies_ave
        energies_1.append(value)

    ticks = np.array(ind_1)
    labels = np.array(ind_1)
    plt.bar(ind, energies_1)
    #plt.bar(ind, energies_sort)
    plt.axhline(0)
    #plt.axhline(energies[2], color='red')
    #plt.xlim(-446,-444)
    plt.ylim(-1,1)
    plt.xlabel('Structure')
    plt.ylabel('Energy(eV)')
    #plt.xticks(ind ,ticks)
    plt.savefig('energy_dis.png', dpi=600)
    plt.show()
#run()
anal()

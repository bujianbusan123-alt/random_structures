# Cu100-553, 4co,8oh, 30 random structures, ranking 6, had 2 co, 1 oh
# x range, y range (0, 0.5)
from ase.io import read, write
from ase.build import add_adsorbate
from ase import Atoms
import os
import random
from ase.collections import g2
from math import sqrt
x=12.7798995972
y=12.7798995972
z=23.6147003174
OH = Atoms('OH', positions=[[0.,0.,0.],[0.,0.,1.2]])
CO = Atoms('CO', positions=[[0.,0.,0.],[0.,0.,1.2]])

#CO-special = Atoms('CO', positions=[[0.66*10.2239,0.65*10.2239,0.41*18.61],[0.63*10.2239,0.76*10.2239,0.40*18.61]])
site = ["ontop", "bridge", "hollow"]
#hollow = (0.1*n1, 0.1*n2)# n1, n2 belong to odd <= 9
#ontop = (0.1*n3, 0.1*n4)# n3,n4 beling to even < 10
#bridge1 = (0.1*n5, 0.2*n6) # n4, belong to odd < 9
#bridge2 = (0.2*n7, 0.1*n8) # n8 belong to odd < 9
#identify active site including top , hollow, bridge, 1.8 ans distance
slabs = []
init_num = 0
def distance(a,b):
    dis_all = []
    for k in b:
        dis = sqrt((a[0]-k[0])**2+(a[1]-k[1])**2)
        dis_all.append(dis)
    return min(dis_all)

while (len(slabs) < 30):
    print(init_num)
    add_pos = []
    origin_atoms = read('/home/project/lxu/Cu100-553/POSCAR')
    add_adsorbate(origin_atoms,CO,1.5, position=(0.5*x,0.7*y))
    add_pos.append((0.5*x,0.7*y))
    OH.rotate(30,'y')
    add_adsorbate(origin_atoms,OH,1.5, position=(0.8*x,0.7*y))
    add_pos.append((0.8*x,0.7*y))
    OH.rotate(-30,'y')
    CO.rotate(240,'x')
   # CO.translate((0.,-0.1*x,0.))
    add_adsorbate(origin_atoms,CO,4.2, position=(0.7*x,0.7*y))
    add_pos.append((0.7*x,0.8*y))
    CO.rotate(-240,'x')
    #CO.translate((0.,0.1*x,0.))

    os.makedirs(str(init_num), exist_ok=True)
    os.chdir(str(init_num))
    # add 2 co, 7 oh
    num_oh = 0
    num_co = 0
    slab = origin_atoms
    pos_ontop = []
    pos_hollow = []
    pos_bridge_1 = []
    pos_bridge_2 = []
    pos_ontop_oh = []
    pos_hollow_oh = []
    pos_bridge_oh_1 = []
    pos_bridge_oh_2 = []
    while (num_co < 3): #num of co
        num = random.randint(0, 2) # active site
        if (site[num]=="ontop"):
            num1 = random.randint(1,9)
            num2 = random.randint(1,9)
            if ((num1%2 == 0) & (num2%2 == 0)):
                if ({num1:num2} not in pos_ontop):
                    pos=(0.1*num1*x,0.1*num2*y)# tuple may be index
                    if (distance(pos,add_pos) > 0.15*x):
                        pos_ontop.append({num1:num2})
                        add_pos.append(pos)
                        add_adsorbate(slab, CO, 1.5, position=(0.1*num1*x,0.1*num2*y))
                        num_co += 1
        elif (site[num] == "hollow"):
            num3 = random.randint(1,9)
            num4 = random.randint(1,9)
            if ((num3%2 != 0) & (num4%2 != 0)):
                if ({num3:num4} not in pos_hollow):
                    pos = (0.1*num3*x,0.1*num4*y)
                    if (distance(pos,add_pos) > 0.15*x):
                        pos_hollow.append({num3:num4})
                        add_pos.append(pos)
                        add_adsorbate(slab, CO, 1.5, position=(0.1*num3*x,0.1*num4*y))
                        num_co += 1
        elif (site[num] == "bridge"):
            num_rand = random.randint(1,10)
            if (num_rand%2 != 0):
                num5 = random.randint(1,9)
                num6 = random.randint(1,4)
                if (num5%2 != 0):
                    if ({num5:num6} not in pos_bridge_1):
                        pos = (0.1*num5*x,0.2*num6*y) 
                        if (distance(pos,add_pos) > 0.15*x):
                            pos_bridge_1.append({num5:num6})
                            add_pos.append(pos)
                            add_adsorbate(slab, CO, 1.5, position=(0.1*num5*x,0.2*num6*y))
                            num_co += 1
            else:
                num5 = random.randint(1,9)
                num6 = random.randint(1,4)
                if (num5%2 != 0):
                    if ({num5:num6} not in pos_bridge_2):
                        pos = (0.2*num6*x,0.1*num5*y) 
                        if (distance(pos,add_pos) > 0.15*x):
                            pos_bridge_2.append({num5:num6}) 
                            add_pos.append(pos)
                            add_adsorbate(slab, CO, 1.5, position=(0.2*num6*x,0.1*num5*y))
                            num_co += 1
    while (num_oh < 7):
        #print(num_oh)
        num = random.randint(0, 2)
        if (site[num]=="ontop"):
            num1 = random.randint(1,9)
            num2 = random.randint(1,9)
            if ((num1%2 == 0) & (num2%2 == 0)):
                if ({num1:num2} not in pos_ontop_oh):
                    pos = (0.1*num1*x,0.1*num2*y)
                    if (distance(pos,add_pos) > 0.15*x):
                        pos_ontop_oh.append({num1:num2})
                        add_pos.append(pos)
                        add_adsorbate(slab, OH, 1.5, position=(0.1*num1*x,0.1*num2*y))
                        num_oh += 1
        elif (site[num] == "hollow"):
            num3 = random.randint(1,9)
            num4 = random.randint(1,9)
            if ((num3%2 != 0) & (num4%2 != 0)):
                if ({num3:num4} not in pos_hollow_oh):
                    pos = (0.1*num*x,0.1*num4*y)
                    if (distance(pos, add_pos) > 0.15*x):
                        pos_hollow_oh.append({num3:num4})
                        add_pos.append(pos)
                        add_adsorbate(slab, OH, 1.5, position=(0.1*num*x,0.1*num4*y))
                        num_oh += 1
        elif (site[num] == "bridge"):
            num_rand = random.randint(1,10)
            if (num_rand%2 == 0):
                num5 = random.randint(1,9)
                num6 = random.randint(1,4)
                if (num5%2 != 0):
                    if ({num5:num6} not in pos_bridge_oh_1):
                        pos = (0.1*num5*x,0.2*num6*y)
                        if (distance(pos,add_pos) > 0.15*x):
                            pos_bridge_oh_1.append({num5:num6})
                            add_pos.append(pos)
                            add_adsorbate(slab, OH, 1.5,position=(0.1*num5*x,0.2*num6*y))
                            num_oh += 1
            else:
                num5 = random.randint(1,9)
                num6 = random.randint(1,4)
                if (num5%2 != 0):
                    if ({num5:num6} not in pos_bridge_oh_2):
                        pos = (0.2*num6*x, 0.1*num5*y)
                        if (distance(pos, add_pos) > 0.15*x):
                            pos_bridge_oh_2.append({num5:num6})
                            add_pos.append(pos)    
                            add_adsorbate(slab, OH, 1.5, position=(0.2*num6*x, 0.1*num5*y))
                            num_oh += 1
            
    if (slab not in slabs):
        slabs.append(slab)
        write("POSCAR", slab, vasp5=True, direct=True)
        init_num += 1
    os.chdir('..')

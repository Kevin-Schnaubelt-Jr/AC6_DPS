damage=560.0
impact=30
acc_impact=88
fire_rate=1.3
reload_time=4 + 0.3
mag=4
is_heat_mag = True
is_overheat = False
is_charged_attack = False
is_charged_infinite = False
charge_time=3.5
charged_attack_mag=2
charged_fire_rate=1.7
energy_specialization = 100
heat_build=161
cooling_rate=303
cooling_delay=1.4
overheat_cooling_rate=100
overheat_cooling_delay=2
if (is_heat_mag):
    energy_specialization-=100
    damage = damage * (1 + energy_specialization * 0.005)
    mag = 1000 // heat_build
    if (heat_build * mag == 1000):
        mag-=1
    reload_time = (mag * heat_build) / cooling_rate
    if (is_overheat):
        reload_time = 1000 / (cooling_rate * overheat_cooling_rate * 0.01)
        mag+=1
        reload_time+=overheat_cooling_delay
        reload_time = round(reload_time, 3)
    else:
        reload_time+=cooling_delay
        reload_time = round(reload_time, 3)
    print(f"{heat_build=}")
    print(f"{cooling_rate=}")
    print(f"{cooling_delay=}")
    print(f"{overheat_cooling_rate=}")
    print(f"{overheat_cooling_delay=}")
    if (is_charged_attack):
        charge_time = charge_time * (100 - energy_specialization) * 0.01
        print(f"{charge_time=}")
        fire_rate = charged_fire_rate + charge_time + 0.7
        mag = charged_attack_mag
        reload_time = 1000 / (cooling_rate * overheat_cooling_rate * 0.01)
        reload_time+=overheat_cooling_delay
        reload_time = round(reload_time, 3)
        if (is_charged_infinite):
            mag=1
            reload_time = 0



total_damage = mag * damage
total_impact = mag * impact
total_acc_impact = mag * acc_impact
fire_time = mag * fire_rate
if (is_heat_mag == True and is_charged_infinite == False):
        if (is_charged_attack):
            fire_time -= charged_fire_rate
        else:
             fire_time -= fire_rate
total_time = fire_time + reload_time
print(f"{total_time=}")
print(f"{fire_time=}")
dps = round(total_damage / total_time, 1)
ips = round(total_impact / total_time, 1)
acc_ips = round(total_acc_impact / total_time, 1)

print(f"{total_damage=}")
print(f"{total_impact=}")
print(f"{total_acc_impact=}")
print(f"{damage=}")
print(f"{impact=}")
print(f"{acc_impact=}")
print(f"{fire_rate=}")
print(f"{reload_time=}")
print(f"{mag=}")
print(f"{dps=}")
print(f"{ips=}")
print(f"{acc_ips=}")

'''
---Rifles---

___Turner___
W 3560
R 171
total_damage=1890 
total_impact=1170 
total_acc_impact=504 
damage=105
impact=65
acc_impact=28
fire_rate=0.3 * 0.28
reload_time=2.2 
mag=18 
dps=248.6 * 261
ips=153.9 * 161.6
acc_ips=66.3 * 69.6

___Scudder___
total_damage=2025 
total_impact=1230 
total_acc_impact=585 
damage=135
impact=82
acc_impact=39
fire_rate=0.35  
reload_time=2.4 
mag=15 
dps=264.7 
ips=160.8 
acc_ips=76.5

___AK-47___
total_damage=1848
total_impact=1176
total_acc_impact=600
damage=77
impact=49
acc_impact=25
fire_rate=0.21
reload_time=2.2
mag=24
dps=255.2
ips=162.4
acc_ips=82.9

___Attache___
total_damage=2480
total_impact=2480
total_acc_impact=1000
damage=62
impact=62
acc_impact=25
fire_rate=0.2 * 0.16
reload_time=2.1 * 2.2
mag=40
dps=245.5 * 288.4
ips=245.5 * 288.4
acc_ips=99.0 * 116.3

___LudLow___
total_damage=1260
total_impact=1230
total_acc_impact=570
damage=42
impact=41
acc_impact=19
fire_rate=0.1
reload_time=1.5
mag=30
dps=280.0
ips=273.3333333333333
acc_ips=126.66666666666667

___Chen___
total_damage=1755
total_impact=1800
total_acc_impact=810
damage=39
impact=40
acc_impact=18
fire_rate=0.1 * 0.9
reload_time=2.2 * 2.4
mag=45
dps=261.9 * 272.1
ips=268.7 * 279.1
acc_ips=120.9 * 125.6

___AK-47U___
total_damage=1104
total_impact=1152
total_acc_impact=528
damage=46 * 47
impact=48
acc_impact=22 * 21
fire_rate=0.1375 * .11
reload_time=1.5
mag=24 * 28
dps=230.0 * 287.3
ips=240.0 * 293.4
acc_ips=110.0 * 128.4

___GAT___
heat_build=9
cooling_rate=220 * 194
cooling_delay=1 * 0.4
overheat_cooling_rate=85 * 95
overheat_cooling_delay=1.3 * 0.7
total_damage=2775
total_impact=2220
total_acc_impact=1221 
damage=25
impact=20
acc_impact=11
fire_rate=0.05
reload_time=5.5 * 5.0
mag=111
-IDEAL-
dps=251.2 * 151.0
ips=201.0
acc_ips=110.5
-OVERHEAT-
dps=229.5 * 239.8
ips=183.6
acc_ips=101 * 105.5

___back gat___
heat_build=39
cooling_rate=650
cooling_delay=0.125
overheat_cooling_rate=90
overheat_cooling_delay=0.8
total_damage=624
total_impact=520
total_acc_impact=286
damage=24
impact=20
acc_impact=11
fire_rate=0.07
reload_time=1.6584615384615384
mag=26
-IDEAL-
dps=179.38965059708093
ips=149.49137549756745
acc_ips=82.22025652366209
-OVERHEAT-
dps=147.29275542517433
ips=122.74396285431196
acc_ips=67.50917956987158

---Shotguns---

___Halderman___
total_time=1.4000000000000001
fire_time=0.1
total_damage=576
total_impact=360
total_acc_impact=280
damage=576
impact=360
acc_impact=280
fire_rate=0.1
reload_time=1.3
mag=1
dps=411.4
ips=257.1
acc_ips=200.0

___Zimmerman___
total_time=2.1
fire_time=0.1
total_damage=800
total_impact=620
total_acc_impact=360
damage=800
impact=620
acc_impact=360
fire_rate=0.1
reload_time=2
mag=1
dps=381.0
ips=295.2
acc_ips=171.4

---Pistols---

___Coquillett___
total_time=4.9
total_damage=1162
total_impact=1645
total_acc_impact=1043
damage=166
impact=235
acc_impact=149
fire_rate=0.4
reload_time=2.1
mag=7
dps=237.1
ips=335.7
acc_ips=212.9

___Duckett___
total_time=6.7
total_damage=1645
total_impact=2100
total_acc_impact=1057
damage=235
impact=300
acc_impact=151
fire_rate=0.6
reload_time=2.5
mag=7
dps=245.5 
ips=313.4
acc_ips=157.8

___Viento___
total_time=3.15
total_damage=905
total_impact=975
total_acc_impact=635
damage=181
impact=195
acc_impact=127
fire_rate=0.25
reload_time=1.9
mag=5
dps=287.3
ips=309.5
acc_ips=201.6

---Lasers---

___LH___
heat_build=90
cooling_rate=315
cooling_delay=0.5
overheat_cooling_rate=85 * 90
overheat_cooling_delay=1.3 * 0.5
total_damage=1925
total_impact=1045
total_acc_impact=429
damage=175
impact=95
acc_impact=39
fire_rate=0.4
reload_time=3.6
mag=11
-IDEAL-
dps=251.9
ips=136.7
acc_ips=56.1
-OVERHEAT-
dps=222.6 * 249.2
ips=120.8
acc_ips=49.6
-CHARGED-
dps=294.9

___LR___
heat_build=160
cooling_rate=413
cooling_delay=0.7
overheat_cooling_rate=85
overheat_cooling_delay=1.3 * 0.7
charge_time=1.6
total_damage=1536
total_impact=624
total_acc_impact=276
damage=256
impact=104
acc_impact=46
fire_rate=0.6
reload_time=3.121
mag=6
-IDEAL-
dps=255.0
ips=103.6
acc_ips=45.8
-OVERHEAT-
dps=231.3 * 250.7
ips=93.9
acc_ips=41.6
-CHARGED-
charged_fire_rate=2
dps=284.2

___LRA___
charge_time= 3.8 * 3.4
heat_build=205
cooling_rate=281
cooling_delay=1
overheat_cooling_rate=85 * 95
overheat_cooling_delay=1.6 * 1
total_damage=2215
total_impact=970
total_acc_impact=405
damage=443
impact=194
acc_impact=81
fire_rate=0.9
reload_time=4.559
mag=4
-IDEAL-
dps=267.8
ips=117.3
acc_ips=49.0
-OVERHEAT-
dps=236.0 * 261.6
ips=103.3
acc_ips=43.1
-CHARGED-
damage=1677
fire_rate=2
charge_time=3.8
dps=258.0 * 274.9

___LRB___
charged_heat = 1000
heat_build=280
cooling_rate=246
cooling_delay=1.7
overheat_cooling_rate=85
overheat_cooling_delay=1.7
total_damage=2334
total_impact=864
total_acc_impact=402
damage=778
impact=288
acc_impact=134
fire_rate=1.4
reload_time=5.765
mag=3
-IDEAL-
dps=295
ips=100.9
acc_ips=52
-OVERHEAT-
dps=291.3
ips=107.8
acc_ips=50.2
-CHARGED-
damage=1176 * 2
fire_rate=2
charge_time=2.3 * 1.8
dps=248.0 * 261.9

___Wuerger/66E___
heat_build=180
cooling_rate=291
cooling_delay=1
overheat_cooling_rate=85
overheat_cooling_delay=1
total_time=9.543
fire_time=4.5
total_damage=3024.0
total_impact=2430
total_acc_impact=864
damage=504.0
impact=405
acc_impact=144
fire_rate=0.9
reload_time=5.043
mag=6
-IDEAL-
dps=327.6
ips=263.2
acc_ips=93.6
-OVERHEAT-
dps=316.9
ips=254.6
acc_ips=90.5

___KRSV___
heat_build=120
cooling_rate=167
cooling_delay=0.7
overheat_cooling_rate=70 * 100
overheat_cooling_delay=2 * .7
total_time=8.549
fire_time=2.1
total_damage=2496.0
total_impact=896
total_acc_impact=608
damage=312.0
impact=112
acc_impact=76
fire_rate=0.3 * .38
reload_time=6.449
mag=8
-IDEAL-
dps=292.0 * 288.7
ips=104.8
acc_ips=71.1
-OVERHEAT-
dps=216.8
ips=77.8
acc_ips=52.8
-CHARGED 1-
damage=1098
charged_mag = 5
charged_fire_rate = 1.2 * 1.4
charge_time=0.5
dps=257.1 * dps=300.2
-CHARGED 2-
damage=2522
charged_mag = 1 * 2
charged_fire_rate = 2 * 1.7
charge_time=4.5 * 3.5
heat = 995
dps=160.1

___Laser Shotgun___
heat_build=190 * 161
cooling_rate=203 * 303
cooling_delay=1.4
overheat_cooling_rate=85  * 100
overheat_cooling_delay=1.6 * 2
total_time=11.526
fire_time=5.2
total_damage=2800.0       
total_impact=1520
total_acc_impact=440      
damage=560.0
impact=304
acc_impact=88
fire_rate=1.3
reload_time=6.326
mag=5
-IDEAL-
dps=248.2 * 303
ips=134.8
acc_ips=39.0
-OVERHEAT-
dps=241.8 * 299.2
ips=131.3
acc_ips=38.0
-CHARGED-
damage=1307
charge_time=.9
charged_fire_rate=1.3
charged_attack_mag=2
dps=219.8
dps=252 on staggered target - 45di

___WLT___
heat_build=200
cooling_rate=180
cooling_delay=1
overheat_cooling_rate=85
overheat_cooling_delay=1.6
total_time=8.144
fire_time=2.7
total_damage=1620.0
total_impact=608
total_acc_impact=608
damage=405.0
impact=152
acc_impact=152
fire_rate=0.9
reload_time=5.444
mag=4
-IDEAL-
dps=198.9
ips=74.7
acc_ips=74.7
-OVERHEAT-
dps=172.5
ips=64.8
acc_ips=64.8



___LCS___
heat_build=320
cooling_rate=210
cooling_delay=1.7
overheat_cooling_rate=85
overheat_cooling_delay=1.6
total_time=9.271
fire_time=3.0
total_damage=2775.0
total_impact=1500
total_acc_impact=540
damage=925.0
impact=500
acc_impact=180
fire_rate=1.5
reload_time=6.271
mag=3
-IDEAL-
dps=299.3
ips=161.8
acc_ips=58.2
-OVERHEAT-
dps=316.2
ips=170.9
acc_ips=61.5

___LCD___
heat_build=440
cooling_rate=232
cooling_delay=1.7
overheat_cooling_rate=85
overheat_cooling_delay=1.6
total_damage=2616
total_impact=1296
total_acc_impact=408
damage=1308
impact=648
acc_impact=204
fire_rate=1.8
reload_time=6.0103448275862075
mag=2
-IDEAL-
dps=272.2066738428418
ips=134.85468245425187
acc_ips=42.45425188374596
-OVERHEAT-
dps=325.0767938161654
ips=161.04721895479753
acc_ips=50.700050411695514

___LCB___
heat_build=320
cooling_rate=172
cooling_delay=2.3
overheat_cooling_rate=75
overheat_cooling_delay=2
total_time=11.881
fire_time=4
total_damage=3603.0
total_impact=2280
total_acc_impact=540
damage=1201.0
impact=760
acc_impact=180
fire_rate=2
reload_time=7.881
mag=3
-IDEAL-
dps=303.3
ips=191.9
acc_ips=45.5
-OVERHEAT-
dps=305.0
ips=193.0
acc_ips=45.7

___Pulse Gun 1___
cooling_rate=623
cooling_delay=0.4
overheat_cooling_rate=85
overheat_cooling_delay=1.3
total_damage=1102
total_impact=319
total_acc_impact=174
damage=38
impact=11
acc_impact=6
fire_rate=0.05
reload_time=2.
mag=29
-IDEAL-
dps=318.9
ips=92.3
acc_ips=50.3
-OVERHEAT-
dps=243.1
ips=70.3
acc_ips=38.3

___Pulse Gun 2___
heat_build=55
cooling_rate=295
cooling_delay=0.4
overheat_cooling_rate=85 
overheat_cooling_delay=1.3 
total_damage=1224
total_impact=432
total_acc_impact=216
damage=68
impact=24
acc_impact=12
fire_rate=0.1
reload_time=3.789830508474576
mag=18
-IDEAL-
dps=218.9
ips=77.2
acc_ips=38.6
-OVERHEAT-
dps=179.74312028406567 * 276.9
ips=63.4 * 97.7
acc_ips=31.7 * 48.8

---LRs---

___RF___
charged_direct_damage=120 * 130
ideal = 200
vel = 530
total_damage=3360
total_impact=3675
total_acc_impact=1365
damage=224
impact=245
acc_impact=91
fire_rate=0.7
reload_time=1.9
mag=15
dps=270.9
ips=296.3
acc_ips=110.0

___Curtis___
Velocity=600 * 700
charged_velocity= 840
total_time=7.0
fire_time=4.8
total_damage=1704
total_impact=1620
total_acc_impact=624
damage=142 * 149
impact=135
acc_impact=52
fire_rate=0.4
reload_time=2.2
mag=12
dps=243.4
ips=231.4
acc_ips=89.1

___Harris___
Velocity=650 * 730
charged_velocity= 900
total_time=11.0
fire_time=8.0
total_damage=2390
total_impact=2850
total_acc_impact=1090
damage=239 * 267
impact=285
acc_impact=109
fire_rate=0.8
reload_time=3 * 1.9
mag=10
dps=217.3 * 269.7
ips=259.1
acc_ips=99.1
--CHARGED--
damage=977 * 1122
direct_impact=120 * 130

---Missiles---

___Active Homing Missiles___
homingAngle = 115 * 135

___vert missiles___
homingStopRange = 45 * 11

___vert plasma missile Vvc-70VPM___
homingStopRange = 32 * 18

___4 pod normal___
damage=103
impact=72
acc_impact=43
fire_rate=0.05
reload_time=4
lock_time=0.3
dps=91.6
ips=84.4
acc_ips=34.7

___6 pod normal___
damage=103
impact=72
acc_impact=43
fire_rate=0.08
reload_time=5
lock_time=0.4
dps=105.1
ips=73.5
acc_ips=43.9

___10 pod normal___
damage=103
impact=72
acc_impact=43
fire_rate=0.16
reload_time=6.4
lock_time=0.8
dps=117.0
ips=81.8
acc_ips=48.9

---Generators---

___AORTA___
EnergyFirearmSpec=105 * 110

___NGI 000___
EnergyFirearmSpec=110 * 115

'''
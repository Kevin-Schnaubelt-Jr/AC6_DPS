damage=2352
impact=690
acc_impact=330
fire_rate=2
charge_time=3.8
reload_time=4.559
mag=28
is_heat_mag = True
is_overheat = False
is_charged_attack = False
is_charged_infinite = False
charged_attack_mag= 1
energy_specialization = 100
heat_build = 420
cooling_rate = 246
cooling_delay = 1.7
overheat_cooling_rate = 85
overheat_cooling_delay = 1.7
if (is_heat_mag):
    energy_specialization-=100
    damage = damage * (1 + energy_specialization * 0.005)
    mag = 1000 // heat_build
    if (heat_build * mag == 1000):
        mag-=1
    reload_time = 1000 / cooling_rate
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
        fire_rate = fire_rate + charge_time
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
total_time = fire_time + reload_time
print(f"{total_time=}")
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
---Vanilla---
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
cooling_rate=220
cooling_delay=1 * 0.5
overheat_cooling_rate=85
overheat_cooling_delay=1.3 * 1
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
dps=250.1 * 261.9
ips=200.0 * 209.5
acc_ips=110.0 * 115.2
-OVERHEAT-
dps=228.6 * 234.4
ips=182.8 * 187.5
acc_ips=100.5 * 103.1

___back gat___
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

___LH___
cooling_rate=315
cooling_delay=0.5
overheat_cooling_rate=85
overheat_cooling_delay=1.3
total_damage=1925
total_impact=1045
total_acc_impact=429
damage=175
impact=95
acc_impact=39
fire_rate=0.4
reload_time=3.6746031746031744
mag=11
-IDEAL-
dps=238.401808531551
ips=129.4181246314134
acc_ips=53.12954590131709
-OVERHEAT-
dps=213.5268819245996
ips=115.91459304478263
acc_ips=47.58599082891077

___LR___
heat_build=160
cooling_rate=413
cooling_delay=0.7
overheat_cooling_rate=85
overheat_cooling_delay=1.3
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
dps=228.5
ips=92.8
acc_ips=41.0
-OVERHEAT-
dps=214.6 * 244.8
ips=87.2 * 99.4
acc_ips=38.5 * 44.0
-CHARGED-
dps=339.4
ips=138.9
acc_ips=50.0

___LRA___
heat_build=205
cooling_rate=281
cooling_delay=1
overheat_cooling_rate=85
overheat_cooling_delay=1.6
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
dps=217.2
ips=95.1
acc_ips=39.7
-OVERHEAT-
dps=215.3 * 244.5
ips=94.3 * 107.1
acc_ips=39.4 * 44.7
-CHARGED-
dps=289.1
ips=92.2
acc_ips=39.7

___LRB___
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
dps=234.2 
ips=86.7
acc_ips=40.3
-OVERHEAT-
dps=257.6 * 273.8
ips=95.3 * 101.4
acc_ips=44.4 * 47.2
-CHARGED-
dps=191.5
ips=56.2
acc_ips=26.9



___WLT___
heat_build=201
cooling_rate=200
cooling_delay=1
overheat_cooling_rate=85
overheat_cooling_delay=1.6
total_damage=1620
total_impact=608
total_acc_impact=608
damage=405
impact=152
acc_impact=152
fire_rate=0.9
reload_time=6.0
mag=4
-IDEAL-
dps=168.8
ips=63.3
acc_ips=63.3
-OVERHEAT-
dps=169.0
ips=63.4
acc_ips=63.4


___LS___
cooling_rate=203
cooling_delay=1.4
overheat_cooling_rate=85
overheat_cooling_delay=1.6
total_damage=2800
total_impact=1520
total_acc_impact=440
damage=560
impact=304
acc_impact=88
fire_rate=1.3
reload_time=6.326108374384237
mag=5
-IDEAL-
dps=218.3047202058609
ips=118.50827668318162
acc_ips=34.305027460920996
-OVERHEAT-
dps=221.11923477385324
ips=120.03615602009175
acc_ips=34.74730832160551

___LCS___
cooling_rate=210
cooling_delay=1.7
overheat_cooling_rate=85
overheat_cooling_delay=1.6
total_damage=2775
total_impact=1500
total_acc_impact=540
damage=925
impact=500
acc_impact=180
fire_rate=1.5
reload_time=6.461904761904762
mag=3
-IDEAL-
dps=253.14943527367507
ips=136.8375325803649
acc_ips=49.26151172893136
-OVERHEAT-
dps=280.2554527709412
ips=151.48943393023848
acc_ips=54.536196214885855

___LCD___
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
cooling_rate=172
cooling_delay=2.3
overheat_cooling_rate=75
overheat_cooling_delay=2
total_damage=3603
total_impact=2280
total_acc_impact=540
damage=1201
impact=760
acc_impact=180
fire_rate=2
reload_time=8.113953488372093
mag=3
-IDEAL-
dps=255.27928818586258
ips=161.5422639644093
acc_ips=38.260009886307465
-OVERHEAT-
dps=270.61834061135374
ips=171.24890829694323
acc_ips=40.5589519650655

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
reload_time=2.0051364365971107
mag=29
-IDEAL-
dps=318.94543680750735
ips=92.32631065480476
acc_ips=50.35980581171169
-OVERHEAT-
dps=243.15353198482322
ips=70.38654873244883
acc_ips=38.39266294497209

___Pulse Gun 2___
heat_build=55 * 50
cooling_rate=295
cooling_delay=0.4
overheat_cooling_rate=85 * 115
overheat_cooling_delay=1.3 * 0.4
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
dps=218.9 * 249.7
ips=77.2 * 88.1
acc_ips=38.6 * 44.0
-OVERHEAT-
dps=179.74312028406567 * 276.9
ips=63.4 * 97.7
acc_ips=31.7 * 48.8

___KRSV___
heat_build=120
cooling_rate=167
cooling_delay=0.7
overheat_cooling_rate=70
overheat_cooling_delay=2
total_damage=2496
total_impact=896
total_acc_impact=608
damage=312
impact=112
acc_impact=76
fire_rate=0.3
reload_time=6.688023952095809
mag=8
-IDEAL-
dps=274.6
ips=98.5
acc_ips=66.9
-OVERHEAT-
dps=211.85545652272128
ips=76.05067670046405
acc_ips=51.60581633245775

___RF___
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

---Missiles---

___Active Homing Missiles___
homingAngle = 115 * 135

___vert missiles___
homingStopRange = 45 * 11

___vert plasma missile Vvc-70VPM___
homingStopRange = 32 * 18

---Generators---

___AORTA___
EnergyFirearmSpec=105 * 110

___NGI 000___
EnergyFirearmSpec=110 * 115

'''
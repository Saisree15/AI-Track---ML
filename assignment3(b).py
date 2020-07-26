import math
x0=2
y0=5
eta=0.01
eps=0.000001
del_x=1
del_y=1
max_iter=100
iters=0

def diff(x,y):
    x_der=6*(x)
    b=math.exp(-y)
    y_der=-5*b
    return x_der,y_der
while max(abs(del_x),abs(del_y))>eps and iters<max_iter:
    p_x=x0
    p_y=y0
    del_x,del_y=diff(p_x,p_y)
    del_x=-eta*del_x
    del_y=-eta*del_y
    x0=x0+del_x
    y0=y0+del_y
    iters=iters+1
    print("Iteraction",iters,"\n X value is",x0,"\n Y value is",y0)
print("The Local minimum occurs at",x0,y0)

""""OUTPUT:
    
    Iteraction 1 
 X value is 1.88 
 Y value is 5.000336897349954
Iteraction 2 
 X value is 1.7671999999999999 
 Y value is 5.000673681219201
Iteraction 3 
 X value is 1.661168 
 Y value is 5.001010351684171
Iteraction 4 
 X value is 1.5614979199999999 
 Y value is 5.001346908821216
Iteraction 5 
 X value is 1.4678080448 
 Y value is 5.001683352706614
Iteraction 6 
 X value is 1.3797395621119999 
 Y value is 5.002019683416564
Iteraction 7 
 X value is 1.29695518838528 
 Y value is 5.002355901027188
Iteraction 8 
 X value is 1.219137877082163 
 Y value is 5.002692005614531
Iteraction 9 
 X value is 1.1459896044572333 
 Y value is 5.003027997254563
Iteraction 10 
 X value is 1.0772302281897992 
 Y value is 5.003363876023175
Iteraction 11 
 X value is 1.0125964144984112 
 Y value is 5.003699641996184
Iteraction 12 
 X value is 0.9518406296285066 
 Y value is 5.00403529524933
Iteraction 13 
 X value is 0.8947301918507962 
 Y value is 5.004370835858275
Iteraction 14 
 X value is 0.8410463803397484 
 Y value is 5.004706263898606
Iteraction 15 
 X value is 0.7905835975193636 
 Y value is 5.005041579445835
Iteraction 16 
 X value is 0.7431485816682017 
 Y value is 5.005376782575396
Iteraction 17 
 X value is 0.6985596667681097 
 Y value is 5.005711873362649
Iteraction 18 
 X value is 0.6566460867620231 
 Y value is 5.006046851882877
Iteraction 19 
 X value is 0.6172473215563017 
 Y value is 5.006381718211288
Iteraction 20 
 X value is 0.5802124822629235 
 Y value is 5.006716472423014
Iteraction 21 
 X value is 0.5453997333271481 
 Y value is 5.0070511145931125
Iteraction 22 
 X value is 0.5126757493275192 
 Y value is 5.007385644796564
Iteraction 23 
 X value is 0.4819152043678681 
 Y value is 5.007720063108275
Iteraction 24 
 X value is 0.453000292105796 
 Y value is 5.008054369603077
Iteraction 25 
 X value is 0.42582027457944827 
 Y value is 5.008388564355725
Iteraction 26 
 X value is 0.4002710581046814 
 Y value is 5.0087226474409015
Iteraction 27 
 X value is 0.3762547946184005 
 Y value is 5.0090566189332115
Iteraction 28 
 X value is 0.35367950694129646 
 Y value is 5.0093904789071875
Iteraction 29 
 X value is 0.33245873652481867 
 Y value is 5.009724227437285
Iteraction 30 
 X value is 0.31251121233332957 
 Y value is 5.010057864597887
Iteraction 31 
 X value is 0.2937605395933298 
 Y value is 5.010391390463302
Iteraction 32 
 X value is 0.27613490721773004 
 Y value is 5.0107248051077615
Iteraction 33 
 X value is 0.25956681278466626 
 Y value is 5.011058108605426
Iteraction 34 
 X value is 0.24399280401758627 
 Y value is 5.011391301030381
Iteraction 35 
 X value is 0.2293532357765311 
 Y value is 5.011724382456636
Iteraction 36 
 X value is 0.21559204162993925 
 Y value is 5.01205735295813
Iteraction 37 
 X value is 0.2026565191321429 
 Y value is 5.012390212608724
Iteraction 38 
 X value is 0.1904971279842143 
 Y value is 5.0127229614822095
Iteraction 39 
 X value is 0.17906730030516144 
 Y value is 5.013055599652302
Iteraction 40 
 X value is 0.16832326228685174 
 Y value is 5.013388127192642
Iteraction 41 
 X value is 0.15822386654964063 
 Y value is 5.0137205441768
Iteraction 42 
 X value is 0.14873043455666218 
 Y value is 5.0140528506782704
Iteraction 43 
 X value is 0.13980660848326246 
 Y value is 5.014385046770476
Iteraction 44 
 X value is 0.1314182119742667 
 Y value is 5.014717132526766
Iteraction 45 
 X value is 0.1235331192558107 
 Y value is 5.015049108020415
Iteraction 46 
 X value is 0.11612113210046206 
 Y value is 5.0153809733246275
Iteraction 47 
 X value is 0.10915386417443433 
 Y value is 5.015712728512533
Iteraction 48 
 X value is 0.10260463232396827 
 Y value is 5.016044373657188
Iteraction 49 
 X value is 0.09644835438453017 
 Y value is 5.016375908831577
Iteraction 50 
 X value is 0.09066145312145836 
 Y value is 5.016707334108613
Iteraction 51 
 X value is 0.08522176593417086 
 Y value is 5.017038649561135
Iteraction 52 
 X value is 0.0801084599781206 
 Y value is 5.017369855261911
Iteraction 53 
 X value is 0.07530195237943337 
 Y value is 5.017700951283634
Iteraction 54 
 X value is 0.07078383523666737 
 Y value is 5.018031937698928
Iteraction 55 
 X value is 0.06653680512246733 
 Y value is 5.0183628145803425
Iteraction 56 
 X value is 0.06254459681511929 
 Y value is 5.018693582000357
Iteraction 57 
 X value is 0.058791921006212125 
 Y value is 5.019024240031378
Iteraction 58 
 X value is 0.0552644057458394 
 Y value is 5.019354788745739
Iteraction 59 
 X value is 0.05194854140108904 
 Y value is 5.019685228215704
Iteraction 60 
 X value is 0.048831628917023695 
 Y value is 5.020015558513464
Iteraction 61 
 X value is 0.045901731182002276 
 Y value is 5.020345779711139
Iteraction 62 
 X value is 0.04314762731108214 
 Y value is 5.020675891880777
Iteraction 63 
 X value is 0.040558769672417214 
 Y value is 5.021005895094356
Iteraction 64 
 X value is 0.03812524349207218 
 Y value is 5.02133578942378
Iteraction 65 
 X value is 0.03583772888254785 
 Y value is 5.021665574940886
Iteraction 66 
 X value is 0.033687465149594975 
 Y value is 5.021995251717435
Iteraction 67 
 X value is 0.03166621724061928 
 Y value is 5.022324819825121
Iteraction 68 
 X value is 0.02976624420618212 
 Y value is 5.0226542793355655
Iteraction 69 
 X value is 0.027980269553811193 
 Y value is 5.0229836303203195
Iteraction 70 
 X value is 0.026301453380582523 
 Y value is 5.023312872850863
Iteraction 71 
 X value is 0.02472336617774757 
 Y value is 5.023642006998606
Iteraction 72 
 X value is 0.023239964207082717 
 Y value is 5.023971032834887
Iteraction 73 
 X value is 0.021845566354657755 
 Y value is 5.024299950430975
Iteraction 74 
 X value is 0.02053483237337829 
 Y value is 5.024628759858068
Iteraction 75 
 X value is 0.019302742430975593 
 Y value is 5.024957461187294
Iteraction 76 
 X value is 0.018144577885117058 
 Y value is 5.025286054489713
Iteraction 77 
 X value is 0.017055903212010035 
 Y value is 5.02561453983631
Iteraction 78 
 X value is 0.01603254901928943 
 Y value is 5.025942917298004
Iteraction 79 
 X value is 0.015070596078132065 
 Y value is 5.026271186945644
Iteraction 80 
 X value is 0.014166360313444142 
 Y value is 5.0265993488500085
Iteraction 81 
 X value is 0.013316378694637494 
 Y value is 5.026927403081805
Iteraction 82 
 X value is 0.012517395972959243 
 Y value is 5.027255349711673
Iteraction 83 
 X value is 0.011766352214581688 
 Y value is 5.0275831888101825
Iteraction 84 
 X value is 0.011060371081706787 
 Y value is 5.027910920447833
Iteraction 85 
 X value is 0.01039674881680438 
 Y value is 5.028238544695056
Iteraction 86 
 X value is 0.009772943887796117 
 Y value is 5.028566061622213
Iteraction 87 
 X value is 0.00918656725452835 
 Y value is 5.028893471299596
Iteraction 88 
 X value is 0.00863537321925665 
 Y value is 5.029220773797429
Iteraction 89 
 X value is 0.008117250826101251 
 Y value is 5.029547969185867
Iteraction 90 
 X value is 0.007630215776535176 
 Y value is 5.029875057534994
Iteraction 91 
 X value is 0.007172402829943065 
 Y value is 5.030202038914829
Iteraction 92 
 X value is 0.006742058660146481 
 Y value is 5.030528913395319
Iteraction 93 
 X value is 0.006337535140537693 
 Y value is 5.030855681046344
Iteraction 94 
 X value is 0.005957283032105431 
 Y value is 5.031182341937715
Iteraction 95 
 X value is 0.005599846050179105 
 Y value is 5.031508896139175
Iteraction 96 
 X value is 0.005263855287168359 
 Y value is 5.031835343720398
Iteraction 97 
 X value is 0.0049480239699382575 
 Y value is 5.0321616847509905
Iteraction 98 
 X value is 0.004651142531741962 
 Y value is 5.03248791930049
Iteraction 99 
 X value is 0.0043720739798374444 
 Y value is 5.032814047438366
Iteraction 100 
 X value is 0.004109749541047198 
 Y value is 5.0331400692340225
The Local minimum occurs at 0.004109749541047198 5.0331400692340225
    
    """
x_o=2
eta=0.01
eps=0.000001
del_x=1
max_iters=1000
iters=0
y,z=0,0
def deriv(x):
    y=x**3
    z=4*y+6*x
    ans=x-z
    return ans
while abs(del_x)>eps and iters < max_iters:
    prev_x = x_o
    del_x=-eta*deriv(prev_x)
    x_o=x_o-del_x
    iters+=1
    print("Iteration",iters,"\n X value is",x_o)

print("The local minimun occurs at",x_o)

"""OUTPUT:
Iteration 1 
 X value is 1.58
Iteration 2 
 X value is 1.3432275200000001
Iteration 3 
 X value is 1.1791248674305674
Iteration 4 
 X value is 1.0545934597912563
Iteration 5 
 X value is 0.954948409610474
Iteration 6 
 X value is 0.872367280031941
Iteration 7 
 X value is 0.802193195129812
Iteration 8 
 X value is 0.7414346357953037
Iteration 9 
 X value is 0.6880594883336759
Iteration 10 
 X value is 0.6406267077313174
Iteration 11 
 X value is 0.5980787782323297
Iteration 12 
 X value is 0.5596175706260311
Iteration 13 
 X value is 0.5246264338510184
Iteration 14 
 X value is 0.49261933406917524
Iteration 15 
 X value is 0.4632065349721099
Iteration 16 
 X value is 0.4360707790096937
Iteration 17 
 X value is 0.4109503509802938
Iteration 18 
 X value is 0.3876267784811559
Iteration 19 
 X value is 0.36591573254487486
Iteration 20 
 X value is 0.3456601843415252
Iteration 21 
 X value is 0.32672518265607414
Iteration 22 
 X value is 0.30899381555376865
Iteration 23 
 X value is 0.2923640504743153
Iteration 24 
 X value is 0.27674623493676503
Iteration 25 
 X value is 0.2620611002667783
Iteration 26 
 X value is 0.2482381527160516
Iteration 27 
 X value is 0.23521436603046147
Iteration 28 
 X value is 0.2229331108289917
Iteration 29 
 X value is 0.21134327164761574
Iteration 30 
 X value is 0.2003985139043812
Iteration 31 
 X value is 0.19005667152836958
Iteration 32 
 X value is 0.18027923237765703
Iteration 33 
 X value is 0.1710309034182514
Iteration 34 
 X value is 0.16227924135011823
Iteration 35 
 X value is 0.15399433723669403
Iteration 36 
 X value is 0.1461485459300381
Iteration 37 
 X value is 0.13871625283820527
Iteration 38 
 X value is 0.13167367196773067
Iteration 39 
 X value is 0.12499867027668891
Iteration 40 
 X value is 0.11867061425605915
Iteration 41 
 X value is 0.11267023536715991
Iteration 42 
 X value is 0.10697951153740962
Iteration 43 
 X value is 0.10158156238383853
Iteration 44 
 X value is 0.09646055621547013
Iteration 45 
 X value is 0.09160162717892867
Iteration 46 
 X value is 0.08699080116976005
Iteration 47 
 X value is 0.08261492934550219
Iteration 48 
 X value is 0.07846162825385675
Iteration 49 
 X value is 0.07451922573705137
Iteration 50 
 X value is 0.07077671189697639
Iteration 51 
 X value is 0.06722369450922559
Iteration 52 
 X value is 0.0638503583612429
Iteration 53 
 X value is 0.060647428063197756
Iteration 54 
 X value is 0.05760613394228515
Iteration 55 
 X value is 0.054718180683757014
Iteration 56 
 X value is 0.05197571842669023
Iteration 57 
 X value is 0.04937131606056212
Iteration 58 
 X value is 0.046897936501194205
Iteration 59 
 X value is 0.044548913752417645
Iteration 60 
 X value is 0.04231793158364085
Iteration 61 
 X value is 0.04019900367397003
Iteration 62 
 X value is 0.03818645509115907
Iteration 63 
 X value is 0.036274904988872946
Iteration 64 
 X value is 0.03445925041890012
Iteration 65 
 X value is 0.0327346511663459
Iteration 66 
 X value is 0.0310965155257379
Iteration 67 
 X value is 0.029540486944591896
Iteration 68 
 X value is 0.02806243146850528
Iteration 69 
 X value is 0.026658425928421492
Iteration 70 
 X value is 0.025324746816474272
Iteration 71 
 X value is 0.02405785980188792
Iteration 72 
 X value is 0.02285440984287473
Iteration 73 
 X value is 0.021711211854415286
Iteration 74 
 X value is 0.020625241895301114
Iteration 75 
 X value is 0.01959362884092229
Iteration 76 
 X value is 0.01861364651104605
Iteration 77 
 X value is 0.017682706224300352
Iteration 78 
 X value is 0.016798349753286344
Iteration 79 
 X value is 0.015958242656228413
Iteration 80 
 X value is 0.015160167962857648
Iteration 81 
 X value is 0.014402020193838615
Iteration 82 
 X value is 0.013681799694510744
Iteration 83 
 X value is 0.012997607265042711
Iteration 84 
 X value is 0.01234763907030631
Iteration 85 
 X value is 0.011730181813879123
Iteration 86 
 X value is 0.011143608161594484
Iteration 87 
 X value is 0.010586372400983025
Iteration 88 
 X value is 0.010057006323801392
Iteration 89 
 X value is 0.009554115319628362
Iteration 90 
 X value is 0.00907637466923324
Iteration 91 
 X value is 0.008622526027092235
Iteration 92 
 X value is 0.00819137408305051
Iteration 93 
 X value is 0.007781783393705594
Iteration 94 
 X value is 0.007392675374625748
Iteration 95 
 X value is 0.007023025445018414
Iteration 96 
 X value is 0.006671860316932045
Iteration 97 
 X value is 0.006338255421512538
Iteration 98 
 X value is 0.006021332465245361
Iteration 99 
 X value is 0.005720257109498802
Iteration 100 
 X value is 0.005434236767044431
Iteration 101 
 X value is 0.0051625185095697515
Iteration 102 
 X value is 0.004904387080516676
Iteration 103 
 X value is 0.004659163007879465
Iteration 104 
 X value is 0.004426200811878354
Iteration 105 
 X value is 0.004204887302691528
Iteration 106 
 X value is 0.0039946399636794664
Iteration 107 
 X value is 0.0037949054157729784
Iteration 108 
 X value is 0.003605157958920395
Iteration 109 
 X value is 0.0034248981867012187
Iteration 110 
 X value is 0.0032536516704138488
Iteration 111 
 X value is 0.0030909677091344617
Iteration 112 
 X value is 0.0029364181424234572
Iteration 113 
 X value is 0.0027895962225256174
Iteration 114 
 X value is 0.002650115543070887
Iteration 115 
 X value is 0.00251760902143497
Iteration 116 
 X value is 0.002391727932063214
Iteration 117 
 X value is 0.0022721409881980223
Iteration 118 
 X value is 0.002158533469579676
Iteration 119 
 X value is 0.0020506063938133643
Iteration 120 
 X value is 0.0019480757292118013
Iteration 121 
 X value is 0.0018506716470333897
Iteration 122 
 X value is 0.0017581378111407747
Iteration 123 
 X value is 0.0016702307032041618
Iteration 124 
 X value is 0.001586718981668214
Iteration 125 
 X value is 0.0015073828727909598
Iteration 126 
 X value is 0.0014320135921482087
Iteration 127 
 X value is 0.0013604127950777108
Iteration 128 
 X value is 0.0012923920546139367
Iteration 129 
 X value is 0.0012277723655371195
Iteration 130 
 X value is 0.001166383673229274
Iteration 131 
 X value is 0.0011080644260955028
Iteration 132 
 X value is 0.0010526611503711674
Iteration 133 
 X value is 0.0010000280461946458
Iteration 134 
 X value is 0.0009500266038815478
Iteration 135 
 X value is 0.0009025252393895891
Iteration 136 
 X value is 0.0008573989480139671
Iteration 137 
 X value is 0.0008145289754011799
Iteration 138 
 X value is 0.0007738025050149081
Iteration 139 
 X value is 0.0007351123612309639
Iteration 140 
 X value is 0.0006983567272795155
Iteration 141 
 X value is 0.0006634388772919375
Iteration 142 
 X value is 0.0006302669217468054
Iteration 143 
 X value is 0.0005987535656448668
Iteration 144 
 X value is 0.0005688158787763576
Iteration 145 
 X value is 0.0005403750774758905
Iteration 146 
 X value is 0.0005133563172904021
Iteration 147 
 X value is 0.00048768849601439374
Iteration 148 
 X value is 0.0004633040665739994
Iteration 149 
 X value is 0.0004401388592673585
Iteration 150 
 X value is 0.0004181319128934036
Iteration 151 
 X value is 0.00039722531432458146
Iteration 152 
 X value is 0.00037736404610125767
Iteration 153 
 X value is 0.00035849584164667446
Iteration 154 
 X value is 0.0003405710477213958
Iteration 155 
 X value is 0.00032354249375523116
Iteration 156 
 X value is 0.0003073653677127358
Iteration 157 
 X value is 0.00029199709816558406
Iteration 158 
 X value is 0.00027739724226145105
Iteration 159 
 X value is 0.0002635273792945583
Iteration 160 
 X value is 0.0002503510095977863
Iteration 161 
 X value is 0.00023783345849026074
Iteration 162 
 X value is 0.00022594178502762806
Iteration 163 
 X value is 0.00021464469531487634
Iteration 164 
 X value is 0.00020391246015356515
Iteration 165 
 X value is 0.00019371683680673732
Iteration 166 
 X value is 0.0001840309946756221
Iteration 167 
 X value is 0.0001748294446925349
Iteration 168 
 X value is 0.00016608797224415935
Iteration 169 
 X value is 0.00015778357344868848
Iteration 170 
 X value is 0.00014989439461912904
Iteration 171 
 X value is 0.0001423996747534575
Iteration 172 
 X value is 0.0001352796909002833
Iteration 173 
 X value is 0.00012851570625624118
Iteration 174 
 X value is 0.00012208992085852502
Iteration 175 
 X value is 0.00011598542474280411
Iteration 176 
 X value is 0.0001101861534432516
Iteration 177 
 X value is 0.00010467684571757827
Iteration 178 
 X value is 9.944300338582057e-05
Iteration 179 
 X value is 9.447085317719423e-05
Iteration 180 
 X value is 8.97473104846094e-05
Iteration 181 
 X value is 8.525994493146385e-05
Iteration 182 
 X value is 8.09969476600996e-05
Iteration 183 
 X value is 7.694710025583938e-05
Iteration 184 
 X value is 7.30997452248237e-05
Iteration 185 
 X value is 6.944475794795797e-05
Iteration 186 
 X value is 6.597252003716398e-05
Iteration 187 
 X value is 6.26738940238203e-05
Iteration 188 
 X value is 5.954019931278191e-05
Iteration 189 
 X value is 5.656318933869993e-05
Iteration 190 
 X value is 5.3735029864526216e-05
Iteration 191 
 X value is 5.104827836509361e-05
Iteration 192 
 X value is 4.849586444151781e-05
Iteration 193 
 X value is 4.607107121487972e-05
Iteration 194 
 X value is 4.3767517650224216e-05
Iteration 195 
 X value is 4.157914176435937e-05
Iteration 196 
 X value is 3.950018467326608e-05
Iteration 197 
 X value is 3.7525175437137545e-05
Iteration 198 
 X value is 3.5648916663167045e-05
Iteration 199 
 X value is 3.386647082819652e-05
Iteration 200 
 X value is 3.2173147285232986e-05
Iteration 201 
 X value is 3.056448991963923e-05
Iteration 202 
 X value is 2.9036265422515148e-05
Iteration 203 
 X value is 2.7584452150410167e-05
Iteration 204 
 X value is 2.6205229542050095e-05
Iteration 205 
 X value is 2.489496806422777e-05
Iteration 206 
 X value is 2.3650219660399227e-05
Iteration 207 
 X value is 2.246770867685013e-05
Iteration 208 
 X value is 2.1344323242553957e-05
Iteration 209 
 X value is 2.0277107080037297e-05
Iteration 210 
 X value is 1.9263251725701947e-05
Iteration 211 
 X value is 1.8300089139130926e-05

print("The local minimun occurs at",x_o)
The local minimun occurs at 1.8300089139130926e-05
"""
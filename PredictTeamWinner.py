import yaml as y
import os
import numpy as np
from sklearn.svm import SVC
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
import random
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(7)

mypath = "./odis/"

# my_Set = ("1022353.yaml", "1022361.yaml", "1022361.yaml", "1022367.yaml", "1022375.yaml", "1030219.yaml", "1030221.yaml", "1030227.yaml", "238188.yaml", "238189.yaml", "238190.yaml", "238193.yaml", "238194.yaml", "244510.yaml", "256607.yaml", "256612.yaml", "256665.yaml", "256665.yaml", "267708.yaml", "267709.yaml", "267710.yaml", "267710.yaml", "267712.yaml", "267712.yaml", "267713.yaml", "267713.yaml", "267715.yaml", "267715.yaml", "291366.yaml", "291366.yaml", "291369.yaml", "291369.yaml", "293076.yaml", "293077.yaml", "297795.yaml", "297796.yaml", "297797.yaml", "297798.yaml", "297799.yaml", "297801.yaml", "297802.yaml", "297803.yaml", "297804.yaml", "297805.yaml", "335356.yaml", "335356.yaml", "335358.yaml", "335358.yaml", "343732.yaml", "343732.yaml", "343733.yaml", "343733.yaml", "343734.yaml", "343734.yaml", "343736.yaml", "343736.yaml", "345471.yaml", "361043.yaml", "361044.yaml", "361045.yaml", "361046.yaml", "361047.yaml", "366341.yaml", "366341.yaml", "386530.yaml", "386530.yaml", "386531.yaml", "386531.yaml", "386533.yaml", "386534.yaml", "386534.yaml", "403381.yaml", "403381.yaml", "403382.yaml", "403383.yaml", "403383.yaml", "415278.yaml", "415284.yaml", "416236.yaml", "416237.yaml", "416238.yaml", "416239.yaml", "416240.yaml", "416241.yaml", "430886.yaml", "430886.yaml", "430887.yaml", "430887.yaml", "430888.yaml", "430888.yaml", "430889.yaml", "430889.yaml", "430890.yaml", "430890.yaml", "433568.yaml", "433578.yaml", "433582.yaml", "433586.yaml", "433599.yaml", "433601.yaml", "433605.yaml", "433606.yaml", "433606.yaml", "434264.yaml", "434264.yaml", "441827.yaml", "441828.yaml", "441829.yaml", "452147.yaml", "452147.yaml", "452150.yaml", "452150.yaml", "455234.yaml", "455236.yaml", "455236.yaml", "455237.yaml", "455237.yaml", "456662.yaml", "456663.yaml", "456663.yaml", "456665.yaml", "456666.yaml", "456666.yaml", "456668.yaml", "456668.yaml", "464529.yaml", "467884.yaml", "467885.yaml", "467886.yaml", "467887.yaml", "518960.yaml", "518960.yaml", "518963.yaml", "518963.yaml", "518966.yaml", "518966.yaml", "521218.yaml", "521219.yaml", "521220.yaml", "521221.yaml", "521222.yaml", "535795.yaml", "535795.yaml", "535798.yaml", "536929.yaml", "536930.yaml", "536931.yaml", "536932.yaml", "536933.yaml", "564781.yaml", "564781.yaml", "564782.yaml", "564782.yaml", "564783.yaml", "564783.yaml", "564784.yaml", "564784.yaml", "564785.yaml", "564785.yaml", "565812.yaml", "565813.yaml", "565814.yaml", "565815.yaml", "565816.yaml", "566947.yaml", "566947.yaml", "578614.yaml", "578619.yaml", "578623.yaml", "589308.yaml", "589309.yaml", "589310.yaml", "597925.yaml", "597925.yaml", "597928.yaml", "597928.yaml", "597929.yaml", "597929.yaml", "647249.yaml", "647251.yaml", "647261.yaml", "656405.yaml", "656423.yaml", "656439.yaml", "656453.yaml", "656465.yaml", "656475.yaml", "676529.yaml", "676531.yaml", "676533.yaml", "710297.yaml", "710297.yaml", "710301.yaml", "770121.yaml", "792289.yaml", "792291.yaml", "792291.yaml", "792293.yaml", "792293.yaml", "792295.yaml", "792295.yaml", "792297.yaml", "903595.yaml", "903597.yaml", "903599.yaml", "903601.yaml")
#
# m = ("467883.yaml", "345469.yaml", "792297.yaml", "903593.yaml", "293078.yaml", "297793.yaml", "297794.yaml", "434259.yaml", "434259.yaml", "434262.yaml", "434262.yaml", "1034819.yaml", "1034821.yaml", "1034823.yaml", "249753.yaml", "249756.yaml", "647253.yaml", "647255.yaml", "647259.yaml", "386532.yaml", "386532.yaml", "386533.yaml", "244511.yaml", "247476.yaml", "247476.yaml", "249745.yaml", "291360.yaml", "291360.yaml", "518957.yaml", "518957.yaml", "1030223.yaml", "1030225.yaml", "770123.yaml", "770127.yaml", "792289.yaml")

# my_Set = list(my_Set)
# random.shuffle(my_Set)
#
# m = my_Set[:35]
# my_Set = my_Set[35:]

team1 = input('Country as India/Australia/England')#"India"#input('Enter Country 1')
team2 = input('Country as Sri Lanka/Australia/England')#"Sri Lanka"#input('Enter Country 2')

# player1 = "V Kohli"
# player2 = "MS Dhoni"

c1= 0
c2 = 0
total = 0
no_outcome = 0



india_win = []
toss_winner = []
batfirst_decision = []
runs_gte300 = []
runs_250to299 = []
runs_200to249 = []
runs_lt200 = []
wickets0   = []
wickets1t4 = []
wickets5t7 = []
wicketsgte8 = []

c = 0
d = {}
match_winner = ""

def classify(team_total, wickets):
    if wickets >= 8:
        wicketsgte8.append(1)
        wickets5t7.append(0)
        wickets1t4.append(0)
        wickets0.append(0)
    elif wickets >=5 and wickets < 8:
        wicketsgte8.append(0)
        wickets5t7.append(1)
        wickets1t4.append(0)
        wickets0.append(0)
    elif wickets >= 1 and wickets < 5:
        wicketsgte8.append(0)
        wickets5t7.append(0)
        wickets1t4.append(1)
        wickets0.append(0)
    else:
        wicketsgte8.append(0)
        wickets5t7.append(0)
        wickets1t4.append(0)
        wickets0.append(1)

    if team_total >= 300:
        runs_gte300.append(1)
        runs_250to299.append(0)
        runs_200to249.append(0)
        runs_lt200.append(0)
    elif team_total >= 250 and team_total < 300:
        runs_250to299.append(1)
        runs_gte300.append(0)
        runs_200to249.append(0)
        runs_lt200.append(0)

    elif team_total >= 200 and team_total < 250:
        runs_200to249.append(1)
        runs_gte300.append(0)
        runs_250to299.append(0)
        runs_lt200.append(0)
    else:
        runs_lt200.append(1)
        runs_200to249.append(0)
        runs_gte300.append(0)
        runs_250to299.append(0)

my_Set = []
for root,dirs,files in os.walk(mypath):
    for file in files:
        if file.endswith(".yaml"):
            my_Set.append(file)


m = []
if team1 == 'India':
    my_Set = ("1022353.yaml", "1022361.yaml", "1022361.yaml", "1022367.yaml", "1022375.yaml", "1030219.yaml", "1030221.yaml", "1030227.yaml", "238188.yaml", "238189.yaml", "238190.yaml", "238193.yaml", "238194.yaml", "244510.yaml", "256607.yaml", "256612.yaml", "256665.yaml", "256665.yaml", "267708.yaml", "267709.yaml", "267710.yaml", "267710.yaml", "267712.yaml", "267712.yaml", "267713.yaml", "267713.yaml", "267715.yaml", "267715.yaml", "291366.yaml", "291366.yaml", "291369.yaml", "291369.yaml", "293076.yaml", "293077.yaml", "297795.yaml", "297796.yaml", "297797.yaml", "297798.yaml", "297799.yaml", "297801.yaml", "297802.yaml", "297803.yaml", "297804.yaml", "297805.yaml", "335356.yaml", "335356.yaml", "335358.yaml", "335358.yaml", "343732.yaml", "343732.yaml", "343733.yaml", "343733.yaml", "343734.yaml", "343734.yaml", "343736.yaml", "343736.yaml", "345471.yaml", "361043.yaml", "361044.yaml", "361045.yaml", "361046.yaml", "361047.yaml", "366341.yaml", "366341.yaml", "386530.yaml", "386530.yaml", "386531.yaml", "386531.yaml", "386533.yaml", "386534.yaml", "386534.yaml", "403381.yaml", "403381.yaml", "403382.yaml", "403383.yaml", "403383.yaml", "415278.yaml", "415284.yaml", "416236.yaml", "416237.yaml", "416238.yaml", "416239.yaml", "416240.yaml", "416241.yaml", "430886.yaml", "430886.yaml", "430887.yaml", "430887.yaml", "430888.yaml", "430888.yaml", "430889.yaml", "430889.yaml", "430890.yaml", "430890.yaml", "433568.yaml", "433578.yaml", "433582.yaml", "433586.yaml", "433599.yaml", "433601.yaml", "433605.yaml", "433606.yaml", "433606.yaml", "434264.yaml", "434264.yaml", "441827.yaml", "441828.yaml", "441829.yaml", "452147.yaml", "452147.yaml", "452150.yaml", "452150.yaml", "455234.yaml", "455236.yaml", "455236.yaml", "455237.yaml", "455237.yaml", "456662.yaml", "456663.yaml", "456663.yaml", "456665.yaml", "456666.yaml", "456666.yaml", "456668.yaml", "456668.yaml", "464529.yaml", "467884.yaml", "467885.yaml", "467886.yaml", "467887.yaml", "518960.yaml", "518960.yaml", "518963.yaml", "518963.yaml", "518966.yaml", "518966.yaml", "521218.yaml", "521219.yaml", "521220.yaml", "521221.yaml", "521222.yaml", "535795.yaml", "535795.yaml", "535798.yaml", "536929.yaml", "536930.yaml", "536931.yaml", "536932.yaml", "536933.yaml", "564781.yaml", "564781.yaml", "564782.yaml", "564782.yaml", "564783.yaml", "564783.yaml", "564784.yaml", "564784.yaml", "564785.yaml", "564785.yaml", "565812.yaml", "565813.yaml", "565814.yaml", "565815.yaml", "565816.yaml", "566947.yaml", "566947.yaml", "578614.yaml", "578619.yaml", "578623.yaml", "589308.yaml", "589309.yaml", "589310.yaml", "597925.yaml", "597925.yaml", "597928.yaml", "597928.yaml", "597929.yaml", "597929.yaml", "647249.yaml", "647251.yaml", "647261.yaml", "656405.yaml", "656423.yaml", "656439.yaml", "656453.yaml", "656465.yaml", "656475.yaml", "676529.yaml", "676531.yaml", "676533.yaml", "710297.yaml", "710297.yaml", "710301.yaml", "770121.yaml", "792289.yaml", "792291.yaml", "792291.yaml", "792293.yaml", "792293.yaml", "792295.yaml", "792295.yaml", "792297.yaml", "903595.yaml", "903597.yaml", "903599.yaml", "903601.yaml")

    m = ("467883.yaml", "345469.yaml", "792297.yaml", "903593.yaml", "293078.yaml", "297793.yaml", "297794.yaml", "434259.yaml", "434259.yaml", "434262.yaml", "434262.yaml", "1034819.yaml", "1034821.yaml", "1034823.yaml", "249753.yaml", "249756.yaml", "647253.yaml", "647255.yaml", "647259.yaml", "386532.yaml", "386532.yaml", "386533.yaml", "244511.yaml", "247476.yaml", "247476.yaml", "249745.yaml", "291360.yaml", "291360.yaml", "518957.yaml", "518957.yaml", "1030223.yaml", "1030225.yaml", "770123.yaml", "770127.yaml", "792289.yaml")
elif team1 == 'Australia':
    my_Set = ("1000887.yaml","1000889.yaml","1000891.yaml","1000893.yaml","1000895.yaml","1001371.yaml","1001373.yaml","1001375.yaml","1022349.yaml","1022355.yaml","226375.yaml","226376.yaml","226377.yaml","226378.yaml","226380.yaml","226381.yaml","226382.yaml","236358.yaml","236595.yaml","236963.yaml","247458.yaml","247466.yaml","247478.yaml","247485.yaml","247491.yaml","247496.yaml","247499.yaml","247503.yaml","247506.yaml","247507.yaml","249228.yaml","249229.yaml","249230.yaml","249231.yaml","249232.yaml","249233.yaml","249234.yaml","249235.yaml","249240.yaml","249241.yaml","249748.yaml","249750.yaml","249757.yaml","249759.yaml","256608.yaml","256610.yaml","256614.yaml","256615.yaml","291345.yaml","291346.yaml","291347.yaml","291359.yaml","291361.yaml","291362.yaml","291364.yaml","291365.yaml","291367.yaml","291368.yaml","291370.yaml","291371.yaml","291372.yaml","336201.yaml","336202.yaml","336204.yaml","351684.yaml","351685.yaml","351686.yaml","351687.yaml","351688.yaml","351689.yaml","351690.yaml","351691.yaml","351692.yaml","351693.yaml","392616.yaml","392617.yaml","392618.yaml","392619.yaml","392620.yaml","406192.yaml","406193.yaml","406194.yaml","406195.yaml","406196.yaml","406202.yaml","406203.yaml","406204.yaml","406205.yaml","406206.yaml","415277.yaml","415281.yaml","415283.yaml","415285.yaml","415287.yaml","433561.yaml","433565.yaml","433577.yaml","433588.yaml","433592.yaml","433596.yaml","446957.yaml","446958.yaml","446959.yaml","446962.yaml","446963.yaml","446964.yaml","446965.yaml","446966.yaml","446967.yaml","446968.yaml","516206.yaml","516207.yaml","516208.yaml","516209.yaml","516210.yaml","518956.yaml","518958.yaml","518959.yaml","518961.yaml","518962.yaml","518964.yaml","518965.yaml","518967.yaml","518968.yaml","518969.yaml","518970.yaml","571145.yaml","571146.yaml","571147.yaml","573014.yaml","573015.yaml","573016.yaml","573017.yaml","573018.yaml","573022.yaml","573023.yaml","573024.yaml","573025.yaml","573026.yaml","578620.yaml","578625.yaml","636159.yaml","636160.yaml","636161.yaml","636162.yaml","636163.yaml","656401.yaml","656449.yaml","656461.yaml","656477.yaml","656487.yaml","656493.yaml","656495.yaml","727919.yaml","727921.yaml","727923.yaml","736445.yaml","736451.yaml","736455.yaml","754723.yaml","754725.yaml","754727.yaml","754729.yaml","754731.yaml","754749.yaml","754751.yaml","754755.yaml","754757.yaml","754761.yaml","895807.yaml","895809.yaml","895811.yaml","895813.yaml","895815.yaml","932853.yaml","932855.yaml","932861.yaml","936133.yaml","995457.yaml","995459.yaml","995461.yaml","995463.yaml","995465.yaml")
elif team1 == 'England':
    my_Set = ("1022347.yaml","1022357.yaml","1022365.yaml","1022371.yaml","1029001.yaml","1029003.yaml","1031425.yaml","1031427.yaml","1031429.yaml","225245.yaml","225246.yaml","225247.yaml","225248.yaml","225249.yaml","225250.yaml","225251.yaml","225252.yaml","225253.yaml","225254.yaml","247463.yaml","247479.yaml","247484.yaml","247489.yaml","247500.yaml","249236.yaml","249237.yaml","249238.yaml","249239.yaml","249755.yaml","258465.yaml","258466.yaml","258467.yaml","258471.yaml","258472.yaml","258473.yaml","258474.yaml","258475.yaml","258476.yaml","258477.yaml","291217.yaml","291218.yaml","291220.yaml","291221.yaml","296904.yaml","296905.yaml","296906.yaml","296907.yaml","296908.yaml","296914.yaml","296915.yaml","296916.yaml","296917.yaml","296918.yaml","350043.yaml","350044.yaml","350045.yaml","350046.yaml","350047.yaml","350048.yaml","350049.yaml","380715.yaml","380716.yaml","415276.yaml","415282.yaml","426387.yaml","426388.yaml","426389.yaml","426390.yaml","426391.yaml","426403.yaml","426404.yaml","426405.yaml","426428.yaml","426429.yaml","426430.yaml","426431.yaml","426432.yaml","433562.yaml","433572.yaml","433579.yaml","433593.yaml","433603.yaml","474467.yaml","474468.yaml","474469.yaml","474470.yaml","474471.yaml","474477.yaml","474478.yaml","474479.yaml","474480.yaml","474481.yaml","531631.yaml","531632.yaml","531633.yaml","531634.yaml","534209.yaml","534210.yaml","534215.yaml","534216.yaml","534218.yaml","534219.yaml","534228.yaml","534229.yaml","534230.yaml","534231.yaml","534232.yaml","566923.yaml","566924.yaml","566925.yaml","566942.yaml","566943.yaml","566944.yaml","566945.yaml","566946.yaml","566948.yaml","578616.yaml","578621.yaml","578624.yaml","656425.yaml","656441.yaml","667723.yaml","667725.yaml","667727.yaml","667729.yaml","667889.yaml","667891.yaml","667893.yaml","667895.yaml","667897.yaml","743943.yaml","743945.yaml","743947.yaml","743949.yaml","743951.yaml","743977.yaml","743979.yaml","743981.yaml","743983.yaml","743985.yaml","750663.yaml","750665.yaml","750667.yaml","750669.yaml","750671.yaml","750673.yaml","750675.yaml","754753.yaml","754759.yaml","902641.yaml","902643.yaml","902645.yaml","902647.yaml","913623.yaml","913625.yaml","913627.yaml","913629.yaml","913631.yaml","913653.yaml","913655.yaml","913657.yaml","913659.yaml","913661.yaml")
random.shuffle(my_Set)

m = my_Set[:35]
my_Set = my_Set[35:]

for root,dirs,files in os.walk(mypath):
    for file in files:
        if file.endswith(".yaml"):# and file in my_Set:
            d = y.load(open(mypath + file))
            teams = d['info']['teams']
            c = c + 1
            print("Reading file ", c)
            s = set(teams)
            if team1 in s:
                for t in s:
                    m.append(t)
                if 'winner' in d['info']['outcome']:
                    match_winner = d['info']['outcome']['winner']
                    if match_winner == team1:
                         india_win.append(1)
                    else:
                         india_win.append(0)
                else:
                    no_outcome = no_outcome + 1
                    continue

                twinner = d['info']['toss']['winner']
                if twinner == team1:
                    toss_winner.append(1)
                    toss = d['info']['toss']['decision']
                    if toss == 'bat':
                        batfirst_decision.append(1)
                    else:
                        batfirst_decision.append(0)
                else:
                    toss_winner.append(0)
                    toss = d['info']['toss']['decision']
                    if toss == 'bat':
                        batfirst_decision.append(0)
                    else:
                        batfirst_decision.append(1)
                total += 1


                team_total = 0
                wickets = 0

                #if india playing in 1st
                if d['innings'][0]['1st innings']['team'] == team1:
                    for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                        new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                        for j in new_dic:
                            team_total = team_total + new_dic[j]['runs']['total']
                            try:
                                if new_dic[j]['wicket']:
                                    wickets = wickets + 1
                            except:
                                pass
                try:
                    for i in range(len(d['innings'][1]['2nd innings']['deliveries'])):
                        new_dic = d['innings'][1]['2nd innings']['deliveries'][i]
                        for j in new_dic:
                            if d['innings'][1]['2nd innings']['team'] == team1:
                                team_total = team_total + new_dic[j]['runs']['total']
                                try:
                                    if new_dic[j]['wicket']:
                                        wickets = wickets + 1
                                except KeyError:
                                     pass

                except IndexError:
                    print("No Second Innings")
                    continue

                classify(team_total,wickets)
            else:
                continue


toss_win = np.array(toss_winner)
batfirst = np.array(batfirst_decision)
gte300 = np.array(runs_gte300)
btw250_299 = np.array(runs_250to299)
btw200_250 = np.array(runs_200to249)
btw1_200 = np.array(runs_lt200)
gte8 = np.array(wicketsgte8); btw5_7 = np.array(wickets5t7); btw1_4 = np.array(wickets1t4); w0 = np.array(wickets0)

features = np.array([toss_win, batfirst, gte300, btw1_200, btw200_250, btw250_299, gte8, btw5_7, btw1_4, w0])
class_label_X = np.array(india_win)

# print(features.shape)
features = features.reshape((features.shape[1], -1))
# print(features.shape)

clf = SVC(gamma='auto')
clf.fit(features, class_label_X)

clf_dt = tree.DecisionTreeClassifier(max_depth=5)
clf_dt.fit(features, class_label_X)

clf_rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
clf_rf.fit(features, class_label_X)

clf_ab = AdaBoostClassifier(tree.DecisionTreeClassifier(max_depth=1),
                         algorithm="SAMME",
                         n_estimators=200)
clf_ab.fit(features, class_label_X)

clf_lin = SGDClassifier()
clf_lin.fit(features, class_label_X)
clf_glb = GaussianNB()
clf_glb.fit(features, class_label_X)

c1= 0
c2 = 0
total = 0
no_outcome = 0


india_win = []
toss_winner = []
batfirst_decision = []
runs_gte300 = []
runs_250to299 = []
runs_200to249 = []
runs_lt200 = []
wickets0   = []
wickets1t4 = []
wickets5t7 = []
wicketsgte8 = []

for root,dirs,files in os.walk(mypath):
    for file in files:
        if file.endswith(".yaml") and file in m:
            d = y.load(open(mypath + file))
            teams = d['info']['teams']
            c = c + 1
            print("Reading file", c)
            s = set(teams)
            if team1 in s:
                if 'winner' in d['info']['outcome']:
                    match_winner = d['info']['outcome']['winner']
                    if match_winner == team1:
                         india_win.append(1)
                    else:
                         india_win.append(0)
                else:
                    no_outcome = no_outcome + 1
                    continue

                twinner = d['info']['toss']['winner']
                if twinner == team1:
                    toss_winner.append(1)
                    toss = d['info']['toss']['decision']
                    if toss == 'bat':
                        batfirst_decision.append(1)
                    else:
                        batfirst_decision.append(0)
                else:
                    toss_winner.append(0)
                    toss = d['info']['toss']['decision']
                    if toss == 'bat':
                        batfirst_decision.append(0)
                    else:
                        batfirst_decision.append(1)
                total += 1

                team_total = 0
                wickets = 0

                #if india playing in 1st
                if d['innings'][0]['1st innings']['team'] == team1:
                    for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                        new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                        for j in new_dic:
                            team_total = team_total + new_dic[j]['runs']['total']
                            try:
                                if new_dic[j]['wicket']:
                                    wickets = wickets + 1
                            except:
                                pass
                try:
                    #If second innings, and india plays second innings
                    for i in range(len(d['innings'][1]['2nd innings']['deliveries'])):
                        new_dic = d['innings'][1]['2nd innings']['deliveries'][i]
                        for j in new_dic:
                            if d['innings'][1]['2nd innings']['team'] == team1:
                                team_total = team_total + new_dic[j]['runs']['total']
                                try:
                                    if new_dic[j]['wicket']:
                                        wickets = wickets + 1
                                except KeyError:
                                     pass

                except IndexError:
                    print("No Second Innings")
                    continue

                classify(team_total,wickets)
            else:
                continue

toss_win = np.array(toss_winner)
batfirst = np.array(batfirst_decision)
gte300 = np.array(runs_gte300)
btw250_299 = np.array(runs_250to299)
btw200_250 = np.array(runs_200to249)
btw1_200 = np.array(runs_lt200)

# features_y = np.array([toss_win, batfirst, gte300, btw1_200, btw200_250, btw250_299])
gte8 = np.array(wicketsgte8); btw5_7 = np.array(wickets5t7); btw1_4 = np.array(wickets1t4); w0 = np.array(wickets0)
features_y = np.array([toss_win, batfirst, gte300, btw1_200, btw200_250, btw250_299, gte8, btw5_7, btw1_4, w0])
class_label_Y = np.array(india_win)


features_y = features_y.reshape((features_y.shape[1], -1))
# print(features_y.shape)
pred = clf.predict(features_y)

# print('Original Lables', class_label_Y)
# print('SVM Predictions', clf.predict(features_y))

pred_dt = clf_dt.predict(features_y)
pred_rf = clf_rf.predict(features_y)
pred_ab = clf_ab.predict(features_y)
pred_ln = clf_lin.predict(features_y)
pred_glb = clf_glb.predict(features_y)

print('Decision Tree Predictions', pred_dt)
print('Random Forest Predictions', pred_rf)
print('Adaboost Predictions', pred_ab)
print('Naive Bayes Classifier', pred_glb)
correct = 0
for i in range(len(class_label_Y)):
    if class_label_Y[i] == pred[i]:
        correct+=1
print("SVM accuracy is {}:".format(correct/len(pred)))

correct = 0
for i in range(len(class_label_Y)):
    if class_label_Y[i] == pred_dt[i]:
        correct+=1
print("Decision Tree accuracy is {}:".format(correct/len(pred_dt)))

correct = 0
for i in range(len(class_label_Y)):
    if class_label_Y[i] == pred_rf[i]:
        correct+=1
print("Random Forest accuracy is {}:".format(correct/len(pred_rf)))

correct = 0
for i in range(len(class_label_Y)):
    if class_label_Y[i] == pred_rf[i]:
        correct+=1
print("Adaboost accuracy is {}:".format(correct/len(pred_ab)))

correct = 0
for i in range(len(class_label_Y)):
    if class_label_Y[i] == pred_ln[i]:
        correct+=1
print("Linear Classifier accuracy is {}:".format(correct/len(pred_ln)))

correct = 0
for i in range(len(class_label_Y)):
    if class_label_Y[i] == pred_ln[i]:
        correct+=1
print("Naive Bayes accuracy is {}:".format(correct/len(pred_glb)))

#
model = Sequential()
model.add(Dense(40, input_dim=10, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(features, class_label_X, epochs=1000, batch_size=10)
pred_NN = model.predict(features_y)
for x in range(len(pred_NN)):
    if x<0.5:
        pred_NN[x] =0
    else:
        pred_NN[x]= 1
correct = 0
for i in range(len(pred_NN)):
    if pred_NN[i] == class_label_Y[i]:
        correct+=1
acc = correct/len(class_label_Y)
print("Accuracy of NN is ", acc)
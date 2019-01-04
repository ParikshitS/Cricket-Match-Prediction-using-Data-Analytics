import yaml as y
import os
import numpy as np
import sklearn
import matplotlib.pyplot as plt

mypath = "C:/CSCourses/CSCI 720 Big Data Analytics/Group Project/temp/"

team1 = 'India'   #input country of batsman
team2 = 'South Africa'     #input country of bowler
# from toss winner and toss decision I will know whose first inngs batting is
# use this in test files
dots, singles, two, threes, fours, fives, sixes, wicket, extra = [], [], [], [], [], [], [], [], []
ball_no = []

def dot():
    dots.append(1);singles.append(0);two.append(0);threes.append(0);fours.append(0);fives.append(0);sixes.append(0)

def one():
    dots.append(0);
    singles.append(1);
    two.append(0);
    threes.append(0);
    fours.append(0);
    fives.append(0);
    sixes.append(0)

def twos():
    dots.append(0);
    singles.append(0);
    two.append(1);
    threes.append(0);
    fours.append(0);
    fives.append(0);
    sixes.append(0)

def three():
    dots.append(0);
    singles.append(0);
    two.append(0);
    threes.append(1);
    fours.append(0);
    fives.append(0);
    sixes.append(0)

def four():
    dots.append(0);
    singles.append(0);
    two.append(0);
    threes.append(0);
    fours.append(1);
    fives.append(0);
    sixes.append(0)

def five():
    dots.append(0);
    singles.append(0);
    two.append(0);
    threes.append(0);
    fours.append(0);
    fives.append(1);
    sixes.append(0)

def six():
    dots.append(0);
    singles.append(0);
    two.append(0);
    threes.append(0);
    fours.append(0);
    fives.append(0);
    sixes.append(1)

options = {0 : dot,
           1 : one,
           2 : twos,
           3 : three,
           4 : four,
           5 : five,
           6 : six,
}

d = {}
match_winner = ""
for root,dirs,files in os.walk(mypath):
    for file in files:
        if file.endswith(".yaml"):
            d = y.load(open(mypath + file))
            teams = d['info']['teams']
            if team1 not in teams and team2 not in teams:
                break
            toss_win = d['info']['toss']['winner']
            toss_dec = d['info']['toss']['decision']
            if toss_win == team1 and toss_dec == 'bat':
                inng1_bat = team1; inng2_bat = team2
            elif toss_win == team2 and toss_dec == 'bat':
                inng1_bat = team2; inng2_bat = team1
            elif toss_win == team1 and toss_dec == 'field':
                inng1_bat = team2; inng2_bat = team1
            else:
                inng1_bat = team1; inng2_bat = team2

            if team1 == inng1_bat: #India's first batting
                """ Check for Dhoni in batsmen and Malinga for bowler.
                if found break."""
                bat_notfound = True
                x = d['innings'][0]['1st innings']['deliveries'][0]
                # print(d['innings'][0]['1st innings']['deliveries'][1])

                for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                    new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                    for j in new_dic:
                        if new_dic[j]['batsman'] == 'V Kohli' and new_dic[j]['bowler'] == 'Imran Tahir':
                            bat_notfound = False
                            break
                if bat_notfound:
                    break
                else:
                    for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                        new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                        for j in new_dic:
                            if new_dic[j]['batsman'] == 'V Kohli' and new_dic[j]['bowler'] == 'Imran Tahir':
                                if new_dic[j]['runs']['extras'] > 0:
                                    extra.append(1)
                                    dots.append(0);
                                    singles.append(0);
                                    two.append(0);
                                    threes.append(0);
                                    fours.append(0);
                                    fives.append(0);
                                    sixes.append(0)
                                else:
                                    extra.append(0)
                                    runs = new_dic[j]['runs']['batsman']
                                    options[runs]()
                                for keys in new_dic:
                                    # print(new_dic[keys])
                                    if 'wicket' in new_dic[keys]:
                                        wicket.append(1)
                                    else:
                                        wicket.append(0)
            else:'''India's 2nd batting'''
            bat_notfound = True
            x = d['innings'][0]['1st innings']['deliveries'][0]
            for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                for j in new_dic:
                    if new_dic[j]['batsman'] == 'V Kohli' and new_dic[j]['bowler'] == 'Imran Tahir':
                        bat_notfound = False
                        break
            if bat_notfound:
                break
            else:
                try:
                    for i in range(len(d['innings'][1]['2nd innings']['deliveries'])):
                        new_dic = d['innings'][1]['2nd innings']['deliveries'][i]
                        for j in new_dic:
                            if new_dic[j]['batsman'] == 'V Kohli' and new_dic[j]['bowler'] == 'Imran Tahir':
                                if new_dic[j]['runs']['extras'] > 0:
                                    extra.append(1)
                                    dots.append(0);singles.append(0);two.append(0);threes.append(0);fours.append(0);fives.append(0);sixes.append(0)
                                else:
                                    print('a')
                                    runs = new_dic[j]['runs']['batsman']
                                    options[runs]()
                                for keys in new_dic:
                                    if 'wicket' in keys:
                                        wicket.append(1)
                                    else:
                                        wicket.append(0)
                except IndexError:
                    print("No Second Innings")
                    continue


features_ = [dots, singles, two, threes, fours, fives, sixes, extra, wicket]

# print(dots);print(singles);print(two);print(threes);print(fours);print(fives);print(sixes);print(wicket);print(extra)

dots = np.array(dots);singles = np.array(singles); two = np.array(two); threes = np.array(threes); fours = np.array(fours);
fives = np.array(fives); sixes = np.array(sixes); wicket = np.array(wicket); extra = np.array(extra)

features = np.array([dots, singles, two, threes, fours, fives, sixes, extra, wicket])
print(features)
print(features.shape)
features = features.reshape((features.shape[1], -1))
print(features.shape)

mypath = "C:/CSCourses/CSCI 720 Big Data Analytics/Group Project/temp_test/"

dots, singles, two, threes, fours, fives, sixes, wicket, extra = [], [], [], [], [], [], [], [], []
ball_no = []

for root,dirs,files in os.walk(mypath):
    for file in files:
        if file.endswith(".yaml"):
            d = y.load(open(mypath + file))
            teams = d['info']['teams']
            if team1 not in teams and team2 not in teams:
                break
            toss_win = d['info']['toss']['winner']
            toss_dec = d['info']['toss']['decision']
            if toss_win == team1 and toss_dec == 'bat':
                inng1_bat = team1; inng2_bat = team2
            elif toss_win == team2 and toss_dec == 'bat':
                inng1_bat = team2; inng2_bat = team1
            elif toss_win == team1 and toss_dec == 'field':
                inng1_bat = team2; inng2_bat = team1
            else:
                inng1_bat = team1; inng2_bat = team2

            if team1 == inng1_bat: #India's first batting
                """ Check for Dhoni in batsmen and Malinga for bowler.
                if found break."""
                bat_notfound = True
                x = d['innings'][0]['1st innings']['deliveries'][0]
                # print(d['innings'][0]['1st innings']['deliveries'][1])

                for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                    new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                    for j in new_dic:
                        if new_dic[j]['batsman'] == 'V Kohli' and new_dic[j]['bowler'] == 'Imran Tahir':
                            bat_notfound = False
                            break
                if bat_notfound:
                    break
                else:
                    for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                        new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                        for j in new_dic:
                            if new_dic[j]['batsman'] == 'V Kohli' and new_dic[j]['bowler'] == 'Imran Tahir':

                                if new_dic[j]['runs']['extras'] > 0:
                                    extra.append(1)
                                    dots.append(0);
                                    singles.append(0);
                                    two.append(0);
                                    threes.append(0);
                                    fours.append(0);
                                    fives.append(0);
                                    sixes.append(0)
                                else:
                                    extra.append(0)
                                    runs = new_dic[j]['runs']['batsman']

                                    options[runs]()
                                for keys in new_dic:
                                    # print(new_dic[keys])
                                    if 'wicket' in new_dic[keys]:
                                        wicket.append(1)
                                    else:
                                        wicket.append(0)
            else:'''India's 2nd batting'''
            bat_notfound = True
            x = d['innings'][0]['1st innings']['deliveries'][0]
            for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                for j in new_dic:
                    if new_dic[j]['batsman'] == 'V Kohli' and new_dic[j]['bowler'] == 'Imran Tahir':
                        bat_notfound = False
                        break
            if bat_notfound:
                break
            else:
                try:
                    for i in range(len(d['innings'][1]['2nd innings']['deliveries'])):
                        new_dic = d['innings'][1]['2nd innings']['deliveries'][i]
                        for j in new_dic:
                            if new_dic[j]['batsman'] == 'V Kohli' and new_dic[j]['bowler'] == 'Imran Tahir':
                                print('dsds')
                                if new_dic[j]['runs']['extras'] > 0:
                                    extra.append(1)
                                    dots.append(0);singles.append(0);two.append(0);threes.append(0);fours.append(0);fives.append(0);sixes.append(0)
                                else:
                                    runs = new_dic[j]['runs']['batsman']
                                    options[runs]()
                                for keys in new_dic:
                                    if 'wicket' in keys:
                                        wicket.append(1)
                                    else:
                                        wicket.append(0)
                except IndexError:
                    print("No Second Innings")
                    continue


# print(dots);print(singles);print(two);print(threes);print(fours);print(fives);print(sixes);print(wicket);print(extra)

# dots = np.array(dots);singles = np.array(singles); two = np.array(two); threes = np.array(threes); fours = np.array(fours);
# fives = np.array(fives); sixes = np.array(sixes); wicket = np.array(wicket); extra = np.array(extra)
#
# Y = np.array([dots, singles, two, threes, fours, fives, sixes, extra, wicket])
# print(Y.shape)
# print(Y)
# print(Y.shape[1], Y.shape[0])
# Y = features.reshape((Y.shape[1], Y.shape[0]))
# print(Y.shape)
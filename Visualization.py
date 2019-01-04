import yaml as y
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import os
mypath = "./odis/"

my_Set = ("1022353.yaml", "1022361.yaml", "1022361.yaml", "1022367.yaml", "1022375.yaml", "1030219.yaml", "1030221.yaml", "1030223.yaml", "1030225.yaml", "1030227.yaml", "1034819.yaml", "1034821.yaml", "1034823.yaml", "238188.yaml", "238189.yaml", "238190.yaml", "238193.yaml", "238194.yaml", "244510.yaml", "244511.yaml", "247476.yaml", "247476.yaml", "249745.yaml", "249753.yaml", "249756.yaml", "256607.yaml", "256612.yaml", "256665.yaml", "256665.yaml", "267708.yaml", "267709.yaml", "267710.yaml", "267710.yaml", "267712.yaml", "267712.yaml", "267713.yaml", "267713.yaml", "267715.yaml", "267715.yaml", "291360.yaml", "291360.yaml", "291366.yaml", "291366.yaml", "291369.yaml", "291369.yaml", "293076.yaml", "293077.yaml", "293078.yaml", "297793.yaml", "297794.yaml", "297795.yaml", "297796.yaml", "297797.yaml", "297798.yaml", "297799.yaml", "297801.yaml", "297802.yaml", "297803.yaml", "297804.yaml", "297805.yaml", "335356.yaml", "335356.yaml", "335358.yaml", "335358.yaml", "343732.yaml", "343732.yaml", "343733.yaml", "343733.yaml", "343734.yaml", "343734.yaml", "343736.yaml", "343736.yaml", "345469.yaml", "345471.yaml", "361043.yaml", "361044.yaml", "361045.yaml", "361046.yaml", "361047.yaml", "366341.yaml", "366341.yaml", "386530.yaml", "386530.yaml", "386531.yaml", "386531.yaml", "386532.yaml", "386532.yaml", "386533.yaml", "386533.yaml", "386534.yaml", "386534.yaml", "403381.yaml", "403381.yaml", "403382.yaml", "403383.yaml", "403383.yaml", "415278.yaml", "415284.yaml", "416236.yaml", "416237.yaml", "416238.yaml", "416239.yaml", "416240.yaml", "416241.yaml", "430886.yaml", "430886.yaml", "430887.yaml", "430887.yaml", "430888.yaml", "430888.yaml", "430889.yaml", "430889.yaml", "430890.yaml", "430890.yaml", "433568.yaml", "433578.yaml", "433582.yaml", "433586.yaml", "433599.yaml", "433601.yaml", "433605.yaml", "433606.yaml", "433606.yaml", "434259.yaml", "434259.yaml", "434262.yaml", "434262.yaml", "434264.yaml", "434264.yaml", "441827.yaml", "441828.yaml", "441829.yaml", "452147.yaml", "452147.yaml", "452150.yaml", "452150.yaml", "455234.yaml", "455236.yaml", "455236.yaml", "455237.yaml", "455237.yaml", "456662.yaml", "456663.yaml", "456663.yaml", "456665.yaml", "456666.yaml", "456666.yaml", "456668.yaml", "456668.yaml", "464529.yaml", "467883.yaml", "467884.yaml", "467885.yaml", "467886.yaml", "467887.yaml", "518957.yaml", "518957.yaml", "518960.yaml", "518960.yaml", "518963.yaml", "518963.yaml", "518966.yaml", "518966.yaml", "521218.yaml", "521219.yaml", "521220.yaml", "521221.yaml", "521222.yaml", "535795.yaml", "535795.yaml", "535798.yaml", "536929.yaml", "536930.yaml", "536931.yaml", "536932.yaml", "536933.yaml", "564781.yaml", "564781.yaml", "564782.yaml", "564782.yaml", "564783.yaml", "564783.yaml", "564784.yaml", "564784.yaml", "564785.yaml", "564785.yaml", "565812.yaml", "565813.yaml", "565814.yaml", "565815.yaml", "565816.yaml", "566947.yaml", "566947.yaml", "578614.yaml", "578619.yaml", "578623.yaml", "589308.yaml", "589309.yaml", "589310.yaml", "597925.yaml", "597925.yaml", "597928.yaml", "597928.yaml", "597929.yaml", "597929.yaml", "647249.yaml", "647251.yaml", "647253.yaml", "647255.yaml", "647259.yaml", "647261.yaml", "656405.yaml", "656423.yaml", "656439.yaml", "656453.yaml", "656465.yaml", "656475.yaml", "676529.yaml", "676531.yaml", "676533.yaml", "710297.yaml", "710297.yaml", "710301.yaml", "770121.yaml", "770123.yaml", "770127.yaml", "792289.yaml", "792289.yaml", "792291.yaml", "792291.yaml", "792293.yaml", "792293.yaml", "792295.yaml", "792295.yaml", "792297.yaml", "792297.yaml", "903593.yaml", "903595.yaml", "903597.yaml", "903599.yaml", "903601.yaml")

my_Set_t20 = ("1034825.yaml", "1034827.yaml", "1034829.yaml", "1041615.yaml", "1041617.yaml", "287862.yaml", "287865.yaml", "287879.yaml", "297800.yaml", "356001.yaml", "356006.yaml", "356014.yaml", "386535.yaml", "412682.yaml", "412699.yaml", "430884.yaml", "430885.yaml", "521217.yaml", "533291.yaml", "533295.yaml", "564786.yaml", "565810.yaml", "565811.yaml", "565820.yaml", "589306.yaml", "589307.yaml", "647247.yaml", "682921.yaml", "682929.yaml", "682963.yaml", "682965.yaml", "903587.yaml", "903589.yaml", "951329.yaml", "951341.yaml", "951353.yaml", "951363.yaml", "951371.yaml", "963697.yaml", "963699.yaml", "963701.yaml", "966751.yaml", "966757.yaml", "966761.yaml")


countries = ("india","australia","south africa","sri lanka","england")
print("Enter these Countries only for Data Visualization")
print("1. India ")
print("2. Australia ")
print("3. South Africa ")
print("4. Sri Lanka ")
print("5. England ")

team1 = input("Enter team1: ")

if team1.lower() not in countries:
    print("Invalid Input")
    exit(-1)

singles = 0
doubles = 0
boundary = 0
six = 0
three= 0
total_runs = 0
year_to_runs = {}
year_to_mathces = {}
type_of_wicket = {}
c1 = 0
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

c = 0
d = {}
match_winner = ""


def runsperyear(year_to_runs, years, team_total):
    # later create a list for matplotlib
    if years not in year_to_runs:
        year_to_runs[years] = [[team_total],1]
    else:
        year_to_runs[years][0].append(team_total)
        year_to_runs[years][1] = year_to_runs[years][1]+ 1


def matchesperyear(year_to_mathces, years,win, loss):
    # year : [W,L,Total]
    if years not in year_to_mathces:
        year_to_mathces[years] = [win,loss,1]
    else:
        year_to_mathces[years][0] = year_to_mathces[years][0] + win
        year_to_mathces[years][1] = year_to_mathces[years][1] + loss
        year_to_mathces[years][2] = year_to_mathces[years][2] + 1

def drawrunspiechart():
    global team1
    labels = 'Sixes', 'Boundaries', 'Three', 'Doubles', 'Singles'
    sizes = [six,boundary,three,doubles,singles]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Type of Runs Scored')
    plt.show()


def drawwicketspiechart():
    global team1
    labels = list(type_of_wicket.keys())
    sizes = []
    for key in type_of_wicket:
        sizes.append(type_of_wicket[key])
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Type of Wickets given')
    plt.show()



for root,dirs,files in os.walk(mypath):
    for file in files:
        if file.endswith(".yaml"):
            d = y.load(open(mypath + file))
            # Add male conditions here
            teams = d['info']['teams']
            years = d['info']['dates'][0].year
            #print(years)
            c = c + 1
            print("Reading Match ",c)
            s = set(teams)
            win = 0
            loss = 0
            if team1 in s:
                if 'winner' in d['info']['outcome']:
                    match_winner = d['info']['outcome']['winner']
                    if match_winner == team1:
                        india_win.append(1)
                        win = 1
                    else:
                        india_win.append(0)
                        loss = 1
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

                if d['innings'][0]['1st innings']['team'] != team1:
                    for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                        new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                        for j in new_dic:
                            try:
                                if new_dic[j]['wicket']:
                                    typewicket = new_dic[j]['wicket']['kind']
                                    if typewicket not in type_of_wicket:
                                        type_of_wicket[typewicket] = 1
                                    else:
                                        type_of_wicket[typewicket] += 1
                            except KeyError:
                                pass
                try:
                    #If second innings, and india plays second innings
                    for i in range(len(d['innings'][1]['2nd innings']['deliveries'])):
                        new_dic = d['innings'][1]['2nd innings']['deliveries'][i]
                        for j in new_dic:
                            if d['innings'][1]['2nd innings']['team'] != team1:
                                try:
                                    if new_dic[j]['wicket']:
                                        typewicket = new_dic[j]['wicket']['kind']
                                        if typewicket not in type_of_wicket:
                                            type_of_wicket[typewicket] = 1
                                        else:
                                            type_of_wicket[typewicket] += 1
                                except:
                                    pass

                except:
                    continue


                #if india playing in 1st
                if d['innings'][0]['1st innings']['team'] == team1:
                    for i in range(len(d['innings'][0]['1st innings']['deliveries'])):
                        new_dic = d['innings'][0]['1st innings']['deliveries'][i]
                        for j in new_dic:
                            team_total = team_total + new_dic[j]['runs']['total']

                            runs_per_ball = new_dic[j]['runs']['batsman']
                            total_runs = total_runs + runs_per_ball
                            if runs_per_ball == 1:
                                singles = singles + 1
                            elif runs_per_ball == 4:
                                boundary = boundary + 4
                            elif runs_per_ball == 3:
                                three = three + 3
                            elif runs_per_ball == 2:
                                doubles = doubles + 2
                            elif runs_per_ball == 6:
                                six = six + 6
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
                                runs_per_ball = new_dic[j]['runs']['batsman']
                                total_runs = total_runs + runs_per_ball
                                if runs_per_ball == 1:
                                    singles = singles + 1
                                elif runs_per_ball == 4:
                                    boundary = boundary + 4
                                elif runs_per_ball == 3:
                                    three = three + 3
                                elif runs_per_ball == 2:
                                    doubles = doubles + 2
                                elif runs_per_ball == 6:
                                    six = six + 6
                                try:
                                    if new_dic[j]['wicket']:
                                        wickets = wickets + 1
                                except KeyError:
                                     pass

                except IndexError:
                    #print("No Second Innings")
                    pass
                runsperyear(year_to_runs,years,team_total)
                matchesperyear(year_to_mathces,years,win,loss)
            else:
                continue

def drawyeartoruns(year_to_runs):
    global team1
    objects = []
    performance = []

    for key in sorted(year_to_runs):
        objects.append(key)
        performance.append(sum(year_to_runs[key][0])/year_to_runs[key][1])

    #print(objects)
    #print(performance)
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Runs Per Match ')
    plt.xlabel('Years')
    plt.title('Runs per match over the years')
    plt.show()


def drawyeartomatches(year_to_mathces):
    global team1
    N = len(list(year_to_mathces.keys()))
    wins = []
    losses = []
    yea = []
    for key in sorted(year_to_mathces):
        yea.append(key)
        wins.append(year_to_mathces[key][0])
        losses.append(year_to_mathces[key][1])

    ind = np.arange(N)    # the x locations for the groups
    width = 0.50       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, wins, width, color='#d62728')
    p2 = plt.bar(ind, losses, width,
                 bottom=wins)

    plt.ylabel('Total Matches Per Year ')
    plt.xlabel('Years')

    plt.title('Wins/Loses by year')

    plt.xticks(ind, yea)
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Wins', 'Losses'))

    plt.show()

drawyeartomatches(year_to_mathces)
drawyeartoruns(year_to_runs)
drawrunspiechart()
drawwicketspiechart()

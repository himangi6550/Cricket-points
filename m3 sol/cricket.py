p1={ 'name' : 'Virat Kohli' , 'role' : 'bat' , 'runs' :112, '4' :10, '6' :0,
'balls' :119, 'field' :0}
p2={ 'name' : 'du Plessis' , 'role' : 'bat' , 'runs' :120, '4' :11, '6' :2,
'balls' :112, 'field' :0}
p3={ 'name' : 'Bhuvneshwar Kumar' , 'role' : 'bowl' , 'wkts' :1, 'overs' :10,
'runs' :71, 'field' :1}
p4={ 'name' : 'Yuzvendra Chahal' , 'role' : 'bowl' , 'wkts' :2, 'overs' :10,
'runs' :45, 'field' :0}
p5={ 'name' : 'Kuldeep Yadav' , 'role' : 'bowl' , 'wkts' :3, 'overs' :10, 'runs' :34,
'field' :0}
max=0
import points
for i in [p1,p2,p3,p4,p5]:
    if(i['role']=='bat'):
        bat=points.batting_points(i['runs'],i['balls'],i['field'],i['4'],i['6'])
        print("'Name' : '{:s}' , 'batscore' : {}".format(i['name'],bat))
        if bat>max:
            max=bat
            nm=i['name']
    else:
        bowl=points.bowling_points(i['wkts'],i['runs'],i['overs'])
        print("'Name' : '{:s}' , 'bowlscore' : {}".format(i['name'],bowl))
        if bowl>max:
            max=bowl
            nm=i['name']

print(" Man of the match: '{}' , score: {}  ".format(nm,max))

    

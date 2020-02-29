import re

beatList = []
mapList = []
with open("YMCA-Beats.txt",'r') as f:
    beatList = f.readlines()
with open("YMCA_Beatmap_final.txt",'r') as f:
    mapList = f.readlines()
with open("YMCA-Beatmap.txt",'w') as f:
    f.write(mapList[0])
    for s in mapList[1:]:
        beatNumber = float(re.search(r'(.+?),',s).group(1))
        time = float(beatList[int(beatNumber)-1])
        if(beatNumber!=int(beatNumber)):
            time+=float(beatList[int(beatNumber)])
            time/=2
        f.write(str(time)+re.search(r'(,.+)',s).group(1)+"\n")
        
    #= beatList[int(re.search(r'(.+?),',mapList[1]).group(1))]-1

#print(beatList[int(re.search(r'(.+?),',mapList[1]).group(1))]-1)
#output = open("YMCA-Beatmap.csv",'w')

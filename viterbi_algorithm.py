#happy is 0 sad is 1
given = [0, 0, 1, 1, 1, 0]

#happy if sunny 0.8
#sad if sunny 0.2
sunny = [0.8, 0.2]

#happy if rainy 0.4
#sad if rainy 0.6
rainy = [0.4, 0.6]

#sunny -> sunny 0.8
#sunny -> rainy 0.2
tran_sunny = [0.8, 0.2]

#rainy -> sunny 0.4
#rainy -> rainy 0.6
tran_rainy = [0.4, 0.6]

#sunny probability 2/3
#rainy probability 1/3
init = [2.0/3.0, 1.0/3.0]

#sunny is 0 rainy is 1
prediction = [[[init[0]*sunny[given[0]], None], [init[1]*rainy[given[0]], None]]]

for i in range(1, len(given)):
    sun_sun = prediction[i-1][0][0]*tran_sunny[0]*sunny[given[i]]
    rain_sun = prediction[i-1][1][0]*tran_rainy[1]*sunny[given[i]]
    if sun_sun > rain_sun:
        t1 = [sun_sun, 0]
    else:
        t1 = [rain_sun, 1]
    sun_rain = prediction[i-1][0][0]*tran_sunny[1]*rainy[given[i]]
    rain_rain = prediction[i-1][1][0]*tran_rainy[1]*rainy[given[i]]
    if sun_rain > rain_rain:
        t2 = [sun_rain, 0]
    else:
        t2 = [rain_rain, 1]
    prediction.append([t1,t2])
    if t1 > t2:
        head = 0
    else:
        head = 1
        
print prediction

temp_head = head
print head
for i in range(len(prediction)-1, -1, -1):
    print prediction[i][temp_head][0], prediction[i][temp_head][1]
    temp_head = prediction[i][temp_head][1]

# n = 2, t = 4000
# 1000 500
# 1500 1000
# 0 500 1000 1500   2000 2500   3000 3500 4000
#       1->  1<-2->      2<-1-> 1<-  

n, t = map(int,input().split(" "))
toilets = [0]*t
max = 0

for _ in range(n):
    capacity, release = map(int,input().split(" "))
    
    time = capacity
    # find sekunder gæst er på toilet og så sig toilets[i] += 1
    while time < t:
        #end = t % release
        # og: (time, time + release)
        # new: (time, t % (time + release))
        end = time + release
        if end > t - time:
            end = t - time
        for i in range (time, end):
            toilets[i] += 1
            if toilets[i] > max:
                max = toilets[i]
        time += release + capacity

print(max)
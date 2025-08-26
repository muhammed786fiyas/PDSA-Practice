def merge(intervals):
    intervals.sort() #sorting based on first element
    prev=intervals[0]
    l=[]
    for i in range(1,len(intervals)):
        if prev[1]>=intervals[i][0]:  
            prev[1]=max(prev[1],intervals[i][1])
        else:
            l.append(prev)
            prev=intervals[i]
    l.append(prev)
    return l
            
intervals=[[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
          

            

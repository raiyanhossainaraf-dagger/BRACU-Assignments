import sys

input = sys.stdin.readline

N = int(input())

train_record=[]

def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

for i in range(N):

    raw_input=input().strip()
    arr=raw_input.split()
    train_name=arr[0]
    destination=arr[-3]
    departure_time=arr[-1]

    time_in_minutes=time_to_minutes(departure_time)

    train_record.append([train_name, destination, time_in_minutes, raw_input, i]) 
   
   
for i in range(1,N):

    key=train_record[i]
    j=i-1

    def previous_key(x,y):

        if x[0]<y[0]:

            return True
        
        if x[0]>y[0]:

            return False
        
        if x[2]>y[2]:
            return True
        
        if x[2]<y[2]:

            return False

        return False
    
    while j>=0 and previous_key(key,train_record[j]):

        train_record[j+1]=train_record[j]
        j-=1

    train_record[j+1]=key

for record in train_record:

    print(record[3])
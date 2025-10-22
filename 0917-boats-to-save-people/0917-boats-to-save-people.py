class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        boat_count=0
        start=0
        end=len(people)-1
        
        # print(people)
        people.sort()
        # print(people)
        boat_sum=0
        while start<=end:
            boat_sum+=people[start]+people[end]
            if boat_sum<=limit:
                start+=1
                end-=1
            else:
                end-=1
            boat_count+=1
            #because the weight of the earlier person should not be added in the current boat weight
            boat_sum=0
        return boat_count
            
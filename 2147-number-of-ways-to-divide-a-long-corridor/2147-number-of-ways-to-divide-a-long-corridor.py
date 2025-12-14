class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        total_seats = corridor.count('S')
        # If total seats is 0 or odd, no valid division
        if total_seats == 0 or total_seats % 2 != 0:
            return 0
        
        seat_count = 0
        plant_count = 0
        ways = 1
        
        for ch in corridor:
            if ch == 'S':
                seat_count += 1
                # When we encounter the first seat of the next section
                if seat_count > 2 and seat_count % 2 == 1:
                    ways = (ways * (plant_count + 1)) % MOD
                    plant_count = 0
            else:  # ch == 'P'
                # Count plants only between completed seat pairs
                if seat_count >= 2 and seat_count % 2 == 0:
                    plant_count += 1
        
        return ways

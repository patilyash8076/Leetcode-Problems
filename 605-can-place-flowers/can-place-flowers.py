class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if not n : return True

        count =0
        for i in range(0, len(flowerbed)):
            if flowerbed[i]==0:
                if i==0:
                    if len(flowerbed)>1:
                        if flowerbed[i+1]==0:
                            flowerbed[i] = 1
                            count += 1
                    else:
                        flowerbed[i] = 1
                        count += 1

                elif i == len(flowerbed)-1:
                    # last element check
                    if flowerbed[i-1]==0:
                            flowerbed[i] = 1
                            count += 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count+=1
            if count == n:
                return True
        
        return False
            

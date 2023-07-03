#I saw several solution on web, studied and in the end came out with this.
#further explanations are in remarks below.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [ [1] * x for x in range(1,numRows+1)]
        #sort of creating empty (1) triangle of desired length

        
        for row in range(2, len(pascalTriangle)):
            for col in range(1, row):
                pascalTriangle[row][col] = pascalTriangle[row-1][col] + pascalTriangle[row-1][col-1]
                #applying math fundam,entals to derive the value of the element
        return pascalTriangle
            
        

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor != newColor:
            self.fill(image, sr, sc, newColor, oldColor)
            
        return image
    
    def fill(self, image, sr, sc, newColor, oldColor):
        if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == oldColor:
            image[sr][sc] = newColor
            
            self.fill(image, sr + 1, sc, newColor, oldColor)
            self.fill(image, sr - 1, sc, newColor, oldColor)
            self.fill(image, sr, sc + 1, newColor, oldColor)
            self.fill(image, sr, sc - 1, newColor, oldColor)
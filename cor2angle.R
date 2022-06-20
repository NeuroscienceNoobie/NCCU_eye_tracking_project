# the approaching angle data analysis 
# the function to turn the x y coordinates of two fixations points into "approaching angle"

cor2angle <- function(x1,y1,x2,y2) {
  temp = abs(x1-x2)/(sqrt((x1-x2)**2+(y1-y2)**2))
  theta = rad2deg(acos(temp))
  return(theta)
}
library(boot)
c<-c(5,4)
A<-rbind(c(6,4),c(1,2),c(-1,1),c(0,1))
b<-c(24,6,1,2)

simplex(a=c,A1=A,b1=b,maxi="TRUE")
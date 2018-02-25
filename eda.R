library(dplyr)
library(data.table)
library()

setwd("E:/USA/Projects/dataopen")

uber_2015=fread("uber_trips_2015.csv")
zones=fread("zones.csv")


head(zones)
head(uber_2015)
nta=zones[,c(1,5)]


ifelse(length(unique(uber_2015$pickup_location_id))==length(unique(zones$location_id)),1,0)

file=merge(x=uber_2015,y=nta,by.x="pickup_location_id",by.y="location_id",all.y=T,all.x = F,sort=F)
#length(as.factor(is.na(file)))

write.table(file,"uber_nta_2015.csv")

file=fread()

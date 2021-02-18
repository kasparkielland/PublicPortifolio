# Load data from files ----------------------------------------------------

monday = read.csv("data/220615.csv", header = TRUE)
tuesday = read.csv("data/230615.csv", header = TRUE)
wedensday = read.csv("data/240615.csv", header = TRUE)
thursday = read.csv("data/250615.csv", header = TRUE)
friday = read.csv("data/260615.csv", header = TRUE)
saturday = read.csv("data/270615.csv", header = TRUE)
sunday = read.csv("data/280615.csv", header = TRUE)

# Load necessary packages -------------------------------------------------

install.packages("lubridate")
library(lubridate)

# Make data for the whole week --------------------------------------------

fullWeek <- monday
fullWeek <- rbind(fullWeek, tuesday, wedensday, thursday, friday, saturday, sunday)

# Add Time and Date as separete columns -----------------------------------
dateTime <- dmy_hms(fullWeek$DateAndTime, tz = "CET")
date(dateTime)
as.Date(dateTime) # by default as.Date assumes you want to know the date in UTC
dateTime

date <- as.Date(dmy_hms(fullWeek$DateAndTime, tz = "CET"))
date

time <- format(as.POSIXct(dmy_hms(fullWeek$DateAndTime, tz = "CET")) ,format = "%H:%M:%S") 
time

fullWeek.date = data.frame(Date = date, fullWeek[,])
fullWeek.time = data.frame(Time = time, fullWeek[,])

fullWeek.date$Date
fullWeek.time$Time

fullWeek <- data.frame(Date = fullWeek.date$Date, fullWeek[,])
fullWeek <- data.frame(Time = fullWeek.time$Time, fullWeek[,])

head(fullWeek)

 # Make plot for time-/date intervals -----------------------------------
mondayMeanSolData <- mean(monday$SolData)
mondayMeanSolData
tuesdayMeanSolData <- mean(tuesday$SolData)
tuesdayMeanSolData
wedensdayMeanSolData <- mean(wedensday$SolData)
wedensdayMeanSolData
thursdayMeanSolData <- mean(thursday$SolData)
thursdayMeanSolData
fridayMeanSolData <- mean(friday$SolData)
fridayMeanSolData
saturdayMeanSolData <- mean(saturday$SolData)
saturdayMeanSolData
sundayMeanSolData <- mean(sunday$SolData)
sundayMeanSolData
fullWeekMeanSolData <- mean(fullWeek$SolData)
fullWeekMeanSolData

mondayMeanTamb <- mean(monday$Tamb)
mondayMeanTamb
tuesdayMeanTamb <- mean(tuesday$Tamb)
tuesdayMeanTamb
wedensdayMeanTamb <- mean(wedensday$Tamb)
wedensdayMeanTamb
thursdayMeanTamb <- mean(thursday$Tamb)
thursdayMeanTamb
fridayMeanTamb <- mean(friday$Tamb)
fridayMeanTamb
saturdayMeanTamb <- mean(saturday$Tamb)
saturdayMeanTamb
sundayMeanTamb <- mean(sunday$Tamb)
sundayMeanTamb
fullWeekMeanTamb <- mean(fullWeek$Tamb)
fullWeekMeanTamb

mondayMinTamb <- min(monday$Tamb)
mondayMinTamb
tuesdayMinTamb <- min(tuesday$Tamb)
tuesdayMinTamb
wedensdayMinTamb <- min(wedensday$Tamb)
wedensdayMinTamb
thursdayMinTamb <- min(thursday$Tamb)
thursdayMinTamb
fridayMinTamb <- min(friday$Tamb)
fridayMinTamb
saturdayMinTamb <- min(saturday$Tamb)
saturdayMinTamb
sundayMinTamb <- min(sunday$Tamb)
sundayMinTamb
fullWeekMinTamb <- min(fullWeek$Tamb)
fullWeekMinTamb

mondayMaxTamb <- max(monday$Tamb)
mondayMaxTamb
tuesdayMaxTamb <- max(tuesday$Tamb)
tuesdayMaxTamb
wedensdayMaxTamb <- max(wedensday$Tamb)
wedensdayMaxTamb
thursdayMaxTamb <- max(thursday$Tamb)
thursdayMaxTamb
fridayMaxTamb <- max(friday$Tamb)
fridayMaxTamb
saturdayMaxTamb <- max(saturday$Tamb)
saturdayMaxTamb
sundayMaxTamb <- max(sunday$Tamb)
sundayMaxTamb
fullWeekMaxTamb <- max(fullWeek$Tamb)
fullWeekMaxTamb

mondayMaxAirMass <- max(monday$Airmass)
mondayMaxAirMass
tuesdayMaxAirMass <- max(tuesday$Airmass)
tuesdayMaxAirMass
wedensdayMaxAirMass <- max(wedensday$Airmass)
wedensdayMaxAirMass
thursdayMaxAirMass <- max(thursday$Airmass)
thursdayMaxAirMass
fridayMaxAirMass <- max(friday$Airmass)
fridayMaxAirMass
saturdayMaxAirMass <- max(saturday$Airmass)
saturdayMaxAirMass
sundayMaxAirMass <- max(sunday$Airmass)
sundayMaxAirMass
fullWeekMaxAirMass <- max(fullWeek$Airmass)
fullWeekMaxAirMass


mondayMeanT_aSi <- mean(monday$T.a.Si)
mondayMeanT_aSi
tuesdayMeanT_aSi <- mean(tuesday$T.a.Si)
tuesdayMeanT_aSi
wedensdayMeanT_aSi <- mean(wedensday$T.a.Si)
wedensdayMeanT_aSi
thursdayMeanT_aSi <- mean(thursday$T.a.Si)
thursdayMeanT_aSi
fridayMeanT_aSi <- mean(friday$T.a.Si)
fridayMeanT_aSi
saturdayMeanT_aSi <- mean(saturday$T.a.Si)
saturdayMeanT_aSi
sundayMeanT_aSi <- mean(sunday$T.a.Si)
sundayMeanT_aSi
fullWeekMeanT_aSi <- mean(fullWeek$T.a.Si)
fullWeekMeanT_aSi


# Extra ---------------------------------------------------------------
summary(monday, tuesday)
plot(monday)
rm(date, time)

#Sets last coloumn to the first
monday <- monday[,c(ncol(mandag),1:(ncol(mandag)-1))]

 
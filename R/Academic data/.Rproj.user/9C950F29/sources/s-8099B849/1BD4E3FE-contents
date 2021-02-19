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
install.packages("ggplot2")
library(ggplot2)
install.packages("ggpubr")
library(ggpubr)
install.packages("ggridges")
library(ggridges)

# Make data for the whole week --------------------------------------------

fullWeek <- monday
fullWeek <-
  rbind(fullWeek, tuesday, wedensday, thursday, friday, saturday, sunday)

# Add Time and Date as separete columns -----------------------------------
dateTime <- dmy_hms(fullWeek$DateAndTime, tz = "CET")
date(dateTime)
as.Date(dateTime) # by default as.Date assumes you want to know the date in UTC
dateTime

date <- as.Date(dmy_hms(fullWeek$DateAndTime, tz = "CET"))
date

time <-
  format(as.POSIXct(dmy_hms(fullWeek$DateAndTime, tz = "CET")) , format = "%H:%M:%S")
time

fullWeek.date = data.frame(Date = date, fullWeek[, ])
fullWeek.time = data.frame(Time = time, fullWeek[, ])

fullWeek.date$Date
fullWeek.time$Time

fullWeek <- data.frame(Date = fullWeek.date$Date, fullWeek[, ])
fullWeek <- data.frame(Time = fullWeek.time$Time, fullWeek[, ])

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

head(fullWeek)
levels()

max(
  max(fullWeek$Pmax.a.Si),
  max(fullWeek$Pmax.423),
  max(fullWeek$Pmax.422),
  max(fullWeek$Pmax.433),
  max(fullWeek$Pmax.459),
  max(fullWeek$Pmax.A10160),
  max(fullWeek$Pmax.A10156),
  max(fullWeek$Pmax.CIS),
  max(fullWeek$Pmax.GPV),
  max(fullWeek$Pmax.NESTE)
)

m <- matrix(
  data = cbind(
    fullWeek$Pmax.a.Si,
    fullWeek$Pmax.459,
    fullWeek$Pmax.CIS,
    fullWeek$Pmax.NESTE,
    fullWeek$Pmax.433,
    fullWeek$Pmax.422,
    fullWeek$Pmax.A10160,
    fullWeek$Pmax.A10156,
    fullWeek$Pmax.423,
    fullWeek$Pmax.GPV
  ),
  nrow = 6095,
  ncol = 10
)

summary(m)

colnames(m) <- c(
  "Unisolar 3J a-Si",
  "BP Solar mono-Si",
  "AvanCIS",
  "Sunconnex mono-Si",
  "RS Solar mono-Si",
  "RS Solar poly-Si",
  "Q-Cells E multi-Si",
  "Q-Cells R multi-Si",
  "Sanyo HIT mono/a-Si",
  "Gallivare multi-Si"
)
stargazer(df, rownames = FALSE)
summary(df)
View(m)
head(m)

df <- as.data.frame(m)
df
df <- data.frame(Date = fullWeek.date$Date, df[, ])

dfs <- stack(df)
dfs

dfs$Date <- fullWeek$Date
dfs$Time <- fullWeek$Time

dfs
colnames(dfs) <- c("Values", "Modules")

is.factor(dfs[, 3])

unstack(dfs)

#Temeratures in module
ggplot(dfs,
       aes(x = Values, y = Modules)) +
  grid(NA, 5, lwd = 2) +
  geom_density_ridges_gradient(aes(fill = ..x..), scale = 0.9, size = 0) +
  scale_fill_gradientn(colours = c("#1E9600FF", "#FFF200FF", "#FF0000FF"),
                       name = "Power [W]") +
  labs(title = 'Maximum power point power in modules', x = "Power [W]")


install.packages("viridis")
library(viridis)

ggplot(lincoln_weather,
       aes(x = `Mean Temperature [F]`, y = `Month`, fill = ..x..)) +
  geom_density_ridges_gradient(scale = 3,
                               rel_min_height = 0.01,
                               gradient_lwd = 1.) +
  scale_x_continuous(expand = c(0.01, 0)) +
  scale_y_discrete(expand = c(0.01, 0)) +
  scale_fill_viridis(name = "Temp. [F]", option = "C") +
  labs(title = 'Temperatures in Lincoln NE',
       subtitle = 'Mean temperatures (Fahrenheit) by month for 2016\nData: Original CSV from the Weather Underground') +
  theme_ridges(font_size = 13, grid = TRUE) + theme(axis.title.y = element_blank())

dfs$Date <- fullWeek$Date
dfs$Time <- fullWeek$Time

ggplot(dfs,
       aes(x = Values, y = Modules)) +
  geom_density_ridges_gradient(aes(fill = Values, y = Modules),
                               scale = 0.9,
                               size = 0) +
  scale_fill_gradientn(colours = c("#1E9600FF", "#FFF200FF", "#FF0000FF"),
                       name = "Power [W]") +
  labs(title = 'Maximum power point power in modules', x = "Power [W]")


#Calculating production estimate
ProdEst_aSi = 1
panelSize_a.Si = 1.01
eff_a.Si = 0.063
i = 6095
#while (i != 6095) {
#  ProdEst_a.Si = fullWeek$SolData[i]*panelSize_a.Si*eff_a.Si
#  print("Hello")
#  i++
#}



ProdEst = matrix(ncol = 10, nrow = 6095)
colnames(ProdEst) <- c(
  "Unisolar 3J a-Si",
  "BP Solar mono-Si",
  "AvanCIS",
  "Sunconnex mono-Si",
  "RS Solar mono-Si",
  "RS Solar poly-Si",
  "Q-Cells E multi-Si",
  "Q-Cells R multi-Si",
  "Sanyo HIT mono/a-Si",
  "Gallivare multi-Si"
)
panelData = matrix(ncol = 2, nrow = 10)
panelData[1,1] = 1.01
panelData[2,1] = 0.63
panelData[3,1] = 1.07
panelData[4,1] = 0.54
panelData[5,1] = 1.94
panelData[6,1] = 1.94
panelData[7,1] = 1.71
panelData[8,1] = 1.71
panelData[9,1] = 1.39
panelData[10,1] = 0.44
panelData[1,2]= 0.063
panelData[2,2]= 0.117
panelData[3,2]= 0.103
panelData[4,2]= 0.174
panelData[5,2]= 0.155
panelData[6,2]= 0.144
panelData[7,2]= 0.126
panelData[8,2]= 0.127
panelData[9,2]= 0.173
panelData[10,2]= 0.117
i = 1
j = 1
for (i in 1:6094) {
  for (j in 1:10) {
  ProdEst[i, j] <- (fullWeek$SolData[i] * panelData[j, 1] * panelData[j, 2])
  }
}

View(ProdEst)
head(ProdEst)

df_prodEst <- as.data.frame(ProdEst)
df_prodEst

dfs_prodEst <- stack(df_prodEst)
colnames(dfs_prodEst) <- c("Values", "Modules")
dfs_prodEst

summary(dfs)

dfs %>%
  ggplot(aes(y = as.factor(Modules) %>% fct_rev())) +
  geom_joy(
    aes(x = dfs_prodEst$Values),
    fill = "red",
    colour = FALSE,
    alpha = 0.7,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = "Recorded Values"),
    fill = "blue",
    colour = FALSE,
    alpha = 0.4,
    show.legend = TRUE,
    scale = 0.9
  ) +
  scale_fill_cyclical(
    breaks = c("Values", "Values"),
    labels = c('Values' = "Recorded watt production", 'Values' = "Estimated watt production"),
    values = c("#ff0000", "#0000ff", "#ff8080", "#8080ff"),
    name = "", guide = "legend"
  )+
  scale_x_continuous(expand = c(0, 0)) +
labs(
  x = "Watt production [W]",
  y = "Module",
  title = "Watt production comparison between modules",
  caption = "MA171-G 19V Group 6 | Source: UiA"
) +
  theme_bw() +
  theme(panel.border = element_blank())
p2 + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                        panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))


colnames(dfs_prodEst) <- c("Estimated Values", "Modules")
colnames(dfs) <- c("Recorded Values", "Modules")
colnames(dfsUni) <- c("Recorded.Values", "Modules", "Estimated.Values")

dfsUni <- dfs
dfsUni$Estimated.Values <- dfs_prodEst

dfs_prodEst <- dfs_prodEst[,-2]

dfsUni <- stack(dfUni)

dfsUni
dfsUni %>%
  ggplot(aes(y = Modules)) +
  geom_density_ridges(
    aes(fill = paste("Estimated.Values", "Recorded.Values")), 
    alpha = .8, color = "white"
  ) +
  labs(
    x = "Watt production [W]",
    y = "Modules",
    title = "Indy vs Unionist vote in Catalan elections",
    subtitle = "(SolData (W/m^2)) * (størrelse på panelet (m^2)) * (effektivitet (%)) = produksjonsestimat (W)",
    caption = "MA171-G 19V Group 6 | Source: UiA"
  ) +
  scale_y_discrete(expand = c(0.01, 0)) +
  scale_x_continuous(expand = c(0.01, 0)) +
  scale_fill_cyclical(
    breaks = c("Estimated.Values", "Recorded.Values"),
    labels = c('Estimated.Values' = "Indy", 'Recorded.Values' = "Unionist"),
    values = c("#ff0000", "#0000ff", "#ff8080", "#8080ff"),
    name = "Data", guide = "legend"
  ) +
  theme_ridges(grid = FALSE)

##### Watt production comparison [Calculated VS Recorded] #####

p3 <- dfsUni %>%
  ggplot(aes(y = as.factor(Modules) %>% fct_rev())) +
  geom_joy(
    aes(x = dfsUni$Recorded.Values),
    fill = "red",
    colour = FALSE,
    alpha = 0.6,
    show.legend = TRUE,
    scale = 0.9,
    to = 350
  ) +
  geom_joy(
    aes(x = dfsUni$Estimated.Values),
    fill = "blue",
    colour = FALSE,
    alpha = 0.4,
    show.legend = TRUE,
    scale = 0.9,
    to = 350
  ) +
labs(
  x = "Watt production [W]",
  y = "Module",
  title = "Watt production comparison",
  subtitle = "Blue: Calculated watt production \n Red: Recorded watt production",
  caption = "MA171-G 19V Group 6 | Source: UiA"
) +
  theme_bw() +
  theme(panel.border = element_blank())
p3 + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                        panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))


##### Watt production plot ####

p1 <- df %>%
  ggplot(aes(y = as.factor(Date) %>% fct_rev())) +
  geom_joy(
    aes(x = df$Unisolar.3J.a.Si),
    fill = "purple",
    colour = FALSE,
    alpha = 0.6,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$BP.Solar.mono.Si),
    fill = "blue",
    colour = FALSE,
    alpha = 0.4,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$AvanCIS),
    fill = "brown",
    colour = FALSE,
    alpha = 0.5,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$Sunconnex.mono.Si),
    fill = "cyan",
    colour = FALSE,
    alpha = 0.45,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$RS.Solar.mono.Si),
    fill = "green",
    colour = FALSE,
    alpha = 0.4,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$RS.Solar.poly.Si),
    fill = "red",
    colour = FALSE,
    alpha = 0.35,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$Q.Cells.E.multi.Si),
    fill = "grey",
    colour = FALSE,
    alpha = 0.3,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$Q.Cells.R.multi.Si),
    fill = "orange",
    colour = FALSE,
    alpha = 0.25,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$Sanyo.HIT.mono.a.Si),
    fill = "pink",
    colour = FALSE,
    alpha = 0.2,
    show.legend = TRUE,
    scale = 0.9
  ) +
  geom_joy(
    aes(x = df$Gallivare.multi.Si),
    fill = "yellow",
    colour = FALSE,
    alpha = 0.15,
    show.legend = TRUE,
    scale = 0.9
  ) +
  #legend(
  #  "right",
  #  legend = TRUE,
  #  fill = c(
  #    "Unisolar.3J.a.Si",
  #    "BP.Solar.mono.Si",
  #    "AvanCIS",
  #    "Sunconnex.mono.Si",
  #    "RS.Solar.mono.Si",
  #    "RS.Solar.poly.Si",
  #    "Q.Cells.E.multi.Si",
  #    "Q.Cells.R.multi.Si",
  #    "Sanyo.HIT.mono.a.Si",
  #    "Gallivare.multi.Si"
  #  )
  #) +
  labs(
    x = "Watt production [W]",
    y = "Date of measurment",
    title = "Watt production comparison between modules",
    caption = "MA171-G 19V Group 6 | Source: UiA"
  ) +
  theme_bw() +
  theme(panel.border = element_blank())
p1 + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                              panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))

# Extra ---------------------------------------------------------------
#summary(monday, tuesday)
#plot(monday)
#rm(date, time)
install.packages("stargazer")

library(stargazer)

stargazer(fullWeek)

#Sets last coloumn to the first
monday <- monday[, c(ncol(mandag), 1:(ncol(mandag) - 1))]

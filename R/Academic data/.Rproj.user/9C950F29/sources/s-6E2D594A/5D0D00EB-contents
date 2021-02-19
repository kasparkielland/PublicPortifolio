org_data <- read.csv("Portfolio\ 2\ data.csv", header = TRUE)
# org_data <- read.csv(file.choose(), header = TRUE)

install.packages("ggpubr", "tidyverse", "hexbin")
library("ggpubr")
library("gridExtra")
library("dplyr")
library("tidyverse")
install.packages(hexbin)
library("hexbin")

data <- org_data[2:15]
attach(data)
colnames(data)

# Summary
summary(data)
summary(Attrition)
summary(Degree_Type)
summary(Achieved_Credit_Points)
summary(Attendance_Type)
summary(Age)
summary(Failed_Credit_Points)
summary(International_student)
summary(Gender)
summary(GPA)
summary(OP_Score)
summary(Socio_Economic_Status)
summary(Teaching._Period_Admitted)
summary(Faculty)

# Histogram
# hist(Attrition)
# hist(Degree_Type)
hist(Achieved_Credit_Points)
# hist(Attendance_Type)
hist(Age)
hist(Failed_Credit_Points)
# hist(International_student)
# hist(Gender)
hist(GPA)
hist(OP_Score)
# hist(Socio_Economic_Status)
# hist(Teaching._Period_Admitted)
# hist(Faculty)

#### Table ####
table(Attrition)                  # NA
table(Degree_Type)                # NA
# table(Achieved_Credit_Points)     # 92.96941
table(Attendance_Type)            # NA
# table(Age)                        # 22.74157
# table(Failed_Credit_Points)       # 8.032941
table(International_student)      # NA
table(Gender)                     # NA
# table(GPA)                        # 4.549467
# table(OP_Score)                   # 10.73529
table(Socio_Economic_Status)      # NA
table(Teaching._Period_Admitted)  # NA
table(Faculty)                    # NA

#----- Task 1 -----
#### GPA ####
density_GPA <- data %>%
  ggplot( aes(x=GPA))+
  xlab("GPA") + 
  ylab("Density") +
  geom_density(fill="#13BFC4", 
               color="#e9ecef", 
               alpha=0.9) +
  geom_vline(xintercept = mean(GPA), 
             color="#13BFC4") +
  geom_text(aes(round(mean(GPA), 2), 0.3, 
                label = paste("Mean: ", round(mean(GPA), 2)), 
                hjust = 1.5), 
            size = 4, 
            color = "#13BFC4") +
  theme_minimal()
density_GPA <- density_GPA + 
  ggtitle("GPA")

#### OP score ####
density_OP_score <- data %>%
  ggplot( aes(x=OP_Score)) +
  xlab("OP score") + 
  ylab("Density") +
  geom_density(fill="#F7766D", 
               color="#e9ecef", 
               alpha=0.9) +
  geom_vline(xintercept = mean(OP_Score), 
             color="#F7766D") +
  geom_text(aes(round(mean(OP_Score), 2), 0.06, 
                label = paste("Mean: ", round(mean(OP_Score), 2)), 
                hjust = -0.2), 
            size = 4, color = "#F7766D") +
  theme_minimal()
density_OP_score <- density_OP_score + 
  ggtitle("OP Score")

#### Achived credit points ####
histogram_Achieved_Credit_Points <- data %>%
  ggplot(aes(x=Achieved_Credit_Points)) +
  xlab("Achieved credit points") + 
  ylab("Number of occurences") +
  geom_histogram(fill="#02BC38", 
                 color="#e9ecef", 
                 alpha=0.9) +
  geom_vline(xintercept = mean(Achieved_Credit_Points), 
             color="#02BC38") +
  geom_text(aes(round(mean(Achieved_Credit_Points), 2), 1000, 
                label = paste("Mean: ", round(mean(Achieved_Credit_Points), 2)), 
                hjust = -0.1), 
            size = 4, 
            color = "#02BC38") +
  theme_minimal()
histogram_Achieved_Credit_Points <- histogram_Achieved_Credit_Points + 
  ggtitle("Achived Credit Points")

#### Failed credit points ####
histogram_Failed_Credit_Points <- data %>%
  ggplot( aes(x=Failed_Credit_Points)) +
  xlab("Failed credit points") + 
  ylab("Number of occurences") +
  geom_histogram(fill="#F7766D", 
                 color="#e9ecef", 
                 alpha=0.9) +
  geom_vline(xintercept = mean(Failed_Credit_Points), 
             color="#F7766D") +
  geom_text(aes(round(mean(Failed_Credit_Points), 2), 1750, 
                label = paste("Mean: ", round(mean(Failed_Credit_Points), 2)), 
                hjust = -0.1), 
            size = 4, color = "#F7766D") +
  theme_minimal()
histogram_Failed_Credit_Points <- histogram_Failed_Credit_Points + 
  ggtitle("Failed Credit Points")

#### Age ####
density_Age <- data %>%
  ggplot( aes(x=Age)) +
  coord_cartesian(xlim = c(min(Age), 
                           max(Age)), 
                  expand = FALSE) +
  xlab("Age") + 
  ylab("Density") +
  geom_density(fill="#6599FF", 
               color="#e9ecef", 
               alpha=0.9) +
  geom_vline(xintercept = mean(Age), 
             color="#6599FF") +
  geom_text(aes(round(mean(Age), 0), 0.25, 
                label = paste("Mean: ", round(mean(Age), 0)), 
                hjust = -0.1, 
                vjust = 1.5), 
            size = 4, 
            color = "#6599FF") +
  theme_minimal()
density_Age <- density_Age + 
  ggtitle("Age")

#### Attrition Distrubiation ####
df_Attrition <- data %>%
  group_by(Attrition) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_Attrition <- df_Attrition %>%
  arrange(desc(Attrition)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)
# Creates pie chart for distrubiation
pie_chart_Attrition <- ggplot(df_Attrition, 
                              aes(x = "", 
                                  y = prop, 
                                  fill = Attrition)) +
  geom_bar(width = 1,
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", start = 0) +
  theme_void()
pie_chart_Attrition <- pie_chart_Attrition + 
  labs(fill = "Attrition") + 
  ggtitle("Attrition")

#### Degree_Type Distrubiation ####
df_Degree_Type <- data %>%
  group_by(Degree_Type) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_Degree_Type <- df_Degree_Type %>%
  arrange(desc(Degree_Type)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)
# Creates pie chart for distrubiation
pie_chart_Degree_Type <- ggplot(df_Degree_Type, 
                                aes(x = "", 
                                    y = prop, 
                                    fill = Degree_Type)) +
  geom_bar(width = 1, 
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", start = 0) +
  theme_void()
pie_chart_Degree_Type <- pie_chart_Degree_Type + 
  labs(fill = "Degree type") + 
  ggtitle("Degree type")

#### Attendance_Type Distrubiation ####
df_Attendance_Type <- data %>%
  group_by(Attendance_Type) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_Attendance_Type <- df_Attendance_Type %>%
  arrange(desc(Attendance_Type)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)

# Creates pie chart for gender distrubiation
pie_chart_Attendance_Type <- ggplot(df_Attendance_Type, 
                                    aes(x = "", 
                                        y = prop, 
                                        fill = Attendance_Type)) +
  geom_bar(width = 1, 
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", start = 0) +
  theme_void()
pie_chart_Attendance_Type <- pie_chart_Attendance_Type + 
  labs(fill = "Attendance type") + 
  ggtitle("Attendance type")

#### International_student Distrubiation ####
df_International_student <- data %>%
  group_by(International_student) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_International_student <- df_International_student %>%
  arrange(desc(International_student)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)
# Creates pie chart for gender distrubiation
pie_chart_International_student <- ggplot(df_International_student, 
                                          aes(x = "", 
                                              y = prop, 
                                              fill = International_student)) +
  geom_bar(width = 1, 
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", start = 0) +
  theme_void()
pie_chart_International_student <- pie_chart_International_student + 
  labs(fill = "International student") + 
  ggtitle("International student")

#### Gender Distrubiation ####
df_Gender <- data %>%
  group_by(Gender) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_Gender <- df_Gender %>%
  arrange(desc(Gender)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)
# Creates pie chart for distrubiation
pie_chart_Gender <- ggplot(df_Gender, 
                           aes(x = "", 
                               y = prop, 
                               fill = Gender)) +
  geom_bar(width = 1, 
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", 
              start = 0) +
  theme_void()
pie_chart_Gender <- pie_chart_Gender + 
  scale_fill_discrete(name = "Gender", 
                      labels = c("Female", "Male")) + 
  ggtitle("Gender")

#### Socio_Economic_Status Distrubiation ####
df_Socio_Economic_Status <- data %>%
  group_by(Socio_Economic_Status) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_Socio_Economic_Status <- df_Socio_Economic_Status %>%
  arrange(desc(Socio_Economic_Status)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)
# Creates pie chart for gender distrubiation
pie_chart_Socio_Economic_Status <- ggplot(df_Socio_Economic_Status, 
                                          aes(x = "", 
                                              y = prop, 
                                              fill = Socio_Economic_Status)) +
  geom_bar(width = 1, 
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", start = 0) +
  theme_void()

pie_chart_Socio_Economic_Status <- pie_chart_Socio_Economic_Status + 
  labs(fill = "Socio economic status") + 
  ggtitle("Socio economic status")


#### Teaching._Period_Admitted Distrubiation ####
df_Teaching._Period_Admitted <- data %>%
  group_by(Teaching._Period_Admitted) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_Teaching._Period_Admitted <- df_Teaching._Period_Admitted %>%
  arrange(desc(Teaching._Period_Admitted)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)
# Creates pie chart for gender distrubiation
pie_chart_Teaching._Period_Admitted <- ggplot(df_Teaching._Period_Admitted, 
                                              aes(x = "", 
                                                  y = prop, 
                                                  fill = Teaching._Period_Admitted)) +
  geom_bar(width = 1, 
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", start = 0) +
  theme_void()
pie_chart_Teaching._Period_Admitted <- pie_chart_Teaching._Period_Admitted + 
  labs(fill = "Teaching period admitted") + 
  ggtitle("Teaching period admitted")

#### Faculty Distrubiation ####
df_Faculty <- data %>%
  group_by(Faculty) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_Faculty <- df_Faculty %>%
  arrange(desc(Faculty)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)
# Creates pie chart for distrubiation
pie_chart_Faculty <- ggplot(df_Faculty, 
                            aes(x = "", 
                                y = prop, 
                                fill = Faculty)) +
  geom_bar(width = 1, 
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", start = 0) +
  theme_void()
pie_chart_Faculty <- pie_chart_Faculty + 
  labs(fill = "Faculty") + 
  ggtitle("Faculty")


#### First_in_family ####
df_First_in_family <- data %>%
  group_by(First_in_family) %>%
  summarise(counts = n())
# Updates df with percantage distrubiation and a vector with the cumulative sum as element
df_First_in_family <- df_First_in_family %>%
  arrange(desc(First_in_family)) %>%
  mutate(prop = round(counts/sum(counts), 3), 
         lab.ypos = cumsum(prop) - 0.5*prop)
# Creates pie chart for distrubiation
pie_chart_First_in_family <- ggplot(df_First_in_family, 
                                    aes(x = "", 
                                        y = prop, 
                                        fill = First_in_family)) +
  geom_bar(width = 1, 
           stat = "identity", 
           color = "transparent") +
  geom_text(aes(y = lab.ypos, 
                label = prop*100), 
            color = "white") +
  coord_polar("y", start = 0) +
  theme_void()
pie_chart_First_in_family <- pie_chart_First_in_family + 
  labs(fill = "First in family") + 
  ggtitle("First in family")


#### All charts ####
combined_charts <- grid.arrange(
  arrangeGrob(pie_chart_Gender, pie_chart_Attrition, pie_chart_Degree_Type, ncol = 3),
  arrangeGrob(pie_chart_Teaching._Period_Admitted, pie_chart_Attendance_Type, pie_chart_International_student, ncol = 3),
  arrangeGrob(pie_chart_Socio_Economic_Status, pie_chart_First_in_family, pie_chart_Faculty, ncol = 3),
  arrangeGrob(histogram_Achieved_Credit_Points, histogram_Failed_Credit_Points, ncol = 2),
  arrangeGrob(density_Age, ncol = 1),
  arrangeGrob(density_OP_score, density_GPA, ncol = 2),
  nrow = 6)

#----- Task 2 -----
means <- aggregate(GPA ~  Gender, data, mean)
medians <- aggregate(GPA ~  Gender, data, median)

box_plot_GPA_Gender <- ggplot(data, 
                              aes(x=Gender, 
                                  y=GPA, 
                                  fill=Gender)) +
  geom_boxplot(alpha=0.8, 
               fatten = 0,
               notch = TRUE,
               varwidth = FALSE) +
  stat_summary(fun.y=mean, 
               geom="errorbar", 
               aes(ymax = ..y.., 
                   ymin = ..y..),
               width = 0.75, 
               size = 1, 
               linetype = "solid") +
  stat_summary(geom = "text", 
               label = paste("Mean: ", round(means$GPA, 2)),
               fun.y = mean,
               vjust=1.2) +
  stat_summary(geom = "text", 
               label = paste("Median: ", round(medians$GPA, 2)),
               fun.y = median,
               vjust=-1.2) +
  theme(legend.position="right",
        axis.title.x = element_blank(),
        axis.text.x = element_blank(),
        axis.ticks.x = element_blank()) +
  scale_fill_discrete(name = "Gender", 
                      labels = c("Female", "Male"))
#geom_text(data = means, aes(label = x, y = x), size = 5) + #adds average labels
#geom_text(data = medians, aes(label = round(x, 2), y = x - 0.5), size = 5) #adds median labels
box_plot_GPA_Gender + 
  ggtitle("Comparison of average GPA between\nfemale and male students", 
          subtitle = "The respective mean is represented by the black horizontal line\nThe respective median is reprenseted by the notch") +
  scale_y_continuous(breaks=seq(0,7,1))

t.test(GPA ~ Gender)

means

#----- Task 3 -----
library(hexbin)
library(RColorBrewer)

bin<-hexbin(GPA, OP_Score, xbins=20)
my_colors=colorRampPalette(rev(brewer.pal(11,'Spectral')))
plot(bin, style = "colorscale", legend = 1.2, lcex = 1,
     mincnt = 1, maxcnt = 40,
     colorcut = seq(0, 1, length = min(9, max(bin@count))),
     border = 1,
     colramp = my_colors,
     xlab = "GPA", ylab = "OP Score", 
     main = "Relationship between\nOP Score and GPA")

#----- Task 4 -----
plot(GPA, Achieved_Credit_Points)
lmGPA <- lm(Achieved_Credit_Points ~ GPA, data=data) #Create the linear regression
summary(lmGPA)
coefficients(lmGPA)
confint(lmGPA, level=0.95) # CIs for model parameters 
fitted(lmGPA) # predicted values
residuals(lmGPA) # residuals
anova(lmGPA) # anova table 
vcov(lmGPA) # covariance matrix for model parameters 
influence(lmGPA) # regression diagnostics

layout(matrix(c(1,2,3,4),2,2)) # optional 4 graphs/page 
plot(lmGPA)

layout(1)
plot(lmGPA$residuals, pch = 16, col = "blue") #Plot the results
abline(lmGPA) #Add a regression line

smoothScatter(GPA, y=Achieved_Credit_Points, ylab = "Achived Credit Points", main = "Achived Credit Points ~ GPA")
# plot(Achieved_Credit_Points ~ GPA, data = data, col = "blue")
with(data, lines(loess.smooth(GPA, Achieved_Credit_Points), col = "red"))
scatter.smooth(GPA, Achieved_Credit_Points, main="GPA ~ Achived Credit Points")

predictor_variables = c(Achieved_Credit_Points, Age, Failed_Credit_Points, OP_Score)
colnames(data) <- c("ID", "Attrition", "Degree Type", "Achieved Credit Points", "Attendance Type", "Age",
                    "Failed Credit Points", "International student", "First in family", "Gender", "GPA",
                    "OP Score", "Socio Economic Status", "Teaching Period Admitted", "Faculty")


head(data)

for (variable in 1:14) {
  # store data in column.i as x
  y_variable <- data[,variable]
  plot(y_variable ~ GPA, col = "blue")
  smoothScatter(GPA, y=y_variable, main = paste(colnames(data)[variable], " ~ GPA"))
  # plot(Achieved_Credit_Points ~ GPA, data = data, col = "blue")
  with(data, lines(loess.smooth(GPA, y_variable), col = "red"))
  
}

#Using Scatter Plot to visualise the relationship
par(mfrow = c(2, 2))  # Set up a 2 x 2 plotting space

smoothScatter(Achieved_Credit_Points, y=GPA, xlab = "Achived Credit Points", main = "GPA ~ Achived Credit Points")+
  with(data, lines(loess.smooth(Achieved_Credit_Points, GPA), col = "red"))

smoothScatter(Age, y=GPA, main = "GPA ~ Age")+
  with(data, lines(loess.smooth(Age, GPA), col = "red"))

smoothScatter(Failed_Credit_Points, y=GPA, xlab = "Failed Credit Points", main = "GPA ~ Failed Credit Points")+
  with(data, lines(loess.smooth(Failed_Credit_Points, GPA), col = "red"))

smoothScatter(OP_Score, y=GPA, xlab = "OP Score", main = "GPA ~ OP Score")+
  with(data, lines(loess.smooth(OP_Score, GPA), col = "red"))

# Using Boxplot to check for outliers
par(mfrow = c(1, 2))  # Set up a 1 x 2 plotting space
boxplot(Failed_Credit_Points, main = "Failed Credit Points", sub=paste("Outlier rows: ", boxplot.stats(Failed_Credit_Points)$out))
#boxplot(Achieved_Credit_Points, main = "Achived Credit Points", sub=paste("Outlier rows: ", boxplot.stats(Achieved_Credit_Points)$out))
#boxplot(OP_Score, main = "OP Score", sub=paste("Outlier rows: ", boxplot.stats(OP_Score)$out))
boxplot(GPA, main = "GPA", sub=paste("Outlier rows: ", boxplot.stats(GPA)$out))

# Using Density Plot to check of response variable is close to normal
library(e1071)
par(mfrow=c(1,2))
plot(density(GPA), main="Density Plot: GPA", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(GPA), 2)))
polygon(density(GPA), col="red")

#plot(density(Achieved_Credit_Points), main="Density Plot: Achived Credit Points", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(Achieved_Credit_Points), 2))) 
#polygon(density(Achieved_Credit_Points), col="red")

plot(density(Failed_Credit_Points), main="Density Plot: Failed Credit Points", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(Failed_Credit_Points), 2))) 
polygon(density(Failed_Credit_Points), col="red")

#plot(density(OP_Score), main="Density Plot: OP Score", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(OP_Score), 2))) 
#polygon(density(OP_Score), col="red")

cor(GPA, Achieved_Credit_Points)

linearMod <- lm(GPA ~ Failed_Credit_Points)
summary(linearMod)
# GPA = 4.929 - 0.047 * Achived_Credit_Points

gpaFunc = function(Failed_Credit_Points){4.929 - 0.047 * Failed_Credit_Points}
plot(gpaFunc, 1, 100, type = 'l')

# Create Training and Test data -
set.seed(100)  # setting seed to reproduce results of random sampling
trainingRowIndex <- sample(1:nrow(data), 0.8*nrow(data))  # row indices for training data
trainingData <- data[trainingRowIndex, ]  # model training data
testData  <- data[-trainingRowIndex, ]   # test data

# Build the model on training data
lmMod <- lm(GPA ~ OP_Score + Achieved_Credit_Points + Failed_Credit_Points, data=trainingData)  # build the model
gpaPred <- predict(lmMod, testData)  # predict GPA

summary (lmMod)  # model summary

numericalData <- data.frame(GPA, Achieved_Credit_Points, Age, Failed_Credit_Points, OP_Score)
colnames(numericalData) <- c("GPA", "Achieved Credit Points", "Age", "Failed Credit Points", "OP Score")
                    

mLinearMod<- lm(GPA ~ Achieved_Credit_Points + Age + Failed_Credit_Points + OP_Score, data=data)
summary(mLinearMod)
vif(mLinearMod)

install.packages("corrplot")
library(corrplot)
par(mfrow=c(1,1))
corrplot(cor(numericalData[,]))
corrplot.mixed(cor(numericalData[,]), lower.col = "black", number.cex = .5, tl.cex = .5)

mod <- lm(GPA ~ Achieved_Credit_Points + Failed_Credit_Points)
summary(mod)
vif(mod)

plot(Failed_Credit_Points, GPA)
abline(4.929, -0.047)

AIC (lmMod)  # Calculate akaike information criterion

actuals_preds$actuals

actuals_preds <- data.frame(cbind(actuals=testData$GPA, predicteds=gpaPred))  # make actuals_predicteds dataframe.
correlation_accuracy <- cor(actuals_preds)  # 44.66%
head(actuals_preds)

# Min-Max Accuracy Calculation
min_max_accuracy <- mean(apply(actuals_preds, 1, min) / apply(actuals_preds, 1, max))  
# => 77.35%, min_max accuracy

# MAPE Calculation
mape <- mean(abs((actuals_preds$predicteds - actuals_preds$actuals))/actuals_preds$actuals)  
# => inf %, mean absolute percentage deviation

install.packages('DMwR')
DMwR::regr.eval(actuals_preds$actuals, actuals_preds$predicteds)

# Create Training and Test data -
set.seed(100)  # setting seed to reproduce results of random sampling
trainingRowIndex <- sample(1:nrow(data), 0.8*nrow(data))  # row indices for training data
trainingData <- data[trainingRowIndex, ]  # model training data
testData  <- data[-trainingRowIndex, ]   # test data

xtabs(~ Attrition + Degree_Type, data=trainingData)
xtabs(~ Attrition + Achieved_Credit_Points, data=trainingData)
xtabs(~ Attrition + Attendance_Type, data=trainingData)
xtabs(~ Attrition + Age, data=trainingData)
xtabs(~ Attrition + Failed_Credit_Points, data=trainingData)
xtabs(~ Attrition + International_student, data=trainingData)
xtabs(~ Attrition + First_in_family, data=trainingData)
xtabs(~ Attrition + Gender, data=trainingData)
xtabs(~ Attrition + GPA, data=trainingData)
xtabs(~ Attrition + OP_Score, data=trainingData)
xtabs(~ Attrition + Socio_Economic_Status, data=trainingData)
xtabs(~ Attrition + Teaching._Period_Admitted, data=trainingData)
xtabs(~ Attrition + Faculty, data=trainingData)

logistic <- glm(Attrition ~ ., data=trainingData, family=binomial(link='logit'))
summary(logistic)

anova(logistic, test="Chisq")

fitted.results <- predict(logistic,newdata=subset(trainingData,select=c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)),type='response')
fitted.results <- ifelse(fitted.results > 0.5,1,0)

misClasificError <- mean(fitted.results != trainingData$Attrition)
print(paste('Accuracy',1-misClasificError))

p <- predict(logistic, newdata=subset(testData), type="response")
pr <- prediction(p, testData$Attrition)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)

auc <- performance(pr, measure = "auc")
auc <- auc@y.values[[1]]
auc

# Calculating overall pseudo R-square and p-value
ll.null <- logistic$null.deviance/-2
ll.proposed <- logistic$deviance/-2

# McFadden's pseudo R-square
(ll.null - ll.proposed) / ll.null

# p-value for R-square
1 - pchisq(2*(ll.proposed - ll.null), df=(length(logistic$coefficients)-1))

library(DAAG)
vif(logistic)

predicted.data <- data.frame(probability.of.attrition=logistic$fitted.values, attrition=data$Attrition)
predicted.data <- predicted.data[order(predicted.data$probability.of.attrition, decreasing=FALSE),]
# add a new column of the rank orders to the data frame
predicted.data$rank <- 1:nrow(predicted.data)
ggplot(data=predicted.data, aes(x=rank, y=probability.of.attrition)) +
  geom_point(aes(color=Attrition), alpha=1, shape=4, stroke=2) +
  xlab("Index") +
  ylab("Predicted probability of getting retained")

predicted.data$actuals <-factor(predicted.data$attrition, labels =c(0,1))
plotROC(actuals= predicted.data$actuals, predictedScores = predicted.data$probability.of.attrition)

optCutOff <- optimalCutoff(predicted.data$actuals, predicted.data$probability.of.attrition)[1]
optCutOff

misClassError(predicted.data$actuals, predicted.data$probability.of.attrition, threshold = optCutOff)

sensitivity(predicted.data$actuals, predicted.data$probability.of.attrition, threshold = optCutOff)

specificity(predicted.data$actuals, predicted.data$probability.of.attrition, threshold = optCutOff)

confusionMatrix(predicted.data$actuals, predicted.data$probability.of.attrition, threshold = optCutOff)

ci.auc(predicted.data$actuals, predicted.data$probability.of.attrition)

ci.auc(predicted.data$actuals, predicted.data$probability.of.attrition, conf.level = 0.9)

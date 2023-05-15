# predicting_hotel_cancellation
Final project for Data Science for Public Health 

We made a dashboard to present the booking status of hotel in 2017 and 2018 in the US.

R analysis: Expanding upon python analysis, we also used a different software R analyze on the hotel dataset. We generated additional deep learning models to predict the booking status (Binary response). These models include: Linear Discriminant Analysis, Classification Decision Tree, K-nearest Neighbors, Support Vector Machine (Radial), Random Forest, Logistic Regression, Stochastic Gradient Boosting, and Neural Network. The reason why we chose to use these models because this is a type of classification problem and our goal is to improve the prediction accuracy on the response. However, the disadvantage of running these models are that some of the models are computationally expensive. To ensure an efficient workflow, we decided to unify the control using 10 fold cross validation when training the models. To evaluate prediction performance of these models, we used confusion matrices to compare the sensitivity and specificity scores, prediction accuracy scores, and ROC. In conclusion, the best performed models are Random Forest, Stochastic Gradient Boosting, Support Vector Machine (Radial), and Neural Network.


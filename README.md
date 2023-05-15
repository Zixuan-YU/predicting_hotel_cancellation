### predicting_hotel_cancellation
Final project for Data Science for Public Health 

### EDA
We made a dashboard to present the booking status of hotel in 2017 and 2018 in the US.

### Python Analysis:

### R analysis: 
Expanding upon python analysis, we also used a different software R analyze on the hotel dataset. We generated additional deep learning models to predict the booking status (Binary response). These models include: Linear Discriminant Analysis, Classification Decision Tree, K-nearest Neighbors, Support Vector Machine (Radial), Random Forest, Logistic Regression, Stochastic Gradient Boosting, and Neural Network. The reason why we chose to use these models because this is a type of classification problem and our goal is to improve the prediction accuracy on the response. However, the disadvantage of running these models are that some of the models are computationally expensive. To ensure an efficient workflow, we decided to unify the control using 10 fold cross validation when training the models. To evaluate prediction performance of these models, we used confusion matrices to compare the sensitivity and specificity scores, prediction accuracy scores, and ROC. In conclusion, the best performed models are Random Forest, Stochastic Gradient Boosting, Support Vector Machine (Radial), and Neural Network.  

### Take home messages and summary:
In this analysis, we first explore the data and examine missing values. Then we build prediction models and compare their performance via 10-fold cross validation.   
  
Because we still have a substantiate amount of data, we drop all rows containing missing values. Our exploratory data analysis revealed that certain patterns in booking behaviors. The most significant pattern was associated with the variable 'lead_time'. Bookings with a longer lead time were more inclined to cancellations while bookings with shorter lead times had a lower likelihood of cancellation. Additionally, we found that previous guests and those who required car parking spaces or made special requests were less likely to cancel their bookings. We also found that the more expensive the room and the longer the lead time, the higher the likelihood of a room cancellation.  

According to the correlations matrix, we found no significantly strong correlations between different variables, suggesting a good degree of independence between our features. So we are confident we could build robust prediction models based on the available data.  
 
With respect to the machine learning models, we had to balance the classes, as our dataset contained significantly more non-cancellation data than cancellation data. To address this imbalance, we employed an OverSampling strategy.    
 
The models varied in their performance, with the Random Forest model achieving the highest AUC of 0.958. This model was effective at predicting both outcomes, i.e., cancellations and non-cancellations. It outperformed the other models because it excels at handling a large number of features and is particularly adept at managing complex interactions among variables. In the context of our hotel booking project, this model can effectively capture the intricate relationships between features such as 'lead_time', 'avg_price_per_room', and 'number_of_special_requests'. Moreover, Random Forest is less prone to overfitting, thereby making it more robust for predicting booking cancellations. Its ensemble nature, which aggregates results from numerous decision trees, provides a more reliable and accurate prediction, making it the most suitable model for this application.   

**Sensitivity & Specificity**: Specificity scores are much higher than sensitivity scores, emphasizing a need to improve the prediction accuracy for the true canceled cases in future analysis.  

 
In summary, our data analysis and modeling provide valuable insights for hotel management in understanding the factors contributing to booking cancellations. With these insights, the hotel can devise strategies to reduce cancellations and hence increase revenue. The predictive model can also be used to forecast future cancellations, assisting in effective room inventory management. Continuous updating of the model with new data can further enhance its accuracy and usefulness.  
 



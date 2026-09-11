# Risk Register

| Risk           | Impact                                             | Mitigation                                         |
| -------------- | -------------------------------------------------- | -------------------------------------------------- |
| False Positive | Customer incorrectly identified as likely to churn | Human review and threshold tuning                  |
| False Negative | Customer likely to churn is missed                 | Monitor recall and improve model                   |
| Data Leakage   | Model learns from future information               | Proper feature selection and train-test separation |
| Data Bias      | Unfair predictions for some customer groups        | Regular bias checks and dataset review             |
| Missing Data   | Reduced model performance                          | Data validation and preprocessing                  |
| Privacy Risk   | Exposure of customer information                   | Secure data handling and access control            |
| Model Drift    | Performance decreases over time                    | Continuous monitoring and retraining               |

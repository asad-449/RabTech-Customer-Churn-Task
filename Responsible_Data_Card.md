# Responsible Data Card

## Dataset Purpose

This dataset is used to predict whether a customer is likely to churn. The prediction will support customer retention efforts and service improvement. It should not be used for legal, hiring, or financial decisions.

## Provenance and Permission

The dataset was provided as part of the RabTech Academy internship task and is used for educational and learning purposes.

## Population and Representation

The dataset represents customers of a service. Some customer groups may be underrepresented, and the dataset may not reflect all real-world customer behaviors.

## Features and Target

### Features

* customer_id
* tenure_months
* support_tickets
* monthly_spend_inr
* last_login_days
* plan_type

### Target

* churned

### Possible Risks

* Data leakage if future information is included.
* Plan type may indirectly act as a proxy for customer segments.

## Quality Checks

* Check for missing values.
* Check for duplicate records.
* Check for outliers.
* Maintain proper train-test separation.

## Risks and Safeguards

### False Positive Risk

A loyal customer may be incorrectly classified as likely to churn.

### False Negative Risk

A customer likely to churn may be missed.

### Privacy Risk

Customer information should be handled securely.

### Mitigation

Regular evaluation, monitoring, and responsible use of predictions.

## Intended Evaluation

* Baseline Rule-Based Model
* Accuracy
* Precision
* Recall
* F1 Score
* Error Analysis

# ML Problem Framing Memo

## Decision

Predict whether a customer is likely to churn (leave the service).

## Prediction Target

Target Variable: **churned**

* 1 = Customer Churned
* 0 = Customer Retained

## Unit of Observation

One row represents one customer.

## Action Window

The prediction will be used before customer churn occurs so that the business can take retention actions such as offers, support, or engagement campaigns.

## Non-ML Baseline

A simple rule-based approach:

* Customers with high last_login_days and multiple support tickets are considered high-risk.
* Customers with recent activity and longer tenure are considered low-risk.

## Business Objective

Reduce customer churn and improve customer retention.

## Expected Outcome

Identify customers who are likely to leave and take preventive actions to retain them.

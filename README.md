# 🏷️ Advanced Marketing Analytics for Sports Wear Group

## 📊 Project Overview
This project simulates a consulting role for Sports Wear Group to demonstrate how advanced analytics can improve marketing campaign performance. The goal is to build a predictive model that identifies which customers are most likely to convert during promotional campaigns, and evaluate the financial impact of data-driven targeting strategies.

---

## 🎯 Business Objectives
- Predict whether a customer will buy (`label = 1`) or not (`label = 0`) during a marketing campaign.
- Optimize who receives the campaign to maximize profit and minimize wasted cost.
- Simulate Return on Investment (ROI) at different probability thresholds to guide real-world decisions.

---

## 🧠 Data Summary

The dataset contains product, promotion, pricing, and campaign performance features, including:

- **Product Features**:  
  - `productgroup`, `category`, `style`, `gender`, `sizes`, `main_color`, `sec_color`
- **Pricing Features**:  
  - `regular_price`, `current_price`, `ratio`, `discount_pct`, `cost`
- **Promotions**:  
  - `promo1` (media ad), `promo2` (store event)
- **Time Context**:  
  - `retailweek`, `month`, `week_number`, `is_holiday_season`
- **Target**:  
  - `label` (0 = no conversion, 1 = conversion)

> Note: `sales`, `unit_profit`, and `total_profit` were excluded from modeling due to leakage (they occur *after* the label is known).

---

## ⚙️ Modeling Workflow

1. **Feature Engineering**
   - Derived discount percentages, time-based features, and size range flags.
   - Converted RGB values to approximate human-readable colors.
   - Encoded categorical features and dropped leaky ones.

2. **Model Training**
   - Models: Random Forest and Logistic Regression
   - Metrics: Precision, Recall, F1 Score, Accuracy
   - Custom threshold tuning to balance false positives/negatives

3. **Business ROI Simulation**
   - Developed reusable function to simulate profit and ROI based on:
     - `profit_per_conversion = $804.5`
     - `cost_per_offer = $6.5`
   - Evaluated thresholds from 0.2 to 0.9

---

## 📈 Key Results

| Threshold | ROI (x) | Precision (1) | Recall (1) | Net Profit |
|-----------|---------|----------------|-------------|------------|
| 0.5       | 42.8x   | 0.35           | 89.8%       | $1.66M     |
| 0.65      | 46.1x   | 0.38           | 67.6%       | $1.25M     |
| 0.7       | **47.5x** | 0.39         | 48.2%       | $894K      |

- 🔥 Threshold = **0.7** gives highest ROI but misses over 50% of potential buyers.
- ✅ Threshold = **0.65** is best balanced in terms of cost and reach.

---

## 📂 Files Included

| File                          | Description |
|-------------------------------|-------------|
| `campaign_model.ipynb`        | Jupyter Notebook with EDA, feature engineering, model training, and ROI analysis |
| `model_roi_evaluator.py`      | Reusable function for ROI evaluation |
| `plots/`                      | Visualizations: conversion rates, threshold-vs-ROI graphs |
| `README.md`                   | This file |

---

## 📌 Takeaways

- Deep discounts alone don’t ensure conversions — data-driven targeting is more effective.
- Models benefit from engineered features like color, sizes, seasonality, and promo signals.
- ROI simulation is critical for aligning model predictions with real business outcomes.

---

## 🚀 Next Steps
- Deploy the model in production to score real-time campaign targets.
- Integrate into marketing dashboard for continuous testing and ROI tracking.
- Extend the dataset with customer behavioral and demographic data.

---


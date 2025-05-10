# 🏷️ Advanced Marketing Analytics for Sports Wear Group

## 📊 Project Overview

This project simulates a real-world consulting engagement with **Sports Wear Group**, a global sports retailer. The objective is to analyze campaign effectiveness, optimize targeting strategies, and build a predictive model to identify customers most likely to convert — using historical transaction, pricing, and product data.

---

## 🎯 Business Goals

- Understand what drives conversion across time, products, and customer segments
- Identify the most profitable combinations of product group, price, promo, and timing
- Build a predictive model to support smarter, data-driven campaign targeting
- Support marketing decisions with explainable KPIs, visualizations, and customer insights

---

## 🧠 Data Summary [After Feature Engineering]

The dataset contains product-level features and campaign results across several dimensions:

### 📦 Product Features
- `productgroup`, `category`, `style`, `gender`, `sizes`, `main_color`, `sec_color`

### 💸 Pricing & Promotion
- `regular_price`, `current_price`, `ratio` (current/regular price), `cost`, `discount_pct`
- `promo1`, `promo2` 

### 🗓️ Time Context
- `retailweek`, `month`, `week_number`, `holiday_season`, `month-yr`

### 🎯 Target
- `label` → 1 = customer converted, 0 = no conversion

> Note: `sales`, `unit_profit`, and `total_profit` were excluded from modeling due to target leakage.

---

## 🧾 Campaign Summary KPIs

- **🧍 Total Conversions**: 13,909 customers
- **📈 Overall Conversion Rate**: 14.0%
- **💸 Average Discount Given**: 45.44%
- **💰 Average Profit Margin**: 52.73%

---

## 🔍 Insights Summary

### 📅 Time Series
- Sales and conversions spike in **Nov–Dec** (holidays), but margins drop
- Lighter discount periods (Feb–Mar) show stronger profitability

### 📦 Product Group
| Group               | Sales   | Profit    | Margin | Note            |
|---------------------|---------|-----------|--------|-----------------|
| Hardware Accessories| 1.14M   | \$25.6M   | 89.2%  | ✅ Very high margin |
| Shorts              | 0.57M   | \$12.4M   | 83.4%  | ✅ High margin |
| Shoes               | 3.41M   | \$50.4M   | 32.7%  | ❗ High volume, low margin |

### 🌍 Country
| Country | Sales  | Profit    | Margin | Note          |
|---------|--------|-----------|--------|---------------|
| Germany | 2.80M  | \$48.3M   | 54.4%  | ✅ Top performer |
| France  | 0.89M  | \$16.2M   | 49.9%  | 🟡 Underutilized |

### 🚻 Gender
| Gender  | Sales  | Profit    | Margin | Note              |
|---------|--------|-----------|--------|-------------------|
| Women   | 3.97M  | \$74.4M   | 61.1%  | ✅ Highest returns |
| Unisex  | 0.57M  | \$8.0M    | 28.2%  | 🔻 Underperforming |

### 🎯 Promotion
- **Promo1**: Drives volume but lowers margin; used heavily in holiday months
- **Promo2**: Sparingly used; unclear impact; consider structured testing

---

## ✅ Takeaways

- Women, Germany, and Hardware Accessories drive the majority of profit
- Promo1 campaigns increase sales but can erode margin
- Discounting is effective, but optimal levels must be balanced
- Random Forest model provides a valuable targeting layer for campaign efficiency
- Future testing and rollout can integrate predictions with marketing tools

---

## 🤖 Predictive Modeling: Random Forest Classifier

A Random Forest model was trained to predict which customers are most likely to convert. The goal is to support **smarter campaign targeting** that avoids waste and maximizes return.

### ⚙️ Modeling Workflow

- **Feature Engineering**:
  - Extracted time components, size flags, color names from RGB
  - Encoded categorical variables
  - Removed features with data leakage (e.g., `sales`, `unit_profit`)

- **Model Training**:
  - Models tested: Logistic Regression and Random Forest
  - Final model: Random Forest with threshold tuning

- **Final Threshold**: 0.65  
  - **Precision**: 84%  
  - **Recall**: 75% 
  - **F1 Score**: 78% 
  - **Accuracy**: 75%  
  - Balanced between reach and precision

---

## 📈 Final Evaluation

### 📋 Classification Report
|              | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| **0**        | 0.93      | 0.75   | 0.83     | 13010   |
| **1**        | 0.36      | 0.71   | 0.48     | 2529    |
| **Accuracy** |           |        | 0.75     | 15539   |
| **Macro Avg**| 0.65      | 0.73   | 0.66     | 15539   |
| **Weighted Avg** | 0.84  | 0.75   | 0.78     | 15539   |


### 🔲 Confusion Matrix
![](./reports/rf_less_features_confusion_matrix.png)

---





🚚 **OFI Predictive Delivery Optimizer**
📘 **Overview**

The OFI Predictive Delivery Optimizer is a machine-learning powered web application that predicts potential delivery delays before they occur.
It empowers logistics teams to take proactive actions such as rescheduling, reassigning carriers, or changing dispatch times — thereby reducing delivery risks, costs, and improving customer satisfaction.

This project demonstrates a full end-to-end AI workflow — from data ingestion and model training to an interactive Streamlit dashboard.


🧠 **Key Features**

✅ **Machine Learning Delay Prediction**

Predicts whether an order is likely to be delayed (High / Medium / Low risk).

Generates a probability score (0–1) for each order.

✅ **Data-Driven Insights**

Combines multiple datasets (orders, routes, vehicles, warehouses, costs, and customer feedback).

Cleans, merges, and enriches data automatically.

✅ **Interactive Streamlit Dashboard**

Upload your dataset directly from the UI.

Apply filters (by product category, priority, etc.).

View risk probabilities and download prediction results.

✅ **Business Visualizations**

📊 Delay Probability Distribution (Histogram)

📦 Delay Risk by Priority (Boxplot)

🥧 Risk Level Proportion (Pie Chart)

📈 Delay Probability vs Distance (Line Chart)

📊 Average Delay by Product Category (Bar Chart)


⚙️ **Tech Stack**
Category	                  Tools
Language	                  Python
Frontend	                  Streamlit
Machine Learning	          scikit-learn, joblib
Data Handling	              pandas, numpy
Visualization	              Plotly
Version Control           	Git & GitHub


  🚀 **How to Run Locally**
1️⃣ Clone the Repository
git clone https://github.com/snitehacker/OFI-Predictive-Delivery-Optimizer.git
cd OFI-Predictive-Delivery-Optimizer

2️⃣ Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
cd app
streamlit run app.py
Then open the local Streamlit link (usually http://localhost:8501/).


🧩 **Workflow Summary**

1️⃣ Data Ingestion & Cleaning

Reads and merges multiple CSV files using Pandas.

Handles missing values and normalizes numeric columns.

2️⃣ Feature Engineering

Derived metrics: distance_km, delivery_priority, weather_impact_score, carrier_performance_score.

3️⃣ Model Training

Classification model trained to predict is_delayed.

Algorithms: Random Forest, Logistic Regression, XGBoost (tested).

Model saved as model.pkl.

4️⃣ Visualization & Dashboard

User uploads data → App predicts → Dashboard displays visual trends & KPIs.


📊 **Example Insights**
Metric	                              Example Output
Average Delay Probability	                 0.37
High-Risk Deliveries	                     142
Total Orders Processed	                  2,500
Average Distance	                       186 km


💡 **Business Impact**

📦 Operational Efficiency — Proactively identify at-risk deliveries.
💰 Cost Reduction — Optimize routes, reduce fuel and labor costs.
🚛 Customer Satisfaction — Improve on-time delivery rate by >10%.
📈 Data-Driven Decision Making — Visual KPIs for strategic insights.

🧑‍💻 **Author**

Snigdha Jhureley


# -----------------------------------------
# SECTION 1: Load Libraries and Model
# -----------------------------------------
import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load the trained model
model = joblib.load("model.pkl")

# -----------------------------------------
# SECTION 2: Streamlit Page Setup
# -----------------------------------------
st.set_page_config(page_title="Predictive Delivery Optimizer", layout="wide")
st.title("🚚 Predictive Delivery Optimizer")
st.write("This app predicts whether a delivery will be delayed based on order-level data.")

# -----------------------------------------
# SECTION 3: File Upload and Data Preview
# -----------------------------------------
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read data
    data = pd.read_csv(uploaded_file)
    st.subheader("📄 Uploaded Data Preview")
    st.dataframe(data.head())

    # Prepare features
    if "is_delayed" in data.columns:
        X = data.drop("is_delayed", axis=1)
    else:
        X = data.copy()

    # -----------------------------------------
    # SECTION 4: Model Prediction with Error Handling
    # -----------------------------------------
    try:
        predictions = model.predict(X)
        probabilities = model.predict_proba(X)[:, 1]
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
        st.stop()

    # Add prediction columns
    data["Predicted Delay Probability"] = probabilities
    data["Predicted Delay Category"] = [
        "High Risk" if p > 0.8 else "Medium Risk" if p > 0.5 else "Low Risk"
        for p in probabilities
    ]

    # -----------------------------------------
    # SECTION 5: KPI SUMMARY
    # -----------------------------------------
    st.subheader("📊 Key Business Metrics")

    total_orders = len(data)
    high_risk = data["Predicted Delay Category"].eq("High Risk").sum()
    medium_risk = data["Predicted Delay Category"].eq("Medium Risk").sum()
    low_risk = data["Predicted Delay Category"].eq("Low Risk").sum()
    avg_delay_prob = data["Predicted Delay Probability"].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Orders", total_orders)
    col2.metric("High Risk Deliveries", high_risk)
    col3.metric("Medium Risk Deliveries", medium_risk)
    col4.metric("Average Delay Probability", f"{avg_delay_prob:.2f}")

    # -----------------------------------------
    # SECTION 6: FILTERS (Sidebar)
    # -----------------------------------------
    st.sidebar.header("🔍 Filters")

    # Filter by Priority
    if "priority" in data.columns:
        selected_priorities = st.sidebar.multiselect(
            "Select Priority",
            options=data["priority"].unique(),
            default=data["priority"].unique()
        )
        data = data[data["priority"].isin(selected_priorities)]

    # Filter by Product Category
    if "product_category" in data.columns:
        selected_categories = st.sidebar.multiselect(
            "Select Product Category",
            options=data["product_category"].unique(),
            default=data["product_category"].unique()
        )
        data = data[data["product_category"].isin(selected_categories)]

    # -----------------------------------------
    # SECTION 7: VISUALIZATIONS
    # -----------------------------------------
    st.subheader("📈 Data Insights & Visualizations")

    # 1️⃣ Histogram - Distribution of Predicted Probabilities
    fig_hist = px.histogram(
        data,
        x="Predicted Delay Probability",
        nbins=20,
        title="Distribution of Predicted Delay Probability"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    # 2️⃣ Boxplot - Delay Probability by Priority
    if "priority" in data.columns:
        fig_box = px.box(
            data,
            x="priority",
            y="Predicted Delay Probability",
            color="priority",
            title="Delay Probability by Priority Level"
        )
        st.plotly_chart(fig_box, use_container_width=True)

    # 3️⃣ Line Chart - Delay Probability vs Distance
    if "distance_km" in data.columns:
        fig_line = px.line(
            data.sort_values("distance_km"),
            x="distance_km",
            y="Predicted Delay Probability",
            title="Delay Probability vs Distance Trend"
        )
        st.plotly_chart(fig_line, use_container_width=True)

    # 4️⃣ Pie Chart - Risk Distribution
    fig_pie = px.pie(
        data,
        names="Predicted Delay Category",
        title="Proportion of Delay Risk Levels"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    # 5️⃣ (Optional) Bar Chart - Average Delay Probability by Product Category
    if "product_category" in data.columns:
        avg_delay_by_cat = (
            data.groupby("product_category")["Predicted Delay Probability"]
            .mean()
            .reset_index()
        )
        fig_bar = px.bar(
            avg_delay_by_cat,
            x="product_category",
            y="Predicted Delay Probability",
            title="Average Delay Probability by Product Category"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # -----------------------------------------
    # SECTION 8: DOWNLOAD RESULTS
    # -----------------------------------------
    st.download_button(
        label="⬇️ Download Results as CSV",
        data=data.to_csv(index=False).encode("utf-8"),
        file_name="predicted_delays.csv",
        mime="text/csv"
    )

else:
    st.info("📤 Please upload a CSV file to begin.")

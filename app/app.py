import streamlit as st
import pandas as pd
import joblib
import plotly.express as px


model = joblib.load("model.pkl")

st.set_page_config(page_title="Predictive Delivery Optimizer", layout="wide")
st.title("🚚 Predictive Delivery Optimizer")
st.write("This app predicts whether a delivery will be delayed based on order-level data.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data Preview")
    st.dataframe(data.head())

    if "is_delayed" in data.columns:
        X = data.drop("is_delayed", axis=1)
    else:
        X = data.copy()

    predictions = model.predict(X)
    probabilities = model.predict_proba(X)[:, 1]

    data["Predicted Delay Probability"] = probabilities
    data["Predicted Delay Category"] = ["High Risk" if p > 0.8 else "Medium Risk" if p > 0.5 else "Low Risk" for p in probabilities]

    st.subheader("Predictions")
    st.dataframe(data[["order_id", "Predicted Delay Probability", "Predicted Delay Category"]].head(10))

    st.subheader("📊 Delay Probability Distribution")
    fig = px.histogram(data, x="Predicted Delay Probability", nbins=20, title="Distribution of Predicted Delay Probability")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Delay Risk by Priority")
    if "priority" in data.columns:
        fig2 = px.box(data, x="priority", y="Predicted Delay Probability", color="priority", title="Delay Probability by Priority Level")
        st.plotly_chart(fig2, use_container_width=True)

    st.download_button(
        label="Download Results as CSV",
        data=data.to_csv(index=False).encode("utf-8"),
        file_name="predicted_delays.csv",
        mime="text/csv"
    )

import streamlit as st
import requests
st.set_page_config(page_title="Customer Churn Prediction", page_icon=":bar_chart:", layout="wide")
API_URL = st.secrets["API_URL"]
with st.sidebar:
    st.title("Customer Information")
    tenure_months = st.slider("Tenure Months", min_value=0,value=12)
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)","Unknown"])
    contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two years"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "None","Unknown"])
    promo_discount_pct = st.slider("Promo Discount Percentage", min_value=0.0, max_value=100.0, value=10.0)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    support_tickets_3m = st.number_input("Support Tickets in Last 3 Months", min_value=0, value=1)
    last_login_days = st.slider("Days Since Last Login", min_value=0, max_value=365, value=30)

    predict_button=st.button("Predict Churn")
    st.markdown(
        """
           <style>
           .watermark {
               position: fixed;
               bottom: 10px;
               right: 10px;
               opacity: 0.5;
               font-size: 12px;
               color: black;
           }
           </style>
           <div class="watermark">Created by Your Name</div>
           Omari Kwache's Churn Prediction App
           </div>
        """,
        unsafe_allow_html=True
    )

st.title("Customer Churn Prediction")
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("Input Data")
    st.write(f"**Tenure Months:** {tenure_months}")
    st.write(f"**Payment Method:** {payment_method}")
    st.write(f"**Contract Type:** {contract_type}")
    st.write(f"**Internet Service:** {internet_service}")
    st.write(f"**Promo Discount Percentage:** {promo_discount_pct}%")
    st.write(f"**Monthly Charges:** {monthly_charges}")
    st.write(f"**Support Tickets in Last 3 Months:** {support_tickets_3m}")
    st.write(f"**Days Since Last Login:** {last_login_days}")

    with col2:
        st.subheader("Prediction Result")
        if predict_button:
            input_data = {
                "tenure_months": tenure_months,
                "payment_method": payment_method,
                "contract_type": contract_type,
                "internet_service": internet_service,
                "promo_discount_pct": promo_discount_pct,
                "monthly_charges": monthly_charges,
                "support_tickets_3m": support_tickets_3m,
                "last_login_days": last_login_days
            }
            response = requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                result = response.json()
                st.write(f"**Churn Probability:** {result['churn_probability']:.2f}")
                st.write(f"**Churn Prediction with Tuned Threshold:** {result['churn_prediction with tuned threshold']}")
                st.write(f"**Status with Untuned Threshold:** {result['Status with untuned threshold']}")
            else:
                st.error("Error in API request. Please try again.")
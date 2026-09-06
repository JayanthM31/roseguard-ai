import streamlit as st

st.set_page_config(
    page_title="RoseGuard AI",
    page_icon="🌹",
    layout="wide"
)

st.title("🌹 RoseGuard AI")
st.subheader("Neuro-Symbolic AI Framework for Rose Disease Detection")

st.success("✅ RoseGuard AI website is running successfully!")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌡 Temperature", "24.5 °C")

with col2:
    st.metric("💧 Humidity", "87 %")

with col3:
    st.metric("🍃 Leaf Wetness", "81 %")

with col4:
    st.metric("🌱 Soil Moisture", "68 %")

st.markdown("---")

st.header("📷 Rose Disease Analysis")

uploaded_file = st.file_uploader(
    "Upload a rose image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="Uploaded Rose Image",
        use_container_width=True
    )

    st.info("🧠 AI analysis module will be connected in the next step.")

st.markdown("---")

st.header("⚠️ Pre-Symptomatic Risk")

st.warning("HIGH RISK")

st.write(
    "The environmental monitoring and Neuro-Symbolic AI modules "
    "will be connected in the next stage."
)

st.markdown("---")

st.caption(
    "RoseGuard AI | Real-Time IoT + Vision AI + Neuro-Symbolic Reasoning"
)

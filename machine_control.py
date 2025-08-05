import streamlit as st
import paho.mqtt.publish as publish

MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = "esp32/relay"

st.set_page_config(page_title="Machine Relay Control", layout="centered")
st.title("🛠️ Machine Relay Control Panel")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔌 Turn ON Relay 1"):
        publish.single(MQTT_TOPIC, "relay1_on", hostname=MQTT_BROKER)
    if st.button("🛑 Turn OFF Relay 1"):
        publish.single(MQTT_TOPIC, "relay1_off", hostname=MQTT_BROKER)

with col2:
    if st.button("🔌 Turn ON Relay 2"):
        publish.single(MQTT_TOPIC, "relay2_on", hostname=MQTT_BROKER)
    if st.button("🛑 Turn OFF Relay 2"):
        publish.single(MQTT_TOPIC, "relay2_off", hostname=MQTT_BROKER)

st.success("Relays will respond through the public broker.")

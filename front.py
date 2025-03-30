import streamlit as st
from trip_advisor_bcp import setup_travel_crew

# Configuração da página
st.set_page_config(
    page_title="Travel Advisor",
    page_icon="✈️",
    layout="centered"
)

# Título
st.title("✈️ Travel Advisor")

# Formulário principal
with st.form("travel_form"):
    # Destino
    destination = st.text_input("Destination", placeholder="Where are you going?")

    # Preferências
    preferences = st.text_area("Travel Preferences",
                               placeholder="Enter your preferences separated by commas\ne.g.: beach, hiking, museums...",
                               height=100)

    # Sobre você
    about_you = st.text_area("About You (optional)",
                             placeholder="Tell us about your travel style...",
                             height=100)

    submitted = st.form_submit_button("Generate Itinerary")

# Gerar itinerário
if submitted:
    if not destination:
        st.warning("Please enter a destination")
    else:
        inputs = {
            'travel_preferences': preferences,
            'destination': destination,
            'user_input': about_you
        }

        # Container para o resultado
        result_container = st.empty()

        # Mostra o spinner enquanto processa
        with st.spinner("✈️ Planning your perfect trip... This might take a moment..."):
            response = setup_travel_crew(inputs)

            # Limpa o spinner e mostra o resultado
            result_container.success(f"## ✈️ {destination} Itinerary")
            st.write(response)
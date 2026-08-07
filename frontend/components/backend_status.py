import streamlit as st

from frontend.services.api_client import APIClientError, api_client


def render_backend_status() -> None:
    try:
        health = api_client.get_health()
    except APIClientError:
        st.error("Backend: Unavailable")
        return

    if health.get("status") == "healthy":
        st.success("Backend: Healthy")
    else:
        st.warning("Backend: Unknown status")
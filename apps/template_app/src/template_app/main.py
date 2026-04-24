import streamlit as st

from template_app.utils.calculations import calculate_dental_metrics


def run() -> None:
    st.set_page_config(page_title="Dental AI Template", page_icon="🦷")
    st.title("🦷 Dental Assistant")
    st.write(
        "Enter dental measurement data (e.g., pocket depth in mm), and let's calculate the average!"
    )

    # User input
    raw_input = st.text_input("Enter measurements separated by commas:", "1.5, 2.0, 3.2, 1.8")

    try:
        # Data processing
        data = [float(x.strip()) for x in raw_input.split(",") if x.strip()]

        if st.button("Run Analysis"):
            results = calculate_dental_metrics(data)

            # Display results in cards
            col1, col2 = st.columns(2)
            col1.metric("Average Depth", f"{results['average']:.2f} mm")
            col2.metric("Maximum Value", f"{results['max']:.2f} mm")

            st.success("The analysis completed successfully.")
    except ValueError:
        st.error("Please enter only numbers separated by commas!")


if __name__ == "__main__":
    run()

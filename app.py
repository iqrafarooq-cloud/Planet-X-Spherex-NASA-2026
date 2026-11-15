
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="SPHEREx Explorer",
    page_icon="🌌",
    layout="wide"
)

ROOT = Path(__file__).parent

st.title("🌌 SPHEREx Explorer")
st.subheader("Explore the infrared universe with NASA SPHEREx")

st.write(
    "Explore SPHEREx observations, compare aligned images "
    "and investigate changes in the sky."
)

# Load NASA observation metadata
metadata_path = ROOT / "spherex_metadata.csv"

if metadata_path.exists():
    metadata = pd.read_csv(metadata_path)

    st.success(f"Loaded {len(metadata)} metadata records")

    st.subheader("SPHEREx Observation Data")
    st.dataframe(metadata, use_container_width=True)
else:
    st.warning("Metadata file not found.")

# Show existing image preview
st.subheader("Image Difference Preview")

preview = ROOT / "aligned_difference_preview.png"

if preview.exists():
    st.image(
        str(preview),
        caption="Preliminary SPHEREx aligned difference preview",
        use_container_width=True
    )
else:
    st.info("Image preview not available yet.")

st.divider()

st.subheader("About SPHEREx Explorer")
st.write(
    "Our project uses NASA SPHEREx observations to explore "
    "the infrared universe and compare astronomical images."
)

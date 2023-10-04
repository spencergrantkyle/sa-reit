import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data


@st.cache
def load_data():
    df = pd.read_excel(
        "/Users/spencerkyle/Documents/SA_REIT_Property_Fund_Data/Bloomberg_Terminal_REIT_Data/DPS 2023 to 2019.xlsx")
    df_cleaned = df.iloc[2:].reset_index(drop=True)
    return df_cleaned


df = load_data()

# Title
st.title("DPS Data Visualization for REITs")

# Sidebar for REIT selection
selected_reits = st.sidebar.multiselect(
    "Select REITs for Visualization",
    df['Name'].unique(),
    default=df['Name'].unique()
)

# Filter the dataframe based on selected REITs
df_filtered = df[df['Name'].isin(selected_reits)]

# Plotting
fig, ax = plt.subplots(figsize=(15, 10))

# Loop through each row (REIT) in the filtered dataframe and plot its data
for index, row in df_filtered.iterrows():
    ax.plot(['2023', '2022', '2021', '2019', '2020'], [row['DPS:2023'], row['DPS:2022'],
            row['DPS:2021'], row['DPS:2019'], row['DPS:2020']], label=row['Name'])

# Adding title and labels
ax.set_title("DPS Data for Selected Years per REIT")
ax.set_xlabel("Year")
ax.set_ylabel("DPS Value")
ax.legend(loc="upper right")
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

st.pyplot(fig)

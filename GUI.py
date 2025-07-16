import streamlit as st
import numpy as np

def matrix_input(name = "Matrix", rows = 3, cols = 3):
    st.write(f"Enter values for **{name}**")
    matrix = []

    for i in range(rows):
        row = []
        cols_container = st.columns(cols)
        for j in range(cols):
            val = cols_container[j].number_input(f"{name}[{i + 1},{j + 1}]", key = f"{name}_{i}_{j}", value = 0.0)
            row.append(val)
        matrix.append(row)
    return np.array(matrix)

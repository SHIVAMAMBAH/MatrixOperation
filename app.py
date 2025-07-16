import streamlit as st
from GUI import matrix_input
import matrix_operations as mo

st.title("🧮 Matrix Operation App")

operation = st.selectbox("Choose Operation", ["Addition", "Subtraction", "Multiplication", "Transpose", "Determinant", "Inverse", "Trace"])

rows = st.number_input("Rows", min_value=1, value=2)
cols = st.number_input("Columns", min_value=1, value=2)

if operation in ["Addition", "Subtraction", "Multiplication"]:
    st.subheader("Matrix A")
    A = matrix_input("A", int(rows), int(cols))

    st.subheader("Matrix B")
    B = matrix_input("B", int(rows), int(cols if operation != "Multiplication" else int(rows)))

    if st.button("Calculate"):
        try:
            if operation == "Addition":
                st.write(mo.matrix_add(A, B))
            elif operation == "Subtraction":
                st.write(mo.matrix_subtract(A, B))
            elif operation == "Multiplication":
                st.write(mo.matrix_multiplication(A, B))
        except Exception as e:
            st.error(f"Error: {e}")

elif operation in ["Transpose", "Determinant", "Inverse", "Trace"]:
    st.subheader("Matrix A")
    A = matrix_input("A", int(rows), int(cols))

    if st.button("Calculate"):
        try:
            if operation == "Transpose":
                st.write(mo.matrix_transpose(A))
            elif operation == "Determinant":
                if rows == cols:
                    st.write(mo.matrix_determinant(A))
                else:
                    st.error("Matrix must be square for determinant.")
            elif operation == "Inverse":
                if rows == cols:
                    st.write(mo.matrix_inverse(A))
                else:
                    st.error("Matrix must be square for inverse.")
            elif operation == "Trace":
                if rows == cols:
                    st.write(mo.matrix_trace(A))
                else:
                    st.write("Matrix must be square fo trace.")
        except Exception as e:
            st.error(f"Error: {e}")

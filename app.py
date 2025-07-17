import streamlit as st
from GUI import matrix_input
import matrix_operations as mo


st.set_page_config(
    page_title="Matrix Master",  
    page_icon="🔢",              # You can use an emoji or a custom image
    layout="centered"            
)


st.title("Matrix Operation App")
st.caption("*open in desktop mode if using in mobile phone")

operation = st.selectbox("Choose Operation", 
                         ["Addition", 
                          "Subtraction", 
                          "Multiplication", 
                          "Transpose", 
                          "Determinant", 
                          "Inverse", 
                          "Trace",
                          "Adjoint"]
                        )
st.caption("Currently, Only these operations are supported, will support more in future.")


if operation in ["Addition", "Subtraction", "Multiplication"]:
    st.subheader("Matrix A")

    rows_A = st.number_input("Rows_A", min_value=1, value=2)
    cols_A = st.number_input("Columns_A", min_value=1, value=2)

    A = matrix_input("A", int(rows_A), int(cols_A))

    st.subheader("Matrix B")

    rows_B = st.number_input("Rows_B", min_value=1, value=2)
    cols_B = st.number_input("Columns_B", min_value=1, value=2)
    
    B = matrix_input("B", int(rows_B), int(cols_B))

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

elif operation in ["Transpose", "Determinant", "Inverse", "Trace", "Adjoint"]:
    st.subheader("Matrix A")
    
    rows = st.number_input("Rows", min_value=1, value=2)
    cols = st.number_input("Columns", min_value=1, value=2)

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
            elif operation == "Adjoint":
                 st.write(mo.matrix_adjoint(A))
        except Exception as e:
            st.error(f"Error: {e}")

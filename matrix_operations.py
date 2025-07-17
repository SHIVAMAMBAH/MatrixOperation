import numpy as np
from sympy import Matrix
from typing import Union


def matrix_add(a:np.ndarray, b:np.ndarray)-> Union[np.ndarray, str]:
    '''This function takes two input matrices and returs thier SUM 
    if the shape is same Otherwise an ERROR message in string form.'''

    if a.shape != b.shape:
        return "Error: Matrices must have same shape to be added."
    return np.add(a, b)

def matrix_subtract(a:np.ndarray, b:np.ndarray)-> Union[np.ndarray, str]:
    '''This function takes two input matrices and returs thier DIFFERENCE 
    if the shape is same Otherwise an ERROR message in string form.'''

    if a.shape != b.shape:
        return "Error: Matrices must have same shape to be added."
    return np.subtract(a, b)

def matrix_multiplication(a:np.ndarray, b:np.ndarray)-> Union[np.ndarray, str]:
    '''This function takes two input matrices and returs thier PRODUCT 
    if the number of columns of Matrix 1 is equal to the number of rows
    of Matrix 2 Otherwise an ERROR message in string form.'''

    if a.shape[1] != b.shape[0]:
        return "Error: Number of columns of Matrix 1 must be equal to the number of rows of Matrix 2."
    return np.multiply(a, b)

def matrix_transpose(a:np.ndarray)->np.ndarray:
    '''This function takes one input Matrix and returns its transpose.'''

    return np.transpose(a)

def matrix_adjoint(a:Matrix)->Matrix:
    '''This function takes a matrix as input and return its adjoint and is written using sympy'''
    
    return np.array(a.adjugate()).astype(np.float64)

def matrix_determinant(a:np.ndarray)->np.float32:
    '''This function takes a square matrix as input and returns it's transpose'''

    if a.shape[0]!=a.shape[1]:
        return "Error: Matrix should be a square matrix"
    return np.linalg.det(a)

def matrix_inverse(a:np.ndarray)->np.ndarray:
    '''This function takes one input Matrix and returns its inverse.'''

    if a.shape[1]!=a.shape[0]:
        return "Error: Matrix should be a square matrix."
    return np.linalg.inv(a)

def matrix_trace(a:np.ndarray)->np.float32:
    '''This function takes one input Matrix and returns its trace.'''

    if a.shape[1]!=a.shape[0]:
        return "Error: Matrix should be a square matrix."
    return np.linalg.trace(a)
from pydantic import BaseModel

class model_input(BaseModel):
    N : float
    P : float
    K : float
    temperature : float
    humidity : float
    ph : float
    rainfall : float
    
"""
N
P
K
temperature
humidity
ph
rainfall
"""

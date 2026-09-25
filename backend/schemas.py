from pydantic import BaseModel

class model_input(BaseModel):
    N : float
    P : float
    k : float
    temp : float
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

from pydantic import BaseModel 
class Input(BaseModel): 
    balance: float
    rec_sent: int 
    amount: float 
    size: int 
    weight: int 
    version: int 
    lock_time: int 
    is_coinbase: int 
    has_witness: int
    input_count: int 
    output_count: int 
    input_total_usd: float 
    output_total_usd: float 
    fee_usd: float 
    fee_per_kb_usd: float 
    fee_per_kwu_usd: float 
    cdd_total: float 
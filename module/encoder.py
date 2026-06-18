import torch.nn as nn
from torch.nn import MultiheadAttention

class TransformerEncoderBlock(nn.Module):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.multi_head_attn=MultiheadAttention()

# JSON Proof Structure definition
from typing import List, Union, Literal, Optional
from pydantic import BaseModel, Field

AnyNode = Union[
    'ShowNode', 'AssumeNode', 'FixNode', 'FindNode',
    'HaveNode', 'ObtainNode', 'SufficesToProveNode', 'LogicChainNode',
    'CalculationChainNode', 'DefineNode', 'HintNode', 'PlaceHolderNode'
]

class ShowNode(BaseModel):
    type: Literal["Show"] = "Show"
    proposition: List[str]
    method: Optional[List[str]] = None
    scope: List['AnyNode']

class AssumeNode(BaseModel):
    type: Literal["Assume"] = "Assume"
    assumption: List[str]
    scope: List['AnyNode']

class FixNode(BaseModel):
    type: Literal["Fix"] = "Fix"
    variable: List[str]
    condition: Optional[List[str]] = None
    scope: List['AnyNode']

class HaveNode(BaseModel):
    type: Literal["Have"] = "Have"
    claim: List[str]
    reason: Optional[List[str]] = None

class SufficesToProveNode(BaseModel):
    type: Literal["SufficesToProve"] = "SufficesToProve"
    sufficient_proposition: List[str]
    reason: Optional[List[str]] = None

class ObtainNode(BaseModel):
    type: Literal["Obtain"] = "Obtain"
    obtained_variable: List[str]
    condition: List[str]
    reason: Optional[List[str]] = None

class FindNode(BaseModel):
    type: Literal["Find"] = "Find"
    target: List[str]
    condition: Optional[List[str]] = None
    scope: List['AnyNode']

class LogicChainStep(BaseModel):
    operator: str
    proposition: List[str]
    reason: Optional[List[str]] = None

class LogicChainNode(BaseModel):
    type: Literal["LogicChain"] = "LogicChain"
    initial_proposition: List[str]
    step: List[LogicChainStep]

class CalculationChainStep(BaseModel):
    operator: str
    expression: List[str]
    reason: Optional[List[str]] = None

class CalculationChainNode(BaseModel):
    type: Literal["CalculationChain"] = "CalculationChain"
    initial_expression: List[str]
    step: List[CalculationChainStep]

class DefineNode(BaseModel):
    type: Literal["Define"] = "Define"
    term: str
    definition: str

class HintNode(BaseModel):
    type: Literal["Hint"] = "Hint"
    text: str

class PlaceHolderNode(BaseModel):
    type: Literal["PlaceHolder"] = "PlaceHolder"
    text: str

class Structure(BaseModel):
    thinking: Optional[str] = None
    structure: List[AnyNode]

for model in [
    ShowNode, AssumeNode, FixNode, FindNode, HaveNode, ObtainNode,
    SufficesToProveNode, LogicChainNode, CalculationChainNode, DefineNode,
    HintNode, PlaceHolderNode
]:
    model.update_forward_refs()
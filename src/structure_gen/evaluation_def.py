# JSON structure designed for structure-evaluation
from typing import Literal
from pydantic import BaseModel, Field

class PrincipleEvaluation(BaseModel):
    issues: str
    score: Literal[1, 2, 3, 4, 5]

class EvaluationSummary(BaseModel):
    information_equivalency: PrincipleEvaluation = Field(..., alias="InformationEquivalency")
    no_free_variables: PrincipleEvaluation = Field(..., alias="NoFreeVariables")
    concrete_reference: PrincipleEvaluation = Field(..., alias="ConcreteReference")
    accurate_node_type: PrincipleEvaluation = Field(..., alias="AccurateNodeType")
    accurate_scoping: PrincipleEvaluation = Field(..., alias="AccurateScoping")
    logical_clarification: PrincipleEvaluation = Field(..., alias="LogicalClarification")

class EvaluationResult(BaseModel):
    evaluation: EvaluationSummary
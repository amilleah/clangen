from __future__ import annotations

from enum import Enum
from typing import Dict, List, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from scripts.models.common.biome import BiomeNoExclusions


class PreySize(Enum):
    small = "small"
    medium = "medium"
    threat = "threat"


class PreyItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    biome: List[Union[BiomeNoExclusions, Literal["any"]]] = Field(
        ..., description="Biomes that prey can be found in."
    )
    singular: str = Field(..., description="Name of one of the prey.")
    plural: str = Field(..., description="Name of several of the prey.")
    size: PreySize = Field(..., description="Size of the prey.")


class PreySchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    comment: List[str] = Field(default_factory=list, description="Notes for writers.")
    catalog: Dict[str, Dict[str, PreyItem]] = Field(
        ..., description="Prey animals keyed by the name used in prey tags."
    )
    groups: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="Prey tag names used to look up keys or groups.",
    )

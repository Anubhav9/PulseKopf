from pydantic import BaseModel
from typing import Literal

class MetricsModel(BaseModel):
    heartRate_enabled: bool
    stepCount_enabled: bool
    activeEnergy_enabled: bool
    restingEnergy_enabled: bool
    interval: int


class MetricsModelStatus(BaseModel):
    current_heartRate : int | Literal["Not Enabled"]
    heartRate_lastupdated_timestamp: str | Literal["Not Enabled"]
    current_stepCount: int | Literal["Not Enabled"]
    stepCount_lastupdated_timestamp: str | Literal["Not Enabled"]
    current_activeEnergy: int | Literal["Not Enabled"]
    activeEnergy_lastupdated_timestamp: str | Literal["Not Enabled"]
    current_restingEnergy: int | Literal["Not Enabled"]
    restingEnergy_lastupdated_timestamp: str | Literal["Not Enabled"]


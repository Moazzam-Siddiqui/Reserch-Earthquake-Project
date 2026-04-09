from pydantic import BaseModel, Field


class PredictInput(BaseModel):
    """JSON body for /predict: raw waveform samples (training used 2000 Z-channel points)."""

    input: list[float] = Field(
        ...,
        description="Numerical features: seismic waveform samples; padded or truncated to 2000 points.",
    )

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class dataingestion_config:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    unzip_data_dir : Path
    STATUS_FILE : str
    all_schema : dict 

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_dir : Path
    scaler_path : Path
    model_feature_path : Path
    transformed_data : Path
    preprocessed_dir : Path

#config_entity.py under entity
# data ingestion related config/entity
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True) #to prevent accidental modifictaion and setting custom datatype of entity
class PrepareBaseModelConfig:
    #config.yaml datatype
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str 
    params_classes: int
    #params.yaml datatype
    #ignoring some parameters as initializing some which are needed
    #in prepare_base_model function
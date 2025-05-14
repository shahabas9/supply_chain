from src.entity.config_entity import dataingestion_config,DataValidationConfig,DataTransformationConfig
from src.constants import *
from src.utils.common import read_yaml,create_directories
print(config_file_path,"hi")

class ConfiguarationManager:
    def __init__(
        self,
        config_file = config_file_path,
    
        schema_file = schema_file_path,
        params_file = params_file_path):

        self.config = read_yaml(config_file)
        self.schema = read_yaml(schema_file)
        self.params = read_yaml(params_file)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->dataingestion_config:
        config = self.config.data_ingestion
        print(f"{config}hi")
        create_directories([config.root_dir])

        data_ingestion_config = dataingestion_config(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            STATUS_FILE = config.STATUS_FILE,
            all_schema = schema
        )
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_dir = config.data_dir,
            scaler_path = config.scaler_path,
            model_feature_path = config.model_feature_path,
            transformed_data = config.transformed_data,
            preprocessed_dir = config.preprocessed_dir
        )
        return data_transformation_config
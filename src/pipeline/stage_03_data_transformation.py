from src.config.configuration import ConfiguarationManager
from src.components.data_transformation import DataTransformation
from src import logger
from pathlib import Path


STAGE_NAME = " Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfiguarationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.preprocess_data()
                data_transformation.one_hot_preprocess()
                data_transformation.train_test_spliting()
            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)

if __name__ =="__main__":
    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
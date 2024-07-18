from cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
#tagnine - ai auto completion tool
# logger.info("Welcome to my custom log")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<<<<<<<<<stage {STAGE_NAME} completed<<<<<<\n\nx===========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<<<<<<<<<stage {STAGE_NAME} completed<<<<<<\n\nx===========x")

except Exception as e:
    logger.exception(e)
    raise e

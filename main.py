from cnn_classifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnn_classifier.pipeline.stage_04_evaluation import EvaluationPipeline
from src.cnn_classifier.get_logger import logger
from src.cnn_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnn_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=====x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Prepare Base Model'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=====x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "TRAINING"

try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        data_ingestion = ModelTrainingPipeline()

        data_ingestion.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "EVALUATION"

try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        data_ingestion = EvaluationPipeline()

        data_ingestion.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

except Exception as e:
    logger.exception(e)
    raise e
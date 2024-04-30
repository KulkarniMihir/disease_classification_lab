from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.components.prepare_base_model import PrepareBaseModel
from cnn_classifier.get_logger import logger


STAGE_NAME = 'Prepare Base Model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self): 
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        data_ingestion = PrepareBaseModel(config=prepare_base_model_config)
        data_ingestion.get_base_model()
        data_ingestion.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=====x')
    except Exception as e:
        logger.exception(e)
        raise e    
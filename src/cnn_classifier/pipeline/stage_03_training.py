from cnn_classifier.get_logger import logger
from cnn_classifier.components.prepare_callbacks import PrepareCallback
from cnn_classifier.components.training import Training
from cnn_classifier.entity.config_entity import *
from cnn_classifier.config.configuration import *
from cnn_classifier.components.prepare_base_model import *

STAGE_NAME = "TRAINING"

class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()


        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )



if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        obj = ModelTrainingPipeline()

        obj.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

    except Exception as e:
        logger.exception(e)
        raise e
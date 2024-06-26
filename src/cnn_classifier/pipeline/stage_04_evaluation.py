from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.components.evaluation import Evaluation
from cnn_classifier.get_logger import logger

STAGE_NAME = "EVALUATION"

class EvaluationPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        obj = EvaluationPipeline()

        obj.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

    except Exception as e:
        logger.exception(e)
        raise e
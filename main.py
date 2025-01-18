from mlProject.Logging import logger
from mlProject.pipeline.stage_01_data_ingesion import DataIngesionTrainingPipeline


stage_name="Data Ingesion stage"
try:
    logger.info(f">>>>>stage {stage_name} startrd <<<<<")
    obj=DataIngesionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {stage_name} compleated <<<<<\n\nx=========")
except Exception as e:
    logger.exception(e)
    raise e

from mlProject.components.data_ingesion import DataIngestion
from mlProject.config.configuration import ConfigurationManager
from mlProject.Logging import logger

stage_name="Data Ingesion stage"
class DataIngesionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    
if __name__=='__main__':
    try:
        logger.info(f">>>>>stage {stage_name} startrd <<<<<")
        obj=DataIngesionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {stage_name} compleated <<<<<\n\nx=========")
    except Exception as e:
        logger.exception(e)
        raise e

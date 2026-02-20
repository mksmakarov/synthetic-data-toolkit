import os
import logging
import pandas as pd
import io

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BatchConcatenator:
    def concateate(self, path: str = 'generated'):
        batches: list = os.listdir(path)
        df = pd.concat([self.__to_csv(self.__read(os.path.join(path, batch))) for batch in batches])
        return df
    
    def __read(self, path: str):
        with open(path, 'r', errors='ignore', encoding='utf-8') as f:
            dataset = f.readlines()
        return self.__preprocess(dataset)
    
    def __preprocess(self, dataset: list):
        '''
        Each batch has:
        - first line: ```csv
        - second line: 'raw,target\n'
        - last line: ```

        This function removes the first and last lines.
        Rename columns to have strict comma delimiter.
        '''
        return "".join(dataset[1:len(dataset)-1])
    
    def __to_csv(self, dataset: str) -> pd.DataFrame:
        buffer = io.StringIO(dataset)
        
        df = pd.DataFrame()
        try:
            df = pd.read_csv(buffer, sep=",")
        except Exception as e:
            logging.error("Error reading CSV: %s", e)  

        return df         

if __name__ == "__main__":
    concatenator = BatchConcatenator()
    df = concatenator.concateate()
    df.to_csv('synthetic_data.csv', index=False)
    logging.info("All batches concatenated and saved to synthetic_data.csv")
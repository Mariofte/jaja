import pandas as pd 
import gspread as gs 
from oauth2client.service_account import ServiceAccountCredentials as sac
from streamlit import *

class API:
    def __init__(self, id:str, sheet:int):
        self.id = id
        self.sheet = sheet
        self.creds = sac.from_json_keyfile_name(
            filename='lib\service\Google\Token.json',
            scopes=[
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
        )
        
    def get(self,scout:str):
        try:
            
            client = gs.authorize(self.creds)
            work = client.open_by_key(self.id).get_worksheet(self.sheet)
            
            data = work.get_all_records()
            df = pd.DataFrame(data)
            
            with expander(scout):
                dataframe(df)
        
        except Exception as e:
            with expander("Error"):
                error(f"Hubo un error desconocido: {e}")
                info("Informar a Mario")

        
        except gs.exceptions.APIError as API:
            with expander("Error"):
                error(f"Hubo un error en el API : {API}")
                info("Informar a Mario")
            
        except FileNotFoundError as token:
            with expander("Error"):
                error(f"Token no encontrado o autorizado: {token}")
                info("Informar a Mario")
            
        except ModuleNotFoundError as modulo:
            with expander("Error"):
                error(f"Hubo un error en los requerimientos : {modulo}")
                info("Informar a Mario")
            
    def get_crude(self):
        try:
            
            client = gs.authorize(self.creds)
            work = client.open_by_key(self.id).get_worksheet(self.sheet)
            
            data = work.get_all_records()
            
            return data
        
        except Exception as e:
            with expander("Error"):
                error(f"Hubo un error desconocido: {e}")
                info("Informar a Mario")

        
        except gs.exceptions.APIError as API:
            with expander("Error"):
                error(f"Hubo un error en el API : {API}")
                info("Informar a Mario")
            
        except FileNotFoundError as token:
            with expander("Error"):
                error(f"Token no encontrado o autorizado: {token}")
                info("Informar a Mario")
            
        except ModuleNotFoundError as modulo:
            with expander("Error"):
                error(f"Hubo un error en los requerimientos : {modulo}")
                info("Informar a Mario")
            
    def post(self, data:list):
        try:
            
            client = gs.authorize(self.creds)
            work = client.open_by_key(self.id).get_worksheet(self.sheet)

            if button("Ingresar"):
                work.insert_rows(data,2)
                success("Se ingresaron los datos")
        
        except Exception as e:
            with expander("Error"):
                error(f"Hubo un error desconocido: {e}")
                info("Informar a Mario")

        
        except gs.exceptions.APIError as API:
            with expander("Error"):
                error(f"Hubo un error en el API : {API}")
                info("Informar a Mario")
            
        except FileNotFoundError as token:
            with expander("Error"):
                error(f"Token no encontrado o autorizado: {token}")
                info("Informar a Mario")
            
        except ModuleNotFoundError as modulo:
            with expander("Error"):
                error(f"Hubo un error en los requerimientos : {modulo}")
                info("Informar a Mario")
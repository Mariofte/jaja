import pandas as pd 
import streamlit as st 
import gspread as gs 
from oauth2client.service_account import ServiceAccountCredentials as sac

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
        
    def get(self):
        try:
            
            client = gs.authorize(self.creds)
            work = client.open_by_key(self.id).get_worksheet(self.sheet)
            
            data = work.get_all_records()
            df = pd.DataFrame(data)
            
            return df 
        
        except Exception as e:
            st.error(f"Hubo un error desconocido: {e}")
            st.info("Informar a Mario")

        
        except gs.exceptions.APIError as API:
            st.error(f"Hubo un error en el API : {API}")
            st.info("Informar a Mario")
            
        except FileNotFoundError as token:
            st.error(f"Token no encontrado o autorizado: {token}")
            st.info("Informar a Mario")
            
        except ModuleNotFoundError as modulo:
            st.error(f"Hubo un error en los requerimientos : {modulo}")
            st.info("Informar a Mario")
            
    def get_crude(self):
        try:
            
            client = gs.authorize(self.creds)
            work = client.open_by_key(self.id).get_worksheet(self.sheet)
            
            data = work.get_all_records()
            
            return data
        
        except Exception as e:
            st.error(f"Hubo un error desconocido: {e}")
            st.info("Informar a Mario")

        
        except gs.exceptions.APIError as API:
            st.error(f"Hubo un error en el API : {API}")
            st.info("Informar a Mario")
            
        except FileNotFoundError as token:
            st.error(f"Token no encontrado o autorizado: {token}")
            st.info("Informar a Mario")
            
        except ModuleNotFoundError as modulo:
            st.error(f"Hubo un error en los requerimientos : {modulo}")
            st.info("Informar a Mario")
            
    def post(self, data:list):
        try:
            
            client = gs.authorize(self.creds)
            work = client.open_by_key(self.id).get_worksheet(self.sheet)
            
            work.insert_rows(data,2)
        
        except Exception as e:
            st.error(f"Hubo un error desconocido: {e}")
            st.info("Informar a Mario")

        
        except gs.exceptions.APIError as API:
            st.error(f"Hubo un error en el API : {API}")
            st.info("Informar a Mario")
            
        except FileNotFoundError as token:
            st.error(f"Token no encontrado o autorizado: {token}")
            st.info("Informar a Mario")
            
        except ModuleNotFoundError as modulo:
            st.error(f"Hubo un error en los requerimientos : {modulo}")
            st.info("Informar a Mario")
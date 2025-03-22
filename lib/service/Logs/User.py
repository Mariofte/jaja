import streamlit as st 
import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
from streamlit_authenticator.utilities import *
from pathlib import Path

class user:
    def __init__(self):
        self.file_path = Path(__file__).parent / 'config.yaml'
        
    def log_in(self):
        try:
            
            with self.file_path.open('r',encoding='utf-8') as file:
                config = yaml.load(file, SafeLoader)
                
            authenticator = stauth.Authenticate(
                credentials = config['credentials'],
                cookie_name = config['cookie']['name'],
                cookie_key = config['cookie']['key'],
                cookie_expiry_days = config['cookie']['expiry_days'],
                validator = config['pre-authorized']['emails'],
                auto_hash = True,
                api_key = config['api_key']
            )
            
            with st.expander("Log in"):
                authenticator.login(key='Login', location='main', captcha=False)
            
            with self.file_path.open('w', encoding='utf-8') as file:
                config = yaml.dump(config, file, default_flow_style = False, allow_unicode=True)
            
        
        except Exception as e:
            with st.expander("Error"):
                st.error(f"Hubo un error desconocido : {e}")
                st.info("Informar a Mario")

        except LoginError as le:
            with st.expander("Error"):
                st.error(f"Hubo un error al intentar iniciar sesión : {le}")
                st.info("Informar a Mario")
            
    def log_out(self):
        try:
            
            with self.file_path.open('r', encoding='utf-8') as file:
                config = yaml.load(file, Loader=SafeLoader)
                
            authenticator = stauth.Authenticate(
                credentials = config['credentials'],
                cookie_name = config['cookie']['name'],
                cookie_key = config['cookie']['key'],
                cookie_expiry_days = config['cookie']['expiry_days'],
                validator = config['pre-authorized']['emails']
            )
            
            authenticator.logout(key='Logout', location='sidebar')
            
            with self.file_path.open('w', encoding='utf-8') as file:
                config = yaml.dump(config, file, default_flow_style = False, allow_unicode=True)
            
        except Exception as e:
            with st.expander("Error"):
                st.error(f"Hubo un error desconocido : {e}")
                st.info("Informar a Mario")

        except LogoutError as le:
            with st.expander("Error"):
                st.error(f"Hubo un error al intentar salir de la sesión : {le}")
                st.info("Informar a Mario")
            
    def creat_user(self):
        try:
            
            with self.file_path.open('r', encoding='utf-8') as file:
                config = yaml.load(file, Loader=SafeLoader)
                
            authenticator = stauth.Authenticate(
                credentials = config['credentials'],
                cookie_name = config['cookie']['name'],
                cookie_key = config['cookie']['key'],
                cookie_expiry_days = config['cookie']['expiry_days'],
                validator = config['pre-authorized']['emails'],
                auto_hash = True,
                api_key = config['api_key']
            )
            
            with st.expander("Crear usuario"):
                authenticator.register_user(location="main", captcha=False)
        
        except Exception as e:
            with st.expander("Error"):
                st.error(f"Hubo un error desconocido : {e}")
                st.info("Informar a Mario")

        except LoginError as le:
            with st.expander("Error"):
                st.error(f"Hubo un error al intentar iniciar sesión : {le}")
                st.info("Informar a Mario")
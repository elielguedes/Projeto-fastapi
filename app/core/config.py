from fastapi import Depends , HTTPException
from dotenv import load_dotenv
from .security import oauth2_schemas
from app.database import pegar_sessao
from jose import jwt , JWTError
from app.models.user import User
from sqlalchemy.orm import Session
import os

load_dotenv()

SECRET_KEY = str =  os.getenv("SECRET_KEY")
ALGORITHM = str = os.getenv("ALGORITHM")
ACCESS_TOKEN_MUNUTE = int(os.getenv("ACCESS_TOKEN_MUNUTE" , 30))


def verificar_token(token: str = Depends(oauth2_schemas), session: Session = Depends(pegar_sessao)):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithm = [ALGORITHM])
        id_usuario = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code = 401 , detail = "Acesso Negado verifique o token")
    usuario = session.query(User).filter(User.id == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code = 401 , detail = "Acesso invalido")
    return usuario
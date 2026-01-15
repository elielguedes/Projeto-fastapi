from fastapi import Depends , HTTPException
from .security import oauth2_schemas
from dotenv import load_dotenv
from app.database import pegar_sessao
from jose import jwt , JWTError
from app.models.user import User
from sqlalchemy.orm import Session
import os

load_dotenv()

SECRET_KEY = str =  os.getenv("SECRET_KEY")
ALGORITHM = str = os.getenv("ALGORITHM")
ACCESS_TOKEN_MUNUTE = int(os.getenv("ACCESS_TOKEN_MUNUTE" , 30))


def verificar_token(token: str = Depends(oauth2_schemas),session: Session = Depends(pegar_sessao)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Token inválido")
        user_id = int(user_id)
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Acesso negado")
    usuario = session.query(User).filter(User.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return usuario
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..core.security import bcrypt_context
from ..models.user import User
from sqlalchemy.orm import Session
from datetime import datetime ,  timedelta , timezone
from ..core.config import SECRET_KEY , ACCESS_TOKEN_MUNUTE , ALGORITHM
from jose import jwt

def autenticar_user(senha , email , session: Session):
    usuario = session.query(User).filter(User.email == email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha , usuario.senha):
        return False
    return usuario


def criar_token_service(id_usuario , duracao_token: timedelta = timedelta(minutes = ACCESS_TOKEN_MUNUTE)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    payload = {"sub": str(id_usuario) , "exp": data_expiracao}
    jwt_codificado = jwt.encode(payload, SECRET_KEY , algorithm = ALGORITHM)
    return jwt_codificado
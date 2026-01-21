from fastapi  import HTTPException , Depends
from ..models.user import User
from sqlalchemy.orm import Session
from ..core.config import pegar_sessao
from ..schemas.user import UserCreate
from ..core.security import bcrypt_context
from fastapi.security import OAuth2PasswordRequestForm

# ----- Função que criar Usuario e verifica se e-mail é ecistente -----
def create_user_service(session: Session, data = UserCreate):
    usuario = session.query(User).filter(User.email == data.email).first()
    if usuario:
        raise HTTPException(status_code = 400 , detail = "E-mail já cadastrado")
    senha_criptografada = bcrypt_context.hash(data.senha)

    novo_usuario = User(name = data.name ,email = data.email ,senha = senha_criptografada, perfil = False)
    session.add(novo_usuario)
    session.commit()


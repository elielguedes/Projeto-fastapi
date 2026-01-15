from fastapi import APIRouter , Depends , HTTPException
from app.database import pegar_sessao
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import user , loguinSchemas
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import bcrypt_context
from app.core.config import verificar_token , SECRET_KEY , ALGORITHM , ACCESS_TOKEN_MUNUTE
from datetime import timedelta , datetime , timezone
from jose import jwt 

auth = APIRouter(prefix="/auth" , tags=['auth'])

def criar_token(id_usuario , duracao_token: timedelta = timedelta(minutes = ACCESS_TOKEN_MUNUTE)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    payload = {"sub": str(id_usuario) , "exp": data_expiracao}
    jwt_codificado = jwt.encode(payload, SECRET_KEY , algorithm = ALGORITHM)
    return jwt_codificado

def autenticar(email , senha , session: Session = Depends(pegar_sessao)):
    usuario = session.query(User).filter(User.email == email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha , usuario.senha):
        return False
    return usuario


@auth.post("/create_user")
async def create_user(user_schemas: user, session: Session = Depends(pegar_sessao)):
    usuario = session.query(User).filter(User.email == user_schemas.email).first()
    if usuario:
        raise HTTPException(status_code = 400 , detail = "Usuario não cadastrou")
    senha_criptografada = bcrypt_context.hash(user_schemas.senha)
    novo_usuario = User(name = user_schemas.name ,email = user_schemas.email ,senha = senha_criptografada, perfil = False)
    session.add(novo_usuario)
    session.commit()
    return {"mensagem":f"E-mail cadastrado com sucesso {user_schemas.email}"}

@auth.post("/Loguin")
async def loguin(user_schemas: loguinSchemas , session: Session = Depends(pegar_sessao)):
    usuario = session.query(User).filter(User.email == user_schemas.email).first()
    if not usuario:
        raise HTTPException(status_code = 401 , detail = "Usuario não encontrado")
    access_token = criar_token(usuario.id)
    refresh_token = criar_token(usuario.id)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
@auth.post("/loguin-form")
async def loguin_form(dados_formulario: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(pegar_sessao)):
    usuario = autenticar(dados_formulario.username , dados_formulario.password , session)
    if not usuario:
        raise HTTPException(status_code = 401 , detail = "Usuario não encontrado")
    access_token = criar_token(usuario.id)
    return {"access_token": access_token}

@auth.get("/refresh")
async def refresh(usuario: User = Depends(verificar_token)):
    access_token = criar_token(usuario.id)
    return {"access_token": access_token, "token_type": "Bearer"}


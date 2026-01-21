from fastapi import APIRouter , Depends , HTTPException
from ..database import pegar_sessao
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate , UserResponse , MensagemResponse
from ..schemas.loguin import LoguinResponse , LoguinCreate
from fastapi.security import OAuth2PasswordRequestForm
from ..core.config import verificar_token
from ..services.auth_service import create_user_service
from ..services.loguinservice import autenticar_user , criar_token_service

auth = APIRouter(prefix="/auth" , tags=['auth'])

@auth.post("/create_user", response_model = MensagemResponse)
async def create_user(data: UserCreate, session: Session = Depends(pegar_sessao)):
    create_user_service(session , data)
    return {"Mensagem": f"E-mail {data.email} cadastrado com sucesso !"}

@auth.post("/Loguin", response_model = LoguinResponse)
async def loguin(user_schemas: LoguinCreate , session: Session = Depends(pegar_sessao)):
    usuario = session.query(User).filter(User.email == user_schemas.email).first()
    if not usuario:
        raise HTTPException(status_code = 401 , detail = "Usuario não encontrado")
    access_token = criar_token_service(usuario.id)
    refresh_token = criar_token_service(usuario.id)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

@auth.post("/loguin-form")
async def loguin_form(dados_formulario: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(pegar_sessao)):
    usuario = autenticar_user(dados_formulario.password , dados_formulario.username , session)
    if not usuario:
        raise HTTPException(status_code = 401 , detail = "Usuario não encontrado")
    access_token = criar_token_service(usuario.id)
    return {"access_token": access_token}

@auth.get("/refresh")
async def refresh(usuario: User = Depends(verificar_token)):
    access_token = criar_token_service(usuario.id)
    return {"access_token": access_token, "token_type": "Bearer"}


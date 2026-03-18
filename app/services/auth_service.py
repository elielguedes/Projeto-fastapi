from fastapi  import HTTPException , Depends
from ..models.user import User
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate
from ..core.security import bcrypt_context
from ..repositoryes.auth import UserRepository

# ----- objeto que criar Usuario e verifica se e-mail é existente -----
class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def create_auth(self ,data: UserCreate):
        user = self.repository.get_by_email(data.email)
        if user:
            raise HTTPException(status_code = 401 ,detail = "User not autheticator")
        senha_criptografada = bcrypt_context.hash(data.senha)
        novo_user = User(name = data.name, email = data.email , senha = senha_criptografada , perfil = False)
        self.repository.create(novo_user)
        return {"Mensagem": "User create sucess !"}

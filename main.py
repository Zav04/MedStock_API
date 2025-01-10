from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from REQUESTS_MedStock.LOGIN.POST_Login import router as POST_login_router
from REQUESTS_MedStock.RESET_PASSWORD.POST_Reset_Password import router as POST_reset_password_router
from REQUESTS_MedStock.UTILIZADOR.POST_Utilizador import router as POST_utilizador_router
from REQUESTS_MedStock.UTILIZADOR.GET_Utilizador import router as GET_utilizador_router
from REQUESTS_MedStock.UTILIZADOR.PUT_Utilizador import router as PUT_utilizador_router
from REQUESTS_MedStock.ROLES.GET_Roles import router as GET_roles_router
from REQUESTS_MedStock.CONSUMIVEIS.GET_Consumiveis import router as GET_Consumiveis_router
from REQUESTS_MedStock.CONSUMIVEIS.PUT_Consumiveis import router as PUT_Consumiveis_router
from REQUESTS_MedStock.CONSUMIVEIS.POST_Consumiveis import router as POST_Consumiveis_router
from REQUESTS_MedStock.REQUERIMENTO.GET_REQUERIMENTO import router as GET_requerimento_router
from REQUESTS_MedStock.LOGIN.GET_Login import router as GET_login_router
from REQUESTS_MedStock.SETORES.GET_Setor import router as GET_setor_router
from REQUESTS_MedStock.SETORES.POST_Setor import router as POST_setor_router
from REQUESTS_MedStock.REQUERIMENTO.POST_REQUERIMENTO import router as POST_requerimento_router
from REQUEST_MedReader.LOGIN.POST_Login import router as POST_login_router_MedReader
from REQUEST_MedReader.REQUERIMENTO.GET_REQUERIMENTO import router as GET_requerimento_router_MedReader
from REQUEST_MedReader.REQUERIMENTO.PUT_REQUERIMENTO import router as PUT_requerimento_router_MedReader
from REQUESTS_MedStock.REQUERIMENTO.PUT_REQUERIMENTO import router as PUT_requerimento_router
from REQUESTS_MedStock.REALOCACOES.GET_Realocacoes import router as GET_realocacoes_router


from REQUEST_MedOcurrencias.LOGIN.POST_Login import router as POST_login_router_MedOcurrencias
from REQUEST_MedOcurrencias.REQUERIMENTO.POST_Requerimento import router as GET_requerimento_router_MedOcurrencias


api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(POST_login_router)
api.include_router(POST_reset_password_router)
api.include_router(POST_utilizador_router)
api.include_router(GET_utilizador_router)
api.include_router(PUT_utilizador_router)
api.include_router(GET_roles_router)
api.include_router(GET_Consumiveis_router)
api.include_router(PUT_Consumiveis_router)
api.include_router(POST_Consumiveis_router)
api.include_router(GET_requerimento_router)
api.include_router(POST_requerimento_router)
api.include_router(GET_login_router)
api.include_router(GET_setor_router)
api.include_router(POST_setor_router)
api.include_router(PUT_requerimento_router)
api.include_router(GET_realocacoes_router)



api.include_router(POST_login_router_MedOcurrencias)
api.include_router(GET_requerimento_router_MedOcurrencias)

api.include_router(POST_login_router_MedReader)
api.include_router(GET_requerimento_router_MedReader)
api.include_router(PUT_requerimento_router_MedReader)

# if __name__ == "__main__":
#     #uvicorn.run("main:api", reload=True)
#     uvicorn.run("main:api", host="localhost", port=8888, reload=True)

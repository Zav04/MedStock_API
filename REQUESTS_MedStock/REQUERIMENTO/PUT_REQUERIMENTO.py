from fastapi import APIRouter, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from dependencies import get_db_MEDSTOCK
from Models.C_Update_Requerimento import C_Update_Requerimento
from Models.C_RequerimentoRequest import C_RequerimentoRequest
import json

router = APIRouter()


@router.put("/MedStock_CancelRequerimento/")
async def MedStock_CancelRequerimento(requerimento: C_Update_Requerimento, db=Depends(get_db_MEDSTOCK)):
    try:

        query = text("""
            SELECT update_requerimento_cancel(:p_requerimento_id);
        """)

        result = db.execute(query, {
            "p_requerimento_id": requerimento.requerimento_id,
        })

        success = result.scalar()

        if success:
            db.commit()
            return {
                "response": True,
                "data": "Requerimento Cancelado."
            }
        else:
            db.rollback()
            return {
                "response": False,
                "error": "Erro ao cancelar o requerimento."
            }

    except SQLAlchemyError as e:
        db.rollback()
        error_msg = str(e.__dict__['orig']).split('\n')[0]
        return {
            "response": False,
            "error": error_msg
        }

    except Exception as e:
        db.rollback()
        error_messages = [str(arg) for arg in e.args]
        return {
            "response": False,
            "error": error_messages
        }
        
@router.put("/MedStock_RejectRequerimento/")
async def MedStock_RejectRequerimento(requerimento: C_Update_Requerimento, db=Depends(get_db_MEDSTOCK)):
    try:

        query = text("""
            SELECT update_requerimento_reject(:p_requerimento_id, :p_user_id);
        """)

        result = db.execute(query, {
            "p_requerimento_id": requerimento.requerimento_id,
            "p_user_id": requerimento.user_id
        })

        success = result.scalar()

        if success:
            db.commit()
            return {
                "response": True,
                "data": "Requerimento Recusado."
            }
        else:
            db.rollback()
            return {
                "response": False,
                "error": "Erro ao recusar o requerimento."
            }

    except SQLAlchemyError as e:
        db.rollback()
        error_msg = str(e.__dict__['orig']).split('\n')[0]
        return {
            "response": False,
            "error": error_msg
        }

    except Exception as e:
        db.rollback()
        error_messages = [str(arg) for arg in e.args]
        return {
            "response": False,
            "error": error_messages
        }


@router.put("/MedStock_AcceptRequerimento/")
async def MedStock_AcceptRequerimento(requerimento: C_Update_Requerimento, db=Depends(get_db_MEDSTOCK)):
    try:

        query = text("""
            SELECT update_requerimento_accept(:p_requerimento_id,:p_user_id);
        """)

        result = db.execute(query, {
            "p_requerimento_id": requerimento.requerimento_id,
            "p_user_id": requerimento.user_id
        })

        success = result.scalar()

        if success:
            db.commit()
            return {
                "response": True,
                "data": "Requerimento Aceite."
            }
        else:
            db.rollback()
            return {
                "response": False,
                "error": "Erro ao aceitar o requerimento."
            }

    except SQLAlchemyError as e:
        db.rollback()
        error_msg = str(e.__dict__['orig']).split('\n')[0]
        return {
            "response": False,
            "error": error_msg
        }

    except Exception as e:
        db.rollback()
        error_messages = [str(arg) for arg in e.args]
        return {
            "response": False,
            "error": error_messages
        }
        
        


@router.put("/MedStock_StandByRequerimento/")
async def MedStock_StandByRequerimento(requerimento: C_RequerimentoRequest, db=Depends(get_db_MEDSTOCK)):
    try:

        query = text("""
            SELECT update_requerimento_standby(:p_requerimento_id);
        """)

        result = db.execute(query, {
            "p_requerimento_id": requerimento.requerimento_id,
        })

        success = result.scalar()

        if success:
            db.commit()
            return {
                "response": True,
                "data": "Requerimento Colocado em Stand-By."
            }
        else:
            db.rollback()
            return {
                "response": False,
                "error": "Erro ao colocar o requerimento em Stand-By."
            }

    except SQLAlchemyError as e:
        db.rollback()
        error_msg = str(e.__dict__['orig']).split('\n')[0]
        return {
            "response": False,
            "error": error_msg
        }

    except Exception as e:
        db.rollback()
        error_messages = [str(arg) for arg in e.args]
        return {
            "response": False,
            "error": error_messages
        }
        
        
@router.put("/MedStock_ResumeRequerimento/")
async def MedStock_ResumeRequerimento(requerimento: C_RequerimentoRequest, db=Depends(get_db_MEDSTOCK)):
    try:

        query = text("""
            SELECT update_requerimento_resume(:p_requerimento_id);
        """)

        result = db.execute(query, {
            "p_requerimento_id": requerimento.requerimento_id,
        })

        success = result.scalar()

        if success:
            db.commit()
            return {
                "response": True,
                "data": "Requerimento Colocado na Lista de Espera."
            }
        else:
            db.rollback()
            return {
                "response": False,
                "error": "Erro ao colocar o requerimento na Lista de Espera."
            }

    except SQLAlchemyError as e:
        db.rollback()
        error_msg = str(e.__dict__['orig']).split('\n')[0]
        return {
            "response": False,
            "error": error_msg
        }

    except Exception as e:
        db.rollback()
        error_messages = [str(arg) for arg in e.args]
        return {
            "response": False,
            "error": error_messages
        }
        
@router.put("/MedStock_PrepareRequerimento/")
async def MedStock_PrepareRequerimento(requerimento: C_RequerimentoRequest, db=Depends(get_db_MEDSTOCK)):
    try:

        query = text("""
            SELECT update_requerimento_preparation(:p_requerimento_id);
        """)

        result = db.execute(query, {
            "p_requerimento_id": requerimento.requerimento_id,
        })

        success = result.scalar()

        if success:
            db.commit()
            return {
                "response": True,
                "data": "Requerimento Colocado em Stand-By."
            }
        else:
            db.rollback()
            return {
                "response": False,
                "error": "Erro ao colocar o requerimento em Stand-By."
            }

    except SQLAlchemyError as e:
        db.rollback()
        error_msg = str(e.__dict__['orig']).split('\n')[0]
        return {
            "response": False,
            "error": error_msg
        }

    except Exception as e:
        db.rollback()
        error_messages = [str(arg) for arg in e.args]
        return {
            "response": False,
            "error": error_messages
        }
        
@router.put("/MedStock_SendRequerimento/")
async def MedStock_SendRequerimento(requerimento: C_Update_Requerimento, db=Depends(get_db_MEDSTOCK)):
    try:

        query = text("""
            SELECT update_requerimento_send(:p_requerimento_id,:p_user_id);
        """)

        result = db.execute(query, {
            "p_requerimento_id": requerimento.requerimento_id,
            "p_user_id": requerimento.user_id
        })

        success = result.scalar()

        if success:
            db.commit()
            return {
                "response": True,
                "data": "Requerimento Aceite."
            }
        else:
            db.rollback()
            return {
                "response": False,
                "error": "Erro ao aceitar o requerimento."
            }

    except SQLAlchemyError as e:
        db.rollback()
        error_msg = str(e.__dict__['orig']).split('\n')[0]
        return {
            "response": False,
            "error": error_msg
        }

    except Exception as e:
        db.rollback()
        error_messages = [str(arg) for arg in e.args]
        return {
            "response": False,
            "error": error_messages
        }
        
        
        
        
from fastapi import APIRouter, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from dependencies import get_db_MEDSTOCK
from Models.C_CreatePedidoFornecedor import C_CreatePedidoFornecedor
import json

router = APIRouter()


@router.post("/MedStock_PedidoFornecedor/")
async def MedStock_PedidoFornecedor(pedido: C_CreatePedidoFornecedor, db=Depends(get_db_MEDSTOCK)):
    try:
        consumiveis_json = json.dumps([consumivel.model_dump() for consumivel in pedido.consumiveis or []])

        query = text("""
            SELECT create_pedido_fornecedor(:pedido_id_input, :fornecedor_nome_input, :consumiveis_input);
        """)

        result = db.execute(query, {
            "pedido_id_input": pedido.pedido_id,
            "fornecedor_nome_input": pedido.fornecedor_nome,
            "consumiveis_input": consumiveis_json
        }).scalar()
        

        if result:
            db.commit()
            return {
                "response": True,
                "data": f"Pedido {pedido.pedido_id} criado com sucesso."
            }
        else:
            db.rollback()
            return {
                "response": False,
                "error": f"Falha ao registar o pedido {pedido.fornecedor_nome}."
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
        return {
            "response": False,
            "error": str(e)
        }
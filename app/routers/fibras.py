from fastapi import APIRouter, HTTPException
from domain.models import FibraPrecio
from infra.services.fibra_prices import FibraNoEncontrada
from usecases.get_fibra_price import get_fibra_price

router = APIRouter(
    prefix="/fibras",
    tags=["FIBRAs"]
)


@router.get("/funo", response_model=FibraPrecio)
async def get_funo_price():
    """
    Obtiene el precio más reciente de FUNO
    """
    try:
        return get_fibra_price('funo')
    except FibraNoEncontrada as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fmty", response_model=FibraPrecio)
async def get_fmty_price():
    """
    Obtiene el precio más reciente de FMTY
    """
    try:
        return get_fibra_price('fmty')
    except FibraNoEncontrada as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/danhos", response_model=FibraPrecio)
async def get_danhos_price():
    """
    Obtiene el precio más reciente de DANHOS
    """
    try:
        return get_fibra_price('danhos')
    except FibraNoEncontrada as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
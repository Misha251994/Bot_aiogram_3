from app.handlers.base_handlers import base_router
from app.handlers.registration_handler import register_router

router_list = [
    register_router,
    base_router,
]

__all__ = ["router_list"]

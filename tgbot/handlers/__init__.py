"""Import all routers and add them to routers_list."""
from .users.admin import admin_router
from .users.echo import echo_router
from .users.simple_menu import menu_router
from .users.user import user_router

routers_list = [
    admin_router,
    menu_router,
    user_router,
    echo_router,  # echo_router must be last
]

__all__ = [
    "routers_list",
]

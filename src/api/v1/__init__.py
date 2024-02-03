from fastapi import APIRouter

# Справочниковые контроллеры
from .role_controller import router as role_controller
from .permission_controller import router as permission_controller


from .email_controller import router as email_controller
from .invitation_controller import router as invitation_controller

from .user_controller import router as user_controller

from .login_controller import router as login_controller

from .meet_controller import router as meet_controller

router = APIRouter()

router.include_router(permission_controller)
router.include_router(role_controller)
router.include_router(user_controller)
router.include_router(email_controller)
router.include_router(invitation_controller)
router.include_router(login_controller)
router.include_router(meet_controller)

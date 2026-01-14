from bot.core.config import settings


def is_admin(user_id: int) -> bool:
    raw_ids = [value.strip() for value in settings.admin_ids.split(",") if value.strip()]
    admin_ids = {int(value) for value in raw_ids if value.isdigit()}
    return not admin_ids or user_id in admin_ids
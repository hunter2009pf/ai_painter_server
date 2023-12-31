from configs.config import settings


class PathUtil:
    @classmethod
    def get_image_saved_dir_path(cls) -> str:
        return settings.SERVICE.IMAGE_OUTPUT_DIR_PATH
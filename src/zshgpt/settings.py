from pathlib import Path
from typing import Optional, Tuple, Type

from pydantic import model_validator
from pydantic_settings import BaseSettings, JsonConfigSettingsSource, PydanticBaseSettingsSource

JSON_PATH: Path = Path('~/.zshgpt/config.json').expanduser()


class Settings(BaseSettings):
    model: str = 'gpt-3.5-turbo'
    assistant_name: str = 'ZSHGPT'
    assistant_id: Optional[str] = None
    thread_id: Optional[str] = None

    @model_validator(mode='after')
    def update_json(self) -> 'Settings':
        if not JSON_PATH.exists():
            JSON_PATH.parent.mkdir(parents=True, exist_ok=False)
        with open(JSON_PATH, 'w') as f:
            f.write(self.model_dump_json(indent=4))
        return self

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            JsonConfigSettingsSource(
                settings_cls=settings_cls,
                json_file=JSON_PATH,
            ),
            env_settings,
            dotenv_settings,
        )


settings = Settings()

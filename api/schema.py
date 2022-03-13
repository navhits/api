import typing
import pydantic

class Info(pydantic.BaseModel):
    personal: typing.Dict[str, typing.Union[str, int, list, dict]]
    social: typing.List[typing.Dict[str, typing.Union[str, int, list, dict]]]
    education: typing.Dict[str, typing.List[typing.Dict[str, typing.Union[str, int, list, dict]]]]
    work: typing.Dict[str, typing.List[typing.Dict[str, typing.Union[str, int, list, dict]]]]


class Storage(pydantic.BaseModel):
    url: str

class Drive(pydantic.BaseModel):
    url: str

class StorageError(pydantic.BaseModel):
    error: str

class DriveError(pydantic.BaseModel):
    error: str
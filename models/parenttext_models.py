from rpft.parsers.creation.datarowmodel import DataRowModel
from rpft.parsers.common.rowparser import ParserModel
from parenttext_pipeline.models.parenttext_models import *
from typing import List


# content delivery data models (Malaysia specific)
class Language(ParserModel):
    eng: str = ""
    zho: str = ""

class GoalDataModel(DataRowModel):
    priority_c: str = ""
    priority_p: str = ""
    relationship: List[str] = []
    name_c: Language = Language()


class ModuleDataModel(DataRowModel):
    topic_ID: str = ""
    priority_in_topic: str = ""
    age: List[int] = []
    child_gender: List[str] = []
    name_c: Language = Language()

class GoalTopicLinkModel(DataRowModel):
    goal_id_c: str = ""
    priority_in_goal_c: str = ""



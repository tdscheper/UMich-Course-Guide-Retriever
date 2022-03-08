"""Map ArgTypes to Arg classes."""
from args import _ArgType
#from args.meta_arg import MetaArg
from args.arg import Arg
from args.term import Term
from args.type import Type as Tipe
from args.keyword import Keyword
from args.instructor import Instructor
from args.show import Show
from args.course_level import CourseLevel
from args.subject import Subject
from args.credit_hours import CreditHours
from args.course import Course
from args.distribution_req import DistributionReq
from args.skills_req import SkillsReq
from args.special_offering import SpecialOffering
from args.meeting_day import MeetingDay
from args.meeting_time import MeetingTime
from args.instruction_mode import InstructionMode
from args.page_number import PageNumber
from args.department import Department
from args.catalog import Catalog
from args.other_req import OtherReq
from args.meeting_time_start import MeetingTimeStart
from args.meeting_time_end import MeetingTimeEnd
from typing import Dict, Type


ARGTYPE_TO_ARG: Dict[Type[_ArgType], Type[Arg]] = {
    _ArgType._TERM                    : Term            ,
    _ArgType._TYPE                    : Tipe            ,
    _ArgType._KEYWORD                 : Keyword         ,
    _ArgType._INSTRUCTOR              : Instructor      ,
    _ArgType._SHOW                    : Show            ,
    _ArgType._COURSE_LEVEL            : CourseLevel     ,
    _ArgType._SUBJECT                 : Subject         ,
    _ArgType._CREDIT_HOURS            : CreditHours     ,
    _ArgType._COURSE                  : Course          ,
    _ArgType._DISTRIBUTION_REQUIREMENT: DistributionReq ,
    _ArgType._SKILLS_REQUIREMENT      : SkillsReq       ,
    _ArgType._SPECIAL_OFFERING        : SpecialOffering ,
    _ArgType._MEETING_DAY             : MeetingDay      ,
    _ArgType._MEETING_TIME            : MeetingTime     ,
    _ArgType._INSTRUCTION_MODE        : InstructionMode ,
    _ArgType._PAGE_NUMBER             : PageNumber      ,
    _ArgType._DEPARTMENT              : Department      ,
    _ArgType._CATALOG                 : Catalog         ,
    _ArgType._OTHER_REQUIREMENT       : OtherReq        ,
    _ArgType._MEETING_TIME_START      : MeetingTimeStart,
    _ArgType._MEETING_TIME_END        : MeetingTimeEnd
}

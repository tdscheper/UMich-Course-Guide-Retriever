"""Args package initializer."""
from enum import Enum
from typing import List, Tuple, Set, Dict, Type


# [(key1, [val1, val2]), (key2, [val3])] => key1=val1+val2&key2=val3
# key1 and key2 can be the same, so we can't use dictionary
_RawInputValue = str
_InputKey      = str
_InputValue    = str
_InputValues   = List[_InputValue]
_QueryKey      = str
_QueryValue    = str
_QueryValues   = Tuple[_QueryValue, ...]
_QueryKVPair   = Tuple[_QueryKey, _QueryValues]
_QueryKVPairs  = Set[_QueryKVPair]


# Keys that can be used in a Course Guide Search
class _QueryKeyType(Enum):
    _TERM                     =  1
    _TYPE                     =  2
    _KEYWORD                  =  3
    _INSTRUCTOR               =  4
    _SHOW                     =  5
    _COURSE_LEVEL             =  6
    _DEPARTMENT               =  7
    _CREDIT_HOURS             =  8
    _CATALOG                  =  9
    _DISTRIBUTION_REQUIREMENT = 10
    _OTHER_REQUIREMENT        = 11
    _MEETING_DAY              = 12
    _MEETING_TIME_START       = 13
    _MEETING_TIME_END         = 14
    _INSTRUCTION_MODE         = 15
    _PAGE_NUMBER              = 16


_QUERY_KEY_TYPE_TO_QUERY_KEY: Dict[Type[_QueryKeyType], _QueryKey] = {
    _QueryKeyType._TERM                    : 'termArray'   ,
    _QueryKeyType._TYPE                    : 'cgtype'      ,
    _QueryKeyType._KEYWORD                 : 'keyword'     ,
    _QueryKeyType._INSTRUCTOR              : 'instr'       ,
    _QueryKeyType._SHOW                    : 'show'        ,
    _QueryKeyType._COURSE_LEVEL            : 'numlvl'      ,
    _QueryKeyType._DEPARTMENT              : 'department'  ,
    _QueryKeyType._CREDIT_HOURS            : 'credit'      ,
    _QueryKeyType._CATALOG                 : 'catalog'     ,
    _QueryKeyType._DISTRIBUTION_REQUIREMENT: 'dist'        ,
    _QueryKeyType._OTHER_REQUIREMENT       : 'reqs'        ,
    _QueryKeyType._MEETING_DAY             : 'mp_day'      ,
    _QueryKeyType._MEETING_TIME_START      : 'mp_starttime',
    _QueryKeyType._MEETING_TIME_END        : 'mp_endtime'  ,
    _QueryKeyType._INSTRUCTION_MODE        : 'instruction' ,
    _QueryKeyType._PAGE_NUMBER             : 'iPageNum'
}


# Arguments used to form a Course Guide search
class _ArgType(Enum):
    _TERM                     =  1
    _TYPE                     =  2
    _KEYWORD                  =  3
    _INSTRUCTOR               =  4
    _SHOW                     =  5
    _COURSE_LEVEL             =  6
    _SUBJECT                  =  7  # Department alias
    _CREDIT_HOURS             =  8
    _COURSE                   =  9  # Combo of Department and Catalog
    _DISTRIBUTION_REQUIREMENT = 10
    _SKILLS_REQUIREMENT       = 11  # OtherRequirement alias
    _SPECIAL_OFFERING         = 12  # OtherRequirement alias
    _MEETING_DAY              = 13
    _MEETING_TIME             = 14  # Combo of MeetingTimeStart, MeetingTimeEnd
    _INSTRUCTION_MODE         = 15
    _PAGE_NUMBER              = 16
                                     # ArgTypes below here are not stand-alone
    _DEPARTMENT               = 17
    _CATALOG                  = 18
    _OTHER_REQUIREMENT        = 19
    _MEETING_TIME_START       = 20
    _MEETING_TIME_END         = 21


_NUM_STANDALONE_ARGTYPES = 16


_ARG_TYPE_TO_QUERY_KEY: Dict[Type[_ArgType], _QueryKey] = {
    _ArgType._TERM                    : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._TERM]                    ,
    _ArgType._TYPE                    : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._TYPE]                    ,
    _ArgType._KEYWORD                 : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._KEYWORD]                 ,
    _ArgType._INSTRUCTOR              : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._INSTRUCTOR]              ,
    _ArgType._SHOW                    : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._SHOW]                    ,
    _ArgType._COURSE_LEVEL            : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._COURSE_LEVEL]            ,
    _ArgType._CREDIT_HOURS            : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._CREDIT_HOURS]            ,
    _ArgType._DISTRIBUTION_REQUIREMENT: \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._DISTRIBUTION_REQUIREMENT],
    _ArgType._MEETING_DAY             : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._MEETING_DAY]             ,
    _ArgType._INSTRUCTION_MODE        : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._INSTRUCTION_MODE]        ,
    _ArgType._PAGE_NUMBER             : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._PAGE_NUMBER]             ,
    _ArgType._DEPARTMENT              : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._DEPARTMENT]              ,
    _ArgType._CATALOG                 : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._CATALOG]                 ,
    _ArgType._OTHER_REQUIREMENT       : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._OTHER_REQUIREMENT]       ,
    _ArgType._MEETING_TIME_START      : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._MEETING_TIME_START]      ,
    _ArgType._MEETING_TIME_END        : \
        _QUERY_KEY_TYPE_TO_QUERY_KEY[_QueryKeyType._MEETING_TIME_END]
}


_INPUT_KEY_TO_ARG_TYPE: Dict[_InputKey, Type[_ArgType]] = {
    'Term'                     : _ArgType._TERM                    ,
    'Type'                     : _ArgType._TYPE                    ,
    'Keyword'                  : _ArgType._KEYWORD                 ,
    'Instructor'               : _ArgType._INSTRUCTOR              ,
    'Course Level'             : _ArgType._COURSE_LEVEL            ,
    'Subject'                  : _ArgType._SUBJECT                 ,
    'Credit Hours'             : _ArgType._CREDIT_HOURS            ,
    'Course'                   : _ArgType._COURSE                  ,
    'Distribution Requirements': _ArgType._DISTRIBUTION_REQUIREMENT,
    'Skills Requirements'      : _ArgType._SKILLS_REQUIREMENT      ,
    'Special Offerings'        : _ArgType._SPECIAL_OFFERING        ,
    'Meeting Days'             : _ArgType._MEETING_DAY             ,
    'Meeting Time'             : _ArgType._MEETING_TIME            ,
    'Instruction Modes'         : _ArgType._INSTRUCTION_MODE
}


_ARG_TYPE_TO_INPUT_KEY: Dict[Type[_ArgType], _InputKey] = {
    _ArgType._TERM                    : 'Term'                     ,
    _ArgType._TYPE                    : 'Type'                     ,
    _ArgType._KEYWORD                 : 'Keyword'                  ,
    _ArgType._INSTRUCTOR              : 'Instructor'               ,
    _ArgType._COURSE_LEVEL            : 'Course Level'             ,
    _ArgType._SUBJECT                 : 'Subject'                  ,
    _ArgType._CREDIT_HOURS            : 'Credit Hours'             ,
    _ArgType._COURSE                  : 'Course'                   ,
    _ArgType._DISTRIBUTION_REQUIREMENT: 'Distribution Requirements',
    _ArgType._SKILLS_REQUIREMENT      : 'Skills Requirements'      ,
    _ArgType._SPECIAL_OFFERING        : 'Special Offerings'        ,
    _ArgType._MEETING_DAY             : 'Meeting Days'             ,
    _ArgType._MEETING_TIME            : 'Meeting Time'             ,
    _ArgType._INSTRUCTION_MODE        : 'Instruction Mode'
}


_ARG_TYPE_TO_INPUT_VAL_TO_QUERY_VAL: \
    Dict[Type[_ArgType], Dict[_InputValue, _QueryValue]] = {
    _ArgType._TERM: {
        'Fall 2021'         : 'f_21_2360',
        'Winter 2022'       : 'w_22_2370',
        'Spring 2022'       : 'sp_22_2380',
        'Spring/Summer 2022': 'ss_22_2390',
        'Summer 2022'       : 'su_22_2400',
        'Fall 2022'         : 'f_22_2410'
    },
    _ArgType._TYPE: {
        'Undergraduate': 'ug'
    },
    _ArgType._COURSE_LEVEL: {
        '100' : '100', 
        '200' : '200',
        '300' : '300',
        '400' : '400',
        '500+': '500,600,700,800,900'
    },
    _ArgType._CREDIT_HOURS: {
        '1' : '1',
        '2' : '2',
        '3' : '3',
        '4' : '4',
        '5+': '5,6,7,8,9,10,11,12,13,14,15,16,17,18'
    },
    _ArgType._DISTRIBUTION_REQUIREMENT: {
        'CE' : 'CE' ,                 # Creative Expression
        'HU' : 'HU' ,                 # Humanities
        'ID' : 'ID' ,                 # Interdisciplinary
        'MSA': 'MSA',                 # Math and Symbolic Analysis
        'NS' : 'NS' ,                 # Natural Sciences
        'SS' : 'SS'                   # Social Sciences
    },
    _ArgType._SKILLS_REQUIREMENT: {
        'FYWR'    : 'IC'  ,           # First-Year Writing Requirement
        'ULWR'    : 'ULWR',           # Upper-Level Writing Requirement
        'RE'      : 'RE'  ,           # Race and Ethnicity
        'QR/1'    : 'QR/1',           # Quantitative Reasoning Full
        'QR/2'    : 'QR/2',           # Quantitative Reasoning Half
        'LANG_REQ': 'Lang_Req'        # Language Requirement
    },
    _ArgType._SPECIAL_OFFERING: {
        'BS'     : 'BS'            ,  # Bachelor of Science Eligibility
        'CBL'    : 'CBL'           ,  # Community-Based Learning
        'FYS'    : 'First_Year_Sem',  # First-Year Seminar
        'HNRS'   : 'HNRS'          ,  # Honors
        'MINI'   : 'MINI'          ,  # Minicourse
        'SUSTAIN': 'Sustain'       ,  # Sustainability
        'THEME'  : 'Theme_Sem'        # Theme Semester
    },
    _ArgType._MEETING_DAY: {
        'Monday'   : 'Mon'  ,
        'Tuesday'  : 'Tues' ,
        'Wednesday': 'Wed'  ,
        'Thursday' : 'Thurs',
        'Friday'   : 'Fri'  ,
        'Saturday' : 'Sat'  ,
        'Sunday'   : 'Sun'
    },
    _ArgType._INSTRUCTION_MODE: {
        'InPerson': 'InPerson',
        'Online'  : 'Online'  ,
        'Hybrid'  : 'Hybrid'
    }
}


_ARG_TYPE_TO_DEFAULT_INPUT_VALUE: Dict[Type[_ArgType], _InputValue] = {
    _ArgType._TERM       : 'Fall 2022'    ,
    _ArgType._TYPE       : 'Undergraduate',
    _ArgType._SHOW       : '250'          ,
    _ArgType._PAGE_NUMBER: '1'
}
